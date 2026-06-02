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

### Sprint 2 — static visual upgrade — **PLANNED (deferred until all HS STEM SGs ship)**

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
| DP-1 | Practice Questions + Solutions product per unit (MC + FRQ-style, bilingual, mirroring HS Math's region + paper-style chip taxonomy) | Needs Study Guide content first to anchor question scope. Open after the Unit 1 template locks. |
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
