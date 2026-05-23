# Subject Spec — IB Math AA HL

## Identity

- **Display (section heading):** IB Math AA HL
- **Display (hero chip):** IB Math AA HL
- **Directory:** `IB Math HL/`
- **Audit:** `IB Math HL/AUDIT.md` (Sprint 3 = "Complete the units" — every official IB AA HL sub-topic becomes one unit)

## Official curriculum reference

**IB Mathematics: Analysis and Approaches HL guide, first exams 2021.**
The "AA" track is distinct from "AI" (Applications and Interpretation) —
see `ib_math_ai_hl.md` for the parallel subject. Sub-topic enumeration
below mirrors the official IB Topic numbering so a student can match any
syllabus reference (e.g. "AHL 3.13 vectors") directly to one of our
units.

> **Verification note 2026-05-22.** Sub-topic titles and SL / AHL splits
> below were drafted from working knowledge of the AA HL guide first
> exams 2021. Where a sub-topic title or boundary looks off relative to
> your IB AA HL printed guide, that's a spec bug — flag in review and
> update this file. The total sub-topic count below (79) is the working
> target.

## Naming convention

Units are named after their official IB sub-topic number — the
consumer-facing student can match any sub-topic reference in the IB
guide directly to one of our units.

```
IB Math HL/Study Guides/Unit_<T>_<N>_<Slug>.html
IB Math HL/Practice Questions/Unit_<T>_<N>_<Slug>_Practice.html
IB Math HL/Practice Questions/Solutions/Unit_<T>_<N>_<Slug>_Solutions.html
```

`<T>` is the Topic number (1–5). `<N>` is the sub-topic number. Periods
in IB references become underscores in filenames. Example:

- Sub-topic SL 4.4 (linear correlation of bivariate data) →
  `Unit_4_4_Bivariate_Data.html`

**Legacy filenames preserved.** Existing shipped units (Unit_A1,
Unit_A3, Unit_A4, Unit_C, Unit_D1, Unit_D2, Unit_D3) keep their current
filenames to avoid breaking deployed links. The mapping table below
shows which sub-topics each legacy unit covers, and notes when a legacy
unit's coverage will be retired in favour of split sub-topic units.

## Required `<title>` format

```
IB Math AA HL — Unit {T.N}: {Sub-topic Title} | Dingrui Scholars
```

Example: `IB Math AA HL — Unit 4.4: Bivariate Data | Dingrui Scholars`.
For legacy combined units the title format from existing shipped files
is preserved:
`IB Math AA HL — Unit A1: Sequences & Series | Dingrui Scholars`.

## Exam structure (HL)

- **Paper 1:** No calculator — short and extended response, 2h.
- **Paper 2:** Calculator allowed — short and extended response, 2h.
- **Paper 3 (HL only):** Two extended problem-solving investigations, 1h.
- **Internal Assessment:** Mathematical exploration.

## Standing principle — dual-goal contract

Every guide serves two students at once: the **crammer** (last-ditch
pass the night before) and the **7-chaser** (going deep for top score).
Canonical articulation in `prompts/create-unit.md`. Each section layers:
cheat-sheet at top → worked example(s) → "going deeper" proof /
derivation. Quiz items mix recall and synthesis.

Flashcards (when present) follow the locked terse style from A1/A3:
question on front, `$$formula$$` on back, no prose.

## HL flagging

HL-only sub-topics (the AHL extensions) carry the `hl-flag` chip (see
A1, A3, A4, D2 §2.7, D3 §§3.3 / 3.7 / 3.8 for the pattern). A reader
should see at a glance which content is HL-extension material.

In the table below, the **SL / AHL** column does this at spec level:
`SL` = required for both SL and HL students; `AHL` = HL-only extension.

---

## Unit list — full IB AA HL sub-topic enumeration

Status legend:
- ✅ **shipped** — Study Guide live on `main`; Practice / Solutions
  status tracked separately in `IB Math HL/AUDIT.md` Sprint 3 grid.
- 📁 **legacy-covered** — content is included in a legacy combined
  unit (A1 / A3 / A4 / C / D1 / D2 / D3); split-out unit not yet drafted.
- ⬜ **unbuilt** — no coverage in the repo yet.

### Topic 1 — Number and Algebra (16 sub-topics)

