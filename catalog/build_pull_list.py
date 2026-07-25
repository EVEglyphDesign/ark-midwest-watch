#!/usr/bin/env python3
"""Generate HOLDINGS.md, LOCK-INS.md, and holdings.html from pull_status.json.

HOLDINGS.md  what is actually held in this repository, dataset by dataset
LOCK-INS.md  every wall encountered, named, with the reason and who can remove it
holdings.html  the same, searchable, loading only from this repository
"""
import json, os, collections, html, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
st = json.load(open(os.path.join(HERE, "pull_status.json")))
recs = st["records"]
gen = st["generated"]

FOOT = """
---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
"""

by_state = collections.defaultdict(list)
for r in recs:
    by_state[r["state"]].append(r)

pulled = by_state["PULLED"]
schema = by_state["SCHEMA"]
withheld = by_state["WITHHELD"]
blocked = by_state["BLOCKED"]
feats = st["features_pulled"]
files = st["files"]
mb = st["bytes"] / 1024 / 1024
part = st.get("partial_layers", 0)


def rows(r):
    return sum(l.get("features", 0) for l in r.get("layers", []))


# ------------------------------------------------------------------ HOLDINGS
L = [f"""# ARK-CIVIC · Holdings

**Captured:** {gen}
**Held in this repository:** {len(pulled):,} datasets · {files:,} files · {feats:,} records · {mb:.0f} MB
**Held in part:** {part} layers are shorter than the publisher's own row count and each says so
**Instance:** `midwest-lenexa`

Every file below is in `catalog/data/`, gzipped, pulled from the publisher's own
endpoint. Nothing here is fetched at page load. If every upstream endpoint were
withdrawn tomorrow, all of it would still be here.

Every count was read back off the stored file after trimming, not carried over
from the fetch. {part} layers are held in part rather than whole — an ArcGIS
service answers with one page at a time, and files over this repository's 4 MB
ceiling were cut. Each of those carries a `truncated` field in `pull_status.json`
stating both numbers. **A partial holding presented as a whole one is a quiet
falsehood, so none of them are counted as complete.**

| State | Datasets | Meaning |
|---|---:|---|
| **PULLED** | {len(pulled):,} | contents held in this repository |
| **SCHEMA** | {len(schema):,} | endpoint reachable, structure and row count held, contents not mirrored |
| **WITHHELD** | {len(withheld):,} | reachable and deliberately not requested — person-level screen |
| **BLOCKED** | {len(blocked):,} | could not be pulled; every reason named in [`LOCK-INS.md`](LOCK-INS.md) |

**WITHHELD is a choice, not a failure.** Those {len(withheld)} datasets were never
requested — not fetched and discarded. The canon forbids person-level data in this
repository and the screen runs before any content request is made.

## Held datasets by publisher
"""]
by_auth = collections.Counter(r["authority"] for r in pulled)
L.append("| Publishing authority | Datasets held | Records held |")
L.append("|---|---:|---:|")
for a, n in by_auth.most_common():
    fr = sum(rows(r) for r in pulled if r["authority"] == a)
    L.append(f"| {a} | {n:,} | {fr:,} |")

L.append("\n## Largest holdings\n")
L.append("| Dataset | Publisher | Records | Endpoint |")
L.append("|---|---|---:|---|")
for r in sorted(pulled, key=rows, reverse=True)[:40]:
    ep = (r.get("layers") or [{}])[0].get("endpoint") or r.get("endpoint", "")
    L.append(f"| {r['title'][:70]} | {r['authority'][:34]} | {rows(r):,} | [`endpoint`]({ep}) |")

L.append(f"\n## Every held dataset ({len(pulled):,})\n")
L.append("| Dataset | Publisher | Records | Files |")
L.append("|---|---|---:|---:|")
for r in sorted(pulled, key=lambda x: (x["authority"], x["title"].lower())):
    nf = sum(1 for l in r.get("layers", []) if l.get("file"))
    L.append(f"| {r['title'][:78]} | {r['authority'][:32]} | {rows(r):,} | {nf} |")
L.append(FOOT)
open(os.path.join(HERE, "HOLDINGS.md"), "w").write("\n".join(L))

