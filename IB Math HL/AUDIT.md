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

Last reviewed: **2026-05-21** (`improve_study_guides` audit checkpoint —
Sprint 2 opened with worked-examples / exam-tips / sliders focus per
the user-locked 3-vector improvement direction).

---

## Active Sprint — what we're working on now

### Sprint 2 — Worked examples / exam tips / sliders (opened 2026-05-21)

Audit-driven sprint per the user-locked 3-vector improvement focus
(see `rag/study-guide-audit-checklist.md` Section E). **English-first**:
each item lands as an English revision commit, user reviews, then the
Mandarin follow-up commit picks up the same file per
`prompts/create-bilingual-translation.md`.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-1** | **Unit C** `Unit_C_Geometry.html`: surface worked examples — unwrap `<details><summary>Worked Example — …</summary>` blocks so they're visible by default (sibling parity with A1/A3/A4). Reserve `<details>` for "Going deeper" proofs only. (E1 / B2) | P0 | **Open** |
| **S2-2** | **Unit C**: add worked example + quiz to crammer-only topic sections — C1.3 Radian Measure, C2.1 SOHCAHTOA, C2.3 Bearings, C2.4 Unit Circle, C2.10 Symmetry. Add quiz to C2.6 Reciprocal/Inverse and C3.3 Vector Eqn of Line. (E1 / B2) | P1 | **Open** |
| **S2-3** | All 4 units: per-major-topic exam-tip callout (E2). A1/A3/A4 have some "AP-style" strategy callouts — extend to every topic with concrete IB-paper guidance (Paper 1 calc vs Paper 2, HL-only flagging, command-term hints, "what graders look for"). Unit C has none. | P1 | **Open** |
| **S2-4** | **Unit C**: page-fill / column-parity audit (A14). Unit C predates the A1/A3/A4 layout pattern; verify `.main-wrap` / `--max-w` / sidebar mode match siblings. | P2 | **Open** |
| **S2-5** | Slider widget candidates (E3): IB Math HL currently has zero widgets. High-leverage one-slider-one-concept: GP convergence ratio slider (A1.6), Pascal-triangle row slider (A3.5), Argand diagram angle slider (A4 polar form), arc-length on unit circle (C2.4). Each = single slider, one observable. | P2 | **Open** |

**Deferred to bilingual follow-up** (per English-first gate locked
2026-05-21):

- Theme persistence via `localStorage` (A5 — all 4 files).
- HL-flagging migration to inline chips on Unit C (C2 — currently uses
  text suffix; siblings use `<span class="hl-flag">HL</span>`).
- `#how-to-use` section addition for Unit C.
- Unit C flashcard density boost (12 → ~16).
- Unit A3.5 add labelled worked-solution block.

### Closed (Translation Sprint — closed 2026-05-21)

All currently-shipped IB Math HL study guides (A1, A3, A4, C)
bilingualized EN↔ZH. Branch `ib_math_hl_translation` fast-forwarded
to `main`.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**T-1**~~ | Unit A1 Sequences &amp; Series bilingual translation | P1 | ✅ closed — `cdca220` |
| ~~**T-2**~~ | Unit A3 Combinatorics bilingual translation | P1 | ✅ closed — `ea3124d` |
| ~~**T-3**~~ | Unit A4 Complex Numbers bilingual translation | P1 | ✅ closed — `12dc6ad` (+ Argand-gloss polish in follow-up) |
| ~~**T-4**~~ | Unit C Geometry bilingual translation | P1 | ✅ closed — `ebf8d11` |

**Audience contract** — Mandarin-Chinese-language students preparing to
write the IB Math AA HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terminology (sequence / series /
binomial theorem / De Moivre / Argand / modulus / argument / etc.) stays
in `<code>` inline. Math notation untouched. A2 / A5 / A6 will be
translated as they ship (separate Translation Sprint Wave 2 entry to be
opened when those files land).

**Backlog candidates beyond this sprint:** Sprint 1 (Unit A refactor —
A2, A5, A6 study guides) and Sprint 2 (Units B / D / E).

