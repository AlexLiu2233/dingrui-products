# University Calculus — Grounding Sources (manifest)

**This folder is the grounding source-of-record for the University Calculus study guides.** It is internal
reference material, stripped from deploy (everything under `rag/` is removed by `.github/workflows/deploy.yml`).
Every study guide must be checkable against a source section listed here; new or revised content should trace to
a committed source. Scope is anchored to the MIT / Georgia Tech / Princeton syllabi; depth, theorem statements,
and standard examples are grounded against the open textbooks and notes.

This matches the repo's existing grounding pattern (see `rag/sources/bc/calc12_extract.md`): curated markdown
extracts plus this manifest, rather than committing large or gated binary PDFs.

## Per-source table

| Source | Type | URL | License / access | Grounds |
|---|---|---|---|---|
| MIT OCW 18.01 Single Variable Calculus | syllabus + notes + psets | https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ | CC BY-NC-SA | Calc I + II (A, B) |
| MIT OCW 18.02 Multivariable Calculus | syllabus + notes + psets | https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/ | CC BY-NC-SA | Calc III (C) |
| MIT OCW 18.03 Differential Equations | syllabus + notes + psets | https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ | CC BY-NC-SA | Calc IV / ODE (D) |
| Georgia Tech MATH 1551/1552/2551/2552 | course syllabi | https://catalog.gatech.edu/coursesaz/math/ | public catalog | A, B, C, D (1:1 by course) |
| Princeton MAT 103/104/201 + ODE | course descriptions | https://www.math.princeton.edu/undergraduate/courses | public catalog | A, B, C (rigor calibration) |
| OpenStax Calculus Vol 1-3 | open textbook | https://openstax.org/details/books/calculus-volume-1 (and -2, -3) | CC BY 4.0 | A, B, C, + intro/2nd-order ODE |
| Strang, Calculus (MIT) | free textbook | https://ocw.mit.edu/resources/res-18-001-calculus-online-textbook-spring-2005/ | free / CC | A, B, C |
| Paul's Online Notes | free notes | https://tutorial.math.lamar.edu/ | free (personal/educational use) | A, B, C, D (best for D) |

Per-source topic extracts live alongside this file:
`MIT_18.01_18.02_18.03_syllabi.md`, `GeorgiaTech_MATH_1551_1552_2551_2552_syllabi.md`,
`Princeton_MAT_calculus_syllabi.md`, `OpenStax_Calculus_Vol1-3_TOC.md`, `Strang_Calculus_TOC.md`,
`Pauls_Online_Notes_topic_index.md`.

## 32-unit grounding map