| Sub-topic | Title | SL/AHL | Status | Covered by / target file |
|---|---|---|---|---|
| 1.1 | Operations with numbers in scientific form $a \times 10^k$ | SL | ⬜ | `Unit_1_1_Scientific_Notation.html` |
| 1.2 | Arithmetic sequences and series, sigma notation, applications | SL | 📁 | covered by `Unit_A1_Sequences_and_Series.html` |
| 1.3 | Geometric sequences and series, sigma notation, applications | SL | 📁 | covered by `Unit_A1_Sequences_and_Series.html` |
| 1.4 | Financial applications of geometric sequences (compound interest, annuities, mortgages) | SL | 📁 | covered by `Unit_A1_Sequences_and_Series.html` |
| 1.5 | Laws of exponents with integer exponents; introduction to logarithms base 10 / base e | SL | ⬜ | `Unit_1_5_Exponents_and_Logarithms.html` |
| 1.6 | Simple deductive proof, numerical and algebraic | SL | ⬜ | `Unit_1_6_Simple_Proof.html` |
| 1.7 | Laws of exponents (rational exponents); laws of logarithms; change of base | SL | ⬜ | `Unit_1_7_Logarithm_Laws.html` |
| 1.8 | Sum of infinite convergent geometric sequences | SL | 📁 | covered by `Unit_A1_Sequences_and_Series.html` |
| 1.9 | The binomial theorem $(a+b)^n$, $n \in \mathbb{N}$; Pascal's triangle, $\binom{n}{r}$ | SL | 📁 | covered by `Unit_A3_Combinatorics.html` |
| 1.10 | Counting principles, permutations, combinations; extended binomial theorem (rational / negative indices) | AHL | 📁 | covered by `Unit_A3_Combinatorics.html` |
| 1.11 | Partial fractions (max two distinct linear terms in denominator) | AHL | ⬜ | `Unit_1_11_Partial_Fractions.html` |
| 1.12 | Complex numbers: Cartesian form $z = a + bi$, modulus, argument, conjugate | AHL | 📁 | covered by `Unit_A4_Complex_Numbers.html` |
| 1.13 | Modulus-argument (polar) form; Euler form $re^{i\theta}$; arithmetic in all three forms | AHL | 📁 | covered by `Unit_A4_Complex_Numbers.html` |
| 1.14 | Complex conjugate roots; De Moivre's theorem; powers and roots of complex numbers | AHL | 📁 | covered by `Unit_A4_Complex_Numbers.html` |
| 1.15 | Proof by mathematical induction; proof by contradiction; counterexamples | AHL | ⬜ | `Unit_1_15_Proof_HL.html` |
| 1.16 | Solutions of systems of linear equations (max 3 equations, 3 unknowns); unique / infinite / no solutions | AHL | ⬜ | `Unit_1_16_Linear_Systems.html` |

### Topic 2 — Functions (16 sub-topics)

