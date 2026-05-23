# IB Math AA HL — Audit

Open punch list for the IB Math AA HL study guides, scored against
[`prompts/create-unit.md`](../prompts/create-unit.md) (the dual-goal contract)
and the IB Math AA HL syllabus (first exams 2021).

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "going for a 7" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope** — this audit covers the *Study Guide* product only. Practice
question files and any future digital products are out of scope until they
exist.

Last reviewed: **2026-05-21** (`improve_study_guides` audit checkpoint —
Sprint 2 opened with worked-examples / exam-tips / sliders focus per
the user-locked 3-vector improvement direction).

---

## Active Sprint — what we're working on now

### Sprint 3 — Complete the units (opened 2026-05-22)

**Goal.** Every official IB Math AA HL sub-topic ships as a unit with
4 deliverables: Study Guide, Practice Questions, Solutions,
ZH translation. **79 sub-topics × 4 = ~316 deliverables** total scope.

**Sub-topic numbering.** Matches the official IB AA HL guide
(first exams 2021). Spec authority is `rag/subjects/ib_math_aa_hl.md`
— see that file for sub-topic titles and SL/AHL classification.

**Cadence.** Per the locked review-then-merge pattern, each Study Guide
ships as its own commit. Practice + Solutions follow per unit.
ZH translation pass per the locked English-first → ZH playbook.

**Sprint 2 status.** Topic D part of Sprint 2 is closed (D1/D2/D3
shipped 2026-05-22). S2-B (Unit B Functions) and S2-E (Unit E Calculus)
rows are **absorbed into Sprint 3's deliverable grid below** —
Topic 2 (16 sub-topics) and Topic 5 (18 sub-topics) cover the same
ground at sub-topic granularity. Legacy Sprint 2 polish items
(`S2-1` Unit C worked-examples surfacing, `S2-2` Unit C concept-box
additions, etc.) are kept in the **Sprint 2 follow-up section** below
since they apply to the existing Unit_C monolith and its retirement
is deferred until C-split units ship.

**Sub-topic-per-unit decision.** Spec adopts strict sub-topic-per-unit
granularity per user direction "use the official IB sub-topics so the
consumer can easily match it (like the APs do)". Legacy combined units
(A1, A3, A4, C, D1, D2, D3) stay shipped with their existing filenames;
retirement to `rag/archive/` happens once all their constituent
sub-topic units ship.

#### Sprint 3 deliverable grid

Status legend per cell: `⬜` unbuilt · `🟡` drafting · `📁` covered by legacy combined unit · `✅` shipped · `🌐` ZH translation done

##### Topic 1 — Number and Algebra (16 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 1.1 | SL | Scientific Notation | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.2 | SL | Arithmetic Sequences & Series | 📁 (A1) | 📁 | 📁 | ⬜ |
| 1.3 | SL | Geometric Sequences & Series | 📁 (A1) | 📁 | 📁 | ⬜ |
| 1.4 | SL | Financial Applications of GP | 📁 (A1) | 📁 | 📁 | ⬜ |
| 1.5 | SL | Exponents & Logarithms (Intro) | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.6 | SL | Simple Deductive Proof | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.7 | SL | Logarithm Laws (Rational Exp + Change of Base) | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.8 | SL | Infinite Geometric Series | 📁 (A1) | 📁 | 📁 | ⬜ |
| 1.9 | SL | Binomial Theorem (Positive Integer) | 📁 (A3) | 📁 | 📁 | ⬜ |
| 1.10 | AHL | Permutations, Combinations, Extended Binomial | 📁 (A3) | 📁 | 📁 | ⬜ |
| 1.11 | AHL | Partial Fractions | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.12 | AHL | Complex Numbers (Cartesian) | 📁 (A4) | ⬜ | ⬜ | ⬜ |
| 1.13 | AHL | Polar / Euler Forms | 📁 (A4) | ⬜ | ⬜ | ⬜ |
| 1.14 | AHL | Conjugate Roots, De Moivre, Complex Roots | 📁 (A4) | ⬜ | ⬜ | ⬜ |
| 1.15 | AHL | Proof by Induction / Contradiction | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.16 | AHL | Systems of Linear Equations | ⬜ | ⬜ | ⬜ | ⬜ |

