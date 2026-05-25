# IB Math AA HL — Audit

Open punch list for the IB Math AA HL study guides, scored against
[`prompts/create-unit.md`](../prompts/create-unit.md) (the dual-goal contract)
and the IB Math AA HL syllabus (first assessment **2029** — switched from
2021 on 2026-05-22 once the IB Subject Brief landed in
`rag/sources/IB Math HL/`).

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "going for a 7" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope** — this audit covers the *Study Guide*, *Practice Questions*, and
*Solutions* products for IB Math AA HL. IB Math AI HL has its own audit
(to be created when AI HL drafting begins; spec lives at
`rag/subjects/ib_math_ai_hl.md`).

Last reviewed: **2026-05-24** (Topic A 100% closed — A5 P+S shipped
`d0839fa`, 8 Qs / 63 marks, EN+ZH built in. Topic A is now 5/5
super-topics fully complete across all 4 deliverables). Greenfield
focus shifts to Topic E (calculus — most-tested AA HL topic).

---

## Active Sprint — what we're working on now

### 🎯 Immediate focus (relocked 2026-05-24 after Topic A 100% closure)

1. ~~**Topic D Practice + Solutions.**~~ ✅ EN drafts all shipped
   2026-05-22. ZH translation pass for the 6 Topic D P+S files still
   open — handled in a combined D+A translation pass.
2. ~~**Complete Combinatorics (A3).**~~ ✅ closed 2026-05-23.
3. ~~**Close Topic A 100%.**~~ ✅ closed 2026-05-24 via A5 P+S
   (`d0839fa`, 8 Qs / 63 marks, EN+ZH built in). Topic A is now 5/5
   super-topics × 4 deliverables — fully shipped.
4. **Open Topic E greenfield (E1 → E4).** Calculus is the most-tested
   AA HL topic on Paper 2; greatest student impact. E1 (principles of
   differential calculus) opens the topic.
5. **Open Topic B greenfield (B1 → B5).** Functions; foundational for
   calculus.

### Sprint 3 — Complete the 2029 units (opened 2026-05-22)

**Goal.** Every 2029 super-topic ships as one unit with 4 deliverables:
Study Guide, Practice Questions, Solutions, ZH translation.
**22 super-topics × 4 = 88 deliverables** total scope.

**Syllabus authority — locked.** 2029 AA HL super-topic structure
(see `rag/subjects/ib_math_aa_hl.md` and
`rag/sources/IB Math HL/sb_maths_analysis_en.pdf`):
- **Topic A** Number and Algebra: A1, A2, A3, A4 (HL), A5
- **Topic B** Functions: B1, B2, B3, B4, B5
- **Topic C** Geometry: C1, C2, C3 (HL)
- **Topic D** Statistics and Probability: D1, D2, D3
- **Topic E** Calculus: E1, E2, E3, E4, E5 (HL), E6 (HL)

**Cadence.** Per the locked review-then-merge pattern, each Study Guide
ships as its own commit. Practice + Solutions follow per unit.
ZH translation pass per the locked English-first → ZH playbook.

**Sub-topic mapping retained.** The 2021 sub-topic numbering (1.1, 1.2,
…, 5.18) is preserved in `rag/subjects/ib_math_aa_hl.md` as a mapping
table — useful while the full 2029 sub-bullet enumeration is pending and
while legacy units (drafted against 2021) remain on disk.

#### Sprint 3 deliverable grid — 22 super-topics

Status legend per cell: `⬜` unbuilt · `🟡` partial (in legacy combined unit) · `📁` covered by legacy combined unit · `✅` shipped

##### Topic A — Number and Algebra (5 super-topics)

| ID | Super-topic | SL/AHL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **A1** | Sequences | SL + AHL | ✅ | ✅ | ✅ ¹ | ✅ |
| **A2** | Exponents and logarithms | SL + AHL | ✅ ² | ✅ ² | ✅ ² | ✅ ² |
| **A3** | Combinatorics | SL + AHL | ✅ | ✅ | ✅ | ✅ |
| **A4** | Complex numbers (HL only) | AHL | ✅ | ✅ ³ | ✅ ³ | ✅ |
| **A5** | Proof and algebraic manipulation | SL + AHL | ✅ ⁴ | ✅ ⁵ | ✅ ⁵ | ✅ ⁵ |

¹ A1 Solutions shipped 2026-05-23 (`52d1f55`) — 11 Qs / 87 marks,
EN+ZH, mirroring the A3 Solutions template. Closed the
Solutions-surface parity gap.

