# ARK-CIVIC · Lock-in register

**Captured:** 2026-07-25T20:50:25Z
**Blocked:** 251 datasets · **schema-only:** 812 · **withheld by canon:** 79

A wall that is named is a finding. A wall that is silently skipped is a lie by
omission. Every dataset this record could not pull is listed here with the exact
reason, and with who can remove it.

**Filed against instruments, never people.** Every entry below describes a
publishing arrangement, a format decision, or an access configuration. None of it
is a judgement about the competence or intent of anyone maintaining these systems.
Most of these conditions are inherited from procurement and platform defaults that
the people operating them did not choose.

## Blocked — reasons

| Reason | Datasets | Who can remove it |
|---|---:|---|
| no distribution offers a machine-readable format | 97 | publisher — The record carries only a landing page — a description of data with no download and no API. Removable by the publisher at no cost by attaching a distribution to the existing record. |
| the record is an application or viewer, not a dataset | 92 | publisher — The record points at a map viewer, story map, or application page rather than a dataset. The data behind the viewer exists in a service; only the viewer is catalogued. Removable by the publisher by listing the underlying layer alongside the app. |
| HTTP 400 — the data API rejects the record | 27 | publisher — A Socrata record holding a document or file attachment rather than a table; the data API rejects it. The document itself is reachable through the portal page. Removable by publishing the underlying figures as a table beside the document. |
| no machine-readable distribution - viewer or application only | 12 | publisher — Published as a map viewer or app. The data behind it exists in a service; only the viewer is exposed. Removable by the publisher by sharing the underlying layer. |
| HTTP 403 — anonymous access refused | 10 | publisher — The endpoint exists and refuses anonymous access. Removable by the publisher's access configuration, or by a credential the public does not hold. |
| service error: Service IMAGERY_STATEWIDE/FSA_NAIP_N_CIR/ImageServer not started  | 6 | publisher — Cause recorded verbatim from the endpoint. |
| service error: Layer not found | 6 | publisher — The catalogue record points at a layer index that no longer exists in the service. Removable by the publisher by repairing the catalogue entry. |
| payload exceeded this record's transfer cap | 1 | this record — Not a wall — this record's own transfer cap stopped the download. |

## Blocked by publisher

| Publishing authority | Blocked | Total indexed | Share blocked |
|---|---:|---:|---:|
| Kansas Data Access & Support Center | 178 | 621 | 28% |
| Mid-America Regional Council | 51 | 670 | 7% |
| City of Lenexa, Kansas | 12 | 54 | 22% |
| City of Kansas City, Missouri | 10 | 351 | 2% |

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


## Schema-only — reasons

These are reachable. The structure and the row count are held; the contents are not.

| Reason | Datasets |
|---|---:|
| repository size budget reached | 419 |
| endpoint refused a count query | 134 |
| N rows exceeds the N mirror cap | 71 |
| N features exceeds the N mirror cap | 70 |
| endpoint is a service rootN not a layer | 69 |
| service exposes no layers or tables | 24 |
| reached, contents not mirrored | 16 |
| download contained zero features | 4 |
| dataset is empty | 3 |
| payload exceeds per-file cap | 1 |
| layer is empty | 1 |

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
in the 1,755 records indexed. The asymmetry is not deliberate; it follows
from GIS platforms emitting APIs by default while document systems do not.
*Removable by publishing the documents through any system with a feed.*

**CMN-4 · The open-meetings floor is opt-in.** KOMA (K.S.A. 75-4317 et seq.)
requires no agenda, no minutes, and no posted notice. Where a Kansas public body
publishes those things, it is a local choice that a future body can reverse without
violating any statute. *Removable only by the Legislature.*

## Withheld by canon — not a lock-in

79 datasets were reachable and were deliberately not requested. This is
the privacy invariant operating as designed, and it is recorded here so the count is
never mistaken for a wall imposed from outside. It is a wall this record imposes on
itself.

