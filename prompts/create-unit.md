# Create New Unit

You are creating a new Dingrui Scholars HTML product unit.

## Inputs
- **Subject**: {{SUBJECT}}
- **Unit Number**: {{UNIT_NUMBER}}  (or letter, e.g. `B` for IB Math HL)
- **Unit Title**: {{UNIT_TITLE}}
- **Topics**: {{TOPICS_LIST}}

## The dual-goal contract (READ FIRST)

Every study guide must serve **two students at once**, in the same file:

1. **The crammer.** A student opening this the night before the exam, who
   needs a last-ditch pass. They should be able to skim the page top-to-bottom
   and walk into the exam with the formulas, the canonical worked examples,
   and the question patterns the exam actually rewards. They should never have
   to read a derivation to find a formula.
2. **The 5-chaser.** A student studying in depth, going for a top score (a 5
   on AP, a 7 on IB). They should find the *why* — the derivation, the
   subtleties, the edge cases, the proof structure — without leaving the page.

Concretely, this means every section should layer:

- **A cheat-sheet element at the top** (key-formula card, "what you must
  know" callout, or a one-line summary box) that the crammer can lift in
  under a minute.
- **A worked example or two** demonstrating the canonical exam application
  — these double as both crammer fuel and depth practice.
- **A "going deeper" / proof / derivation section** (clearly labeled, often
  in a `box--proof` or expandable `<details>`) that the crammer can skip and
  the 5-chaser can dive into.
- **Quiz items** that mix recall (crammer-pass) with synthesis (5-chaser).

If a section reads as "just notes," it serves neither student well. Either
crystallize the takeaway for the crammer, or expand the derivation for the
5-chaser — usually both.

## Instructions
1. Read `rag/style-guide.md` for design tokens, layout patterns, and required
   sections.
2. Read `rag/template.html` for the base HTML structure.
3. **Read an existing unit in the same subject folder** for tone, depth,
   structural conventions, and component patterns. The new unit must feel
   like a sibling of the existing units — same hero schema, same TOC
   sidebar, same quiz markup, same flashcard markup, same dark-mode wiring.
4. Check for a subject-level `AUDIT.md` (e.g. `AP Physics/AUDIT.md`,
   `IB Math HL/AUDIT.md`) — that is the master tracker. Honor any
   in-flight sprint conventions or locked decisions documented there.
5. Generate the full self-contained HTML file with:
   - All sections from the topic list, each satisfying the dual-goal contract
     above
   - A "key formulas" cheat-sheet block per section (crammer-targeted)
   - 1-2 worked examples per major section with KaTeX math
   - A "going deeper" / proof block per major section where applicable
     (5-chaser-targeted)
   - 2-3 quiz questions per major section, mixing recall and synthesis
   - Flashcard deck (8+ cards) covering the unit's must-know facts
   - Proper dark mode support
   - Print-friendly layout
6. Save to `{{SUBJECT}}/Unit_{{UNIT_NUMBER}}_{{UNIT_TITLE_SNAKE}}.html`.
7. Run `bash scripts/validate.sh` on the output.
8. If a subject-level `AUDIT.md` exists, update it to reflect the new unit
   (cross-unit snapshot table, sprint status, etc.).

## Subject-specific notes

### IB Math AA HL
- Units are letters, not numbers: `Unit_A_*`, `Unit_B_*`, `Unit_C_*`,
  `Unit_D_*`, `Unit_E_*` (Topics 1–5: Number & Algebra, Functions,
  Geometry & Trigonometry, Statistics & Probability, Calculus).
- Grade scale is 1–7. The "cram → pass" target is roughly a 4; the
  "depth → top mark" target is a 7. The dual-goal contract phrases this as
  "last-ditch pass" vs. "going for a 5" by analogy with the AP scale, but
  for IB write the depth tier as "going for a 7."
- HL-only content (vs. SL) should be flagged inline — a small chip or
  callout — so an SL student knows what they can skip.
- Calculator paper vs. non-calculator paper: where a topic has a clear
  calculator/no-calc split (e.g. statistics distributions), note it in the
  section header.

### AP Physics C / AP Calculus BC / AP CSA
- Units are numbered: `Unit_N_*`. Match the existing per-subject
  conventions for hero chips, section anchors, and worked-example schema.

## Quality Checks
- Cheat-sheet element present and lift-able in <1 minute per section
- Going-deeper / proof block present where the topic has one
- All KaTeX delimiters properly escaped (`$…$` inline, `$$…$$` display);
  no unicode subscripts/superscripts/Greek inside `\text{}`
- Quiz answers are hidden until revealed (or scored, per the existing
  in-subject pattern)
- Mobile responsive at 375px+
- Dark mode toggling works (use `[data-theme="dark"]` overrides only;
  no hard-coded light-only colors)
- Print preview is clean (no clipped equations, no orphaned headers)
- No broken internal anchors (every TOC link resolves to an `id=`)
