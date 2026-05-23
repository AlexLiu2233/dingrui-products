# Subject Spec — IB Math AI HL

## Identity

- **Display (section heading):** IB Math AI HL
- **Display (hero chip):** IB Math AI HL
- **Directory:** `IB Math AI HL/` (greenfield as of 2026-05-22)
- **Audit:** `IB Math AI HL/AUDIT.md` (Sprint 3 = "Complete the units")

## Official curriculum reference

**IB Mathematics: Applications and Interpretation HL guide, first exams 2021.**
The "AI" track is distinct from "AA" (Analysis and Approaches) —
see `ib_math_aa_hl.md`. AI is the more applied / modeling-oriented
track: graph theory, Voronoi diagrams, statistical tests, Markov
chains, and numerical methods replace AA's abstract function theory,
deeper integration techniques, and Maclaurin series. AI students sit
the same paper format as AA students (Paper 1, 2, 3) but with content
slanted toward real-world modelling.

> **High-uncertainty notice 2026-05-22.** The sub-topic enumeration
> below was drafted from working knowledge of the AI HL syllabus and
> is **not yet verified line-by-line against the official IB AI HL
> guide**. Sub-topic titles, the exact SL / AHL boundary, and the
> assignment of certain HL extensions (Markov chains / coupled DE
> systems / graph theory) may be off. Treat this file as a v0 draft
> until the user confirms sub-topic numbering against their IB AI HL
> printed guide.
>
> **What to verify**: (1) the total sub-topic count per topic; (2)
> exact sub-topic titles; (3) the SL/AHL boundary; (4) whether
> "Markov chains" sits in Topic 1 (matrices) or Topic 4 (probability);
> (5) whether "graph theory" is in Topic 3 or in a separate AHL block.

## Naming convention (mirrors AA HL)

Units are named after their official IB sub-topic number so a student
can match any AI HL syllabus reference (e.g. "AHL 4.15 t-tests")
directly to one of our units.

```
IB Math AI HL/Study Guides/Unit_<T>_<N>_<Slug>.html
IB Math AI HL/Practice Questions/Unit_<T>_<N>_<Slug>_Practice.html
IB Math AI HL/Practice Questions/Solutions/Unit_<T>_<N>_<Slug>_Solutions.html
```

`<T>` is the Topic number (1–5). `<N>` is the sub-topic number.
Periods in IB references become underscores in filenames. Example:

- Sub-topic AHL 4.15 (t-tests) →
  `Unit_4_15_t_Tests.html`

## Required `<title>` format

```
IB Math AI HL — Unit {T.N}: {Sub-topic Title} | Dingrui Scholars
```

Example: `IB Math AI HL — Unit 3.5: Voronoi Diagrams | Dingrui Scholars`.

## Exam structure (HL)

- **Paper 1:** Short / medium / extended response, calculator allowed (AI is calculator-throughout, unlike AA).
- **Paper 2:** Longer response questions, calculator allowed.
- **Paper 3 (HL only):** Two extended modelling questions, 1h.
- **Internal Assessment:** Mathematical exploration with real-world data.

> **Key AI / AA difference**: AI permits a calculator on Paper 1.
> AA Paper 1 is no-calculator. Practice question chrome should
> reflect this — no `<span class="pill p1a">Paper 1A · No
> calculator</span>` style chip for AI.

## Standing principle — dual-goal contract

Same as AA HL. Every guide serves the **crammer** AND the **7-chaser**.
Cram cheat-sheet on top → worked examples → "going deeper" derivation /
modelling-context discussion. AI-specific framing: worked examples
should lean toward **real-world data scenarios** (population growth,
investment, traffic flow, demographics) rather than abstract algebra.

Flashcards: locked terse style from AA HL A1/A3.

## HL flagging

HL-only sub-topics carry the `hl-flag` chip. AI HL has substantial
HL-only content: matrices, eigenvalues, Markov chains, t-tests,
chi-squared (some variants), coupled DEs, graph theory.

---

## Unit list — full IB AI HL sub-topic enumeration (v0 — verify with user)

Status legend:
- ✅ **shipped** — Study Guide live (none yet for AI HL)
- ⬜ **unbuilt** — no coverage in the repo yet (all of AI HL — greenfield)

### Topic 1 — Number and Algebra (proposed 16 sub-topics)

