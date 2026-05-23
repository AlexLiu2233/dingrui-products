# Subject Spec — IB Math AA HL

## Identity

- **Display (section heading):** IB Math AA HL
- **Display (hero chip):** IB Math AA HL
- **Directory:** `IB Math HL/`
- **Audit:** `IB Math HL/AUDIT.md` (Sprint 3 = "Complete the units" — one
  unit per 2029 super-topic, 22 total)
- **IB-authoritative source:** `rag/sources/IB Math HL/sb_maths_analysis_en.pdf`
  (Subject Brief, first assessment 2029)

## Official curriculum reference — 2029 syllabus (locked 2026-05-22)

**IB Mathematics: Analysis and Approaches, first assessment 2029.** This
spec is now organized around the 2029 super-topic structure (5 Topics,
22 super-topics, AHL flagged). The 2021 syllabus structure is retained
as a *mapping table* below so the currently-shipped units (A1, A3, A4,
D1, D2, D3) — which were drafted against 2021 sub-topic numbering —
can be traced cleanly to their 2029 home.

The "AA" track is distinct from "AI" (Applications and Interpretation) —
see `ib_math_ai_hl.md`. AA is the more rigorous / analytical track:
proof, complex numbers, abstract function theory, integration
techniques, and Maclaurin series. AI is the modelling-oriented track:
piecewise functions, graph theory, statistical tests, Markov chains.
AA students sit Paper 1 **without a calculator**; AI students have
calculators on every paper.

## Naming convention

Units are named after their 2029 super-topic ID — the consumer-facing
student can match any 2029 super-topic reference in the IB guide
directly to one of our units. The 2029 IDs (A1, A3, A4, B1, …, E6)
also happen to match the filename prefix we have been using since
2026-05-08, so existing shipped units need no rename.

```
IB Math HL/Study Guides/Unit_<SuperID>_<Slug>.html
IB Math HL/Practice Questions/Unit_<SuperID>_<Slug>_Practice.html
IB Math HL/Practice Questions/Solutions/Unit_<SuperID>_<Slug>_Solutions.html
```

`<SuperID>` is one of the 22 2029 super-topic identifiers (`A1` … `E6`).
Example: 2029 super-topic D2 "Probability" → `Unit_D2_Probability.html`.

## Required `<title>` format

```
IB Math AA HL — Unit {SuperID}: {Super-topic Title} | Dingrui Scholars
```

Example: `IB Math AA HL — Unit D1: Univariate Data | Dingrui Scholars`.

## Exam structure — 2029 first assessment

- **Paper 1 (no technology):** SL 1h30 (40%), HL 2h (30%). Section A
  compulsory short-response, Section B compulsory extended-response.
- **Paper 2 (technology required):** SL 1h30 (40%), HL 2h (30%). Same
  Section A / B structure.
- **Paper 3 (HL only, technology required):** 1h (20%). Two compulsory
  extended-response questions.
- **Internal Assessment:** Mathematical exploration, 30 hours (20%).

Total external assessment: SL 3h / HL 5h (80% of final grade).

> **Practice-question chrome implication.** Paper 1A (short response,
> no calc) and Paper 1B (extended response, no calc) pills remain
> AA-distinctive — Paper 1 is no-tech, unlike AI where every paper is
> calculator-allowed. Practice files should continue using the
> Paper 1A / 1B / 2 / 3 EMH split.

## Standing principle — dual-goal contract

Every guide serves two students at once: the **crammer** (last-ditch
pass the night before) and the **7-chaser** (going deep for top score).
Canonical articulation in `prompts/create-unit.md`. Each section layers:
cheat-sheet at top → worked example(s) → "going deeper" proof /
derivation. Quiz items mix recall and synthesis.

Flashcards (when present) follow the locked terse style from A1/A3:
question on front, `$$formula$$` on back, no prose.

## HL flagging

HL-only super-topics (A4 Complex numbers, C3 Vectors, E5 Differential
equations, E6 Maclaurin series) carry the `hl-flag` chip at unit level.
Within a mixed-SL/HL super-topic (e.g. A5 Proof and algebraic
manipulation contains SL simple deductive proof + HL induction /
contradiction), individual sections carry `hl-flag` chips per the
pattern already used in A1 / A3 / A4 / D2 §2.7 / D3 §§3.3 / 3.7 / 3.8.

A reader should see at a glance which content is HL-extension material.

---