² A2 SG shipped 2026-05-23 (`f9be199`, 1001 lines, 6 sections,
covers 2021 1.5/1.7). A2 P+S shipped same day (`cd96f3f`) — 8 Qs /
62 marks, EN+ZH built in. Topic A2 fully closed.

³ A4 P+S shipped 2026-05-23 (`1bfaff4`) — 8 Qs / 67 marks, EN+ZH
built in. A4 SG ZH was already in via T-3.

⁴ A5 SG shipped 2026-05-23 (`cc943a4`, 1068 lines, 6 sections,
covers 2021 1.6/1.11/1.15/1.16).

⁵ A5 P+S shipped 2026-05-24 (`d0839fa`) — 8 Qs / 63 marks, EN+ZH
built in. Covers all 6 SG sections: 1.6 direct/contradiction (Q1, Q2),
1.15 induction (Q3 sum identity, Q4 divisibility), 1.11 partial
fractions + telescoping (Q5), 1.16 3×3 systems (Q6 unique solution,
Q7 parametric consistency), 1.15 Paper 3 Fibonacci strong induction +
Binet (Q8). **Topic A is now 5/5 super-topics fully closed across all
4 deliverables.**

##### Topic B — Functions (5 super-topics)

| ID | Super-topic | SL/AHL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **B1** | Representation of functions | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B2** | Polynomial functions | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B3** | Functions with asymptotes | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B4** | Trigonometric functions | SL + AHL | 🟡 ³ | ⬜ | ⬜ | 🟡 ³ |
| **B5** | Transformations of graphs and functions | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |

³ B4 partial via `Unit_C_Geometry.html` §§C2.4–C2.10 (unit circle,
identities, circular functions, solving trig equations). Standalone B4
unit not yet drafted.

##### Topic C — Geometry (3 super-topics)

| ID | Super-topic | SL/AHL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **C1** | Surface areas, volumes and measurement in circles | SL | 🟡 ⁴ | ⬜ | ⬜ | 🟡 ⁴ |
| **C2** | Trigonometry and its applications | SL | 🟡 ⁴ | ⬜ | ⬜ | 🟡 ⁴ |
| **C3** | Vectors (HL only) | AHL | ⬜ | ⬜ | ⬜ | ⬜ |

⁴ C1 + C2 partial via `Unit_C_Geometry.html` (3D distance / volumes /
surface areas / radian / arc / sector for C1; right-angled trig /
sine / cosine rules / bearings for C2). Standalone units not yet
drafted.

##### Topic D — Statistics and Probability (3 super-topics)

| ID | Super-topic | SL/AHL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **D1** | Univariate data (univariate + bivariate) | SL | ✅ | ✅ | ✅ | ✅ ⁵ |
| **D2** | Probability | SL + AHL | ✅ | ✅ | ✅ | ✅ ⁵ |
| **D3** | Probability distributions | SL + AHL | ✅ | ✅ | ✅ | ✅ ⁵ |

⁵ Study Guide ZH complete (`148fa51`, `231f6e8`, `0f84a70`). Practice +
Solutions EN drafts shipped 2026-05-22. ZH pass for the 6 P+S files
still open — deferred to a combined D+A translation batch.

##### Topic E — Calculus (6 super-topics)

| ID | Super-topic | SL/AHL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **E1** | Principles of differential calculus | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E2** | Techniques of differential calculus | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E3** | Techniques of integral calculus | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E4** | Problem-solving using calculus | SL + AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E5** | Differential equations (HL only) | AHL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E6** | Maclaurin series (HL only) | AHL | ⬜ | ⬜ | ⬜ | ⬜ |

#### Topic D sub-sprint — Practice + Solutions (🎯 immediate, opened 2026-05-22)

**Deliverable contract per super-topic.** Two HTML files in the existing
folders:

```
IB Math HL/Practice Questions/Unit_<D1|D2|D3>_<Slug>_Practice.html
IB Math HL/Practice Questions/Solutions/Unit_<D1|D2|D3>_<Slug>_Solutions.html
```

Each ships English-first per the locked cadence, then a ZH pass per
`prompts/create-bilingual-translation.md`. Reference templates:
`Unit_A1_Sequences_and_Series_Practice.html` (Practice),
`Unit_A3_Combinatorics_Solutions.html` (Solutions, mark-by-mark
M1/A1/R1 callouts).

**Paper mix per super-topic** — EMH (Easy / Medium / Hard) across:
- **Paper 1A** short response, no calc
- **Paper 1B** extended response, no calc
- **Paper 2** calculator
- **Paper 3** HL extended exploration (relevant for D2 + D3 since both
  contain AHL content; D1 is SL-only)

