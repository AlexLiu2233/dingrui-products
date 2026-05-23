# Subject Spec — IB Math AI HL

## Identity

- **Display (section heading):** IB Math AI HL
- **Display (hero chip):** IB Math AI HL
- **Directory:** `IB Math AI HL/` (greenfield as of 2026-05-22)
- **Audit:** `IB Math AI HL/AUDIT.md` (to be created when first unit drafts)
- **IB-authoritative source:** `rag/sources/IB Math HL/sb_maths_application_en.pdf`
  (Subject Brief, first assessment 2029)

## Official curriculum reference — 2029 syllabus (locked 2026-05-22)

**IB Mathematics: Applications and Interpretation, first assessment 2029.**
This spec is organized around the 2029 super-topic structure (5 Topics,
26 super-topics, AHL flagged). AI HL is entirely greenfield — no units
have shipped — so there is no 2021 → 2029 mapping pressure for already-
built content; we draft directly against 2029 from the start.

The "AI" track is distinct from "AA" (Analysis and Approaches) —
see `ib_math_aa_hl.md`. AI is the more applied / modelling-oriented
track: piecewise functions, matrices, graph theory, Voronoi diagrams,
statistical tests, and Markov chains replace AA's abstract function
theory, proof, deeper integration techniques, and Maclaurin series.
AI students sit Paper 1 **with a calculator**; AA students do not.

## Naming convention

Units are named after their 2029 super-topic ID.

```
IB Math AI HL/Study Guides/Unit_<SuperID>_<Slug>.html
IB Math AI HL/Practice Questions/Unit_<SuperID>_<Slug>_Practice.html
IB Math AI HL/Practice Questions/Solutions/Unit_<SuperID>_<Slug>_Solutions.html
```

`<SuperID>` is one of the 26 2029 super-topic identifiers (`A1` … `E5`).
Example: 2029 super-topic D5 "Inferential statistics" →
`Unit_D5_Inferential_Statistics.html`.

## Required `<title>` format

```
IB Math AI HL — Unit {SuperID}: {Super-topic Title} | Dingrui Scholars
```

Example: `IB Math AI HL — Unit C5: Graph Theory | Dingrui Scholars`.

## Exam structure — 2029 first assessment

- **Paper 1 (technology required):** SL 1h30 (40%), HL 2h (30%).
  Compulsory short-response questions.
- **Paper 2 (technology required):** SL 1h30 (40%), HL 2h (30%).
  Compulsory extended-response questions.
- **Paper 3 (HL only, technology required):** 1h (20%). Two compulsory
  extended-response questions.
- **Internal Assessment:** Mathematical exploration, 30 hours (20%).

Total external assessment: SL 3h / HL 5h (80% of final grade).

> **Key AI / AA difference.** AI Paper 1 permits a calculator. Practice
> question chrome should reflect this — **no `Paper 1A · No calculator`
> pill** for AI. Use a single Paper 1 pill (no A / B split, since AI
> Paper 1 is one block of short-response).

## Standing principle — dual-goal contract

Same as AA HL. Every guide serves the **crammer** AND the **7-chaser**.
Cram cheat-sheet on top → worked examples → "going deeper" derivation /
modelling-context discussion. AI-specific framing: worked examples
should lean toward **real-world data scenarios** (population growth,
investment, traffic flow, demographics, public health) rather than
abstract algebra.

Flashcards: locked terse style from AA HL A1/A3 (question on front,
`$$formula$$` on back, no prose).

## HL flagging

HL-only super-topics — **A6** Transformations of graphs and functions,
**B5** Matrices, **C4** Vectors, **C5** Graph theory, **E5** Differential
equations — carry the `hl-flag` chip at unit level. Within mixed-SL/HL
super-topics (the 21 others), individual sections carry `hl-flag` chips
per the pattern from AA HL.

---

## Unit list — 2029 super-topic enumeration (26 units total)

Hours figures are IB-recommended teaching hours per Topic (SL / HL),
not per super-topic. They give a rough sense of weighting.

Status legend:
- ⬜ **unbuilt** — no coverage in the repo yet (all of AI HL — greenfield)

