# Subject Spec — High School Computer Science (multi-syllabus, topic-organised)

## Identity

- **Display (section heading):** High School Computer Science
- **Display (hero chip):** High School Computer Science
- **Directory:** `High School Computer Science/`
- **Audit:** `High School Computer Science/AUDIT.md`

## Strategic posture (locked 2026-05-31)

**One study-guide set, organised by computer-science topic.** Intro CS
is intro CS — computational thinking, variables and data types, control
flow, functions, arrays, OOP basics, and the binary/Boolean foundations
cover the same scope in every modern HS curriculum. Each guide is
written once around the universal topic, with **syllabus-specific
callouts** inside the page where coverage genuinely diverges.

**Market priority (largest → smallest, English-language):**

1. **US** — primary commercial target. Important nuance: **there is no
   "Common Core" for computer science.** Common Core covers Math and
   English Language Arts only. The relevant US standards for HS CS are:
   - **CSTA K-12 Computer Science Standards — Level 3 (grades 9-12),
     bands 3A and 3B.** This is the de-facto national framework adopted
     or adapted by most US states.
   - **AP Computer Science Principles (CSP) framework** — the College
     Board's foundations-of-CS course (Big Ideas: Creative Development,
     Data, Algorithms & Programming, Computer Systems & Networks, Impact
     of Computing). CSP is the natural college-credit feeder for the
     foundations covered here.
2. **Canadian provinces:** Ontario, British Columbia, Alberta —
   secondary target. Repo author is based in Canada, so this audience is
   acknowledged explicitly and tested against per-unit.

We do **not** ship four separate course tracks. We ship one
topic-indexed set that serves all four curricula implicitly.

**Distinct from AP CSA.** This subject is *not* the existing
[`AP CSA`](../../AP%20CSA/) product. AP CSA is the College Board's
college-credit, Java-specific Computer Science **A** course (objects,
inheritance, ArrayList, 2D arrays, recursion in Java). HS Computer
Science is the broader, **language-agnostic introductory** tier that
feeds *into* both AP CSP (foundations) and AP CSA (programming depth).
Where a topic feeds AP CSA or AP CSP, flag it with a `feeder-link`.

## Source documents

To be catalogued in [`sources.txt`](../../sources.txt) at the repo root.
Status `[x]` = PDF/standards doc pulled to `rag/sources/`; `[ ]` =
queued; `[!]` = URL is a publications landing page, not a direct PDF
link.

| Region | Course / doc | Course code(s) | Status (2026-05-31) |
|---|---|---|---|
| 🇺🇸 US | CSTA K-12 Computer Science Standards (Level 3) | CSTA 3A / 3B (grades 9-12) | PENDING `[ ]` |
| 🇺🇸 US | AP Computer Science Principles — Course & Exam Description | AP CSP | PENDING `[ ]` |
| 🇨🇦 ON | Introduction to Computer Science, Grade 11 (University) | ICS3U | PENDING `[ ]` |
| 🇨🇦 ON | Computer Science, Grade 12 (University) | ICS4U | PENDING `[ ]` |
| 🇨🇦 BC | Computer Studies 11 / Computer Studies 12 (+ ADST Computer Programming components) | Computer Studies 11/12; ADST | PENDING `[ ]` |
| 🇨🇦 AB | Computing Science under Career and Technology Studies | CTS — Computing Science (CSE) cluster | PENDING `[ ]` |

**Source-grounding state: PENDING for all four curricula.** No standards
documents have been fetched yet. All per-unit mappings in this spec are
**draft — pending per-unit source verification** and must not be cited
in a shipped guide until the corresponding document is in
`rag/sources/`.

**Verification rule:** any syllabus-specific claim in a guide (course
code, topic placement, exam-expected emphasis, standard identifier)
must be checked against the corresponding source document before
shipping. Training-data recall is *not* an acceptable citation. Place
the source PDF / standards export under `rag/sources/<region>/...` per
the `SAVE_AS` column once fetched.

## Naming convention

Flat, topic-indexed — no course prefix, no per-region split:

```
High School Computer Science/Study Guides/Unit_N_Topic.html
High School Computer Science/Practice Questions/Unit_N_Topic_Practice.html
High School Computer Science/Practice Questions/Solutions/Unit_N_Topic_Solutions.html
```