# ------------------------------------------------------------------ LOCK-INS
def norm(s):
    return re.sub(r"[\d,]+", "N", (s or ""))[:100]


groups = collections.Counter(norm(r.get("reason")) for r in blocked)
schema_groups = collections.Counter(norm(r.get("reason")) for r in schema)

REMEDY = {
    "response was not valid JSON":
        ("The record points at a map viewer, story map, or application page rather than a dataset. "
         "The data behind the viewer exists in a service; only the viewer is catalogued. "
         "Removable by the publisher by listing the underlying layer alongside the app.", "publisher"),
    "no distribution offers a machine-readable format":
        ("The record carries only a landing page — a description of data with no download and no API. "
         "Removable by the publisher at no cost by attaching a distribution to the existing record.", "publisher"),
    "no machine-readable distribution - human-readable page only":
        ("The publisher describes the dataset but offers no download or API. "
         "Removable by the publisher at no cost by attaching a distribution to the existing record.", "publisher"),
    "no machine-readable distribution - viewer or application only":
        ("Published as a map viewer or app. The data behind it exists in a service; only the viewer is exposed. "
         "Removable by the publisher by sharing the underlying layer.", "publisher"),
    "HTTP N Forbidden":
        ("The endpoint exists and refuses anonymous access. Removable by the publisher's access "
         "configuration, or by a credential the public does not hold.", "publisher"),
    "HTTP N ":
        ("A Socrata record holding a document or file attachment rather than a table; the data API "
         "rejects it. The document itself is reachable through the portal page. "
         "Removable by publishing the underlying figures as a table beside the document.", "publisher"),
    "service error: Layer not found":
        ("The catalogue record points at a layer index that no longer exists in the service. "
         "Removable by the publisher by repairing the catalogue entry.", "publisher"),
    "ValueError: payload exceeded the size cap during transfer":
        ("Not a wall — this record's own transfer cap stopped the download.", "this record"),
}
SELF = {
    "repository size budget reached":
        ("Not a wall. This record's own size budget for a single run was reached. The endpoint is "
         "reachable and the data is available. Removable by raising the budget and running again.", "this record"),
    "N features exceeds the N mirror cap":
        ("Not a wall. Larger than this record's per-dataset mirror cap. Reachable and available.", "this record"),
    "N rows exceeds the N mirror cap":
        ("Not a wall. Larger than this record's per-dataset mirror cap. Reachable and available.", "this record"),
}
REMEDY.update(SELF)

K = [f"""# ARK-CIVIC · Lock-in register

**Captured:** {gen}
**Blocked:** {len(blocked):,} datasets · **schema-only:** {len(schema):,} · **withheld by canon:** {len(withheld):,}

A wall that is named is a finding. A wall that is silently skipped is a lie by
omission. Every dataset this record could not pull is listed here with the exact
reason, and with who can remove it.

**Filed against instruments, never people.** Every entry below describes a
publishing arrangement, a format decision, or an access configuration. None of it
is a judgement about the competence or intent of anyone maintaining these systems.
Most of these conditions are inherited from procurement and platform defaults that
the people operating them did not choose.

## Blocked — reasons
"""]
K.append("| Reason | Datasets | Who can remove it |")
K.append("|---|---:|---|")
DISPLAY = {
    "HTTP N ": "HTTP 400 — the data API rejects the record",
    "HTTP N Forbidden": "HTTP 403 — anonymous access refused",
    "response was not valid JSON": "the record is an application or viewer, not a dataset",
    "ValueError: payload exceeded the size cap during transfer": "payload exceeded this record's transfer cap",
}
for reason, n in groups.most_common():
    rem, who = REMEDY.get(reason, ("Cause recorded verbatim from the endpoint.", "publisher"))
    K.append(f"| {DISPLAY.get(reason, reason)} | {n:,} | {who} — {rem} |")

K.append("\n## Blocked by publisher\n")
K.append("| Publishing authority | Blocked | Total indexed | Share blocked |")
K.append("|---|---:|---:|---:|")
tot = collections.Counter(r["authority"] for r in recs)
bl = collections.Counter(r["authority"] for r in blocked)
for a, n in bl.most_common():
    K.append(f"| {a} | {n:,} | {tot[a]:,} | {n*100//max(tot[a],1)}% |")

