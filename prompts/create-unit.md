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

<authoring_order>

## English first, bilingual is a follow-up commit (locked 2026-05-21)

**New units ship in English first.** Once the user confirms the
English revision for the file, the Mandarin teaching translation
lands as a separate follow-up commit per the locked playbook in
[`create-bilingual-translation.md`](create-bilingual-translation.md).

This applies to:

- Brand-new units drafted with this prompt.
- Improvements to existing English content (worked examples, exam
  tips, slider widgets).
- Coverage-gap drafts in subjects mid-translation (the new file ships
  English; bilingual catches up in the next translation wave).

**Why:** bilingual drafting in parallel doubled the surface area
under review without doubling editorial value. English-first lets the
user lock notes / examples / widgets once, then the translation pass
becomes mechanical against the locked English. It also keeps the
review cadence one-language-at-a-time per file, matching the locked
review-then-merge pattern.

</authoring_order>

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

**Naming.** Units use the **2029 super-topic ID**: `Unit_A1_*`
through `Unit_E6_*`. The full enumeration (locked 2026-05-22 against
the 2029 Subject Brief, first assessment 2029) is below. Use this
table whenever you invoke the prompt for an AA HL unit; the ID
becomes the filename prefix and the `<title>` super-topic tag.

| ID | Super-topic | SL/AHL | Filename slug |
|---|---|---|---|
| **A1** | Sequences | SL + AHL | `Unit_A1_Sequences_and_Series.html` |
| **A2** | Exponents and logarithms | SL + AHL | `Unit_A2_Exponents_and_Logarithms.html` |
| **A3** | Combinatorics | SL + AHL | `Unit_A3_Combinatorics.html` |
| **A4** | Complex numbers | AHL only | `Unit_A4_Complex_Numbers.html` |
| **A5** | Proof and algebraic manipulation | SL + AHL | `Unit_A5_Proof_and_Algebraic_Manipulation.html` |
| **B1** | Representation of functions | SL + AHL | `Unit_B1_Representation_of_Functions.html` |
| **B2** | Polynomial functions | SL + AHL | `Unit_B2_Polynomial_Functions.html` |
| **B3** | Functions with asymptotes | SL + AHL | `Unit_B3_Functions_with_Asymptotes.html` |
| **B4** | Trigonometric functions | SL + AHL | `Unit_B4_Trigonometric_Functions.html` |
| **B5** | Transformations of graphs and functions | SL + AHL | `Unit_B5_Transformations_of_Graphs_and_Functions.html` |
| **C1** | Surface areas, volumes, measurement in circles | SL | `Unit_C1_Surface_Areas_Volumes_Circles.html` |
| **C2** | Trigonometry and its applications | SL | `Unit_C2_Trigonometry_Applications.html` |
| **C3** | Vectors | AHL only | `Unit_C3_Vectors.html` |
| **D1** | Univariate data (with bivariate) | SL | `Unit_D1_Univariate_Data.html` |
| **D2** | Probability | SL + AHL | `Unit_D2_Probability.html` |
| **D3** | Probability distributions | SL + AHL | `Unit_D3_Probability_Distributions.html` |
| **E1** | Principles of differential calculus | SL + AHL | `Unit_E1_Principles_of_Differential_Calculus.html` |
| **E2** | Techniques of differential calculus | SL + AHL | `Unit_E2_Techniques_of_Differential_Calculus.html` |
| **E3** | Techniques of integral calculus | SL + AHL | `Unit_E3_Techniques_of_Integral_Calculus.html` |
| **E4** | Problem-solving using calculus | SL + AHL | `Unit_E4_Problem_Solving_Using_Calculus.html` |
| **E5** | Differential equations | AHL only | `Unit_E5_Differential_Equations.html` |
| **E6** | Maclaurin series | AHL only | `Unit_E6_Maclaurin_Series.html` |

**Twenty-two super-topics total.** Three are AHL-only (A4, C3, E5,
E6 — wait, that is four). Correction: four are AHL-only (A4 Complex
Numbers, C3 Vectors, E5 Differential Equations, E6 Maclaurin Series).
The rest are SL + AHL with HL extension sub-bullets flagged via the
`<span class="hl-flag">HL</span>` chip at section level.

**Title tag format.** `IB Math AA HL — Unit {ID}: {Title} | Dingrui Scholars`.
Examples:

- `IB Math AA HL — Unit E1: Principles of Differential Calculus | Dingrui Scholars`
- `IB Math AA HL — Unit B4: Trigonometric Functions | Dingrui Scholars`

**Grade scale and dual-goal phrasing.** Grade scale is 1 through 7.
The dual-goal contract phrases the two students as "last-ditch pass"
(target a 4) and "going for a 7".

**HL flagging.** A super-topic that is entirely AHL (A4, C3, E5, E6)
carries the `hl-flag` chip at unit level (in the hero meta strip).
Within a mixed-SL/HL super-topic, individual sections that are HL
extensions carry the chip at section level (next to the `<h2>` and
the `.ib-ref` chip). Pattern already established on A1, A3, A5, D2,
D3, E1. Keep that consistency.

**Calculator splits.** Where a topic has a clear calc / no-calc
split (most prominently in D3 Statistics Distributions), call it out
in the section header so the student knows which paper they are
preparing for.

**Cross-references.**
- Status authority (what is shipped, what is open): `IB Math HL/AUDIT.md`.
- Content authority (super-topic titles, SL/AHL split, 2021 to 2029
  sub-topic mapping): `rag/subjects/ib_math_aa_hl.md`.
- Source PDF (the 2029 Subject Brief): `rag/sources/IB Math HL/sb_maths_analysis_en.pdf`.

### AP Physics C / AP Calculus AB·BC / AP CSA
- Units numbered: `Unit_N_*`. Match the existing per-subject conventions
  for hero chips, section anchors, and worked-example schema.
- Dual-goal contract phrased as "last-ditch pass" vs "going for a 5."

### IB Chemistry HL
- Uses syllabus topic codes in the title: `Structure 1`, `Reactivity 2`,
  etc., not `Unit N`. Match the existing file's naming exactly.
</subject_notes>

<tone>

## Tone rules live in [`_tone.md`](_tone.md)

The two rules that apply to every authoring playbook in this
directory (no em or en dashes anywhere in prose, and the pre-LLM
textbook voice positive spec) have been hoisted to
[`prompts/_tone.md`](_tone.md). Read it before writing any prose
in this Study Guide. The sweep-for-dashes step before declaring
done is the highest-leverage style rule in the codebase; it lives
in `_tone.md` with the full rewrite table and exemption list.

</tone>

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
5. **No em or en dashes anywhere in prose.** See `<tone>` above. This
   is the single highest-leverage style rule. Six characters to
   sweep: `—`, `–`, `&mdash;`, `&ndash;`, `&#8212;`, `&#8211;`.
   All should return zero hits in a finished file.
6. **Pre-LLM textbook voice.** Definition, theorem, proof, worked
   example, remark. Not "Let's break this down" coaching prose. See
   the `<tone>` block for the positive spec.
</reminders>