| Sub-topic | Title | SL/AHL | Status | Covered by / target file |
|---|---|---|---|---|
| 2.1 | Equations of straight lines; gradients; parallel ($m_1 = m_2$) and perpendicular ($m_1 m_2 = -1$) | SL | ⬜ | `Unit_2_1_Straight_Lines.html` |
| 2.2 | Concept of function; domain, range; function notation; concept of inverse function | SL | ⬜ | `Unit_2_2_Functions_Domain_Range.html` |
| 2.3 | Graph of a function $y = f(x)$; creating sketches; using technology | SL | ⬜ | `Unit_2_3_Graphs_of_Functions.html` |
| 2.4 | Key features of graphs; intersections of curves; solving graphically | SL | ⬜ | `Unit_2_4_Key_Features.html` |
| 2.5 | Composite functions; identity function; finding $f^{-1}(x)$ | SL | ⬜ | `Unit_2_5_Composite_Functions_and_Inverses.html` |
| 2.6 | Quadratic function: graph, vertex, axis of symmetry; factored, vertex, standard forms | SL | ⬜ | `Unit_2_6_Quadratic_Functions.html` |
| 2.7 | Solution of quadratic equations and inequalities; quadratic formula; discriminant | SL | ⬜ | `Unit_2_7_Quadratic_Equations.html` |
| 2.8 | Reciprocal function $f(x) = 1/x$; rational $f(x) = (ax+b)/(cx+d)$; asymptotes | SL | ⬜ | `Unit_2_8_Rational_Functions_SL.html` |
| 2.9 | Exponential and logarithmic functions and their graphs | SL | ⬜ | `Unit_2_9_Exp_and_Log_Functions.html` |
| 2.10 | Solving equations both graphically and analytically | SL | ⬜ | `Unit_2_10_Solving_Equations.html` |
| 2.11 | Transformations of graphs: translations, reflections, stretches | SL | ⬜ | `Unit_2_11_Transformations.html` |
| 2.12 | Polynomial functions; factor and remainder theorems; sum / product of roots | AHL | ⬜ | `Unit_2_12_Polynomial_Functions_HL.html` |
| 2.13 | Rational functions $f(x) = (ax+b)/(cx^2+dx+e)$ and $f(x) = (ax^2+bx+c)/(dx+e)$ | AHL | ⬜ | `Unit_2_13_Rational_Functions_HL.html` |
| 2.14 | Odd and even functions; inverse with domain restriction; self-inverse functions | AHL | ⬜ | `Unit_2_14_Odd_Even_Self_Inverse.html` |
| 2.15 | Solutions of $g(x) \ge f(x)$ both graphically and analytically | AHL | ⬜ | `Unit_2_15_Function_Inequalities_HL.html` |
| 2.16 | Graphs of $\|f(x)\|$, $f(\|x\|)$, $1/f(x)$, $f(ax+b)$, $[f(x)]^2$ | AHL | ⬜ | `Unit_2_16_Graph_Transformations_HL.html` |

### Topic 3 — Geometry and Trigonometry (18 sub-topics)

| Sub-topic | Title | SL/AHL | Status | Covered by / target file |
|---|---|---|---|---|
| 3.1 | Distance between two points in 3D; midpoint; volume / surface area of solids | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.2 | Angle between two intersecting lines or between a line and a plane | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.3 | Right-angled trigonometry (sin / cos / tan ratios); sine rule (with ambiguous case); cosine rule; area $\tfrac{1}{2}ab\sin C$ | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.4 | Radian measure; arc length; sector area | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.5 | Unit-circle definition of $\cos\theta$, $\sin\theta$, $\tan\theta$; exact values | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.6 | Pythagorean identity $\cos^2\theta + \sin^2\theta = 1$; double-angle identities for sine and cosine | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.7 | Circular functions $\sin x$, $\cos x$, $\tan x$; amplitude, period, transformations; real-life contexts | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.8 | Solving trigonometric equations in a finite interval (graphical / analytical); quadratic in trig | SL | 📁 | covered by `Unit_C_Geometry.html` |
| 3.9 | Reciprocal trig ratios ($\sec, \csc, \cot$); inverse trig functions ($\arcsin, \arccos, \arctan$); Pythagorean identities involving these | AHL | ⬜ | `Unit_3_9_Reciprocal_and_Inverse_Trig.html` |
| 3.10 | Compound angle identities; double-angle identity for tan | AHL | ⬜ | `Unit_3_10_Compound_Angle_Identities.html` |
| 3.11 | Symmetry properties of trig functions; relationships between trig functions | AHL | ⬜ | `Unit_3_11_Trig_Symmetries.html` |
| 3.12 | Vectors: position / displacement; base vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$; components; magnitude; unit vectors | AHL | ⬜ | `Unit_3_12_Vectors_Introduction.html` |
| 3.13 | Scalar product (dot product); angle between two vectors; perpendicular / parallel vectors | AHL | ⬜ | `Unit_3_13_Scalar_Product.html` |
| 3.14 | Vector equation of a line in 2D and 3D: $\mathbf{r} = \mathbf{a} + \lambda \mathbf{b}$; angle between lines; simple kinematics | AHL | ⬜ | `Unit_3_14_Vector_Equations_of_Lines.html` |
| 3.15 | Coincident, parallel, intersecting, and skew lines; points of intersection | AHL | ⬜ | `Unit_3_15_Relationships_Between_Lines.html` |
| 3.16 | Vector product (cross product); $\|\mathbf{v}\times\mathbf{w}\|$ geometric interpretation; component form | AHL | ⬜ | `Unit_3_16_Vector_Product.html` |
| 3.17 | Vector equation of a plane: $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}$; $\mathbf{r}\cdot\mathbf{n} = \mathbf{a}\cdot\mathbf{n}$; Cartesian form $ax+by+cz=d$ | AHL | ⬜ | `Unit_3_17_Vector_Equations_of_Planes.html` |
| 3.18 | Intersections of: line with plane; two planes; three planes; angles | AHL | ⬜ | `Unit_3_18_Intersections.html` |

