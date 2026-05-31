# Subject Spec — High School Chemistry (multi-syllabus, topic-organised)

## Identity

- **Display (section heading):** High School Chemistry
- **Display (hero chip):** High School Chemistry
- **Directory:** `High School Chemistry/`
- **Audit:** `High School Chemistry/AUDIT.md`

## Strategic posture

**One study-guide set, organised by chemistry topic.** Atomic structure,
bonding, the mole, stoichiometry, acids/bases and equilibrium cover the
same conceptual scope in every modern HS chemistry curriculum. Each
guide is written once around the universal topic, with
**syllabus-specific callouts** inside the page where coverage genuinely
diverges (depth, grade placement, exam emphasis).

**Market priority (largest → smallest, English-language):**

1. **US NGSS** — primary commercial target. *Note:* the US science
   standard is the **Next Generation Science Standards (NGSS)**, NOT
   Common Core. Common Core covers Math and English Language Arts only;
   it has no chemistry strand. The relevant NGSS bundle is **HS-PS1
   (Matter and its Interactions)**, supplemented by **HS-PS2 (Motion and
   Stability — bonding/forces)** and **HS-PS3 (Energy —
   thermochemistry)** where a topic crosses over. State NGSS performance
   expectations (e.g. HS-PS1-1, HS-PS1-2) are the citable unit, since
   NGSS itself is a national framework many states adopt or adapt.
2. **Canadian provinces:** Ontario, British Columbia, Alberta —
   secondary target. Repo author is based in Canada, so this audience is
   acknowledged explicitly and tested against per-unit.

We do **not** ship four separate course tracks. We ship one
topic-indexed set that serves all four implicitly.

**Distinct from IB Chemistry HL.** This is the *secondary-school* tier
(Grade 9-12 / NGSS / provincial). It is **separate from** the existing
`IB Chemistry HL/` product, which sits in the college-credit tier
alongside AP. Where an HS Chemistry topic feeds into the college-credit
tier (e.g. equilibrium, thermochemistry, redox), use a **feeder-link**
pointing at the corresponding IB Chemistry HL / AP Chemistry unit. See
`project_product_positioning` (HS → AP/IB → first-year uni pipeline).

## Source documents

To be catalogued in [`sources.txt`](../../sources.txt) at the repo root
once fetched. Status `[x]` = PDF pulled to `rag/sources/`; `[ ]` =
queued; `[!]` = URL is a publications landing page, not a direct PDF
link.

**Source-grounding status: PENDING — no PDFs fetched yet.** All rows
below are queued; the official URLs are recorded so Sprint 1 can fetch
and extract before any unit is drafted.

| Region | Course / doc | Real course codes | Status (2026-05-31) |
|---|---|---|---|
| 🇺🇸 US | NGSS HS Physical Science — performance expectations | **HS-PS1** (Matter and its Interactions), with **HS-PS2 / HS-PS3** crossover | `[ ]` PENDING |
| 🇨🇦 ON | Chemistry, Grade 11 / Grade 12 + Grade 10 Science foundations | **SCH3U** (Gr 11 University), **SCH4U** (Gr 12 University); **SNC2D** (Science 10) for foundations | `[ ]` PENDING |
| 🇨🇦 BC | Chemistry 11 / Chemistry 12 + Science 10 foundations | **Chemistry 11**, **Chemistry 12**; **Science 10** for foundations | `[ ]` PENDING |
| 🇨🇦 AB | Chemistry 20 / Chemistry 30 + Science 10 foundations | **Chemistry 20**, **Chemistry 30**; **Science 10** for foundations | `[ ]` PENDING |

**Verification rule:** any syllabus-specific claim in a guide (course
code, performance expectation, topic placement, exam-expected emphasis)
must be checked against the corresponding source document before
shipping. Training-data recall is *not* an acceptable citation. Place
the source PDF under `rag/sources/<region>/...` per the `SAVE_AS`
column added to `sources.txt` when fetched.

## Naming convention

Flat, topic-indexed — no course prefix, no per-region split. Identical
pattern to High School Math:

```
High School Chemistry/Study Guides/Unit_N_Topic.html
High School Chemistry/Practice Questions/Unit_N_Topic_Practice.html
High School Chemistry/Practice Questions/Solutions/Unit_N_Topic_Solutions.html
```

