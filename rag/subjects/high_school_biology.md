# Subject Spec — High School Biology (multi-syllabus, topic-organised)

## Identity

- **Display (section heading):** High School Biology
- **Display (hero chip):** High School Biology
- **Directory:** `High School Biology/`
- **Audit:** `High School Biology/AUDIT.md`

## Strategic posture (locked 2026-05-31)

**One study-guide set, organised by biological topic.** Cell structure,
genetics, evolution, ecology, and human physiology cover essentially the
same scope in every modern HS curriculum. Each guide is written once
around the universal topic, with **syllabus-specific callouts** inside
the page where coverage genuinely diverges.

**Market priority (largest → smallest, English-language):**

1. **US — NGSS HS Life Sciences (HS-LS).** Primary commercial target.

   > **NUANCE — NGSS, not Common Core.** Unlike HS Math (which targets
   > US **Common Core State Standards for Mathematics**, CCSSM), there is
   > **no Common Core for science**. The Common Core initiative covers
   > **Mathematics and English Language Arts only.** The de-facto US
   > national science standard is the **Next Generation Science Standards
   > (NGSS)**, and the biology slice is the **Life Sciences (LS)** domain
   > at the high-school level: **HS-LS1, HS-LS2, HS-LS3, HS-LS4**. Cite
   > NGSS performance-expectation codes (e.g. `HS-LS1-1`, `HS-LS3-2`),
   > never a "Common Core" science code — that does not exist.

2. **Canadian provinces:** Ontario, British Columbia, Alberta — secondary
   target. Repo author is based in Canada, so this audience is
   acknowledged explicitly and tested against per-unit.

We do **not** ship separate course tracks (Grade 11 vs. Grade 12, or
SBI3U vs. SBI4U). We ship one topic-indexed set that serves all four
curricula implicitly, flagging the harder provincial stream (Biology 30 /
SBI4U / Anatomy & Physiology 12) inline where the content steps up.

## Source documents

Catalogued in [`sources.txt`](../../sources.txt) at the repo root.
Status `[x]` = PDF/source pulled to `rag/sources/`; `[ ]` = queued;
`[!]` = URL is a publications landing page, not a direct PDF link.

| Region | Course / doc | Course code | Status (2026-05-31) |
|---|---|---|---|
| 🇺🇸 US | NGSS High School Life Sciences performance expectations | HS-LS1 / HS-LS2 / HS-LS3 / HS-LS4 | **PENDING** `[ ]` |
| 🇨🇦 ON | Biology, Grade 11, University Prep | SBI3U | **PENDING** `[ ]` |
| 🇨🇦 ON | Biology, Grade 12, University Prep | SBI4U | **PENDING** `[ ]` |
| 🇨🇦 ON | Science, Grade 10 (foundations) | SNC2D | **PENDING** `[ ]` |
| 🇨🇦 BC | Life Sciences 11 | — | **PENDING** `[ ]` |
| 🇨🇦 BC | Anatomy and Physiology 12 | — | **PENDING** `[ ]` |
| 🇨🇦 BC | Science 10 (foundations) | — | **PENDING** `[ ]` |
| 🇨🇦 AB | Biology 20 | — | **PENDING** `[ ]` |
| 🇨🇦 AB | Biology 30 | — | **PENDING** `[ ]` |
| 🇨🇦 AB | Science 10 (foundations) | — | **PENDING** `[ ]` |

**All source-grounding is PENDING.** No source PDFs/extracts have been
fetched yet. Sprint 1's first job is to fetch the priority documents
(NGSS HS-LS, plus one provincial doc per region) and write
`*_extract.md` companions before any Syllabus Map ships.

**Official curriculum URLs** (fetch from these; verify, do not paraphrase
from memory):

- **US NGSS:** <https://www.nextgenscience.org/> (HS-LS Life Sciences PEs)
- **BC:** <https://curriculum.gov.bc.ca/curriculum/science>
- **Ontario:** <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
- **Alberta:** <https://www.alberta.ca/programs-of-study>