K.append("""
## Walls that are mine, not the publishers'

Honesty requires separating the two. Of the schema-only records, **419** were not
mirrored because this run reached its own size budget, and **141** because the
dataset is larger than this record's per-dataset mirror cap. Those endpoints are
open, the publishers are doing nothing wrong, and the data is available. Raising
the caps and running again pulls them.

Two further corrections belong here rather than in any publisher's column. The
first pass of this pull marked 868 records "not a queryable service" and 407
"page only". Both verdicts were wrong. Every record in the MARC and Kansas DASC
feeds carries five or six distributions — Web Page, ArcGIS REST, CSV, ZIP,
GeoJSON, KML — and the first pass selected the first matching format string, saw
it was not a REST path, and stopped without trying the REST endpoint or the
GeoJSON sitting in the same record. The second pass tries every distribution in
preference order, which is why the held count moved from 264 datasets to 613 and
the held record count from 733,582 to 2,870,381. The blocked count fell from 429
to 251. **Every one of the 178 records that moved out of BLOCKED had been blocked
by this record's own shortcut, not by any publisher.**
""")

K.append("\n## Schema-only — reasons\n")
K.append("These are reachable. The structure and the row count are held; the contents are not.\n")
K.append("| Reason | Datasets |")
K.append("|---|---:|")
for reason, n in schema_groups.most_common(12):
    K.append(f"| {reason or 'reached, contents not mirrored'} | {n:,} |")

K.append(f"""
## Structural lock-ins

These are not per-dataset failures. They are conditions of the jurisdiction, and
each one is a `CMN` register finding — commons access — filed against the
arrangement, not the operator.

**CMN-1 · Johnson County publishes no open-data catalogue feed.** Eight plausible
endpoints were probed and none exist: `opendata.jocogov.org`, `data.jocogov.org`,
`data-jocogov.opendata.arcgis.com`, `aims-jocogov.opendata.arcgis.com`, and four
others recorded in `PROVENANCE.md`. County data is reachable only by knowing that
an ArcGIS REST directory exists at `maps.jocogov.org` and knowing how to walk it.
Neighbouring MARC and the State of Kansas both publish DCAT-US 1.1 feeds; the
county does not. *Removable by the county at low cost — the ArcGIS platform they
already run emits this feed as a configuration option.*

**CMN-2 · Bulk county data remains a paid Digital Data Request.** The free
download page offers roughly 90 datasets; anything beyond it is a priced request.
Data produced by public taxation is metered on re-access. *Removable by the county
by fee-schedule decision.*

**CMN-3 · Government data is less machine-reachable than land data.** Parcels,
aquifers, and soils resolve as queryable services. Budgets, contracts, meeting
records, and procurement do not appear as machine-readable distributions anywhere
in the {len(recs):,} records indexed. The asymmetry is not deliberate; it follows
from GIS platforms emitting APIs by default while document systems do not.
*Removable by publishing the documents through any system with a feed.*

**CMN-4 · The open-meetings floor is opt-in.** KOMA (K.S.A. 75-4317 et seq.)
requires no agenda, no minutes, and no posted notice. Where a Kansas public body
publishes those things, it is a local choice that a future body can reverse without
violating any statute. *Removable only by the Legislature.*

## Withheld by canon — not a lock-in

{len(withheld)} datasets were reachable and were deliberately not requested. This is
the privacy invariant operating as designed, and it is recorded here so the count is
never mistaken for a wall imposed from outside. It is a wall this record imposes on
itself.
""")
K.append("| Dataset | Publisher | Screen |")
K.append("|---|---|---|")
for r in sorted(withheld, key=lambda x: x["title"].lower())[:50]:
    K.append(f"| {r['title'][:66]} | {r['authority'][:30]} | `{r['reason'].replace('person-level screen: ','')}` |")
if len(withheld) > 50:
    K.append(f"\n*{len(withheld)-50} further withheld records in `pull_status.json`.*")
K.append(FOOT)
open(os.path.join(HERE, "LOCK-INS.md"), "w").write("\n".join(K))

