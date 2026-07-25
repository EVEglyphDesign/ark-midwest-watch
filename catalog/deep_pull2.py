#!/usr/bin/env python3
"""
ARK-CIVIC deep pull, pass 2.

Pass 1 marked 868 records "not a queryable service" and 407 "page only". That
verdict was wrong and it was mine, not the publishers'. Every DCAT record in the
MARC and Kansas DASC feeds carries five or six distributions - Web Page, ArcGIS
REST, CSV, ZIP, GeoJSON, KML. Pass 1 selected the first matching format string,
which was CSV, saw it was not a REST path, and stopped. It never tried the REST
endpoint or the GeoJSON download sitting in the same record.

This pass re-reads the raw DCAT snapshots, picks the best distribution rather
than the first, and retries every record pass 1 gave up on.

Preference order:
  1. ArcGIS REST layer  - queryable, gives schema and an exact row count, and
                          respects the mirror cap without downloading first
  2. GeoJSON download   - one shot, capped by byte size
  3. CSV download       - last resort, no geometry

The person-level screen still runs first and is still absolute.
"""

import json, os, gzip, time, urllib.request, urllib.error, datetime, socket
import concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
UA = "ARK-CIVIC/1.0 (+https://eveglyphdesign.github.io/ark-midwest-watch/) civic-condition record"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

MAX_FEATURES = 30000
MAX_BYTES = 25 * 1024 * 1024
ADDED_BUDGET = 260 * 1024 * 1024
WORKERS = 8
state = {"bytes": 0}


def fetch(url, timeout=45, deadline=90):
    """Read with a hard wall-clock deadline.

    A socket timeout only fires when nothing arrives at all. An endpoint that
    trickles bytes slowly never trips it, so the first attempt at this pass hung
    all eight workers indefinitely on slow downloads. The deadline below bounds
    the whole transfer, not just the gaps in it.
    """
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    t0 = time.time()
    buf, n = [], 0
    with urllib.request.urlopen(req, timeout=timeout) as r:
        while True:
            if time.time() - t0 > deadline:
                raise TimeoutError(f"transfer exceeded the {deadline}s time budget")
            c = r.read(262144)
            if not c:
                break
            buf.append(c)
            n += len(c)
            if n > MAX_BYTES * 3:
                raise ValueError("payload exceeded the size cap during transfer")
    return b"".join(buf)


def jget(url, timeout=60):
    return json.loads(fetch(url, timeout))


def why(e):
    if isinstance(e, urllib.error.HTTPError):
        return f"HTTP {e.code} {e.reason}"
    if isinstance(e, urllib.error.URLError):
        r = getattr(e, "reason", e)
        if isinstance(r, socket.gaierror):
            return "DNS does not resolve - host does not exist"
        if isinstance(r, socket.timeout):
            return "timeout - endpoint did not respond"
        return f"unreachable - {r}"
    if isinstance(e, (socket.timeout, TimeoutError)):
        return f"timeout - {e}" if str(e) else "timeout - endpoint did not respond"
    if isinstance(e, json.JSONDecodeError):
        return "response was not valid JSON"
    return f"{type(e).__name__}: {str(e)[:150]}"