## Unit list — 2029 super-topic enumeration (22 units total)

Hours figures are IB-recommended teaching hours per Topic (SL / HL),
not per super-topic. They give a rough sense of weighting.

Status legend:
- ✅ **shipped** — Study Guide live on `main`. Practice / Solutions / ZH
  status tracked separately in `IB Math HL/AUDIT.md`.
- 🟡 **partial** — content covered inside a legacy combined unit;
  standalone super-topic unit not yet drafted.
- ⬜ **unbuilt** — no coverage in the repo yet.

### Topic A — Number and Algebra (SL 19h, HL 42h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Currently shipped as |
|---|---|---|---|---|
| **A1** | Sequences | SL + AHL | ✅ | `Unit_A1_Sequences_and_Series.html` |
| **A2** | Exponents and logarithms | SL + AHL | ⬜ | (target: `Unit_A2_Exponents_and_Logarithms.html`) |
| **A3** | Combinatorics | SL + AHL | ✅ | `Unit_A3_Combinatorics.html` |
| **A4** | Complex numbers (HL only) | AHL | ✅ | `Unit_A4_Complex_Numbers.html` |
| **A5** | Proof and algebraic manipulation | SL + AHL | ⬜ | (target: `Unit_A5_Proof_and_Algebraic_Manipulation.html`) |

### Topic B — Functions (SL 33h, HL 46h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Currently shipped as |
|---|---|---|---|---|
| **B1** | Representation of functions | SL + AHL | ⬜ | greenfield |
| **B2** | Polynomial functions | SL + AHL | ⬜ | greenfield |
| **B3** | Functions with asymptotes | SL + AHL | ⬜ | greenfield (= rational functions) |
| **B4** | Trigonometric functions | SL + AHL | 🟡 | partly inside `Unit_C_Geometry.html` §§C2.4–C2.10 (unit-circle, identities, circular functions, solving trig equations) |
| **B5** | Transformations of graphs and functions | SL + AHL | ⬜ | greenfield |

### Topic C — Geometry (SL 16h, HL 35h) — 3 super-topics

| ID | Super-topic | SL/AHL | Status | Currently shipped as |
|---|---|---|---|---|
| **C1** | Surface areas, volumes and measurement in circles | SL | 🟡 | partly inside `Unit_C_Geometry.html` §§C1.1–C1.3 (3D distance, volumes, surface areas, radian / arc / sector) |
| **C2** | Trigonometry and its applications | SL | 🟡 | partly inside `Unit_C_Geometry.html` §§C2.1–C2.3 (right-angled, sine / cosine rules, bearings) |
| **C3** | Vectors (HL only) | AHL | ⬜ | greenfield |

### Topic D — Probability and Statistics (SL 22h, HL 28h) — 3 super-topics

| ID | Super-topic | SL/AHL | Status | Currently shipped as |
|---|---|---|---|---|
| **D1** | Univariate data | SL | ✅ | `Unit_D1_Univariate_Data.html` (covers univariate + bivariate — 2029 AA D1 includes both since AA has no separate "bivariate" super-topic) |
| **D2** | Probability | SL + AHL | ✅ | `Unit_D2_Probability.html` |
| **D3** | Probability distributions | SL + AHL | ✅ | `Unit_D3_Probability_Distributions.html` |

### Topic E — Calculus (SL 30h, HL 59h) — 6 super-topics

| ID | Super-topic | SL/AHL | Status | Currently shipped as |
|---|---|---|---|---|
| **E1** | Principles of differential calculus | SL + AHL | ⬜ | greenfield |
| **E2** | Techniques of differential calculus | SL + AHL | ⬜ | greenfield |
| **E3** | Techniques of integral calculus | SL + AHL | ⬜ | greenfield |
| **E4** | Problem-solving using calculus | SL + AHL | ⬜ | greenfield (tangents/normals, optimisation, kinematics, volumes, related rates) |
| **E5** | Differential equations (HL only) | AHL | ⬜ | greenfield |
| **E6** | Maclaurin series (HL only) | AHL | ⬜ | greenfield |

---

## 2021 → 2029 mapping (for currently-shipped legacy units)

This table preserves the 2021 sub-topic numbering for cross-reference,
since shipped units were drafted against it. Mappings to 2029
super-topics are inferred from super-topic titles in the 2029 Subject
Brief — when the full IB AA HL 2029 guide is published with sub-bullets,
verify and correct any drift.