##### Topic 2 — Functions (16 sub-topics — entirely greenfield)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 2.1 | SL | Straight Lines | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.2 | SL | Function Concepts (Domain, Range, Inverse) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.3 | SL | Graphs of Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.4 | SL | Key Features & Intersections | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.5 | SL | Composite Functions & Inverses | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.6 | SL | Quadratic Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.7 | SL | Quadratic Equations & Inequalities | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.8 | SL | Rational Functions (Linear Numerator) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.9 | SL | Exponential & Logarithmic Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.10 | SL | Solving Equations | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.11 | SL | Transformations of Graphs | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.12 | AHL | Polynomial Functions (Factor / Remainder) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.13 | AHL | Rational Functions HL | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.14 | AHL | Odd / Even / Self-Inverse Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.15 | AHL | Function Inequalities | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.16 | AHL | Graph Transformations HL (\|f(x)\|, 1/f(x), etc.) | ⬜ | ⬜ | ⬜ | ⬜ |

##### Topic 3 — Geometry and Trigonometry (18 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 3.1 | SL | 3D Geometry, Volumes, Surface Areas | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.2 | SL | Angles Between Lines / Planes | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.3 | SL | Right-Angled & Non-Right Trigonometry | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.4 | SL | Radian Measure, Arc, Sector | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.5 | SL | Unit Circle Definitions, Exact Values | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.6 | SL | Pythagorean & Double-Angle Identities | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.7 | SL | Circular Functions (Amplitude, Period, Transformations) | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.8 | SL | Solving Trig Equations | 📁 (C) | ⬜ | ⬜ | ⬜ |
| 3.9 | AHL | Reciprocal & Inverse Trig | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.10 | AHL | Compound Angle Identities | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.11 | AHL | Trig Symmetries & Relationships | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.12 | AHL | Vectors — Introduction | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.13 | AHL | Scalar Product | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.14 | AHL | Vector Equations of Lines | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.15 | AHL | Relationships Between Lines | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.16 | AHL | Vector Product (Cross Product) | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.17 | AHL | Vector Equations of Planes | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.18 | AHL | Intersections of Lines & Planes | ⬜ | ⬜ | ⬜ | ⬜ |

##### Topic 4 — Statistics and Probability (11 sub-topics — FULLY SHIPPED ✅)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 4.1 | SL | Sampling Concepts | ✅ (D1) | ⬜ | ⬜ | ✅ |
| 4.2 | SL | Data Presentation | ✅ (D1) | ⬜ | ⬜ | ✅ |
| 4.3 | SL | Central Tendency & Dispersion | ✅ (D1) | ⬜ | ⬜ | ✅ |
| 4.4 | SL | Bivariate Linear (PMCC, Regression) | ✅ (D1) | ⬜ | ⬜ | ✅ |
| 4.5 | SL | Probability Basics | ✅ (D2) | ⬜ | ⬜ | ✅ |
| 4.6 | SL | Combined Events, Conditional, Independent | ✅ (D2) | ⬜ | ⬜ | ✅ |
| 4.7 | SL | Discrete RVs, E(X) | ✅ (D3) | ⬜ | ⬜ | ✅ |
| 4.8 | SL | Binomial Distribution | ✅ (D3) | ⬜ | ⬜ | ✅ |
| 4.9 | SL | Normal Distribution | ✅ (D3) | ⬜ | ⬜ | ✅ |
| 4.10 | AHL | Bayes' Theorem | ✅ (D2) | ⬜ | ⬜ | ✅ |
| 4.11 | AHL | Variance, Continuous RVs, Linear Transforms | ✅ (D3) | ⬜ | ⬜ | ✅ |

> **Topic 4 Practice + Solutions gap.** Study Guides are shipped and
> translated, but per-sub-topic Practice / Solutions files haven't
> been built (A1 / A3 currently have Practice but no per-sub-topic
> Practice for Topic 4). Pre-existing A1 Practice, A3 Practice, A3
> Solutions cover the Topic 1 portion of Sprint 3 partially. Topic 4
> Practice + Solutions is a Sprint 3 deliverable. The bilingual ZH
> mark above reflects Study Guide translation only.

