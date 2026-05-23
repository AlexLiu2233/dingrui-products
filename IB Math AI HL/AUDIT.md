# IB Math AI HL — Audit

Open punch list for the IB Math AI HL products (Study Guides + Practice
Questions + Solutions), scored against `prompts/create-unit.md`,
`rag/subjects/ib_math_ai_hl.md`, and the official IB Mathematics:
Applications and Interpretation HL guide (first exams 2021).

**Tier definitions**

- **P0** — content-correctness or coverage gap that blocks "going for a 7"
  use of the product.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the IB Math AI HL subject
(Applications and Interpretation HL). The Analysis and Approaches HL
track is `IB Math HL/AUDIT.md`.

Last reviewed: **2026-05-22** (Sprint 3 opened — entire subject is
greenfield as of this date).

---

## Active Sprint — what we're working on now

### Sprint 3 — Complete the units (opened 2026-05-22)

**Goal.** Every official IB Math AI HL sub-topic ships as a unit with
4 deliverables: Study Guide, Practice Questions, Solutions,
ZH translation. Subject is greenfield; 63 sub-topics × 4 deliverables
= **252 deliverables** total.

**Cadence.** Per the locked review-then-merge pattern, each Study Guide
ships as its own commit. Practice + Solutions follow per unit.
ZH translation pass per the locked English-first → ZH playbook.

**Sub-topic numbering.** Verify against the official AI HL guide
before drafting — the spec at `rag/subjects/ib_math_ai_hl.md` is v0
and explicitly flagged for verification. **High uncertainty** on:
total sub-topic count per topic; exact sub-topic titles; SL/AHL
boundary; placement of Markov chains (Topic 1 vs Topic 4); placement
of graph theory.

**Order of operations.** Suggested build order per topic — start
with the SL sub-topics that have no prior dependencies, then layer
AHL extensions:

