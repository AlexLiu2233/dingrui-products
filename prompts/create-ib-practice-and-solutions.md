# Create IB Practice + Solutions Set

<task>
Produce a Practice + Solutions HTML pair for one IB Math AA HL unit
(template generalizes to any IB subject). The two files are locked to
each other by a `dingrui:version` tag that `scripts/validate.sh`
enforces; bumping a version on one without the other is a build error.
</task>

<inputs>
- **Unit**: {{UNIT_ID}}                *e.g. `A3`, `B`, `D`*
- **Title**: {{UNIT_TITLE}}            *e.g. `Combinatorics`*
- **Syllabus scope**: {{TOPIC_RANGE}}  *e.g. `1.9 – 1.11`*
- **Pair key**: {{PAIR_KEY}}           *e.g. `IB-Math-HL-A3`*
- **Version**: starts at `v1.0`; bump both files together
</inputs>

<contract>

### Difficulty + paper mix — locked

- **Difficulty mix**: MEDIUM and HARD only. **No EASY.** The first
  sellable cut is exam-level and concept-extending, not recall practice.
- **Papers**: Paper 1A (no-calc, short) · Paper 1B (no-calc, extended)
  · Paper 2 (calc, mixed). **Skip Paper 3** unless the user asks for it
  — different product (HL-only, longer modeling problems).
- **Question count**: ~8–12 items.
- **Mark target**: ~80 marks total, distributed 1A : 1B : 2 ≈ 30 : 25 : 30.
- **Coverage**: every syllabus sub-topic in scope must appear in at
  least one question. Re-read the Study Guide's section list and tick
  them off.

### Concept extension — the actual deliverable

Every question must do more than direct application. Use these patterns:

| Pattern | Use for |
|---|---|
| Multi-part scaffolded P1B | Set up a system, solve it, apply the result (e.g. find $n, a$ from two coefficients, extract another) |
| Identity proof via $(1+x)^n$ manipulation | Differentiate / substitute to derive $\sum r\binom{n}{r}$, $\sum r^2 \binom{n}{r}$, etc. |
| Combinatorial proof | "Count this set two ways" (hockey-stick, Vandermonde) |
| Consecutive-ratio test | Largest coefficient in $(1+bx)^n$; consecutive-coefficient-ratio systems |
| Scaling trick on extended binomial | Approximate irrationals outside the radius of convergence (e.g. $\sqrt{2} = \tfrac{7}{5}\sqrt{1+r}$) |
| Gap method | "No two X adjacent" in linear OR circular arrangements (circle has $n$ gaps not $n+1$) |
| Block method | "X must be together" or "X sits between Y and Z" |
| Conditional probability with combinations | $P(\text{exactly } k \mid \text{at least } 1)$ committee problems |

Each question card carries a `topic` pill naming the **specific extension
pattern**, not just the syllabus reference. Helps the student recognize
the machinery.

### Version-pair invariant

Both files carry this HTML comment immediately after `<title>`:

```html
<!-- dingrui:version v1.0  dingrui:pair-key IB-Math-HL-<ID>  dingrui:doc-type practice -->
```

(`dingrui:doc-type solutions` on the Solutions file; **same `pair-key`
and `version` on both**.)

`scripts/validate.sh` fails on mismatch. This is the canonical pairing
handle — banner text, footer chip, and the comment must agree.
</contract>

<output_format>

### File layout

```
<Subject>/Practice Questions/Unit_<ID>_<Topic>_Practice.html
<Subject>/Practice Questions/Solutions/Unit_<ID>_<Topic>_Solutions.html
```

### Practice file — non-negotiable structure

1. **Engineering banner** (replaces the old prose draft banner):
   ```html
   <p class="draft-banner"><code>v1.0</code> · 10 Qs · 81 marks · Papers 1A/1B/2 · MED–HARD · Topics 1.9–1.11 · solutions: <code>Solutions/Unit_A3_Combinatorics_Solutions.html</code></p>
   ```
   Just the facts: version, item count, total marks, papers,
   difficulty band, syllabus range, solutions path. No promo copy.