`N` is the topic index across the whole subject (1, 2, 3, …). Topic
uses underscores in filenames; avoid commas / ampersands.

Examples:
- `Unit_1_Computational_Thinking_and_Algorithms.html`
- `Unit_8_Object-Oriented_Programming_Intro.html`

### Why no "Unit N:" in the visible chrome (inherited from HS Math)

HS Computer Science is **topic-organised** across four curricula (US
CSTA/CSP / ON / BC / AB), so a sequential unit number reads as noise —
students locate content by topic, not by sprint order. The filename
keeps `Unit_N_` for directory sort stability and cross-link permanence;
everything visible (title tag, hero h1, nav badge, hero meta chips,
section labels, worked-example labels, quiz numbers, cross-section
refs, footer) strips it.

**Visible chrome rules:**

- **Hero h1:** topic name only, no `Unit N:` prefix.
- **Nav badge (second chip):** topic code, not unit number — table below.
- **Hero meta chip "Unit N of 13":** removed entirely. Replace with a
  content-count chip like `7 sections` or a curriculum chip.
- **Section labels:** `Section 1 · …` instead of `Section 8.1 · …`.
  Same for Worked Example labels and quiz numbers (`§1 · Q1`).
- **Cross-section references inside the same guide:** `§1`, `§2`, …
  Cross-unit references use topic names ("see the Control Flow guide"),
  not unit numbers.
- **HTML `id` attributes:** keep `s-8-1`, `s-8-2`, etc. for URL anchor
  stability. Visible labels change; the IDs are implementation detail.

## Required `<title>` format

```
High School Computer Science — <Topic> | Dingrui Scholars
```

Examples:
- `High School Computer Science — Computational Thinking and Algorithms | Dingrui Scholars`
- `High School Computer Science — Object-Oriented Programming (Intro) | Dingrui Scholars`

`build-index.py` reads this verbatim to generate the home-page card.

### Topic-code mapping for nav badges

| Filename | Nav badge |
|---|---|
| `Unit_1_Computational_Thinking_and_Algorithms.html` | `COMP THINK` |
| `Unit_2_Programming_Fundamentals.html` | `PROG FUND` |
| `Unit_3_Control_Flow.html` | `CONTROL` |
| `Unit_4_Functions_and_Modular_Design.html` | `FUNCTIONS` |
| `Unit_5_Data_Structures.html` | `DATA STRUCT` |
| `Unit_6_Strings_and_Text_Processing.html` | `STRINGS` |
| `Unit_7_Searching_and_Sorting.html` | `SEARCH/SORT` |
| `Unit_8_Object-Oriented_Programming_Intro.html` | `OOP` |
| `Unit_9_Boolean_Logic_and_Number_Systems.html` | `LOGIC/BIN` |
| `Unit_10_Data_Databases_and_the_Web.html` | `DATA/WEB` |
| `Unit_11_Networks_and_the_Internet.html` | `NETWORKS` |
| `Unit_12_Cybersecurity_Ethics_and_Society.html` | `SEC/ETHICS` |
| `Unit_13_Software_Development_Process.html` | `SDLC` |

## Topic list (initial proposal, ~13 units to span the full scope)

**Status: draft — pending per-unit source verification.** This is the
working scope grounded in the four curricula's foundations courses. Lock
per-unit ordering and the verbatim standard codes when the unit is
opened for drafting (after the corresponding source doc is fetched).
Each unit's audit row should record the topic chosen and the syllabus
codes it maps to.

