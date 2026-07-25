#!/usr/bin/env python3
"""Generate CATALOG.md and catalog.html from catalog.json.

The surface loads catalog.min.json from this repository. It makes no request to
any third party at page load. If every upstream endpoint were withdrawn tomorrow,
this index would still resolve and still show what existed, when it was captured,
and where it used to live.
"""
import json, os, collections, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
cat = json.load(open(os.path.join(HERE, "catalog.json")))
ds = cat["datasets"]
gen = cat["generated"]

by_source = collections.Counter(d["source"] for d in ds)
by_auth = collections.Counter(d["authority"] for d in ds)
machine = sum(1 for d in ds if d["machine_readable"])
person = [d for d in ds if d["person_flags"]]
lenexa = [d for d in ds if d["lenexa_specific"]]

FOOTER = """
---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
"""

# ----------------------------------------------------------------- CATALOG.md
L = []
L.append("# ARK-CIVIC · Catalogue index\n")
L.append(f"**Captured:** {gen}  ")
L.append(f"**Records:** {len(ds):,} across {len(by_source)} catalogues  ")
L.append(f"**Machine-reachable:** {machine:,} ({machine*100//len(ds)}%)  ")
L.append("**Instance:** `midwest-lenexa`\n")
L.append("""> **This index holds metadata, not contents.** It records what each dataset is,
> who publishes it, when it last changed, and the endpoint it can be reached at.
> It does not contain the records inside any dataset. No person-level data is
> mirrored into this repository, by canon and without exception.
>
> Held here so the record does not depend on any third party keeping an endpoint
> alive. Every upstream source could be withdrawn and this index would still
> resolve.
""")
L.append("## Sources captured\n")
L.append("| Catalogue | Publishing authority | Records | Endpoint |")
L.append("|---|---|---:|---|")
SRC_URL = {
    "MARC Open Data": "https://opendata-marc-gis.hub.arcgis.com/api/feed/dcat-us/1.1.json",
    "Kansas DASC": "https://hub.kansasgis.org/api/feed/dcat-us/1.1.json",
    "KCMO Open Data": "https://data.kcmo.org/api/views.json",
    "JoCo AIMS": "https://maps.jocogov.org/arcgis/rest/services",
    "Lenexa hosted": "https://services.arcgis.com/rQNf5tVFXFoS6EhP/arcgis/rest/services",
    "Lenexa published items": "https://www.arcgis.com/sharing/rest/search?q=owner:LenexaEST",
}
for s, n in by_source.most_common():
    auth = collections.Counter(d["authority"] for d in ds if d["source"] == s).most_common(1)[0][0]
    L.append(f"| {s} | {auth} | {n:,} | [`endpoint`]({SRC_URL.get(s,'')}) |")

L.append(f"\n## Lenexa-specific records ({len(lenexa)})\n")
L.append("| Dataset | Publisher | Machine-reachable | Last change |")
L.append("|---|---|---|---|")
for d in sorted(lenexa, key=lambda x: x["title"].lower()):
    m = "yes" if d["machine_readable"] else "**no**"
    L.append(f"| [{d['title']}]({d['landing'] or d['access_url']}) | {d['publisher']} | {m} | {d['modified'] or '—'} |")

L.append(f"\n## Person-level screen ({len(person)} flagged)\n")
L.append("""These datasets carry terms indicating they may contain person-level or
address-level records — arrests, citations, calls for service, ownership,
court, payroll. **They are indexed as existing and are never mirrored.** The
flag is a stop condition requiring a human read before any use, not a
judgement that the publisher was wrong to publish them.
""")
L.append("| Dataset | Publisher | Flags |")
L.append("|---|---|---|")
for d in sorted(person, key=lambda x: x["title"].lower())[:60]:
    L.append(f"| [{d['title']}]({d['landing'] or d['access_url']}) | {d['publisher']} | `{'`, `'.join(d['person_flags'][:4])}` |")
if len(person) > 60:
    L.append(f"\n*{len(person)-60} further flagged records in `catalog.json`.*")

L.append("""
## Refresh

```bash
python3 catalog/ingest.py         # re-pull upstream, rewrite catalog.json
python3 catalog/build_surface.py  # regenerate this file and catalog.html
```

Snapshots are kept in `catalog/raw/` exactly as received. Delete a file there to
force a re-pull of that source. Provenance and one corrected attribution error
are recorded in [`PROVENANCE.md`](PROVENANCE.md).
""")
L.append(FOOTER)
open(os.path.join(HERE, "CATALOG.md"), "w").write("\n".join(L))

# ----------------------------------------------------------------- catalog.html
rows_json = json.dumps([{
    "t": d["title"], "d": d["description"][:260], "p": d["publisher"], "s": d["source"],
    "m": d["modified"], "u": d["landing"] or d["access_url"], "a": d["access_url"],
    "r": 1 if d["machine_readable"] else 0, "f": d["person_flags"][:3],
    "x": 1 if d["lenexa_specific"] else 0, "fmt": d["formats"][:3],
} for d in ds], separators=(",", ":"))

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Catalogue index · ARK-CIVIC Midwest Watch</title>
<meta name="description" content="Held index of {len(ds):,} public datasets covering Lenexa, Johnson County, and the Kansas City metro. Metadata only, no person-level data.">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/ark-civic.css">
</head>
<body>
<header class="ark-head">
  <div class="wrap">
    <img class="crest" src="assets/portal-crest.svg" alt="" width="60" height="60">
    <p class="eyebrow">Archive of Recorded Kondition · civic sub-record</p>
    <h1>Catalogue index</h1>
    <p class="sub">What public data exists here, and whether a person can actually reach it</p>
    <p class="meta">{len(ds):,} records · {len(by_source)} catalogues · captured {gen[:10]}</p>
  </div>