### Topic 4 — Statistics and Probability (11 sub-topics)

| Sub-topic | Title | SL/AHL | Status | Covered by / target file |
|---|---|---|---|---|
| 4.1 | Population, sample, random sample; discrete vs continuous; reliability and bias in sampling | SL | ✅ | covered by `Unit_D1_Univariate_Data.html` |
| 4.2 | Presentation of data: frequency distributions, histograms, cumulative frequency, box-and-whisker | SL | ✅ | covered by `Unit_D1_Univariate_Data.html` |
| 4.3 | Measures of central tendency (mean, median, mode); measures of dispersion (IQR, SD, variance); effect of linear transformations | SL | ✅ | covered by `Unit_D1_Univariate_Data.html` |
| 4.4 | Linear correlation of bivariate data; PMCC $r$; scatter; lines of best fit; regression $y = a + bx$ | SL | ✅ | covered by `Unit_D1_Univariate_Data.html` |
| 4.5 | Trial, outcome, equally likely, sample space $U$, event; $P(A) = n(A)/n(U)$; complementary events | SL | ✅ | covered by `Unit_D2_Probability.html` |
| 4.6 | Venn / tree / sample-space diagrams; combined events; mutually exclusive; conditional; independent | SL | ✅ | covered by `Unit_D2_Probability.html` |
| 4.7 | Discrete random variables and their probability distributions; expected value $E(X)$ | SL | ✅ | covered by `Unit_D3_Probability_Distributions.html` |
| 4.8 | Binomial distribution: mean $np$ and variance $np(1-p)$ | SL | ✅ | covered by `Unit_D3_Probability_Distributions.html` |
| 4.9 | Normal distribution; properties; standardisation; normal and inverse normal calculations | SL | ✅ | covered by `Unit_D3_Probability_Distributions.html` |
| 4.10 | Bayes' theorem for a maximum of three events | AHL | ✅ | covered by `Unit_D2_Probability.html` |
| 4.11 | Variance of discrete RV; continuous RVs and PDFs; mode / median / mean / variance / SD for both; effect of linear transformations of $X$ | AHL | ✅ | covered by `Unit_D3_Probability_Distributions.html` |

> **Spec note 2026-05-22.** `Unit_D3_Probability_Distributions.html`
> as shipped includes §§3.7 (continuous RVs + PDFs) and §3.8 (linear
> transformations + sums of independent RVs + linear combinations of
> normals). Per the AA HL guide first exams 2021 syllabus the only AHL
> Topic 4 extensions are **4.10** (Bayes) and **4.11** (variance +
> continuous RVs + linear transformations of a single $X$). The
> "sums of independent RVs / linear combination of normals" content in
> §3.8 of D3 **may be off-syllabus for AA HL** (those topics appear in
> AI HL and in first-year university probability courses). Track as a
> P1 audit item: confirm against your AA HL guide and either (a) keep
> the §3.8 content with an "enrichment, beyond syllabus" callout, or
> (b) trim §3.8 down to the strict linear-transformation content of
> 4.11.

### Topic 5 — Calculus (18 sub-topics)

