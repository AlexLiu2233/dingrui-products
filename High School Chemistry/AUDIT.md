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

### Sprint — Deployment-Readiness Audit — 2026-06-03 (findings; audit-only)

**✅ RESOLVED 2026-06-03 (fix sprint on `hs_stem_complete`):** D1 dead-toggle + D4 localStorage normalized across all 66 SGs (`1b749f3`); A6 CJK-in-`	ext{}` cleared in all 25 affected SGs (`4ff2b62`, `5a7c0c3`); P2 favicon `../LOGO.png`→`../../LOGO.png` (`e580250`); B3 going-deeper added to Chem U4/U5 (`b644a18`). Findings below retained as the audit record.


Read-only audit of all 14 Study Guides against
`rag/study-guide-audit-checklist.md` Sections **A**, **B**, **D** with the
HS-STEM adjustments (E3/C1/interactive checks EXCLUDED; "no stray visual/JS"
ADDED; HS no-colon title + 4-column syllabus map + region chips + honors-flag +
bilingual + IB Chemistry HL feeders treated as correct conventions, not flagged;
Section D ACTIVE — D1 EN==ZH hard gate). No `.html` edited.

**Mechanical results (all 14 files):**
- **A8** `scripts/validate.sh` — exit 0 on all 14 (odd-`$` WARN benign). PASS.
- **D1** `data-lang="en"` == `data-lang="zh"` — parity on all 14 (counts 347-447). PASS.
- **A1** title — HS no-colon form `High School Chemistry — <Topic> | Dingrui Scholars` on all 14. PASS.
- **A2/A3** tokens — `--accent` + CJK font fallback (`PingFang SC`) present on all 14. PASS.
- **A4** external deps — KaTeX 0.16.9 + Google Fonts only; no novel CDN. PASS.
- **A5/A11/A12** dark-mode / `@media print` / `max-width: 600px` blocks present on all 14. PASS.
- **A7** TOC anchors — all sidebar `href="#…"` resolve to existing `id=` on all 14. PASS.
- **A10/A13** hero + footer + progress bar + `id="langToggle"` + `toggleLang()` present on all 14. PASS.
- **No stray visual/JS** — zero `<svg>`/`<img>`/`<canvas>`; 3 `<script>` per file = 2 KaTeX CDN + 1 inline (quiz/flashcard/toggle only, no chart/visual JS). PASS.
- **Feeder hrefs** — every `../../IB Chemistry HL/Study Guides/…` target resolves (Structure 1/2, Reactivity 1/2 all exist). PASS.
- **Syllabus-map codes** — all NGSS codes used (HS-PS1-1…1-8, HS-PS2-6, HS-PS3-1/3-4/3-5) trace to `rag/sources/us/` extracts; ON (SCH3U/SCH4U/SNC2D), BC (Chemistry 11/12), AB (Chemistry 20/30) match real codes. No fabricated codes (AB OCR caveat noted, none surfaced). PASS.
- **B (dual-goal)** — 10-12 worked examples + 12-14 flashcards (>8 gate) + quiz clusters per file; cheat-sheet/concept boxes present. PASS.

**Findings:**

| ID | File: gap | Tier | Status |
|---|---|---|---|
| **A6-1** | Unit_1_Atomic_Structure: 7 CJK chars inside `\text{}` in `$…$` math (e.g. `\text{上}`, `\text{电荷}`) render with fallback glyphs | P0 | Open |
| **A6-2** | Unit_4_Nomenclature: 1 CJK-in-`\text{}` (`\text{Fe 电荷}`) | P0 | Open |
| **A6-3** | Unit_5_The_Mole: 21 CJK-in-`\text{}` (e.g. `\text{实际产量}`, `\text{理论产量}`) | P0 | Open |
| **A6-4** | Unit_7_Gas_Laws: 16 CJK-in-`\text{}` (e.g. `\text{干气体}`, `\text{水蒸气}`) | P0 | Open |
| **A6-5** | Unit_9_Acids_Bases: 4 CJK-in-`\text{}` (e.g. `n_\text{酸}`, `\text{ 电离}`) | P0 | Open |
| **A6-6** | Unit_10_Thermochemistry: 90 CJK-in-`\text{}` (e.g. `q_\text{系统}`, `q_\text{环境}`, `E_\text{断}`) — worst offender | P0 | Open |
| **A6-7** | Unit_11_Reaction_Rates: 1 CJK-in-`\text{}` (`\text{速率比}`) | P0 | Open |
| **A6-8** | Unit_12_Chemical_Equilibrium: 7 CJK-in-`\text{}` (e.g. `\text{产物}`, `\text{反应物}`, `\text{系数}`) | P0 | Open |
| **A6-9** | Unit_13_Redox: 10 CJK-in-`\text{}` (e.g. `\text{阴极}`, `\text{阳极}`) | P0 | Open |
| **D4-1** | ALL 14 files: `toggleLang()` calls `localStorage.setItem('lang', …)` and an on-load `localStorage.getItem('lang')` adds `lang-zh` — page does NOT default to English on load once toggled. Violates locked A13/D4 rule (`toggleLang()` must not read/write `localStorage`; every page defaults to English). | P0 | Open |
| **Feeder-1** | Unit_7_Gas_Laws: `.feeder-link` CSS defined but no rendered feeder link in body (IB Structure 1 covers mole/gas — a feeder would be consistent with siblings) | P2 | Open |
| **Feeder-2** | Unit_14_Organic: no rendered feeder link (organic not cleanly covered by shipped IB Structure 1/2 + Reactivity 1/2 — omission defensible) | P2 | Open |
| **B3-1** | Unit_4_Nomenclature, Unit_5_The_Mole: zero `<details>`/going-deeper blocks (siblings carry 1-3) — top-score-chaser depth gap | P1 | Open |

**Overall verdict — NOT DEPLOYMENT-READY (blocked on P0).** Chrome,
mechanical hygiene, bilingual parity (D1), source-grounding, dual-goal
coverage, and the no-stray-visual sweep are all clean across 14 files. Two
P0 classes block ship: (1) **A6** — CJK characters inside `\text{}` in 9
files render as KaTeX fallback glyphs / broken math on the ZH side (worst:
Unit 10 with 90 hits; move Chinese outside math, use `\mathrm{}`/subscript
labels, or romanise); (2) **D4** — all 14 files persist language to
`localStorage` and auto-load ZH, violating the locked English-default rule
(strip the two `localStorage` lines from `toggleLang()` + the on-load block).
Fix the 9 A6 files and the uniform D4 pattern, re-run D1 parity + validate,
then this set is clean for FF. P1/P2 items (B3 depth on Units 4-5, missing
feeders on Units 7/14) are polish, not blockers.

**Counts: P0 = 10 (9× A6 + 1× D4 spanning all 14 files) · P1 = 1 · P2 = 2.**

---


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
