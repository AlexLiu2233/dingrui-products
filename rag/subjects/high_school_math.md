# Subject Spec — High School Math (multi-syllabus, topic-organised)

## Identity

- **Display (section heading):** High School Math
- **Display (hero chip):** High School Math
- **Directory:** `High School Math/`
- **Audit:** `High School Math/AUDIT.md`

## Strategic posture (locked 2026-05-16)

**One study-guide set, organised by mathematical topic.** Math is math —
linear functions, quadratics, trig, exponentials cover the same scope
in every modern HS curriculum. Each guide is written once around the
universal topic, with **syllabus-specific callouts** inside the page
where coverage genuinely diverges.

**Market priority (largest → smallest, English-language):**

1. **US Common Core** — primary commercial target.
2. **Canadian provinces:** Ontario, British Columbia, Alberta — secondary
   target. Repo author is based in Canada, so this audience is
   acknowledged explicitly and tested against per-unit.

We do **not** ship four separate course tracks (Algebra I, Geometry,
Algebra II, Pre-Calc). We ship one topic-indexed set that serves all
four implicitly.

## Source documents

Catalogued in [`sources.txt`](../../sources.txt) at the repo root.
Status `[ ]` means URL queued but not yet pulled into `rag/sources/`.

| Region | Course / doc | Status |
|---|---|---|
| 🇺🇸 US | CCSSM High School (single PDF, ~93 pp) | **Not yet in `sources.txt`** — add as the next sprint step |
| 🇨🇦 BC | Foundations & Pre-Calc 10, Pre-Calc 11, Pre-Calc 12, Calculus 12 | Listed (rows 1–4), not pulled |
| 🇨🇦 ON | Gr 9–10 (MPM2D), Gr 11–12 (MCR3U / MHF4U / MCV4U / MDM4U) | Listed (rows 5–6), not pulled |
| 🇨🇦 AB | Math 10C / 20-1 / 30-1, Math 31, assessment standards & exemplars | Listed (rows 7–12), not pulled |

**Verification rule:** any syllabus-specific claim in a guide (course
code, topic placement, exam-expected emphasis) must be checked against
the corresponding source document before shipping. Training-data
recall is *not* an acceptable citation. Place the source PDF under
`rag/sources/<region>/...` per the `SAVE_AS` column.

## Naming convention

Flat, topic-indexed — no course prefix, no per-region split:

```
High School Math/Study Guides/Unit_N_Topic.html
High School Math/Practice Questions/Unit_N_Topic_Practice.html
High School Math/Practice Questions/Solutions/Unit_N_Topic_Solutions.html
```

`N` is the topic index across the whole subject (1, 2, 3, …). Topic
uses underscores in filenames; avoid commas / ampersands.

Examples:
- `Unit_1_Linear_Functions_and_Systems.html`
- `Unit_5_Exponential_and_Logarithmic_Functions.html`

## Required `<title>` format

```
High School Math — Unit N: <Topic> | Dingrui Scholars
```

Examples:
- `High School Math — Unit 1: Linear Functions and Systems | Dingrui Scholars`
- `High School Math — Unit 7: Right-Triangle Trigonometry | Dingrui Scholars`

`build-index.py` reads this verbatim to generate the home-page card.

## Topic list (initial proposal, ~15 units to span the full scope)

This is the working scope. Lock per-unit ordering when the unit is
opened for drafting. Each unit's audit row should record the topic
chosen and the syllabus codes it maps to.

| Unit | Topic | Cross-syllabus weight |
|---|---|---|
| 1   | Linear Functions and Systems            | universal — all four |
| 2   | Quadratic Functions and Equations       | universal |
| 3   | Polynomial Functions                    | universal |
| 4   | Rational and Radical Expressions        | universal |
| 5   | Exponential and Logarithmic Functions   | universal |
| 6   | Sequences and Series                    | universal (timing differs) |
| 7   | Right-Triangle Trigonometry             | universal |
| 8   | Unit-Circle Trig and Trigonometric Functions | universal |
| 9   | Trigonometric Identities and Equations  | universal |
| 10  | Function Transformations and Composition| universal |
| 11  | Combinatorics and the Binomial Theorem  | BC PC12, AB 30-1, ON MHF4U cover; US is Pre-Calc-light |
| 12  | Conic Sections                          | US Pre-Calc strong; Canadian curricula treat lightly |
| 13  | Probability and Statistics Foundations  | universal, but ON splits to MDM4U |
| 14  | Vectors (2D and 3D)                     | ON MCV4U strong; US Pre-Calc light; not in BC/AB Pre-Calc |
| 15  | Introduction to Limits and Calculus     | feeder to AP Calc / IB Math AA HL; cross-syllabus optional |