##### Topic 5 — Calculus (18 sub-topics — entirely greenfield)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 5.1 | SL | Introduction to Differentiation | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.2 | SL | Increasing & Decreasing Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.3 | SL | Power Rule & Linearity | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.4 | SL | Tangents & Normals | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.5 | SL | Anti-Differentiation | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.6 | SL | Definite Integrals | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.7 | SL | Derivative Rules (Chain, Product, Quotient, Trig/Exp/Log) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.8 | SL | Maxima & Minima | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.9 | SL | Kinematics (Differentiation) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.10 | SL | Indefinite Integrals (Reverse Chain Rule) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.11 | SL | Volumes of Revolution (x-axis) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.12 | AHL | Continuity & Differentiability | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.13 | AHL | Related Rates & Implicit Differentiation | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.14 | AHL | Concavity & Inflection | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.15 | AHL | Advanced Integration (Substitution, Parts) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.16 | AHL | y-Axis Integration & Volumes | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.17 | AHL | Differential Equations | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.18 | AHL | Maclaurin Series | ⬜ | ⬜ | ⬜ | ⬜ |

#### Sprint 3 roll-up

- **Topic 1**: 7 sub-topics 📁 covered by legacy combined units (A1 + A3 + A4); 9 ⬜ unbuilt
- **Topic 2**: 16 ⬜ unbuilt (greenfield)
- **Topic 3**: 8 📁 covered by Unit_C monolith; 10 ⬜ unbuilt (AHL 3.9–3.18)
- **Topic 4**: 11 ✅ Study Guides shipped + ZH (D1, D2, D3); Practice + Solutions ⬜ per sub-topic
- **Topic 5**: 18 ⬜ unbuilt (greenfield)

**Sprint 3 priority order** (suggested):

1. **AHL 4.11 audit fix** — verify whether `Unit_D3` §3.8 (sums of independent RVs / linear combinations of normals) is in-syllabus or off-syllabus per the AA HL guide. If off-syllabus, either trim D3 or add an explicit "enrichment beyond syllabus" callout.
2. **Topic 5 SL block** (5.1 – 5.11) — calculus is the most-tested AA HL topic on Paper 2; biggest student-impact greenfield work.
3. **Topic 2 SL block** (2.1 – 2.11) — functions underpin calculus and trigonometry; second-priority greenfield.
4. **Topic 3 AHL block** (3.9 – 3.18) — vectors is HL-distinctive content; Unit_C currently leaves it uncovered.
5. **Topic 1 gaps** (1.1, 1.5, 1.6, 1.7, 1.11, 1.15, 1.16) — fills the legacy A-monolith retirement path.
6. **Topic 5 AHL block** (5.12 – 5.18) — densest HL content; integration techniques + Maclaurin series.
7. **Topic 2 AHL block** (2.12 – 2.16) — polynomial/rational HL extensions.
8. **Topic 4 Practice + Solutions** — fills the per-sub-topic Practice gap for the already-shipped Topic 4.

### Sprint 2 follow-up — Unit_C monolith polish (kept open)

These rows apply to the existing `Unit_C_Geometry.html` monolith
which remains in production until C-split sub-topic units 3.1–3.8
all ship. The polish work below makes Unit_C consistent with A1/A3/A4
during the transition window. Each row will be marked closed-by-split
once the corresponding sub-topic units replace the monolith section.

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

**Glossary check** — IB Math AA HL Wave 1 terminology applied as-is
(sequence / series / common difference / common ratio / sum to infinity
/ partial sum / closed-form / GDC / exact form). Combinatorics-specific
terms added inline via `<code>` glosses (binomial expansion / general
term / binomial coefficient / binomial theorem / multiset / gap method
/ block method / circular permutation / lattice paths / monotone paths
/ multiplication principle / inclusion-exclusion / extended binomial
theorem / radius of convergence / conditional probability / symmetry
argument / triangular numbers).

**Commits on `wave2_ib_math_hl`:**