1. **Topic 1** (Number & Algebra, 16 units): 1.1 → 1.5 → 1.2 → 1.3 → 1.4 → 1.6 → 1.7 → 1.8 → AHL 1.9 → 1.10 → 1.11 → 1.12 → 1.13 → 1.14 → 1.15 → 1.16
2. **Topic 2** (Functions, 10 units): 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → AHL 2.7 → 2.8 → 2.9 → 2.10
3. **Topic 3** (Geometry & Trig, 10 units): 3.1 → 3.2 → 3.3 → 3.4 → 3.5 → AHL 3.6 → 3.7 → 3.8 → 3.9 → 3.10
4. **Topic 4** (Statistics & Probability, 15 units — AI's largest): 4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6 → 4.7 → 4.8 → 4.9 → 4.10 → 4.11 → 4.12 → AHL 4.13 → 4.14 → 4.15
5. **Topic 5** (Calculus, 12 units): 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6 → AHL 5.7 → 5.8 → 5.9 → 5.10 → 5.11 → 5.12

---

## Sprint 3 deliverable grid

Status legend per cell: `⬜` unbuilt · `🟡` drafting · `✅` shipped · `🌐` ZH translation done

### Topic 1 — Number and Algebra (16 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 1.1 | SL | Scientific Notation | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.2 | SL | Arithmetic Sequences & Series | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.3 | SL | Geometric Sequences & Series | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.4 | SL | Financial Mathematics | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.5 | SL | Exponent Laws | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.6 | SL | Approximation | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.7 | SL | Amortization & Annuities | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.8 | SL | Linear Systems (Technology) | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.9 | AHL | Logarithm Laws | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.10 | AHL | Infinite Geometric Series | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.11 | AHL | Rational Exponents | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.12 | AHL | Complex Numbers | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.13 | AHL | Matrices — Introduction | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.14 | AHL | Eigenvalues & Eigenvectors | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.15 | AHL | Matrix Applications (incl. Markov chains) | ⬜ | ⬜ | ⬜ | ⬜ |
| 1.16 | AHL | Graph Theory | ⬜ | ⬜ | ⬜ | ⬜ |

### Topic 2 — Functions (10 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 2.1 | SL | Straight Lines | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.2 | SL | Function Concepts (Domain, Range, Notation) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.3 | SL | Function Families & Key Features | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.4 | SL | Modelling — Choosing a Model | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.5 | SL | Regression Modelling (Technology) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.6 | SL | Piecewise Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.7 | AHL | Composite & Inverse Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.8 | AHL | Logistic Models | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.9 | AHL | Logarithmic Scaling | ⬜ | ⬜ | ⬜ | ⬜ |
| 2.10 | AHL | Linearizing Data | ⬜ | ⬜ | ⬜ | ⬜ |

### Topic 3 — Geometry and Trigonometry (10 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 3.1 | SL | 3D Geometry, Volumes, Surface Areas | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.2 | SL | Right-Angled Trigonometry | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.3 | SL | Sine & Cosine Rules, Triangle Area | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.4 | SL | 3D Trigonometry Applications | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.5 | SL | Voronoi Diagrams (AI signature) | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.6 | AHL | Vectors — Introduction | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.7 | AHL | Scalar (Dot) Product | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.8 | AHL | Vector Equations of Lines | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.9 | AHL | Vector Kinematics | ⬜ | ⬜ | ⬜ | ⬜ |
| 3.10 | AHL | Vector (Cross) Product | ⬜ | ⬜ | ⬜ | ⬜ |

### Topic 4 — Statistics and Probability (15 sub-topics — largest topic)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 4.1 | SL | Sampling & Bias | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.2 | SL | Data Presentation | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.3 | SL | Central Tendency & Dispersion | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.4 | SL | Bivariate Linear (Pearson, Regression) | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.5 | SL | Spearman's Rank | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.6 | SL | Probability Basics | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.7 | SL | Combined Events | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.8 | SL | Conditional & Independent Events | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.9 | SL | Discrete Random Variables | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.10 | SL | Binomial Distribution | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.11 | SL | Normal Distribution | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.12 | SL | Chi-Squared Tests (AI-specific) | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.13 | AHL | RV Linear Transformations | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.14 | AHL | t-Tests & Confidence Intervals | ⬜ | ⬜ | ⬜ | ⬜ |
| 4.15 | AHL | Markov Chains | ⬜ | ⬜ | ⬜ | ⬜ |

### Topic 5 — Calculus (12 sub-topics)

| Sub-topic | SL/AHL | Title | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| 5.1 | SL | Introduction to Differentiation | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.2 | SL | Increasing & Decreasing Functions | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.3 | SL | Power Rule | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.4 | SL | Tangents & Normals | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.5 | SL | Integration SL | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.6 | SL | Trapezoidal Rule | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.7 | AHL | Derivative Rules HL (chain/product/quotient + trig/exp/log) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.8 | AHL | Optimisation | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.9 | AHL | Advanced Integration | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.10 | AHL | Differential Equations (Euler, slope fields) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.11 | AHL | Coupled Systems (AI signature) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5.12 | AHL | Modelling with DEs | ⬜ | ⬜ | ⬜ | ⬜ |

---

## Standing Principles

*To be locked once the first AI HL Study Guide ships.* Candidate
principles inherited from AA HL:

- **Dual-goal contract** — cram cheat-sheet + 7-chaser depth.
- **HL flagging** via `hl-flag` chip on HL-only sub-topics.
- **Sub-topic numbering** matches the official IB AI HL guide so a
  student can map any syllabus reference directly to a unit.

AI-specific principles likely to lock here:

- **Calculator-throughout chrome.** No "no calculator" pill anywhere
  in AI HL practice files (Paper 1 permits GDC, unlike AA).
- **Modelling-first worked examples.** Worked examples should lean
  toward real-world data scenarios. Population dynamics, finance,
  surveys, voting patterns are good defaults.
- **Real datasets in Practice Questions.** Practice questions should
  pose problems against concrete data tables rather than abstract
  symbolic setups.

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Voronoi diagram interactive widget | One-slider-one-concept candidate: "add a site at (x, y) and watch the diagram redraw". Beyond static HTML — needs a JS implementation of Fortune's algorithm. |
| DP-2 | Markov chain steady-state visualizer | Same envelope issue as DP-1 — stateful interactive tool. The static unit can still present transition matrices and steady-state calculations. |
| DP-3 | Coupled DE phase portrait viewer | Tied to Topic 5.11. Could be a JSXGraph component. |
| DP-4 | Live regression-fit demo (drag points, watch line) | Topic 2.5 (Regression Modelling) is a natural fit. Punted until the static unit is reviewed. |