Geometry units (congruence, similarity, circles, 3D figures) are
deliberately omitted from this initial list — they're a full course in
the US system but distributed across grades in Canadian curricula.
Decision deferred to a follow-on sprint if the topic-set proves
demand.

## In-page conventions (the multi-syllabus pattern)

Each unit's HTML must include, near the top of the page (immediately
under the hero or in the first section), a **Syllabus Map callout**:

```html
<aside class="syllabus-map">
  <div class="syllabus-map-label">Where this lives in your syllabus</div>
  <ul>
    <li><strong>🇺🇸 US Common Core:</strong> HSF-LE.A.1, HSF-LE.A.2, HSA-REI.D.10–12</li>
    <li><strong>🇨🇦 Ontario:</strong> MPM2D — Linear Systems; MCR3U review</li>
    <li><strong>🇨🇦 BC:</strong> Foundations &amp; Pre-Calc 10 — Relations and Functions</li>
    <li><strong>🇨🇦 Alberta:</strong> Math 10C — Relations and Functions</li>
  </ul>
</aside>
```

CSS class `syllabus-map` is **TBD** — define on first unit (use the
existing accent-ruled callout style as a starting point; see
`rag/style-guide.md`).

Where the curricula **genuinely diverge** (a topic emphasised in one
but absent or deferred in another), use a smaller inline callout:

```html
<div class="syllabus-note">
  <strong>Syllabus note.</strong> Ontario's MCR3U covers this through
  worked examples only; BC Pre-Calc 11 includes a formal proof on the
  Provincial-style assessment. If you're prepping for the BC provincial,
  read the going-deeper proof below; if MCR3U, focus on the examples.
</div>
```

Use these **sparingly** — only when there's a real difference a
student would feel. Don't pepper every section with one.

## Standing principles

- **Dual-goal contract** (inherited from IB Math HL): every guide
  serves both the test-tomorrow crammer (≥ pass) and the depth student
  (5 on AP feeder / 100 on provincial). Cram cheat-sheet at top,
  worked examples, going-deeper proofs in `<details>`. Canonical
  articulation in [`prompts/create-unit.md`](../../prompts/create-unit.md).
- **English-first** — translation tracks are a future sprint.
- **No HL flag** (there's no HL tier in HS Math). Where a topic is
  honors-level in a typical US classroom OR is the harder "1" stream
  in Canada (BC Pre-Calc vs. Foundations, AB Math 30-1 vs. 30-2),
  mark with an `honors-flag` chip (CSS TBD when first used).
- **AP / IB feeder pointers** — Algebra II / Pre-Calc topics flag the
  AP Calc / AP Stats / IB AA HL units they feed into. Hyperlink where
  the target unit already exists in this repo.

## Build-index integration (do at first unit ship)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Math", "High School Math", "chip-green"),
   ```
   (chip colour: pick one not already used.)

2. **No `WORD_PRIORITY` entry needed** — units are numbered
   sequentially with no sub-categories, so default numerical sort is
   correct.

3. Re-run `python scripts/build-index.py`. `index.html` may need a
   `<h2 class="section-title">High School Math</h2>` + empty grid
   block inserted manually the first time, after which the script
   handles re-indexing.

## Cross-references

- Dual-goal contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Style tokens: [`rag/style-guide.md`](../style-guide.md)
- Source URLs (queued): [`sources.txt`](../../sources.txt) at repo root
- Official references (verify against, do not paraphrase from memory):
  - CCSSM: <https://www.thecorestandards.org/Math/>
  - BC: <https://curriculum.gov.bc.ca/curriculum/mathematics/>
  - Ontario: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-mathematics>
  - Alberta: <https://www.alberta.ca/programs-of-study>