### Sprint 1 — Refactor Unit A into focused sub-units (paused for translation)

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
| ~~**S1-4**~~ | Draft `Unit_A4_Complex_Numbers.html` (Topic 1.12–1.14) | P0 | ✅ **Shipped 2026-05-15** — 6 sections (Cartesian form, Argand &amp; polar form, Euler form &amp; multiplication, De Moivre, roots &amp; roots of unity, polynomials over ℂ). 6 inline quizzes + 10-item practice quiz, 14 flashcards, 14-item readiness checklist. Includes inductive proof of De Moivre, derivation of multiple-angle identities, and proof of the conjugate root theorem. Introduces `argand-figure` SVG component (Argand-diagram inline graphics for $z = a + bi$, multiplication-as-rotation, and the 5th roots of unity). |
| **S1-5** | Draft `Unit_A5_Proof.html` (Topic 1.6, 1.15) | P0 | **Open** — direct proof, induction, contradiction. Cross-link from A1 induction-of-sums. |
| **S1-6** | Draft `Unit_A6_Algebra_and_Systems.html` (Topic 1.11 + linear systems) | P0 | **Open** — partial fractions, $3\times 3$ systems, RREF. |
| **S1-7** | Remove old `Unit_A_Number_and_Algebra.html` + update `index.html` cards | P1 | 🟡 **Partial 2026-05-15** — file moved to `rag/archive/Unit_A_Number_and_Algebra.html` (stripped from deploy by `deploy.yml`); Unit A card dropped from `index.html`. Full deletion of the archived copy pending A2/A5/A6 ship (content needs to land in sub-units before the reference copy can be discarded). |

Build order: **A1 (✓) → A3 (✓) → A4 (✓) → A2 → A5 → A6 → cleanup**. (A3
jumped ahead of A2 on user request 2026-05-09; A4 jumped ahead of A2 on
user request 2026-05-14.)

### Practice Questions sub-stream

Parallel build-out of IB-style practice files in `Practice Questions/`,
mirroring the AP Physics pattern but adapted for IB paper structure
(Paper 1A short / Paper 1B extended / Paper 2 calc / Paper 3 HL). Each
question carries difficulty (Easy/Medium/Hard), paper, syllabus topic,
and mark allocation pills. Question-only — no embedded answers.

| ID | Item | Status |
|---|---|---|
| ~~**SQ-1**~~ | `Practice Questions/README.md` + locked conventions | ✅ Shipped 2026-05-09 |
| ~~**SQ-2**~~ | `Unit_A1_Sequences_and_Series_Practice.html` (11 Qs, 67 marks total) | ✅ Shipped 2026-05-09 |
| ~~**SQ-3**~~ | `Unit_A3_Combinatorics_Practice.html` (11 Qs, 61 marks total) | ✅ Shipped 2026-05-09 |
| **SQ-4** | Practice files for A2 / A4 / A5 / A6 / B / D / E (one per study guide as those land) | **Open** — track per study-guide ship |

### Sprint 2 (queued) — new topic units
Once Sprint 1 closes, Sprint 2 picks up the missing units (B Functions,
D Statistics &amp; Probability, E Calculus). Build order: **B → D → E**.
Original P0 work; preserved here so it isn't lost.

---

## Translation audit (per-file, post-ship)

**Audit target.** All currently-shipped IB Math AA HL study guides
bilingualized to support a Mandarin-Chinese-language student writing the
IB exam in English. Chinese is a *teaching translation* — explains the
concept; English exam-rubric terms remain in `<code>` inline so the
student recognizes them on the exam paper. Playbook:
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).

**Audit method.** (1) Structural — count `data-lang="en"` vs
`data-lang="zh"` attributes; they must be equal. (2) Lexical — verify
core IB Math AA HL terminology is consistently rendered across files
(glossary in `prompts/create-bilingual-translation.md`). (3)
Pedagogical — spot-read sample concept-boxes / worked-examples in each
file; check the Chinese explains rather than literally translates.
(4) Validation — `scripts/validate.sh` passes on each file.

### Per-file scorecard

Mark ✅ when balanced and `validate.sh` passes; ✗ if either fails;
⏳ until the unit's translation commit lands. Fill in EN/ZH counts via
`grep -c 'data-lang="en"' "IB Math HL/Study Guides/Unit_*.html"` and
the matching `"zh"` count.