| Unit | Topic | 🇺🇸 CSTA L3 / AP CSP | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|---|
| 1  | Computational Thinking and Algorithms | CSTA 3A/3B Algorithms · CSP Big Idea 4 (Algorithms & Programming) | ICS3U algorithm design | Computer Studies 11 problem-solving | CSE intro / computational thinking |
| 2  | Programming Fundamentals (variables, data types, I/O) | CSTA 3A-AP-13/-14 · CSP variables & data abstraction | ICS3U programming basics | Computer Studies 11 programming | CSE intro programming |
| 3  | Control Flow (conditionals and loops) | CSTA 3A-AP-15/-16 · CSP selection & iteration | ICS3U control structures | Computer Studies 11 control structures | CSE structured programming |
| 4  | Functions and Modular Design | CSTA 3A-AP-17/-18 · CSP procedural abstraction | ICS3U/ICS4U modular design | Computer Studies 11/12 procedures | CSE modular design |
| 5  | Data Structures (arrays, lists) | CSTA 3B-AP-12/-13 · CSP lists & collections | ICS4U data structures | Computer Studies 12 data structures | CSE data structures |
| 6  | Strings and Text Processing | CSTA 3A-AP string manipulation · CSP data | ICS3U/ICS4U strings | Computer Studies 11/12 strings | CSE text processing |
| 7  | Searching and Sorting | CSTA 3B-AP-11 algorithm efficiency · CSP algorithms | ICS4U searching & sorting | Computer Studies 12 algorithms | CSE algorithms |
| 8  | Object-Oriented Programming (Intro) | CSTA 3B-AP-15 · CSP procedural/data abstraction | ICS4U OOP | Computer Studies 12 OOP | CSE OOP intro |
| 9  | Boolean Logic and Number Systems (binary/hex) | CSTA 3A/3B-CS data representation · CSP Big Idea 2 (Data) | ICS3U data representation | Computer Studies 11 number systems | CSE digital logic / number systems |
| 10 | Data, Databases and the Web | CSTA 3A/3B-DA · CSP Big Idea 2 (Data) | ICS4U databases / web | Computer Studies 12 databases/web | CSE databases / web design |
| 11 | Networks and the Internet | CSTA 3A/3B-NI · CSP Big Idea 5 (Computer Systems & Networks) | ICS3U/ICS4U networks | Computer Studies 11/12 networks | CSE networking |
| 12 | Cybersecurity, Ethics and Society | CSTA 3A/3B-IC & -NI security · CSP Big Idea 6 (Impact of Computing) | ICS3U/ICS4U environmental & ethical issues | Computer Studies 11/12 ethics & security | CSE ethics / security |
| 13 | Software Development Process | CSTA 3B-AP-16/-22 project lifecycle · CSP Big Idea 1 (Creative Development) | ICS4U software engineering | Computer Studies 12 project management | CSE project / systems development |

**Language-agnostic framing.** The four curricula differ on the
required teaching language (ON ICS commonly Python/Java; BC ADST
language-flexible; AB CTS language-flexible; AP CSP language-agnostic /
pseudocode, AP CSA Java). Guides therefore present logic in
**pseudocode first**, with a worked code rendering in a **mainstream
language (Python)** as the canonical example, and a `syllabus-note`
where a curriculum mandates a specific language. Avoid hard-coding any
single language as "the" language. (AP CSA — Java-specific — remains a
separate downstream product.)

Hardware/robotics, game design, and capstone-project units are
deliberately omitted from this initial list — they are
implementation-specific electives rather than universal foundations.
Decision deferred to a follow-on sprint if the topic-set proves demand.

## In-page conventions (the multi-syllabus pattern)

Each unit's HTML must include, near the top of the page (immediately
under the hero or in the first section), a **Syllabus Map callout**
(inherited from HS Math):

```html
<aside class="syllabus-map">
  <div class="syllabus-map-label">Where this lives in your syllabus</div>
  <ul>
    <li><strong>🇺🇸 US (CSTA / AP CSP):</strong> CSTA 3A-AP-15, 3A-AP-16; AP CSP Big Idea 4 (Algorithms &amp; Programming)</li>
    <li><strong>🇨🇦 Ontario:</strong> ICS3U — Programming strand (control structures)</li>
    <li><strong>🇨🇦 BC:</strong> Computer Studies 11 — control structures</li>
    <li><strong>🇨🇦 Alberta:</strong> CTS — Computing Science (CSE) structured programming</li>
  </ul>
</aside>
```

CSS classes `syllabus-map`, `syllabus-map-label`, `syllabus-map-grid`,
`region-header`, `region-chip`, `syllabus-note`, `honors-flag`,
`feeder-link` are **inherited from the HS Math design** — reuse the
locked HS Math definitions (see `rag/style-guide.md` and any shipped HS
Math unit). Adjust only if a CS-specific layout genuinely needs it.

Where the curricula **genuinely diverge** (a topic emphasised in one
but absent or deferred in another, or a mandated language), use a
smaller inline callout:

```html
<div class="syllabus-note">
  <strong>Syllabus note.</strong> Ontario's ICS3U teaches this in a
  specific language chosen by the school (often Python); AP CSP assesses
  it in language-agnostic pseudocode. The logic is identical — read the
  pseudocode box first, then the Python rendering.
</div>
```