# ------------------------------------------------------------------ holdings.html
payload = json.dumps([{
    "t": r["title"][:150], "a": r["authority"], "s": r["source"], "st": r["state"],
    "n": rows(r), "r": (r.get("reason") or "")[:150],
    "u": (r.get("layers") or [{}])[0].get("endpoint") or r.get("endpoint", ""),
    "f": [l.get("file") for l in r.get("layers", []) if l.get("file")][:3],
} for r in recs], separators=(",", ":"))

STATE_NOTE = {
    "PULLED": "contents held in this repository",
    "SCHEMA": "reachable; structure and row count held, contents not mirrored",
    "WITHHELD": "reachable and deliberately not requested — person-level screen",
    "BLOCKED": "could not be pulled; reason recorded",
}
page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Holdings and lock-ins · ARK-CIVIC Midwest Watch</title>
<meta name="description" content="{len(pulled):,} datasets held, {feats:,} records, and every wall named.">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/ark-civic.css">
</head>
<body>
<header class="ark-head">
  <div class="wrap">
    <img class="crest" src="assets/portal-crest.svg" alt="" width="60" height="60">
    <p class="eyebrow">Archive of Recorded Kondition · civic sub-record</p>
    <h1>Holdings and lock-ins</h1>
    <p class="sub">What was pulled, what was held back, and every wall named</p>
    <p class="meta">{len(recs):,} datasets assessed · captured {gen[:10]}</p>
  </div>
</header>

<main class="wrap">
  <section>
    <div class="stat-row">
      <div class="stat"><span class="n">{len(pulled):,}</span><span class="l">pulled</span></div>
      <div class="stat"><span class="n">{feats:,}</span><span class="l">records held</span></div>
      <div class="stat"><span class="n">{len(schema):,}</span><span class="l">schema only</span></div>
      <div class="stat"><span class="n">{len(withheld)}</span><span class="l">withheld by canon</span></div>
      <div class="stat"><span class="n">{len(blocked):,}</span><span class="l">blocked</span></div>
      <div class="stat"><span class="n">{part}</span><span class="l">held in part</span></div>
    </div>
    <p class="lede">{feats:,} records across {files:,} files are held in this repository, pulled
    from each publisher's own endpoint. {part} of those layers are held in part rather than whole,
    because a service answers with one page at a time and files over this record's 4&nbsp;MB ceiling
    were cut; each one states both numbers rather than being counted as complete. <strong>A wall that is named is a finding; a wall that is
    silently skipped is a lie by omission</strong> — so every dataset that could not be pulled is
    listed below with the reason and with who can remove it.</p>
    <div class="callout">
      <p><strong>{len(withheld)} datasets were reachable and deliberately not requested.</strong></p>
      <p>The person-level screen runs before any content request is made, so these were never
      fetched at all — not fetched and discarded. That includes the City of Lenexa Calls for Service
      service. This is the one wall in the list that this record imposes on itself, and it is the
      reason the honest answer to <em>what did you take</em> is: nothing about any person.</p>
    </div>
  </section>

  <section>
    <h2>Structural lock-ins</h2>
    <p>Not per-dataset failures — conditions of the jurisdiction. Each is a <code>CMN</code> register
    finding, filed against the arrangement and never against the people who operate it.</p>
    <div class="results">
      <article class="rec flagged"><h3>CMN-1 · No county open-data feed</h3>
      <p class="rec-desc">Eight plausible catalogue endpoints probed, none exist. County data is
      reachable only by knowing an ArcGIS REST directory exists and how to walk it. MARC and the
      State of Kansas both publish DCAT-US 1.1; the county does not.</p>
      <p class="tags"><span class="tag flag">removable by the county — the platform emits this feed as a configuration option</span></p></article>
      <article class="rec flagged"><h3>CMN-2 · Bulk data is a paid request</h3>
      <p class="rec-desc">Roughly 90 datasets download free; beyond that is a priced Digital Data
      Request. Data produced by public taxation is metered on re-access.</p>
      <p class="tags"><span class="tag flag">removable by fee-schedule decision</span></p></article>
      <article class="rec flagged"><h3>CMN-3 · Land data is reachable, government data is not</h3>
      <p class="rec-desc">Parcels, aquifers, and soils resolve as queryable services. Budgets,
      contracts, meeting records, and procurement appear as machine-readable distributions nowhere in
      the {len(recs):,} records indexed. Not deliberate — GIS platforms emit APIs by default and
      document systems do not.</p>
      <p class="tags"><span class="tag flag">removable by publishing documents through any system with a feed</span></p></article>
      <article class="rec flagged"><h3>CMN-4 · The open-meetings floor is opt-in</h3>
      <p class="rec-desc">KOMA requires no agenda, no minutes, and no posted notice. Where a Kansas
      public body publishes these, it is a local choice a future body can reverse without violating
      any statute.</p>
      <p class="tags"><span class="tag flag">removable only by the Legislature</span></p></article>
    </div>
  </section>

  <section>
    <h2>Every dataset assessed</h2>
    <div class="controls">
      <input id="q" type="search" placeholder="Search datasets, publishers, reasons…" aria-label="Search">
      <select id="st" aria-label="Filter by state">
        <option value="">All states</option>
        {''.join(f'<option value="{k}">{k} ({len(by_state[k])}) — {STATE_NOTE[k]}</option>' for k in ("PULLED","SCHEMA","WITHHELD","BLOCKED"))}
      </select>
    </div>
    <p id="count" class="count"></p>
    <div id="results" class="results"></div>
    <p id="more" class="more"></p>
  </section>

  <section>
    <p><a href="catalog.html">← Catalogue index</a> · <a href="index.html">civic-condition record</a> ·
    <a href="catalog/HOLDINGS.md">HOLDINGS.md</a> · <a href="catalog/LOCK-INS.md">LOCK-INS.md</a> ·
    <a href="catalog/pull_status.json">pull_status.json</a></p>
  </section>
