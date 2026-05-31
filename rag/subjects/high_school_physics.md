# Subject Spec — High School Physics (multi-syllabus, topic-organised)

## Identity

- **Display (section heading):** High School Physics
- **Display (hero chip):** High School Physics
- **Directory:** `High School Physics/`
- **Audit:** `High School Physics/AUDIT.md`

## Strategic posture (locked 2026-05-31)

**One study-guide set, organised by physics topic.** Physics is physics —
kinematics, dynamics, energy, waves, electricity cover the same core
scope in every modern HS curriculum. Each guide is written once around
the universal topic, with **syllabus-specific callouts** inside the page
where coverage genuinely diverges.

**IMPORTANT — the US standard is NGSS, not Common Core.** Common Core
applies to **Math and English/Language Arts only**; it has no science
strand. The US science standard targeted here is **NGSS (Next Generation
Science Standards)**, specifically the **HS-PS (High School — Physical
Science)** performance expectations **HS-PS1 through HS-PS4**. Do **not**
label any US physics content "Common Core" — that is a category error
this subject must avoid in every guide, syllabus map, and audit row.

**Market priority (largest → smallest, English-language):**

1. **US NGSS HS-PS (Physical Science)** — primary commercial target.
2. **Canadian provinces:** Ontario, British Columbia, Alberta — secondary
   target. Repo author is based in Canada, so this audience is
   acknowledged explicitly and tested against per-unit.

We do **not** ship four separate course tracks (Physics 11 / Physics 12 /
SPH3U / SPH4U). We ship one topic-indexed set that serves all four
implicitly.

## Source documents

To be catalogued in [`sources.txt`](../../sources.txt) at the repo root
once the PDFs are fetched. Status `[x]` = PDF pulled to `rag/sources/`;
`[ ]` = queued; `[!]` = URL is a publications landing page, not a direct
PDF link.

| Region | Course / doc | Real course codes | Status (2026-05-31) |
|---|---|---|---|
| 🇺🇸 US | NGSS HS Physical Science — performance expectations | HS-PS1, HS-PS2, HS-PS3, HS-PS4 | **PENDING** — PDF not yet fetched |
| 🇨🇦 ON | Physics, Grade 11 (University); Physics, Grade 12 (University); Science 10 for foundations | SPH3U, SPH4U; SNC2D | **PENDING** — PDF not yet fetched |
| 🇨🇦 BC | Physics 11, Physics 12; Science 10 for foundations | Physics 11, Physics 12; Science 10 | **PENDING** — PDF not yet fetched |
| 🇨🇦 AB | Physics 20, Physics 30; Science 10 for foundations | Physics 20, Physics 30; Science 10 | **PENDING** — PDF not yet fetched |

**URLs to fetch from** (verify against these; do not paraphrase from memory):
- NGSS HS-PS performance expectations: <https://www.nextgenscience.org/>
  (DCI strand pages HS-PS1 Matter and Its Interactions, HS-PS2 Motion and
  Stability: Forces and Interactions, HS-PS3 Energy, HS-PS4 Waves and
  Their Applications in Technologies for Information Transfer).
- BC Science (Physics 11 / 12, Science 10): <https://curriculum.gov.bc.ca/curriculum/science>
- Ontario (SPH3U / SPH4U / SNC2D): <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
- Alberta (Physics 20 / 30, Science 10): <https://www.alberta.ca/programs-of-study>

**Verification rule:** any syllabus-specific claim in a guide (course
code, NGSS performance-expectation code, topic placement, exam-expected
emphasis) must be checked against the corresponding **fetched source
document** before shipping. Training-data recall is *not* an acceptable
citation. Place the source PDF under `rag/sources/<region>/...` and write
a verbatim `*_extract.md` companion next to it, organised by HS Physics
unit relevance, exactly as HS Math does.

## Naming convention

Flat, topic-indexed — no course prefix, no per-region split:

```
High School Physics/Study Guides/Unit_N_Topic.html
High School Physics/Practice Questions/Unit_N_Topic_Practice.html
High School Physics/Practice Questions/Solutions/Unit_N_Topic_Solutions.html
```

`N` is the topic index across the whole subject (1, 2, 3, …). Topic
uses underscores in filenames; avoid commas / ampersands.

Examples:
- `Unit_1_Kinematics.html`
- `Unit_9_Current_Electricity_and_Circuits.html`

## Required `<title>` format

```
High School Physics — <Topic> | Dingrui Scholars
```

Examples:
- `High School Physics — Kinematics | Dingrui Scholars`
- `High School Physics — Waves and Sound | Dingrui Scholars`

`build-index.py` reads this verbatim to generate the home-page card.

### Why no "Unit N:" in the visible title

HS Physics is **topic-organised** across four curricula (US/ON/BC/AB), so
a sequential unit number reads as noise — students locate content by
topic, not by sprint order. The filename keeps `Unit_N_` for directory
sort stability and cross-link permanence; everything visible (title tag,
hero h1, nav badge, hero meta chips, section labels, worked-example
labels, quiz numbers, cross-section refs, footer) strips it. This is the
same convention HS Math locked 2026-05-27.

