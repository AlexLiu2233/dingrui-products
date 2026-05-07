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

**Status:** ✅ Closed 2026-05-04 (initial pass) + 2026-05-04 (Sprint 1-b
follow-up trim). **Tier:** P0. **Where:** all 22 study-guide widgets across
Units 1–7 (the previous estimate of 11 was incorrect — the actual count is
22).

**Resolution (initial pass):**

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

**Resolution (Sprint 1-b condensation pass):**

- **`impV0` slider trimmed from `impulse-widget`.** Initial velocity didn't
  affect the impulse $J$ or $\Delta v$ (it only fed the downstream $v_\text{f}$
  result card). Removed the slider, the v-final card, and the v0/vf
  references in `drawImpulse()`. The widget is now a clean
  3-slider × 3-result demo of $J = F \cdot \Delta t = \Delta p$. Removed
  control logged as DP-6.

**Deferred to a future "deep condensation" pass** (logged here so they
aren't lost):

| Widget | Candidate trim | Why deferred |
|---|---|---|
| `incline-widget` (U2) | `inc_m` slider | Acceleration is mass-independent under fixed $\mu$, so by rule 4 mass is gratuitous. But three result cards (mg sin θ, N, f_k) all depend on $m$ — trimming the slider would orphan them. Needs concept-recasting + card pruning, not a one-line trim. |
| `circular-widget` (U2) | `circ_m` slider | $a_c = v^2/r$ is mass-independent; only the $F_c$ card depends on $m$. Trimming requires removing $F_c$ and rewriting the concept comment from "centripetal force F = mv²/r" to "centripetal acceleration v²/r." |
| `ux-widget` (U3) | `uxXpos` test-point slider + 4 dependent result cards (U(x), KE, F(x), d²U/dx²) | Probe-only behaviour — useful for advanced students but orthogonal to the "where E intersects U(x)" core concept. The 4 cards plus the JS that updates them on Xpos change is a meaningful refactor. |
| `spring-energy-widget` (U3) | `sprF` friction slider + Friction Loss / Efficiency cards | Friction is conceptually orthogonal to PE→KE conversion. Three result cards depend on the slider. Same invasiveness as the others. |

These four trims should be done together in a single "widget-condensation"
sprint with explicit before/after screenshots, since each one changes the
widget's visible result-card layout and may need a brief tour-style note.

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

## Sprint 2 — Content Gaps (P0)

**Sprint 2 closed 2026-05-04** — both items landed on
`sprint2_content_gaps`. Resolved details preserved below.

### ~~P0-1 — Units 1–4 have zero ISEE worked examples~~

**Status:** ✅ Closed 2026-05-04. **Where:** `Unit_1_Kinematics.html`,
`Unit_2_Force_and_Dynamics.html`, `Unit_3_Work_Energy_Power.html`,
`Unit_4_Linear_Momentum.html`.

**Resolution:** added 2 ISEE FRQ-style worked examples to each of Units
1–4 (8 new examples total). Each follows the canonical
Identify / Set Up / Execute / Evaluate format and inherits the S1-A
hygiene rules from the start (acceptance grep targets all return zero).
Inserted at the end of the existing `unit-quiz` section, mirroring U5's
collected-FRQ pattern.

| Unit | ISEE-1 | ISEE-2 |
|---|---|---|
| 1 | Projectile range R(θ) + 45° optimization (calculus + numeric) | Non-constant $a(t) = 6t - 12$ — integrate to $v(t), x(t)$; total distance with sign change at $t = 4$ |
| 2 | Atwood with friction on the table — solve symbolically then numerically; tension by back-substitution | Block on incline with applied force up-slope — incline coordinates; verify above the slip threshold |
| 3 | Double-well $U(x) = x^4 - 8x^2 + 5$ — equilibria + stability via $d^2U/dx^2$; speed at $x=0$; turning points at $\pm 3$ | Spring → frictionless launch → frictioned ramp — full energy bookkeeping; check whether block slides back |
| 4 | 2-D perfectly inelastic collision — component-wise momentum conservation; COM-frame interpretation of KE loss | Ballistic pendulum + spring recoil — three steps (collision/swing/spring) with the right conservation law per step |

### ~~P0-2 — Unit 3 quiz is below the spec floor~~

**Status:** ✅ Closed 2026-05-04. **Where:**
`Unit_3_Work_Energy_Power.html` — was 5 quiz items, now 8.

**Resolution:** added 3 new MC items (Q6, Q7, Q8) covering:
- Q6: friction work as a non-conservative, sign-aware quantity ($W_f < 0$).
- Q7: instantaneous power $P = \vec F \cdot \vec v$ on an inclined car.
- Q8: turning points from $U(x) = E$ for a quadratic potential.
Quiz total updated from 5 to 8 (above the spec floor of 6). Bundled with
P0-1 since both touched the unit-quiz section.

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

## Sprint 4 — Practice Questions (in flight)

The `Practice Questions/` folder is being built out unit by unit. See
[`Practice Questions/README.md`](Practice%20Questions/README.md) for the
full conventions and per-unit index.

### Sprint 4 scope (Phase 1 closed 2026-05-04)

| ID | Item | Status |
|---|---|---|
| ~~S4-1~~ | Bring Unit 1 from 14 MC → 18 MC | ✅ Closed — added Q15 (1.4 relative motion, EASY), Q16 (1.2 sign analysis, MED), Q17 (1.5 simultaneous-fall conceptual, MED), Q18 (1.5 cliff-launch impact speed via energy, HARD). Difficulty mix balanced (4 EASY / 9 MED / 5 HARD). |
| ~~S4-2~~ | Draft Units 2–7 practice files | ✅ **Closed 2026-05-07** — all six units (U2 → U7) shipped at 18 MC + 4 FRQ each, full topic coverage, locked S4-3/S4-4 conventions throughout. Total: 126 MC + 28 FRQ across U1–U7. |
| ~~S4-3~~ | Decide answer-key format | ✅ Locked: **question-only**, no embedded answers. Matches AP Calculus house style (verified: AP Calculus practice files contain no `<details>` reveals or answer markers). If teacher answer keys are needed later, they ship as a separate `Unit_N_*_Answer_Key.html` companion file — deferred until classroom demand. |
| ~~S4-4~~ | Lock unit-typography convention | ✅ Locked: `\mathrm{...}` for unit composition, `~` for value/unit tying. Documented in `Practice Questions/README.md` "Locked conventions" section. |
| S4-5 | Render PDFs for distribution | **Open** — manual `chrome --headless --print-to-pdf=...`. Wait until S4-2 is complete so all units render together. |

**Earlier resolutions (Sprint 1-b polish, retained for traceability):**

- ~~Q11 had no correct answer~~ — fixed: choice (C) now reads $2 \pm \tfrac{2\sqrt{3}}{3}$ s, which is the actual MVT solution. Distractor (D) kept as a near-miss (factor-of-two slip).
- ~~Q13 distractor (D) was incoherent~~ — replaced "$\sqrt{25}$ m/s but pointing in $-\hat\jmath$" with `$\sqrt{18}~\mathrm{m/s}$` (the trap is computing $|\vec r(1)|$ instead of $|\vec v(1)|$). Choice (A) tightened to `$2~\mathrm{m/s}$` (y-component only trap).
- ~~README claimed "18 MC" but file had 14~~ — README now reads `18 MC + 4 FRQ ✓`.

### Sprint 4 — Phase 2 closed 2026-05-07

Per-unit build-out complete. Order shipped: **~~U2~~ → ~~U3~~ → ~~U4~~ → ~~U5~~ → ~~U6~~ → ~~U7~~**. Only S4-5 (PDF render) remains in the sprint.

**Unit 4 — Phase 2 (2026-05-07):**

- 18 MC items spanning all 4 sub-topics (4.1 momentum → 4.4 elastic/inelastic), with the locked S4-3/S4-4 conventions. Difficulty mix 4 EASY / 9 MED / 5 HARD.
- 4 FRQ items: variable-force impulse $F(t) = \alpha t$ with bag/dashboard reasoning (4.2), skater-recoil with relative-frame variant (4.3), 1-D head-on elastic collision with full derivation + COM verification (4.4), 2-D unequal-mass collision with elastic/inelastic classification + COM check (4.4). Picked deliberately to avoid duplicating the U4 study-guide ISEE examples (2-D perfectly-inelastic + ballistic-pendulum-with-spring-recoil).
- Bundled CSS update: practice files now use `clamp()` padding so layout fits narrow screens, stacks 2-column options on phones, and re-asserts `@page { size: letter }` inside `@media print` so print always defaults to letter regardless of browser-dialog quirks. Applied to U1–U4 in the same commit.

**Units 5/6/7 — Phase 2 (2026-05-07):**

- **U5 Torque & Rotational Dynamics (5.1 – 5.6):** Atwood with massive pulley + ladder-against-frictionless-wall ($\tan\theta = 1/(2\mu)$) + composite-rod $I$ + yo-yo $a = 2g/3$ (HARD); FRQs cover massive-pulley dynamics, beam-and-cable static equilibrium, pivoted composite rod (release from horizontal → vertical), and rolling cylinder on incline with $\mu_s$ derivation.
- **U6 Energy & Momentum of Rotating Systems (6.1 – 6.6):** Sphere/disk/hoop rolling race, person-walks-toward-axis $L$ conservation, geosynchronous orbital radius ($\approx 4.2 \times 10^4$ km), bound-orbit total energy $E = -GMm/(2r)$ (HARD); FRQs cover disk-on-disk inelastic collision with KE accounting, sphere rolling down incline with $\mu_s$ derivation, ballistic-pendulum-with-rod (bullet embeds at free end → max swing angle), and orbital-mechanics derivation + $\Delta E$ to raise orbit.
- **U7 Oscillations (7.1 – 7.5):** $x = A/\sqrt{2}$ for KE = PE, $v/v_\mathrm{max} = \sqrt{3}/2$ at $x = A/2$, physical-pendulum rod period $T = 2\pi\sqrt{2L/(3g)}$, "Both I and II" choice for $\tfrac{1}{2}kA^2 = \tfrac{1}{2}m\omega^2A^2$ (HARD); FRQs cover full mass-spring SHM characterization, phase-analysis of $x(t) = A\cos(\omega t + \phi)$, rod physical pendulum with small-angle vs. exact-energy comparison, and vertical mass-spring with new-equilibrium derivation + KE = 3PE position.
- All three files inherit the locked CSS contract (responsive screen + print-letter).

**Unit 2 — Phase 2 entry (2026-05-05):**

- 18 MC items spanning all 10 sub-topics (2.1 inertia → 2.10 Kepler), with the locked S4-3/S4-4 conventions (`\mathrm{...}` for units, no embedded answers, question-only).
- Difficulty mix 4 EASY / 9 MED / 5 HARD (matches Unit 1).
- 4 FRQ items: Atwood with table friction (2.2/2.4), incline with applied force + friction (2.6/2.4), linear drag derivation including ODE solution (2.5), and vertical-loop centripetal+energy problem (2.9).
- All AP-style: each MC labeled with topic and calculator/no-calc, each FRQ scaffolded into 4 sub-parts (a)–(d) with sized `.work` zones.

**Unit 3 — Phase 2 (2026-05-06):**

- 18 MC items spanning all 5 sub-topics (3.1 KE → 3.5 conservation of energy). Same locked conventions and difficulty mix.
- Concept coverage: $K = \tfrac{1}{2}mv^2$, work at an angle, average + instantaneous power, $U_s = \tfrac{1}{2}kx^2$, work-energy theorem with friction, $F = -dU/dx$, frictionless ramp speed, variable-force integral, equilibrium classification via $d^2U/dx^2$, spring launchers, instantaneous power on incline, conservative-vs-non-conservative classification, KE scaling, 2-D line integral $\int \vec F \cdot d\vec r$, constant-power kinematics, loop-the-loop minimum height, pump power $P = (dm/dt)\,gh$.
- 4 FRQ items: ramp + spring + friction energy bookkeeping (3.5), $U(x) = x^4/4 - 2x^2 + 3$ double-well analysis (3.4), variable friction coefficient $\mu_k(x) = 0.10 + 0.05x$ work integral (3.2), constant-power car ODE derivation $v = \sqrt{2Pt/m}$ (3.3).
- Inherits the pill-styling + spacing fix from `b789754` so the q-head pills render properly from the start.

---

## Cross-Unit Snapshot

| Unit | Sections | Widgets | ISEE | Flashcards | Quiz | h1 prefix | JSXGraph |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 2 | **2** ✓ | 8 | 10 | ✓ "Unit 1:" | — |
| 2 | 10 | 5 | **2** ✓ | 8 | 11 | **✗ missing** | — |
| 3 | 5 | 3 | **2** ✓ | 8 | **8** ✓ | **✗ missing** | — |
| 4 | 4 | 3 | **2** ✓ | 8 | 10 | ✓ "Unit 4:" | — |
| 5 | 6 | 4 | 8 blocks | 8 | 11 | ✓ "Unit 5:" | ✓ |
| 6 | 6 | 4 | 8 blocks | 8 | 11 | ✓ "Unit 6:" | ✓ |
| 7 | 5 | 1 + phase | 9 blocks | 8 | 10 | ✓ "Unit 7:" | ✓ |

`GENERATION_PROMPT.md` baselines: ≥2 widgets per unit (✓ all), 8+ flashcards
(✓ all), 6+ quiz items (✓ all units now), 2–3 ISEE worked examples (✓ all
units now).

---

## Known Infra / Tooling Items

### ~~I-1 — `scripts/validate.sh` is hard-coded for study-guide products~~

**Status:** ✅ Resolved 2026-05-04 (Sprint 4 Phase 1). The dark-mode check
in `scripts/validate.sh` now skips files whose path contains
`Practice Questions`. The `data-theme` check is preserved for all files
(both Physics and Calculus practice files should declare a theme — Physics
already has `data-theme="light"`; AP Calculus practice files genuinely
omit it, which is a separate bug in those files, not the validator).

The change is intentionally minimal — single conditional rather than a
new `--profile` flag — because there are only two profiles in play
(study guide vs. print practice) and a path-based heuristic is enough.
If a third product type appears, revisit.

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
| DP-6 | "Pre-loaded velocity" impulse widget — set initial velocity, watch how impulse adds to it | Stripped from `impulse-widget` per S1-B condensation | Useful for showing v_final = v_0 + J/m as a separate concept; doesn't fit the study-guide one-concept rule for the impulse widget |

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