**Verification rule:** any syllabus-specific claim in a guide (course
code, performance-expectation code, topic placement, exam-expected
emphasis) must be checked against the corresponding source document
before shipping. Training-data recall is *not* an acceptable citation.
Place the source PDF under `rag/sources/<region>/...` per the `SAVE_AS`
column in `sources.txt`, and write a verbatim `*_extract.md` slice next
to it organised by HS Biology unit relevance.

## Naming convention

Flat, topic-indexed — no course prefix, no per-region split:

```
High School Biology/Study Guides/Unit_N_Topic.html
High School Biology/Practice Questions/Unit_N_Topic_Practice.html
High School Biology/Practice Questions/Solutions/Unit_N_Topic_Solutions.html
```

`N` is the topic index across the whole subject (1, 2, 3, …). Topic
uses underscores in filenames; avoid commas / ampersands.

Examples:
- `Unit_1_Cell_Structure_and_Function.html`
- `Unit_6_Molecular_Genetics.html`

### Why no "Unit N:" in the visible chrome (inherited from HS Math)

HS Biology is **topic-organised** across four curricula
(US-NGSS / ON / BC / AB), so a sequential unit number reads as noise —
students locate content by topic, not by sprint order. The filename
keeps `Unit_N_` for directory sort stability, cross-link permanence, and
build-index ordering; everything visible (title tag, hero h1, nav badge,
hero meta chips, section labels, worked-example labels, quiz numbers,
cross-section refs, footer) strips it.

**Visible chrome rules:**

- **Hero h1:** topic name only, no `Unit N:` prefix.
- **Nav badge (second chip):** topic code, not unit number — table below.
- **Hero meta chip "Unit N of 13":** removed entirely. Replace with a
  content-count chip like `7 sections` or a curriculum chip.
- **Section labels:** `Section 1 · …` (sequential within the unit). Same
  for Worked Example labels and quiz numbers (`§1 · Q1`).
