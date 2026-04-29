# AP Calculus AB & BC — Study Guides

Polished, AP-CED-aligned single-page study guides for Units 1–10 of AP Calculus.
Each unit is a self-contained `.html` file with KaTeX math, dark mode, interactive
widgets, flashcards, an exam-strategy section, and a readiness checklist.

The set is built so a student can rely on the study guide for both:

- **Last-minute cram** — flashcards, formula tables, must-know callouts, common-mistakes
  boxes are surfaced; key formulas are scannable.
- **Shooting for a 5** — every CED-required derivation is worked out (squeeze theorem,
  inverse derivatives, FTC chain rule, arc-length, logistic inflection, etc.) and
  every BC-only topic is clearly tagged.

Each unit's practice questions live in [`../Practice Questions/`](../Practice%20Questions/).

---

## Index

| Unit | Title | Scope | File |
|---|---|---|---|
| 1 | Limits & Continuity | AB & BC · Topics 1.1 – 1.16 | [Unit_1_Limits_and_Continuity.html](Unit_1_Limits_and_Continuity.html) |
| 2 | Differentiation: Definition & Fundamental Properties | AB & BC · Topics 2.1 – 2.10 | [Unit_2_Differentiation_Definition_Fundamental_Properties.html](Unit_2_Differentiation_Definition_Fundamental_Properties.html) |
| 3 | Composite, Implicit, & Inverse Functions | AB & BC · Topics 3.1 – 3.6 | [Unit_3_Composite__Implicit____Inverse_Functions.html](Unit_3_Composite__Implicit____Inverse_Functions.html) |
| 4 | Contextual Applications of Differentiation | AB & BC · Topics 4.1 – 4.7 | [Unit_4_Contextual_Applications_of_Differentiation.html](Unit_4_Contextual_Applications_of_Differentiation.html) |
| 5 | Analytical Applications of Differentiation | AB & BC · Topics 5.1 – 5.12 | [Unit_5_Analytical_Applications_of_Differentiation.html](Unit_5_Analytical_Applications_of_Differentiation.html) |
| 6 | Integration & Accumulation of Change | AB & BC · Topics 6.1 – 6.14 (BC: 6.11–6.13) | [Unit_6_Integration_Accumulation.html](Unit_6_Integration_Accumulation.html) |
| 7 | Differential Equations | AB & BC · Topics 7.1 – 7.9 (BC: 7.5, 7.9) | [Unit 7 Differential Equations.html](Unit%207%20Differential%20Equations.html) |
| 8 | Applications of Integration | AB & BC · Topics 8.1 – 8.13 (BC: 8.13) | [Unit 8 Applications of Integration.html](Unit%208%20Applications%20of%20Integration.html) |
| 9 | Parametric, Polar, and Vector-Valued Functions | BC · Topics 9.1 – 9.9 | [Unit 9 Parametric Polar and Vectors.html](Unit%209%20Parametric%20Polar%20and%20Vectors.html) |
| 10 | Infinite Sequences & Series | BC · Topics 10.1 – 10.15 | [Unit 10 Sequences and Series.html](Unit%2010%20Sequences%20and%20Series.html) |

---

## Per-Unit Highlights

### Unit 1 — Limits & Continuity
The 16/16 CED topics in one place: graphical and numerical limit estimation,
algebraic technique selection (factoring, rationalizing, trig identities), the
Squeeze Theorem with worked example, three-condition continuity, classification
of discontinuities, infinite limits and limits at infinity (including radical
end-behavior), and the Intermediate Value Theorem with a justification checklist.
Eight flashcards and a readiness checklist anchor the cram path.

### Unit 2 — Differentiation: Definition & Fundamental Properties
Limit-definition derivative (with disguised-form recognition), differentiability
vs. continuity (corner / cusp / vertical tangent / discontinuity), and all the
basic rules (power, sum, product, quotient, $e^x$, $\ln x$, sin/cos/tan/cot/sec/csc).
Includes full proofs of $\frac{d}{dx}[\sin x] = \cos x$ via the Squeeze Theorem
and $\frac{d}{dx}[a^x] = a^x \ln a$ via $a^x = e^{x\ln a}$.

### Unit 3 — Composite, Implicit, & Inverse Functions
Chain rule with decomposition table, implicit differentiation 4-step procedure,
inverse-function derivative formula with full algebraic derivation from
$f(f^{-1}(x)) = x$, and inverse-trig derivatives with implicit-diff derivations
for arcsin and arccos (including principal-range branch selection). Domain column
on the inverse-trig reference table. Higher-order derivatives covered as Topic 3.6.

