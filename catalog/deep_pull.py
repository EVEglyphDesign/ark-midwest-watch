#!/usr/bin/env python3
"""
ARK-CIVIC deep pull.

Stage 1 held the catalogue (what exists). This holds the contents (the data
itself), for everything that can lawfully and safely be pulled.

Every record ends in exactly one state, and every state is recorded:

  PULLED    contents mirrored into catalog/data/, gzipped
  SCHEMA    endpoint reachable, schema and row count held, contents not mirrored
            (over size cap, or no bulk query support)
  WITHHELD  reachable and deliberately not pulled - person-level screen
  BLOCKED   cannot be pulled; the reason is recorded verbatim and becomes a
            lock-in finding

BLOCKED is the important column. A wall that is named is a finding; a wall that
is silently skipped is a lie by omission.

PRIVACY: the person-level screen from ingest.py is authoritative and is applied
before any content request is made. A WITHHELD record is never fetched at all -
not fetched and discarded, never requested.
"""

import json, os, gzip, time, urllib.request, urllib.error, urllib.parse, datetime, socket
import concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
os.makedirs(DATA, exist_ok=True)
UA = "ARK-CIVIC/1.0 (+https://eveglyphdesign.github.io/ark-midwest-watch/) civic-condition record"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

MAX_FEATURES = 30000        # per layer; above this we hold schema + count only
MAX_BYTES = 30 * 1024 * 1024
TOTAL_BUDGET = 350 * 1024 * 1024
WORKERS = 8

state = {"bytes": 0}


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def jget(url, timeout=60):
    return json.loads(fetch(url, timeout))


def why(e):
    """Turn an exception into a plain reason a human can act on."""
    if isinstance(e, urllib.error.HTTPError):
        return f"HTTP {e.code} {e.reason}"
    if isinstance(e, urllib.error.URLError):
        r = getattr(e, "reason", e)
        if isinstance(r, socket.gaierror):
            return "DNS does not resolve - host does not exist"
        if isinstance(r, socket.timeout):
            return "timeout - endpoint did not respond"
        return f"unreachable - {r}"
    if isinstance(e, socket.timeout):
        return "timeout - endpoint did not respond"
    if isinstance(e, json.JSONDecodeError):
        return "endpoint returned non-JSON - not a machine-readable service"
    return f"{type(e).__name__}: {str(e)[:160]}"


