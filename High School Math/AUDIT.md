# High School Math — Audit

Open punch list for the High School Math product, scored against the
canonical generation prompt ([`prompts/create-unit.md`](../prompts/create-unit.md))
plus the subject-specific spec at
[`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md).

**Strategic posture (locked 2026-05-16):** One topic-organised study-guide
set serving both US Common Core (primary commercial target) and the top
three Canadian provincial curricula — Ontario, BC, Alberta — implicitly
through universal topic coverage. Genuine curriculum differences are
called out *inside* each guide via Syllabus Map and Syllabus Note
callouts, not by forking content. See spec for details.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / SAT / AP-feeder / provincial-exam use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only.
Practice Questions, SAT-prep cross-references, and bilingual translation
all live in the [Digital Product Backlog](#digital-product-backlog) until
those product surfaces spin up.

Last reviewed: **2026-05-17** (Sprint 0.5 paused — PDFs fetched, text
extraction blocked by sandbox; awaiting user-supplied extracts).

---

## Active Sprint — what we're working on now

**Sprint 0.5 — Source-grounding and first unit choice.** Before any
unit drafting, we ground the multi-syllabus posture in actual source
documents so syllabus claims inside guides cite real codes, not
training-data recall.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0.5-1**~~ | Add **CCSSM High School** (US Common Core) as a row in `sources.txt` | P0 | ✅ shipped 2026-05-16 (commit `ecbc87a`, row 13) |
| **S0.5-2a** | Fetch 4 priority PDFs into `rag/sources/` | P0 | ✅ shipped 2026-05-16 — files committed (see [Manual extraction checklist](#manual-extraction-checklist--blocking-unit-1) below) |
| **S0.5-2b** | Extract Linear-Functions text from those PDFs into `*_extract.md` companions | P0 | 🟡 **BLOCKED — user-action required.** Sandbox lacks `pdftoppm`; Read tool cannot parse PDFs. Checklist below. |
| ~~**S0.5-3**~~ | Pick the topic for Unit 1 | P0 | ✅ 2026-05-16 — **Linear Functions and Systems** |
| **S0.5-4** | Define the `syllabus-map` and `syllabus-note` CSS callout classes | P1 | Open &mdash; lands with Unit 1 |

Build order: S0.5-2b (user) → open Sprint 1 (Unit 1 drafting) → S0.5-4
lands as part of Unit 1.

### Manual extraction checklist — blocking Unit 1

The four primary PDFs are on disk in `rag/sources/` (commit `ecbc87a`),
but this sandbox can't extract text from them. User opens each PDF
locally, finds the Linear-Functions / Linear-Systems sections, and saves
the verbatim extract as a markdown sibling next to the PDF. Format
suggestion below the table.

| # | Region | Source PDF (on disk now) | Extract file to create | What to pull out |
|---|---|---|---|---|
| 1 | 🇺🇸 US | `rag/sources/us/ccssm_hs_math.pdf` (93 pp) | `rag/sources/us/ccssm_hs_math_extract.md` | All HS standards under domains **HSA-CED**, **HSA-REI** (linear portions: A.1, A.3, B.3, C.5–6, D.10–12), **HSA-SSE** (A.1 cases), **HSF-IF** (B.4, B.6, C.7a, C.9 linear), **HSF-LE** (A.1–4, B.5), **HSF-BF** (A.1a, B.3 linear), **HSN-Q** (modeling) |
| 2 | 🇨🇦 BC | `rag/sources/bc/fmpc10_elab.pdf` | `rag/sources/bc/fmpc10_elab_extract.md` | The **Big Ideas**, **Curricular Competencies**, and **Content** standards from the **Relations and Functions** strand of FMPC10. Include the elaborations columns (column 3 in the curriculum tables). Slope, linear relations, systems, function notation. |
| 3 | 🇨🇦 ON | `rag/sources/on/math_grades_9-10.pdf` | `rag/sources/on/math_grades_9-10_extract.md` | The **MPM2D — Principles of Mathematics, Grade 10 Academic** strand for **Linear Systems** (strand and specific expectations with codes — typically appears as "LS" or under "Linear Systems"), plus any **Analytic Geometry** expectations touching linear (slope, distance, midpoint, equation of a line). Skip quadratics and trig. |
| 4 | 🇨🇦 ON | `rag/sources/on/math_grades_11-12.pdf` | `rag/sources/on/math_grades_11-12_extract.md` | **MCR3U — Functions, Grade 11 University** specific expectations that review or extend linear functions (function notation, domain/range, transformations of linear). Brief; skip if MCR3U has no dedicated linear strand. |

**Suggested extract format** (per file):

```markdown
# {Subject} — Linear-Functions Extract
Source: `{path/to/file.pdf}` p. X–Y (date or revision if visible on cover)

## {Domain / Strand name}
- **{CODE}**: {verbatim standard text}
  - {sub-bullet if present}
- **{CODE}**: {verbatim standard text}

## {Next domain / strand}
...
```

Anything beyond verbatim standards (commentary, study notes) is fine but
optional — what blocks the draft is having the **codes + text** verbatim
so the in-guide Syllabus Map can cite them without paraphrase risk. Once
all four `*_extract.md` files exist, S0.5-2b closes and Unit 1 drafting
opens.

**Optional later additions** (don't block Unit 1, but useful for later units):

| # | Region | Source URL (in `sources.txt`, row #) | Why later |
|---|---|---|---|
| 5 | 🇨🇦 BC | row 02 — `bc/pc11_elab.pdf` | Drives Units 2–6 (quadratics, exp/log, sequences, trig basics) |
| 6 | 🇨🇦 BC | row 03 — `bc/pc12_elab.pdf` | Drives Units 5–12 (function families, trig identities, combinatorics) |
| 7 | 🇨🇦 AB | row 07 — `ab/pos_10-12_indicators.pdf` | One doc covering AB Math 10C / 20-1 / 30-1 — needed to add the AB column to every Unit's Syllabus Map |
| 8 | 🇨🇦 AB | row 09 — `ab/math10c_standards.pdf` | Granular Math 10C assessment standards; useful but Math 30-1 is higher leverage |

---

## Standing principles

- **Topic-indexed, single set.** One unit per mathematical topic, not
  per US course. Filename: `Unit_N_Topic.html`, sequential `N` across
  the whole subject. Title format and naming locked in
  [`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md).
