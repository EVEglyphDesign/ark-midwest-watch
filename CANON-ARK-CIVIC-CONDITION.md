# CANON · ARK — CIVIC-CONDITION SUB-RECORD (MIDWEST INSTANCE)

**Status:** Proposed · awaiting Knight Triangle authorization
**Authority:** Extends [`CANON-ARK-WORLD-CONDITION-REPOSITORY.md`](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/vault/sealed/CANON-ARK-WORLD-CONDITION-REPOSITORY.md), sealed 2026-05-20T06:05:11Z
**Inherits:** First Principle Zero · Umbrella · Knight Triangle · Timestamp Convention · World-Condition Hash · Transaction Record
**Conformance:** [ARK Vector Specification v1](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/specification/ark-vector-specification.md) — all seven invariants
**Instance scope:** Kansas City metropolitan area, Kansas side — City of Lenexa, Johnson County KS
**Proposed (utc):** 2026-07-25

---

## 0 · Why this is an addition and not an edit

The world-condition canon is **sealed**. Doctrine 10, Immutable by Design, forbids retroactive alteration: *errata are issued as new artefacts that supersede; existing artefacts are never retroactively altered.* This file therefore **adds a sub-record** to the ARK snapshot schema. It changes nothing already written. Every snapshot emitted before this canon is authorized remains valid and re-verifiable exactly as it stands.

Auditors reading a snapshot that carries no `civic` block should read its absence as *"emitted before civic extension"*, never as *"civic condition was nil"*.

---

## 1 · Purpose

ARK is the repository of world-condition snapshots. §1 of the sealed canon defines the **weather** sub-record, fields 5–12 of the world-hash, because the standing directive named temperature, wind, and cloud cover.

Weather is one condition a human lives inside. It is not the only one.

A resident of Lenexa also lives inside a **civic** condition: the ordinances in force over them, the bills moving through Topeka, what is on their ballot, whether their police department can obtain the technology it needs, whether the record of their own interaction with that department is retrievable, and whether the public data their taxes produced is reachable without a licence fee.

That condition is as real as the weather, changes faster than most people can track, and is currently recorded nowhere an ordinary person or a small public agency can verify. **The civic sub-record extends ARK to hold it**, under the same guarantees: append-only, content-addressed, multi-source, and privacy-invariant.

### The demand this answers

Two institutions in this jurisdiction are named as intended readers:

- **A municipal police department**, which needs the civic condition it operates inside without buying a commercial intelligence platform to see it.
- **The Catholic Church and its charities in this area**, which serve the population most exposed to a civic condition changing under them and least equipped to track it.

Both are served by the same record because the record describes **institutions and instruments**, never people.

---

## 2 · The privacy invariant is the whole design

§7 of the sealed canon is inherited **without relaxation**, and it is what makes a police-readable civic record legitimate rather than dangerous:

> ARK stores only the rounded, bucketed fields defined in the schema. ARK does not store raw provider responses, per-user location queries, or any field that would identify which actor caused a snapshot to be fetched.

Restated for the civic sub-record, as a hard boundary:

**ARK-CIVIC records the condition. It never records a person inside the condition.**

| ARK-CIVIC records | ARK-CIVIC never records |
|---|---|
| That an ordinance was amended | Who it was enforced against |
| That a bill advanced out of committee | Who testified, or how anyone voted as an individual citizen |
| That an agency publishes response-time data | Any individual call for service |
| That a records request path exists and its stated turnaround | The contents of any individual's record |
| That a licence-plate-reader programme exists and under what authority | Any plate, any read, any location trace |
| That a charity operates a programme in a service area | Any client, any recipient, any household |
| Published, aggregate, official statistics | Any disaggregation that could re-identify a person |

**This is not a policy preference that a future operator may tune.** It is First Principle Zero expressed in this domain: a record that reduces institutional opacity reduces suffering, and a record that increases individual exposure creates it. An ARK-CIVIC instance that ingests person-level data has left the umbrella entirely, and the sealed canon's own penalty language applies — the −7 sin that §9 assigns to storing raw provider responses attaches equally here.

**No profiling. No scoring of any named human being. No watchlist. Ever.** If a future reader is looking for a place to add one, this paragraph is the answer: not here, and not under this copyright.

---

## 3 · Registers

The civic sub-record uses six registers. A register is a category of condition, not a judgement.