`N` is the topic index across the whole subject (1, 2, 3, …). Topic
uses underscores in filenames; avoid commas / ampersands.

Examples:
- `Unit_1_Atomic_Structure_and_the_Quantum_Model.html`
- `Unit_9_Acids_Bases_and_pH.html`

### No "Unit N:" in the visible chrome (inherited from HS Math)

HS Chemistry is **topic-organised** across four curricula (US/ON/BC/AB),
so a sequential unit number reads as noise — students locate content by
topic, not by sprint order. The filename keeps `Unit_N_` for directory
sort stability and cross-link permanence; everything visible (title
tag, hero h1, nav badge, hero meta chips, section labels,
worked-example labels, quiz numbers, cross-section refs, footer) strips
it.

**Visible chrome rules:**

- **Hero h1:** topic name only, no `Unit N:` prefix.
- **Nav badge (second chip):** topic code, not unit number — table below.
- **Hero meta chip "Unit N of 14":** removed entirely. Replace with a
  content-count chip like `7 sections` or a curriculum chip.
- **Section labels:** `Section 1 · …` (sequential within the unit).
  Same for Worked Example labels and quiz numbers (`§1 · Q1`).
- **Cross-section references inside the same guide:** `§1`, `§2`, …
  Cross-unit references use topic names ("see the Chemical Bonding
  guide"), not unit numbers.
- **HTML `id` attributes:** keep `s-1-1`, `s-1-2`, etc. for URL anchor
  stability. Visible labels change; the IDs are implementation detail.

**Topic-code mapping for nav badges:**

| Filename | Nav badge |
|---|---|
| `Unit_1_Atomic_Structure_and_the_Quantum_Model.html` | `ATOMIC` |
| `Unit_2_The_Periodic_Table_and_Periodic_Trends.html` | `PERIODIC` |
| `Unit_3_Chemical_Bonding.html` | `BONDING` |
| `Unit_4_Nomenclature_and_Chemical_Formulae.html` | `NAMING` |
| `Unit_5_The_Mole_and_Stoichiometry.html` | `MOLE` |
| `Unit_6_Chemical_Reactions_and_Equations.html` | `REACTIONS` |
| `Unit_7_States_of_Matter_and_the_Gas_Laws.html` | `GASES` |
| `Unit_8_Solutions_and_Solubility.html` | `SOLUTIONS` |
| `Unit_9_Acids_Bases_and_pH.html` | `ACID / BASE` |
| `Unit_10_Thermochemistry_and_Energy.html` | `THERMO` |
| `Unit_11_Reaction_Rates_and_Kinetics.html` | `KINETICS` |
| `Unit_12_Chemical_Equilibrium.html` | `EQUILIBRIUM` |
| `Unit_13_Redox_and_Electrochemistry.html` | `REDOX` |
| `Unit_14_Introduction_to_Organic_Chemistry.html` | `ORGANIC` |

## Required `<title>` format

```
High School Chemistry — <Topic> | Dingrui Scholars
```

Examples:
- `High School Chemistry — Atomic Structure and the Quantum Model | Dingrui Scholars`
- `High School Chemistry — Acids, Bases and pH | Dingrui Scholars`

`build-index.py` reads this verbatim to generate the home-page card.

## Topic list (initial proposal, ~14 units to span the full scope)

**Status: draft — pending per-unit source verification.** This is the
working scope grounded in the four curricula. Lock per-unit ordering
and the exact curriculum codes when the unit is opened for drafting,
after the source PDFs are fetched and extracted. Each unit's audit row
should record the topic chosen and the syllabus codes it maps to.

| Unit | Topic | 🇺🇸 US NGSS | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|---|
| 1  | Atomic Structure and the Quantum Model | HS-PS1-1, HS-PS1-8 (atomic model, nuclear) | SNC2D Chemistry; SCH3U Matter, Chemical Bonding | Science 10; Chemistry 11 atomic theory | Science 10; Chemistry 20 atomic structure |
| 2  | The Periodic Table and Periodic Trends | HS-PS1-1, HS-PS1-2 (periodicity → properties) | SCH3U Matter, Chemical Bonding | Chemistry 11 periodic table | Chemistry 20 periodic trends |
| 3  | Chemical Bonding (Ionic, Covalent, Metallic) | HS-PS1-2, HS-PS1-3, HS-PS2-6 (bonding, IMF) | SCH3U Chemical Bonding | Chemistry 11 bonding | Chemistry 20 / 30 bonding |
| 4  | Nomenclature and Chemical Formulae | HS-PS1 foundational (no direct PE) | SNC2D / SCH3U naming | Science 10 / Chemistry 11 naming | Science 10 / Chemistry 20 naming |
| 5  | The Mole and Stoichiometry | HS-PS1-7 (conservation of mass / quantities) | SCH3U Quantities in Chemical Reactions | Chemistry 11 the mole, stoichiometry | Chemistry 20 the mole, stoichiometry |
| 6  | Chemical Reactions and Equations | HS-PS1-2, HS-PS1-7 (reaction types, balancing) | SNC2D / SCH3U Chemical Reactions | Science 10 / Chemistry 11 reactions | Science 10 / Chemistry 20 reactions |
| 7  | States of Matter and the Gas Laws | HS-PS1-3 (states, forces); HS-PS3 (energy) | SCH3U Gases & Atmospheric Chemistry | Chemistry 11 gases | Chemistry 20 gases |
| 8  | Solutions and Solubility | HS-PS1-3 (solution behaviour) | SCH3U Solutions & Solubility | Chemistry 11 solutions | Chemistry 20 solutions |
| 9  | Acids, Bases and pH | HS-PS1-2 (reaction behaviour) | SCH3U / SCH4U acids & bases | Chemistry 11 / 12 acids & bases | Chemistry 20 / 30 acids & bases |
| 10 | Thermochemistry and Energy | HS-PS1-4, HS-PS3-1, HS-PS3-4 (bond energy, ΔH) | SCH4U Energy Changes & Rates | Chemistry 12 thermochemistry | Chemistry 30 thermochemistry |
| 11 | Reaction Rates (Kinetics) | HS-PS1-5 (rate, collision theory) | SCH4U Energy Changes & Rates of Reaction | Chemistry 12 reaction kinetics | Chemistry 30 kinetics (honors stream) |
| 12 | Chemical Equilibrium | HS-PS1-6 (Le Chatelier, equilibrium) | SCH4U Chemical Systems & Equilibrium | Chemistry 12 equilibrium | Chemistry 30 equilibrium |
| 13 | Redox and Electrochemistry | HS-PS1 / HS-PS3 crossover (electron transfer, energy) | SCH4U Electrochemistry | Chemistry 12 electrochemistry | Chemistry 30 electrochemistry |
| 14 | Introduction to Organic Chemistry | HS-PS1 (carbon chemistry, light) | SCH4U Organic Chemistry | Chemistry 12 organic (intro) | Chemistry 30 organic (intro) |

Per-unit mapping above is a **draft** — every code must be confirmed
against the fetched source PDF before the unit's Syllabus Map locks.
NGSS performance-expectation numbers in particular need verification
against the official `HS-PS1` bundle, since several topics here (naming,
nomenclature) have no direct performance expectation and are framed as
foundational skills supporting the PEs.

## In-page conventions (the multi-syllabus pattern)

Inherited verbatim from HS Math. Each unit's HTML must include, near the
top of the page, a **Syllabus Map callout**:

```html
<aside class="syllabus-map">
  <div class="syllabus-map-label">Where this lives in your syllabus</div>
  <ul>
    <li><strong>🇺🇸 US NGSS:</strong> HS-PS1-1, HS-PS1-2</li>
    <li><strong>🇨🇦 Ontario:</strong> SCH3U — Matter, Chemical Bonding</li>
    <li><strong>🇨🇦 BC:</strong> Chemistry 11 — Atomic Theory</li>
    <li><strong>🇨🇦 Alberta:</strong> Chemistry 20 — Diversity of Matter</li>
  </ul>
</aside>
```

CSS classes `syllabus-map`, `syllabus-map-label`, `syllabus-map-grid`,
`region-header`, `region-chip`, `syllabus-note`, `honors-flag`,
`feeder-link` are **inherited** from the HS Math Unit 1 lock (see
`rag/style-guide.md` and the shipped HS Math units). Reuse them as-is;
do not fork the styling.

Where the curricula **genuinely diverge** (a topic emphasised in one but
absent or deferred in another), use a smaller inline callout:

```html
<div class="syllabus-note">
  <strong>Syllabus note.</strong> Ontario's SCH4U treats equilibrium
  quantitatively (Ksp, ICE tables); BC Chemistry 12 expects the same
  depth, but NGSS HS-PS1-6 is qualitative (Le Chatelier only). If you're
  prepping NGSS, the qualitative shift-direction reasoning is enough; for
  SCH4U / Chem 12 read the quantitative worked examples below.
</div>
```

Use these **sparingly** — only when there's a real difference a student
would feel.

### Honors / advanced-stream flag

Where a topic is honors-level OR is the harder provincial stream
(**AB Chemistry 30**, **ON SCH4U** Grade-12 University depth vs. the
Grade-11 / Science-10 baseline), mark with an `honors-flag` chip so a
regular-track student can skip cleanly. Quantitative equilibrium,
electrochemical cell potentials, and enthalpy-of-formation calculations
are typical honors-flag content.

### Feeder pointers

Topics that feed the college-credit tier (equilibrium, thermochemistry,
kinetics, redox, organic) flag the **IB Chemistry HL** / **AP Chemistry**
unit they feed into. Hyperlink where the target unit already exists in
this repo (e.g. `IB Chemistry HL/Study Guides/...`).

## Standing principles

- **Dual-goal contract** (inherited from IB Math HL / HS Math): every
  guide serves both the test-tomorrow crammer (≥ pass) and the depth
  student (provincial-exam / AP-IB feeder). Cram cheat-sheet at top,
  worked examples, going-deeper derivations in `<details>`. Canonical
  articulation in [`prompts/create-unit.md`](../../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every Study Guide
  ships with paired `<span data-lang="en">` + `<span data-lang="zh">`
  markup and a working `toggleLang()` script **in the same commit it is
  first drafted**. This is **non-negotiable for new subjects** — HS Math
  paid a multi-sprint retroactive-translation tax (Sprints 5-6) by
  shipping English-first; HS Chemistry must not repeat it. No
  `data-zh-ready="false"` parking.
- **Honors-flag** — honors / harder-stream topics (AB Chemistry 30,
  ON SCH4U depth) use an `honors-flag` chip so regular-track students can
  skip cleanly.
- **Feeder pointers** — topics feeding IB Chemistry HL / AP Chemistry
  hyperlink the target unit where it already exists in this repo.
- **Verification rule** — any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not acceptable.

## Build-index integration (do at first unit ship)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Chemistry", "High School Chemistry", "chip-XXX"),
   ```
   **Chip colour: pick one not already in use.** Current assignments
   (verify against the live `SUBJECTS` list before choosing) include
   chip-green (HS Math). Choose an unused colour token (e.g.
   `chip-teal` / `chip-amber`) so HS Chemistry is visually distinct.

2. **No `WORD_PRIORITY` entry needed** — units are numbered
   sequentially with no sub-categories, so default numerical sort is
   correct. `parse_title()` already handles the no-colon HS title
   format (patched for HS Math in Sprint 4).

3. Re-run `python scripts/build-index.py`. `index.html` may need a
   `<h2 class="section-title">High School Chemistry</h2>` + empty grid
   block inserted manually the first time, after which the script
   handles re-indexing.

## Cross-references

- Dual-goal contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Sibling spec (conventions mirrored from here): [`rag/subjects/high_school_math.md`](high_school_math.md)
- Style tokens / shared CSS classes: [`rag/style-guide.md`](../style-guide.md)
- College-credit-tier sibling (feeder target): [`rag/subjects/ib_chemistry_hl.md`](ib_chemistry_hl.md)
- Source URLs (to be queued in `sources.txt`): [`sources.txt`](../../sources.txt) at repo root
- Official references (verify against, do not paraphrase from memory):
  - US NGSS: <https://www.nextgenscience.org/>
  - BC: <https://curriculum.gov.bc.ca/curriculum/science>
  - Ontario: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
  - Alberta: <https://www.alberta.ca/programs-of-study>