### Unit 4 — Contextual Applications of Differentiation
Derivative-as-rate interpretation in context, motion (position / velocity /
acceleration with the speeding-up rule), related rates with a 5-step template,
linearization with concavity-based over/underestimate analysis, and L'Hôpital's
Rule on the indeterminate forms $\frac{0}{0}$ and $\frac{\infty}{\infty}$,
including a worked $0\cdot\infty \to \frac{0}{0}$ rewrite ($x \ln x$).

### Unit 5 — Analytical Applications of Differentiation
The "12 topics in one document" classics: MVT and EVT with hypothesis-checking,
critical points, First and Second Derivative Tests, concavity and inflection
(including the $f''(c) = 0$ counterexample $f(x) = x^4$), curve sketching,
optimization, and contextual related rates. Interactive widgets visualize the
$f$ ↔ $f'$ relationship.

### Unit 6 — Integration & Accumulation of Change
Riemann sums (with the over/under table by monotonicity × concavity), the
Fundamental Theorem in both forms, accumulation functions $g(x) = \int_a^x f(t)\,dt$,
properties of definite integrals, $u$-substitution 5-step template, and the FTC1
chain rule on **both** the upper limit and the lower limit (sign-flip variant).
BC topics covered with full rigor: integration by parts (LIATE), linear partial
fractions (with proper-rational long-division caveat), and improper integrals —
both infinite limits **and** interior discontinuities (the $\int_0^2 (x-1)^{-1/3}\,dx$
worked example splits at $x=1$).

### Unit 7 — Differential Equations
Modeling, slope fields, separation of variables (4-step template), exponential
growth, branch-selection on $y = \pm\sqrt{\cdots}$ via the initial condition, and
domain-of-validity ("largest open interval"). BC topics get full treatment:
Euler's method with the **concavity → over/underestimate bias** rule and worked
example, plus a derivation of $d^2y/dt^2$ for the logistic that shows the inflection
point lives at $y = a/2$ via sign analysis.

### Unit 8 — Applications of Integration
Average value, motion (with a $v(t)$ sign-changing worked example covering
displacement vs. total distance), accumulation in applied contexts (tank filling
with rate $R(t)$), area between curves (functions of $x$ and $y$), and a
multi-intersection worked example $\int_{-1}^{1} |x^3 - x|\,dx$ with sign-chart
and symmetry shortcut. The **Volume Methods Roadmap** (between Topics 8.6 and
8.7) is a 4-step decision tree (cross-section vs. disc vs. washer; standard vs.
shifted axis; $dx$ vs. $dy$; identifying the radius) plus a same-region-three-axes
comparison table. Disc and washer are each illustrated with worked examples for
both standard and shifted axes. BC arc-length includes a 5-step MVT-based
derivation of $L = \int_a^b \sqrt{1+[f'(x)]^2}\,dx$ from the polygonal Riemann-sum
approximation.

### Unit 9 — Parametric, Polar, and Vector-Valued Functions  *(BC)*
Derivatives of parametric curves $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ with
tangent-line analysis, second derivatives via the correct chain-rule sandwich,
arc length for parametric and polar curves, vector-valued functions (velocity,
acceleration, speed), and area in polar coordinates.

### Unit 10 — Infinite Sequences & Series  *(BC)*
Sequences vs. series, geometric series, $n$th-Term Test, $p$-series, integral
test, comparison and limit comparison, ratio and alternating-series tests,
absolute vs. conditional convergence, alternating-series error bound, power
series (radius and interval of convergence), Taylor and Maclaurin series,
Lagrange error bound, and the standard Maclaurin reference table for $e^x$,
$\sin x$, $\cos x$, and $\frac{1}{1-x}$.

---

## Conventions & Tags

- **BC-only** topics carry a purple `BC` tag in section headers, navigation, and
  flashcards. AB students can skip them; BC students should treat them as
  required.
- **Practice cross-references**: a "Practice Q*N*" callout means the indicated
  practice file question is teachable directly from the SG content above it.
- **Derivations** live in collapsible `<details>` blocks so cram-track readers
  can skip them and 5-tier readers can expand them.
- **Common-mistake** callouts are red. **Best-habit / sanity-check** callouts
  are green. **Caveats / domain notes** are orange. **BC-only** is purple.
- The **30-second sketch routine** in Unit 8 is the canonical "before you
  integrate, draw" pattern.

## Building / Local Development

Each `.html` file is fully self-contained — no build step, no bundler. External
dependencies are limited to:

- Google Fonts (DM Serif Display, Source Sans 3, JetBrains Mono)
- KaTeX 0.16.9 from jsDelivr (math rendering)

Open any file in a modern browser. Dark mode toggles via the theme button in the
top nav. Print stylesheets are tuned for letter-size paper.
