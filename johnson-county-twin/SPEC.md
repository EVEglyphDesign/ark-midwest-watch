# Johnson County Commons Twin — Technical Specification & Bill of Materials

Document ID: EgD-PROP-JCT-001-SPEC · Key ID: EgD-KEY-2026-07
Operator: Dany Thériault, EVEglyphDesign (EgD) · Recipient: Jeff Eden
This specification implements the [source brief](./BRIEF.md) and does not contradict it.

## 1. Hardware tier

Strix Halo class mini PC, **Ryzen AI 9 HX 470** tier, **32 GB** unified memory,
~150 × 150 × 43 mm, under 120 W sustained, rated for 24/7 duty, reachable only over
Tailscale (no public inbound ports). This is an appliance form factor, not a workstation
and not a rack.

**Why 32 GB, not 128 GB.** The workload — indexing, classification, and drafting — sits in
the 14–32B parameter class, not dense 70B, so 32 GB unified memory serves it comfortably.
128 GB Strix Halo is capacity technology for 70B-class models at roughly 5 tok/s, priced
for that different job, and currently inflated to **$3,000–3,300** by the ongoing memory
shortage. A same-day check confirms the spread: the **MINISFORUM AI X1 Pro-470** (HX 470,
32 GB DDR5, 1 TB NVMe) lists at **$1,359** ([TerminalBytes](https://terminalbytes.com/best-mini-pc-for-local-llm-2026/)),
the **GEEKOM A9 Max** 32 GB/2 TB configuration runs **$1,399–$1,699** at retail
([GEEKOM](https://www.geekompc.com/geekom-a9-max-mini-pc/),
[Best Buy](https://www.bestbuy.com/product/geekom-a9-max-ai-mini-pc-amd-ryzen-ai-9-hx-470-radeon-890m-32gb-ddr5-ram-2tb-ssd-windows-11-pro-pre-installed-silver-black/J3GW6689GL)),
and 128 GB boxes that launched near $1,999 now clear $3,299 on the same listings
([TerminalBytes](https://terminalbytes.com/best-mini-pc-for-local-llm-2026/)). 32 GB is
the correct tier at roughly a third of the cost.

## 2. Bill of materials

| Line | Item | Cost (USD) |
|---|---|---|
| 1 | Strix Halo mini PC, Ryzen AI 9 HX 470, 32 GB DDR5 ([MINISFORUM AI X1 Pro-470](https://terminalbytes.com/best-mini-pc-for-local-llm-2026/)) | $1,359 |
| 2 | NVMe expansion, 4 TB tier (data-layer headroom beyond onboard SSD) | $280 |
| 3 | Tailscale connectivity (fixed node, no subscription tier required at this scale) | $0 |
| 4 | Enclosure hardening, cabling, PoE/power conditioning for 24/7 duty | $150 |
| 5 | Build labor — appliance assembly, burn-in, thermal validation | $600 |
| 6 | ARK Midwest Watch mirror build — ingest, dedupe, provenance tagging (2,756,484 records, 89 layers) | $4,200 |
| 7 | Spatial layer composition — 3D coordinate registration across civic/AIMS sources | $3,800 |
| 8 | Anonymised presence filter — edge model tuning and integration against existing camera feeds | $3,500 |
| 9 | Arrival-gated information model — geofencing, on-arrival recommendation logic | $2,200 |
| 10 | Concentric safety beacon system — zone logic, safe-word trigger, stamping pipeline | $2,600 |
| 11 | Payment path integration and charity routing configuration | $900 |
| 12 | Licence — non-exclusive, non-transferable, EgD IP (filter, arrival model, beacon design, payment routing) | included in fixed price |
| **Hardware + NVMe subtotal** | | **$1,639** |
| **Build, software, and licence subtotal** | | **$18,361** |
| **Total (fixed price)** | | **$20,000** |

Margin arithmetic: the $20,000 fixed price returns roughly **$1,639 in metal** and
**$18,361 in build, integration, and licence** — over 91% licence/build to under 9%
hardware. The price is for the finished, sealed system and the right to run it, not the
box it ships in. Jeff Eden could buy the mini PC himself for under $1,400; the mirror,
the spatial composition, the filter, and the licence are what he cannot buy elsewhere.

## 3. Data layer

A full local mirror of the [ARK Midwest Watch](https://github.com/EVEglyphDesign/ark-midwest-watch)
civic holdings for Lenexa and Johnson County: the corrected baseline of **2,756,484 held
records** across **89 partial layers**, held on disk — not linked, not proxied — so an
upstream shutdown does not erase the evidence surface. The 4 TB NVMe tier (BOM line 2)
gives roughly 3–4× headroom over the current corpus footprint for layer growth and
point-in-time snapshots without a hardware swap. Refresh is scheduled, not live-streamed:
nightly incremental pulls, full reconciliation weekly, each write tagged with source,
retrieval timestamp, and layer version so provenance is preserved end to end. Person-level
datasets are **indexed as existing and never mirrored** — the appliance knows such a
dataset exists and where it lives, and stops there; it is never requested or held.

## 4. Spatial layer

Every reachable civic and [AIMS](https://github.com/EVEglyphDesign/lenexa-city-center-commons)
geospatial layer — parcels, infrastructure, streets, places — is registered into one 3D
coordinate space rather than left in fourteen incompatible viewers. Plausible open
components: a PostGIS store for the authoritative vector base, [3D Tiles](https://github.com/CesiumGS/3d-tiles)
as the streaming format for terrain and structures, [CesiumJS](https://cesium.com/platform/cesiumjs/)
as the rendering surface, and OpenStreetMap-derived road and building geometry as
scaffolding where county layers have gaps. This is a composition layer, not a new survey —
it does not replace county GIS, it reconciles it into one coordinate frame.

## 5. Anonymised presence layer

The filter runs at the edge, on camera hardware already in place — civic, commercial, and
residential systems keep operating exactly as they do today. What leaves the camera:
**counts and movement vectors only.** What never leaves the camera, under any condition:
**frames, faces, or any identity-linkable data.** No image or video frame is transmitted,
stored, or queryable off-device. The output is a live signal, not a live feed.

## 6. Arrival-gated information model

Geofence entry is the **only** trigger. There is no pre-arrival promotional feed — a
visitor who has not yet arrived sees nothing. Once physically inside the geofence, the
surface adds on-arrival recommendations only: what is good here, what to order, what not
to miss. This is a layer added where no platform currently operates pre-arrival, so no
merchant and no resident has a competitive complaint to raise.

## 7. Concentric safety beacons

Three zones, entirely resident-set. A spoken safe word raises a beacon visible to other
users in the affected zone. Camera feeds inside a raised zone are digitally stamped at the
moment of the raise, retrievable **only on a specific subpoena** — no automatic authority
notification, no aggregate signal pushed to the Lenexa Police Department or any other
agency. Evidence stays distributed with the citizens involved, not pooled centrally.

## 8. Payment path and charity routing

Payment clears at the point of experience — pay in place, less time at the till. Because
the delivery cost of the payment path is close to nil at this scale, proceeds route to a
named local Johnson County charity rather than to a platform rake.

## 9. Handover

**Jeff Eden receives:** the sealed appliance, the local mirror and spatial build resident
on it, a non-exclusive, non-transferable licence to operate the filter, arrival model,
beacon design, and payment routing, and an operational runbook (below). **Stays with
EVEglyphDesign:** copyright and design rights in the concept, the anonymised presence
filter, the arrival-gated information model, the concentric beacon design, and the
charity-routed payment path — no derivative, resale, or re-implementation without a
written EgD licence.

**Runbook, in outline:** (1) power and Tailscale check on boot; (2) nightly mirror
sync and weekly reconciliation job; (3) camera-filter health check per site; (4) beacon
zone review with residents on a standing cadence; (5) payment path reconciliation against
the named charity; (6) quarterly NVMe headroom check against corpus growth.

## 10. What this is not

Not surveillance — the presence layer emits counts and vectors, never frames or identity.
Not a live video feed — nothing streams off any camera. Not a replacement for existing
platforms — Google, Yelp, Nextdoor, OpenStreetMap, and city feeds remain the usable back
ends this sits in front of. Not a centralised community database — the mirror is a local,
disk-held evidence surface with person-level data indexed but never pulled, and beacon
evidence stays distributed rather than pooled.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