| ID | Super-topic | SL/AHL | Practice | Solutions | ZH (P+S) |
|---|---|---|---|---|---|
| **S3-D1** | D1 Univariate data | SL | ✅ `f3c371e` | ✅ `50fd2ea` | ⬜ |
| **S3-D2** | D2 Probability | SL + AHL | ✅ `612071c` (+ Paper 3 Q12 `fcf74e6`) | ✅ `68ef8f3` | ⬜ |
| **S3-D3** | D3 Probability distributions | SL + AHL | ✅ `49b2dcc` (+ Paper 3 Q12 `f9dbea4`) | ✅ `22ff5f1` | ⬜ |

**Sub-sprint roll-up.** EN drafts 6/6 ✅. ZH for the 6 P+S files
remaining — bundled into the next combined D+A translation batch.

#### Sprint 3 priority order (refreshed 2026-05-24 after Topic A 100% closure)

1. ~~**Topic D Practice + Solutions** (S3-D1 → S3-D3)~~ ✅ EN drafts
   shipped 2026-05-22. ZH pass remaining (6 files, bundled into next
   D+A translation batch).
2. ~~**Complete A3 Combinatorics**~~ ✅ closed 2026-05-23.
3. ~~**Legacy unit retrofit — `.ib-ref` chips on A1 / A3 / A4 / Unit_C.**~~
   ✅ shipped 2026-05-23 in `e30142c`.
4. ~~**A5 Proof and Algebraic Manipulation** Study Guide~~ ✅ shipped
   2026-05-23 (`cc943a4`).
5. ~~**A2 Exponents and Logarithms** Study Guide + P+S~~ ✅ shipped
   2026-05-23. Topic A2 fully closed.
6. ~~**A5 Practice + Solutions**~~ ✅ shipped 2026-05-24 (`d0839fa`,
   8 Qs / 63 marks, EN+ZH built in). **Topic A 100% closed.**
7. **E1 Principles of differential calculus** — opens Topic E. Calculus
   is the most-tested AA HL topic on Paper 2; biggest student-impact
   greenfield work. **Next up.**
8. **E2 → E4** — rest of SL+AHL differential and integral calculus.
9. **B1 Representation of functions** — opens Topic B. Underpins
   calculus.
10. **B2 → B5** — rest of functions.
11. **C3 Vectors (HL only)** — geometry HL component.
12. **B4 / C1 / C2 standalone splits** — extract from `Unit_C_Geometry.html`;
    triggers Unit_C retirement once all three ship.