- **Multi-syllabus crosswalk inside each guide.** Every unit ships
  with a Syllabus Map callout near the top listing the matching codes
  in US CCSSM, Ontario, BC, and Alberta. Genuine divergences (a topic
  one curriculum emphasises but another defers) get an inline
  Syllabus Note &mdash; sparingly, only where it matters.
- **Dual-goal contract** &mdash; every guide must serve both the
  test-tomorrow crammer and the depth student. Cram cheat-sheet on top,
  going-deeper proofs at the bottom. Locked from IB Math HL; canonical
  articulation in [`prompts/create-unit.md`](../prompts/create-unit.md).
- **Verification rule:** any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not an
  acceptable citation. Spec enforces.
- **English-first.** No bilingual track until the EN content stabilises.
- **No HL flag.** Honors-level topics use an `honors-flag` chip (CSS
  defined when first used) so a regular-track student can skip cleanly.

---

## Cross-Unit Snapshot

| Unit | Topic | Sections | Worked Ex. | Quiz | Status |
|---|---|---|---|---|---|
| 1   | Linear Functions and Systems            | &mdash; | &mdash; | &mdash; | **Sprint 1 queued** |
| 2   | Quadratic Functions and Equations       | &mdash; | &mdash; | &mdash; | unbuilt |
| 3   | Polynomial Functions                    | &mdash; | &mdash; | &mdash; | unbuilt |
| 4   | Rational and Radical Expressions        | &mdash; | &mdash; | &mdash; | unbuilt |
| 5   | Exponential and Logarithmic Functions   | &mdash; | &mdash; | &mdash; | unbuilt |
| 6   | Sequences and Series                    | &mdash; | &mdash; | &mdash; | unbuilt |
| 7   | Right-Triangle Trigonometry             | &mdash; | &mdash; | &mdash; | unbuilt |
| 8   | Unit-Circle Trig and Trigonometric Functions | &mdash; | &mdash; | &mdash; | unbuilt |
| 9   | Trigonometric Identities and Equations  | &mdash; | &mdash; | &mdash; | unbuilt |
| 10  | Function Transformations and Composition| &mdash; | &mdash; | &mdash; | unbuilt |
| 11  | Combinatorics and the Binomial Theorem  | &mdash; | &mdash; | &mdash; | unbuilt |
| 12  | Conic Sections                          | &mdash; | &mdash; | &mdash; | unbuilt |
| 13  | Probability and Statistics Foundations  | &mdash; | &mdash; | &mdash; | unbuilt |
| 14  | Vectors (2D and 3D)                     | &mdash; | &mdash; | &mdash; | unbuilt |
| 15  | Introduction to Limits and Calculus     | &mdash; | &mdash; | &mdash; | unbuilt |