**Visible chrome rules:**

- **Hero h1:** topic name only, no `Unit N:` prefix.
- **Nav badge (second chip):** topic code, not unit number — table below.
- **Hero meta chip "Unit N of 12":** removed entirely. Replace with a
  content-count chip like `7 sections` or a curriculum chip.
- **Section labels:** `Section 1 · …` instead of `Section 7.1 · …`
  (sequential within the unit). Same for Worked Example labels and
  quiz numbers (`§1 · Q1`).
- **Cross-section references inside the same guide:** `§1`, `§2`, …
  Cross-unit references use topic names ("see the Dynamics guide"),
  not unit numbers.
- **HTML `id` attributes:** keep `s-7-1`, `s-7-2`, etc. for URL anchor
  stability. Visible labels change; the IDs are implementation detail.

**Topic-code mapping for nav badges:**

| Filename | Nav badge |
|---|---|
| `Unit_1_Kinematics.html` | `KINEMATICS` |
| `Unit_2_Forces_and_Newtons_Laws.html` | `DYNAMICS` |
| `Unit_3_Work_Energy_and_Power.html` | `ENERGY` |
| `Unit_4_Momentum_and_Collisions.html` | `MOMENTUM` |
| `Unit_5_Circular_Motion_and_Gravitation.html` | `GRAVITATION` |
| `Unit_6_Waves_and_Sound.html` | `WAVES` |
| `Unit_7_Light_and_Geometric_Optics.html` | `OPTICS` |
| `Unit_8_Electrostatics_and_Electric_Fields.html` | `ELECTROSTATICS` |
| `Unit_9_Current_Electricity_and_Circuits.html` | `CIRCUITS` |
| `Unit_10_Magnetism_and_Electromagnetic_Induction.html` | `MAGNETISM` |
| `Unit_11_Thermodynamics_and_Heat.html` | `THERMO` |
| `Unit_12_Modern_and_Nuclear_Physics.html` | `MODERN` |

## Topic list (draft — pending per-unit source verification)

~12 units to span the full scope. **This list is a draft pending
per-unit source verification** against the fetched NGSS / ON / BC / AB
documents. Lock per-unit ordering and the syllabus map when each unit
is opened for drafting. Each unit's audit row should record the topic
chosen and the syllabus codes it maps to.

| Unit | Topic | 🇺🇸 US NGSS HS-PS | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|---|
| 1  | Kinematics (1D / 2D motion)               | HS-PS2-1 (motion analysis) | SPH3U Kinematics | Physics 11 — Kinematics | Physics 20 — Kinematics |
| 2  | Forces and Newton's Laws (Dynamics)       | HS-PS2-1, HS-PS2-2 | SPH3U Forces | Physics 11 — Dynamics | Physics 20 — Dynamics |
| 3  | Work, Energy and Power                    | HS-PS3-1, HS-PS3-2, HS-PS3-3 | SPH3U / SPH4U Energy & Momentum | Physics 11 — Energy | Physics 20 — Mechanical Energy |
| 4  | Momentum and Collisions                   | HS-PS2-2, HS-PS2-3 | SPH4U Energy & Momentum | Physics 12 — Momentum | Physics 30 — Momentum & Impulse |
| 5  | Circular Motion and Gravitation           | HS-PS2-1, HS-PS2-4 | SPH4U Dynamics (gravitation) | Physics 12 — Circular Motion & Gravitation | Physics 20 — Circular Motion / Physics 30 |
| 6  | Waves and Sound                           | HS-PS4-1 | SPH3U Waves & Sound | Physics 11 — Waves | Physics 20 — Mechanical Waves |
| 7  | Light and Geometric Optics                | HS-PS4-3, HS-PS4-5 | SPH3U Light & Geometric Optics | Physics 11 — Optics / Physics 12 | Physics 30 — Electromagnetic Radiation (optics) |
| 8  | Electrostatics and Electric Fields        | HS-PS2-4, HS-PS3-5 | SPH4U Electric, Gravitational & Magnetic Fields | Physics 12 — Electrostatics | Physics 30 — Electric Forces & Fields |
| 9  | Current Electricity and Circuits          | HS-PS3-5 | SPH3U Electricity & Magnetism | Physics 11 — Circuitry | Physics 20 (foundations) / Physics 30 |
| 10 | Magnetism and Electromagnetic Induction   | HS-PS2-5 | SPH4U Fields; SPH3U Electromagnetism | Physics 12 — Electromagnetism | Physics 30 — Magnetic Forces & EM Induction |
| 11 | Thermodynamics and Heat                   | HS-PS3-4, HS-PS3-1 | SNC2D / SPH4U (thermal) | Physics 11 — Heat (Science 10 / 11) | Physics 20 — Heat & Thermal Energy |
| 12 | Modern / Nuclear Physics (intro)          | HS-PS1-8, HS-PS4-3 | SPH4U Revolutions in Modern Physics | Physics 12 — Nuclear / Modern (intro) | Physics 30 — Atomic / Nuclear Physics |

