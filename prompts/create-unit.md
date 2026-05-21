# Create New Unit

<task>
Generate a self-contained Dingrui Scholars Study Guide HTML file for
one unit of one subject. The output must follow the in-subject
conventions of the existing units (hero schema, TOC sidebar, quiz
markup, flashcard markup, dark-mode wiring) and must satisfy the
**dual-goal contract** below — the locked editorial promise of the
product.
</task>

<inputs>
- **Subject**: {{SUBJECT}}                     *e.g. `AP Physics`, `IB Math HL`*
- **Unit number / letter**: {{UNIT_NUMBER}}    *e.g. `5`; or `B` for IB Math HL*
- **Unit title**: {{UNIT_TITLE}}               *e.g. `Magnetic Fields`*
- **Topics**: {{TOPICS_LIST}}                  *bullet list of sub-topics to cover*
</inputs>

<contract>

## The dual-goal contract (read first, enforce at every section)

Every Study Guide must serve **two students at once**, in the same file:

1. **The crammer.** Opens this the night before the exam, needs a
   last-ditch pass. They should skim top-to-bottom and walk into the
   exam with the formulas, the canonical worked examples, and the
   question patterns the exam actually rewards. **They should never
   have to read a derivation to find a formula.**
2. **The top-score chaser.** Studying in depth, aiming for a 5 on AP
   or a 7 on IB. They should find the *why* — derivation, subtleties,
   edge cases, proof structure — without leaving the page.

**Concrete layering, per section:**