- `89b8a12` — W2-1 A1 Practice ZH translation (67/67, +81/−66)
- `bd62129` — W2-2 A3 Practice ZH translation (76/76, +90/−75)
- `2dce66c` — W2-3 A3 Solutions ZH translation (51/51, +353/−51)

**Note — out of Wave 2 scope (build, not translate).** Practice +
Solutions files for A2 / A4 / A5 / A6 / B / D / E (SQ-4 above) do not
exist yet; they ship bilingual end-to-end under the locked English-first
→ ZH cadence as each one lands.

### Closed (Translation Sprint — closed 2026-05-21)

All currently-shipped IB Math HL study guides (A1, A3, A4, C)
bilingualized EN↔ZH. Branch `ib_math_hl_translation` fast-forwarded
to `main`.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**T-1**~~ | Unit A1 Sequences &amp; Series bilingual translation | P1 | ✅ closed — `cdca220` |
| ~~**T-2**~~ | Unit A3 Combinatorics bilingual translation | P1 | ✅ closed — `ea3124d` |
| ~~**T-3**~~ | Unit A4 Complex Numbers bilingual translation | P1 | ✅ closed — `12dc6ad` (+ Argand-gloss polish in follow-up) |
| ~~**T-4**~~ | Unit C Geometry bilingual translation | P1 | ✅ closed — `ebf8d11` |

**Audience contract** — Mandarin-Chinese-language students preparing to
write the IB Math AA HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terminology (sequence / series /
binomial theorem / De Moivre / Argand / modulus / argument / etc.) stays
in `<code>` inline. Math notation untouched. A2 / A5 / A6 will be
translated as they ship (covered by the SQ-4 "as they ship" rule; the
Practice Questions / Solutions surface for A1 + A3 is tracked in the
**Translation Sprint Wave 2** entry above, opened 2026-05-22).

**Backlog candidates beyond this sprint:** Sprint 1 (Unit A refactor —
A2, A5, A6 study guides) and Sprint 2 (Units B / **D shipped 2026-05-22** / E).

### Sprint 1 — Refactor Unit A into focused sub-units (paused for translation)