13. **E5 / E6** — HL-only calculus (differential equations, Maclaurin).
14. **Topic D ZH translation batch** — 6 P+S files (deferred ZH from
    Sprint 3 priority #1).
15. **Practice + Solutions** — drafted in batch after each SG lands,
    bilingual built-in per the A2/A5 pattern.

### Sprint 2 follow-up — Unit_C monolith polish (kept open)

These rows apply to the existing `Unit_C_Geometry.html` monolith which
remains in production until B4 + C1 + C2 units all ship (the three
2029 super-topics it currently straddles). The polish work below makes
Unit_C consistent with A1/A3/A4 during the transition window. Each row
will be marked closed-by-split once the corresponding super-topic units
replace the monolith section.

### Sprint 2 — Worked examples / exam tips / sliders (opened 2026-05-21)

Audit-driven sprint per the user-locked 3-vector improvement focus
(see `rag/study-guide-audit-checklist.md` Section E). **English-first**:
each item lands as an English revision commit, user reviews, then the
Mandarin follow-up commit picks up the same file per
`prompts/create-bilingual-translation.md`.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-1** | **Unit C** `Unit_C_Geometry.html`: surface worked examples — unwrap `<details><summary>Worked Example — …</summary>` blocks so they're visible by default (sibling parity with A1/A3/A4). Reserve `<details>` for "Going deeper" proofs only. (E1 / B2) | P0 | **Open** |
| **S2-2** | **Unit C**: add worked example + quiz to crammer-only topic sections — C1.3 Radian Measure, C2.1 SOHCAHTOA, C2.3 Bearings, C2.4 Unit Circle, C2.10 Symmetry. Add quiz to C2.6 Reciprocal/Inverse and C3.3 Vector Eqn of Line. (E1 / B2) | P1 | **Open** |
| **S2-3** | All 4 units: per-major-topic exam-tip callout (E2). A1/A3/A4 have some "AP-style" strategy callouts — extend to every topic with concrete IB-paper guidance (Paper 1 calc vs Paper 2, HL-only flagging, command-term hints, "what graders look for"). Unit C has none. | P1 | **Open** |
| **S2-4** | **Unit C**: page-fill / column-parity audit (A14). Unit C predates the A1/A3/A4 layout pattern; verify `.main-wrap` / `--max-w` / sidebar mode match siblings. | P2 | **Open** |
| **S2-5** | Slider widget candidates (E3): IB Math HL currently has zero widgets. High-leverage one-slider-one-concept: GP convergence ratio slider (A1.6), Pascal-triangle row slider (A3.5), Argand diagram angle slider (A4 polar form), arc-length on unit circle (C2.4). Each = single slider, one observable. | P2 | **Open** |

**Deferred to bilingual follow-up** (per English-first gate locked
2026-05-21):

- Theme persistence via `localStorage` (A5 — all 4 files).
- HL-flagging migration to inline chips on Unit C (C2 — currently uses
  text suffix; siblings use `<span class="hl-flag">HL</span>`).
- `#how-to-use` section addition for Unit C.
- Unit C flashcard density boost (12 → ~16).
- Unit A3.5 add labelled worked-solution block.

### Translation Sprint Wave 2 — Practice Questions & Solutions — CLOSED 2026-05-22

Bilingual EN↔ZH pass over the IB Math AA HL Practice Questions and
Solutions surfaces, extending Wave 1 (Study Guides A1/A3/A4/C) which
closed 2026-05-21. **First subject to close Wave 2** — the 3-file set
shipped on branch `wave2_ib_math_hl` and is ready for fast-forward
into `main` for customer deploy.

| ID | Item | Tier | Status | EN/ZH balance |
|---|---|---|---|---|
| ~~**W2-EN**~~ | ~~EN hygiene sweep across all 3 Practice/Solutions files~~ | P1 | ✅ **No-op** — zero CJK characters across all 3 files (no `\text{...}` collision risk), em dashes are paper-chrome convention (legitimate), no AI-voice drift. No changes needed. | — |
| ~~**W2-1**~~ | ~~`Practice Questions/Unit_A1_Sequences_and_Series_Practice.html`~~ | P1 | ✅ closed — `89b8a12` | 67 / 67 ✅ |
| ~~**W2-2**~~ | ~~`Practice Questions/Unit_A3_Combinatorics_Practice.html`~~ | P1 | ✅ closed — `bd62129` | 76 / 76 ✅ |
| ~~**W2-3**~~ | ~~`Practice Questions/Solutions/Unit_A3_Combinatorics_Solutions.html`~~ | P1 | ✅ closed — `2dce66c` | 51 / 51 ✅ |

**Audience contract** — Mandarin-Chinese-language students preparing
to write the IB Math AA HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terms remain in `<code>` glosses
inside the Chinese prose. Math notation untouched.

**Form choice** — Practice files use inline `<span data-lang="en">…</span><span data-lang="zh">…</span>`
pairs throughout. The Solutions file uses Form B (parallel
`<div class="rationale" data-lang="en">…</div><div class="rationale" data-lang="zh">…</div>`)
for the 12 worked-solution blocks because each has internal h4 / list /
insight structure that's cleaner as a parallel block than as inline
spans. Inline span pairs still used for prompts, answer lines,
paper-header pills, and footer in the Solutions file.

**`scripts/validate.sh`** passes on all 3 files.

**Commits on `wave2_ib_math_hl`:**

- `89b8a12` — W2-1 A1 Practice ZH translation (67/67, +81/−66)
- `bd62129` — W2-2 A3 Practice ZH translation (76/76, +90/−75)
- `2dce66c` — W2-3 A3 Solutions ZH translation (51/51, +353/−51)

**Note — out of Wave 2 scope (build, not translate).** Practice +
Solutions files for A2 / A4 / A5 / B / D / E (SQ-4 above) do not exist
yet; they ship bilingual end-to-end under the locked English-first → ZH
cadence as each one lands.

### Closed (Translation Sprint Wave 1 — closed 2026-05-21)

All currently-shipped IB Math HL study guides (A1, A3, A4, C)
bilingualized EN↔ZH. Branch `ib_math_hl_translation` fast-forwarded
to `main`.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**T-1**~~ | Unit A1 Sequences &amp; Series bilingual translation | P1 | ✅ closed — `cdca220` |
| ~~**T-2**~~ | Unit A3 Combinatorics bilingual translation | P1 | ✅ closed — `ea3124d` |
| ~~**T-3**~~ | Unit A4 Complex Numbers bilingual translation | P1 | ✅ closed — `12dc6ad` (+ Argand-gloss polish in follow-up) |
| ~~**T-4**~~ | Unit C Geometry bilingual translation | P1 | ✅ closed — `ebf8d11` |

### Sprint 1 — Refactor Unit A into focused sub-units (partial)

**Sprint 1 — Refactor Unit A into focused sub-units.** The original
`Unit_A_Number_and_Algebra.html` is a 2588-line monolith covering 24
sub-topics. Per 2026-05-08 decision, it's being split into focused
sub-units. Under the 2029 super-topic structure (locked 2026-05-22), the
6-unit split collapses into a **5-unit split** matching 2029 Topic A:
**A1, A2, A3, A4, A5** — Sprint 1's S1-5 (Proof) and S1-6 (Algebra & Systems)
merge into the single super-topic A5 "Proof and algebraic manipulation."

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S1-1**~~ | Draft `Unit_A1_Sequences_and_Series.html` | P0 | ✅ **Shipped 2026-05-08** — 8 sections, 18 quiz items, 12 flashcards, 14-item readiness checklist. Introduces the `cram-cheat` CSS pattern + `hl-flag` chip. |
| ~~**S1-2**~~ | Draft `Unit_A2_Exponents_and_Logarithms.html` (2029 A2 — covers 2021 1.5, 1.7) | P0 | ✅ **Shipped 2026-05-23** — `f9be199`, 1001 lines, 6 content sections (Integer Exponents, Rational Exponents, Log Laws, Change of Base, Solving Eq, Growth/Decay). EN+ZH built in. |
| ~~**S1-3**~~ | Draft `Unit_A3_Combinatorics.html` | P0 | ✅ **Shipped 2026-05-09** — 6 sections, 16 quizzes total, 12 flashcards, 14-item readiness checklist. Renamed from "Counting & Binomial" to user's preferred "Combinatorics." |
| ~~**S1-4**~~ | Draft `Unit_A4_Complex_Numbers.html` | P0 | ✅ **Shipped 2026-05-15** — 6 sections, 16 quizzes total, 14 flashcards, 14-item readiness checklist. Includes Argand SVG components. |
| ~~**S1-5-and-6**~~ | Draft `Unit_A5_Proof_and_Algebraic_Manipulation.html` (2029 A5 — covers 2021 1.6, 1.11, 1.15, 1.16) | P0 | ✅ **Shipped 2026-05-23** — `cc943a4`, 1068 lines, 6 content sections (Direct Proof, Contradiction, Induction HL, Partial Fractions HL, 3×3 Systems HL, RREF HL). EN+ZH built in. Collapses 2021 S1-5 + S1-6 per the 2029 boundary. |
| **S1-7** | Remove old `Unit_A_Number_and_Algebra.html` + update `index.html` cards | P1 | 🟡 **Partial 2026-05-15** — file moved to `rag/archive/Unit_A_Number_and_Algebra.html` (stripped from deploy by `deploy.yml`); Unit A card dropped from `index.html`. Full deletion now unblocked since A2 + A5 SGs shipped. |

Build order under the 2029 collapse: **A1 (✓) → A3 (✓) → A4 (✓) → A2 (✓) → A5 (✓ SG; P+S pending) → S1-7 cleanup**.

#### A3 completion row (immediate task #2) — ✅ closed 2026-05-23

| ID | Item | Tier | Status | Resolution |
|---|---|---|---|---|
| ~~**A3-complete**~~ | Define and finish "complete Combinatorics (A3)" | P0 | ✅ closed | Path (b) + (c) executed. (b) Paper 3 Q13 (Vandermonde + sum-of-squares, 16 marks) added to A3 Practice in `832e7e7` (bumping A3 Practice to v1.2 / 13 Qs / 116 marks); legend chip and topics-line follow-on syncs in `7922014` and `6f5a257`. (c) A1 Solutions drafted in `52d1f55` (11 Qs / 87 marks, EN+ZH) — closes the Solutions-surface parity gap. Path (a) deferred until IB publishes the full AA HL 2029 sub-bullet enumeration. |

### Practice Questions sub-stream

Parallel build-out of IB-style practice files in `Practice Questions/`,
mirroring the AP Physics pattern but adapted for IB paper structure
(Paper 1A short / Paper 1B extended / Paper 2 calc / Paper 3 HL). Each
question carries difficulty (Easy/Medium/Hard), paper, syllabus topic,
and mark allocation pills. Question-only — no embedded answers.

| ID | Item | Status |
|---|---|---|
| ~~**SQ-1**~~ | `Practice Questions/README.md` + locked conventions | ✅ Shipped 2026-05-09 |
| ~~**SQ-2**~~ | `Unit_A1_Sequences_and_Series_Practice.html` (11 Qs, 87 marks) | ✅ Shipped 2026-05-09 (now also has Solutions companion `52d1f55`) |
| ~~**SQ-3**~~ | `Unit_A3_Combinatorics_Practice.html` (13 Qs, 116 marks at v1.2) | ✅ Shipped 2026-05-09; Q13 Paper 3 added 2026-05-23 (`832e7e7`) |
| **SQ-4** | Practice files for A2 / A4 / A5 / B (all 5) / D1-D3 / E (all 6) | 🟡 **Partially closed.** ✅ A2 (`cd96f3f`), A4 (`1bfaff4`), A5 (`d0839fa`), D1/D2/D3 (P+S EN drafts 2026-05-22). ⬜ Remaining: B (all 5), C (all 3), E (all 6). |

### Sprint 2 — New super-topic units (Topic D shipped 2026-05-22)

Sprint 2 picked up the missing super-topic units (Functions, Statistics &
Probability, Calculus). Under the 2029 collapse: **B Functions** splits
into B1-B5, **E Calculus** splits into E1-E6, **D Statistics &
Probability** stays as the already-shipped D1/D2/D3 (clean match).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-D1** | Draft `Unit_D1_Univariate_Data.html` covering 2021 SL 4.1, 4.2, 4.3, 4.4 (univariate descriptive + bivariate correlation/regression — 2029 AA D1 includes bivariate) | P0 | ✅ **Shipped 2026-05-22** — 2092 lines, 7 sections each tagged with its official IB sub-topic via `.ib-ref` chip in h2. Commit `f8db91f`. |
| **S2-D2** | Draft `Unit_D2_Probability.html` covering 2021 SL 4.5, 4.6, AHL 4.10 | P0 | ✅ **Shipped 2026-05-22** — 1810 lines, 7 sections. Section 2.7 Bayes is HL-only. Commit `4a74130`. |
| **S2-D3** | Draft `Unit_D3_Probability_Distributions.html` covering 2021 SL 4.7, 4.8, 4.9, AHL 4.11 | P0 | ✅ **Shipped 2026-05-22** — 1992 lines, 8 sections (densest of the 3). Cram cheat-sheet splits SL · CORE from HL · AHL ONLY. Commit `8bb208a`. |
| **S2-D-index** | Add D1/D2/D3 cards to `index.html` IB Math AA HL section (manual edit) | P1 | ✅ **Shipped 2026-05-22** — count chip updated to "7 units" / "7 个单元". Commit `c03cc67`. |
| **S2-B-greenfield** | Draft 5 B-super-topic units: B1 Representation of functions, B2 Polynomial functions, B3 Functions with asymptotes, B4 Trigonometric functions (partial via Unit_C), B5 Transformations of graphs and functions | P0 | **Open — 5 units total** |
| **S2-E-greenfield** | Draft 6 E-super-topic units: E1 Principles, E2 Techniques (diff), E3 Techniques (int), E4 Problem-solving, E5 Differential equations (HL), E6 Maclaurin (HL) | P0 | **Open — 6 units total** |
| ~~**S2-D-translate**~~ | Bilingual ZH translation of `Unit_D1`, `Unit_D2`, `Unit_D3` per the locked English-first → ZH cadence | P1 | ✅ **Shipped 2026-05-22** — D1 391/391 pairs (`148fa51`), D2 281/281 pairs (`231f6e8`), D3 312/312 pairs (`0f84a70`). |
| ~~**S2-D-practice**~~ | Practice + Solutions EN drafts for D1 / D2 / D3 | P1 | ✅ **Shipped 2026-05-22** — 6 files: `f3c371e` D1 Practice, `50fd2ea` D1 Solutions, `612071c` D2 Practice (+ `fcf74e6` Paper 3 Q12 add), `68ef8f3` D2 Solutions, `49b2dcc` D3 Practice (+ `f9dbea4` Paper 3 Q12 add), `22ff5f1` D3 Solutions. ZH translation pass for the 6 files remains open. |
| **S2-build-index** | Extend `scripts/build-index.py` to preserve `<span data-lang="zh">` alongside auto-generated English title in card markup | P1 | **Open** — punted 2026-05-22 when shipping D-units. Manual-edit was used as workaround for that ship. |

---

## Translation audit (per-file, post-ship)

**Audit target.** All currently-shipped IB Math AA HL study guides
bilingualized to support a Mandarin-Chinese-language student writing the
IB exam in English. Chinese is a *teaching translation* — explains the
concept; English exam-rubric terms remain in `<code>` inline so the
student recognizes them on the exam paper. Playbook:
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).