</header>

<main class="wrap">
  <section>
    <p class="lede">Every record below is <strong>held in this repository</strong>. The page makes no
    request to any third party when it loads. If every upstream endpoint were withdrawn tomorrow,
    this index would still resolve and still show what existed, when it was captured, and where it
    used to live.</p>
    <div class="callout">
      <p><strong>Metadata only. No dataset contents are mirrored here.</strong></p>
      <p>This index records what a dataset is, who publishes it, and how it can be reached. It does
      not contain the records inside any dataset. {len(person)} datasets carry terms indicating
      person-level content — arrests, citations, calls for service, ownership, court, payroll. Those
      are indexed as existing and marked <em>never-mirror</em>. The flag is a stop condition, not a
      judgement that the publisher was wrong to publish.</p>
    </div>
    <div class="stat-row">
      <div class="stat"><span class="n">{len(ds):,}</span><span class="l">records held</span></div>
      <div class="stat"><span class="n">{machine:,}</span><span class="l">machine-reachable</span></div>
      <div class="stat"><span class="n">{len(lenexa)}</span><span class="l">Lenexa-specific</span></div>
      <div class="stat"><span class="n">{len(person)}</span><span class="l">never-mirror</span></div>
    </div>
  </section>

  <section>
    <h2>Search the index</h2>
    <div class="controls">
      <input id="q" type="search" placeholder="Search titles, publishers, descriptions…" aria-label="Search the catalogue">
      <select id="src" aria-label="Filter by catalogue">
        <option value="">All catalogues</option>
        {''.join(f'<option value="{html.escape(s)}">{html.escape(s)} ({n})</option>' for s, n in by_source.most_common())}
      </select>
      <label class="chk"><input type="checkbox" id="lx"> Lenexa only</label>
      <label class="chk"><input type="checkbox" id="mr"> Machine-reachable only</label>
    </div>
    <p id="count" class="count"></p>
    <div id="results" class="results"></div>
    <p id="more" class="more"></p>
  </section>

  <section>
    <h2>Provenance</h2>
    <p>Upstream snapshots are kept in <code>catalog/raw/</code> exactly as received. The full
    normalised record, including fields not shown above, is in
    <a href="catalog/catalog.json">catalog.json</a>. Generation is reproducible from
    <a href="catalog/ingest.py">ingest.py</a>.</p>
    <p>One attribution error was made and corrected during the first build: 8,110 hosted services
    were pulled from an ArcGIS organisation assumed to be Johnson County. Verification against the
    portal API showed the organisation was the University of Wisconsin–Madison, and the records were
    student coursework. They were removed before publication. Recorded in
    <a href="catalog/PROVENANCE.md">PROVENANCE.md</a> rather than quietly dropped, because a
    catalogue that hides its own corrections cannot be audited.</p>
    <p><a href="index.html">← Back to the civic-condition record</a></p>
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
const DATA = {rows_json};
const q=document.getElementById('q'), src=document.getElementById('src'),
      lx=document.getElementById('lx'), mr=document.getElementById('mr'),
      out=document.getElementById('results'), cnt=document.getElementById('count'),
      more=document.getElementById('more');
let limit=100;
function esc(s){{return String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));}}
function match(){{
  const term=q.value.trim().toLowerCase(), s=src.value;
  return DATA.filter(d=>{{
    if(s && d.s!==s) return false;
    if(lx.checked && !d.x) return false;
    if(mr.checked && !d.r) return false;
    if(!term) return true;
    return (d.t+' '+d.p+' '+d.d+' '+d.s).toLowerCase().includes(term);
  }});
}}
function render(){{
  const m=match();
  cnt.textContent = m.length.toLocaleString()+' of '+DATA.length.toLocaleString()+' records';
  out.innerHTML = m.slice(0,limit).map(d=>`
    <article class="rec${{d.f.length?' flagged':''}}">
      <h3><a href="${{esc(d.u)}}" rel="noopener">${{esc(d.t)}}</a></h3>
      <p class="rec-meta">${{esc(d.p)}} · ${{esc(d.s)}}${{d.m?' · updated '+esc(d.m):''}}</p>
      ${{d.d?`<p class="rec-desc">${{esc(d.d)}}</p>`:''}}
      <p class="tags">
        ${{d.r?'<span class="tag ok">machine-reachable</span>':'<span class="tag no">page only</span>'}}
        ${{d.x?'<span class="tag lx">Lenexa</span>':''}}
        ${{d.f.length?'<span class="tag flag">never-mirror: '+d.f.map(esc).join(', ')+'</span>':''}}
        ${{(d.fmt||[]).filter(Boolean).map(f=>'<span class="tag fmt">'+esc(f)+'</span>').join('')}}
      </p>
    </article>`).join('');
  more.textContent = m.length>limit ? 'Showing first '+limit+'. Narrow the search to see more.' : '';
}}
[q,src,lx,mr].forEach(e=>e.addEventListener('input',()=>{{limit=100;render();}}));
render();
</script>
</body>
</html>
"""
open(os.path.join(ROOT, "catalog.html"), "w").write(page)
print(f"CATALOG.md and catalog.html written · {len(ds)} records · {len(rows_json)/1024:.0f} KB inline")
