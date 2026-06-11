# Subject Spec — University Calculus

## Identity

- **Display (section heading):** University Calculus
- **Display (hero chip):** University Calculus
- **Directory:** `University Calculus/`
- **Audit:** `University Calculus/AUDIT.md`
- **Tier:** first-year university (the top tier of the HS to AP/IB to first-year-uni pipeline). New as of 2026-06-09.

## Who this is for

Current NA undergraduates (MIT / Georgia Tech / Princeton tier) in their first or second year, working through the standard calculus sequence and looking for help. Lead-gen goal: capture high-intent search traffic ("Calc 2 series convergence help", "18.02 Lagrange multipliers", "ODE undetermined coefficients") and route it to the consult CTA. SEO long-tail is the primary acquisition channel for this tier, since nothing feeds it from above. The guides also serve as a self-study and teaching reference (the mastery half of the dual-goal contract).

## Official curriculum reference

Scope is anchored to what NA top-10 schools actually teach, captured in the grounding folder `rag/sources/University Calculus/` (manifest: `rag/sources/University Calculus/SOURCES.md`):

- **MIT** 18.01 (Single Variable Calculus), 18.02 (Multivariable Calculus), 18.03 (Differential Equations).
- **Georgia Tech** MATH 1551 (Differential Calculus), 1552 (Integral Calculus), 2551 (Multivariable Calculus), 2552 (Differential Equations).
- **Princeton** MAT 103 (Calculus I), 104 (Calculus II), 201 (Multivariable Calculus), and the ODE course.