### Per-file scorecard

| # | Unit (2029 ID) | EN/ZH balance | Glossary fit | Pedagogical | Validates | Notes |
|---|---|---|---|---|---|---|
| **A1** | Sequences | 260 / 260 ✅ | ✅ | ✅ | ✅ | T-1 shipped `cdca220`. Solutions companion shipped 2026-05-23 (`52d1f55`, bilingual built-in). |
| **A2** | Exponents & Logarithms | bilingual built-in ✅ | ✅ | ✅ | ✅ | SG `f9be199` + P/S `cd96f3f` — all three shipped EN+ZH inline on 2026-05-23. |
| **A3** | Combinatorics | 213 / 213 ✅ | ✅ | ✅ | ✅ | T-2 shipped `ea3124d`. Practice+Solutions Q13 (Paper 3) added bilingual `832e7e7`. |
| **A4** | Complex Numbers | 241 / 241 SG ✅ | ✅ | ✅ | ✅ | SG T-3 `12dc6ad`. P+S `1bfaff4` shipped 2026-05-23 bilingual built-in. |
| **A5** | Proof & Algebraic Manipulation | bilingual built-in ✅ | ✅ | ✅ | ✅ | SG `cc943a4` + P/S `d0839fa` — all three shipped EN+ZH inline (SG 2026-05-23, P/S 2026-05-24). **Topic A 100% closed.** |
| **C** (legacy: B4+C1+C2 straddle) | Geometry & Trigonometry | 356 / 356 ✅ | ✅ | ✅ | ✅ | T-4 shipped `ebf8d11`. Largest file. |
| **D1** | Univariate Data | 391 / 391 SG ✅ | ✅ | ✅ | ✅ | SG `148fa51`. P+S EN drafts shipped `f3c371e`/`50fd2ea`; P+S ZH pending. |
| **D2** | Probability | 281 / 281 SG ✅ | ✅ | ✅ | ✅ | SG `231f6e8`. P+S EN drafts `612071c`/`68ef8f3` + Paper 3 Q12 `fcf74e6`; P+S ZH pending. |
| **D3** | Probability Distributions | 312 / 312 SG ✅ | ✅ | ✅ | ✅ | SG `0f84a70`. P+S EN drafts `49b2dcc`/`22ff5f1` + Paper 3 Q12 `f9dbea4`; P+S ZH pending. |