def save(path, raw_bytes):
    full = os.path.join(DATA, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with gzip.open(full, "wb", compresslevel=9) as f:
        f.write(raw_bytes)
    n = os.path.getsize(full)
    state["bytes"] += n
    return n


def best_dists(ds):
    rest = geo = csv = None
    for x in ds.get("distribution", []) or []:
        f = (x.get("format") or "").lower()
        u = x.get("downloadURL") or x.get("accessURL")
        if not u:
            continue
        if "geoservices" in f or "rest api" in f:
            rest = rest or u
        elif f == "geojson":
            geo = geo or u
        elif f == "csv":
            csv = csv or u
    return rest, geo, csv


def try_rest(url, rid, src):
    """url is usually a layer URL (.../MapServer/1). Returns (state, reason, info)."""
    base = url.split("?")[0].rstrip("/")
    meta = jget(base + "?f=json", 45)
    if meta.get("error"):
        return "BLOCKED", "service error: " + str(meta["error"].get("message"))[:110], {}
    info = {
        "endpoint": base,
        "geometry_type": meta.get("geometryType"),
        "fields": [{"name": f.get("name"), "type": f.get("type")} for f in (meta.get("fields") or [])],
        "max_record_count": meta.get("maxRecordCount"),
    }
    if "fields" not in meta and "layers" in meta:
        return "SCHEMA", "endpoint is a service root, not a layer", info
    try:
        info["count"] = jget(base + "/query?where=1%3D1&returnCountOnly=true&f=json", 45).get("count")
    except Exception as e:
        info["count"] = None
        info["count_error"] = why(e)
    c = info.get("count")
    if c is None:
        return "SCHEMA", "endpoint refused a count query", info
    if c == 0:
        return "SCHEMA", "layer is empty", info
    if c > MAX_FEATURES:
        return "SCHEMA", f"{c:,} features exceeds the {MAX_FEATURES:,} mirror cap", info
    if state["bytes"] > ADDED_BUDGET:
        return "SCHEMA", "repository size budget reached", info
    q = (base + "/query?where=1%3D1&outFields=*&returnGeometry=true&outSR=4326"
                "&f=geojson&resultRecordCount=" + str(MAX_FEATURES))
    blob = fetch(q, 45, 110)
    if len(blob) > MAX_BYTES:
        return "SCHEMA", f"payload {len(blob)//1024//1024} MB exceeds per-file cap", info
    gj = json.loads(blob)
    if gj.get("error"):
        return "BLOCKED", "query rejected: " + str(gj["error"].get("message"))[:110], info
    p = f"{src.replace(' ','_')}/{rid}.geojson.gz"
    info["bytes"] = save(p, blob)
    info["file"] = p
    info["features"] = len(gj.get("features", []))
    return "PULLED", "", info


def try_download(url, rid, src, kind):
    blob = fetch(url, 45, 110)
    if len(blob) > MAX_BYTES:
        return "SCHEMA", f"payload {len(blob)//1024//1024} MB exceeds per-file cap", {}
    if state["bytes"] > ADDED_BUDGET:
        return "SCHEMA", "repository size budget reached", {}
    ext = "geojson" if kind == "geojson" else "csv"
    info = {"endpoint": url}
    if kind == "geojson":
        try:
            gj = json.loads(blob)
        except Exception:
            return "BLOCKED", "download was not valid GeoJSON", info
        if gj.get("error"):
            return "BLOCKED", "download returned a service error", info
        info["features"] = len(gj.get("features", []))
        if info["features"] == 0:
            return "SCHEMA", "download contained zero features", info
    else:
        info["features"] = max(blob.count(b"\n") - 1, 0)
        if info["features"] == 0:
            return "SCHEMA", "download contained zero rows", info
    p = f"{src.replace(' ','_')}/{rid}.{ext}.gz"
    info["bytes"] = save(p, blob)
    info["file"] = p
    return "PULLED", "", info


def handle(item):
    rec, ds = item
    rid, src = rec["id"], rec["source"]
    rest, geo, csv = best_dists(ds)
    attempts = []
    for url, fn, kind in ((rest, try_rest, "rest"), (geo, try_download, "geojson"), (csv, try_download, "csv")):
        if not url:
            continue
        try:
            st, rsn, info = fn(url, rid, src) if kind == "rest" else fn(url, rid, src, kind)
            attempts.append({"via": kind, "state": st, "reason": rsn})
            if st == "PULLED":
                return {**rec_slim(rec), "state": "PULLED", "reason": "", "via": kind,
                        "layers": [info], "attempts": attempts}
            if st == "SCHEMA" and info.get("fields"):
                schema_hit = {**rec_slim(rec), "state": "SCHEMA", "reason": rsn, "via": kind,
                              "layers": [info], "attempts": attempts}
        except Exception as e:
            attempts.append({"via": kind, "state": "BLOCKED", "reason": why(e)})
    for a in attempts:
        if a["state"] == "SCHEMA":
            return {**rec_slim(rec), "state": "SCHEMA", "reason": a["reason"],
                    "via": a["via"], "layers": [], "attempts": attempts}
    if attempts:
        return {**rec_slim(rec), "state": "BLOCKED", "reason": attempts[0]["reason"],
                "via": attempts[0]["via"], "layers": [], "attempts": attempts}
    return {**rec_slim(rec), "state": "BLOCKED",
            "reason": "no distribution offers a machine-readable format", "layers": [], "attempts": []}


def rec_slim(r):
    return {"id": r["id"], "title": r["title"], "source": r["source"],
            "authority": r["authority"], "endpoint": r.get("access_url") or r.get("landing", "")}


if __name__ == "__main__":
    cat = json.load(open(os.path.join(HERE, "catalog.json")))
    status = json.load(open(os.path.join(HERE, "pull_status.json")))
    prev = {r["id"]: r for r in status["records"]}

    dcat = {}
    for fn in ("marc-dcat-us-1.1.json", "kansas-dasc-dcat-us-1.1.json"):
        for ds in json.load(open(os.path.join(HERE, "raw", fn))).get("dataset", []):
            if ds.get("landingPage"):
                dcat[ds["landingPage"]] = ds

    todo = []
    for r in cat["datasets"]:
        p = prev.get(r["id"])
        if not p or p["state"] in ("PULLED", "WITHHELD"):
            continue
        ds = dcat.get(r.get("landing"))
        if ds:
            todo.append((r, ds))

    # resumable: a long pull will be interrupted, and losing an hour of work to a
    # signal is not acceptable. Every result is appended to disk as it completes.
    JL = os.path.join(HERE, "pull2.jsonl")
    done = {}
    if os.path.exists(JL):
        for line in open(JL):
            try:
                r = json.loads(line)
                done[r["id"]] = r
            except Exception:
                pass
        state["bytes"] = sum(os.path.getsize(os.path.join(DATA, f))
                             for f in os.listdir(DATA) if os.path.isfile(os.path.join(DATA, f))) if False else state["bytes"]
        print(f"resuming: {len(done)} already done")
    todo = [t for t in todo if t[0]["id"] not in done]

    print(f"retrying {len(todo)} records that pass 1 gave up on\n")
    out, t0 = list(done.values()), time.time()
    jl = open(JL, "a")
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = [ex.submit(handle, t) for t in todo]
        for i, f in enumerate(cf.as_completed(futs), 1):
            try:
                res = f.result()
            except Exception:
                continue
            out.append(res)
            jl.write(json.dumps(res) + "\n")
            if i % 50 == 0:
                jl.flush()
                print(f"  {i}/{len(todo)}  +{state['bytes']/1024/1024:.0f} MB  {time.time()-t0:.0f}s", flush=True)
    jl.close()

    merged = dict(prev)
    for r in out:
        merged[r["id"]] = r

    import collections
    recs = list(merged.values())
    tally = collections.Counter(r["state"] for r in recs)
    feats = sum(l.get("features", 0) for r in recs for l in r.get("layers", []))
    files = sum(1 for r in recs for l in r.get("layers", []) if l.get("file"))
    total_bytes = status.get("bytes", 0) + state["bytes"]

    json.dump({"generated": NOW, "passes": 2,
               "caps": {"max_features": MAX_FEATURES, "max_bytes": MAX_BYTES},
               "tally": dict(tally), "features_pulled": feats, "files": files,
               "bytes": total_bytes, "records": recs},
              open(os.path.join(HERE, "pull_status.json"), "w"), indent=1)

    print("\n" + "=" * 46)
    for k, v in tally.most_common():
        print(f"  {k:9s} {v:5d}")
    print(f"  files    {files:5d}\n  features {feats:,}\n  total    {total_bytes/1024/1024:.1f} MB")
    print(f"  elapsed  {time.time()-t0:.0f}s")
