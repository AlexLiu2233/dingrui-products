# AP Physics C: Mechanics — Study Guides

Polished, AP-CED-aligned single-page study guides for Units 1–7 of AP Physics C:
Mechanics. Each unit is a self-contained `.html` file with KaTeX math, dark mode,
canvas + JSXGraph interactive widgets, flashcards, an exam-strategy section, and
ISEE worked examples.

The set is built so a student can rely on the study guide for both:

- **Last-minute cram** — flashcards, formula tables, must-know callouts, and
  common-mistakes boxes are surfaced; key equations are scannable.
- **Shooting for a 5** — every CED-required derivation is worked out (kinematic
  equations from calculus, Newton's-second-law applications on inclines and with
  drag, work-energy theorem, impulse-momentum, parallel-axis theorem, rolling
  without slipping, SHM from $F = -kx$, damped/driven extensions) and every
  interactive widget mirrors a canonical AP scenario.

Practice question sets for these units live in [`../Practice Questions/`](../Practice%20Questions/).

The master generation specification (head template, design tokens, component
library, JS architecture) is in [`../GENERATION_PROMPT.md`](../GENERATION_PROMPT.md).

---

## Index

| Unit | Title | Scope | Sections | Widgets | File |
|---|---|---|---|---|---|
| 1 | Kinematics | Topics 1.1 – 1.5 | 5 | 2 canvas | [Unit_1_Kinematics.html](Unit_1_Kinematics.html) |
| 2 | Force & Translational Dynamics | Topics 2.1 – 2.10 | 10 | 5 canvas | [Unit_2_Force_and_Dynamics.html](Unit_2_Force_and_Dynamics.html) |
| 3 | Work, Energy, & Power | Topics 3.1 – 3.5 | 5 | 3 canvas | [Unit_3_Work_Energy_Power.html](Unit_3_Work_Energy_Power.html) |
| 4 | Linear Momentum | Topics 4.1 – 4.4 | 4 | 3 canvas | [Unit_4_Linear_Momentum.html](Unit_4_Linear_Momentum.html) |
| 5 | Torque & Rotational Dynamics | Topics 5.1 – 5.6 | 6 | 4 canvas + JSXGraph | [Unit_5_Torque_and_Rotational_Dynamics.html](Unit_5_Torque_and_Rotational_Dynamics.html) |
| 6 | Energy & Momentum of Rotating Systems | Topics 6.1 – 6.6 | 6 | 4 canvas + JSXGraph | [Unit_6_Energy_and_Momentum_of_Rotating_Systems.html](Unit_6_Energy_and_Momentum_of_Rotating_Systems.html) |
| 7 | Oscillations | Topics 7.1 – 7.5 | 5 | 1 canvas + phase-space + JSXGraph | [Unit_7_Oscillations.html](Unit_7_Oscillations.html) |

> **Coverage:** 41 topics across the seven units, mapping 1:1 to the College
> Board CED for AP Physics C: Mechanics. Exam weight ≈ 100% (Mechanics-only
> exam).

---

## Per-Unit Highlights

### Unit 1 — Kinematics
Position/velocity/acceleration as derivative-integral pairs, the constant-$a$
equations derived from calculus, free fall, and 2-D projectile motion. Two
canvas explorers: a stroboscopic 1-D track for free-fall and a launch-angle
projectile widget. AP weight ≈ 10–15%.

### Unit 2 — Force & Translational Dynamics
Newton's three laws, free-body diagrams, kinetic vs. static friction, linear
and quadratic drag (with terminal velocity disambiguated), inclined planes,
spring forces, and uniform circular motion. Five canvas explorers cover $F=ma$,
inclines, springs, drag, and centripetal motion. AP weight ≈ 20–25%.

### Unit 3 — Work, Energy, & Power
Work as a path integral $W = \int \vec F \cdot d\vec r$, kinetic and
gravitational/elastic potential energy, conservative forces and $F = -dU/dx$,
and instantaneous power. Three canvas explorers (work, $U(x)$ landscape,
spring oscillator). AP weight ≈ 15–25%.

### Unit 4 — Linear Momentum
Impulse-momentum theorem, conservation in elastic and inelastic collisions,
center-of-mass motion, and the link to energy conservation. Three canvas
explorers covering impulse, 1-D collision outcomes, and energy/momentum
trade-offs. AP weight ≈ 10–20%.

### Unit 5 — Torque & Rotational Dynamics
Angular kinematics, moment of inertia, parallel-axis theorem, $\tau = I\alpha$,
and rolling without slipping. Four widgets including a JSXGraph-driven rolling
animation. Includes ISEE-style FRQ worked examples. AP weight ≈ 10–15%.

### Unit 6 — Energy & Momentum of Rotating Systems
Rotational work-energy theorem, angular momentum conservation, rolling energy
partition, and orbital mechanics (Kepler's laws, escape velocity). Four
widgets. ISEE worked examples. AP weight ≈ 10–15%.

### Unit 7 — Oscillations
SHM from Hooke's law, energy in SHM, the simple and physical pendulum, damped
oscillation regimes (underdamped/critical/overdamped), and driven resonance.
The signature widget shows position/phase-space simultaneously with damping
controls. ISEE worked examples. AP weight ≈ 10–15%.

---

## Conventions

- **File naming:** `Unit_{N}_{Title_With_Underscores}.html`
- **Self-contained:** All CSS and JavaScript inline; only external deps are
  Google Fonts, KaTeX (CDN), and JSXGraph (CDN, Units 5–7).
- **Design system:** maroon `#7A2E2E` accent, DM Serif Display headings,
  Source Sans 3 body, JetBrains Mono code. See
  [`../GENERATION_PROMPT.md`](../GENERATION_PROMPT.md) §5.
- **Validation:** `bash scripts/validate.sh "AP Physics/Study Guides/Unit_N_*.html"`

---

## Status

See [`../AUDIT.md`](../AUDIT.md) for the open punch list (P0/P1 items) tracking
parity gaps between units and against the master generation spec.