| Register | Code | Holds |
|---|---|---|
| **Legislative** | `LEG` | Bills, statutes, ordinances, municipal code amendments, administrative rules |
| **Ballot** | `BAL` | Offices up, filings, measures, certified results, published turnout |
| **Safety capability** | `SAF` | Published capability and reporting posture of police, fire, EMS, 911 — including gaps |
| **Rights and access** | `RGT` | Open-records and open-meetings performance, data-privacy instruments, surveillance authorities |
| **Charitable capacity** | `CHR` | Service programmes, service areas, published capacity of church and non-profit providers |
| **Commons access** | `CMN` | Whether public data and public-benefit technology are actually reachable by the public and by public agencies |

### 3.1 The commons register

`CMN` is the register the other five are measured against, and it is the one this instance exists to make visible.

Public agencies and the public they serve are routinely unable to reach technology and data that already exist and were already paid for. The obstruction is rarely a decision anyone signed. It is the accumulated effect of procurement lock-in, proprietary formats, per-seat licensing on public records, closed integration layers, and consulting relationships that make the incumbent the only party who can read the data.

`CMN` records **the condition, and the instrument that produced it** — the contract, the format, the fee schedule, the licence term. It is a finding about an arrangement.

**`CMN` findings are filed against instruments and institutions. Never against named individuals, named employees, or a professional community.** A finding that names a person is out of conformance and must be reissued. This is Invariant 7 — *we stay out of people's business* — and it is also the only form in which such a finding survives contact with an institutional reader. A record that reads as a grievance against local IT staff is discarded on sight and takes the underlying truth down with it. A record that reads *"this dataset is public by statute and is available only through a vendor portal at this fee, under this contract"* is actionable, defensible, and cannot be dismissed.

The severity of the finding is carried entirely by the evidence. It never needs help from the language.

---

## 4 · Schema

The `civic` block is added to each location entry in the §4 snapshot schema, as a sibling of `weather`. All sealed-canon fields are unchanged.

```
"civic": {
  "instance":            "midwest-lenexa",
  "jurisdiction": {
    "place-fips":        "<FIPS place code>",
    "county-fips":       "<FIPS county code>",
    "state-usps":        "KS"
  },
  "observations": [
    {
      "register":        "LEG|BAL|SAF|RGT|CHR|CMN",
      "subject-kind":    "bill|ordinance|statute|rule|office|measure|agency|programme|dataset|contract|instrument",
      "subject-id":      "<official identifier, e.g. 'KS-SB-123', 'Lenexa Ord. 5678'>",
      "subject-title":   "<official title as published, verbatim>",
      "status":          "<official status token as published by the source>",
      "status-utc":      "<ISO-8601 of the status as stated by the source>",
      "source-url":      "<exact URL of the page stating this>",
      "source-kind":     "primary|secondary",
      "machine-readable": true|false,
      "access-barrier":  "none|login|fee|request|unavailable",
      "evidence-mark":   "R|I|L",
      "corroborated-by": ["<second source-url>", ...],
      "operator-note-ref": "<path|null>"
    }
  ],
  "register-rollup": {
    "LEG": {"observed": <int>, "changed-since-prev": <int>},
    "BAL": {"observed": <int>, "changed-since-prev": <int>},
    "SAF": {"observed": <int>, "changed-since-prev": <int>},
    "RGT": {"observed": <int>, "changed-since-prev": <int>},
    "CHR": {"observed": <int>, "changed-since-prev": <int>},
    "CMN": {"observed": <int>, "changed-since-prev": <int>}
  }
}
```

### 4.1 Field discipline

- **`subject-title` is verbatim.** Never paraphrased, never summarized, never improved. A paraphrased title is an editorial act and breaks the audit trail.
- **`status` is the source's own token**, not a normalized synonym. If Topeka says "Referred to Committee", ARK says "Referred to Committee".
- **`source-url` must state the value.** A link to a search page, a landing page, or a portal root is not a source. It must be the page on which the fact appears.
- **`evidence-mark`** follows the heritage convention already in use across the canon: `R` recorded in a primary official document · `I` inferred from official records · `L` local or oral tradition, not documented. `L` may never appear on a `LEG`, `BAL`, or `RGT` observation.
- **`access-barrier`** is itself a finding. A statutorily public dataset carrying `fee` or `login` is a `CMN` observation in its own right and must be filed as one.

