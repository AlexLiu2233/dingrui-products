# IB Math AA HL — Practice Questions

IB-style practice question sets for the IB Math AA HL study guides in
[`../`](../). **Paper-organized, mark-allocated, question-only.**

> **Status — in flight on the `ib_math_hl_units` branch.** Sub-units
> A1 (Sequences &amp; Series) and A3 (Combinatorics) are the first two
> shipped. See [`../AUDIT.md`](../AUDIT.md) for the active sprint.

Each practice set ships as standalone HTML, KaTeX-rendered, print-styled
at letter size. Open in a browser, or render to PDF via browser
"Save as PDF" (margins default).

## Index

| Sub-unit | Title | Items | Scope | HTML |
|---|---|---|---|---|
| A1 | Sequences &amp; Series | Paper 1A · Paper 1B · Paper 2 · Paper 3 | 1.2 – 1.4, 1.8 | [Unit_A1_Sequences_and_Series_Practice.html](Unit_A1_Sequences_and_Series_Practice.html) |
| A3 | Combinatorics | Paper 1A · Paper 1B · Paper 2 · Paper 3 | 1.9 – 1.11 | [Unit_A3_Combinatorics_Practice.html](Unit_A3_Combinatorics_Practice.html) |

Sub-units A2, A4, A5, A6 will follow as those study guides ship.

---

## Question taxonomy

Every question is tagged with **three pills** in the header (plus a mark
allocation):

### Paper labels

The IB AA HL exams have three papers:

- **Paper 1** (90 min, **no calculator**, 110 marks)
  - **Section A** — short response, 4–7 marks each. Tagged **`Paper 1A`**.
  - **Section B** — extended response, 12–20 marks each. Tagged **`Paper 1B`**.
- **Paper 2** (90 min, **GDC required**, 110 marks). Same A/B structure
  but mixed throughout. Tagged **`Paper 2`** without subdivision since
  practice doesn't replicate the strict timing split.
- **Paper 3** (HL only, 60 min, GDC required, 55 marks). Two long
  modeling/exploration problems. Tagged **`Paper 3`**.

### Difficulty pills

- **`EASY`** — direct application of one formula or definition. Should
  feel automatic to a 5-chaser.
- **`MEDIUM`** — multi-step, requires choosing the right formula and
  setting up cleanly. Most IB exam questions live here.
- **`HARD`** — synthesis across topics, clever set-up, or non-obvious
  technique. Where 6→7 students pull ahead.

The mix per practice file targets roughly **30% / 50% / 20%**
(Easy / Medium / Hard).

### Topic pills

IB syllabus reference, e.g. `1.2 Arithmetic Sequences`,
`1.10 Permutations`, `1.11 Extended Binomial`. Lets students (and
teachers) trace each item back to a syllabus point.

### Mark pills

`[N marks]` — IB uses these on every question. Practice files mirror
the convention so students get used to budgeting time by marks.

---

## Locked conventions (2026-05-09)

- **Question-only.** No embedded answers, no `<details>` reveals, no
  inline mark-schemes. Matches the AP Physics / AP Calculus house style.
  Teacher answer keys, if needed, ship as a separate
  `Unit_X_*_Answer_Key.html` companion.
- **`\mathrm{...}` for unit composition** (e.g. `\mathrm{m/s}`,
  `\mathrm{years}`); plain math mode for variables.
- **`~` for value-unit spacing** — `5~\mathrm{years}`, `\$2000`.
- **CSS contract:** `@page { size: letter; margin: 0.6in 0.65in; }`,
  Times New Roman body, DM Serif Display chapter title, Source Sans 3
  pills. Print-targeted; no dark mode.
- **Maroon `#7A2E2E`** accent on the question card's left border for MC
  / short-response items; navy `#1E3F75` for FRQ-style extended response.
- **Page breaks** between Section B / Paper 3 problems so each gets a
  full sheet for student work.

---

## Workflow

```bash
# Validate
bash scripts/validate.sh "IB Math HL/Practice Questions/Unit_A1_*.html"

# Render PDF (browser "Save as PDF" — keep margins at default)
# or use Chromium headless:
#   chrome --headless --print-to-pdf=Unit_A1.pdf <file>
```
