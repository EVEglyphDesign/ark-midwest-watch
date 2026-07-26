# Kansas Open Records Act request — Johnson County AIMS geospatial records

**Draft for signature. Not sent.**

**To:** Freedom of Information Officer, Johnson County, Kansas
Office of the County Manager
111 S. Cherry, Suite 3300
Olathe, Kansas 66061
Telephone 913-715-5000

**Copy to:** Automated Information Mapping System (AIMS), Department of Technology and Innovation — Mapper of the Day, mapper@jocogov.org, 913-715-1600

**From:** Dany Theriault
[street address]
[city, state, ZIP]
[email] · [telephone]

**Date:** [date of sending]

**Subject:** Request under the Kansas Open Records Act, K.S.A. 45-215 *et seq.*, for copies of existing geospatial records in the electronic form in which they are maintained

---

## 1. Statutory basis

This is a request for copies of existing public records under the Kansas Open Records Act, K.S.A. 45-215 *et seq.* It is addressed to the county's Freedom of Information Officer, whom the county's own Open Records page identifies as the County Manager ([Johnson County Open Records](https://www.jocogov.org/department/treasury-taxation-and-vehicles/register-deeds/open-records)).

Three points frame everything below.

**This request asks for copies, not for work.** KORA does not require an agency to create a record, compile a report, or answer questions ([Kansas Attorney General, KORA FAQ](https://www.ag.ks.gov/divisions/administration/open-government/kora-faq)). Every item below already exists as a maintained dataset or a maintained document. Nothing here asks the county to build anything.

**The electronic form is the form requested.** Digitalised information meets the definition of a public record, and it must be provided in the form requested where the agency has the capability of producing it in that form ([Kansas Legislative Research Department, KORA briefing](https://klrd.gov/publications/briefing-book-2021/kansas-open-records-act/)). AIMS maintains these records in ArcGIS. AIMS already exports them to shapefile, DWG, DXF and DGN through its own ordering application ([AIMS Data Prices](https://aims.jocogov.org/AIMSData/DataPrices.aspx)). The capability is not in question.

**Fees may not exceed actual cost.** KORA permits reasonable fees, and reasonable means not exceeding the actual cost to the agency of providing the record ([Kansas Attorney General, KORA FAQ](https://www.ag.ks.gov/divisions/administration/open-government/kora-faq); K.S.A. 45-219(c)). The county's own Open Records page states the same standard. Section 5 of this request addresses fees directly and asks for the itemised basis of any amount charged.

## 2. Records requested — geospatial datasets

For each item, a single countywide copy of the current dataset, in shapefile or file geodatabase, or GeoJSON if more convenient to produce, in the projection in which it is maintained. Where a dataset is available free of charge through the AIMS Free Data page, that free copy satisfies the item and no further action is needed on it.

**A. Property and cadastral**

1. The countywide parcel dataset, geometry and attributes, **excluding all owner-name fields** — see the privacy limitation at section 6.
2. Plat boundaries, countywide.
3. Subdivisions, countywide.
4. Scanned recorded plats, or, if the images cannot reasonably be copied in bulk, the index of recorded plats with the identifier used by the county's plat search.

**B. Planimetric and elevation**

5. Planimetrics — building footprints, pavement edge, and related captured features — countywide.
6. Topography and contours, countywide.
7. Digital elevation and surface models, countywide, in the resolution and vintage maintained.

**C. Infrastructure and transportation**

8. Street centrelines, countywide.
9. Traffic counts, countywide.
10. Right-of-way document index and geometry.
11. Johnson County Wastewater sewer mains and manholes, countywide.
12. Countywide zoning.
13. Address points, countywide.

**D. Imagery**

14. The most recent countywide orthophotography, at the resolution maintained. If a countywide copy is impractical to transfer, please state the medium and the actual cost of that medium, and I will arrange for delivery on hardware I provide or pay the media cost.

## 3. Records requested — the arrangement itself

These are administrative records, not datasets.

15. The county's written procedures for requesting access to and obtaining copies of public records, and its fee schedule, as required to be provided on request by K.S.A. 45-220(f). The Open Records page refers to a "Charges and Fees" document that does not appear to be published anywhere on the county website; this item requests that document.
16. The name and title of the person currently designated as the county's Freedom of Information Officer under K.S.A. 45-226, and the name and title of the official custodian for AIMS records.
17. Records sufficient to show the **cost basis** for the unit prices published on the AIMS Data Prices page — for example $0.48 per parcel for property data, $0.24 per parcel for planimetrics and topography, $5.00 per square mile for census, plat boundary, subdivision and traffic-count data, and $30.00 per quarter square mile for current photography ([AIMS Data Prices](https://aims.jocogov.org/AIMSData/DataPrices.aspx)). This item asks for the cost study, rate derivation, board or administrative action, memorandum, or other existing record on which those unit prices rest.
18. Any resolution, order, policy, or administrative action of the Board of County Commissioners or the County Manager establishing or approving the AIMS data pricing schedule, and any subsequent amendment.
19. Records showing annual revenue received through the Digital Data Request application, and the fund into which that revenue is deposited, for fiscal years 2021 through 2026.
20. The standard data licence, use agreement, or terms of use presented to a purchaser through the Digital Data Request application, and the equivalent agreement presented to Government and Utility data partners.
21. Any existing record — study, proposal, staff report, vendor quotation, or decision memorandum — concerning publication of a county open-data catalogue or DCAT-format metadata feed, including any decision not to publish one.

## 4. Why the datasets in section 2 are requested despite being visible online

Johnson County's ArcGIS services are publicly reachable, and this request is not made in ignorance of them. It is made because reachable is not the same as obtainable.

An ArcGIS service returns one page of records per query and does not state that more exist. On 25 July 2026, an automated read of the county's public services at `maps.jocogov.org` returned the following, where the second number is the layer's own reported record count:

| Layer | Returned in one response | Layer's own count |
|---|---:|---:|
| Parcels | 2,000 | 10,419 |
| JCW Locaters | 2,000 | 14,949 |
| Communication Towers | 1,000 | 8,660 |
| Zoning (Countywide) | 3,000 | 7,760 |
| Address points (MSNaddress) | 2,000 | 6,295 |
| Streams and Ponds | 1,000 | 5,446 |
| Right-of-Way documents | 1,000 | 3,458 |
| Special Assessments | — | 165,063 |
| JCW Sewer Manholes | — | 64,045 |
| JCW Sewer Mains | — | 63,197 |

Fifteen distinct layers were capped in this way. A member of the public reading these services receives a fraction of each record and no notice that the remainder exists. The county's own metadata is candid about where the rest lives: data is "available to purchase through Digital Data Request (DDR) application ... for a fee on a parcel or section basis" ([Johnson County AIMS metadata, as republished by the City of Olathe](https://arcgis.olatheks.org/arcgis/rest/services/Basemap/Basemap_Standard/MapServer/16/metadata)).

I am not alleging that this is improper. It is how the platform behaves by default and how the ordering application was designed. I am stating the practical result plainly: for these datasets, the public interface is a sample and the complete record is behind a price. That is why this request is made under KORA rather than through the ordering application.

## 5. Fees

I ask the county to treat this as a KORA request for copies of existing electronic records, and to apply the KORA standard — actual cost — rather than the AIMS per-parcel and per-square-mile schedule, which is a price for a product rather than a statement of what a copy costs the county to produce.

The distinction matters and I want to state it without heat. A per-parcel unit price scales with the size of the dataset. The actual cost of copying a maintained dataset does not: it is the staff time to run an export the county already knows how to run, plus media. For a countywide file, those two figures diverge by orders of magnitude. K.S.A. 45-219(c) speaks to the second figure.

Accordingly:

- Please provide an **itemised written estimate before any chargeable work begins**, showing the classification and hourly rate of each person whose time is billed, the number of hours, and any media or delivery cost.
- Please charge the **lowest-cost staff classification reasonably capable** of running the export.
- **Do not incur charges exceeding \$[cap, e.g. 100] without contacting me first.** If the estimate exceeds that figure, I would welcome a conversation about narrowing the request — by dataset, by geography, or by dropping the imagery in section 2 item 14, which I expect to be the costliest item and the least central.
- Where a dataset is already offered free of charge on the [AIMS Free Data](https://aims.jocogov.org/AIMSData/FreeData.aspx) page, simply say so and I will take the free copy. I do not want the county to spend staff time producing something it already publishes.
- If the county maintains that the AIMS schedule rather than the KORA standard governs, please say so in writing and identify the provision of law relied on, so that the position is on the record rather than inferred.

I am willing to pay lawful fees. I am asking that they be the fees the statute allows.

## 6. Privacy limitation, stated by the requester

This request **excludes person-level records**, and that exclusion is mine, not something the county needs to argue for.

- No owner names, no mailing addresses of owners, no taxpayer identifiers. For the parcel dataset in item 1, geometry, parcel identifier, and physical-characteristic attributes are sufficient; please redact or drop name and owner-address fields before delivery, and bill me for that redaction time if any is required.
- No law-enforcement records of any kind. No calls for service, no incident, arrest, booking, citation, or case records. Nothing in section 2 or 3 touches them, and none is wanted.
- No individual utility-customer records. Items 11 and 13 concern network and address geometry, not accounts or occupants.

**Certification under K.S.A. 45-220(c):** I certify that I will not use any name or address obtained from these records to solicit sales of services or property to any person, and I will sign the county's standard certification to that effect on request.

The purpose of the request is to hold a durable public copy of the county's civic and infrastructure geography, so that the record of what the county looks like does not depend on any single vendor platform remaining online. The records will be published as received, subject to the exclusions above.

## 7. Form of response

- Electronic delivery is preferred: a download link, or a transfer to cloud storage I will nominate. If the volume requires physical media, say so and I will provide a drive or pay the media cost.
- Please respond within three business days as provided by K.S.A. 45-218, even if the response is that additional time is needed. The county's Open Records page commits to exactly this.
- If any item is denied in whole or in part, I request a written statement of the grounds, citing the specific provision of law relied on, as provided by KORA.
- If a record does not exist, please say that it does not exist. That answer is useful to me and it costs the county nothing. An item recorded as "no such record" will be published as exactly that, and not as a refusal.

## 8. A note on tone, offered in good faith

Nothing in this request implies wrongdoing by anyone at AIMS or in the County Manager's office. Johnson County publishes a substantial amount of geography free of charge — the AIMS Free Data page runs to well over a hundred datasets across administration, elections, environment, flood, schools, survey and transportation — and that is more than many counties do. The conditions this request pushes against are inherited ones: a platform that pages its answers by default, and a cost-recovery schedule built for engineering firms buying a subdivision's worth of parcels rather than for a resident asking for a copy of the whole.

Those are arrangements, not attitudes. They can be changed by decision, and the people who would have to run the export are not the people who set the price.

**Requested by:**

Dany Theriault
[signature]
[date]

---

*Drafting note for the sender, not part of the request: this document is a draft for your signature. Fill the bracketed fields, choose the fee cap in section 5, and decide whether to send by mail to the County Manager's office, by email to the AIMS Mapper of the Day with the County Manager copied, or both. The county's Open Records page states no email address and no submission form, so posting a signed paper copy to 111 S. Cherry, Suite 3300 and emailing a scan to mapper@jocogov.org creates the cleanest record of the date received. Nothing in this request touches Lenexa Police Department or City of Lenexa records, and it does not disturb the standing hold on that lane.*

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