| # | Unit | EN/ZH balance | Glossary fit | Pedagogical | Validates | Notes |
|---|---|---|---|---|---|---|
| A1 | Sequences & Series       | 260 / 260 ✅ | ✅ | ✅ | ✅ | T-1 shipped `cdca220`. Supersedes playbook's stale `af27baf` reference. |
| A3 | Combinatorics            | 213 / 213 ✅ | ✅ | ✅ | ✅ | T-2 shipped `ea3124d`. Glossary covers <code>permutation</code>, <code>combination</code>, <code>binomial theorem</code>, <code>Pascal's triangle</code>, <code>Pascal's identity</code>, <code>circular arrangement</code>, <code>combinatorial proof</code>. |
| A4 | Complex Numbers          | 241 / 241 ✅ | ✅ | ✅ | ✅ | T-3 shipped `12dc6ad`. Glossary covers <code>Cartesian form</code>, <code>polar form</code>, <code>Euler form</code>, <code>Euler's formula</code>, <code>De Moivre's theorem</code>, <code>roots of unity</code>, <code>primitive root</code>, <code>conjugate root theorem</code>, <code>fundamental theorem of algebra</code>. Argand-gloss polish landed as follow-up. |
| C  | Geometry & Trigonometry  | 356 / 356 ✅ | ✅ | ✅ | ✅ | T-4 shipped `ebf8d11`. Largest file (2381 → 2909 lines). Glossary covers <code>sine rule</code>, <code>cosine rule</code>, <code>radian</code>, <code>arc length</code>, <code>sector area</code>, <code>dot product</code> (→ 数量积（点积）), <code>vector product</code> / <code>cross product</code> (→ 向量积（叉积）), <code>skew lines</code> (→ 异面), <code>magnitude</code>, <code>normal vector</code>, <code>vector equation of a line</code>, <code>vector equation of a plane</code>, plus <code>bearing</code> / <code>angle of elevation/depression</code>. |

A2, A5, A6 not in this sprint — they have not yet shipped (open in
Sprint 1 above). Translate as they ship.

### Findings — corpus-wide (closed 2026-05-21)

- **All 4 files have perfectly balanced `data-lang="en"` / `data-lang="zh"`
  attribute counts** (A1: 260/260, A3: 213/213, A4: 241/241, C: 356/356).
- **Bilingual infrastructure identical across all 4 files** — CSS toggle
  (`body:not(.lang-zh)…` + mirror), `toggleLang()` JS with
  `localStorage.drs.lang` persistence, nav button between Contents and
  Dark, `PingFang SC → Hiragino Sans GB → Microsoft YaHei` CJK fallback
  in `--font-body`.
- **Exam-term gloss pattern applied uniformly.** Every IB Math AA HL
  rubric term appears once in `<code>` on its first mention per Chinese
  passage; subsequent mentions left as plain Chinese.
- **Math notation untouched.** All LaTeX renders identically in both
  languages — Chinese flip changes only the prose.
- **Glossary consistency.** Core terms (sequence / series / arithmetic /
  geometric / binomial theorem / Pascal's triangle / permutation /
  combination / complex number / Argand diagram / De Moivre / modulus /
  argument / sine rule / cosine rule / dot product / cross product /
  skew lines) render identically across files.
- **`scripts/validate.sh` passes on all 4.**

Translation work is **publish-ready**. No P0 / P1 translation issues
remain.

### Findings — requiring follow-up

None. Sprint cleared with a small polish commit fixing three
`Argand plane` vs `Argand diagram` gloss mismatches in A4 (commit
follow-up to `12dc6ad`). Optional P2 refinements below.

### Optional refinements (P2 — not blocking)

| ID | Item | Why P2 |
|---|---|---|
| TR-1 | Add `lang="en"` / `lang="zh"` attribute (HTML standard) on toggled spans/divs to enhance screen-reader behavior | A11y polish; current behavior works fine for sighted users which is the dominant use case |
| TR-2 | Print stylesheet: decide whether `@media print` should default to EN or to the currently-toggled language | Edge case; consult once a Chinese-language student requests printable practice |
| TR-3 | Translation of `<title>` tags so browser tab reads in Chinese when in zh mode (currently `<title>` is EN-only) | Minor browser-chrome polish |

### Translation contract — standing principle (mirrors AP Calc / AP Physics close-out 2026-05-18 / 2026-05-19)

Chinese is a teaching translation, not literal. English exam-rubric
terminology stays in `<code>` inline. Math notation untouched. See
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).
This standing principle is co-equal with the Dual-Goal Philosophy
below — every future unit must conform to both.

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
