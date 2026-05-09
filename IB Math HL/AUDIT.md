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

Last reviewed: **2026-05-09** (Sprint 1 active: Unit A refactor in flight,
A1 + A3 shipped).

---

## Active Sprint — what we're working on now

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
| **S1-4** | Draft `Unit_A4_Complex_Numbers.html` (Topic 1.12–1.14) | P0 | **Open** — Cartesian, polar, Euler forms, De Moivre, roots, conjugate root theorem. HL-heavy. |
| **S1-5** | Draft `Unit_A5_Proof.html` (Topic 1.6, 1.15) | P0 | **Open** — direct proof, induction, contradiction. Cross-link from A1 induction-of-sums. |
| **S1-6** | Draft `Unit_A6_Algebra_and_Systems.html` (Topic 1.11 + linear systems) | P0 | **Open** — partial fractions, $3\times 3$ systems, RREF. |
| **S1-7** | Remove old `Unit_A_Number_and_Algebra.html` + update `index.html` cards | P1 | **Open** — bundle once S1-6 ships. |

Build order: **A1 (✓) → A3 (✓) → A2 → A4 → A5 → A6 → cleanup**. (A3 jumped
ahead of A2 on user request 2026-05-09.)

### Sprint 2 (queued) — new topic units
Once Sprint 1 closes, Sprint 2 picks up the missing units (B Functions,
D Statistics &amp; Probability, E Calculus). Build order: **B → D → E**.
Original P0 work; preserved here so it isn't lost.

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