### Topic 1 — Number and Algebra (2021) → 2029 Topic A

| 2021 ID | 2021 Title | Maps to 2029 super-topic |
|---|---|---|
| 1.1 | Scientific notation $a \times 10^k$ | A2 Exponents and logarithms (best fit; 2029 AA has no separate "approximation" super-topic) |
| 1.2 | Arithmetic sequences and series | **A1 Sequences** |
| 1.3 | Geometric sequences and series | **A1 Sequences** |
| 1.4 | Financial applications of GP | **A1 Sequences** |
| 1.5 | Exponents (integer) + intro to logs | **A2 Exponents and logarithms** |
| 1.6 | Simple deductive proof | **A5 Proof and algebraic manipulation** |
| 1.7 | Logarithm laws / change of base | **A2 Exponents and logarithms** |
| 1.8 | Sum of infinite convergent GP | **A1 Sequences** |
| 1.9 | Binomial theorem (positive integer $n$) | **A3 Combinatorics** |
| 1.10 | Perms, combs, extended binomial (HL) | **A3 Combinatorics** |
| 1.11 | Partial fractions (HL) | **A5 Proof and algebraic manipulation** (algebraic manipulation strand) |
| 1.12 | Complex numbers Cartesian (HL) | **A4 Complex numbers (HL only)** |
| 1.13 | Polar / Euler forms (HL) | **A4 Complex numbers (HL only)** |
| 1.14 | De Moivre, roots of complex numbers (HL) | **A4 Complex numbers (HL only)** |
| 1.15 | Proof by induction / contradiction (HL) | **A5 Proof and algebraic manipulation** |
| 1.16 | Systems of linear equations (HL) | **A5 Proof and algebraic manipulation** (algebraic manipulation strand) |

### Topic 2 — Functions (2021) → 2029 Topic B

| 2021 ID | 2021 Title | Maps to 2029 super-topic |
|---|---|---|
| 2.1 | Straight lines (gradients, parallel, perpendicular) | **B1 Representation of functions** (AA frames lines as linear functions) |
| 2.2 | Function concepts (domain, range, inverse) | **B1 Representation of functions** |
| 2.3 | Graphs of functions | **B1 Representation of functions** |
| 2.4 | Key features and intersections | **B1 Representation of functions** |
| 2.5 | Composite functions and inverses | **B1 Representation of functions** |
| 2.6 | Quadratic functions | **B2 Polynomial functions** |
| 2.7 | Quadratic equations and inequalities | **B2 Polynomial functions** |
| 2.8 | Rational functions (linear / linear) | **B3 Functions with asymptotes** |
| 2.9 | Exponential and logarithmic functions | **B1 Representation of functions** (graphs); algebra inside **A2** |
| 2.10 | Solving equations | **B1 Representation of functions** |
| 2.11 | Transformations of graphs | **B5 Transformations of graphs and functions** |
| 2.12 | Polynomial functions HL (factor / remainder) | **B2 Polynomial functions** |
| 2.13 | Rational functions HL | **B3 Functions with asymptotes** |
| 2.14 | Odd / even / self-inverse | **B1 Representation of functions** |
| 2.15 | Function inequalities HL | **B1 Representation of functions** (or A5 — verify against 2029 guide) |
| 2.16 | Graph transformations HL ($\|f(x)\|$, $1/f(x)$, etc.) | **B5 Transformations of graphs and functions** |

### Topic 3 — Geometry and Trigonometry (2021) → 2029 Topics B + C

| 2021 ID | 2021 Title | Maps to 2029 super-topic |
|---|---|---|
| 3.1 | 3D distance, volumes, surface areas | **C1 Surface areas, volumes and measurement in circles** |
| 3.2 | Angles between lines / planes | **C1** |
| 3.3 | Right-angled & non-right trig; sine / cosine rules | **C2 Trigonometry and its applications** |
| 3.4 | Radian / arc / sector | **C1** (measurement in circles) |
| 3.5 | Unit circle, exact values | **B4 Trigonometric functions** |
| 3.6 | Pythagorean & double-angle identities | **B4 Trigonometric functions** |
| 3.7 | Circular functions (amplitude, period, transformations) | **B4 Trigonometric functions** |
| 3.8 | Solving trig equations | **B4 Trigonometric functions** |
| 3.9 | Reciprocal & inverse trig (HL) | **B4 Trigonometric functions** |
| 3.10 | Compound angle identities (HL) | **B4 Trigonometric functions** |
| 3.11 | Trig symmetries (HL) | **B4 Trigonometric functions** |
| 3.12 – 3.18 | Vectors (HL: intro, dot product, lines, intersections, cross product, planes) | **C3 Vectors (HL only)** |