| Sub-topic | Title (proposed) | SL/AHL | Status | Target file |
|---|---|---|---|---|
| 1.1 | Operations with numbers in scientific form $a \times 10^k$ | SL | ⬜ | `Unit_1_1_Scientific_Notation.html` |
| 1.2 | Arithmetic sequences and series; sigma notation; real-world applications | SL | ⬜ | `Unit_1_2_Arithmetic_Sequences.html` |
| 1.3 | Geometric sequences and series; sigma notation; real-world applications | SL | ⬜ | `Unit_1_3_Geometric_Sequences.html` |
| 1.4 | Financial applications: compound interest, depreciation, real / nominal interest, inflation, annuities, amortization | SL | ⬜ | `Unit_1_4_Financial_Mathematics.html` |
| 1.5 | Laws of exponents with integer exponents | SL | ⬜ | `Unit_1_5_Exponent_Laws.html` |
| 1.6 | Approximation: decimal places, significant figures, percentage error, upper and lower bounds | SL | ⬜ | `Unit_1_6_Approximation.html` |
| 1.7 | Amortization and annuities (technology-driven) | SL | ⬜ | `Unit_1_7_Amortization.html` |
| 1.8 | Solving systems of linear equations (up to 3 variables) using technology | SL | ⬜ | `Unit_1_8_Linear_Systems.html` |
| 1.9 | Laws of logarithms; solving exponential equations | AHL | ⬜ | `Unit_1_9_Logarithm_Laws.html` |
| 1.10 | Sum of infinite convergent geometric sequences | AHL | ⬜ | `Unit_1_10_Infinite_Geometric.html` |
| 1.11 | Laws of exponents with rational exponents | AHL | ⬜ | `Unit_1_11_Rational_Exponents.html` |
| 1.12 | Complex numbers (Cartesian, polar / Euler forms); applications to AC circuits and oscillation | AHL | ⬜ | `Unit_1_12_Complex_Numbers.html` |
| 1.13 | Matrices: definitions, operations (add, subtract, multiply, scalar), identity, inverse, determinant | AHL | ⬜ | `Unit_1_13_Matrices_Introduction.html` |
| 1.14 | Eigenvalues and eigenvectors of 2x2 matrices; diagonalization | AHL | ⬜ | `Unit_1_14_Eigenvalues_and_Eigenvectors.html` |
| 1.15 | Applications of matrices: solving linear systems, transformations, Markov chains, steady-state vectors | AHL | ⬜ | `Unit_1_15_Matrix_Applications.html` |
| 1.16 | Graph theory: vertices, edges, adjacency matrices, walks, paths, cycles, trees, shortest path algorithms | AHL | ⬜ | `Unit_1_16_Graph_Theory.html` |

### Topic 2 — Functions (proposed 10 sub-topics)

| Sub-topic | Title (proposed) | SL/AHL | Status | Target file |
|---|---|---|---|---|
| 2.1 | Different forms of straight-line equations; gradients; parallel and perpendicular lines | SL | ⬜ | `Unit_2_1_Straight_Lines.html` |
| 2.2 | Concept of function; domain, range, function notation; graphs and key features | SL | ⬜ | `Unit_2_2_Function_Concepts.html` |
| 2.3 | Graphs and key features of: linear, quadratic, exponential, sinusoidal, cubic, direct/inverse variation functions | SL | ⬜ | `Unit_2_3_Function_Families.html` |
| 2.4 | Modelling with the above functions; selecting an appropriate model from a context or scatter plot | SL | ⬜ | `Unit_2_4_Modelling_with_Functions.html` |
| 2.5 | Modelling with technology: regression to fit a model; goodness of fit | SL | ⬜ | `Unit_2_5_Regression_Modelling.html` |
| 2.6 | Modelling with piecewise functions | SL | ⬜ | `Unit_2_6_Piecewise_Functions.html` |
| 2.7 | Composite functions; inverse functions | AHL | ⬜ | `Unit_2_7_Composite_and_Inverse.html` |
| 2.8 | Modelling with logistic functions $L / (1 + Ce^{-kt})$ | AHL | ⬜ | `Unit_2_8_Logistic_Models.html` |
| 2.9 | Scaling very large or very small numbers using logarithms (logarithmic graphs, log-log paper) | AHL | ⬜ | `Unit_2_9_Logarithmic_Scaling.html` |
| 2.10 | Linearizing data using logarithms; using a log graph to determine the model parameters | AHL | ⬜ | `Unit_2_10_Linearizing_Data.html` |

### Topic 3 — Geometry and Trigonometry (proposed 10 sub-topics)

