# Subject Spec — High School Math (US)

## Identity

- **Display (section heading):** High School Math
- **Display (hero chip):** High School Math
- **Directory:** `High School Math/`
- **Audit:** `High School Math/AUDIT.md`

## Official curriculum reference

US **Common Core State Standards for Mathematics (CCSSM)**, High School
conceptual categories. Content is organised around the conventional
**traditional pathway** of four year-long courses (the sequence most US
high schools use): Algebra I, Geometry, Algebra II, Pre-Calculus
(with Trigonometry).

The CCSSM High School standards are grouped by conceptual category
(Number & Quantity · Algebra · Functions · Modeling · Geometry ·
Statistics & Probability) rather than by course; we map them to the
four-course pathway below.

## Audience

US high schoolers (grades 9–12), and motivated grade-8 students taking
Algebra I early. Many readers will be students for whom the AP
Calculus / AP Physics products on this site are too advanced — High
School Math is the on-ramp to those products.

Not yet bilingual; ZH translation is a future-sprint option (same
pattern as the in-flight `ap_chinese_translation` work for AP Calc).

## Naming convention

Flat layout (matches AP Calculus and IB Math HL) — the course is part
of the filename, not a sub-directory:

```
High School Math/Study Guides/<Course>_Unit_N_Topic.html
High School Math/Practice Questions/<Course>_Unit_N_Topic_Practice.html
High School Math/Practice Questions/Solutions/<Course>_Unit_N_Topic_Solutions.html
```

`<Course>` is one of:
- `Algebra_I`
- `Geometry`
- `Algebra_II`
- `Pre_Calculus`

`N` is the unit number within that course (1, 2, 3, …). Topic uses
underscores in filenames; spaces and special characters are avoided.

Examples:
- `High School Math/Study Guides/Algebra_I_Unit_1_Linear_Functions.html`
- `High School Math/Study Guides/Geometry_Unit_3_Triangle_Congruence.html`

## Required `<title>` format

```
High School Math — <Course Display> Unit N: <Topic> | Dingrui Scholars
```

`<Course Display>` is the human-readable course name with a space, not
the filename form:

- `Algebra I`
- `Geometry`
- `Algebra II`
- `Pre-Calculus`

Examples:
- `High School Math — Algebra I Unit 1: Linear Functions | Dingrui Scholars`
- `High School Math — Pre-Calculus Unit 4: Trigonometric Identities | Dingrui Scholars`

`build-index.py` will read this verbatim — the home-page card text comes
straight from the `<title>`. Drift here will surface as a parse warning.

## Exam structure

There is no standardised "High School Math exam" — this is course-level
content. Where useful, units may flag:

- **State-standard cross-references** (CCSSM codes, e.g. HSA-REI.B.3)
- **SAT / ACT alignment** — quick-reference call-outs of the question
  patterns the College Board / ACT actually test
- **AP feeder alignment** — explicit pointers to which AP courses each
  unit feeds into (Algebra II → AP Calculus, Statistics; Pre-Calculus →
  AP Calculus, AP Physics)

The Practice Questions product type for this subject is **TBD** —
defer the format decision until the first practice file ships. Options
on the table: AP-style MCQ (mirrors AP CSA / Calc), short/extended
response (mirrors IB Math HL), or SAT-style mixed.

## Standing principles

- **Dual-goal contract** (inherited from IB Math HL): every guide must
  serve both the crammer (test tomorrow) and the depth student (going
  for a 5 on the AP feeder course). Cram cheat-sheet at the top,
  worked examples in the middle, going-deeper / proof in
  `<details>` blocks at the bottom. See `prompts/create-unit.md`.
- **No HL flag** — all content is in scope. Where a topic is
  "honors-level" in a typical US classroom, mark it with an
  `honors-flag` chip (TBD CSS — define when first used).
- **CCSSM tagging optional** but encouraged: small chip near the
  section heading citing the standard, e.g. `HSF-LE.A.2`.

## Course-to-unit mapping (skeleton)

The full unit list per course will be locked when each course's
Sprint 1 opens. Skeletons below are placeholders; verify against the
authoritative CCSSM scope before scoping a sprint.

### Algebra I (8–10 units typical)
Linear functions · Linear systems · Exponents & exponential functions ·
Polynomials & factoring · Quadratic functions · Quadratic equations ·
Rational & radical expressions · Statistics & data displays.

### Geometry (8–10 units typical)
Transformations · Congruence · Similarity · Right triangles &
trigonometry · Circles · Polygons & quadrilaterals · 3D figures &
volume · Coordinate geometry · Geometric proofs · (optional)
Probability.

### Algebra II (8–10 units typical)
Functions review & transformations · Quadratic functions &
complex numbers · Polynomial functions · Rational functions · Radical
functions & relations · Exponential & logarithmic functions ·
Sequences & series · Trigonometric functions · Statistics & data
analysis.

### Pre-Calculus (8–10 units typical)
Functions & graphs · Polynomial & rational functions · Exponential &
logarithmic functions · Trigonometric functions · Analytic
trigonometry · Trigonometric applications (vectors, polar, complex) ·
Systems & matrices · Conic sections · Sequences, series, &
probability · Introduction to limits.

## Build-index integration (do at first unit ship, not before)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Math", "High School Math", "chip-green"),
   ```
   (chip colour is a placeholder — pick the colour not already used
   by another subject card.)

2. Add to `WORD_PRIORITY` so the four courses sort in pathway order
   regardless of alphabetical ordering:
   ```python
   "High School Math": {
       "Algebra I Unit":   0,
       "Geometry Unit":    1,
       "Algebra II Unit":  2,
       "Pre-Calculus Unit": 3,
   },
   ```

3. Re-run `python scripts/build-index.py` to insert the card sentinels
   and populate the first card. `index.html` may also need a `<h2
   class="section-title">High School Math</h2>` + empty grid block
   inserted manually the first time, after which the script handles
   subsequent re-indexing.

## Cross-references

- Generation contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Style guide (design tokens, KaTeX patterns): [`rag/style-guide.md`](../style-guide.md)
- CCSSM official site: <https://www.thecorestandards.org/Math/>
  (verify against this; do not paraphrase from memory)