- **Cheat-sheet element at the top** (key-formula card, "what you must
  know" callout, or a one-line summary box) — the crammer can lift it
  in under a minute.
- **One or two worked examples** showing the canonical exam application.
  Doubles as crammer fuel and depth practice.
- **A "going deeper" / proof / derivation block** (clearly labeled,
  often in `box--proof` or `<details>`) the crammer skips and the
  top-score chaser dives into.
- **Quiz items** that mix recall (crammer pass) with synthesis
  (top-score pass).

> A section that reads as "just notes" serves neither student. Either
> crystallize the takeaway for the crammer, or expand the derivation
> for the depth student. Usually both.
</contract>

<workflow>
1. **Read [`rag/style-guide.md`](../rag/style-guide.md)** — design
   tokens, typography, color system.
2. **Read [`rag/template.html`](../rag/template.html)** — base HTML
   scaffold.
3. **Read an existing unit in the same subject folder.** The new unit
   must feel like a sibling: same hero schema, same TOC sidebar, same
   quiz markup, same flashcard markup, same dark-mode wiring. *Do not
   invent components a sibling unit doesn't have.*
4. **Read the subject-level audit** — `{{SUBJECT}}/AUDIT.md`. Honor any
   in-flight sprint conventions or locked decisions.
5. **Generate the full HTML.** Cover every topic from `{{TOPICS_LIST}}`,
   each section satisfying the dual-goal contract.
6. **Save** to the canonical path (see `<output_format>` below).
7. **Validate** — `bash scripts/validate.sh {{SUBJECT_DIR}}/Study Guides/{{FILENAME}}` exits 0.
8. **Update `{{SUBJECT}}/AUDIT.md`** — cross-unit snapshot table, sprint status.
9. **Run** `python scripts/build-index.py` to wire the new unit into `index.html`.
</workflow>

<output_format>

**File path:**
```
{{SUBJECT}}/Study Guides/Unit_{{UNIT_NUMBER}}_{{UNIT_TITLE_SNAKE_CASE}}.html
```

**`<title>` tag** (`build-index.py` parses this — exact format required):
```html
<title>{Subject Long} — {Prefix}: {Topic} | Dingrui Scholars</title>
```
Concrete examples:
- `AP Physics C: Mechanics — Unit 1: Kinematics | Dingrui Scholars`
- `IB Chemistry — Structure 1: Models of the Particulate Nature of Matter | Dingrui Scholars`
- `IB Math AA HL — Unit A1: Sequences & Series | Dingrui Scholars`

**Required sections per unit:**
- Hero (overline, h1, subtitle, "Read me first" intro)
- Sticky TOC sidebar
- One section per topic in `{{TOPICS_LIST}}`, each with: cheat-sheet,
  1–2 worked examples, going-deeper block (where applicable),
  2–3 quiz items mixing recall + synthesis
- Flashcard deck — 8+ cards covering must-know facts
- Print-friendly styles (no clipped equations, no orphaned headers)
- Dark-mode wiring via `[data-theme="dark"]` overrides
</output_format>

<examples>

### Example — section skeleton that satisfies the dual-goal contract

```html
<section id="chain-rule">
  <h2>3 · The Chain Rule</h2>

  <!-- (1) CHEAT-SHEET — crammer lifts this in <1 minute -->
  <div class="box box--tip">
    <div class="box__title">Key formula</div>
    <p>If $y = f(g(x))$, then $\dfrac{dy}{dx} = f'(g(x)) \cdot g'(x)$.</p>
    <p>Read: <em>derivative of the outside, evaluated at the inside,
    times derivative of the inside.</em></p>
  </div>

  <!-- (2) WORKED EXAMPLE — canonical exam application -->
  <div class="worked-example">
    <h3>Example 3.1 — polynomial inside, polynomial outside</h3>
    <p>Differentiate $y = (2x^2 + 5)^4$.</p>
    <ol class="steps">
      <li>Identify $f(u) = u^4$, $g(x) = 2x^2 + 5$.</li>
      <li>$f'(u) = 4u^3$, $g'(x) = 4x$.</li>
      <li>$\dfrac{dy}{dx} = 4(2x^2 + 5)^3 \cdot 4x = 16x(2x^2 + 5)^3$.</li>
    </ol>
  </div>

  <!-- (3) GOING DEEPER — top-score chaser dives in, crammer skips -->
  <details class="box box--proof">
    <summary>Going deeper — proof from the limit definition</summary>
    <p>By the definition of the derivative …</p>
  </details>

  <!-- (4) QUIZ — mix recall (Q1) + synthesis (Q2) -->
  <div class="quiz">
    <div class="quiz-q">
      <p class="quiz-q__prompt">If $y = \sin(3x)$, find $\dfrac{dy}{dx}$.</p>
      <!-- options + hidden answer block -->
    </div>
    <div class="quiz-q">
      <p class="quiz-q__prompt">Show that $\dfrac{d}{dx}\bigl(\sqrt{1+\tan^2 x}\bigr) = \sec x \tan x$ for $x \in (0, \pi/2)$.</p>
      <!-- options + hidden answer block -->
    </div>
  </div>
</section>
```

This section reads as a unit even though it's serving two audiences in
parallel. The crammer reads the tip box and Example 3.1 and leaves.
The top-score chaser also reads the proof in `<details>` and works
through Q2.

### Example — failure mode (do not ship this)

A section that has only:
- a wall of prose explaining the chain rule, AND
- one quiz question

…serves neither student. The crammer can't extract the formula in 30
seconds; the top-score chaser gets no derivation. **Add a tip box,
worked example, and proof block before considering the section done.**
</examples>

<acceptance>
- [ ] Cheat-sheet element present in every section, lift-able in <1 minute
- [ ] Going-deeper / proof block present wherever the topic has one
- [ ] All KaTeX delimiters correct: `$…$` inline, `$$…$$` display.
      No unicode subscripts/superscripts/Greek inside `\text{}`
- [ ] Quiz answers hidden until revealed (match the in-subject pattern)
- [ ] Mobile responsive at 375px (no horizontal scroll)
- [ ] Dark mode works — only `[data-theme="dark"]` overrides, no
      hardcoded light-only colors
- [ ] Print preview clean — no clipped equations, no orphaned headers
- [ ] All TOC links resolve to existing `id=` anchors
- [ ] `bash scripts/validate.sh` exits 0 on the new file
- [ ] `python scripts/build-index.py` regenerated `index.html` and the diff is sensible
</acceptance>

<subject_notes>

### IB Math AA HL
- Units use **letters, not numbers**: `Unit_A_*` through `Unit_E_*`
  (Topics 1–5: Number & Algebra, Functions, Geometry & Trigonometry,
  Statistics & Probability, Calculus).
- Grade scale is 1–7. The dual-goal contract phrases this as
  "last-ditch pass" (≈ a 4) vs. "going for a 7."
- HL-only content (vs SL) should be flagged inline with a chip or
  callout so SL students know what to skip.
- Where a topic has a clear calculator / no-calculator split (e.g.
  statistics distributions), call it out in the section header.

### AP Physics C / AP Calculus AB·BC / AP CSA
- Units numbered: `Unit_N_*`. Match the existing per-subject conventions
  for hero chips, section anchors, and worked-example schema.
- Dual-goal contract phrased as "last-ditch pass" vs "going for a 5."

### IB Chemistry HL
- Uses syllabus topic codes in the title: `Structure 1`, `Reactivity 2`,
  etc., not `Unit N`. Match the existing file's naming exactly.
</subject_notes>

<reminders>
Repeated at the tail because these are the most-forgotten rules when
the file gets long:

1. **Dual-goal contract.** Every section needs a cheat-sheet AND
   a going-deeper element. A wall of prose serves neither student.
2. **Sibling parity.** The new unit must look and behave like an
   existing unit in the same subject. Do not invent new components.
3. **`<title>` tag is the source of truth** for `build-index.py`.
   Get the format right or the card on the landing page is wrong.
4. **Run `build-index.py` AND `validate.sh`** before declaring done.
   They catch different classes of mistakes.
</reminders>