> **Unit_C straddle.** Our legacy `Unit_C_Geometry.html` crosses three
> 2029 super-topics (B4 + C1 + C2). When the standalone B4 / C1 / C2
> units ship, Unit_C is archived (same retirement pattern as the legacy
> Unit_A monolith — moved to `rag/archive/`, stripped from deploy via
> `deploy.yml`).

### Topic 4 — Statistics and Probability (2021) → 2029 Topic D

| 2021 ID | 2021 Title | Maps to 2029 super-topic |
|---|---|---|
| 4.1 | Sampling concepts | **D1 Univariate data** |
| 4.2 | Data presentation | **D1 Univariate data** |
| 4.3 | Central tendency and dispersion | **D1 Univariate data** |
| 4.4 | Bivariate linear (PMCC, regression) | **D1 Univariate data** (2029 AA D1 includes bivariate — AA has no separate D2-bivariate super-topic, unlike AI) |
| 4.5 | Probability basics | **D2 Probability** |
| 4.6 | Combined events, conditional, independent | **D2 Probability** |
| 4.7 | Discrete RVs, $E(X)$ | **D3 Probability distributions** |
| 4.8 | Binomial distribution | **D3 Probability distributions** |
| 4.9 | Normal distribution | **D3 Probability distributions** |
| 4.10 | Bayes' theorem (HL) | **D2 Probability** |
| 4.11 | Variance, continuous RVs, linear transformations (HL) | **D3 Probability distributions** |

> **D-cluster shipped 2026-05-22.** Topic D is the only fully-shipped
> Topic in AA HL right now — all 11 sub-topics live across three
> super-topic units (D1, D2, D3) with ZH translation complete. The
> outstanding deliverable is Practice + Solutions at super-topic
> granularity (D1, D2, D3 each).

### Topic 5 — Calculus (2021) → 2029 Topic E

| 2021 ID | 2021 Title | Maps to 2029 super-topic |
|---|---|---|
| 5.1 | Introduction to differentiation | **E1 Principles of differential calculus** |
| 5.2 | Increasing and decreasing functions | **E1 Principles of differential calculus** |
| 5.3 | Power rule and linearity | **E2 Techniques of differential calculus** |
| 5.4 | Tangents and normals | **E4 Problem-solving using calculus** |
| 5.5 | Anti-differentiation | **E3 Techniques of integral calculus** |
| 5.6 | Definite integrals | **E3 Techniques of integral calculus** |
| 5.7 | Derivative rules (chain, product, quotient, trig / exp / log) | **E2 Techniques of differential calculus** |
| 5.8 | Maxima and minima | **E4 Problem-solving using calculus** |
| 5.9 | Kinematics (differentiation) | **E4 Problem-solving using calculus** |
| 5.10 | Indefinite integrals (reverse chain) | **E3 Techniques of integral calculus** |
| 5.11 | Volumes of revolution about $x$-axis | **E4 Problem-solving using calculus** |
| 5.12 | Continuity and differentiability (HL) | **E1 Principles of differential calculus** |
| 5.13 | Related rates and implicit differentiation (HL) | **E4 Problem-solving using calculus** |
| 5.14 | Concavity and inflection (HL) | **E1 Principles of differential calculus** |
| 5.15 | Advanced integration (substitution, parts) (HL) | **E3 Techniques of integral calculus** |
| 5.16 | $y$-axis integration and volumes (HL) | **E4 Problem-solving using calculus** |
| 5.17 | Differential equations (HL) | **E5 Differential equations (HL only)** |
| 5.18 | Maclaurin series (HL) | **E6 Maclaurin series (HL only)** |

---

## Coverage roll-up (as of 2026-05-22)

| 2029 Topic | Super-topics | ✅ shipped | 🟡 partial (in legacy unit) | ⬜ unbuilt |
|---|---|---|---|---|
| **A** Number and Algebra | 5 (A1–A5) | 3 (A1, A3, A4) | 0 | 2 (A2, A5) |
| **B** Functions | 5 (B1–B5) | 0 | 1 (B4 partial in Unit_C) | 4 (B1, B2, B3, B5) |
| **C** Geometry | 3 (C1–C3) | 0 | 2 (C1, C2 partial in Unit_C) | 1 (C3) |
| **D** Statistics and Probability | 3 (D1–D3) | **3 (D1, D2, D3)** | 0 | 0 |
| **E** Calculus | 6 (E1–E6) | 0 | 0 | 6 (E1–E6) |
| **Total** | **22** | **6** | **3** | **13** |