B (all 5) / C1-C3 standalone / E (all 6) not in this audit — they have
not yet shipped. Translate as they ship under the locked English-first
→ ZH cadence.

### Translation contract — standing principle

Chinese is a teaching translation, not literal. English exam-rubric
terminology stays in `<code>` inline. Math notation untouched. See
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).

---

## Dual-Goal Philosophy

**Status:** standing principle, locked 2026-05-08. Every IB Math HL study
guide must serve two students at once:

1. **The crammer** — the student opening the guide the night before Paper 1
   or Paper 2. Target: a *last-ditch pass* (≥4 on the 1–7 scale). They skim
   the cheat-sheet boxes, scan the worked examples, and walk into the exam.
2. **The 7-chaser** — the student studying in depth. Target: a *7*. They
   want the *why* — derivations, edge cases, proof structure, HL-only
   subtleties.

Concretely, every section layers:

- **Cheat-sheet element at the top** — key formulas / "what you must know"
  callout. Lift-able in under a minute.
- **Worked examples** — canonical exam applications. Identify / Set Up /
  Execute / Evaluate (or the IB-style equivalent).
- **Going-deeper block** — derivation, proof, or subtlety. Clearly labeled
  (`box--proof`, expandable `<details>`, or a separate "Why" subsection)
  so the crammer can skip it cleanly.
