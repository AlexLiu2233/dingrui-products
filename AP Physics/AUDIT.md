# AP Physics C: Mechanics — Audit

Open punch list for the Mechanics study guides and practice questions, scored
against [`GENERATION_PROMPT.md`](GENERATION_PROMPT.md) and the AP CED for
AP Physics C: Mechanics.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "shooting for a 5" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only. Anything
that belongs in a richer interactive surface lives in the
[Digital Product Backlog](#digital-product-backlog) at the bottom of this file
and is **out of scope** until that product spins up.

Last reviewed: **2026-05-04** (post text/math + widget-philosophy directive).
Last reorganized: **2026-05-04**.

---

## Active Sprint — what we're working on now

**Sprint 1 closed 2026-05-04** — both items landed on `improve_AP_Physics`.
Resolved details preserved below for traceability; next up is Sprint 2.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S1-A**~~ | ~~Math/text hygiene pass in worked examples~~ | P0 | ✅ closed — see [details](#s1-a--mathtext-hygiene-in-worked-examples) |
| ~~**S1-B**~~ | ~~Apply Interactive Component Philosophy to study-guide widgets~~ | P0 | ✅ closed — see [details](#s1-b--apply-interactive-component-philosophy) |

Sprint 2 (P0-1 content gaps + P0-2 quiz floor) starts on the new
`sprint2_content_gaps` branch.

---

## Interactive Component Philosophy

**Status:** standing principle, locked 2026-05-04. All study-guide widget work
must conform; any deviation gets routed to the
[Digital Product Backlog](#digital-product-backlog).

### Rules

1. **Sliders only.** Study-guide widgets use HTML range inputs and a canvas/
   JSXGraph readout — nothing else. No drag-and-drop, no draw-on-canvas, no
   data-table entry, no multi-stage scenarios. If the interaction can't be
   expressed as "move slider, watch numbers/picture update," it belongs in the
   Digital Product, not here.
2. **One KEY thing per widget.** Each widget demonstrates exactly one canonical
   AP concept (e.g. "how launch angle trades off range vs. height"). The
   primary purpose of the slider is to **save the student from re-running the
   problem with different numbers** — not to teach a new concept.
3. **Crammer-usable, expert-rewarding.** A student who hasn't read the
   surrounding section should be able to drag a slider and see something
   meaningful. A student who has read it should be able to probe edge cases
   (e.g. "what happens to terminal velocity as $b \to 0$").
4. **Strip gratuitous sliders.** Any slider that doesn't change the *concept*
   the widget is demonstrating is noise. Examples: an adjustable $g$ slider on
   the Inclined Plane Explorer (the concept is the angle/friction trade-off,
   not "what if Earth had different gravity"); an adjustable mass slider on
   the projectile widget (mass doesn't matter for projectile motion in
   vacuum — including the slider implies it does).
5. **No tutorial chrome.** No "click here to start," no progress bars, no
   stepper UIs. Slider → result. That's the contract.

### What this rules OUT for the study guide

- Lab-data widgets (table-of-readings + line-fit)
- Free-body-diagram drawing/grading
- Multi-stage scenarios ("now release the block… now reverse the spring")
- Quiz-grading widgets that go beyond the existing MC `<div class="quiz">`
  pattern
- Anything with `localStorage` state

These are good ideas — they live in the [Digital Product Backlog](#digital-product-backlog).

---

## Sprint 1 — Active Items (detail)

### S1-A — Math/text hygiene in worked examples

**Status:** ✅ Closed 2026-05-04. **Tier:** P0. **Where:** all units,
concentrated in Units 5/6/7 worked examples (the units with the most
`step-math` blocks).

**Resolution:** all four grep acceptance criteria return zero hits.

- 9 nested `step-math > step-text` instances unwrapped (U5/6/7).
- 7 unicode-in-prose Greek/subscript instances wrapped in `$…$` (e.g.
  `y₀` → `$y_0$`, `r₁` → `$r_1$`, `θ` → `$\theta$`).
- 3 bare-LaTeX-in-prose instances given proper `$…$` delimiters
  (e.g. `Use T = 2\pi\sqrt(m/k)` → `Use $T = 2\pi\sqrt{m/k}$.`).
- 10 instances of `\text{X·Y}` (literal middle-dot inside `\text{}`)
  rewritten as `\text{X}\cdot\text{Y}`. The unicode `·` rendered visually
  but its MathML annotation encoded as `\cdotp`, which leaked into
  copy-paste output and looked like a render bug. Affected: U2 (`kg·m`,
  `kg·m/s`, `N·m^2/kg^2` — including the gravitational-constant box at
  line 1095), U4 (`N·s`, two `kg·m/s`), U5 (`N·m`), U6 (three `kg·m^2…`).
- Sweep extended to U1–4 for all patterns (no additional hits beyond the
  ones called out above).

**New rule for future authors:** never put unicode `·` inside `\text{…}`.
Use math-mode `\cdot` with `\text{}` alternation, e.g. `\text{N}\cdot\text{m}`.
Plain unicode `·` is fine in HTML prose, table cells, and result-card
labels — only the `\text{}` context is the bug.

**Symptom:** prose and unicode are leaking into containers that the CSS styles
as display math, producing visually awkward "math-mode prose" where the font,
spacing, and alignment fight the content.

**Concrete patterns to fix** (grep targets — current counts on
`improve_AP_Physics`):

1. **`step-text` nested inside `step-math`** — the `step-math` div is styled
   for centered LaTeX display; nesting prose inside it inherits that styling.
   Replace with sibling `step-text` + `step-math` blocks, or promote the inner
   prose to `step-text` and drop the outer wrapper.
   - `Unit_7_Oscillations.html:345, 355, 414–416, 726, 737`
   - `Unit_5_Torque_and_Rotational_Dynamics.html:1312–1315`
   - `Unit_6_Energy_and_Momentum_of_Rotating_Systems.html:1150, 1155, 1347`
2. **Plain-unicode math in `step-label`** — primes, subscripts, and Greek
   rendered as raw glyphs (`y'`, `y₀`, `r₁`) instead of KaTeX. Looks like a
   different font and breaks dark-mode color inheritance.
   - `Unit_7_Oscillations.html:624` — `Substitute y' = y − y₀`
   - `Unit_6_Energy_and_Momentum_of_Rotating_Systems.html:1380, 1384` —
     `Circular speed at r₁`, `Transfer orbit speed at r₁`
3. **Mixed prose+math inside display-math containers** — `$x = 0.20\;\text{m}$`
   stuffed into a `step-math` block reads as left-aligned italic prose because
   the surrounding context expects centered display math.

**Fix recipe** (apply uniformly):

- If a div needs both prose and math: it's `step-text`, with inline `$…$`.
- If a div is centered display math only: it's `step-math`, with `$$…$$` and
  no nested divs.
- Anywhere a label/heading mentions a variable: wrap the variable in `$…$`
  (so `Substitute y' = y − y₀` becomes `Substitute $y' = y - y_0$`).

**Acceptance criteria:**

- `grep -rn 'step-math"><div class="step-text"' "AP Physics/Study Guides/"`
  returns 0 hits.
- No `step-label` or `step-text` content contains unicode subscripts
  (`₀`-`₉`), unicode superscripts (`⁰`-`⁹`), Greek letters, or primes outside
  KaTeX.
- Visual diff via `scripts/screenshot.sh` shows no regressions in non-affected
  examples.

### S1-B — Apply Interactive Component Philosophy

**Status:** ✅ Closed 2026-05-04. **Tier:** P0. **Where:** all 22 study-guide
widgets across Units 1–7 (the previous estimate of 11 was incorrect — the
actual count is 22).

**Resolution:**

- **Slider-only confirmed.** All 22 widgets already use `<input type="range">`
  exclusively — no other input controls in any widget.
- **Concept comments added** to all 22 widget container divs (one-line HTML
  comment immediately above the `formula-explorer` div).
- **`g` slider trimmed from `incline-widget`** (was `inclineExplorer`); $g$
  hard-coded to 9.8 in the JS update function. Removed control logged as
  DP-4.
- **P1-3 bundled in:** all 11 `*Explorer` IDs renamed to `*-widget` —
  `fmaExplorer → fma-widget`, `inclineExplorer → incline-widget`,
  `springExplorer (U2) → spring-force-widget`, `dragExplorer → drag-widget`,
  `circExplorer → circular-widget`, `workExplorer → work-widget`,
  `uxExplorer → ux-widget`, `springExplorer (U3) → spring-energy-widget`,
  `impulseExplorer → impulse-widget`, `collisionExplorer → collision-widget`,
  `energyExplorer → energy-widget`. None of the renamed IDs were referenced
  in JS or CSS, so the rename was contained to the container `id=` attribute.

**Why now:** the philosophy was just locked (see above). Existing widgets were
built before it; some violate rules 1, 2, or 4.

**Audit pass required** — for each widget, classify as one of:

- **KEEP** — already philosophy-conformant, no changes.
- **TRIM** — widget is fundamentally fine but has gratuitous sliders or
  controls; strip them.
- **REWRITE** — widget violates rule 1 (not slider-only) or rule 2 (no single
  clear concept). Rewrite to a slider-only one-concept variant. If the
  original interaction was genuinely valuable, log the idea in the
  [Digital Product Backlog](#digital-product-backlog) before deleting.
- **DEFER** — widget concept doesn't fit the philosophy at all; remove from
  study guide, log in backlog.

**Known offenders to seed the pass** (not exhaustive — full audit pending):

- `Unit_2_Force_and_Dynamics.html` Inclined Plane Explorer (`inclineExplorer`,
  line 1219): has a `g` slider that doesn't serve the concept. **TRIM.**
- All `…Explorer` IDs in Units 2/3/4 should also be renamed to `…-widget` per
  P1-3 — bundle with this pass, since we're touching the markup anyway.

**Acceptance criteria:**

- Every study-guide widget has a one-line "concept demonstrated" comment in
  the HTML next to the widget's container div.
- No widget uses any input control other than `<input type="range">` and the
  existing reset/play buttons used by the kinematics canvas.
- Every removed control or rewritten widget has a corresponding entry in the
  Digital Product Backlog so the idea isn't lost.

---

## Sprint 2 — Content Gaps (P0, queued)

### P0-1 — Units 1–4 have zero ISEE worked examples

**Where:** `Unit_1_Kinematics.html`, `Unit_2_Force_and_Dynamics.html`,
`Unit_3_Work_Energy_Power.html`, `Unit_4_Linear_Momentum.html`.
**Status:** still open (Units 5/6/7 have 8/8/9 ISEE blocks; Units 1–4 have 0).
**Spec:** `GENERATION_PROMPT.md` §6.9 / §7 — every unit's quiz section should
include 2–3 ISEE FRQ-style worked examples.
**Why it matters:** the ISEE block is the primary FRQ-prep surface; Units 1–4
are the most-tested content (Unit 2 alone is 20–25% of the exam).
**Suggested scenarios:**

- Unit 1: 2-D projectile range/launch-angle FRQ; non-constant-$a$ integration
  problem ($a(t)$ given).
- Unit 2: Atwood with friction; block-on-incline with applied force at angle;
  drag terminal-velocity ramp-up.
- Unit 3: Variable-force work integral with $U(x)$ → turning points; spring +
  ramp + friction energy bookkeeping.
- Unit 4: 2-D inelastic collision with COM frame; ballistic pendulum + spring.

**Cross-cutting note:** any new ISEE example written in Sprint 2 must follow
the S1-A hygiene rules from the start (no nested step-text-in-step-math, etc.).

### P0-2 — Unit 3 quiz is below the spec floor

**Where:** `Unit_3_Work_Energy_Power.html` — 5 quiz items vs. spec floor of 6.
**Status:** still open.
**Why it matters:** Unit 3 has the broadest energy-bookkeeping toolkit and is
chained into Units 4/6/7. Five items is too thin to cover work integrals,
$U(x)$, conservative-vs-non-conservative, and power.
**Fix:** add 3–5 MC items plus the ISEE examples from P0-1 (do them together).

---

## Sprint 3 — Consistency & Polish (P1, queued)

### P1-1 — Units 2 & 3 missing "Unit N:" prefix in `<h1>`

**Where:**

- `Unit_2_Force_and_Dynamics.html:715` — `<h1>Force & Translational Dynamics</h1>`
- `Unit_3_Work_Energy_Power.html:589` — `<h1>Work, Energy, & Power</h1>`

**Spec:** `GENERATION_PROMPT.md` §6.6 — hero `<h1>` is `Unit {N}: {Title}`.
Units 1, 4, 5, 6, 7 follow this pattern. **Fix:** prepend `Unit 2: ` and
`Unit 3: ` respectively.

### P1-2 — Hero chip schema drift

**Spec:** `GENERATION_PROMPT.md` §6.6 says hero chips are `chip-maroon`
(sections), `chip-green` (widgets), `chip-gold` (AP exam weight).
**Observed:** units carry chips like "10–15% Exam, ~14–19 Periods, 5 Topics"
— the order, content, and color mapping vary across units.
**Fix:** lock canonical schema (recommend keeping current "Topics / Periods /
Exam %" content but standardizing order and color across all 7 units), and
update `GENERATION_PROMPT.md` §6.6 to match. **Bundle with P1-1** since both
touch the hero block.

### ~~P1-3 — Widget naming conventions diverge~~

**Status:** ✅ Closed 2026-05-04 (bundled into S1-B). All 11 camelCase
`*Explorer` IDs renamed to kebab-case `*-widget`. Canvas-name parity (e.g.
`shmCanvas`) is *not* in scope here — those are sub-IDs not container IDs.

### P1-4 — Unit 1 free-fall widget vs. canvas naming

**Observed:** Unit 1 `freefall-widget` is fine, but `projCanvas` (not
`projectileCanvas`) breaks the `{shortname}Canvas` rule. **Fix:** rename
`projCanvas` → `projectileCanvas` (one ID, one CSS selector, one JS
reference).

### P1-5 — JSXGraph used in 5/6/7 only

Not a defect — §3 lists it as optional — but worth flagging that any future
"add an interactive proof" task should consider adding JSXGraph to Units 1–4
where appropriate. **Action:** track as opportunity, not a blocker.

---

## Practice Questions Status

The `Practice Questions/` folder currently contains
`Unit_1_Kinematics_Practice_Problems.html` (rough draft) plus a README. See
[`Practice Questions/README.md`](Practice%20Questions/README.md). Target:
AP-style MC + FRQ for Units 1–7, mirroring the AP Calculus practice question
shape (HTML + print PDF, with `EASY/MEDIUM/HARD` and `Calculator/No
Calculator` pills). **Schedule:** kick off after Sprint 2 closes (so new
practice questions inherit the current ISEE template and hygiene rules).

---

## Cross-Unit Snapshot

| Unit | Sections | Widgets | ISEE | Flashcards | Quiz | h1 prefix | JSXGraph |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 2 | **0** | 8 | 10 | ✓ "Unit 1:" | — |
| 2 | 10 | 5 | **0** | 8 | 11 | **✗ missing** | — |
| 3 | 5 | 3 | **0** | 8 | **5** | **✗ missing** | — |
| 4 | 4 | 3 | **0** | 8 | 10 | ✓ "Unit 4:" | — |
| 5 | 6 | 4 | 8 blocks | 8 | 11 | ✓ "Unit 5:" | ✓ |
| 6 | 6 | 4 | 8 blocks | 8 | 11 | ✓ "Unit 6:" | ✓ |
| 7 | 5 | 1 + phase | 9 blocks | 8 | 10 | ✓ "Unit 7:" | ✓ |

`GENERATION_PROMPT.md` baselines: ≥2 widgets per unit (✓ all), 8+ flashcards
(✓ all), 6+ quiz items (✗ Unit 3 has 5), 2–3 ISEE worked examples (✗ Units
1–4 have 0).

---

## P2 — Future Work (Study Guide)

### P2-1 — AP Physics C: E&M expansion

`GENERATION_PROMPT.md` §13 lists Mechanics only. The eventual E&M build-out
(Electrostatics → Conductors/Capacitors/Dielectrics → Currents/Circuits →
Magnetic Fields → Electromagnetism) would mirror this folder structure under
a sibling `AP Physics CM/` and `AP Physics CEM/` split, or stay merged with
a clearer per-exam scope chip. Decision pending.

### P2-2 — Cross-unit "spaced-review" deck

Calculus has no equivalent yet. A single HTML "all-units flashcard cram" page
that pulls from each unit's flashcards would be a strong pre-exam product.

---

## Digital Product Backlog

Ideas captured here are explicitly **out of scope** for the study guide. They
live here so they don't get lost when the richer interactive product spins
up. Anything the Interactive Component Philosophy excludes belongs here.

> **Process:** when a widget is rewritten or trimmed under S1-B, log what was
> removed/simplified here with a one-liner — that's the seed for the next
> product.

| ID | Idea | Source | Notes |
|---|---|---|---|
| DP-1 | Lab/data-table widget — given a table of $(t, x)$, fit a line to find $v$ | Migrated from previous P2-3 | JSXGraph regression; generalizes across Units 1, 4, 7 |
| DP-2 | Free-body-diagram constructor with grading | Implied by Unit 2 needs | Drag-and-drop force vectors onto a body, check sum |
| DP-3 | Multi-stage scenario player ("release block → spring compresses → block leaves spring") | Implied by Unit 3/4 energy bookkeeping | State machine + timeline scrubber |
| DP-4 | Adjustable-$g$ "what if Earth had different gravity" sandbox | Stripped from Inclined Plane Explorer per S1-B | Genuinely interesting for intuition; doesn't fit study-guide one-concept rule |
| DP-5 | Interactive FRQ rubric trainer (student types answer, rubric grades it) | Net-new | Pairs naturally with the Practice Questions product |

*Add new entries with auto-incremented `DP-N` ID. When a backlog item is
picked up by the Digital Product team, mark it `→ in flight: <link>` here
rather than deleting — preserves the lineage.*

---

## How to Update This File

When closing a sprint item, mark it with `~~strikethrough~~` and append
`**Resolved:** {commit-sha} — {one-line note}`. When an entire sprint clears,
collapse the section into a single "Sprint N closed as of {date}" line and
promote the next sprint up.

When the Interactive Component Philosophy needs revision, edit it in place
and bump the "locked" date — don't fork it into a separate doc.

When a widget gets rewritten or trimmed, **log the removed interaction in the
Digital Product Backlog** before deleting code. The backlog is the only
canonical home for ideas the study guide won't carry.