</main>

<footer class="ark-foot">
  <div class="wrap">
    <p class="copyright">© 2026 Dany Theriault. EVE &ldquo;digital stem cell&rdquo; glyph and
    glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment
    for large public and institutional usage rests with the Pacific Utilities Design Council.
    Published as a time-stamped record of authorship and intent.</p>
    <p class="fr">Pour le bien-être du peuple.</p>
  </div>
</footer>

<script>
const DATA = {payload};
const q=document.getElementById('q'), stf=document.getElementById('st'),
      out=document.getElementById('results'), cnt=document.getElementById('count'),
      more=document.getElementById('more');
const CLS={{PULLED:'ok',SCHEMA:'fmt',WITHHELD:'lx',BLOCKED:'flag'}};
let limit=100;
function esc(s){{return String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));}}
function render(){{
  const term=q.value.trim().toLowerCase(), s=stf.value;
  const m=DATA.filter(d=>(!s||d.st===s)&&(!term||(d.t+' '+d.a+' '+d.r+' '+d.s).toLowerCase().includes(term)));
  cnt.textContent=m.length.toLocaleString()+' of '+DATA.length.toLocaleString()+' datasets';
  out.innerHTML=m.slice(0,limit).map(d=>`
    <article class="rec${{d.st==='BLOCKED'?' flagged':''}}">
      <h3>${{d.u?`<a href="${{esc(d.u)}}" rel="noopener">${{esc(d.t)}}</a>`:esc(d.t)}}</h3>
      <p class="rec-meta">${{esc(d.a)}} · ${{esc(d.s)}}${{d.n?' · '+d.n.toLocaleString()+' records held':''}}</p>
      ${{d.r?`<p class="rec-desc">${{esc(d.r)}}</p>`:''}}
      <p class="tags"><span class="tag ${{CLS[d.st]}}">${{d.st}}</span>
      ${{(d.f||[]).map(f=>'<span class="tag fmt">'+esc(f)+'</span>').join('')}}</p>
    </article>`).join('');
  more.textContent=m.length>limit?'Showing first '+limit+'. Narrow the search to see more.':'';
}}
[q,stf].forEach(e=>e.addEventListener('input',()=>{{limit=100;render();}}));
render();
</script>
</body>
</html>
"""
open(os.path.join(ROOT, "holdings.html"), "w").write(page)
print(f"HOLDINGS.md · LOCK-INS.md · holdings.html")
print(f"  pulled {len(pulled)}  schema {len(schema)}  withheld {len(withheld)}  blocked {len(blocked)}")
print(f"  {feats:,} records · {files:,} files · {mb:.0f} MB")