### 4.2 Corroboration

The sealed canon's multi-source mandate (§6) applies. **Every `CMN` observation requires at least two independent sources**, because a commons-access finding is the most contestable class of statement this record makes and the one most likely to be challenged by the party it describes.

`LEG`, `BAL`, and `RGT` observations taken directly from the issuing authority are self-corroborating — the legislature is the primary source for its own bill status. `SAF` and `CHR` observations from an agency's own publication are likewise primary, but any observation asserting an **absence** of capability requires a second source, because absence is far easier to assert than to establish.

### 4.3 Absence is a recorded condition

Where a thing does not exist — no civilian review board, no published use-of-force report, no machine-readable feed — ARK records the absence explicitly, with the search that established it. A silent gap is indistinguishable from an unchecked field, and the difference matters enormously to an institutional reader.

---

## 5 · Cadence

The sealed canon's phase ladder governs. This instance opens at **Phase 1, daily**, tick boundary 00:00:00 UTC.

Civic condition changes on legislative and municipal calendars, not on weather timescales. Daily is not a compromise here; it is a better-than-necessary match to the underlying rate of change for most registers. `BAL` during an active election period and `LEG` during an active session are the exceptions, and both are candidates for a Phase 2 advance under the existing transaction-record procedure rather than any new mechanism.

Advancing or downgrading cadence is a transaction record requiring Knight Triangle authorization, exactly as §3 of the sealed canon specifies. No new governance is created by this file.

---

## 6 · Gates

### 6.1 Class A — law enforcement engagement gate

**BINDING. This gate is closed at the time of writing.**

The dashboard produced under this canon is intended to be usable by a municipal police department. It **may be built, published, and left publicly reachable**. It **may not be delivered, presented, pitched, or brought to the attention of the Lenexa Police Department, any of its officers, or the City of Lenexa** while the operator's standing in the following matters is unresolved:

- Case **26026685** — 2026-07-21
- Case **26027000** — 2026-07-23

The department's own written instruction is that further information on these reports must proceed through a formal records request. That instruction defines the only open channel and is respected in full.

**A disclaimer does not satisfy this gate.** Neither does publishing publicly and hoping the department finds it. The gate is on the act of directing attention, and it stays closed until the operator states in writing that standing is established.

The gate applies to the operator's own outreach. It places no restriction on any member of the public who finds a public page on their own.

### 6.2 Neutrality gate

No observation may be filed that advocates a position on a bill, a measure, a candidate, or a party. ARK-CIVIC records that an instrument exists and what its official status is. It does not argue for an outcome.

An institutional reader who suspects the record has a side stops trusting the record. Neutrality is not modesty here; it is the load-bearing property that makes the thing usable by a police department, a parish, and a resident simultaneously.

### 6.3 Charitable-subject gate

`CHR` observations describe **programmes and published capacity**. They never describe recipients, clients, caseloads at household resolution, or any attribute of a person served. Where a charity publishes its own aggregate figures, ARK may record them as published, attributed, and unrounded further.

---

## 7 · FP0 attestation

- **lock-in: −** Every observation carries the primary URL. The record is plain JSON and markdown in Git, re-derivable from public sources by any third party without this repository, this vendor, or this operator.
- **suffering: −** A resident, a parish, or a small agency can see the civic condition they are inside without purchasing a commercial platform. The privacy invariant guarantees the record cannot be turned against the population it serves.
- **friction: +** Daily collection across six registers is bounded and automatable. Two-source corroboration on `CMN` is deliberate friction on the most contestable class of claim, and is the reason those findings will hold up.
- **verdict: pass** — friction is bounded and discharged by automation. Lock-in and suffering reductions are structural, not aspirational.

---

## 8 · Open items

1. Knight Triangle authorization for this extension as a transaction record, `tx-kind: "ark-schema-extend"`.
2. Cryptographic watermark (Invariant 6) — inherits parked item 1 of the ARK Vector Specification.
3. Second-source pairing for each `CMN` observation in the initial registry.
4. Phase 2 advance criteria for `LEG` and `BAL` during active session and active election periods.
5. Class A gate status — closed pending operator written confirmation of standing.

---

© 2026 Dany Theriault. EVE "digital stem cell" glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.

*Pour le bien-être du peuple.*