def save(path, obj):
    full = os.path.join(DATA, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    raw = json.dumps(obj, separators=(",", ":")).encode()
    with gzip.open(full, "wb", compresslevel=9) as f:
        f.write(raw)
    n = os.path.getsize(full)
    state["bytes"] += n
    return n


# ------------------------------------------------------------------ ArcGIS
def pull_arcgis(rec):
    """A FeatureServer/MapServer: enumerate layers, hold schema, mirror rows."""
    base = (rec["access_url"] or rec["landing"]).split("?")[0].rstrip("/")
    out = {"id": rec["id"], "title": rec["title"], "source": rec["source"],
           "authority": rec["authority"], "endpoint": base, "layers": []}
    svc = jget(base + "?f=json", 60)
    layers = (svc.get("layers") or []) + (svc.get("tables") or [])
    if not layers:
        return "SCHEMA", "service exposes no layers or tables", out

    pulled_any = False
    for lyr in layers[:40]:
        lid = lyr.get("id")
        lurl = f"{base}/{lid}"
        entry = {"layer_id": lid, "name": lyr.get("name")}
        try:
            meta = jget(lurl + "?f=json", 45)
            entry["fields"] = [{"name": f.get("name"), "type": f.get("type"),
                                "alias": f.get("alias")} for f in (meta.get("fields") or [])]
            entry["geometry_type"] = meta.get("geometryType")
            entry["description"] = (meta.get("description") or "")[:400]
            entry["max_record_count"] = meta.get("maxRecordCount")
            try:
                c = jget(lurl + "/query?where=1%3D1&returnCountOnly=true&f=json", 45)
                entry["count"] = c.get("count")
            except Exception as e:
                entry["count"] = None
                entry["count_error"] = why(e)
        except Exception as e:
            entry["error"] = why(e)
            out["layers"].append(entry)
            continue

        cnt = entry.get("count")
        if cnt is None:
            entry["state"] = "SCHEMA"
            entry["reason"] = "endpoint refused a count query"
        elif cnt == 0:
            entry["state"] = "SCHEMA"
            entry["reason"] = "layer is empty"
        elif cnt > MAX_FEATURES:
            entry["state"] = "SCHEMA"
            entry["reason"] = f"{cnt:,} features exceeds the {MAX_FEATURES:,} mirror cap"
        elif state["bytes"] > TOTAL_BUDGET:
            entry["state"] = "SCHEMA"
            entry["reason"] = "repository size budget reached"
        else:
            try:
                q = (lurl + "/query?where=1%3D1&outFields=*&returnGeometry=true"
                            "&outSR=4326&f=geojson&resultRecordCount=" + str(MAX_FEATURES))
                blob = fetch(q, 180)
                if len(blob) > MAX_BYTES:
                    entry["state"] = "SCHEMA"
                    entry["reason"] = f"payload {len(blob)//1024//1024} MB exceeds per-file cap"
                else:
                    gj = json.loads(blob)
                    feats = gj.get("features", [])
                    if not feats and gj.get("error"):
                        entry["state"] = "BLOCKED"
                        entry["reason"] = "service error on query: " + str(gj["error"].get("message"))[:120]
                    else:
                        p = f"{rec['source'].replace(' ','_')}/{rec['id']}_{lid}.geojson.gz"
                        entry["bytes"] = save(p, gj)
                        entry["file"] = p
                        entry["features"] = len(feats)
                        entry["state"] = "PULLED"
                        pulled_any = True
            except Exception as e:
                entry["state"] = "BLOCKED"
                entry["reason"] = why(e)
        out["layers"].append(entry)

    return ("PULLED" if pulled_any else "SCHEMA"), "", out


# ------------------------------------------------------------------ Socrata
def pull_socrata(rec):
    base = rec["access_url"]
    out = {"id": rec["id"], "title": rec["title"], "source": rec["source"],
           "authority": rec["authority"], "endpoint": base, "layers": []}
    try:
        cnt = jget(base + "?$select=count(*)", 60)
        n = int(list(cnt[0].values())[0]) if cnt else 0
    except Exception as e:
        return "BLOCKED", why(e), out
    entry = {"name": rec["title"], "count": n}
    if n == 0:
        entry["state"], entry["reason"] = "SCHEMA", "dataset is empty"
    elif n > MAX_FEATURES:
        entry["state"], entry["reason"] = "SCHEMA", f"{n:,} rows exceeds the {MAX_FEATURES:,} mirror cap"
    elif state["bytes"] > TOTAL_BUDGET:
        entry["state"], entry["reason"] = "SCHEMA", "repository size budget reached"
    else:
        try:
            blob = fetch(base + f"?$limit={MAX_FEATURES}", 180)
            if len(blob) > MAX_BYTES:
                entry["state"], entry["reason"] = "SCHEMA", "payload exceeds per-file cap"
            else:
                rows = json.loads(blob)
                p = f"KCMO/{rec['id']}.json.gz"
                entry["bytes"] = save(p, rows)
                entry["file"] = p
                entry["features"] = len(rows)
                entry["state"] = "PULLED"
                if rows:
                    entry["fields"] = [{"name": k, "type": "inferred"} for k in rows[0].keys()]
        except Exception as e:
            entry["state"], entry["reason"] = "BLOCKED", why(e)
    out["layers"].append(entry)
    return (entry["state"] if entry["state"] != "BLOCKED" else "BLOCKED"), entry.get("reason", ""), out


# ------------------------------------------------------------------ driver
def handle(rec):
    if rec["person_flags"]:
        return {"id": rec["id"], "title": rec["title"], "source": rec["source"],
                "authority": rec["authority"], "state": "WITHHELD",
                "reason": "person-level screen: " + ", ".join(rec["person_flags"][:4]),
                "endpoint": rec["access_url"] or rec["landing"], "layers": []}
    if not rec["machine_readable"]:
        return {"id": rec["id"], "title": rec["title"], "source": rec["source"],
                "authority": rec["authority"], "state": "BLOCKED",
                "reason": "no machine-readable distribution - " + rec["access_barrier"],
                "endpoint": rec["landing"] or rec["access_url"], "layers": []}
    url = rec["access_url"] or ""
    try:
        if "/resource/" in url and "kcmo" in url:
            st, rsn, out = pull_socrata(rec)
        elif "rest/services" in url:
            st, rsn, out = pull_arcgis(rec)
        else:
            return {"id": rec["id"], "title": rec["title"], "source": rec["source"],
                    "authority": rec["authority"], "state": "SCHEMA",
                    "reason": "distribution is a download or page, not a queryable service",
                    "endpoint": url, "layers": []}
    except Exception as e:
        return {"id": rec["id"], "title": rec["title"], "source": rec["source"],
                "authority": rec["authority"], "state": "BLOCKED", "reason": why(e),
                "endpoint": url, "layers": []}
    out["state"] = st
    out["reason"] = rsn
    return out


if __name__ == "__main__":
    cat = json.load(open(os.path.join(HERE, "catalog.json")))
    recs = cat["datasets"]
    print(f"{len(recs)} records; workers={WORKERS}; caps {MAX_FEATURES:,} feat / "
          f"{MAX_BYTES//1024//1024} MB file / {TOTAL_BUDGET//1024//1024} MB total\n")

    results, t0 = [], time.time()
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(handle, r): r for r in recs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            try:
                results.append(f.result())
            except Exception as e:
                r = futs[f]
                results.append({"id": r["id"], "title": r["title"], "source": r["source"],
                                "authority": r["authority"], "state": "BLOCKED",
                                "reason": why(e), "endpoint": r.get("access_url", ""), "layers": []})
            if i % 100 == 0:
                print(f"  {i}/{len(recs)}  {state['bytes']/1024/1024:.0f} MB  {time.time()-t0:.0f}s", flush=True)

    import collections
    tally = collections.Counter(r["state"] for r in results)
    feats = sum(l.get("features", 0) for r in results for l in r.get("layers", []))
    files = sum(1 for r in results for l in r.get("layers", []) if l.get("file"))

    json.dump({"generated": NOW, "caps": {"max_features": MAX_FEATURES,
                                          "max_bytes": MAX_BYTES, "budget": TOTAL_BUDGET},
               "tally": dict(tally), "features_pulled": feats, "files": files,
               "bytes": state["bytes"], "records": results},
              open(os.path.join(HERE, "pull_status.json"), "w"), indent=1)

    print("\n" + "=" * 46)
    for k, v in tally.most_common():
        print(f"  {k:9s} {v:5d}")
    print(f"  files    {files:5d}\n  features {feats:,}\n  size     {state['bytes']/1024/1024:.1f} MB")
    print(f"  elapsed  {time.time()-t0:.0f}s")