- **Quiz mix** — recall items (crammer-pass) + synthesis items (7-chaser).

The full contract lives in [`prompts/create-unit.md`](../prompts/create-unit.md);
edit it there, not here.

### HL vs. SL

The guides are HL-targeted but SL students may use them. Flag HL-only
content with an inline chip or callout (e.g. `chip-purple` "HL only") so
SL students know what they can skip without missing core material.

### Calculator vs. non-calculator

Where a super-topic has a clear calc/no-calc split (most prominently in
Topic D Statistics), label it in the section or worked-example header.
Paper 1 is no-calc (AA-distinctive); Paper 2 is calc.

---

## Cross-Unit Snapshot (2029 super-topic basis)

| 2029 ID | Super-topic | Status | Notes |
|---|---|---|---|
| A1 | Sequences | ✅ shipped 2026-05-08 | 8 sections, 18 quiz items, 12 flashcards. **Full stack** (SG+P+S+ZH). |
| A2 | Exponents and logarithms | ✅ shipped 2026-05-23 | 6 sections, ~8 quiz items, 12 flashcards. **Full stack** (SG+P+S+ZH bilingual). |
| A3 | Combinatorics | ✅ shipped 2026-05-09 | 6 sections, 16 quizzes, 12 flashcards. **Full stack** (SG+P+S+ZH; P+S extended with Paper 3 Q13 on 2026-05-23). |
| A4 | Complex numbers (HL only) | ✅ shipped 2026-05-15 | 6 sections, 16 quizzes, 14 flashcards. **Full stack** (SG+P+S+ZH bilingual). |
| A5 | Proof and algebraic manipulation | ✅ shipped 2026-05-23/24 | 6 sections, 5 quiz items, 12 flashcards. **Full stack** (SG+P+S+ZH bilingual). |
| B1 | Representation of functions | open (greenfield) | — |
| B2 | Polynomial functions | open (greenfield) | — |
| B3 | Functions with asymptotes | open (greenfield) | — |
| B4 | Trigonometric functions | 🟡 partial via Unit_C | covered §§C2.4–C2.10 |
| B5 | Transformations of graphs and functions | open (greenfield) | — |
| C1 | Surface areas, volumes, measurement in circles | 🟡 partial via Unit_C | covered §§C1.1–C1.3 |
| C2 | Trigonometry and its applications | 🟡 partial via Unit_C | covered §§C2.1–C2.3 |
| C3 | Vectors (HL only) | open (greenfield) | — |
| D1 | Univariate data | ✅ shipped 2026-05-22 | 7 sections, includes bivariate |
| D2 | Probability | ✅ shipped 2026-05-22 | 7 sections, includes Bayes (HL) |
| D3 | Probability distributions | ✅ shipped 2026-05-22 | 8 sections, includes continuous RVs (HL) |
| E1 | Principles of differential calculus | open (greenfield) | — |
| E2 | Techniques of differential calculus | open (greenfield) | — |
| E3 | Techniques of integral calculus | open (greenfield) | — |
| E4 | Problem-solving using calculus | open (greenfield) | — |
| E5 | Differential equations (HL only) | open (greenfield) | — |
| E6 | Maclaurin series (HL only) | open (greenfield) | — |