| Sub-topic | Title | SL/AHL | Status | Covered by / target file |
|---|---|---|---|---|
| 5.1 | Introduction to limits; concept of differentiation; gradient of tangent at a point | SL | ⬜ | `Unit_5_1_Introduction_to_Differentiation.html` |
| 5.2 | Increasing and decreasing functions; graphical interpretation of $f'(x)$ | SL | ⬜ | `Unit_5_2_Increasing_Decreasing.html` |
| 5.3 | Derivative of $f(x) = ax^n$, $n \in \mathbb{Z}$; sum and difference rules; constant multiples | SL | ⬜ | `Unit_5_3_Power_Rule_and_Linearity.html` |
| 5.4 | Tangents and normals at a given point and their equations | SL | ⬜ | `Unit_5_4_Tangents_and_Normals.html` |
| 5.5 | Anti-differentiation of polynomials; anti-differentiation with a boundary condition | SL | ⬜ | `Unit_5_5_Anti_Differentiation.html` |
| 5.6 | Definite integrals; area enclosed by a curve and the $x$-axis | SL | ⬜ | `Unit_5_6_Definite_Integrals.html` |
| 5.7 | Derivatives of: $ax^n$ ($n \in \mathbb{Q}$), $\sin x$, $\cos x$, $e^x$, $\ln x$; chain / product / quotient rules | SL | ⬜ | `Unit_5_7_Derivative_Rules.html` |
| 5.8 | Local maxima and minima; testing using first or second derivative | SL | ⬜ | `Unit_5_8_Maxima_and_Minima.html` |
| 5.9 | Kinematics: displacement, velocity, acceleration; total distance travelled | SL | ⬜ | `Unit_5_9_Kinematics.html` |
| 5.10 | Indefinite integrals of $x^n$, $\sin x$, $\cos x$, $1/x$, $e^x$ with linear arguments; reverse chain rule; areas between curves | SL | ⬜ | `Unit_5_10_Indefinite_Integrals.html` |
| 5.11 | Definite integrals → areas under a curve and volumes of revolution about the $x$-axis | SL | ⬜ | `Unit_5_11_Volumes_of_Revolution.html` |
| 5.12 | Continuity / differentiability (informal); differentiating $\ln x$ and $\tan x$; differentiability of piecewise functions | AHL | ⬜ | `Unit_5_12_Continuity_and_Differentiability.html` |
| 5.13 | Derivative as a rate of change; related rates; implicit differentiation | AHL | ⬜ | `Unit_5_13_Related_Rates_and_Implicit.html` |
| 5.14 | Second derivative; concavity; points of inflection; higher derivatives | AHL | ⬜ | `Unit_5_14_Concavity_and_Inflection.html` |
| 5.15 | Integration by substitution; integration by parts | AHL | ⬜ | `Unit_5_15_Advanced_Integration_Techniques.html` |
| 5.16 | Area between a curve and the $y$-axis; volumes of revolution about the $y$-axis; total distance | AHL | ⬜ | `Unit_5_16_y_axis_Integration.html` |
| 5.17 | First-order differential equations: Euler, slope fields, separation of variables, integrating factor, homogeneous DEs | AHL | ⬜ | `Unit_5_17_Differential_Equations.html` |
| 5.18 | Maclaurin series; approximation of functions | AHL | ⬜ | `Unit_5_18_Maclaurin_Series.html` |

---

## Coverage roll-up (as of 2026-05-22)

- **Topic 1**: 16 sub-topics. 7 covered (📁 by A1, A3, A4 — combined units). 9 unbuilt: 1.1, 1.5, 1.6, 1.7, 1.11, 1.15, 1.16.
- **Topic 2**: 16 sub-topics. 0 covered. **16 unbuilt** — entirely greenfield.
- **Topic 3**: 18 sub-topics. 8 covered (📁 by Unit_C monolith). 10 unbuilt: all of AHL 3.9 – 3.18.
- **Topic 4**: 11 sub-topics. **11 covered** ✅ — Topic 4 is fully done (D1, D2, D3 ship 2026-05-22).
- **Topic 5**: 18 sub-topics. 0 covered. **18 unbuilt** — entirely greenfield.

**Total**: 79 sub-topics. **26 covered** (combination of ✅ Topic 4 fully done + 📁 partially covered via legacy combined units). **53 unbuilt sub-topics** to ship for Sprint 3 completion.

## Legacy unit retirement plan

