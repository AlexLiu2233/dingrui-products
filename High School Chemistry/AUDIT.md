# High School Chemistry — Audit

Open punch list for the High School Chemistry product, scored against the
canonical generation prompt ([`prompts/create-unit.md`](../prompts/create-unit.md))
plus the subject-specific spec at
[`rag/subjects/high_school_chemistry.md`](../rag/subjects/high_school_chemistry.md).

**Strategic posture:** One topic-organised study-guide set serving both
US **NGSS** (primary commercial target — note the US science standard is
NGSS HS-PS1, **not** Common Core, which is Math/ELA only) and the top
three Canadian provincial curricula — Ontario, BC, Alberta — implicitly
through universal topic coverage. Genuine curriculum differences are
called out *inside* each guide via Syllabus Map and Syllabus Note
callouts, not by forking content. This is the **secondary-school tier**,
distinct from the existing college-credit-tier `IB Chemistry HL/`
product. See spec for details.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / NGSS / AP-IB-feeder / provincial-exam use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product first.
Practice Questions and Solutions follow once the Study Guide template is
locked. All other surfaces live in the
[Digital Product Backlog](#digital-product-backlog).

Last reviewed: **2026-06-02** (**all 14 Study Guides shipped** —
bilingual from start, source-grounded, validate PASS, balanced EN/ZH
spans — on branch `hs_chemistry_sg`, awaiting review/FF to main.
Practice + Solutions and the static-visual upgrade are later waves.)

---

## Active Sprint — what we're working on now

### Sprint 1 — source-grounding + 14 bilingual Study Guides — **CLOSED 2026-06-02** (branch `hs_chemistry_sg`, awaiting FF to main)

**Shipped:** all 4 curricula source-grounded (NGSS HS-PS1, ON SCH3U/4U,
BC Chem 11/12, AB Chem 20/30 — extracts + cached PDFs in `rag/sources/`),
Unit 1 Atomic Structure drafted as the bilingual template lock, then
Units 2-14 bulk-drafted via Sonnet **copy-then-edit** (cp Unit 1, transform
per-section). All 14 SGs: ~1010-1160 lines, balanced EN/ZH spans, validate
PASS, syllabus-maps cite real codes per curriculum; feeder-links → IB
Chemistry HL (Structure 1/2, Reactivity 1/2) where topics align. Divergence
syllabus-notes baked in: NGSS qualitative (no PE for Nomenclature/Gas
Laws/Acids/Redox/Organic; honors-flag quantitative Thermo/Kinetics/
Equilibrium); BC organic in Gr11 + light thermo; AB no standalone kinetics.

| Unit | Topic | Spans (EN=ZH) |
|---|---|---|
| 1 | Atomic Structure (template) | 475 |
| 2 | Periodic Table and Trends | 494 |
| 3 | Chemical Bonding | 487 |
| 4 | Nomenclature and Formulae | 503 |
| 5 | The Mole and Stoichiometry | 407 |
| 6 | Chemical Reactions and Equations | 473 |
| 7 | States of Matter and Gas Laws | 390 |
| 8 | Solutions and Solubility | 485 |
| 9 | Acids, Bases and pH | 449 |
| 10 | Thermochemistry and Energy | 408 |
| 11 | Reaction Rates and Kinetics | 503 |
| 12 | Chemical Equilibrium | 479 |
| 13 | Redox and Electrochemistry | 469 |
| 14 | Introduction to Organic Chemistry | 493 |

**Next:** build-index + landing-page integration (surface 14 Chemistry cards),
then static-visual upgrade (deferred until all HS STEM SGs ship), then P+S.

#### Original Sprint 1 plan (historical)

### Sprint 1 — source-grounding + Unit 1 SG template lock — (historical plan)

Stand up the subject: fetch and extract the four-curriculum source
documents, then draft the **Unit 1 (Atomic Structure and the Quantum
Model)** Study Guide as the template-lock unit — **bilingual EN/ZH from
the first commit** (locked standing principle; no English-first parking,
no retroactive-translation tax). Unit 1 proves the SG template so
Sprint 2+ can bulk-draft.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-sources** | Add NGSS HS-PS1 + ON SCH3U/SCH4U/SNC2D + BC Chemistry 11/12 + AB Chemistry 20/30 rows to `sources.txt`; fetch PDFs into `rag/sources/<region>/` | P0 | **open** — all source-grounding PENDING; official URLs recorded in spec |
| **S1-extracts** | Write `*_extract.md` Atomic-Structure / Periodic slices for each of the 4 curricula | P0 | **open** — blocks Unit 1 Syllabus Map |
| **S1-css** | Confirm `syllabus-map` / `syllabus-note` / `honors-flag` / `feeder-link` CSS reuses the HS Math lock (no fork) | P1 | **open** |
| **S1-SG** | Draft `Unit_1_Atomic_Structure_and_the_Quantum_Model.html` — bilingual EN/ZH, 7 sections, 4-column Syllabus Map (US/ON/BC/AB), honors-flag, feeder-link to IB Chemistry HL | P0 | **open** — template-lock unit |
| **S1-index** | Add HS Chemistry to `scripts/build-index.py` `SUBJECTS` (unused chip colour) + seed index.html subject-group block; re-run build-index | P1 | **open** — do at first SG ship |

Build order: **S1-sources → S1-extracts → S1-css + S1-SG → S1-index**.

Sprint 2+ candidates: bulk-draft Units 2-6 (Periodic Table, Bonding,
Nomenclature, Mole/Stoichiometry, Reactions) from the locked Unit 1
template; Practice + Solutions triplets once ≥3 SGs ship.

---

## Cross-Unit Snapshot

| Unit | Topic | SG | Practice | Solutions | Status |
|---|---|---|---|---|---|
| 1  | Atomic Structure and the Quantum Model       | &mdash; | &mdash; | &mdash; | **Sprint 1 — template lock (open)** |
| 2  | The Periodic Table and Periodic Trends       | &mdash; | &mdash; | &mdash; | unbuilt |
| 3  | Chemical Bonding (Ionic, Covalent, Metallic) | &mdash; | &mdash; | &mdash; | unbuilt |
| 4  | Nomenclature and Chemical Formulae           | &mdash; | &mdash; | &mdash; | unbuilt |
| 5  | The Mole and Stoichiometry                   | &mdash; | &mdash; | &mdash; | unbuilt |
| 6  | Chemical Reactions and Equations             | &mdash; | &mdash; | &mdash; | unbuilt |
| 7  | States of Matter and the Gas Laws            | &mdash; | &mdash; | &mdash; | unbuilt |
| 8  | Solutions and Solubility                     | &mdash; | &mdash; | &mdash; | unbuilt |
| 9  | Acids, Bases and pH                          | &mdash; | &mdash; | &mdash; | unbuilt |
| 10 | Thermochemistry and Energy                   | &mdash; | &mdash; | &mdash; | unbuilt |
| 11 | Reaction Rates (Kinetics)                    | &mdash; | &mdash; | &mdash; | unbuilt |
| 12 | Chemical Equilibrium                         | &mdash; | &mdash; | &mdash; | unbuilt |
| 13 | Redox and Electrochemistry                   | &mdash; | &mdash; | &mdash; | unbuilt |
| 14 | Introduction to Organic Chemistry            | &mdash; | &mdash; | &mdash; | unbuilt |

Unit list is a **draft pending per-unit source verification** — confirm
curriculum codes against the fetched source PDFs before locking each
unit's Syllabus Map. Spec carries the per-unit US/ON/BC/AB mapping.

---

## Source-grounding state

**All PENDING.** No PDFs fetched. Official URLs recorded in the spec
(`rag/subjects/high_school_chemistry.md` → Cross-references). Sprint 1
S1-sources / S1-extracts close this.

| Region | Course / doc | Real course codes | Status (2026-05-31) |
|---|---|---|---|
| 🇺🇸 US | NGSS HS Physical Science | HS-PS1 (Matter & its Interactions); HS-PS2 / HS-PS3 crossover | **PENDING** |
| 🇨🇦 ON | Chemistry Gr 11/12 + Science 10 | SCH3U, SCH4U; SNC2D foundations | **PENDING** |
| 🇨🇦 BC | Chemistry 11/12 + Science 10 | Chemistry 11, Chemistry 12; Science 10 foundations | **PENDING** |
| 🇨🇦 AB | Chemistry 20/30 + Science 10 | Chemistry 20, Chemistry 30; Science 10 foundations | **PENDING** |

Official curriculum URLs (verify against, do not paraphrase from memory):

- US NGSS: <https://www.nextgenscience.org/>
- BC: <https://curriculum.gov.bc.ca/curriculum/science>
- Ontario: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
- Alberta: <https://www.alberta.ca/programs-of-study>

---

## Standing principles

- **Topic-indexed, single set.** One unit per chemistry topic, not per
  US course. Filename: `Unit_N_Topic.html`, sequential `N` across the
  whole subject. Title format and naming locked in
  [`rag/subjects/high_school_chemistry.md`](../rag/subjects/high_school_chemistry.md).
- **No "Unit N" in visible chrome.** Filenames keep `Unit_N_` for sort
  stability; everything visible strips it (inherited from HS Math).
  Topic-code nav-badge mapping locked in the spec.
- **Multi-syllabus crosswalk inside each guide.** Every unit ships with
  a 4-column Syllabus Map callout (US NGSS / Ontario / BC / Alberta).
  Genuine divergences get an inline Syllabus Note &mdash; sparingly.
- **Dual-goal contract** &mdash; every guide serves both the
  test-tomorrow crammer and the depth student. Cram cheat-sheet on top,
  going-deeper derivations at the bottom. Locked from IB Math HL;
  canonical articulation in [`prompts/create-unit.md`](../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every SG ships
  with paired EN/ZH spans + working `toggleLang()` in the first commit.
  **Non-negotiable for new subjects.** No English-first parking, no
  `data-zh-ready="false"` — HS Chemistry must not repeat the HS Math
  retroactive-translation tax (Sprints 5-6).
- **Honors-flag.** Honors / harder-stream topics (AB Chemistry 30, ON
  SCH4U depth) use an `honors-flag` chip so regular-track students can
  skip cleanly.
- **Feeder pointers.** Topics feeding IB Chemistry HL / AP Chemistry
  hyperlink the target unit where it already exists in this repo.
- **Verification rule.** Any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not acceptable.

---

## Closed Sprints

### Sprint 0 — closed 2026-05-31

Subject scaffolding shipped: subject spec
(`rag/subjects/high_school_chemistry.md`), this audit, and the empty
folder structure (`Study Guides/`, `Practice Questions/Solutions/`).
Topic-organised multi-syllabus posture adopted from the start (mirrors
HS Math's revised direction; no US-only-pathway false start).

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-2**~~ | Author audit | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-3**~~ | Create empty folder structure | P0 | ✅ shipped 2026-05-31 |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint.

| ID  | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice Questions product (MC + structured-response sets per unit, with Solutions companion mirroring the HS Math pattern) | Needs Study Guide content first to anchor question scope. Open after ≥3 study guides ship. |
| DP-2 | Lab / practical-skills cards (safety, measurement, error analysis) on each guide | NGSS science-and-engineering practices + provincial lab strands need a separate scoping pass. |
| DP-3 | Per-province exam-prep overlays (AB Diploma Chemistry 30, BC numeracy/provincial) on top of the topic guides | Layer onto existing guides; deferred until Canadian audience demand is measured. |
| DP-4 | Periodic-table / reaction-type interactive widgets | Richer interactive product; out of scope for the static SG surface. |
| DP-5 | Geometry-of-molecules / VSEPR 3D viewer for the Bonding unit | Interactive enhancement; deferred. |

---

## How to update this file

When closing a sprint item, mark with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When a sprint clears,
collapse into a single line in `## Closed Sprints` and promote the
next sprint up.

When standing principles need revision, edit them here; route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_chemistry.md`](../rag/subjects/high_school_chemistry.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork
the contract.

When a unit ships, fill in its row of the cross-unit snapshot with
actual SG / Practice / Solutions status.