Geometry (US one-year course; distributed in Canadian curricula) is
deliberately omitted; revisit after Sprint 2 if demand surfaces.

---

## Topic Scope Reminders (multi-syllabus)

These are placeholder cross-references &mdash; treat as starting points,
verify against the fetched source PDFs in `rag/sources/` before
locking any unit's syllabus map.

| Unit topic | 🇺🇸 CCSSM | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|
| Linear & systems | HSF-LE.A.1–4 · HSA-REI.C/D | MPM2D · MCR3U review | Foundations & PC10 RF | Math 10C RF |
| Quadratics | HSA-REI.B.4 · HSF-IF.C.7–9 | MPM2D quadratics | PC11 quadratics | Math 20-1 quadratics |
| Polynomial functions | HSA-APR.B/C · HSF-IF.C | MHF4U C2 | PC12 polynomial functions | Math 30-1 polynomial |
| Rational / radical | HSA-APR.D · HSA-REI.A | MHF4U rational | PC11 / PC12 rational, radical | Math 20-1 / 30-1 |
| Exp & log | HSF-LE.A · HSF-BF.B.5 | MCR3U · MHF4U | PC12 exp & log | Math 30-1 exp & log |
| Sequences & series | HSF-BF.A.2 · HSA-SSE.B.4 | MCR3U seq | PC11 seq | Math 20-1 seq |
| Trig (right triangle) | HSG-SRT.C.6–8 | MPM2D trig | PC11 trig | Math 10C trig |
| Trig (unit circle, funcs) | HSF-TF.A/B | MHF4U | PC12 trig | Math 30-1 trig |
| Trig identities & eqns | HSF-TF.C | MHF4U | PC12 trig | Math 30-1 trig |
| Function transformations | HSF-BF.B.3 | MHF4U C1 | PC12 RF | Math 30-1 RF |
| Combinatorics & binomial | HSS-CP.B.9 (light) | MHF4U / MDM4U | PC12 combinatorics | Math 30-1 permutations |
| Conics | HSG-GPE.A.1–3 | (sparse) | (sparse) | (sparse) |
| Probability & stats | HSS-IC · HSS-CP | MDM4U (full course) | (sparse) | Math 30-1 (light) |
| Vectors | HSN-VM.A/B/C | MCV4U (full unit) | (not in PC) | (Math 31 lite) |
| Limits / intro calc | (not in CCSSM) | MCV4U | Calc 12 | Math 31 |

---

## Closed Sprints

### Sprint 0 — closed 2026-05-16

Subject scaffolding shipped. The original Sprint 0 framing (4-course
US-only pathway: Algebra I, Geometry, Algebra II, Pre-Calc) was
**revised same-day** to the topic-organised multi-syllabus posture
above. Original commit `9dfc793` is preserved in history; current
spec and audit reflect the revised direction.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec | P0 | ✅ shipped 2026-05-16 (revised same-day) |
| ~~**S0-2**~~ | Author audit | P0 | ✅ shipped 2026-05-16 (revised same-day) |
| ~~**S0-3**~~ | Create empty folder structure | P0 | ✅ shipped 2026-05-16 |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint.

| ID  | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice Questions product (MC and FRQ-style sets per unit, with Solutions companion mirroring IB Math HL A3 pattern) | Needs Study Guide content first to anchor question scope. Open after ≥3 study guides ship. |
| DP-2 | SAT / ACT cross-reference cards on each guide | Format and question-pattern templates need a separate scoping pass. |
| DP-3 | Per-province exam-prep overlays (BC Provincial, AB Diploma) on top of the topic guides | Layer onto existing guides; deferred until Canadian audience demand is measured. |
| DP-4 | ZH translation track (mirroring `ap_chinese_translation` for AP Calc) | Defer until EN content stabilises. |
| DP-5 | Geometry topic-bundle (congruence, similarity, circles, 3D figures, coordinate geometry) | Sprint 2 candidate if topic-set has reach. |
| DP-6 | `honors-flag` and `syllabus-map` / `syllabus-note` CSS specification | Land with Unit 1's HTML; promoted to standing principle once stable. |

---

## How to update this file

When closing a sprint item, mark with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When a sprint clears,
collapse into a single line in `## Closed Sprints` and promote the
next sprint up.

When standing principles need revision, edit them here; route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork
the contract.

When a unit ships, fill in its row of the cross-unit snapshot with
actual section / worked-example / quiz counts.