| Legacy unit | Covers sub-topics | Retirement trigger | Disposition |
|---|---|---|---|
| `Unit_A_Number_and_Algebra.html` (archived) | all of 1.1 – 1.16 (legacy monolith) | already archived 2026-05-15 | gone from deploy via `deploy.yml` strip; full deletion when every 1.x split-unit ships |
| `Unit_A1_Sequences_and_Series.html` (shipped) | 1.2, 1.3, 1.4, 1.8 | When `Unit_1_2`, `Unit_1_3`, `Unit_1_4`, `Unit_1_8` all ship | keep with explicit "this unit consolidates 1.2 + 1.3 + 1.4 + 1.8" callout, OR retire to rag/archive/ — user call |
| `Unit_A3_Combinatorics.html` (shipped) | 1.9, 1.10 | When `Unit_1_9`, `Unit_1_10` both ship | same retirement decision pending |
| `Unit_A4_Complex_Numbers.html` (shipped) | 1.12, 1.13, 1.14 | When `Unit_1_12`, `Unit_1_13`, `Unit_1_14` all ship | same retirement decision pending |
| `Unit_C_Geometry.html` (shipped) | 3.1 – 3.8 (the whole SL block) | When all of `Unit_3_1` through `Unit_3_8` ship | same retirement decision pending |
| `Unit_D1_Univariate_Data.html` (shipped) | 4.1, 4.2, 4.3, 4.4 | — | KEEP. Topic-4 split was already at sub-topic-cluster granularity (D1 = SL 4.1-4.4); no further split planned. |
| `Unit_D2_Probability.html` (shipped) | 4.5, 4.6, 4.10 | — | KEEP — same reasoning |
| `Unit_D3_Probability_Distributions.html` (shipped) | 4.7, 4.8, 4.9, 4.11 | — | KEEP — same reasoning |

> **Open architectural question for user.** D1 / D2 / D3 are the
> "right-sized" Topic-4 grouping in the AA HL spec; they group natural
> pedagogical clusters and are well-balanced units of work. The full
> sub-topic-per-unit split being adopted for Topics 1 / 2 / 3 / 5
> creates units that may be much smaller (e.g. sub-topic 5.4 — tangents
> and normals — is a single technique, not a unit's worth of material).
> Three options:
> 1. **Strict sub-topic per unit.** ~79 small focused units. Maximum
>    consumer-mappability. Possibly thin per unit; cram cheat-sheet
>    may equal the whole unit.
> 2. **Topic-cluster per unit** (like D1/D2/D3). ~25-30 medium units.
>    Easier crammer experience; sub-topic mapping done at the
>    section-header level within each cluster unit.
> 3. **Hybrid.** Strict sub-topic per unit for HL extensions (where
>    each sub-topic is genuinely substantial — e.g. 3.16 cross product
>    is its own beast); cluster SL sub-topics that flow together
>    (e.g. 5.1 / 5.2 / 5.3 / 5.4 → one "Intro to Differentiation" unit).
> Flag preference and the spec will be re-cut. Default if unspecified:
> **strict sub-topic per unit** to match the user direction "use the
> official IB sub-topics so the consumer can easily match".

---

## Deliverable contract per unit (Sprint 3)

For each unit ship the following four products, in order:

1. **Study Guide** HTML — dual-goal contract; cram cheat-sheet, sections, worked examples, per-section quizzes, final unit quiz, flashcards (locked terse style), 14-item readiness checklist. Reference template: `Unit_A3_Combinatorics.html`.
2. **Practice Questions** HTML — IB paper-style. EMH mix (Easy / Medium / Hard) distributed across **Paper 1A** (short response, no calc), **Paper 1B** (extended response, no calc), **Paper 2** (calculator), **Paper 3** (HL extended exploration — only for HL-relevant content). Reference template: `Unit_A1_Sequences_and_Series_Practice.html`.
3. **Solutions** HTML — mark-by-mark with M1 / A1 / R1 callouts. Reference template: `Unit_A3_Combinatorics_Solutions.html`.
4. **ZH translation** of all three (English-first per the locked playbook in `prompts/create-bilingual-translation.md`).

Total Sprint 3 deliverable count: 79 × 4 = **316 deliverables** if going strict-sub-topic-per-unit. ~100 deliverables if going Topic-cluster-per-unit. The active sprint tracker lives in `IB Math HL/AUDIT.md`.

---

## Master sprint tracker

Sprint 3 progress is tracked in `IB Math HL/AUDIT.md` under
"### Sprint 3 — Complete the units". That table has one row per
sub-topic with status per deliverable (Study Guide / Practice /
Solutions / ZH-translation). This spec file is the **content
authority** (sub-topic titles, SL/AHL classification, filename
convention). The audit is the **status authority** (what's shipped,
what's open, what's blocked).
