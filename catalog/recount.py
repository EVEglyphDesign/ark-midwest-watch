#!/usr/bin/env python3
"""Recount every held file from the file itself.

Trimming to the size ceiling changed what is on disk. Reporting counts from
memory of what was fetched, rather than from the bytes actually held, is exactly
the kind of unverified claim this record exists to avoid. So every number below
is read back off the file.
"""
import json, gzip, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CAP = 4 * 1024 * 1024
P = os.path.join(HERE, "pull_status.json")
st = json.load(open(P))

pairs = [(l["file"], r, l) for r in st["records"] for l in r.get("layers", []) if l.get("file")]
print(f"{len(pairs)} files to verify")

missing, trimmed_now = 0, 0
for i, (rel, r, l) in enumerate(pairs, 1):
    full = os.path.join(DATA, rel)
    if not os.path.exists(full):
        l["features"] = 0
        l["truncated"] = "file missing from the repository"
        missing += 1
        continue
    raw = gzip.open(full, "rb").read()
    # anything still over the ceiling gets cut here
    if len(gzip.compress(raw[:1], 1)) and os.path.getsize(full) > CAP:
        if rel.endswith(".csv.gz"):
            lines = raw.split(b"\n")
            lo, hi = 1, len(lines) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if len(gzip.compress(b"\n".join(lines[:mid + 1]), 6)) <= CAP:
                    lo = mid
                else:
                    hi = mid - 1
            raw = b"\n".join(lines[:lo + 1])
        else:
            try:
                gj = json.loads(raw)
                feats = gj.get("features") or []
                lo, hi = 1, len(feats)
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    blob = json.dumps({"type": "FeatureCollection", "features": feats[:mid]},
                                      separators=(",", ":")).encode()
                    if len(gzip.compress(blob, 6)) <= CAP:
                        lo = mid
                    else:
                        hi = mid - 1
                raw = json.dumps({"type": "FeatureCollection", "features": feats[:lo]},
                                 separators=(",", ":")).encode()
            except Exception:
                pass
        open(full, "wb").write(gzip.compress(raw, 9))
        trimmed_now += 1

    if rel.endswith(".csv.gz"):
        n = max(raw.count(b"\n") - 1, 0)
    else:
        try:
            n = len(json.loads(raw).get("features") or [])
        except Exception:
            n = 0
    l["features"] = n
    want = l.get("count")
    if want and n < want:
        l["truncated"] = (f"{n:,} of {want:,} held - trimmed to this repository's 4 MB per-file "
                          f"ceiling; the publisher's endpoint serves the rest")
    else:
        l.pop("truncated", None)
    if i % 150 == 0:
        print(f"  {i}/{len(pairs)}", flush=True)

tot = sum(os.path.getsize(os.path.join(rt, f)) for rt, _, fs in os.walk(DATA) for f in fs)
st["bytes"] = tot
st["features_pulled"] = sum(l.get("features", 0) for r in st["records"] for l in r.get("layers", []))
part = sum(1 for r in st["records"] for l in r.get("layers", []) if l.get("truncated"))
st["partial_layers"] = part
st["verification_note"] = ("Every record count below was read back off the stored file after "
                           "trimming, not carried over from the fetch. Layers held short of the "
                           "publisher's own row count carry a `truncated` field stating both numbers.")
json.dump(st, open(P, "w"), indent=1)
print(f"\n  files {len(pairs)} · missing {missing} · trimmed in this pass {trimmed_now}")
print(f"  records held {st['features_pulled']:,} · partial layers {part} · {tot/1e6:.0f} MB")
