#!/usr/bin/env python3
"""Complete the truncated pulls.

An ArcGIS layer answers a query with at most `maxRecordCount` features, commonly
2,000. Passing resultRecordCount=30000 does not raise that ceiling - the server
silently returns its page and no error. 96 layers came back short by 678,339
records and nothing in the output said so. A partial holding presented as a whole
one is a quiet falsehood, so this pass walks the pages with resultOffset until the
server says exceededTransferLimit is false or the layer's own count is reached.

Anything that still cannot be completed is recorded as PARTIAL with both numbers,
never rounded up into PULLED.
"""
import json, os, gzip, time, urllib.request, urllib.error, socket
import concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
UA = "ARK-CIVIC/1.0 (+https://eveglyphdesign.github.io/ark-midwest-watch/) civic-condition record"
BUDGET = 190 * 1024 * 1024
CAP = 30000
state = {"bytes": 0}


def fetch(url, timeout=45, deadline=100):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    t0, buf = time.time(), []
    with urllib.request.urlopen(req, timeout=timeout) as r:
        while True:
            if time.time() - t0 > deadline:
                raise TimeoutError(f"transfer exceeded the {deadline}s time budget")
            c = r.read(262144)
            if not c:
                break
            buf.append(c)
    return b"".join(buf)


def why(e):
    if isinstance(e, urllib.error.HTTPError):
        return f"HTTP {e.code} {e.reason}"
    if isinstance(e, (socket.timeout, TimeoutError)):
        return f"timeout - {e}"
    if isinstance(e, urllib.error.URLError):
        return f"unreachable - {getattr(e,'reason',e)}"
    return f"{type(e).__name__}: {str(e)[:120]}"


def complete(job):
    rid, title, ep, have, want, path = job
    feats, offset, page = [], 0, 2000
    try:
        while len(feats) < min(want, CAP):
            q = (ep + "/query?where=1%3D1&outFields=*&returnGeometry=true&outSR=4326"
                      f"&f=geojson&resultOffset={offset}&resultRecordCount={page}")
            gj = json.loads(fetch(q))
            got = gj.get("features") or []
            if not got:
                break
            feats.extend(got)
            offset += len(got)
            if len(got) < page and not gj.get("properties", {}).get("exceededTransferLimit"):
                break
            if state["bytes"] > BUDGET:
                break
    except Exception as e:
        if not feats:
            return {"id": rid, "ok": False, "reason": why(e), "have": have, "want": want}

    if len(feats) <= have:
        return {"id": rid, "ok": False, "reason": "pagination returned no more than the first page",
                "have": have, "want": want}

    blob = json.dumps({"type": "FeatureCollection", "features": feats}, separators=(",", ":")).encode()
    full = os.path.join(DATA, path)
    before = os.path.getsize(full) if os.path.exists(full) else 0
    with gzip.open(full, "wb", compresslevel=9) as f:
        f.write(blob)
    state["bytes"] += os.path.getsize(full) - before
    return {"id": rid, "ok": True, "have": len(feats), "want": want,
            "bytes": os.path.getsize(full)}


if __name__ == "__main__":
    P = os.path.join(HERE, "pull_status.json")
    st = json.load(open(P))
    jobs = []
    for r in st["records"]:
        if r["state"] != "PULLED":
            continue
        for l in r.get("layers", []):
            f, c, ep, fp = l.get("features"), l.get("count"), l.get("endpoint"), l.get("file")
            if f is not None and c and ep and fp and f < c:
                jobs.append((r["id"], r["title"], ep.split("?")[0].rstrip("/"), f, c, fp))
    print(f"{len(jobs)} truncated layers to complete\n")

    res = {}
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(complete, j) for j in jobs]
        for i, fu in enumerate(cf.as_completed(futs), 1):
            try:
                r = fu.result()
                res.setdefault(r["id"], []).append(r)
            except Exception:
                pass
            if i % 20 == 0:
                print(f"  {i}/{len(jobs)}  +{state['bytes']/1024/1024:.0f} MB  {time.time()-t0:.0f}s", flush=True)

    fixed = partial = 0
    for rec in st["records"]:
        rs = res.get(rec["id"])
        if not rs:
            continue
        for l in rec.get("layers", []):
            for r in rs:
                if r.get("ok") and l.get("features") is not None and l.get("count") == r["want"]:
                    l["features"] = r["have"]
                    if r["have"] < r["want"]:
                        l["truncated"] = f"{r['have']:,} of {r['want']:,} - capped at {CAP:,}"
                elif not r.get("ok"):
                    l["truncated"] = f"{l.get('features',0):,} of {r['want']:,} - {r['reason']}"
        for l in rec.get("layers", []):
            if l.get("truncated"):
                partial += 1
            elif l.get("file"):
                fixed += 1

    t = sum(os.path.getsize(os.path.join(rt, f)) for rt, _, fs in os.walk(DATA) for f in fs)
    st["bytes"] = t
    st["features_pulled"] = sum(l.get("features", 0) for r in st["records"] for l in r.get("layers", []))
    st["truncation_note"] = ("96 layers were short of the publisher's own row count because ArcGIS "
                             "returns one page per query. They were paginated. Layers still short "
                             "carry a `truncated` field stating both numbers.")
    json.dump(st, open(P, "w"), indent=1)
    print(f"\n  complete layers {fixed}\n  still partial   {partial}")
    print(f"  records held    {st['features_pulled']:,}\n  size            {t/1024/1024:.1f} MB")