| Sub-topic | Title (proposed) | SL/AHL | Status | Target file |
|---|---|---|---|---|
| 3.1 | Distance between points in 3D; midpoint; volume and surface area of solids | SL | ⬜ | `Unit_3_1_3D_Geometry.html` |
| 3.2 | Right-angled trigonometry; angles of elevation and depression | SL | ⬜ | `Unit_3_2_Right_Angled_Trig.html` |
| 3.3 | Non-right-angled trigonometry: sine rule, cosine rule, area of a triangle | SL | ⬜ | `Unit_3_3_Sine_and_Cosine_Rules.html` |
| 3.4 | Applications of trig to 3D problems (bearings, navigation, surveying) | SL | ⬜ | `Unit_3_4_3D_Trigonometry_Applications.html` |
| 3.5 | Voronoi diagrams: nearest-neighbour interpolation, adding sites, "toxic-waste-dump" problems (AI signature topic) | SL | ⬜ | `Unit_3_5_Voronoi_Diagrams.html` |
| 3.6 | Vectors: position, displacement, base vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$, magnitude, unit vectors | AHL | ⬜ | `Unit_3_6_Vectors_Introduction.html` |
| 3.7 | Scalar (dot) product; angle between vectors; perpendicular and parallel | AHL | ⬜ | `Unit_3_7_Scalar_Product.html` |
| 3.8 | Vector equation of a line in 2D / 3D; intersections | AHL | ⬜ | `Unit_3_8_Vector_Equations_of_Lines.html` |
| 3.9 | Vector applications to kinematics: position, velocity, displacement | AHL | ⬜ | `Unit_3_9_Vector_Kinematics.html` |
| 3.10 | Vector product (cross product); applications to area and torque | AHL | ⬜ | `Unit_3_10_Vector_Product.html` |

### Topic 4 — Statistics and Probability (proposed 15 sub-topics — AI's largest topic)

| Sub-topic | Title (proposed) | SL/AHL | Status | Target file |
|---|---|---|---|---|
| 4.1 | Concepts of population, sample, random sample; sampling techniques; reliability and bias | SL | ⬜ | `Unit_4_1_Sampling_and_Bias.html` |
| 4.2 | Presentation of data: tables, histograms, cumulative frequency, box plots, stem-and-leaf | SL | ⬜ | `Unit_4_2_Data_Presentation.html` |
| 4.3 | Measures of central tendency and dispersion (mean, median, mode, IQR, SD, variance) | SL | ⬜ | `Unit_4_3_Central_Tendency_and_Dispersion.html` |
| 4.4 | Bivariate data: scatter, Pearson PMCC $r$, line of best fit, regression $y = ax + b$ | SL | ⬜ | `Unit_4_4_Bivariate_Linear.html` |
| 4.5 | Spearman's rank correlation coefficient $r_s$ (AI-specific addition vs AA) | SL | ⬜ | `Unit_4_5_Spearman_Rank.html` |
| 4.6 | Probability: trial, outcome, sample space, event, $P(A) = n(A)/n(U)$, complement | SL | ⬜ | `Unit_4_6_Probability_Basics.html` |
| 4.7 | Combined events: addition rule, mutually exclusive, tree / Venn / sample-space diagrams | SL | ⬜ | `Unit_4_7_Combined_Events.html` |
| 4.8 | Conditional probability and independence | SL | ⬜ | `Unit_4_8_Conditional_and_Independent.html` |
| 4.9 | Discrete random variables and probability distributions; expected value $E(X)$ | SL | ⬜ | `Unit_4_9_Discrete_RVs.html` |
| 4.10 | Binomial distribution: mean $np$, variance $np(1-p)$ | SL | ⬜ | `Unit_4_10_Binomial_Distribution.html` |
| 4.11 | Normal distribution; standardisation; inverse normal calculations | SL | ⬜ | `Unit_4_11_Normal_Distribution.html` |
| 4.12 | Goodness-of-fit and contingency-table tests using chi-squared $\chi^2$ (AI-specific vs AA) | SL | ⬜ | `Unit_4_12_Chi_Squared_Tests.html` |
| 4.13 | Linear transformations of a single random variable: $E(aX+b) = aE(X)+b$, $\text{Var}(aX+b) = a^2\text{Var}(X)$ | AHL | ⬜ | `Unit_4_13_RV_Linear_Transformations.html` |
| 4.14 | Confidence intervals for the mean of a normal population; t-distribution; small-sample inference; t-tests (one-sample, two-sample, paired) | AHL | ⬜ | `Unit_4_14_t_Tests_and_CIs.html` |
| 4.15 | Markov chains: transition matrices, steady-state vectors, applications to population dynamics, weather, queueing | AHL | ⬜ | `Unit_4_15_Markov_Chains.html` |

### Topic 5 — Calculus (proposed 12 sub-topics)