**Sprint 1 — Refactor Unit A into focused sub-units.** The original
`Unit_A_Number_and_Algebra.html` is a 2588-line monolith covering 24
sub-topics. Per 2026-05-08 decision, it's being split into 6 focused
sub-units (A1 → A6). Each sub-unit conforms to the dual-goal contract
(cram cheat-sheet on top, going-deeper proofs at the bottom). Once the
six sub-units are shipped, the monolith gets removed and `index.html`
updates to list them.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S1-1**~~ | Draft `Unit_A1_Sequences_and_Series.html` (Topic 1.2–1.4, 1.8) | P0 | ✅ **Shipped 2026-05-08** — 8 sections (AP, GP, sigma, infinite-GP convergence, financial apps, mixed patterns), 18 quiz items, 12 flashcards, 14-item readiness checklist. Introduces the `cram-cheat` CSS pattern + `hl-flag` chip. |
| **S1-2** | Draft `Unit_A2_Exponents_and_Logarithms.html` (Topic 1.5, 1.7) | P0 | **Open** — covers laws of exponents, logarithms, exponential equations, change-of-base. |
| ~~**S1-3**~~ | Draft `Unit_A3_Combinatorics.html` (Topic 1.9–1.10) | P0 | ✅ **Shipped 2026-05-09** — 6 sections (counting principles, permutations, combinations, binomial theorem, Pascal's triangle &amp; identities, extended binomial HL). 6 inline quizzes + 10-item practice quiz, 12 flashcards, 14-item readiness checklist. Introduces `pascal-tri` ASCII-table CSS pattern. Renamed from "Counting & Binomial" to user's preferred "Combinatorics." |
| ~~**S1-4**~~ | Draft `Unit_A4_Complex_Numbers.html` (Topic 1.12–1.14) | P0 | ✅ **Shipped 2026-05-15** — 6 sections (Cartesian form, Argand &amp; polar form, Euler form &amp; multiplication, De Moivre, roots &amp; roots of unity, polynomials over ℂ). 6 inline quizzes + 10-item practice quiz, 14 flashcards, 14-item readiness checklist. Includes inductive proof of De Moivre, derivation of multiple-angle identities, and proof of the conjugate root theorem. Introduces `argand-figure` SVG component (Argand-diagram inline graphics for $z = a + bi$, multiplication-as-rotation, and the 5th roots of unity). |
| **S1-5** | Draft `Unit_A5_Proof.html` (Topic 1.6, 1.15) | P0 | **Open** — direct proof, induction, contradiction. Cross-link from A1 induction-of-sums. |
| **S1-6** | Draft `Unit_A6_Algebra_and_Systems.html` (Topic 1.11 + linear systems) | P0 | **Open** — partial fractions, $3\times 3$ systems, RREF. |
| **S1-7** | Remove old `Unit_A_Number_and_Algebra.html` + update `index.html` cards | P1 | 🟡 **Partial 2026-05-15** — file moved to `rag/archive/Unit_A_Number_and_Algebra.html` (stripped from deploy by `deploy.yml`); Unit A card dropped from `index.html`. Full deletion of the archived copy pending A2/A5/A6 ship (content needs to land in sub-units before the reference copy can be discarded). |

Build order: **A1 (✓) → A3 (✓) → A4 (✓) → A2 → A5 → A6 → cleanup**. (A3
jumped ahead of A2 on user request 2026-05-09; A4 jumped ahead of A2 on
user request 2026-05-14.)

### Practice Questions sub-stream

Parallel build-out of IB-style practice files in `Practice Questions/`,
mirroring the AP Physics pattern but adapted for IB paper structure
(Paper 1A short / Paper 1B extended / Paper 2 calc / Paper 3 HL). Each
question carries difficulty (Easy/Medium/Hard), paper, syllabus topic,
and mark allocation pills. Question-only — no embedded answers.

| ID | Item | Status |
|---|---|---|
| ~~**SQ-1**~~ | `Practice Questions/README.md` + locked conventions | ✅ Shipped 2026-05-09 |
| ~~**SQ-2**~~ | `Unit_A1_Sequences_and_Series_Practice.html` (11 Qs, 67 marks total) | ✅ Shipped 2026-05-09 |
| ~~**SQ-3**~~ | `Unit_A3_Combinatorics_Practice.html` (11 Qs, 61 marks total) | ✅ Shipped 2026-05-09 |
| **SQ-4** | Practice files for A2 / A4 / A5 / A6 / B / D / E (one per study guide as those land) | **Open** — track per study-guide ship |

### Sprint 2 — New topic units (Topic D shipped 2026-05-22)

Sprint 2 picks up the missing topic units (B Functions, D Statistics &amp;
Probability, E Calculus). Original build order was **B → D → E**;
**D jumped ahead of B on user request 2026-05-22** because of an
upcoming client need.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-D1** | Draft `Unit_D1_Univariate_Data.html` covering IB AA HL sub-topics SL 4.1, 4.2, 4.3, 4.4 (univariate descriptive + bivariate correlation/regression, folded together to keep Topic D in 3 files) | P0 | ✅ **Shipped 2026-05-22** — 2092 lines, 7 sections each tagged with its official IB sub-topic via `.ib-ref` chip in h2; cram cheat-sheet + per-section quizzes + 10-MCQ final quiz + 14 flashcards (locked terse style) + 14-item readiness checklist. All SL content; no `hl-flag` chips. PMCC + regression line with through-mean-point property explicit. IB convention on SD (divide by `n`) stated. Commit `f8db91f`. |
| **S2-D2** | Draft `Unit_D2_Probability.html` covering SL 4.5, 4.6, AHL 4.10 (probability concepts, combined events, Bayes' theorem) | P0 | ✅ **Shipped 2026-05-22** — 1810 lines, 7 sections. Section 2.7 Bayes is HL-only (carries `hl-flag` chip); cram cheat-sheet visually splits SL core from AHL Bayes; SVG Venn diagram, sample-space table, styled tree diagram included; Bayes statement with max-3-event cap stated. Commit `4a74130`. |
| **S2-D3** | Draft `Unit_D3_Probability_Distributions.html` covering SL 4.7, 4.8, 4.9, AHL 4.11, 4.12, 4.13 (discrete RVs, binomial, normal, continuous RVs, linear transformations, sums of independent normals) | P0 | ✅ **Shipped 2026-05-22** — 1992 lines, 8 sections (densest of the 3). Sections 3.3, 3.7, 3.8 are HL-only (`hl-flag` chips). Cram cheat-sheet visually splits SL · CORE (green) from HL · AHL ONLY (purple). Two required going-deeper derivations: Var(X) = E(X²) − μ² and Var(aX+b) = a²Var(X). Inline SVG bell curve with ±1/2/3σ bands. N(μ, σ²) variance convention stated. Commit `8bb208a`. |
| **S2-D-index** | Add D1/D2/D3 cards to `index.html` IB Math AA HL section (manual edit — `build-index.py` is currently bilingual-unaware and would have regressed `<span data-lang>` markup) | P1 | ✅ **Shipped 2026-05-22** — count chip updated to "7 units" / "7 个单元". Commit `c03cc67`. |
| **S2-B** | Draft `Unit_B_Functions.html` (Topic 2 SL + AHL) | P0 | **Open** — covers function families, transformations, inverses, exponential/log, rational, polynomial division, partial fractions. |
| **S2-E** | Draft `Unit_E_Calculus.html` (Topic 5 SL + AHL) | P0 | **Open** — covers limits, differentiation rules, applications, integration techniques, ODEs, MacLaurin series, related rates. Likely splits into E1/E2/E3 per the same pattern as Topic D. |
| ~~**S2-D-translate**~~ | Bilingual ZH translation of `Unit_D1`, `Unit_D2`, `Unit_D3` per the locked English-first → ZH cadence | P1 | ✅ **Shipped 2026-05-22** — D1 391/391 pairs (`148fa51`), D2 281/281 pairs (`231f6e8`), D3 312/312 pairs (`0f84a70`). All validate clean. Pre-translation review pass surfaced 2 P1 fixes addressed first (`21a0d7d`): D2 Bayes quiz had two mathematically-identical answer options ($\dfrac{7}{10}$ vs $0.7$); D1 regression formula used non-IB form `y = ax + b` instead of IB's `y = a + bx`. |
| **S2-D-practice** | Practice Questions for D1 / D2 / D3 (paper-style, IB Paper 1A / 1B / 2 / 3HL split) per SQ-4 above | P1 | **Open** — follow the pattern used for A1 / A3 Practice. |
| **S2-build-index** | Extend `scripts/build-index.py` to preserve `<span data-lang="zh">` alongside auto-generated English title in card markup | P1 | **Open** — punted 2026-05-22 when shipping D-units. Manual-edit was used as workaround for that ship. |

---

## Translation audit (per-file, post-ship)

**Audit target.** All currently-shipped IB Math AA HL study guides
bilingualized to support a Mandarin-Chinese-language student writing the
IB exam in English. Chinese is a *teaching translation* — explains the
concept; English exam-rubric terms remain in `<code>` inline so the
student recognizes them on the exam paper. Playbook:
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).

**Audit method.** (1) Structural — count `data-lang="en"` vs
`data-lang="zh"` attributes; they must be equal. (2) Lexical — verify
core IB Math AA HL terminology is consistently rendered across files
(glossary in `prompts/create-bilingual-translation.md`). (3)
Pedagogical — spot-read sample concept-boxes / worked-examples in each
file; check the Chinese explains rather than literally translates.
(4) Validation — `scripts/validate.sh` passes on each file.

### Per-file scorecard

Mark ✅ when balanced and `validate.sh` passes; ✗ if either fails;
⏳ until the unit's translation commit lands. Fill in EN/ZH counts via
`grep -c 'data-lang="en"' "IB Math HL/Study Guides/Unit_*.html"` and
the matching `"zh"` count.

| # | Unit | EN/ZH balance | Glossary fit | Pedagogical | Validates | Notes |
|---|---|---|---|---|---|---|
| A1 | Sequences & Series       | 260 / 260 ✅ | ✅ | ✅ | ✅ | T-1 shipped `cdca220`. Supersedes playbook's stale `af27baf` reference. |
| A3 | Combinatorics            | 213 / 213 ✅ | ✅ | ✅ | ✅ | T-2 shipped `ea3124d`. Glossary covers <code>permutation</code>, <code>combination</code>, <code>binomial theorem</code>, <code>Pascal's triangle</code>, <code>Pascal's identity</code>, <code>circular arrangement</code>, <code>combinatorial proof</code>. |
| A4 | Complex Numbers          | 241 / 241 ✅ | ✅ | ✅ | ✅ | T-3 shipped `12dc6ad`. Glossary covers <code>Cartesian form</code>, <code>polar form</code>, <code>Euler form</code>, <code>Euler's formula</code>, <code>De Moivre's theorem</code>, <code>roots of unity</code>, <code>primitive root</code>, <code>conjugate root theorem</code>, <code>fundamental theorem of algebra</code>. Argand-gloss polish landed as follow-up. |
| C  | Geometry & Trigonometry  | 356 / 356 ✅ | ✅ | ✅ | ✅ | T-4 shipped `ebf8d11`. Largest file (2381 → 2909 lines). Glossary covers <code>sine rule</code>, <code>cosine rule</code>, <code>radian</code>, <code>arc length</code>, <code>sector area</code>, <code>dot product</code> (→ 数量积（点积）), <code>vector product</code> / <code>cross product</code> (→ 向量积（叉积）), <code>skew lines</code> (→ 异面), <code>magnitude</code>, <code>normal vector</code>, <code>vector equation of a line</code>, <code>vector equation of a plane</code>, plus <code>bearing</code> / <code>angle of elevation/depression</code>. |

A2, A5, A6 not in this sprint — they have not yet shipped (open in
Sprint 1 above). Translate as they ship.

### Findings — corpus-wide (closed 2026-05-21)

- **All 4 files have perfectly balanced `data-lang="en"` / `data-lang="zh"`
  attribute counts** (A1: 260/260, A3: 213/213, A4: 241/241, C: 356/356).
- **Bilingual infrastructure identical across all 4 files** — CSS toggle
  (`body:not(.lang-zh)…` + mirror), `toggleLang()` JS with
  `localStorage.drs.lang` persistence, nav button between Contents and
  Dark, `PingFang SC → Hiragino Sans GB → Microsoft YaHei` CJK fallback
  in `--font-body`.
- **Exam-term gloss pattern applied uniformly.** Every IB Math AA HL
  rubric term appears once in `<code>` on its first mention per Chinese
  passage; subsequent mentions left as plain Chinese.
- **Math notation untouched.** All LaTeX renders identically in both
  languages — Chinese flip changes only the prose.
- **Glossary consistency.** Core terms (sequence / series / arithmetic /
  geometric / binomial theorem / Pascal's triangle / permutation /
  combination / complex number / Argand diagram / De Moivre / modulus /
  argument / sine rule / cosine rule / dot product / cross product /
  skew lines) render identically across files.
- **`scripts/validate.sh` passes on all 4.**

Translation work is **publish-ready**. No P0 / P1 translation issues
remain.

### Findings — requiring follow-up

None. Sprint cleared with a small polish commit fixing three
`Argand plane` vs `Argand diagram` gloss mismatches in A4 (commit
follow-up to `12dc6ad`). Optional P2 refinements below.

### Optional refinements (P2 — not blocking)

| ID | Item | Why P2 |
|---|---|---|
| TR-1 | Add `lang="en"` / `lang="zh"` attribute (HTML standard) on toggled spans/divs to enhance screen-reader behavior | A11y polish; current behavior works fine for sighted users which is the dominant use case |
| TR-2 | Print stylesheet: decide whether `@media print` should default to EN or to the currently-toggled language | Edge case; consult once a Chinese-language student requests printable practice |
| TR-3 | Translation of `<title>` tags so browser tab reads in Chinese when in zh mode (currently `<title>` is EN-only) | Minor browser-chrome polish |

### Translation contract — standing principle (mirrors AP Calc / AP Physics close-out 2026-05-18 / 2026-05-19)

Chinese is a teaching translation, not literal. English exam-rubric
terminology stays in `<code>` inline. Math notation untouched. See
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).
This standing principle is co-equal with the Dual-Goal Philosophy
below — every future unit must conform to both.

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