- **Cross-section references inside the same guide:** `§1`, `§2`, …
  Cross-unit references use topic names ("see the Molecular Genetics
  guide"), not unit numbers.
- **HTML `id` attributes:** keep `s-6-1`, `s-6-2`, etc. for URL anchor
  stability. Visible labels change; the IDs are implementation detail.

**Topic-code mapping for nav badges (draft — confirm at first unit ship):**

| Filename | Nav badge |
|---|---|
| `Unit_1_Cell_Structure_and_Function.html` | `CELLS` |
| `Unit_2_Biochemistry_Molecules_of_Life.html` | `BIOCHEM` |
| `Unit_3_Cellular_Energetics.html` | `ENERGETICS` |
| `Unit_4_Cell_Division_and_the_Cell_Cycle.html` | `CELL CYCLE` |
| `Unit_5_Mendelian_Genetics_and_Heredity.html` | `GENETICS` |
| `Unit_6_Molecular_Genetics.html` | `DNA / RNA` |
| `Unit_7_Evolution_and_Natural_Selection.html` | `EVOLUTION` |
| `Unit_8_Biodiversity_and_Classification.html` | `TAXONOMY` |
| `Unit_9_Ecology_and_Ecosystems.html` | `ECOLOGY` |
| `Unit_10_Human_Anatomy_and_Physiology.html` | `A & P` |
| `Unit_11_Homeostasis.html` | `HOMEOSTASIS` |
| `Unit_12_Population_Biology.html` | `POPULATIONS` |

## Required `<title>` format

```
High School Biology — <Topic> | Dingrui Scholars
```

Examples:
- `High School Biology — Cell Structure and Function | Dingrui Scholars`
- `High School Biology — Evolution and Natural Selection | Dingrui Scholars`

`build-index.py` reads this verbatim to generate the home-page card.

## Topic list (initial proposal — draft, pending per-unit source verification)

This is the working scope (~12 units to span the full HS Biology range).
Lock per-unit ordering when the unit is opened for drafting. Each unit's
audit row should record the topic chosen and the syllabus codes it maps
to. **The per-unit US-NGSS / ON / BC / AB mapping below is a draft based
on typical curriculum placement and must be verified against the fetched
source PDFs before any Syllabus Map ships.**

| Unit | Topic | 🇺🇸 US NGSS (HS-LS) | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|---|
| 1  | Cell Structure and Function          | HS-LS1-2, HS-LS1-3 | SBI3U (Cell Bio) · SNC2D | Life Sciences 11 (cell bio) · Science 10 | Biology 20 (cells) · Science 10 |
| 2  | Biochemistry (Molecules of Life)     | HS-LS1-6 | SBI4U (Biochem unit) | Life Sciences 11 (biomolecules) | Biology 20 / 30 (biochem) |
| 3  | Cellular Energetics (Photosynthesis & Respiration) | HS-LS1-5, HS-LS1-7, HS-LS2-3, HS-LS2-5 | SBI4U (Metabolic Processes) | Life Sciences 11 (energy in cells) | Biology 20 (energy & matter exchange) |
| 4  | Cell Division and the Cell Cycle     | HS-LS1-4, HS-LS3-2 | SBI3U / SBI4U (cell division) | Life Sciences 11 (cell cycle) | Biology 30 (cell division) |
| 5  | Mendelian Genetics and Heredity      | HS-LS3-1, HS-LS3-2, HS-LS3-3 | SBI3U (Genetic Processes) | Life Sciences 11 (genetics) | Biology 30 (Mendelian genetics) |
| 6  | Molecular Genetics (DNA, RNA, Protein Synthesis) | HS-LS1-1, HS-LS3-1 | SBI4U (Molecular Genetics) | Anatomy & Physiology 12 / Life Sciences 11 | Biology 30 (molecular genetics) |
| 7  | Evolution and Natural Selection      | HS-LS4-1, HS-LS4-2, HS-LS4-3, HS-LS4-4, HS-LS4-5 | SBI3U (Evolution) | Life Sciences 11 (evolution) | Biology 30 (population change / evolution) |
| 8  | Biodiversity and Classification      | HS-LS4-5, HS-LS2-7 | SBI3U (Diversity of Living Things) | Life Sciences 11 (biodiversity / taxonomy) | Biology 20 (biodiversity) |
| 9  | Ecology and Ecosystems               | HS-LS2-1, HS-LS2-2, HS-LS2-4, HS-LS2-6, HS-LS2-7, HS-LS2-8 | SNC2D / SBI3U (ecosystems) | Science 10 (ecology) · Life Sciences 11 | Biology 20 (energy flow in ecosystems) |
| 10 | Human Anatomy and Physiology (systems) | HS-LS1-2, HS-LS1-3 | SBI4U (Homeostasis / systems) | Anatomy & Physiology 12 | Biology 20 / 30 (human systems) |
| 11 | Homeostasis                          | HS-LS1-3 | SBI4U (Homeostasis unit) | Anatomy & Physiology 12 (homeostasis) | Biology 30 (homeostasis / nervous & endocrine) |
| 12 | Population Biology                    | HS-LS2-1, HS-LS2-2, HS-LS2-6 | SBI3U (Population dynamics) | Life Sciences 11 (populations) | Biology 20 (population growth) |

**Status: draft — pending per-unit source verification.** The NGSS codes
and provincial placements above are typical-placement estimates. Confirm
each against the fetched `*_extract.md` slices before locking a unit's
Syllabus Map. Unit count and ordering may shift once sources are read
(e.g. Population Biology may fold into Ecology, or Human A&P may split
across multiple system-specific units).

## In-page conventions (the multi-syllabus pattern)

Inherited from HS Math. Each unit's HTML must include, near the top of
the page, a **Syllabus Map callout**:

```html
<aside class="syllabus-map">
  <div class="syllabus-map-label">Where this lives in your syllabus</div>
  <ul>
    <li><strong>🇺🇸 US NGSS:</strong> HS-LS1-2, HS-LS1-3 (structure &amp; function)</li>
    <li><strong>🇨🇦 Ontario:</strong> SBI3U — Cellular Biology; SNC2D foundations</li>
    <li><strong>🇨🇦 BC:</strong> Life Sciences 11 — Cell biology; Science 10 foundations</li>
    <li><strong>🇨🇦 Alberta:</strong> Biology 20 — Cells; Science 10 foundations</li>
  </ul>
</aside>
```

Reuse the CSS classes locked by HS Math (`syllabus-map`,
`syllabus-map-label`, `syllabus-map-grid`, `region-header`,
`region-chip`, `syllabus-note`, `honors-flag`, `feeder-link`,
`pill.region`, `pill.paper`, `pill.honors`, `syllabus-strip`) — see
`rag/style-guide.md` and any shipped HS Math unit. No new CSS needed at
the spec stage; inherit verbatim.

Where the curricula **genuinely diverge** (a topic emphasised in one but
absent or deferred in another), use a smaller inline callout:

```html
<div class="syllabus-note">
  <strong>Syllabus note.</strong> NGSS frames protein synthesis through
  HS-LS1-1 (structure of DNA → function). Ontario's SBI4U Molecular
  Genetics goes deeper into transcription/translation mechanism and
  biotechnology applications. If you're prepping SBI4U, read the
  going-deeper mechanism below; for NGSS, the conceptual model suffices.
</div>
```

Use these **sparingly** — only when there's a real difference a student
would feel.

### honors-flag (harder provincial stream)

Where a topic is honors-level OR is the harder Grade-12 / advanced
provincial stream (e.g. **Biology 30**, **SBI4U**, **Anatomy &
Physiology 12**) vs. the Grade-10/11 foundation, mark with an
`honors-flag` chip so a foundation-track student can skip cleanly.

### feeder-link (to IB / AP Biology)

Topics that feed forward flag the **IB Biology / AP Biology** units they
lead into. **Note: IB Biology and AP Biology products may not exist yet
in this repo** — write the feeder pointer as plain text now, and convert
to a hyperlink once the target unit ships. Do not link to a file that
does not exist.

## Standing principles

- **Topic-indexed, single set.** One unit per biological topic, not per
  US/provincial course. Filename `Unit_N_Topic.html`, sequential `N`.
- **Dual-goal contract** (inherited from IB Math HL via HS Math): every
  guide serves both the test-tomorrow crammer (≥ pass) and the depth
  student (5 on AP feeder / 100 on provincial). Cram cheat-sheet at top,
  worked examples, going-deeper detail in `<details>`. Canonical
  articulation in [`prompts/create-unit.md`](../../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every HS Biology
  Study Guide ships with paired `<span data-lang="en">` +
  `<span data-lang="zh">` markup and a working `toggleLang()` script in
  the **same commit** it is drafted. This is **non-negotiable for new
  subjects** — HS Biology does NOT repeat HS Math's English-first /
  retroactive-ZH detour. Each new SG lands visible in the landing-page
  ZH mode immediately.
- **Multi-syllabus crosswalk inside each guide.** Syllabus Map callout
  near the top of every unit listing matching codes in US NGSS (HS-LS),
  Ontario, BC, and Alberta. Inline Syllabus Notes only where a genuine
  divergence matters — sparingly.
- **Verification rule:** any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not acceptable.
- **honors-flag** chip for the harder provincial stream (Biology 30 /
  SBI4U / Anatomy & Physiology 12).
- **AP / IB feeder pointers** — flag the IB Biology / AP Biology units a
  topic feeds into. Hyperlink only once the target exists in this repo.

## Build-index integration (do at first unit ship)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Biology", "High School Biology", "chip-<unused>"),
   ```
   **Pick a chip colour not already used** by another subject (audit the
   current `SUBJECTS` palette first; HS Math took `chip-green`).

2. **No `WORD_PRIORITY` entry needed** — units are numbered sequentially
   with no sub-categories, so default numerical sort is correct.

3. Re-run `python scripts/build-index.py`. `index.html` may need a
   `<h2 class="section-title">High School Biology</h2>` + empty grid
   block inserted manually the first time, after which the script handles
   re-indexing. `parse_title()` already handles the no-colon HS-style
   title format (added for HS Math).

## Cross-references

- Dual-goal contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Sister subject spec (mirror this): [`rag/subjects/high_school_math.md`](./high_school_math.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Style tokens: [`rag/style-guide.md`](../style-guide.md)
- Source URLs (queued): [`sources.txt`](../../sources.txt) at repo root
- Official references (verify against, do not paraphrase from memory):
  - NGSS: <https://www.nextgenscience.org/>
  - BC: <https://curriculum.gov.bc.ca/curriculum/science>
  - Ontario: <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-science>
  - Alberta: <https://www.alberta.ca/programs-of-study>