2. **Three Parts**, thick rule separators: PART I (Paper 1A) · PART II
   (Paper 1B) · PART III (Paper 2). One `.page-break` between Parts.

3. **Question card** uses the existing CSS contract (`.q`, `.q-head`,
   pills, `.frq-parts`, `.work` for student work-space). **No
   answers, no `<details>` reveals, no inline mark-schemes** — that's
   the Solutions file's job.

4. **Mark-allocated sub-parts**: every `(a)`, `(b)`, `(i)`, `(ii)`
   carries its own `[N]` marks-inline tag. Total per-question marks
   must match the header pill.

5. **Footer chip** ends with the version tag, e.g.
   `Unit A3 Practice v1.0`.

### Solutions file — non-negotiable structure

1. **Same scaffolding** as Practice (fonts, pills, parts) for visual parity.

2. **Engineering banner**: version + pair reference, plus a one-line
   key for the M1/A1/R1 chips used inside.

3. **Per-question solution block** uses the green `.solution` card with:
   - `answer-line` — one-line summary of the final answers, sub-part labelled.
   - `rationale` — the worked method, broken into `<h4>` sub-parts
     matching the Practice file's `(a) (b) (c) …`.
   - **Mark callouts** as small green chips (`.marks-call`) after each
     sub-part heading: `M1·A1`, `M1·M1·A1`, etc. Match the IB mark scheme.
   - **`.insight` block** at the end of each solution — one paragraph
     for the 7-chaser: the underlying pattern, why this is the canonical
     IB approach, the trap that loses marks, or a generalization.
     **This is the differentiator from a vanilla mark scheme.**

4. **Restate the prompt** at the top of each card (italicized, in
   `.prompt`) so the Solutions file reads standalone.

5. **Footer chip**: `Unit <ID> Solutions v1.0 · Companion to Practice v1.0`.
</output_format>

<workflow>

1. **Read the corresponding Study Guide first.** List every section.
   Practice must cover every section; Solutions must use only
   notation / results the Study Guide introduces.
2. **Draft the question list** before writing HTML — one line per
   question with paper, difficulty, topic, marks, and the *concept
   extension* it tests. Send to the user for review **only if scope is
   unclear**; otherwise proceed.
3. **Verify every answer mathematically before writing the Solutions
   file.** Compute concrete numbers, sanity-check ratios, plug back
   into identities. Solutions with arithmetic errors are worse than no
   Solutions.
4. **Write Practice first, Solutions second.** Sub-part labels and
   marks match exactly between files.
5. **Validate** — `bash scripts/validate.sh` on both. The version-pair
   check fails on `dingrui:version` mismatch.
</workflow>

<examples>

### Example — one Practice question card (Paper 1B style)

```html
<article class="q" id="q4">
  <div class="q-head">
    <span class="pill pill--paper">Paper 1B</span>
    <span class="pill pill--diff">HARD</span>
    <span class="pill pill--topic">scaffolded system + identity proof</span>
    <span class="marks-total">[10]</span>
  </div>
  <p>The first three terms in the expansion of $(1 + ax)^n$ in
  ascending powers of $x$ are $1$, $24x$, and $264x^2$.</p>
  <ol class="frq-parts">
    <li>Find the values of $a$ and $n$. <span class="marks">[3]</span></li>
    <li>Hence find the coefficient of $x^3$. <span class="marks">[2]</span></li>
    <li>Show that $\displaystyle\sum_{r=0}^{n} r \binom{n}{r} a^{r} = na(1+a)^{n-1}$
        and use it to evaluate $\displaystyle\sum_{r=0}^{n} r \binom{n}{r} 2^{r}$
        for the value of $n$ found in (a). <span class="marks">[5]</span></li>
  </ol>
  <div class="work" aria-label="Student work space"></div>
</article>
```

### Example — the paired Solutions card