Where a topic has a clear calc/no-calc split (most prominently in Unit D
Statistics), label it in the section or worked-example header. Paper 1 is
no-calc; Paper 2 is calc.

---

## Cross-Unit Snapshot

| Unit | Topic | Sections | Worked Ex. | Flashcards | Quiz | Status |
|---|---|---|---|---|---|---|
| A (legacy) | Number & Algebra (monolith) | 24 | ~24 | 14 | 9 | **To remove** once A1–A6 ship |
| A1 | Sequences & Series | 8 + how-to + strategy | 12 | 12 | 18 (8 inline + 10 unit) | ✓ Shipped 2026-05-08 |
| A2 | Exponents & Logs | — | — | — | — | **S1-2 open** |
| A3 | Combinatorics | 6 + how-to + strategy | 11 | 12 | 16 (6 inline + 10 unit) | ✓ Shipped 2026-05-09 |
| A4 | Complex Numbers | — | — | — | — | **S1-4 open** |
| A5 | Proof | — | — | — | — | **S1-5 open** |
| A6 | Algebra & Systems | — | — | — | — | **S1-6 open** |
| B | Functions | — | — | — | — | Sprint 2 |
| C | Geometry & Trigonometry | TBA | TBA | TBA | TBA | ✓ Shipped (legacy form) |
| D | Statistics & Probability | — | — | — | — | Sprint 2 |
| E | Calculus | — | — | — | — | Sprint 2 |