The mapping above is a **draft** based on typical curriculum placement;
confirm each cell against the fetched source extract before locking the
unit's Syllabus Map. NGSS HS-PS codes are coarse (performance
expectations, not topic outlines), so several units share a code — that
is expected and not an error.

## In-page conventions (the multi-syllabus pattern)

Inherited verbatim from HS Math. Each unit's HTML must include, near the
top of the page (immediately under the hero or in the first section), a
**Syllabus Map callout**:

```html
<aside class="syllabus-map">
  <div class="syllabus-map-label">Where this lives in your syllabus</div>
  <ul>
    <li><strong>🇺🇸 US NGSS:</strong> HS-PS2-1 — analyze motion via Newton's second law</li>
    <li><strong>🇨🇦 Ontario:</strong> SPH3U — Kinematics strand</li>
    <li><strong>🇨🇦 BC:</strong> Physics 11 — Kinematics</li>
    <li><strong>🇨🇦 Alberta:</strong> Physics 20 — Kinematics</li>
  </ul>
</aside>
```

Where the curricula **genuinely diverge** (a topic emphasised in one
but absent or deferred in another), use a smaller inline callout:

```html
<div class="syllabus-note">
  <strong>Syllabus note.</strong> Alberta's Physics 30 treats
  electromagnetic induction quantitatively (Faraday's law with flux);
  BC Physics 12 stays largely conceptual. If you're prepping the AB
  Diploma, read the going-deeper derivation below.
</div>
```

Use these **sparingly** — only when there's a real difference a student
would feel.

CSS classes `syllabus-map`, `syllabus-map-label`, `syllabus-map-grid`,
`region-header`, `region-chip`, `syllabus-note`, `honors-flag`,
`feeder-link` are inherited from the HS Math template; reuse the locked
HS Math definitions when the first HS Physics SG is drafted.

## Standing principles

- **Dual-goal contract** (inherited from IB Math HL / HS Math): every
  guide serves both the test-tomorrow crammer (≥ pass) and the depth
  student (5 on AP feeder / 100 on provincial / Diploma). Cram
  cheat-sheet at top, worked examples, going-deeper derivations in
  `<details>`. Canonical articulation in
  [`prompts/create-unit.md`](../../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every SG ships
  with paired `<span data-lang="en">` + `<span data-lang="zh">` markup
  **plus** the `toggleLang()` script in the same commit. This is
  **non-negotiable for new subjects** — no English-first phase, no
  retroactive ZH wave. Each new SG must land visible in the landing-page
  ZH mode immediately. Practice + Solutions files ship bilingual too.
- **No HL flag** (there's no HL tier in HS Physics). Where a topic is
  the harder advanced stream in Canada (AB **Physics 30** / ON **SPH4U**
  vs. the Grade-11 stream, BC **Physics 12** vs. Physics 11), mark with
  an `honors-flag` chip so a regular-track student can skip cleanly.
- **AP / IB feeder pointers** — physics topics flag the **AP Physics**
  (C: Mechanics / 1 / 2) and **IB Physics HL** units they feed into.
  Hyperlink where the target unit already exists in this repo
  (`AP Physics/Study Guides/...`, `IB Physics HL/Study Guides/...`).
- **Verification rule:** any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not acceptable.

## Build-index integration (do at first unit ship)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Physics", "High School Physics", "chip-blue"),
   ```
   Pick an **unused** chip colour. The four currently defined in
   `index.html` are `chip-maroon`, `chip-green`, `chip-purple`,
   `chip-gold` (all four are in use across the seven existing subjects).
   **`chip-blue` is unused** — define it in `index.html` CSS
   (`.chip-blue { border: 1px solid var(--blue); color: var(--blue); }`
   plus a `--blue` token) when the first card lands.

2. **No `WORD_PRIORITY` entry needed** — units are numbered
   sequentially with no sub-categories, so default numerical sort is
   correct.

3. Re-run `python scripts/build-index.py`. `index.html` may need a
   `<h2 class="section-title">High School Physics</h2>` + empty grid
   block inserted manually the first time, after which the script
   handles re-indexing. (`parse_title()` already handles the HS no-colon
   title format from the HS Math integration.)

## Cross-references

- Dual-goal contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Style tokens: [`rag/style-guide.md`](../style-guide.md)
- Sibling spec (mirror this structure): [`rag/subjects/high_school_math.md`](high_school_math.md)
- Source URLs (queue into `sources.txt` on fetch): [`sources.txt`](../../sources.txt)
- Official references (verify against, do not paraphrase from memory):
  - NGSS HS-PS: <https://www.nextgenscience.org/>
  - BC Science: <https://curriculum.gov.bc.ca/curriculum/science>
  - Ontario Science: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
  - Alberta: <https://www.alberta.ca/programs-of-study>
