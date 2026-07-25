#!/usr/bin/env python3
"""
ARK-CIVIC catalog ingest.

Pulls the machine-readable dataset catalogues that cover Lenexa, Johnson County,
and the Kansas City metro into this repository, so the record does not depend on
a third party keeping an endpoint alive.

PRIVACY INVARIANT (CANON-ARK-CIVIC-CONDITION.md §2, inherited from the sealed
ARK canon §7): this ingests CATALOGUE METADATA ONLY - the description of what a
dataset is, who publishes it, and how it can be reached. It never downloads the
records inside a dataset. No person-level data enters this repository, and
datasets flagged as person-level are recorded as existing and deliberately not
mirrored.

Run:  python3 catalog/ingest.py
Out:  catalog/raw/*.json         upstream snapshots, unmodified
      catalog/catalog.json       normalised union
      catalog/catalog.min.json   surface payload
      catalog/CATALOG.md         human-readable index
"""

import json, os, re, urllib.request, urllib.parse, urllib.error, datetime, hashlib, concurrent.futures

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
os.makedirs(RAW, exist_ok=True)
UA = "ARK-CIVIC/1.0 (+https://eveglyphdesign.github.io/ark-midwest-watch/) civic-condition record"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get(url, timeout=180):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def cached(name, url, timeout=180):
    p = os.path.join(RAW, name)
    if os.path.exists(p) and os.path.getsize(p) > 200:
        return json.load(open(p))
    b = get(url, timeout)
    open(p, "wb").write(b)
    return json.loads(b)


# ---------------------------------------------------------------- privacy screen
# Terms that indicate a dataset may carry person-level or address-level records.
# A hit does NOT remove the dataset from the index - the index records that it
# exists. It marks it never-mirror and forces a human read before any use.
PERSON_TERMS = [
    "arrest", "booking", "inmate", "offender", "warrant", "citation", "ticket",
    "incident", "calls for service", "crime", "police report", "case",
    "voter", "registrant", "juror", "licensee", "permit holder", "employee",
    "salary", "payroll", "roster", "patient", "student", "resident name",
    "owner name", "ownership", "parcel owner", "tax roll", "delinquen",
    "restraining", "sex offender", "probation", "court", "docket",
]
SENSITIVE_TERMS = [
    "license plate", "plate reader", "alpr", "flock", "surveillance",
    "camera", "drone", "facial", "biometric", "cell site", "stingray",
]


def screen(title, desc, keywords):
    hay = " ".join([title or "", desc or "", " ".join(keywords or [])]).lower()
    person = sorted({t for t in PERSON_TERMS if t in hay})
    sens = sorted({t for t in SENSITIVE_TERMS if t in hay})
    return person, sens


