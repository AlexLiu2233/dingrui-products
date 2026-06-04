# High School Physics — Audit

Open punch list for the High School Physics product, scored against the
canonical generation prompt ([`prompts/create-unit.md`](../prompts/create-unit.md))
plus the subject-specific spec at
[`rag/subjects/high_school_physics.md`](../rag/subjects/high_school_physics.md).

**Strategic posture (locked 2026-05-31):** One topic-organised
study-guide set serving both **US NGSS HS-PS (Physical Science)** —
primary commercial target — and the top three Canadian provincial
curricula (Ontario, BC, Alberta) implicitly through universal topic
coverage. Genuine curriculum differences are called out *inside* each
guide via Syllabus Map and Syllabus Note callouts, not by forking
content. See spec for details.

> **US standard is NGSS, not Common Core.** Common Core is Math/ELA
> only and has no science strand. US physics content maps to NGSS
> **HS-PS1..HS-PS4** performance expectations. Never label a US physics
> claim "Common Core."

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / NGSS / AP-feeder / provincial-exam (ON / BC / AB Diploma) use
  of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity
  but not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product first;
Practice Questions and Solutions land per the spec's bilingual-from-start
contract. Items that don't fit those surfaces live in the
[Digital Product Backlog](#digital-product-backlog).

Last reviewed: **2026-06-01** (**all 12 Study Guides shipped** —
bilingual from start, source-grounded, validate PASS — on branch
`hs_physics_studyguides`, awaiting review/FF to main. Practice +
Solutions are the next wave.)

---

## Active Sprint — what we're working on now

### Sprint — Deployment-Readiness Audit — 2026-06-03 (findings; audit-only)

**✅ RESOLVED 2026-06-03 (fix sprint on `hs_stem_complete`):** D1 dead-toggle + D4 localStorage normalized across all 66 SGs (`1b749f3`); A6 CJK-in-`	ext{}` cleared in all 25 affected SGs (`4ff2b62`, `5a7c0c3`); P2 favicon `../LOGO.png`→`../../LOGO.png` (`e580250`); B3 going-deeper added to Chem U4/U5 (`b644a18`). Findings below retained as the audit record.


Scored all 12 Study Guides against `rag/study-guide-audit-checklist.md`
Sections **A / B / D** with the HS-STEM adjustments from
`rag/hs-stem-deploy-audit.md` (E3 + C1 + interactive/slider checks
EXCLUDED — interactivity + figures scrapped 2026-06-03; "no stray
visual/JS" sweep ADDED; Section D ACTIVE, D1 a hard gate). **Audit-only —
no `.html` edited.** Findings to be fixed in a follow-up sprint.

**Mechanical sweep (all 12):**
- **A8** `validate.sh` exits 0 on all 12 (odd-`$` WARN benign, not logged). **PASS.**
- **D1** `data-lang` parity EN==ZH on all 12 (351–411 spans/file). **PASS.**
- **No stray visual/JS:** 0 `<svg>` / `<img>` / `<canvas>` / chart in any
  file (scrapped-SVG trial confirmed fully removed); only 3 `<script>`
  per file = 2 KaTeX 0.16.9 CDN + 1 inline (quiz/toggle/scrollspy). **PASS.**
- **Feeder hrefs:** all `../../` feeders resolve (AP Physics U1–U7, AP
  Calculus U2, HS Math U7). **PASS (P1 link integrity clean).**
- **Chrome:** dark-mode block, `@media print`, `max-width: 600px`,
  `footer-wrap`, sticky sidebar, progress bar, `checklistUl` readiness,
  14 flashcards, 4-region syllabus map (US NGSS / ON / BC / AB),
  honors-flag, region/paper chips — present and uniform on all 12. **PASS.**
- **A1** title = HS no-colon form on all 12. **PASS.** **A2/A3** tokens +
  DM Serif Display + PingFang SC CJK fallback present. **PASS.**
- **A7** TOC anchors all resolve (the single flagged `#${e.target.id}` is
  a JS scrollspy template literal, not a TOC link — false positive). **PASS.**
- **B1/B2/B6** dual-goal: cheat-sheet markers, 12 worked-example labels/file
  (visible, not collapsed), 2–7 `<details>` going-deeper blocks/file. **PASS.**

**Findings:**

| Finding | File: gap | Tier | Status |
|---|---|---|---|
| **D4-1** | ALL 12 SGs: `toggleLang()` writes `localStorage.setItem('lang', …)` and the page reads `localStorage.getItem('lang')` on load to restore ZH. Violates the locked rule (2026-05-21) that `toggleLang()` must NOT touch localStorage and every page defaults to English on load. | P0 | Open |
| **A6-1** | `Unit_3_Work_Energy_and_Power`: 13 CJK chars inside `\text{}` in math (e.g. `P_\text{有用输出}`, `P_\text{总输入}`) — ZH spans only; renders with fallback glyphs / breaks subscript layout. Move Chinese outside the math. | P0 | Open |
| **A6-2** | `Unit_7_Light_and_Geometric_Optics`: 14 CJK chars inside `\text{}` (e.g. `n_{\text{真空}}`, `\lambda_{\text{介质}}`) — ZH spans only. | P0 | Open |
| **A6-3** | `Unit_11_Thermodynamics_and_Heat`: 13 CJK chars inside `\text{}` (e.g. `\text{水}`, `\text{失}`, `\text{得}`) — ZH spans only. | P0 | Open |
| **A6-4** | `Unit_12_Modern_and_Nuclear_Physics`: 2 CJK chars inside `\text{}` (`\text{高}`, `\text{低}`) — ZH spans only. | P0 | Open |
| **A6-5** | `Unit_5_Circular_Motion_and_Gravitation`: 1 CJK char inside `\text{}` (`\text{常数}`) — ZH span only. | P0 | Open |

**Overall verdict:** 12/12 validate clean, EN==ZH parity holds, links/chrome/
dual-goal/visual-policy all PASS. **Two blockers stand between the corpus and
deploy:** (1) a systemic **D4** localStorage-lang regression in all 12 files
(must default to English on load), and (2) **A6** CJK-in-`\text{}` math hygiene
in 5 files (broken subscript rendering in ZH mode). Both are mechanical,
small-diff fixes. **NOT deploy-ready until D4-1 + A6-1..5 close;** the other
seven SGs (U1, U2, U4, U6, U8, U9, U10) are clean apart from the shared D4-1.

### Sprint 3 — Practice + Solutions wave — **PLANNED (not started)** — promotes DP-1

> **Status: QUEUED.** Playbook authored + committed (`prompts/create-hs-practice-and-solutions.md`,
> `281d8b7` on branch `hs_physics_practice`). **No P+S `.html` built yet** — this is the
> plan only, awaiting the user's go. Physics is the **first STEM subject taken end-to-end**;
> it locks the P+S template the other 4 STEM subjects (Chem/Bio/CS/Math-retro) will copy.

**Goal.** 12 bilingual **Practice + Solutions** pairs (24 files), one per shipped Physics
Study Guide — the exam-prep companion to each SG. Locked HS contract (see playbook): EASY-MED-HARD
mix (~4:7:4, leans MED), **3 Parts by response type** (I Short Response · II Extended Response+Honors ·
III Modeling/Applied), **US/ON/BC/AB region chips** with the **AB Diploma** style as the standardized
hook (Physics 30), gold honors stream, **bilingual EN==ZH from the start** (exit gate), no-colon
topic-only titles, `v1` / `HS-Phys-<N>` version-pair tags, **copy-then-edit** from the HS Math Unit 1 pair.

**Per-pair spec.** ~10–14 questions, **~80 marks** (Parts I:II:III ≈ 25:30:25); every section of the
companion SG covered by ≥1 question; **`.insight` block on every solution** (the differentiator from a
vanilla answer key); **answers verified mathematically — units + numbers — before the Solutions file is
written.** CS would use `<pre><code>` not KaTeX, but that is a later subject; Physics is all KaTeX `$…$`.

**Work list (12 pairs).** File stem = companion SG stem; pair-key `HS-Phys-<N>`.

| N | Topic (pair-key) | Region-fit + emphasis notes (honor the SG's syllabus crosswalk — do NOT fake region chips) |
|---|---|---|
| 1 | Kinematics `HS-Phys-1` | **Template lock.** All 4 regions; AP Phys 1-feeder FRQ + AB Diploma. 1D/2D, graphs, projectiles. |
| 2 | Forces & Newton's Laws `HS-Phys-2` | All regions; FBD-heavy FRQ; core to every course. |
| 3 | Work, Energy & Power `HS-Phys-3` | All regions; energy-conservation modeling in Part III. |
| 4 | Momentum & Collisions `HS-Phys-4` | All regions; 1D/2D collisions; impulse FRQ. |
| 5 | Circular Motion & Gravitation `HS-Phys-5` | All regions; **honors** depth (Kepler, orbital). |
| 6 | Waves & Sound `HS-Phys-6` | All regions; superposition, resonance. |
| 7 | Light & Geometric Optics `HS-Phys-7` | **Thin in NGSS/AB** per SG note → lean ON/BC chips; honors for thin-lens algebra. |
| 8 | Electrostatics & Electric Fields `HS-Phys-8` | All regions; Coulomb / field FRQ. |
| 9 | Current Electricity & Circuits `HS-Phys-9` | **DC circuits thin in NGSS/AB** per SG → lean ON/BC; Kirchhoff honors. |
| 10 | Magnetism & EM Induction `HS-Phys-10` | **AB Phys 30 strong (Diploma hook)**; **honors** for induction/Faraday. |
| 11 | Thermodynamics & Heat `HS-Phys-11` | **Absent from AB Physics** per SG → drop AB chip; honors for gas-law/PV work. |
| 12 | Modern & Nuclear Physics `HS-Phys-12` | **AB Phys 30 strong (Diploma hook)**; honors for mass-energy/decay. |

**Sequence (review-then-merge cadence locked — nothing merges without user approval).**
1. **Lock Unit 1 (Kinematics, `HS-Phys-1`)** as the STEM template — full build, answers verified,
   per-pair gate green. **User reviews the locked pair.**
2. **Waves of ~4 Sonnet subagents** (`model: sonnet`), copy-then-edit from the *locked Physics Unit 1*
   (not Math) once it exists; each agent reads its companion SG + the Unit 1 pair, transforms, runs the
   per-pair gate. Commit per wave so an API outage costs ≤ one wave: **Wave A** (2,3,4,5) · **Wave B**
   (6,7,8,9) · **Wave C** (10,11,12).
3. `python scripts/build-index.py` (surface Practice cards) → review → FF `hs_physics_practice` →
   `preview` → `main`.

**Per-pair gate (before each commit).** `validate.sh` PASS on both files · EN span count == ZH on both ·
leftover-grep ≈ 0 (no Math-Unit-1 terms `linear|slope|intercept|斜率|系统`) · per-question marks sum to the
header pill · `pair-key` + `version` agree across banner / footer chip / `dingrui:` comment · dash sweep
per `_tone.md` (math operators exempt).

**Exit criteria.** 24 files validate clean; EN==ZH everywhere; all 12 SG section-lists covered; answers
verified; `build-index.py` regenerated with Practice cards surfacing EN+ZH; AUDIT + `STATUS.md` +
`project_hs_stem_program` memory updated; then FF to preview → main.

---

### Sprint 1 — source-grounding + 12 bilingual Study Guides — **CLOSED 2026-06-01** (branch `hs_physics_studyguides`, awaiting FF to main)

**Shipped:** all 4 curricula source-grounded (NGSS HS-PS, ON SPH3U/4U,
BC Physics 11/12, AB Physics 20/30 — extracts + cached PDFs in
`rag/sources/`), Unit 1 Kinematics drafted as the bilingual template
lock, then Units 2-12 bulk-drafted via Sonnet **copy-then-edit**
subagents (cp the locked template, transform per-section — avoids the
32k single-write cap that broke earlier from-scratch attempts). All 12
SGs: ~1070-1150 lines, balanced EN/ZH spans, validate PASS, syllabus-maps
cite real codes per curriculum. Divergence syllabus-notes added where a
curriculum lacks a topic: Optics (U7) + DC Circuits (U9) absent from
NGSS/AB; Thermodynamics (U11) absent from AB Physics 20/30.

| Unit | Topic | Spans (EN=ZH) |
|---|---|---|
| 1 | Kinematics (template) | 433 |
| 2 | Forces and Newton's Laws | 457 |
| 3 | Work, Energy and Power | 415 |
| 4 | Momentum and Collisions | 455 |
| 5 | Circular Motion and Gravitation | 416 |
| 6 | Waves and Sound | 440 |
| 7 | Light and Geometric Optics | 432 |
| 8 | Electrostatics and Electric Fields | 430 |
| 9 | Current Electricity and Circuits | 405 |
| 10 | Magnetism and Electromagnetic Induction | 459 |
| 11 | Thermodynamics and Heat | 461 |
| 12 | Modern and Nuclear Physics | 448 |

**Next:** build-index + landing-page tier integration (surface the 12
cards) ✅ done 2026-06-01 (`d52bf1a`, live on main). Then the visual-
improvement sprint below, then the Practice + Solutions wave.

### Sprint 2 — static visual upgrade — **SCRAPPED 2026-06-03**

**Scrapped.** A static inline-SVG trial on Unit 1 Kinematics produced figures
that were not accurate / high-quality enough; Manim/video conflicts with the
static self-contained constraints (and ffmpeg/LaTeX aren't available). In-guide
figures are dropped — guides stay prose + KaTeX. Superseded by the
**HS STEM Deployment-Readiness Audit** sprint (see
[`rag/hs-stem-deploy-audit.md`](../rag/hs-stem-deploy-audit.md)). The original
visual punch list is retained below only as historical reference.

#### (historical) original visual punch list

Per the [Visuals policy](../prompts/create-unit.md) locked 2026-06-01:
add a **clear static visual** (inline SVG / pure CSS — **no interactive /
JS-driven widgets**) wherever a topic is graph- or diagram-based. The
12 SGs currently lean on prose + KaTeX; these visuals materially aid
comprehension. Per-unit punch list (tier P1):

| Unit | Visual to add |
|---|---|
| 1 Kinematics | position-time & velocity-time graphs; projectile parabola |
| 2 Dynamics | free-body diagrams; inclined-plane force decomposition |
| 3 Energy | energy bar charts / KE↔PE exchange along a track |
| 4 Momentum | before/after collision vector diagrams |
| 5 Circular/Gravitation | centripetal-force diagram; orbit + field arrows |
| 6 Waves | transverse/longitudinal waveform; standing-wave harmonics |
| 7 Optics | ray diagrams (mirrors, lenses); refraction at an interface |
| 8 Electrostatics | field-line diagrams (point charge, dipole, parallel plates) |
| 9 Circuits | series/parallel circuit schematics |
| 10 Magnetism | field-around-wire; right-hand-rule; induction loop |
| 11 Thermodynamics | heating/phase-change curve; PV diagram |
| 12 Modern | photoelectric threshold graph; decay curve; energy levels |

**Constraints (apply to ALL subjects' visual work):** static SVG/CSS only;
dark-mode-safe (`currentColor`/CSS vars, no hardcoded fills); bilingual
labels paired like surrounding prose; must not break print or validate.
Also during this sprint: spot-check each SG for content accuracy + the
known cosmetic odd-`$` validate WARN (benign).

#### Original Sprint 1 plan (historical)

**Goal.** Stand up the source-grounding layer for all four curricula,
then draft the **Unit 1 (Kinematics)** Study Guide **bilingual from
start** to lock the HS Physics SG template before any bulk-drafting.

This mirrors how HS Math locked its Unit 1/Unit 2 template before
bulk-drafting Units 3-15: prove the chrome on one unit, get user review,
then scale via parallel subagents.

**Sprint 1 plan:**

1. **Fetch the 4 curricula.** Pull NGSS HS-PS, ON (SPH3U / SPH4U / SNC2D),
   BC (Physics 11 / 12 / Science 10), AB (Physics 20 / 30 / Science 10)
   from the official URLs in the spec into `rag/sources/<region>/`. Use
   `pdftotext -layout` (Poppler) as HS Math did — go straight to
   `pdftotext` via Bash, not the Read tool.
2. **Write Kinematics-slice extracts.** One verbatim `*_extract.md`
   companion per fetched source, scoped to Unit 1 (Kinematics) so the
   Unit 1 Syllabus Map can cite codes directly. Organise by HS Physics
   unit relevance.
3. **Draft Unit 1 (Kinematics) SG — bilingual from start.** Paired
   `<span data-lang="en">` + `<span data-lang="zh">` markup + working
   `toggleLang()` script in the same commit (bilingual-from-start is
   LOCKED per spec, user 2026-05-31). Lock the chrome: grade-by-region
   nav, 4-column Syllabus Map (US NGSS / ON / BC / AB) cited verbatim
   from the extracts, region + paper-style chips, honors-flag for the
   advanced provincial stream, feeder-link to AP Physics / IB Physics HL,
   7 content sections satisfying the dual-goal contract, flashcards,
   readiness checklist.
4. **User review → lock template.** Hold bulk-drafting of Units 2-12
   until the Unit 1 template is approved (review-then-merge cadence).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-sources** | Fetch NGSS HS-PS + ON (SPH3U/SPH4U/SNC2D) + BC (Physics 11/12/Science 10) + AB (Physics 20/30/Science 10) PDFs into `rag/sources/`; queue rows into `sources.txt` | P0 | open |
| **S1-extracts** | Write Kinematics-slice `*_extract.md` companions (one per fetched source) | P0 | open |
| **S1-SG** | Draft `Unit_1_Kinematics.html` Study Guide, **bilingual from start** (EN + ZH spans + `toggleLang()` in one commit) | P0 | open |
| **S1-css** | Define `syllabus-map` / `syllabus-note` / `honors-flag` / `feeder-link` CSS in Unit 1's HTML (reuse locked HS Math definitions) | P1 | open |
| **S1-index** | Add `("High School Physics", "High School Physics", "chip-blue")` to `build-index.py` SUBJECTS; define `chip-blue` + `--blue` token in `index.html`; seed subject-group block; re-run build-index | P1 | open — do at SG ship |
| **S1-feeder** | Wire feeder-links from Unit 1 to `AP Physics/Study Guides/...` and `IB Physics HL/Study Guides/...` kinematics units where they exist | P2 | open |

Build order: **S1-sources → S1-extracts → S1-SG (+ S1-css folded in) →
S1-index → S1-feeder**. After Unit 1 review, Sprint 2 candidate is the
Units 2-12 bilingual bulk-draft via parallel subagents.

---

## Standing principles

- **Topic-indexed, single set.** One unit per physics topic, not per
  US course. Filename: `Unit_N_Topic.html`, sequential `N` across the
  whole subject. Title format and naming locked in
  [`rag/subjects/high_school_physics.md`](../rag/subjects/high_school_physics.md).
- **US standard is NGSS HS-PS, not Common Core.** Common Core is Math/ELA
  only. US physics maps to NGSS HS-PS1..HS-PS4 performance expectations.
- **Multi-syllabus crosswalk inside each guide.** Every unit ships with
  a Syllabus Map callout near the top listing the matching codes in US
  NGSS, Ontario, BC, and Alberta. Genuine divergences get an inline
  Syllabus Note &mdash; sparingly, only where it matters.
- **Dual-goal contract** &mdash; every guide serves both the
  test-tomorrow crammer and the depth student. Cram cheat-sheet on top,
  going-deeper derivations at the bottom. Locked from IB Math HL /
  HS Math; canonical articulation in
  [`prompts/create-unit.md`](../prompts/create-unit.md).
- **Bilingual-from-start &mdash; LOCKED (user 2026-05-31).** Every SG
  (and its Practice + Solutions) ships with paired
  `<span data-lang="en">` + `<span data-lang="zh">` markup **plus** the
  `toggleLang()` script in the same commit. Non-negotiable for this new
  subject &mdash; no English-first phase, no retroactive ZH wave.
- **Verification rule:** any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not acceptable.
- **No HL flag.** Advanced provincial-stream topics (AB Physics 30 /
  ON SPH4U / BC Physics 12) use an `honors-flag` chip so a regular-track
  student can skip cleanly.
- **AP / IB feeder pointers** &mdash; topics flag the AP Physics
  (C: Mechanics / 1 / 2) and IB Physics HL units they feed into;
  hyperlink where the target unit already exists in this repo.

---

## Cross-Unit Snapshot

Draft unit list &mdash; **pending per-unit source verification** against
the fetched NGSS / ON / BC / AB documents (see spec). Fill SG / P / S /
Status when each unit ships.

| Unit | Topic | SG | P | S | Status |
|---|---|---|---|---|---|
| 1  | Kinematics (1D / 2D motion)             | &mdash; | &mdash; | &mdash; | **Sprint 1 — template lock (open)** |
| 2  | Forces and Newton's Laws (Dynamics)     | &mdash; | &mdash; | &mdash; | unbuilt |
| 3  | Work, Energy and Power                  | &mdash; | &mdash; | &mdash; | unbuilt |
| 4  | Momentum and Collisions                 | &mdash; | &mdash; | &mdash; | unbuilt |
| 5  | Circular Motion and Gravitation         | &mdash; | &mdash; | &mdash; | unbuilt |
| 6  | Waves and Sound                         | &mdash; | &mdash; | &mdash; | unbuilt |
| 7  | Light and Geometric Optics              | &mdash; | &mdash; | &mdash; | unbuilt |
| 8  | Electrostatics and Electric Fields      | &mdash; | &mdash; | &mdash; | unbuilt |
| 9  | Current Electricity and Circuits        | &mdash; | &mdash; | &mdash; | unbuilt |
| 10 | Magnetism and Electromagnetic Induction | &mdash; | &mdash; | &mdash; | unbuilt |
| 11 | Thermodynamics and Heat                 | &mdash; | &mdash; | &mdash; | unbuilt |
| 12 | Modern / Nuclear Physics (intro)        | &mdash; | &mdash; | &mdash; | unbuilt |

---

## Source-grounding state

All curricula **PENDING** — no PDFs fetched yet. Sprint 1 closes this.

| Region | Course / doc | Real course codes | PDF fetched? | Extract written? |
|---|---|---|---|---|
| 🇺🇸 US | NGSS HS Physical Science | HS-PS1, HS-PS2, HS-PS3, HS-PS4 | **PENDING** | **PENDING** |
| 🇨🇦 ON | Physics 11 / Physics 12; Science 10 foundations | SPH3U, SPH4U; SNC2D | **PENDING** | **PENDING** |
| 🇨🇦 BC | Physics 11 / Physics 12; Science 10 foundations | Physics 11, Physics 12; Science 10 | **PENDING** | **PENDING** |
| 🇨🇦 AB | Physics 20 / Physics 30; Science 10 foundations | Physics 20, Physics 30; Science 10 | **PENDING** | **PENDING** |

**URLs to fetch from:**
- NGSS HS-PS: <https://www.nextgenscience.org/>
- BC Science: <https://curriculum.gov.bc.ca/curriculum/science>
- Ontario Science: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
- Alberta: <https://www.alberta.ca/programs-of-study>

**Extraction tool note:** use `pdftotext -layout` (Poppler, at
`/mingw64/bin/pdftotext` in the sandbox) via Bash, as HS Math did. The
Read tool's PDF path relies on `pdftoppm` (image rendering), which is
absent in the sandbox.

---

## Closed Sprints

### Sprint 0 — closed 2026-05-31

Subject scaffolding shipped: subject spec (`rag/subjects/high_school_physics.md`),
this audit, and the empty folder structure (`Study Guides/`,
`Practice Questions/Solutions/` with `.gitkeep` sentinels). Topic-organised
multi-syllabus posture (US NGSS HS-PS primary; ON / BC / AB secondary)
locked at scaffold time, mirroring HS Math.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-2**~~ | Author audit | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-3**~~ | Create empty folder structure (`.gitkeep` sentinels) | P0 | ✅ shipped 2026-05-31 |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint.

| ID | Item | Why it's not in scope here |
|---|---|---|
| ~~DP-1~~ | ~~Practice Questions + Solutions product per unit~~ | **→ PROMOTED to Sprint 3 (PLANNED 2026-06-03).** SGs shipped; playbook authored. |
| DP-2 | Per-province exam-prep overlays (BC Provincial, AB Physics 30 Diploma, ON SPH4U) on top of the topic guides | Layer onto existing guides; deferred until Canadian-audience demand is measured. |
| DP-3 | NGSS three-dimensional learning callouts (SEP + CCC + DCI) per unit | NGSS performance expectations bundle practices + crosscutting concepts; a richer pedagogical overlay than the syllabus-map crosswalk. Scope separately. |
| DP-4 | Interactive simulations / PhET-style embeds for motion, circuits, waves | Needs an interactive product surface beyond the self-contained HTML SG. |
| DP-5 | Lab / practical-skills track (measurement, uncertainty, graphing) | Cross-cuts all units; provincial labs differ. Scope as a standalone unit or appendix later. |

---

## How to update this file

When closing a sprint item, mark with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When a sprint clears,
collapse into a single line in `## Closed Sprints` and promote the next
sprint up.

When standing principles need revision, edit them here; route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_physics.md`](../rag/subjects/high_school_physics.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork
the contract.

When a unit ships, fill in its row of the Cross-Unit Snapshot and flip
its Source-grounding state rows from PENDING.
