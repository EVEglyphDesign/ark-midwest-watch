# Catalogue provenance

Every source in this index, why it is here, and what was rejected.

## Captured

| Catalogue | Authority | Endpoint | Records | Verified how |
|---|---|---|---:|---|
| MARC Open Data | Mid-America Regional Council | `opendata-marc-gis.hub.arcgis.com/api/feed/dcat-us/1.1.json` | 670 | DCAT-US 1.1 conformant, publisher name in every record |
| Kansas DASC | Kansas Data Access & Support Center | `hub.kansasgis.org/api/feed/dcat-us/1.1.json` | 621 | DCAT-US 1.1 conformant |
| KCMO Open Data | City of Kansas City, Missouri | `data.kcmo.org/api/views.json` | 351 | Socrata catalogue API on the city's own domain |
| JoCo AIMS | Johnson County AIMS | `maps.jocogov.org/arcgis/rest/services` | 59 | County-owned domain, enumerated root + 8 folders |
| Lenexa hosted | City of Lenexa, Kansas | `services.arcgis.com/rQNf5tVFXFoS6EhP` | 3 | **Org id verified**: portal API returns `name: "Lenexa, Kansas"` |
| Lenexa published items | City of Lenexa, Kansas | AGOL item search, owner allow-list | 51 | `owner:LenexaEST` or a `lenexa.com` identity only |

## Rejected

**University of Wisconsin–Madison, 8,110 hosted services.** The first build pulled
ArcGIS organisation `HRPe58bUyBqyyiCt` and attributed it to Johnson County. It is
not Johnson County. The portal API returns `name: "University of Wisconsin-Madison"`,
and the contents were student GIS coursework — `(GEOG170)HW3_tonyxiao`,
`__Bike_Share_Stations__`, Madison bike paths. All 8,110 records were removed
before publication.

The org id had been carried forward from an earlier research pass without being
checked against the portal API. It would have inflated the index more than fivefold
and attributed a university's coursework to a county government. Both would have
been visible to any reader who clicked a link, and the credibility of every other
record here would have gone with it.

Recorded rather than quietly dropped: **a catalogue that hides its own corrections
cannot be audited.** `ingest_agol()` now carries the verification requirement in its
docstring.

**Endpoints that do not exist.** Probed and returned no DNS or 404, recorded so no
future agent re-probes them: `gis.lenexa.gov`, `maps.lenexa.com`, `opendata.kcmo.org`,
`data.kansas.gov`, `opendata.jocogov.org`, `data.jocogov.org`,
`data-jocogov.opendata.arcgis.com`, `aims-jocogov.opendata.arcgis.com`.

Consequence worth recording: **Johnson County publishes no DCAT or open-data hub feed
of its own.** Its data is reachable only by enumerating an ArcGIS REST directory, which
requires knowing that the directory exists and how to walk it. Bulk access remains a
paid Digital Data Request. This is a `CMN` register condition — filed against the access
arrangement, not against the people who maintain the servers, which they do well.

## Privacy screen

Applied to title, description, and keywords of every record. 79 datasets matched
person-level or address-level terms and are marked `never-mirror`. They remain
indexed — the record states that they exist — but no contents are pulled and no
person-level field enters this repository.

Included in that set is the City of Lenexa `HubCallsForService` feature server, which
backs the public Calls for Service map. It is indexed and deliberately not mirrored.

The screen is deliberately over-inclusive. A false positive costs a human read; a false
negative costs the invariant, which is worth −7 under the sealed canon and is not
recoverable by apology.

## Reproducing

```bash
python3 catalog/ingest.py         # re-pull; delete a file in catalog/raw/ to force refresh
python3 catalog/build_surface.py  # regenerate CATALOG.md and catalog.html
```

`catalog/raw/` holds each upstream response exactly as received.

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