### Topic A — Functions (SL 31h, HL 45h) — 6 super-topics

| ID | Super-topic | SL/AHL | Status | Target file |
|---|---|---|---|---|
| **A1** | Representation of functions | SL + AHL | ⬜ | `Unit_A1_Representation_of_Functions.html` |
| **A2** | Polynomial functions | SL + AHL | ⬜ | `Unit_A2_Polynomial_Functions.html` |
| **A3** | Functions with asymptotes | SL + AHL | ⬜ | `Unit_A3_Functions_with_Asymptotes.html` |
| **A4** | Trigonometric functions | SL + AHL | ⬜ | `Unit_A4_Trigonometric_Functions.html` |
| **A5** | Piecewise functions | SL + AHL | ⬜ | `Unit_A5_Piecewise_Functions.html` |
| **A6** | Transformations of graphs and functions (HL only) | AHL | ⬜ | `Unit_A6_Transformations_of_Graphs.html` |

### Topic B — Number and Algebra (SL 16h, HL 27h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Target file |
|---|---|---|---|---|
| **B1** | Approximation and error | SL + AHL | ⬜ | `Unit_B1_Approximation_and_Error.html` |
| **B2** | Sequences | SL + AHL | ⬜ | `Unit_B2_Sequences.html` |
| **B3** | Use of technology applications | SL + AHL | ⬜ | `Unit_B3_Technology_Applications.html` |
| **B4** | Exponentials | SL + AHL | ⬜ | `Unit_B4_Exponentials.html` |
| **B5** | Matrices (HL only) | AHL | ⬜ | `Unit_B5_Matrices.html` |

### Topic C — Geometry (SL 18h, HL 45h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Target file |
|---|---|---|---|---|
| **C1** | Straight line geometry | SL | ⬜ | `Unit_C1_Straight_Line_Geometry.html` |
| **C2** | Surface areas, volumes and measurement in circles | SL | ⬜ | `Unit_C2_Surface_Areas_and_Volumes.html` |
| **C3** | Trigonometry and its applications | SL + AHL | ⬜ | `Unit_C3_Trigonometry_Applications.html` |
| **C4** | Vectors (HL only) | AHL | ⬜ | `Unit_C4_Vectors.html` |
| **C5** | Graph theory (HL only) | AHL | ⬜ | `Unit_C5_Graph_Theory.html` |

> **AI-distinctive super-topic.** C5 Graph theory is unique to AI HL —
> it does not appear in AA HL. Vertices / edges / adjacency matrices /
> walks / paths / trees / shortest path are real-world-modelling
> content not covered in AA.

### Topic D — Probability and Statistics (SL 36h, HL 52h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Target file |
|---|---|---|---|---|
| **D1** | Univariate data | SL | ⬜ | `Unit_D1_Univariate_Data.html` |
| **D2** | Bivariate data | SL + AHL | ⬜ | `Unit_D2_Bivariate_Data.html` |
| **D3** | Probability | SL + AHL | ⬜ | `Unit_D3_Probability.html` |
| **D4** | Probability distributions | SL + AHL | ⬜ | `Unit_D4_Probability_Distributions.html` |
| **D5** | Inferential statistics | SL + AHL | ⬜ | `Unit_D5_Inferential_Statistics.html` |

> **AI vs AA structural difference.** AI splits stats into 5 super-topics
> where AA collapses to 3. AI's separate D5 Inferential Statistics
> super-topic (chi-squared tests, t-tests, confidence intervals) and
> separate D2 Bivariate Data super-topic (PMCC, Spearman, regression)
> are AI-distinctive content not paralleled in AA.

### Topic E — Calculus (SL 19h, HL 41h) — 5 super-topics

| ID | Super-topic | SL/AHL | Status | Target file |
|---|---|---|---|---|
| **E1** | Principles of differential calculus | SL + AHL | ⬜ | `Unit_E1_Principles_of_Differential_Calculus.html` |
| **E2** | Techniques of differential calculus | SL + AHL | ⬜ | `Unit_E2_Techniques_of_Differential_Calculus.html` |
| **E3** | Techniques of integral calculus | SL + AHL | ⬜ | `Unit_E3_Techniques_of_Integral_Calculus.html` |
| **E4** | Problem-solving using calculus | SL + AHL | ⬜ | `Unit_E4_Problem_Solving_Using_Calculus.html` |
| **E5** | Differential equations (HL only) | AHL | ⬜ | `Unit_E5_Differential_Equations.html` |