**Roll-up: 8/22 super-topics shipped as standalone Study Guides (A1,
A2, A3, A4, A5, D1, D2, D3). 3/22 partial (B4, C1, C2 inside Unit_C).
11/22 entirely greenfield (B1, B2, B3, B5, C3, E1-E6).**

**Practice + Solutions cluster:** 8/8 shipped units have full P+S
(A1, A2, A3, A4, A5 — all bilingual built-in or post-translated;
D1+D2+D3 have EN P+S, ZH P+S pending). **Topic A is 100% closed across
all 4 deliverables (5/5 super-topics × 4).**

*The legacy `Unit_A_Number_and_Algebra.html` is archived under
`rag/archive/`. With Topic A now fully shipped (A1-A5 SGs + P+S all
live), S1-7 cleanup (full deletion) is fully unblocked.
`Unit_C_Geometry.html` stays in production until B4 / C1 / C2 ship,
then archives the same way.*

---

## How to Update This File

When closing a sprint item, mark it with `~~strikethrough~~` and append
`**Resolved:** {commit-sha} — {one-line note}`. When the sprint clears,
collapse the section into a single "Sprint N closed as of {date}" line and
promote the next sprint up.

When the dual-goal contract needs revision, edit it in
[`prompts/create-unit.md`](../prompts/create-unit.md) and reference the
revision here — don't fork the contract.

When a unit ships, fill in its row of the cross-unit snapshot table with
actual section/worked-example/flashcard/quiz counts.

The 2029 super-topic structure is the **status authority** in this file.
The 2021 sub-topic mapping (which legacy units cover which 2021 numbers)
lives in `rag/subjects/ib_math_aa_hl.md` and should not be duplicated
here.