Use these **sparingly** — only when there's a real difference a
student would feel.

**Honors / harder-stream flag.** Use the `honors-flag` chip where a
topic is the harder stream — e.g. **ICS4U** (Grade 12) content sitting
in a guide whose floor is ICS3U (Grade 11), or BC Computer Studies 12
vs. 11. Lets a regular-track student skip cleanly.

**Feeder pointers.** Where a topic feeds a downstream Dingrui product,
add a `feeder-link`: foundations topics (data, algorithms, internet,
impact) feed **AP CSP**; programming-depth topics (OOP, arrays/lists,
searching/sorting, recursion-adjacent) feed **AP CSA**. Hyperlink where
the target unit already exists in this repo (e.g.
`AP CSA/Study Guides/...`).

**Math content is conditional.** `scripts/validate.sh` treats KaTeX
math as **conditional** — CS guides may have little or no rendered math
(Boolean algebra and number-base conversion in Unit 9 are the main
candidates). A CS guide with no `$$...$$` math is valid; do not force
math in to satisfy the validator.

## Standing principles

- **Dual-goal contract** (inherited from IB Math HL / HS Math): every
  guide serves both the test-tomorrow crammer (≥ pass) and the depth
  student (5 on AP CSP/CSA feeder / 100 on provincial). Cram cheat-sheet
  at top, worked examples (pseudocode + Python), going-deeper material
  in `<details>`. Canonical articulation in
  [`prompts/create-unit.md`](../../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every Study
  Guide ships with paired `<span data-lang="en">` + `<span
  data-lang="zh">` markup and a working `toggleLang()` `<script>` in the
  **same commit**. This is **non-negotiable for new subjects** — no
  English-only phase, no retroactive ZH wave. Each new SG lands visible
  in the landing-page ZH mode immediately.
- **No HL flag** (there's no HL tier in HS CS). Where a topic is the
  harder stream (ICS4U vs ICS3U, BC Computer Studies 12 vs 11, AP
  CSA-depth vs CSP-foundations), mark with an `honors-flag` chip.
- **AP feeder pointers** — foundations topics flag the AP CSP Big Idea
  they support; programming-depth topics flag the AP CSA unit they feed.
  Hyperlink where the target unit already exists in this repo.
- **Verification rule:** any syllabus-specific claim cites a fetched
  source doc in `rag/sources/`. Training-data recall is not acceptable.

## Build-index integration (do at first unit ship)

When the first Study Guide HTML lands, update `scripts/build-index.py`:

1. Add to `SUBJECTS`:
   ```python
   ("High School Computer Science", "High School Computer Science", "chip-XXXX"),
   ```
   **Chip colour:** pick one **not already used** by an existing subject
   (HS Math uses `chip-green`; check the current `SUBJECTS` list and
   choose an unused colour token).

2. **No `WORD_PRIORITY` entry needed** — units are numbered
   sequentially with no sub-categories, so default numerical sort is
   correct. (Re-use the HS Math no-colon `parse_title()` handling
   already in `build-index.py`.)

3. Re-run `python scripts/build-index.py`. `index.html` may need a
   `<h2 class="section-title">High School Computer Science</h2>` + empty
   grid block inserted manually the first time, after which the script
   handles re-indexing.

## Cross-references

- Dual-goal contract: [`prompts/create-unit.md`](../../prompts/create-unit.md)
- Audit template: [`rag/AUDIT_TEMPLATE.md`](../AUDIT_TEMPLATE.md)
- Sibling spec to mirror: [`rag/subjects/high_school_math.md`](high_school_math.md)
- AP CSA spec (distinct downstream product): [`rag/subjects/ap_csa.md`](ap_csa.md)
- Style tokens: [`rag/style-guide.md`](../style-guide.md)
- Source URLs (queued): [`sources.txt`](../../sources.txt) at repo root
- Official references (verify against, do not paraphrase from memory):
  - CSTA K-12 CS Standards: <https://csteachers.org/k12-standards/>
  - AP CSP: <https://apcentral.collegeboard.org/courses/ap-computer-science-principles>
  - Ontario (Computer Studies): <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-computer-studies>
  - BC (ADST): <https://curriculum.gov.bc.ca/curriculum/adst>
  - Alberta: <https://www.alberta.ca/programs-of-study>
