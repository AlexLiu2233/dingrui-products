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

Last reviewed: **2026-05-26** (Sprint 4 opened — Units 7-15 bilingual
Study-Guide bulk-draft on `high_school_math_sprint4` branch.
PQ/Solutions deferred to a later sprint per user 2026-05-26
token-optimization decision. **6/15 units shipped end-to-end + 9
SG-only drafts in flight.**

---

## Active Sprint — what we're working on now

### Sprint 4 — Units 7-15 bilingual Study-Guide bulk-draft (SG-only, EN + ZH from start) — **OPEN 2026-05-26** (branch `high_school_math_sprint4`)

**Posture shift locked 2026-05-26:**

1. **SG-only sprint.** PQ + Solutions deferred to a follow-on sprint
   for token-budget reasons. Goal: ship maximum Study Guide coverage
   first, then catch the practice corpus up in a later sprint.
2. **Bilingual-from-start.** Every Unit 7-15 SG ships with paired
   `<span data-lang="en">` + `<span data-lang="zh">` markup in the
   same commit. This is a **departure** from the prior English-first
   pattern in `high_school_math.md`. Reason: each new SG should land
   visible in the landing-page ZH mode immediately, not wait for a
   translation wave.
3. **Retroactive ZH for Units 1-6.** The existing six units are
   English-only and hide in ZH mode via `data-zh-ready="false"`. A
   retroactive ZH translation pass is the second half of this sprint
   so the full HS Math corpus surfaces in ZH mode at sprint close.
4. **Order: curriculum-natural but flexible on numbering.** The
   topic list in `high_school_math.md` is a working sequence;
   curricula vary on when each topic lands per grade, so the unit
   N filename is the canonical handle but the "natural order" is a
   guideline, not a contract.

**Sprint 4 deliverable contract:**

- 9 new bilingual SGs: Units 7-15. Each follows the locked Unit 2
  template (8-row grade-by-region nav, syllabus-map cited verbatim
  from the source extracts, region+paper-style chips, honors-flag
  pattern, feeder-link to AP Calc / IB Math HL where applicable, 7
  content sections satisfying dual-goal contract, 12+ flashcards,
  10+ readiness checklist items).
- 6 retroactive ZH translations: Units 1-6.
- AB column added to the Syllabus Map on all 15 units (now that the
  AB source PDFs are in `rag/sources/ab/`).
- `data-zh-ready="false"` lifted from HS Math cards on landing page
  at sprint close (build-index.py will pick it up automatically once
  every unit file has `data-lang="zh"` markers).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S4-template** | Draft Unit 7 (Right-Triangle Trigonometry) bilingual SG to lock the bilingual-from-start template | P0 | open |
| **S4-SG-bulk** | Bulk-draft Units 8, 9, 10, 11, 12, 13, 14, 15 bilingual SGs in parallel via subagents (8 files, ~10000 lines) | P0 | blocked on S4-template user review |
| **S4-retro-zh** | Retroactive ZH translation pass on Units 1-6 (6 files, ~6500 lines) | P0 | open |
| **S4-ab-column** | Add AB column to Syllabus Map across all 15 unit files using `rag/sources/ab/` PDFs | P1 | open |
| **S4-index** | Re-run `scripts/build-index.py` so HS Math cards surface in ZH mode | P1 | open at sprint close |

Build order: **S4-template → S4-retro-zh + S4-SG-bulk in parallel →
S4-ab-column → S4-index**. Sprint 5+ (PQ + Solutions catch-up) opens
once this sprint closes.

---

### Sprint 3 — Units 3-6 bulk-draft from locked Unit 2 template — **CLOSED 2026-05-26** (branch `high_school_math_sprint3`)

**Closed 2026-05-26**. Sprint 3 doubled the size of the shipped corpus
in one branch by bulk-drafting Units 3-6 (Polynomial, Rational/Radical,
Exp/Log, Sequences/Series) in parallel from the Unit 2 template locked
at end of Sprint 2. All twelve files (4 SG + 4 P + 4 S) share identical
chrome: 8-row grade-by-region nav, region+paper-style chip taxonomy,
syllabus-map with verbatim source citations, .insight callouts on every
Solutions question.

1. **BC PC12 source fetch** (`f052fba`) — fetched `pc12_elab.pdf` from
   `curriculum.gov.bc.ca`; wrote `pc12_elab_extract.md` covering ALL
   non-PC11 content for HS Math Units 3-10 (polynomial, rational, exp/log,
   sequences/series, trig, transformations). Closes the BC column for
   the next 8 units in one fetch.
2. **Units 3-6 SG batch** (`17042c2`) — 4590 SG lines drafted in
   parallel via foreground subagents from Unit 2 template. Each unit
   has 7 content sections, 8-row grade-nav, syllabus-map verified
   verbatim per extract, 21-24 quizzes, 13-14 flashcards, 12 checklist
   items.
3. **Units 3-6 Practice batch** (`0a517e6`) — 1630 Practice lines,
   each Unit 12 Qs / 90 marks, EASY/MED/HARD per Unit 1/2 split,
   region+paper-style chrome verbatim from Unit 2.
4. **Units 3-6 Solutions batch** (`7b15e37`) — 2322 Solutions lines,
   each Unit 12 Qs / 90 marks with mark-callouts summing to declared
   marks, .distractor blocks on MCQs, 12 .insight blocks per Unit,
   index.html regen surfacing Units 3-6 cards.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S3-bcfetch**~~ | Fetch BC PC12 + extract Units 3-10 slice | P1 | ✅ closed — `f052fba` (unblocks BC column for Units 3-10) |
| ~~**S3-SG**~~ | Draft 4 SGs (Units 3-6) | P0 | ✅ closed — `17042c2` (4590 lines, 4 files parallel via subagents) |
| ~~**S3-P**~~ | Draft 4 Practice files (Units 3-6) | P0 | ✅ closed — `0a517e6` (1630 lines, 12 Qs / 90 marks per unit) |
| ~~**S3-S**~~ | Draft 4 Solutions files (Units 3-6) | P0 | ✅ closed — `7b15e37` (2322 lines, mark-sums verified per Q, Unit 4 `\$` → `&#36;` migration) |
| ~~**S3-index**~~ | Re-run scripts/build-index.py to surface Units 3-6 cards in landing page | P1 | ✅ closed — folded into `7b15e37` (SG batch commit forgot it) |

**Sprint 3 deliverable contract met:** 4 units shipped end-to-end with
parity to Unit 2; chip taxonomy and curriculum-callout structure
unchanged from Unit 2; 360 marks total across 48 Practice questions;
48 .insight callouts; 12 .distractor blocks (3 MCQs × 4 units).

**Locked Sprint 4+ template:** Sprint 3 confirmed the Unit 2 template
scales via foreground subagents. Future Units 7-15 follow the same
parallel-bulk-draft pattern with a 4-unit batch as the natural sprint
unit.

---

### Sprint 2 — Unit 2 Quadratic Functions and Equations (full triplet) — **CLOSED 2026-05-25** (branch `high_school_math_unit_2`)

**Closed 2026-05-25**. User feedback after Unit 1 ship: "How to use guide doesn't seem right — should discuss topic-specific stuff and per-grade focus, with source citations." Sprint 2 closes that feedback by:

1. **Unit 1 how-to-use rework** (`b37a192`) — replaced generic "If cramming / If going for top mark" framing with an 8-row grade-by-region nav table. Each row tells a student (e.g. "🇨🇦 ON Grade 9 — MPM1D") which sections to focus on, which to defer, and cites the specific source extract + strand. This pattern is now locked for Sprint 2+.
2. **BC PC11 source fetch** (`94f0988`) — fetched `pc11_elab.pdf` from `curriculum.gov.bc.ca`; wrote `pc11_elab_extract.md` scoped to Quadratics + Polynomial Factoring + Linear/Quadratic Inequalities. Closes S1-bcfetch deferred item.
3. **Unit 2 SG** (`8590923`) — 1171 lines, 7 content sections (§2.1-2.7 Parabola → Quadratic Inequalities), grade-by-region nav with 8 rows, Syllabus Map cites verbatim from all 4 extracts.
4. **Unit 2 Practice** (`db9541d`) — 407 lines, 12 questions, 90 marks, region+paper-style chips throughout.
5. **Unit 2 Solutions** (`2723050`) — 570 lines, mark-sum verified per Q, .distractor blocks for SAT MCQs, 12 quadratic-specific insights.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S1-bcfetch**~~ | Fetch BC PC11 + extract Quadratics slice | P1 | ✅ closed — `94f0988` |
| ~~**U1-how-to-use**~~ | Rework Unit 1 how-to-use into grade-by-region nav with source citations | P0 | ✅ closed — `b37a192` (template locked for Units 2-15) |
| ~~**S2-SG**~~ | Draft Unit_2_Quadratic_Functions_and_Equations.html | P0 | ✅ closed — `8590923` |
| ~~**S2-P**~~ | Draft Unit_2_..._Practice.html | P0 | ✅ closed — `db9541d` |
| ~~**S2-S**~~ | Draft Unit_2_..._Solutions.html | P0 | ✅ closed — `2723050` |
| ~~**S2-index**~~ | Re-run scripts/build-index.py to surface Unit 2 card in landing page | P1 | ✅ closed — this commit |

**Sprint 2 deliverable contract met:** 8-row grade-by-region nav (vs. Unit 1's 8 rows); BC PC11 column populated in Syllabus Map; 7 content sections each with cheat-sheet + worked example + going-deeper + quiz mix; 14 flashcards; 12 readiness items; 5 feeder-links.

**Locked Sprint 3+ template:** how-to-use grade-by-region nav structure is now the standing pattern. Future Units 3-15 follow it.

---

### Sprint 1 — Unit 1 Linear Functions and Systems (full triplet) — **CLOSED 2026-05-25** (branch `high_school_math_unit_1`)

**Closed 2026-05-25**. 4 P0 items shipped in 4 commits + 1 audit-seed + 1 close-out = 6 commits total. **Unit 1 is live on `main`** with all three product formats (SG + Practice + Solutions) and the new subject card visible on the landing page.

Locked Sprint 2+ template artifacts from this sprint:
- CSS classes: `.syllabus-map`, `.syllabus-map-label`, `.syllabus-map-grid`, `.region-header`, `.region-chip`, `.syllabus-note`, `.honors-flag`, `.feeder-link`, `.pill.region`, `.pill.paper`, `.pill.honors`, `.syllabus-strip`, `.q-body ol.mcq` (Practice), `.distractor` (Solutions MCQ rationales)
- Chip taxonomy: region flag + paper-style chips on every Practice question
- Three-layer curriculum chrome: syllabus-map (top of unit) + region-chip (per section) + syllabus-note (inline, sparing)
- Honors-flag pattern for advanced sections (BC PC12 / ON MCV4U / ON MCR3U+ honors-only content)
- Feeder-link pattern for AP/IB cross-references
- MCQ distractor pattern (Solutions explains why each wrong choice fails in 1 line)

### Sprint 1 (active scope, now closed) — original deliverable list:

**Goal.** Ship the first full HS Math product (Study Guide + Practice +
Solutions) for **Unit 1: Linear Functions and Systems**. Proves all
three product templates in one sprint so Sprint 2 can bulk-draft Units
2-6 from validated designs.

**Locked decisions** (user 2026-05-25 consultation):

- **Regions:** 3 columns — 🇺🇸 US Common Core, 🇨🇦 Ontario, 🇨🇦 British
  Columbia. Alberta dropped from current scope.
- **Chip taxonomy on Practice questions:** **Region flag + paper style**.
  Each question carries (a) a region chip (`🇺🇸 US` / `🇨🇦 ON` /
  `🇨🇦 BC`) and (b) a paper-style chip (`SAT-style MCQ`, `AP-feeder FRQ`,
  `ON Provincial-style`, `BC Provincial-style`). Students drilling for
  a specific exam filter by chip. Mirrors IB Math HL's Paper 1A/1B/2/3
  chip system.
- **Three-layer curriculum-callout structure inside each SG:**
  1. *Top of unit:* `syllabus-map` callout box (3 columns: US/ON/BC,
     country flag + course code + standard reference).
  2. *Per-section:* small region-/grade chip where the section diverges
     from "core for everyone" (e.g. `🇨🇦 BC PC12 honors`,
     `🇨🇦 ON MHF4U`, `🇺🇸 not in CCSSM — AP/IB feeder`).
  3. *Inline:* `syllabus-note` callout only where a single curriculum
     requires a different proof / different terminology / different
     exam expectation. Sparingly.
- **Vectors Unit 14:** keep as thin ON-MCV4U-focused unit; deep-content
  students hyperlinked to existing
  `IB Math HL/Study Guides/Unit_C3_Vectors.html`.

**Sprint 1 deliverable contract:**

- ≥6 content sections following the dual-goal contract (cheat-sheet →
  worked example → going-deeper → quiz mix).
- `syllabus-map` callout near hero (3-column US/ON/BC, code-cited from
  the verbatim `*_extract.md` slices in `rag/sources/`).
- `syllabus-note` callouts where genuine divergence (US Common Core's
  HSF-LE.A.4 modeling vs. ON MPM1D's analytic-geometry framing, etc.).
- `honors-flag` chips on the few sections that are honors / advanced
  (linear systems via matrix row-reduction reads as honors in ON;
  parametric form of a line reads as honors in BC PC12).
- 8+ flashcards in the locked terse style.
- 10+ item readiness checklist.
- AP/IB feeder pointers — hyperlinks to existing AP Calc / IB Math HL
  units where a topic feeds in.
- English-only (per spec — no ZH track until subject stabilises).
- `scripts/validate.sh` exit 0.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0.5-4**~~ | Define `syllabus-map`, `syllabus-note`, `honors-flag` CSS classes | P1 | ✅ closed — folded into `dc2548a` (Unit 1 SG) |
| ~~**S1-SG**~~ | Draft `Unit_1_Linear_Functions_and_Systems.html` (Study Guide) | P0 | ✅ closed — `dc2548a` (1069 lines, 7 sections, 17 quizzes, 12 flashcards, 13 checklist items, all syllabus codes verified) |
| ~~**S1-P**~~ | Draft `Unit_1_Linear_Functions_and_Systems_Practice.html` (Practice) | P0 | ✅ closed — `b6fac9c` (407 lines, 12 questions, 91 marks, region+paper-style chip taxonomy locked) |
| ~~**S1-S**~~ | Draft `Unit_1_Linear_Functions_and_Systems_Solutions.html` (Solutions) | P0 | ✅ closed — `f61b9c3` (572 lines, 12 questions, all mark-callouts sum to declared marks, .distractor block for MCQ Solutions locked) |
| ~~**S1-index**~~ | Update `scripts/build-index.py` to discover the new subject; add subject-group blocks to index.html | P1 | ✅ closed — this commit; build-index.py SUBJECTS now lists 7 subjects (added HS Math + IB Physics HL); ensure_sentinels extended to support tiered subject-group anchors; index.html tier 1 + tier 2 seeded with subject-group blocks; HS Math Unit 1 + IB Physics HL A.1 cards now visible on landing page |
| **S1-bcfetch** | Fetch BC `pc11_elab.pdf` + `pc12_elab.pdf` into `rag/sources/bc/`; write topic-slice extracts for Quadratics + Polynomial + Exp/Log + Sequences (unblocks Sprint 2) | P1 | **Deferred to Sprint 2** — Unit 1 didn't need it; ship at start of Sprint 2 before bulk-drafting Units 2-6 |

Build order: **S1-SG → S1-P → S1-S → S1-index** (per-item commits).
S1-bcfetch can run in parallel.

---

### Closed Sprints

#### Sprint 0.5 — closed 2026-05-17

Source-grounding + first unit choice. All 4 priority PDFs (US, BC PC10,
ON 9-10, ON 11-12) fetched and Linear-Functions extracts written via
`pdftotext -layout` from Poppler (located at `/mingw64/bin/pdftotext`
inside the sandbox).

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0.5-1**~~ | Add CCSSM HS row to `sources.txt` | P0 | ✅ shipped 2026-05-16 (`ecbc87a`, row 13) |
| ~~**S0.5-2a**~~ | Fetch 4 priority PDFs into `rag/sources/` | P0 | ✅ shipped 2026-05-16 |
| ~~**S0.5-2b**~~ | Extract Linear-Functions text into `*_extract.md` | P0 | ✅ shipped 2026-05-17 (`31c0fb5`) |
| ~~**S0.5-3**~~ | Pick Unit 1 topic | P0 | ✅ 2026-05-16 — **Linear Functions and Systems** |

### Extracts produced

All four `*_extract.md` companions now sit next to the source PDFs.
Each is the verbatim Linear-Functions / Linear-Systems slice of its
source, formatted so the Unit 1 Syllabus Map can cite codes directly.

| # | Region | Source PDF | Extract |
|---|---|---|---|
| 1 | 🇺🇸 US | `rag/sources/us/ccssm_hs_math.pdf` | `rag/sources/us/ccssm_hs_math_extract.md` — HSN-Q, HSA-SSE, HSA-CED, HSA-REI (A/B/C/D linear-relevant), HSF-IF, HSF-BF, HSF-LE |
| 2 | 🇨🇦 BC | `rag/sources/bc/fmpc10_elab.pdf` | `rag/sources/bc/fmpc10_elab_extract.md` — Big Idea #3 + Content strands *functions and relations*, *linear functions*, *arithmetic sequences*, *systems of linear equations* with full elaborations |
| 3 | 🇨🇦 ON | `rag/sources/on/math_grades_9-10.pdf` | `rag/sources/on/math_grades_9-10_extract.md` — MPM1D Linear Relations strand, MPM1D Analytic Geometry strand, MPM2D Analytic Geometry strand |
| 4 | 🇨🇦 ON | `rag/sources/on/math_grades_11-12.pdf` | `rag/sources/on/math_grades_11-12_extract.md` — MCR3U strand A (linear-touching expectations A1.1–A1.9, A2.5), strand B (B2.1), strand C (arithmetic-sequences-as-linear-growth) |

**Extraction tool note:** `pdftotext -layout` from Poppler (located at
`/mingw64/bin/pdftotext`) works inside the sandbox; the failure earlier
was specifically the Read tool's reliance on `pdftoppm` for image
rendering, which is absent. For future PDF source-grounding work, go
straight to `pdftotext` via Bash.

**Optional later additions** (don't block Unit 1, but useful for later units):

| # | Region | Source URL (in `sources.txt`, row #) | Why later |
|---|---|---|---|
| 5 | 🇨🇦 BC | row 02 — `bc/pc11_elab.pdf` | Drives Units 2–6 (quadratics, exp/log, sequences, trig basics) |
| 6 | 🇨🇦 BC | row 03 — `bc/pc12_elab.pdf` | Drives Units 5–12 (function families, trig identities, combinatorics) |
| 7 | 🇨🇦 AB | row 07 — `ab/pos_10-12_indicators.pdf` | One doc covering AB Math 10C / 20-1 / 30-1 — needed to add the AB column to every Unit's Syllabus Map |
| 8 | 🇨🇦 AB | row 09 — `ab/math10c_standards.pdf` | Granular Math 10C assessment standards; useful but Math 30-1 is higher leverage |

**Alberta gap.** Unit 1's Syllabus Map will be missing its AB column
until at least row 7 (the AB Program of Studies) is fetched and a
`pos_10-12_indicators_extract.md` is written. Either fetch now in a
separate Sprint 0.5 follow-on, or ship Unit 1 with a 3-column Syllabus
Map (US/ON/BC) and add the AB row in a follow-up commit.

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
| 1   | Linear Functions and Systems            | 7 | &mdash; | 17 | shipped (Sprint 1) |
| 2   | Quadratic Functions and Equations       | 7 | &mdash; | &mdash; | shipped (Sprint 2) |
| 3   | Polynomial Functions                    | 7 | &mdash; | 21 | shipped (Sprint 3) |
| 4   | Rational and Radical Expressions        | 7 | &mdash; | 22 | shipped (Sprint 3) |
| 5   | Exponential and Logarithmic Functions   | 7 | &mdash; | 24 | shipped (Sprint 3) |
| 6   | Sequences and Series                    | 7 | &mdash; | 21 | shipped (Sprint 3) |
| 7   | Right-Triangle Trigonometry             | &mdash; | &mdash; | &mdash; | **Sprint 4 queued** |
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