| Sub-topic | Title (proposed) | SL/AHL | Status | Target file |
|---|---|---|---|---|
| 5.1 | Introduction to limits and the derivative; gradient at a point | SL | ⬜ | `Unit_5_1_Introduction_to_Differentiation.html` |
| 5.2 | Increasing and decreasing functions; graphical interpretation of $f'(x)$ | SL | ⬜ | `Unit_5_2_Increasing_Decreasing.html` |
| 5.3 | Power rule, sum / difference rules for $f(x) = ax^n$, $n \in \mathbb{Z}$ | SL | ⬜ | `Unit_5_3_Power_Rule.html` |
| 5.4 | Tangents and normals at a given point | SL | ⬜ | `Unit_5_4_Tangents_and_Normals.html` |
| 5.5 | Anti-derivatives of polynomials; definite integrals; area under a curve | SL | ⬜ | `Unit_5_5_Integration_SL.html` |
| 5.6 | Numerical integration: trapezoidal rule | SL | ⬜ | `Unit_5_6_Trapezoidal_Rule.html` |
| 5.7 | Derivatives of $\sin x$, $\cos x$, $e^x$, $\ln x$; chain / product / quotient rules | AHL | ⬜ | `Unit_5_7_Derivative_Rules_HL.html` |
| 5.8 | Optimisation; related rates | AHL | ⬜ | `Unit_5_8_Optimisation.html` |
| 5.9 | Definite integrals of $\sin x$, $\cos x$, $e^x$, $1/x$; areas between curves; volumes of revolution | AHL | ⬜ | `Unit_5_9_Advanced_Integration.html` |
| 5.10 | First-order differential equations: Euler's method, slope fields, separation of variables | AHL | ⬜ | `Unit_5_10_Differential_Equations.html` |
| 5.11 | Coupled systems of first-order DEs: phase portraits, equilibrium points, classification (AI signature topic) | AHL | ⬜ | `Unit_5_11_Coupled_Systems.html` |
| 5.12 | Modelling with DEs: SIR models, predator-prey, simple harmonic / damped oscillators | AHL | ⬜ | `Unit_5_12_Modelling_with_DEs.html` |

---

## Coverage roll-up (as of 2026-05-22)

- **Topic 1**: 16 sub-topics, all unbuilt
- **Topic 2**: 10 sub-topics, all unbuilt
- **Topic 3**: 10 sub-topics, all unbuilt
- **Topic 4**: 15 sub-topics, all unbuilt
- **Topic 5**: 12 sub-topics, all unbuilt

**Total**: 63 sub-topics (provisional pending verification). **63 unbuilt** — AI HL is entirely greenfield.

## Deliverable contract per unit (Sprint 3)

Same as AA HL — four products per unit:
1. **Study Guide** HTML — dual-goal contract; AI-specific framing leans toward real-world data and modelling scenarios.
2. **Practice Questions** HTML — IB AI paper-style. EMH mix across Paper 1 (calculator allowed), Paper 2, Paper 3 (HL only). NO Paper-1A "no calculator" pill — AI Paper 1 permits calculators.
3. **Solutions** HTML — mark-by-mark with M1 / A1 / R1 callouts.
4. **ZH translation** of all three (English-first per the locked playbook).

Total AI HL Sprint 3 deliverable count: 63 × 4 = **252 deliverables**.

## Combined Sprint 3 scope

| Subject | Sub-topics | Unbuilt | Deliverables (× 4) |
|---|---|---|---|
| IB Math AA HL | 79 | 53 | ~212 |
| IB Math AI HL | 63 | 63 | 252 |
| **Total** | **142** | **116** | **~464** |

## Master sprint tracker

Sprint 3 progress is tracked in `IB Math AI HL/AUDIT.md` (to be
created) under "### Sprint 3 — Complete the units". Same pattern as
AA HL: one row per sub-topic with deliverable-status columns.

## Subject differentiation notes (AI vs AA)

If you've been working in AA HL and are picking up AI HL, the key
non-overlapping content to remember when drafting:

| AI HL has | AA HL has instead |
|---|---|
| Voronoi diagrams (3.5) | More vector geometry depth (lines, planes, intersections) |
| Matrices, eigenvalues, Markov chains | Complex numbers depth (De Moivre, roots of unity) |
| Graph theory | Proof by induction / contradiction / counterexample |
| Spearman's rank, chi-squared, t-tests | Bayes' theorem |
| Logistic models, piecewise modelling, logarithmic scaling of data | Polynomial / rational function depth (factor theorem, sum/product of roots) |
| Trapezoidal rule, Euler's method, coupled DE systems / phase portraits | Maclaurin series, integration by substitution / parts |

AI HL is calculator-throughout (Paper 1 allows GDC). AA HL Paper 1
is no-calculator. Practice question chrome and worked-example
expectations differ accordingly.