So: **6 of 22 super-topics are fully shipped as standalone units**, 3
more have meaningful content trapped inside `Unit_C_Geometry.html`, and
13 are entirely greenfield.

## Sprint 3 deliverable contract per super-topic

For each of the 22 super-topics, four products ship in order:

1. **Study Guide** HTML — dual-goal contract; cram cheat-sheet,
   sections (one per major sub-bullet of the super-topic), worked
   examples, per-section quizzes, final unit quiz, flashcards (locked
   terse style), 14-item readiness checklist. Reference template:
   `Unit_A3_Combinatorics.html`.
2. **Practice Questions** HTML — IB paper-style. EMH mix (Easy /
   Medium / Hard) distributed across Paper 1A (short response, no
   calc), Paper 1B (extended response, no calc), Paper 2 (calculator),
   Paper 3 (HL extended exploration — only for HL-relevant content).
   Reference template: `Unit_A1_Sequences_and_Series_Practice.html`.
3. **Solutions** HTML — mark-by-mark with M1 / A1 / R1 callouts.
   Reference template: `Unit_A3_Combinatorics_Solutions.html`.
4. **ZH translation** of all three (English-first per the locked
   playbook in `prompts/create-bilingual-translation.md`).

Total Sprint 3 deliverable count: 22 × 4 = **88 deliverables**. The
active sprint tracker lives in `IB Math HL/AUDIT.md`.

## Legacy unit retirement plan

| Legacy unit | Covers 2029 super-topics | Retirement trigger | Disposition |
|---|---|---|---|
| `Unit_A_Number_and_Algebra.html` (archived) | all of A1 – A5 (legacy monolith) | already archived 2026-05-15 | gone from deploy via `deploy.yml` strip; full deletion when every A* super-topic unit ships |
| `Unit_A1_Sequences_and_Series.html` (shipped) | A1 (clean match — no straddle) | — | KEEP. Filename matches 2029 super-topic ID. |
| `Unit_A3_Combinatorics.html` (shipped) | A3 (clean match) | — | KEEP. Filename matches 2029 super-topic ID. |
| `Unit_A4_Complex_Numbers.html` (shipped) | A4 (clean match) | — | KEEP. Filename matches 2029 super-topic ID. |
| `Unit_C_Geometry.html` (shipped) | straddles B4 + C1 + C2 | When standalone B4, C1, C2 all ship | archive to `rag/archive/` once the three new units are live; strip from deploy via `deploy.yml` |
| `Unit_D1_Univariate_Data.html` (shipped) | D1 (clean match — 2029 AA D1 includes bivariate) | — | KEEP. |
| `Unit_D2_Probability.html` (shipped) | D2 (clean match) | — | KEEP. |
| `Unit_D3_Probability_Distributions.html` (shipped) | D3 (clean match) | — | KEEP. |

> **D-units `.ib-ref` chips.** D1 / D2 / D3 carry per-section `.ib-ref`
> chips that label each section with its 2021 sub-topic number (e.g.
> `SL 4.4`, `AHL 4.10`). When the 2029 guide is published with
> sub-bullet numbering, retrofit these chips to also surface the 2029
> sub-bullet ID. Track as a P1 audit item; not blocking.

> **A5 merge.** Sprint 1's S1-5 (Proof, covered 2021 1.6 + 1.15) and
> S1-6 (Algebra & Systems, covered 2021 1.11 + linear systems) collapse
> into the single 2029 super-topic **A5 Proof and algebraic
> manipulation**. Ship as one unit: `Unit_A5_Proof_and_Algebraic_Manipulation.html`.

---

## Master sprint tracker

Sprint 3 progress is tracked in `IB Math HL/AUDIT.md` under
"### Sprint 3 — Complete the 2029 units". That table has one row per
2029 super-topic with status per deliverable (Study Guide / Practice /
Solutions / ZH-translation). This spec file is the **content
authority** (super-topic titles, SL/AHL classification, filename
convention, 2021 → 2029 mapping). The audit is the **status authority**
(what's shipped, what's open, what's blocked).