```html
<article class="solution" id="s4">
  <div class="q-head">
    <span class="pill pill--paper">Paper 1B</span>
    <span class="marks-total">[10]</span>
  </div>
  <p class="prompt"><em>The first three terms in the expansion of
  $(1 + ax)^n$ in ascending powers of $x$ are $1$, $24x$, and $264x^2$.
  …</em></p>

  <p class="answer-line"><strong>Answers:</strong>
  (a) $a = 2,\ n = 12$ · (b) $1760$ · (c) $\displaystyle\sum = na(1+a)^{n-1}$; value $= 24 \cdot 3^{11}$.</p>

  <h4>(a) Find $a$ and $n$. <span class="marks-call">M1·M1·A1</span></h4>
  <p>From the linear term: $na = 24$. (M1)</p>
  <p>From the quadratic term: $\binom{n}{2} a^2 = 264 \Rightarrow n(n-1)a^2 = 528$. (M1)</p>
  <p>Solving the system: $a = 2$, $n = 12$. (A1)</p>

  <h4>(b) Coefficient of $x^3$. <span class="marks-call">M1·A1</span></h4>
  <p>$\binom{12}{3} \cdot 2^3 = 220 \cdot 8 = 1760$. (M1·A1)</p>

  <h4>(c) Identity + evaluation. <span class="marks-call">M1·R1·M1·A1·A1</span></h4>
  <p>Differentiate $(1+x)^n = \sum_{r=0}^{n} \binom{n}{r} x^r$ to get
  $n(1+x)^{n-1} = \sum_{r=0}^{n} r\binom{n}{r} x^{r-1}$. (M1)</p>
  <p>Multiply by $x$ and substitute $x = a$: $\sum r\binom{n}{r} a^r = na(1+a)^{n-1}$. (R1)</p>
  <p>With $a = 2, n = 12$: $\sum = 12 \cdot 2 \cdot 3^{11} = 24 \cdot 3^{11}$. (M1·A1)</p>
  <p>Numerically $= 24 \cdot 177{,}147 = 4{,}251{,}528$. (A1)</p>

  <div class="insight">
    <strong>Insight.</strong> Identities of the form $\sum r\binom{n}{r} x^{r}$
    fall out of differentiating the binomial expansion. The trick is to
    keep the dummy variable and the parameter ($x$) separate — students
    who differentiate "in $n$" lose every mark on parts like (c). Once
    the identity is set up, the IB only awards full marks when the
    final numeric value is computed, not left as $24 \cdot 3^{11}$.
  </div>
</article>
```

Notice: sub-part labels `(a) (b) (c)` and mark counts `[3] [2] [5]` =
`[10]` agree exactly across both files. That's what `validate.sh`
checks for in spirit; the `dingrui:version` is what it checks for
literally.
</examples>

<version_rules>

- Bump to `v1.1` when both files get a substantive edit together
  (added questions, reworded solutions, refreshed scope).
- Patch (`v1.0 → v1.0.1` — three components allowed) is fine for
  typo-only fixes; bump on **both files** even if only one was edited.
- The version tag is the canonical pairing handle. Banner, footer chip,
  and the `dingrui:version` comment must agree.
</version_rules>

<cross_references>

- Dual-goal contract for **Study Guides**:
  [`create-unit.md`](create-unit.md) — Practice does NOT follow the
  dual-goal contract; that's a Study Guide pattern. Practice serves
  *exam preparation*, not first-time learning.
- Practice Questions conventions index:
  `<Subject>/Practice Questions/README.md`
- IB Math HL audit (active sprint, what's open):
  [`../IB Math HL/AUDIT.md`](../IB%20Math%20HL/AUDIT.md)
- Reference build (the run that locked this template):
  IB Math HL Unit A3, commit `4d42faf`+ (`ib_math_hl_a3_practice` branch).
</cross_references>

<reminders>
The four invariants most often violated when the file pair gets long —
re-stated at the tail:

1. **No EASY questions.** MED + HARD only. The first cut sells.
2. **`dingrui:version` and `dingrui:pair-key` match on both files.**
   `validate.sh` is the gate.
3. **Per-question mark totals add up.** `(a)[3] + (b)[2] + (c)[5] = [10]`
   in both files.
4. **Insight block on every solution.** It's the difference between
   our Solutions and a vanilla mark scheme.
</reminders>
