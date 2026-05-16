# Create IB Practice + Solutions Set

You are creating a Practice + Solutions pair for an IB Math AA HL unit (and
the same template works for any IB subject). One Practice file, one Solutions
file, locked to each other by a `dingrui:version` tag that
`scripts/validate.sh` enforces.

## Inputs
- **Unit**: {{UNIT_ID}}  (e.g. `A3`, `B`, `D`)
- **Title**: {{UNIT_TITLE}}  (e.g. `Combinatorics`)
- **Syllabus scope**: {{TOPIC_RANGE}}  (e.g. `1.9 – 1.11`)
- **Pair key**: {{PAIR_KEY}}  (e.g. `IB-Math-HL-A3`)
- **Version**: starts at `v1.0`; bump to `v1.1` when both files change together

## Hard-locked design (do not deviate without explicit instruction)

### Scope
- **Difficulty mix**: MEDIUM and HARD only. No EASY. The first sellable cut
  should be exam-level and concept-extending, not recall practice.
- **Papers**: Paper 1A (no-calc, short response) · Paper 1B (no-calc,
  extended) · Paper 2 (calc, mixed). Skip Paper 3 unless the user asks for
  it — it's a different product (HL-only, longer modeling problems).
- **Question count**: roughly 8–12 items. Target **~80 marks total**, with
  the mark distribution roughly 1A : 1B : 2 = 30 : 25 : 30.
- **Coverage**: every syllabus sub-topic in scope must hit at least one
  question. Re-read the study guide's section list and tick them off.

### Concept-extension (the actual deliverable)
Each question must do more than direct application. Lean on these patterns:

| Pattern | Use it for |
|---|---|
| Multi-part scaffolded P1B | Set up a system, solve it, then apply the result (e.g. find $n, a$ from two coefficients, then extract another) |
| Identity proof via $(1+x)^n$ manipulation | Differentiate / substitute to derive $\sum r\binom{n}{r}$, $\sum r^2 \binom{n}{r}$, etc. |
| Combinatorial proof | "Count this set two different ways" (hockey-stick, Vandermonde) |
| Consecutive-ratio test | Largest coefficient in $(1+bx)^n$; consecutive-coefficient-ratio systems |
| Scaling trick on extended binomial | Approximate irrationals that lie outside the radius of convergence (e.g. $\sqrt{2} = \tfrac{7}{5}\sqrt{1+r}$) |
| Gap method | "No two X adjacent" in linear OR circular arrangements (call out circle has $n$ gaps not $n+1$) |
| Block method | "X must be together" or "X sits between Y and Z" |
| Conditional probability with combinations | $P(\text{exactly } k \mid \text{at least } 1)$ committee problems |

Each question card should carry a `topic` pill naming the specific extension
pattern, not just the syllabus reference. Helps the student recognize the
machinery.

## File layout

```
<Subject>/Practice Questions/Unit_<ID>_<Topic>_Practice.html
<Subject>/Practice Questions/Solutions/Unit_<ID>_<Topic>_Solutions.html
```

Both files must include this HTML comment immediately after `<title>`:

```html
<!-- dingrui:version v1.0  dingrui:pair-key IB-Math-HL-<ID>  dingrui:doc-type practice -->
```
(`dingrui:doc-type solutions` for the Solutions file; same `pair-key` and
`version` on both — `scripts/validate.sh` fails on mismatch.)

## Practice file — non-negotiable structure

1. **Engineering banner** (replaces the old prose draft banner):
   ```html
   <p class="draft-banner"><code>v1.0</code> · 10 Qs · 81 marks · Papers 1A/1B/2 · MED–HARD · Topics 1.9–1.11 · solutions: <code>Solutions/Unit_A3_Combinatorics_Solutions.html</code></p>
   ```
   Just the facts: version, item count, total marks, papers, difficulty band,
   syllabus range, solutions path. No promotional copy.

2. **Three Parts** with thick rule separators: PART I (Paper 1A) · PART II
   (Paper 1B) · PART III (Paper 2). One `.page-break` between Parts.

3. **Question card** uses the existing CSS contract (`.q`, `.q-head`, pills,
   `.frq-parts`, `.work` for student work-space). No answers, no `<details>`
   reveals, no inline mark-schemes — that's the Solutions file's job.

4. **Mark-allocated sub-parts**: every sub-part `(a)`, `(b)`, `(i)`, `(ii)`
   carries its own `[N]` marks-inline tag. Total per-question marks must
   match the header pill.

5. **Footer chip** ends with the version tag, e.g.
   `Unit A3 Practice v1.0`.

## Solutions file — non-negotiable structure

1. **Same scaffolding** as Practice (fonts, pills, parts) for visual parity.

2. **Engineering banner**: version + pair reference, plus a one-line key for
   the M1/A1/R1 chips used inside.

3. **Per-question solution block** uses the green `.solution` card with:
   - `answer-line` — one-line summary of the final answers (sub-part labelled).
   - `rationale` — the worked method, broken into `<h4>` sub-parts that match
     the Practice file's `(a) (b) (c) …`.
   - **Mark callouts** as small green chips (`.marks-call`) after each
     sub-part heading: `M1·A1`, `M1·M1·A1`, etc. Match the IB mark scheme.
   - **`.insight` block** at the end of each solution — one paragraph for the
     7-chaser: the underlying pattern, why this is the canonical IB approach,
     the trap that loses marks, or a generalisation. This is the
     differentiator from a vanilla mark scheme.

4. **Restate the prompt** at the top of each card (italicized, in `.prompt`)
   so the Solutions file can be read standalone.

5. **Footer chip**: `Unit <ID> Solutions v1.0 · Companion to Practice v1.0`.

## Build order

1. **Read the corresponding Study Guide** first. List every section.
   The Practice must cover every section; the Solutions must use only
   notation/results the Study Guide introduces.
2. **Draft the question list** before writing HTML — one line per question
   with paper, difficulty, topic, marks, and the *concept extension* it
   tests. Send to the user for review **only if scope is unclear**;
   otherwise proceed.
3. **Verify every answer mathematically** before writing the Solutions
   file. Compute concrete numbers, sanity-check ratios, plug back into
   identities. Solutions with arithmetic errors are worse than no Solutions.
4. **Write Practice first, Solutions second.** Sub-part labels and marks
   must match exactly between files.
5. **Run `scripts/validate.sh`** on both. The version-pair check fails
   if `dingrui:version` differs between the two files.

## Version bumps

- Bump to `v1.1` when both files get a substantive edit together (added
  questions, reworded solutions, refreshed scope).
- Patch ($v1.0 \to v1.0.1$ — three components allowed) is fine for typo-only
  fixes; bump on **both files** even if only one was edited.
- The version tag is the canonical pairing handle. Banners, footer chips,
  and the `dingrui:version` comment must agree.

## Cross-references

- Dual-goal contract for **Study Guides**: [`prompts/create-unit.md`](create-unit.md)
  (Practice doesn't follow the dual-goal contract — that's a Study Guide
  pattern. Practice serves *exam preparation*, not first-time learning.)
- Practice Questions conventions index: [`<Subject>/Practice Questions/README.md`](.)
- IB Math HL audit (active sprint, what's open):
  [`IB Math HL/AUDIT.md`](../IB%20Math%20HL/AUDIT.md)
- Reference build (the run that locked this template):
  IB Math HL Unit A3, commit `4d42faf`+ (`ib_math_hl_a3_practice` branch).