def clean(s, limit=600):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", str(s))
    s = re.sub(r"&nbsp;?", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


records = []


def add(**kw):
    kw.setdefault("keywords", [])
    p, s = screen(kw.get("title"), kw.get("description"), kw.get("keywords"))
    kw["person_flags"] = p
    kw["sensitive_flags"] = s
    kw["mirror_policy"] = "never-mirror" if p else "metadata-only"
    kw["id"] = hashlib.sha1(
        (kw.get("source", "") + "|" + (kw.get("title") or "") + "|" + (kw.get("access_url") or "")).encode()
    ).hexdigest()[:12]
    records.append(kw)


# ---------------------------------------------------------------- DCAT-US 1.1
def ingest_dcat(fname, url, source, authority, coverage):
    d = cached(fname, url)
    for ds in d.get("dataset", []):
        dist = ds.get("distribution", []) or []
        fmts = sorted({(x.get("format") or x.get("mediaType") or "").strip() for x in dist if x.get("format") or x.get("mediaType")})
        access = ""
        for x in dist:
            if (x.get("format") or "").lower() in ("geojson", "csv", "json", "geoservice"):
                access = x.get("accessURL") or x.get("downloadURL") or ""
                break
        if not access:
            access = ds.get("landingPage") or (dist[0].get("accessURL") if dist else "")
        machine = any((x.get("format") or "").lower() in ("geojson", "csv", "json", "geoservice", "api", "shapefile") for x in dist)
        add(
            source=source, authority=authority, coverage=coverage,
            title=clean(ds.get("title"), 300),
            description=clean(ds.get("description")),
            publisher=clean((ds.get("publisher") or {}).get("name"), 160),
            keywords=[clean(k, 60) for k in (ds.get("keyword") or [])][:12],
            issued=(ds.get("issued") or "")[:10],
            modified=(ds.get("modified") or "")[:10],
            license=clean(ds.get("license"), 200) or "not stated",
            landing=ds.get("landingPage") or "",
            access_url=access,
            formats=fmts,
            machine_readable=machine,
            access_barrier="none - open endpoint" if machine else "human-readable page only",
        )


# ---------------------------------------------------------------- Socrata
def ingest_socrata(fname, base, source, authority, coverage):
    d = cached(fname, base + "/api/views.json?limit=5000")
    for v in d if isinstance(d, list) else []:
        if v.get("assetType") in ("story", "href", "measure"):
            continue
        vid = v.get("id", "")
        add(
            source=source, authority=authority, coverage=coverage,
            title=clean(v.get("name"), 300),
            description=clean(v.get("description")),
            publisher=clean((v.get("metadata") or {}).get("custom_fields", {}).get("Publishing", {}).get("Department") or authority, 160),
            keywords=[clean(t, 60) for t in (v.get("tags") or [])][:12],
            issued=datetime.datetime.utcfromtimestamp(v["createdAt"]).strftime("%Y-%m-%d") if v.get("createdAt") else "",
            modified=datetime.datetime.utcfromtimestamp(v["rowsUpdatedAt"]).strftime("%Y-%m-%d") if v.get("rowsUpdatedAt") else "",
            license=clean((v.get("license") or {}).get("name"), 200) or "not stated",
            landing=f"{base}/d/{vid}",
            access_url=f"{base}/resource/{vid}.json",
            formats=["JSON", "CSV", "GeoJSON"],
            machine_readable=True,
            access_barrier="none - open SODA API",
        )


# ---------------------------------------------------------------- ArcGIS server
def ingest_arcgis_server(fname, root, source, authority, coverage):
    """Enumerate an ArcGIS REST services directory, including folders."""
    idx = cached(fname, root + "?f=json", timeout=90)
    targets = [("", idx)]
    folders = idx.get("folders", []) or []

    def fetch_folder(f):
        try:
            return f, json.loads(get(f"{root}/{f}?f=json", timeout=60))
        except Exception:
            return f, None

    if folders:
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
            for f, data in ex.map(fetch_folder, folders):
                if data:
                    targets.append((f, data))
    snapshot = {}
    for folder, data in targets:
        snapshot[folder or "(root)"] = data
        for svc in data.get("services", []) or []:
            name = svc.get("name", "")
            stype = svc.get("type", "")
            short = name.split("/")[-1]
            url = f"{root}/{name}/{stype}"
            add(
                source=source, authority=authority, coverage=coverage,
                title=re.sub(r"(?<!^)(?=[A-Z])", " ", short).replace("_", " ").strip(),
                description=f"ArcGIS {stype} published by {authority}. Folder: {folder or 'root'}.",
                publisher=authority,
                keywords=[stype, folder or "root", "arcgis", "gis"],
                issued="", modified="",
                license="not stated",
                landing=url,
                access_url=url + "?f=json",
                formats=["ArcGIS REST", "JSON", "GeoJSON"] if stype == "FeatureServer" else ["ArcGIS REST", "JSON"],
                machine_readable=True,
                access_barrier="none - open REST endpoint",
            )
    json.dump(snapshot, open(os.path.join(RAW, fname.replace(".json", "-full.json")), "w"), indent=1)


# ---------------------------------------------------------------- AGOL hosted
def ingest_agol(fname, url, source, authority, coverage):
    """Enumerate a verified ArcGIS Online organisation's hosted services.

    The org id MUST be confirmed against
    https://www.arcgis.com/sharing/rest/portals/<orgId>?f=json before use.
    An unverified org id was used here once and turned out to belong to a
    university GIS course, not a county. See catalog/PROVENANCE.md.
    """
    d = cached(fname, url, timeout=120)
    for svc in d.get("services", []) or []:
        add(
            source=source, authority=authority, coverage=coverage,
            title=clean(svc.get("name", "").split("/")[-1].replace("_", " "), 300),
            description=clean(svc.get("description") or f"Hosted ArcGIS {svc.get('type','')} published by {authority}."),
            publisher=authority,
            keywords=[svc.get("type", ""), "arcgis online", "hosted"],
            issued="", modified="",
            license="not stated",
            landing=svc.get("url", ""),
            access_url=(svc.get("url", "") + "?f=json") if svc.get("url") else "",
            formats=["ArcGIS REST", "GeoJSON", "JSON"],
            machine_readable=True,
            access_barrier="none - open REST endpoint",
        )


def ingest_agol_items(fname, source, authority, coverage):
    """Items published by City of Lenexa staff accounts on ArcGIS Online.

    Owner allow-list only. An account is included when its name is the city
    org account or ends in a lenexa.com identity. Items owned by consultants,
    universities, or neighbouring cities are excluded even when Lenexa appears
    in the title, because attributing them to the city would be false.
    """
    p = os.path.join(RAW, fname)
    if os.path.exists(p) and os.path.getsize(p) > 200:
        results = json.load(open(p))
    else:
        results, start = [], 1
        while start > 0 and len(results) < 400:
            u = ("https://www.arcgis.com/sharing/rest/search?f=json&num=100&start=%d"
                 "&q=%s" % (start, urllib.parse.quote('owner:LenexaEST OR owner:"lenexa.com"')))
            d = json.loads(get(u, timeout=90))
            results.extend(d.get("results", []))
            start = d.get("nextStart", -1)
        json.dump(results, open(p, "w"), indent=1)

    for r in results:
        owner = (r.get("owner") or "")
        if not (owner == "LenexaEST" or "lenexa.com" in owner.lower()):
            continue
        url = r.get("url") or ""
        add(
            source=source, authority=authority, coverage=coverage,
            title=clean(r.get("title"), 300),
            description=clean(r.get("snippet") or r.get("description") or f"{r.get('type','item')} published by {authority}."),
            publisher=authority,
            keywords=[clean(t, 60) for t in (r.get("tags") or [])][:12] + [clean(r.get("type"), 40)],
            issued=datetime.datetime.fromtimestamp(r["created"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d") if r.get("created") else "",
            modified=datetime.datetime.fromtimestamp(r["modified"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d") if r.get("modified") else "",
            license=clean(r.get("licenseInfo"), 200) or "not stated",
            landing=f"https://www.arcgis.com/home/item.html?id={r.get('id','')}",
            access_url=url,
            formats=[clean(r.get("type"), 40)],
            machine_readable=bool(url) and ("rest/services" in url),
            access_barrier="none - open REST endpoint" if (url and "rest/services" in url) else "viewer or application only",
        )


if __name__ == "__main__":
    print("MARC DCAT ...")
    ingest_dcat("marc-dcat-us-1.1.json",
                "https://opendata-marc-gis.hub.arcgis.com/api/feed/dcat-us/1.1.json",
                "MARC Open Data", "Mid-America Regional Council", "KC metro (9 counties, KS + MO)")
    print("Kansas DASC DCAT ...")
    ingest_dcat("kansas-dasc-dcat-us-1.1.json",
                "https://hub.kansasgis.org/api/feed/dcat-us/1.1.json",
                "Kansas DASC", "Kansas Data Access & Support Center", "State of Kansas")
    print("KCMO Socrata ...")
    ingest_socrata("kcmo-socrata-views.json", "https://data.kcmo.org",
                   "KCMO Open Data", "City of Kansas City, Missouri", "Kansas City, MO")
    print("Johnson County AIMS ArcGIS ...")
    ingest_arcgis_server("joco-arcgis-root.json", "https://maps.jocogov.org/arcgis/rest/services",
                         "JoCo AIMS", "Johnson County AIMS", "Johnson County, KS")
    print("City of Lenexa hosted (org rQNf5tVFXFoS6EhP, verified 'Lenexa, Kansas') ...")
    ingest_agol("lenexa-agol-services.json",
                "https://services.arcgis.com/rQNf5tVFXFoS6EhP/arcgis/rest/services?f=json",
                "Lenexa hosted", "City of Lenexa, Kansas", "Lenexa, KS")
    print("City of Lenexa published items (AGOL item search) ...")
    ingest_agol_items("lenexa-agol-items.json", "Lenexa published items",
                      "City of Lenexa, Kansas", "Lenexa, KS")

    # ---- de-duplicate on access_url
    seen, uniq = set(), []
    for r in records:
        k = (r.get("access_url") or "") + "|" + r.get("title", "")
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)

    lenexa_re = re.compile(r"lenexa", re.I)
    for r in uniq:
        hay = (r["title"] + " " + r["description"] + " " + " ".join(r["keywords"])).lower()
        r["lenexa_specific"] = bool(lenexa_re.search(hay))

    out = {
        "generated": NOW,
        "instance": "midwest-lenexa",
        "record": "ARK-CIVIC catalogue index",
        "privacy": "Catalogue metadata only. No dataset contents ingested. No person-level data in this repository.",
        "count": len(uniq),
        "sources": sorted({r["source"] for r in uniq}),
        "datasets": sorted(uniq, key=lambda r: (r["source"], r["title"].lower())),
    }
    json.dump(out, open(os.path.join(HERE, "catalog.json"), "w"), indent=1)

    slim = [
        {k: r[k] for k in ("id", "source", "authority", "title", "description", "publisher",
                           "modified", "formats", "landing", "access_url", "machine_readable",
                           "access_barrier", "person_flags", "sensitive_flags", "mirror_policy",
                           "lenexa_specific")}
        for r in out["datasets"]
    ]
    json.dump({"generated": NOW, "count": len(slim), "datasets": slim},
              open(os.path.join(HERE, "catalog.min.json"), "w"), separators=(",", ":"))

    print(f"\ntotal {len(uniq)}")
    from collections import Counter
    for s, n in Counter(r["source"] for r in uniq).most_common():
        print(f"  {n:5d}  {s}")
    print("  person-flagged:", sum(1 for r in uniq if r["person_flags"]))
    print("  sensitive-flagged:", sum(1 for r in uniq if r["sensitive_flags"]))
    print("  lenexa-specific:", sum(1 for r in uniq if r["lenexa_specific"]))