### Group A — Calculus I (anchor: MIT 18.01, GT 1551, Princeton MAT 103)
| SG | Grounding sections |
|---|---|
| A1 Limits and Continuity | MIT 18.01 Unit 1 (limits/continuity); OpenStax V1 Ch 2 (incl. 2.5 epsilon-delta); Paul's Calc I "Limits"; Strang Ch 2 |
| A2 The Derivative: Definition and Interpretation | MIT 18.01 Unit 1 (def. of derivative); OpenStax V1 Ch 3.1-3.2; Paul's Calc I "Derivatives" (definition); Strang Ch 2 |
| A3 Differentiation Rules (Product, Quotient, Chain) | MIT 18.01 Unit 1; OpenStax V1 Ch 3.3-3.6; Paul's Calc I "Derivatives" (formulas, chain rule); Strang Ch 4 |
| A4 Derivatives of Transcendental Functions | MIT 18.01 Unit 1; OpenStax V1 Ch 3.9 + inverse/log/exp; Paul's Calc I (trig, exp/log, inverse trig); Strang Ch 4, 6 |
| A5 Implicit Differentiation and Related Rates | MIT 18.01 Unit 1-2; OpenStax V1 Ch 3.8 + 4.1; Paul's Calc I (implicit diff, related rates); Strang Ch 4 |
| A6 Linear Approximation, Differentials, L'Hopital | MIT 18.01 Unit 2; OpenStax V1 Ch 4.2 + 4.8; Paul's Calc I (linear approx, differentials, L'Hospital); Strang Ch 3 |
| A7 Curve Sketching and Optimization | MIT 18.01 Unit 2; OpenStax V1 Ch 4.3-4.7; Paul's Calc I "Applications of Derivatives"; Strang Ch 3 |
| A8 Antiderivatives and the Definite Integral | MIT 18.01 Unit 3; OpenStax V1 Ch 4.10 + 5.1-5.3 (Riemann, FTC); Paul's Calc I "Integrals"; Strang Ch 5 |

### Group B — Calculus II (anchor: MIT 18.01, GT 1552, Princeton MAT 104)
| SG | Grounding sections |
|---|---|
| B1 Integration Techniques I (Substitution, Parts) | MIT 18.01 Unit 4; OpenStax V1 Ch 5.5 + V2 Ch 3.1; Paul's Calc II "Integration Techniques" (parts); Strang Ch 7 |
| B2 Integration Techniques II (Trig, Partial Fractions) | MIT 18.01 Unit 4; OpenStax V2 Ch 3.2-3.4; Paul's Calc II (trig integrals/sub, partial fractions); Strang Ch 7 |
| B3 Improper Integrals and Numerical Integration | MIT 18.01 Unit 4; OpenStax V2 Ch 3.6-3.7; Paul's Calc II (improper, approximating integrals); Strang Ch 5, 7 |
| B4 Applications: Area, Volume, Arc Length | MIT 18.01 Unit 3; OpenStax V1 Ch 6.1-6.4; Paul's Calc II "Applications of Integrals" + Calc I (volumes); Strang Ch 8 |
| B5 Further Applications: Work, Center of Mass, Probability | MIT 18.01 Unit 3; OpenStax V1 Ch 6.5-6.7; Paul's Calc II (work, center of mass, probability); Strang Ch 8 |
| B6 Sequences and Infinite Series | MIT 18.01 Unit 5; OpenStax V2 Ch 5; Paul's Calc II "Series and Sequences" (convergence tests); Strang Ch 10 |
| B7 Power Series, Taylor and Maclaurin Series | MIT 18.01 Unit 5; OpenStax V2 Ch 6; Paul's Calc II (power series, Taylor); Strang Ch 10 |
| B8 Parametric Equations and Polar Coordinates | OpenStax V2 Ch 7; Paul's Calc II "Parametric and Polar"; Strang Ch 9 |

### Group C — Calculus III (anchor: MIT 18.02, GT 2551, Princeton MAT 201)
| SG | Grounding sections |
|---|---|
| C1 Vectors and the Geometry of Space | MIT 18.02 Unit 1; OpenStax V3 Ch 2; Paul's Calc III "3D Space" (vectors, lines, planes); Strang Ch 11 |
| C2 Vector-Valued Functions and Curves | MIT 18.02 Unit 1; OpenStax V3 Ch 3; Paul's Calc III (vector functions, curvature, motion); Strang Ch 12 |
| C3 Partial Derivatives and the Gradient | MIT 18.02 Unit 2; OpenStax V3 Ch 4.1-4.6; Paul's Calc III "Partial Derivatives"; Strang Ch 13 |
| C4 Directional Derivatives, Tangent Planes, Linearization | MIT 18.02 Unit 2; OpenStax V3 Ch 4.4-4.6; Paul's Calc III (tangent planes, gradient); Strang Ch 13 |
| C5 Optimization and Lagrange Multipliers | MIT 18.02 Unit 2; OpenStax V3 Ch 4.7-4.8; Paul's Calc III "Applications of Partial Derivatives"; Strang Ch 13 |
| C6 Multiple Integrals | MIT 18.02 Unit 3-4; OpenStax V3 Ch 5; Paul's Calc III "Multiple Integrals" (polar/cyl/spherical); Strang Ch 14 |
| C7 Vector Fields, Line Integrals, Green's Theorem | MIT 18.02 Unit 3; OpenStax V3 Ch 6.1-6.4; Paul's Calc III "Line Integrals"; Strang Ch 15 |
| C8 Surface Integrals, Stokes', Divergence | MIT 18.02 Unit 4; OpenStax V3 Ch 6.5-6.8; Paul's Calc III "Surface Integrals"; Strang Ch 15 |

### Group D — Calculus IV / ODE (anchor: MIT 18.03, GT 2552; Paul's = primary method ground)
| SG | Grounding sections |
|---|---|
| D1 First-Order ODEs (Separable, Linear) | MIT 18.03 Unit 1; OpenStax V2 Ch 4.3-4.5; Paul's DE "First Order" (linear, separable); GT 2552 |
| D2 First-Order Models and Exact Equations | MIT 18.03 Unit 1; Paul's DE "First Order" (exact, Bernoulli, modeling, equilibrium); GT 2552 |
| D3 Second-Order Linear ODEs: Homogeneous | MIT 18.03 Unit 2; OpenStax V3 Ch 7.1; Paul's DE "Second Order" (real/complex/repeated roots); GT 2552 |
| D4 Nonhomogeneous Second-Order ODEs | MIT 18.03 Unit 2; OpenStax V3 Ch 7.2-7.3; Paul's DE (undetermined coefficients, variation of parameters); GT 2552 |
| D5 Mechanical and Electrical Vibrations | MIT 18.03 Unit 2 (oscillators, resonance, RLC); OpenStax V3 Ch 7.4; Paul's DE "Mechanical Vibrations"; GT 2552 |
| D6 The Laplace Transform | MIT 18.03 Unit 3; Paul's DE "Laplace Transforms" (IVPs, step, delta, convolution); GT 2552 |
| D7 Systems of First-Order Linear ODEs | MIT 18.03 Unit 4; Paul's DE "Systems of DE" (eigenvalue method, phase plane); GT 2552 |
| D8 Series Solutions and Numerical Methods | MIT 18.03 (supplementary); OpenStax V3 Ch 7.5; Paul's DE "Series Solutions" + Euler's method; GT 2552 |

## Retrieval notes / gaps to fill later

- **Binary PDFs not committed.** Direct PDF downloads for OpenStax (S3-gated, returns AccessDenied) and the Strang
  OCW PDF (redirect loop) were not retrievable in this environment, so they are referenced by URL above rather than
  stored as files. If a future pass wants the raw PDFs in-repo, download them in a browser-equivalent context and
  drop them here; the manifest mapping already names the relevant chapters.
- **Princeton ODE** has no single canonical course; group D is anchored to MIT 18.03 + GT MATH 2552 instead (noted
  in `Princeton_MAT_calculus_syllabi.md`).
- The per-course extract files capture the actual topic/section lists; if a specific target-school term syllabus is
  desired (e.g. a particular MIT 18.02 offering), add it here as a dated extract.