Content depth, theorem statements, and standard examples are grounded against the open sources in the same folder (MIT OCW notes, OpenStax Calculus Vol 1-3, Strang *Calculus*, Paul's Online Notes). Every Study Guide must be checkable against a committed source in that folder. **Rigor target is genuine university level** (epsilon-delta limits done properly, real proofs), not AP-level intuition, which is what differentiates this subject from `AP Calculus`.

## Structure: four course-groups

One subject, four course-groups A/B/C/D corresponding to the four-course university sequence, 8 Study Guides each (32 total). The groups render as four collapsible accordions on the landing page via `build-index.py`'s `GROUP_BY_LETTER` map.

| Group | Course | Standard equivalent |
|---|---|---|
| **A** | Calculus I — Single-Variable Differential Calculus | MIT 18.01 (first half), GT 1551, Princeton MAT 103 |
| **B** | Calculus II — Single-Variable Integral Calculus & Series | MIT 18.01 (second half), GT 1552, Princeton MAT 104 |
| **C** | Calculus III — Multivariable & Vector Calculus | MIT 18.02, GT 2551, Princeton MAT 201 |
| **D** | Calculus IV — Ordinary Differential Equations | MIT 18.03, GT 2552 |

## Naming convention

```
University Calculus/Study Guides/Unit_{ID}_Topic_Name.html
University Calculus/Practice Questions/Unit_{ID}_Topic_Name_Practice_Problems.html
University Calculus/Practice Questions/Solutions/Unit_{ID}_Topic_Name_Solutions.html
```

`{ID}` is the group letter + index: `A1`..`A8`, `B1`..`B8`, `C1`..`C8`, `D1`..`D8`. Topic name uses underscores; avoid commas and ampersands in filenames (rephrase instead).

## Required `<title>` format

```
University Calculus — Unit {ID}: {Topic} | Dingrui Scholars
```

`build-index.py` parses this verbatim (it expects the `Unit {ID}` prefix; the "Calculus I/II/III/IV" course label is supplied by the `GROUP_BY_LETTER` map, NOT the title). Drift here surfaces as a parse warning. Examples:

- `University Calculus — Unit A1: Limits and Continuity | Dingrui Scholars`
- `University Calculus — Unit C5: Optimization and Lagrange Multipliers | Dingrui Scholars`
- `University Calculus — Unit D6: The Laplace Transform | Dingrui Scholars`

## Unit list (Study Guide product) — 32 units

### Group A — Calculus I (Single-Variable Differential Calculus)
| ID | Topic |
|---|---|
| A1 | Limits and Continuity |
| A2 | The Derivative: Definition and Interpretation |
| A3 | Differentiation Rules (Product, Quotient, Chain) |
| A4 | Derivatives of Transcendental Functions |
| A5 | Implicit Differentiation and Related Rates |
| A6 | Linear Approximation, Differentials, and L'Hopital's Rule |
| A7 | Curve Sketching and Optimization |
| A8 | Antiderivatives and the Definite Integral |

### Group B — Calculus II (Single-Variable Integral Calculus & Series)
| ID | Topic |
|---|---|
| B1 | Integration Techniques I: Substitution and Integration by Parts |
| B2 | Integration Techniques II: Trig Integrals, Trig Substitution, Partial Fractions |
| B3 | Improper Integrals and Numerical Integration |
| B4 | Applications of Integration: Area, Volume, Arc Length |
| B5 | Further Applications: Work, Center of Mass, Probability |
| B6 | Sequences and Infinite Series |
| B7 | Power Series, Taylor and Maclaurin Series |
| B8 | Parametric Equations and Polar Coordinates |

### Group C — Calculus III (Multivariable & Vector Calculus)
| ID | Topic |
|---|---|
| C1 | Vectors and the Geometry of Space |
| C2 | Vector-Valued Functions and Curves |
| C3 | Partial Derivatives and the Gradient |
| C4 | Directional Derivatives, Tangent Planes, and Linearization |
| C5 | Optimization and Lagrange Multipliers |
| C6 | Multiple Integrals |
| C7 | Vector Fields, Line Integrals, and Green's Theorem |
| C8 | Surface Integrals, Stokes' Theorem, and the Divergence Theorem |

### Group D — Calculus IV (Ordinary Differential Equations)
| ID | Topic |
|---|---|
| D1 | First-Order ODEs: Separable and Linear Equations |
| D2 | First-Order Models and Exact Equations |
| D3 | Second-Order Linear ODEs: Homogeneous |
| D4 | Nonhomogeneous Second-Order ODEs |
| D5 | Mechanical and Electrical Vibrations |
| D6 | The Laplace Transform |
| D7 | Systems of First-Order Linear ODEs |
| D8 | Series Solutions and Numerical Methods |

## Assessment framing

Universities vary (midterms, finals, problem sets), so there is no single national exam to anchor to. The dual-goal contract is phrased for this tier as:

- **The struggling student** opening the guide before a midterm. Target: pass the midterm. They lift the cheat-sheet boxes and worked examples.
- **The mastery reader** studying for depth, an A, or to teach it. Target: full command of derivations, proofs, and edge cases.

## Conventions / special flags

- **English-first.** New units ship English-only (no `data-lang` span pairs, no language-toggle button), matching how `AP Calculus` shipped before its bilingual commit. The Mandarin teaching translation is a later wave (`prompts/create-bilingual-translation.md`) that wraps the English in spans, adds the paired Mandarin, and re-introduces the toggle infrastructure.
- **Prose + KaTeX only.** No figures, charts, or interactive widgets (the repo-wide visuals policy). The reveal-on-click quiz, flashcard flip, and theme toggle are the only scripted behaviors.
- **No HL/SL split.** University Calculus has a single rigor tier (genuine university level). The group letter encodes the course, not a difficulty stream.
- **CTA copy** is pitched at the struggling-undergrad audience ("1:1 help before your midterm"), still routing to `dingruischolars.com/signup`. UTM `utm_campaign=university_calculus`.

## Cross-references

- **Status authority** (what is shipped, what is open): `University Calculus/AUDIT.md`.
- **Grounding authority** (scope per course, theorem coverage, source mapping): `rag/sources/University Calculus/SOURCES.md`.
- **Generation contract** (dual-goal layering, section schema): `prompts/create-unit.md`.
