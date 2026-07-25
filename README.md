# ARK-CIVIC · Midwest Watch

**Instance:** `midwest-lenexa` — City of Lenexa and Johnson County, Kansas
**Status:** Phase 1 (daily) · genesis snapshot 2026-07-25 · **Class A gate CLOSED**
**Extends:** [`CANON-ARK-WORLD-CONDITION-REPOSITORY.md`](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/vault/sealed/CANON-ARK-WORLD-CONDITION-REPOSITORY.md), sealed 2026-05-20
**Conformance:** [ARK Vector Specification v1](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/specification/ark-vector-specification.md) — seven invariants

---

## What this is

ARK — *Archive of Recorded Kondition* — is the EVE Glyph Design repository of world-condition snapshots. The sealed canon defines the **weather** sub-record, because the standing directive named temperature, wind, and cloud cover.

This repository adds the **civic** sub-record.

A resident of Lenexa lives inside a weather condition and also inside a civic condition: the ordinances in force over them, the bills moving through Topeka, what is on their ballot, whether their police department can obtain the technology it needs, whether the record of their own interaction with that department is retrievable, and whether the public data their taxes already produced is reachable without a licence fee.

That condition is as real as the weather, changes faster than most people can track, and is recorded nowhere that an ordinary resident or a small public agency can verify. This repository records it.

## The one rule that governs everything here

**ARK-CIVIC records the condition. It never records a person inside the condition.**

| Recorded | Never recorded |
|---|---|
| That an ordinance was amended | Who it was enforced against |
| That a bill advanced out of committee | Who testified |
| That an agency publishes response-time data | Any individual call for service |
| That a records-request path exists | The contents of anyone's record |
| That an ALPR programme exists, under what authority | Any plate, any read, any location trace |
| That a charity runs a programme in a service area | Any client or household |

No profiling. No scoring of any named human being. No watchlist. This is not a tunable policy — it is First Principle Zero in this domain, and an instance that ingests person-level data has left the umbrella. Full statement in [canon §2](CANON-ARK-CIVIC-CONDITION.md).

## Registers

| Code | Register | Holds |
|---|---|---|
| `LEG` | Legislative | Bills, statutes, ordinances, code amendments, administrative rules |
| `BAL` | Ballot | Offices up, filings, measures, certified results, turnout |
| `SAF` | Safety capability | Published capability and reporting posture of police, fire, EMS, 911 — including gaps |
| `RGT` | Rights and access | Open-records and open-meetings performance, privacy instruments, surveillance authorities |
| `CHR` | Charitable capacity | Published programmes and capacity of church and non-profit providers |
| `CMN` | Commons access | Whether public data and public-benefit technology are actually reachable |

`CMN` is the register the other five are measured against. It records **arrangements and instruments** — the contract, the format, the fee schedule, the licence term. Per [canon §3.1](CANON-ARK-CIVIC-CONDITION.md) a `CMN` finding never names an individual or a professional community, and requires two independent sources before it stands. A finding that reads as a grievance is discarded by an institutional reader and takes the underlying truth down with it. A finding that reads *"this dataset is public by statute and available only through a vendor portal at this fee"* is actionable and cannot be dismissed.

## Contents

| Path | What it holds |
|---|---|
| [`CANON-ARK-CIVIC-CONDITION.md`](CANON-ARK-CIVIC-CONDITION.md) | The schema extension, privacy invariant, registers, gates, FP0 attestation |
| [`sources/REGISTRY.md`](sources/REGISTRY.md) | 31 verified sources across 6 groups, each with cadence, feed status, endpoint, access barrier |
| [`observations/2026-07-25-baseline.md`](observations/2026-07-25-baseline.md) | Genesis civic-condition observation |
| [`index.html`](index.html) | The dashboard surface |

## What the genesis snapshot found

**The commons here is better provisioned than average, and that is recorded first.** MARC publishes a working DCAT-US catalogue of 670 datasets. Johnson County AIMS runs a live ArcGIS server with roughly 90 free datasets. Lenexa publishes a live Calls for Service feed — free, no login — in which a yellow row means a drone was dispatched. Very few departments of this size publish live dispatch with an explicit unmanned-aerial indicator, and it is the strongest artifact of good faith in the jurisdiction's data posture.

**Against that, three structural conditions.**

Kansas has no comprehensive consumer data privacy act and no statute governing automated licence plate readers. Johnson County holds 475 ALPR devices — 26.1% of the state total, first of 83 counties — and a documented instance exists of a city critic accumulating roughly 150 plate reads in under two years. Lenexa operates seven drones with $995,335 approved for six more. There is no civilian body with investigative power; the Police Community Advisory Board, established by unanimous Council vote in December 2021, advises.

The Kansas Open Meetings Act requires no agenda, no minutes, and no posted public notice. Openness of a Kansas public meeting is opt-in for the citizen. Lenexa exceeds that floor in practice — a municipal choice, not a statutory guarantee.

And the data describing government is markedly less machine-reachable than the data describing land. Spatial data has an open server; legislation, ordinances, election results, and oversight proceedings do not. Almost certainly an artifact of which systems were procured when, rather than a decision to restrict — but the effect on a resident, a parish, or a small agency is identical regardless of how it arose, and the effect is what ARK records.

## Class A gate — CLOSED

The dashboard is intended to be usable by a municipal police department. It **may be built, published, and left publicly reachable.** It **may not be delivered, presented, pitched, or brought to the attention of** the Lenexa Police Department, any of its officers, or the City of Lenexa while the operator's standing in cases **26026685** (2026-07-21) and **26027000** (2026-07-23) is unresolved.

The department's written instruction is that further information on these reports proceeds through a formal records request. That defines the only open channel and is respected in full. **A disclaimer does not satisfy this gate**, and neither does publishing publicly and hoping it is found. The gate is on the act of directing attention. It places no restriction on any member of the public who finds a public page on their own.

## Posture

Source-first. Every observation carries the exact URL of the page stating it, marked `R` recorded, `I` inferred, or `L` local tradition. Titles and status tokens are verbatim, never paraphrased. Absence is recorded explicitly with the search that established it, because a silent gap is indistinguishable from an unchecked field.

No advocacy. ARK-CIVIC records that an instrument exists and what its official status is; it does not argue for an outcome. An institutional reader who suspects the record has a side stops trusting the record — neutrality is the load-bearing property that lets a police department, a parish, and a resident use the same page.

Standard intake only. No back channels, no adversarial outreach, no scraping behind authentication.

Design founder: **Donat Omer Thériault**, EVE Glyph Design. This credit is irrevocable.

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