*The legacy `Unit_A_Number_and_Algebra.html` stays on disk until S1-6
ships, so the live site still has full Topic 1 coverage during the
refactor. Same plan eventually applies to Unit C if monolith size
becomes a problem.*

---

## Topic Scope Reminders (IB AA HL syllabus)

These are not commitments — just the surface area each unit must cover.
Verify against the official IB syllabus before drafting.

### Unit B — Functions
- 2.1 Equations of straight lines, parallel/perpendicular conditions
- 2.2 Concept of a function, domain/range, inverse
- 2.3 Graphing — key features, intercepts, asymptotes
- 2.4 Quadratic functions — discriminant, vertex form, factored form
- 2.5 Rational, exponential, logarithmic functions
- 2.6 Polynomial functions, factor & remainder theorems
- 2.7 Solving equations graphically and analytically
- 2.8 (HL) Sums, differences, products, quotients, composites
- 2.9 (HL) Odd/even functions, self-inverse, modulus, reciprocal
- 2.10 (HL) Rational functions, oblique asymptotes
- 2.11 (HL) Transformations of graphs
- 2.12 (HL) Polynomial division, factor/remainder, partial fractions
  (note: partial fractions overlaps with Unit A — coordinate carefully)

### Unit D — Statistics & Probability
- 4.1 Sampling, populations, bias
- 4.2 Frequency distributions, histograms, cumulative frequency
- 4.3 Measures of central tendency and dispersion
- 4.4 Linear correlation, regression
- 4.5 Probability — events, mutually exclusive, independent
- 4.6 Conditional probability, Bayes' theorem (HL)
- 4.7 Discrete random variables, expectation
- 4.8 Binomial distribution
- 4.9 Normal distribution
- 4.10 (HL) Linear transformations, $E(X)$ and $Var(X)$
- 4.11 (HL) PDFs, expectation/median/mode for continuous variables
- 4.12 (HL) Sample mean distribution, central limit theorem (informal)

### Unit E — Calculus
- 5.1 Limits, derivative as a limit
- 5.2 Differentiation — power rule, sum/difference
- 5.3 Tangents, normals
- 5.4 Stationary points, second derivative test
- 5.5 Indefinite integration, definite integrals, area
- 5.6 Kinematics — displacement/velocity/acceleration
- 5.7 (HL) Chain, product, quotient rules
- 5.8 (HL) Continuity, differentiability, limits, L'Hôpital
- 5.9 (HL) Implicit differentiation, related rates, optimization
- 5.10 (HL) Integration by substitution, by parts
- 5.11 (HL) Volumes of revolution
- 5.12 (HL) Differential equations, Euler's method, separable, integrating
  factor
- 5.13 (HL) Maclaurin series

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