| Dataset | Publisher | Screen |
|---|---|---|
| $10M Demolition List | City of Kansas City, Missouri | `case` |
| 1980 Census Detailed Census Tract Data | City of Kansas City, Missouri | `ownership` |
| 2010 Census Detailed Block Data | City of Kansas City, Missouri | `ownership` |
| 2010 Census/ACS Basic Block Group Data | City of Kansas City, Missouri | `ownership` |
| 2010 Census/ACS Detailed Block Group Data | City of Kansas City, Missouri | `ownership` |
| 311 Cases by Issue Type | City of Kansas City, Missouri | `case` |
| 311 Cases-Main & Broadway CID | City of Kansas City, Missouri | `case` |
| 911 Calls For Service | City of Kansas City, Missouri | `calls for service` |
| Animal Control ALL CASES | City of Kansas City, Missouri | `case` |
| Animal Services Cases | City of Kansas City, Missouri | `case` |
| Annual Illegal Dumping Cases Resolved for Story | City of Kansas City, Missouri | `case` |
| Archive Kansas GIS Data | Kansas Data Access & Support C | `case` |
| Average Days Closed for Closed Cases | City of Kansas City, Missouri | `case` |
| City of KCMO Employee Demographics | City of Kansas City, Missouri | `employee` |
| Count of Open 311 Cases by Department and Issue Type | City of Kansas City, Missouri | `case` |
| COVID-19 Case & Death Trends by Date | City of Kansas City, Missouri | `case` |
| COVID-19 Data by ZIP Code | City of Kansas City, Missouri | `case` |
| COVID-19 Data by ZIP Code | City of Kansas City, Missouri | `case` |
| COVID-19 Overall Trends - Cases & Deaths | City of Kansas City, Missouri | `case` |
| Crime Watch | Johnson County AIMS | `crime` |
| Crimes by Type by 1980 Block - 2000 to 2006 | City of Kansas City, Missouri | `crime` |
| Dangerous Building Cases Remaining Open by Creation Year | City of Kansas City, Missouri | `case, court` |
| Dangerous Buildings Heat Map | City of Kansas City, Missouri | `case, court` |
| Dangerous Buildings List | City of Kansas City, Missouri | `case, court` |
| Dangerous Buildings Map by ZIP | City of Kansas City, Missouri | `case, court` |
| Development_Activity_Type | City of Lenexa, Kansas | `case` |
| Discovering Water Through Exploration | Kansas Data Access & Support C | `student` |
| Hazardous Materials and EHS Facilities (public) | Mid-America Regional Council | `employee` |
| House of Representatives Districts (2025 Roster) | Kansas Data Access & Support C | `roster` |
| Interactive Kansas Streambank Assessment Map | Kansas Data Access & Support C | `case` |
| KanDrive | Kansas Data Access & Support C | `incident` |
| Kansas City Crime (NIBRS) Summary | City of Kansas City, Missouri | `crime, incident, student` |
| Kansas Conservation Assistance Directory | Kansas Data Access & Support C | `case` |
| Kansas Senate Districts (2025 Roster) | Kansas Data Access & Support C | `roster` |
| KBS Report #197 – Milford Sediment Coring (2020) | Kansas Data Access & Support C | `citation` |
| KBS Report #198 – Marion & Sebelius Sediment Coring (2020) | Kansas Data Access & Support C | `citation` |
| KBS Report #202 – Kanopolis & Webster Sediment Coring (2021) | Kansas Data Access & Support C | `citation` |
| KBS Report #207 – Lovewell & Perry Sediment Coring (2021) | Kansas Data Access & Support C | `citation` |
| KBS Report #211 – Tuttle Creek & Waconda Sediment Coring (2023) | Kansas Data Access & Support C | `citation` |
| KBS Report #214 – Kirwin & Wilson Sediment Coring (2024) | Kansas Data Access & Support C | `citation` |
| KBS Report #218 – Clinton & Cedar Bluff Sediment Coring (2024) | Kansas Data Access & Support C | `citation` |
| KCMO Blood Lead Levels | City of Kansas City, Missouri | `patient` |
| KCMO by Race | City of Kansas City, Missouri | `employee` |
| KCMO Employee Count Over Time | City of Kansas City, Missouri | `employee` |
| KCMO Employee Count Over Time | City of Kansas City, Missouri | `employee` |
| KCMO Employees by Race and Gender | City of Kansas City, Missouri | `employee` |
| KCMO Employees by Race and Gender | City of Kansas City, Missouri | `employee` |
| KCPD Calls for Service 2023 | City of Kansas City, Missouri | `calls for service` |
| KCPD crime 2019 by zip code | City of Kansas City, Missouri | `crime, incident, warrant` |
| KCPD Crime Data 2010 Final | City of Kansas City, Missouri | `crime` |

*29 further withheld records in `pull_status.json`.*

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