> **AI vs AA in calculus.** AA HL has E5 Differential equations AND E6
> Maclaurin series. AI HL has E5 only; Maclaurin series is not in AI.
> Conversely, AI Topic E emphasizes the trapezoidal rule, Euler's
> method, and coupled DE systems for real-world modelling — content
> not in AA.

---

## Coverage roll-up (as of 2026-05-22)

| 2029 Topic | Super-topics | ✅ shipped | ⬜ unbuilt |
|---|---|---|---|
| **A** Functions | 6 | 0 | 6 |
| **B** Number and Algebra | 5 | 0 | 5 |
| **C** Geometry | 5 | 0 | 5 |
| **D** Statistics and Probability | 5 | 0 | 5 |
| **E** Calculus | 5 | 0 | 5 |
| **Total** | **26** | **0** | **26** |

AI HL is entirely greenfield.

## Sprint 3 deliverable contract per super-topic

For each of the 26 super-topics, four products ship in order:

1. **Study Guide** HTML — dual-goal contract; cram cheat-sheet,
   sections (one per major sub-bullet of the super-topic), worked
   examples (real-world modelling slant for AI), per-section quizzes,
   final unit quiz, flashcards (locked terse style), 14-item readiness
   checklist.
2. **Practice Questions** HTML — IB AI paper-style. EMH mix across
   Paper 1 (calculator allowed — no A/B split), Paper 2 (calculator),
   Paper 3 (HL only). NO Paper-1A "no calculator" pill — AI Paper 1
   permits calculators.
3. **Solutions** HTML — mark-by-mark with M1 / A1 / R1 callouts.
4. **ZH translation** of all three (English-first per the locked
   playbook in `prompts/create-bilingual-translation.md`).

Total AI HL Sprint 3 deliverable count: 26 × 4 = **104 deliverables**.

## Combined Sprint 3 scope across both Math HL subjects

| Subject | Super-topics | Already shipped | Deliverables (× 4) |
|---|---|---|---|
| IB Math AA HL | 22 | 6 (A1, A3, A4, D1, D2, D3) | 88 (16 already shipped as Study Guide + Translation; 72 remain) |
| IB Math AI HL | 26 | 0 | 104 |
| **Combined** | **48** | **6** | **192** |

## Master sprint tracker

Once AI HL drafting begins, Sprint 3 progress is tracked in
`IB Math AI HL/AUDIT.md` (to be created) under "### Sprint 3 —
Complete the 2029 units". This spec file is the **content authority**
(super-topic titles, SL/AHL classification, filename convention). The
audit is the **status authority** (what's shipped, what's open, what's
blocked).

## Subject differentiation notes (AI vs AA)

Key non-overlapping content to remember when drafting:

| AI HL has | AA HL has instead |
|---|---|
| C5 Graph theory (HL): vertices, edges, adjacency matrices, walks, trees, shortest path | A5 Proof: induction, contradiction, counterexamples |
| B5 Matrices (HL): operations, inverse, determinant, eigenvalues, Markov chains | A4 Complex numbers (HL): polar / Euler, De Moivre, roots of unity |
| D2 Bivariate data (separate super-topic): Spearman rank, regression | D1 includes bivariate (no separate super-topic) |
| D5 Inferential statistics: chi-squared, t-tests, confidence intervals | (not in AA) |
| A5 Piecewise functions: separate super-topic | (folded into B1 in AA) |
| C1 Straight line geometry: separate super-topic (geometric framing) | Lines in B1 Representation of functions (functional framing) |
| B1 Approximation and error: separate super-topic | (not in AA) |
| Trapezoidal rule, Euler's method, coupled DE systems for modelling | E6 Maclaurin series; integration by substitution / parts |

AI HL Paper 1 is calculator-allowed. AA HL Paper 1 is no-calculator.
Practice question chrome and worked-example expectations differ
accordingly.
