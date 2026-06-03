# High School Computer Science — Audit

Open punch list for the High School Computer Science product, scored
against the canonical generation prompt
([`prompts/create-unit.md`](../prompts/create-unit.md)) plus the
subject-specific spec at
[`rag/subjects/high_school_cs.md`](../rag/subjects/high_school_cs.md).

**Strategic posture (locked 2026-05-31):** One topic-organised
study-guide set serving the US (primary commercial target) and the top
three Canadian provincial curricula — Ontario, BC, Alberta — implicitly
through universal topic coverage. **There is no Common Core for CS;** the
US standards are the **CSTA K-12 Computer Science Standards (Level 3,
grades 9-12, bands 3A/3B)** plus the **AP Computer Science Principles
(CSP)** framework for foundations. Genuine curriculum differences
(including the mandated teaching language) are called out *inside* each
guide via Syllabus Map and Syllabus Note callouts, not by forking
content. This subject is **distinct from the existing AP CSA product**
(college-credit, Java-specific Computer Science A); HS CS is the broader
language-agnostic introductory tier that feeds into both AP CSP and AP
CSA. See spec for details.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / AP-feeder (CSP/CSA) / provincial-exam use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity
  but not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product. Per
the bilingual-from-start lock, each Study Guide ships EN + ZH in the
same commit. Practice Questions and AP-feeder cross-references live in
the [Digital Product Backlog](#digital-product-backlog) until those
product surfaces spin up.

Last reviewed: **2026-06-02** (**all 13 Study Guides shipped** —
bilingual from start, source-grounded, validate PASS, balanced EN/ZH
spans — on branch `hs_cs_sg`, awaiting review/FF to main. Practice +
Solutions and the static-visual upgrade are later waves.)

---

## Active Sprint — what we're working on now

### Sprint 1 — source-grounding + 13 bilingual Study Guides — **CLOSED 2026-06-02** (branch `hs_cs_sg`, awaiting FF to main)

**Shipped:** all 4 curricula source-grounded (CSTA L3 + AP CSP, ON ICS3U/4U,
BC ADST Computer Studies, AB CTS CSE — extracts + cached docs in `rag/sources/`),
Unit 1 Computational Thinking drafted as the bilingual template lock (cloned from
the Physics SG chrome), then Units 2-13 bulk-drafted via Sonnet copy-then-edit.
All 13 SGs ~1059-1224 lines, balanced EN/ZH spans, validate PASS. **CODE in
`<pre><code>`** (pseudocode + Python, un-translated, language-agnostic) rather than
KaTeX. **Feeders → AP CSA** where topics align (programming/control-flow/OOP/
data-structures). Divergence syllabus-notes baked in: OOP optional in US/BC
(honors); databases/SQL only in ON college stream (ICS4C); networks heaviest in
AP CSP; searching/sorting/efficiency are Grade-12.

| Unit | Topic | Spans | Unit | Topic | Spans |
|---|---|---|---|---|---|
| 1 | Computational Thinking (template) | 447 | 8 | OOP (intro) | 387 |
| 2 | Programming Fundamentals | 405 | 9 | Boolean Logic & Number Systems | 418 |
| 3 | Control Flow | 338 | 10 | Data, Databases & the Web | 400 |
| 4 | Functions & Modular Design | 411 | 11 | Networks & the Internet | 441 |
| 5 | Data Structures | 444 | 12 | Cybersecurity, Ethics & Society | 488 |
| 6 | Strings & Text Processing | 376 | 13 | Software Development Process | 446 |
| 7 | Searching & Sorting | 445 | | | |

**This completes the HS STEM Study-Guide goal** (Math 15 + Physics 12 + Chemistry
14 + Biology 12 + CS 13). **Next:** improvement runs (static visuals + audit)
across all four new subjects, then build-index + landing integration, then deploy.

#### Original Sprint 1 plan (historical)

### Sprint 1 — source-grounding + Unit 1 SG template lock — (historical)

**Goal.** Fetch the four curriculum source documents, then draft the
first full HS CS Study Guide for **Unit 1: Computational Thinking and
Algorithms** to lock the bilingual-from-start template. Proves the
Study Guide template (syllabus-map, region chips, honors-flag,
feeder-link, dual-goal sections, pseudocode + Python worked examples,
EN/ZH spans + `toggleLang()`) in one sprint so later sprints can
bulk-draft Units 2-13 from a validated design.

**Locked decisions (2026-05-31):**

- **Regions:** 4 columns — 🇺🇸 US (CSTA L3 / AP CSP), 🇨🇦 Ontario
  (ICS3U/ICS4U), 🇨🇦 British Columbia (Computer Studies 11/12 + ADST),
  🇨🇦 Alberta (CTS Computing Science / CSE).
- **Bilingual from start.** Unit 1 SG ships with paired
  `data-lang="en"` + `data-lang="zh"` spans and a working
  `toggleLang()` script in the same commit. Non-negotiable for this new
  subject.
- **Language-agnostic content.** Logic in pseudocode first; canonical
  worked code in Python; `syllabus-note` where a curriculum mandates a
  language. AP CSA (Java) stays a separate downstream product.
- **Inherit HS Math chrome.** Reuse the locked HS Math CSS classes
  (`syllabus-map`, `region-chip`, `syllabus-note`, `honors-flag`,
  `feeder-link`) and the no-"Unit N" visible-chrome convention.

**Sprint 1 deliverable contract:**

- Source-grounding: CSTA L3, AP CSP CED, ON ICS3U/ICS4U, BC Computer
  Studies 11/12, AB CTS CSE fetched into `rag/sources/<region>/` with
  `*_extract.md` companions for the Unit 1 (Computational Thinking)
  slice.
- One bilingual SG: Unit 1, ≥6 content sections following the dual-goal
  contract, syllabus-map cited verbatim from the extracts, region +
  honors-flag chips, feeder-link to AP CSP, pseudocode + Python worked
  examples, 8+ flashcards, 10+ readiness checklist items, paired EN/ZH
  spans + `toggleLang()`.
- `scripts/validate.sh` exit 0 (math conditional — Unit 1 may have none).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-sources** | Fetch CSTA L3, AP CSP CED, ON ICS3U/ICS4U, BC Computer Studies 11/12, AB CTS CSE; add rows to `sources.txt`; write Computational-Thinking `*_extract.md` slices | P0 | open — all four curricula PENDING |
| **S1-css** | Confirm / port HS Math `syllabus-map` / `syllabus-note` / `honors-flag` / `feeder-link` CSS for the CS layout | P1 | open |
| **S1-SG** | Draft `Unit_1_Computational_Thinking_and_Algorithms.html` (bilingual SG) to lock the template | P0 | open — blocked on S1-sources for verbatim codes |
| **S1-index** | Add HS CS to `scripts/build-index.py` `SUBJECTS` (unused chip colour); re-run; seed index.html subject-group block | P1 | open |

Build order: **S1-sources → S1-css + S1-SG → S1-index**.

---

## Standing principles

- **Topic-indexed, single set.** One unit per CS topic, not per region or
  per course. Filename: `Unit_N_Topic.html`, sequential `N` across the
  whole subject. Title format and naming locked in
  [`rag/subjects/high_school_cs.md`](../rag/subjects/high_school_cs.md).
- **No "Unit N" in visible chrome.** Topic-organised subject; the unit
  number is noise to students. Filenames keep `Unit_N_` for sort
  stability and cross-link permanence; everything visible strips it.
  (Inherited from HS Math; same rule book.)
- **Multi-syllabus crosswalk inside each guide.** Every unit ships with
  a Syllabus Map callout near the top listing matching codes in US
  (CSTA L3 / AP CSP), Ontario (ICS3U/ICS4U), BC (Computer Studies
  11/12 + ADST), and Alberta (CTS / CSE). Genuine divergences — including
  a mandated teaching language — get an inline Syllabus Note, sparingly.
- **Dual-goal contract** — every guide serves both the test-tomorrow
  crammer and the depth student. Cram cheat-sheet on top, going-deeper
  material at the bottom. Locked from IB Math HL / HS Math; canonical
  articulation in [`prompts/create-unit.md`](../prompts/create-unit.md).
- **Bilingual-from-start (LOCKED 2026-05-31).** Every SG ships EN + ZH
  (paired `data-lang` spans + `toggleLang()`) in the same commit.
  Non-negotiable for new subjects.
- **Language-agnostic framing.** Pseudocode first, Python as canonical
  worked code; `syllabus-note` where a curriculum mandates a language.
  AP CSA (Java) is a separate downstream product.
- **No HL flag.** Harder-stream topics (ICS4U vs ICS3U, BC Computer
  Studies 12 vs 11) use an `honors-flag` chip so a regular-track student
  can skip cleanly.
- **AP feeder pointers.** Foundations topics flag the supporting AP CSP
  Big Idea; programming-depth topics flag the AP CSA unit they feed.
  Hyperlink where the target unit already exists in this repo.
- **Verification rule.** Any syllabus-specific claim cites a fetched
  source doc in `rag/sources/`. Training-data recall is not acceptable.
- **Math is conditional.** `scripts/validate.sh` treats KaTeX math as
  conditional; a CS guide with no rendered math is valid.

---

## Cross-Unit Snapshot

All units **unbuilt** — subject just scaffolded. Fill in actual
section / worked-example / quiz counts as each unit ships.

| Unit | Topic | SG | P | S | Status |
|---|---|---|---|---|---|
| 1  | Computational Thinking and Algorithms          | &mdash; | &mdash; | &mdash; | **Sprint 1 queued** |
| 2  | Programming Fundamentals (variables, data types, I/O) | &mdash; | &mdash; | &mdash; | unbuilt |
| 3  | Control Flow (conditionals and loops)          | &mdash; | &mdash; | &mdash; | unbuilt |
| 4  | Functions and Modular Design                   | &mdash; | &mdash; | &mdash; | unbuilt |
| 5  | Data Structures (arrays, lists)                | &mdash; | &mdash; | &mdash; | unbuilt |
| 6  | Strings and Text Processing                    | &mdash; | &mdash; | &mdash; | unbuilt |
| 7  | Searching and Sorting                          | &mdash; | &mdash; | &mdash; | unbuilt |
| 8  | Object-Oriented Programming (Intro)            | &mdash; | &mdash; | &mdash; | unbuilt |
| 9  | Boolean Logic and Number Systems (binary/hex)  | &mdash; | &mdash; | &mdash; | unbuilt |
| 10 | Data, Databases and the Web                    | &mdash; | &mdash; | &mdash; | unbuilt |
| 11 | Networks and the Internet                      | &mdash; | &mdash; | &mdash; | unbuilt |
| 12 | Cybersecurity, Ethics and Society              | &mdash; | &mdash; | &mdash; | unbuilt |
| 13 | Software Development Process                    | &mdash; | &mdash; | &mdash; | unbuilt |

Hardware/robotics, game-design, and capstone-project units are
deliberately omitted from this initial list; revisit in a follow-on
sprint if demand surfaces.

---

## Source-grounding state

All four curricula **PENDING** — no documents fetched yet. Per the
verification rule, no per-unit syllabus map may be cited in a shipped
guide until the corresponding doc is in `rag/sources/` with an extract.

| Region | Course / doc | Course code(s) | Source state | Extract |
|---|---|---|---|---|
| 🇺🇸 US | CSTA K-12 CS Standards (Level 3) | CSTA 3A / 3B | PENDING | &mdash; |
| 🇺🇸 US | AP Computer Science Principles — CED | AP CSP | PENDING | &mdash; |
| 🇨🇦 ON | Introduction to Computer Science, Gr 11 | ICS3U | PENDING | &mdash; |
| 🇨🇦 ON | Computer Science, Gr 12 | ICS4U | PENDING | &mdash; |
| 🇨🇦 BC | Computer Studies 11/12 (+ ADST Computer Programming) | Computer Studies 11/12; ADST | PENDING | &mdash; |
| 🇨🇦 AB | Computing Science under CTS | CTS — CSE cluster | PENDING | &mdash; |

Official references (verify against, do not paraphrase from memory):

- CSTA K-12 CS Standards: <https://csteachers.org/k12-standards/>
- AP CSP: <https://apcentral.collegeboard.org/courses/ap-computer-science-principles>
- Ontario (Computer Studies): <https://www.dcp.edu.gov.on.ca/en/curriculum/secondary-computer-studies>
- BC (ADST): <https://curriculum.gov.bc.ca/curriculum/adst>
- Alberta: <https://www.alberta.ca/programs-of-study>

---

## Topic Scope Reminders (multi-syllabus)

These are **draft placeholder cross-references — pending per-unit source
verification.** Treat as starting points; verify against the fetched
source docs in `rag/sources/` before locking any unit's syllabus map.

| Unit topic | 🇺🇸 CSTA L3 / AP CSP | 🇨🇦 ON | 🇨🇦 BC | 🇨🇦 AB |
|---|---|---|---|---|
| Computational thinking & algorithms | CSTA 3A/3B Algorithms · CSP BI 4 | ICS3U algorithm design | Comp Studies 11 problem-solving | CSE computational thinking |
| Programming fundamentals | CSTA 3A-AP-13/-14 · CSP variables | ICS3U programming basics | Comp Studies 11 programming | CSE intro programming |
| Control flow | CSTA 3A-AP-15/-16 · CSP selection/iteration | ICS3U control structures | Comp Studies 11 control structures | CSE structured programming |
| Functions & modular design | CSTA 3A-AP-17/-18 · CSP procedural abstraction | ICS3U/ICS4U modular design | Comp Studies 11/12 procedures | CSE modular design |
| Data structures (arrays, lists) | CSTA 3B-AP-12/-13 · CSP lists | ICS4U data structures | Comp Studies 12 data structures | CSE data structures |
| Strings & text processing | CSTA 3A-AP strings · CSP data | ICS3U/ICS4U strings | Comp Studies 11/12 strings | CSE text processing |
| Searching & sorting | CSTA 3B-AP-11 efficiency · CSP algorithms | ICS4U searching/sorting | Comp Studies 12 algorithms | CSE algorithms |
| OOP (intro) | CSTA 3B-AP-15 · CSP abstraction | ICS4U OOP | Comp Studies 12 OOP | CSE OOP intro |
| Boolean logic & number systems | CSTA 3A/3B-CS data rep · CSP BI 2 (Data) | ICS3U data representation | Comp Studies 11 number systems | CSE digital logic |
| Data, databases & the web | CSTA 3A/3B-DA · CSP BI 2 (Data) | ICS4U databases/web | Comp Studies 12 databases/web | CSE databases/web |
| Networks & the internet | CSTA 3A/3B-NI · CSP BI 5 (Systems & Networks) | ICS3U/ICS4U networks | Comp Studies 11/12 networks | CSE networking |
| Cybersecurity, ethics & society | CSTA 3A/3B-IC & -NI · CSP BI 6 (Impact) | ICS3U/ICS4U ethical issues | Comp Studies 11/12 ethics & security | CSE ethics/security |
| Software development process | CSTA 3B-AP-16/-22 · CSP BI 1 (Creative Dev) | ICS4U software engineering | Comp Studies 12 project mgmt | CSE project/systems dev |

---

## Closed Sprints

### Sprint 0 — closed 2026-05-31

Subject scaffolding shipped: subject spec
([`rag/subjects/high_school_cs.md`](../rag/subjects/high_school_cs.md)),
this audit, and the empty folder structure
(`Study Guides/`, `Practice Questions/Solutions/`). Topic-organised,
multi-syllabus posture (US CSTA L3 / AP CSP + ON / BC / AB) locked from
the outset, mirroring HS Math. No Study Guide HTML drafted.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-2**~~ | Author audit | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-3**~~ | Create empty folder structure | P0 | ✅ shipped 2026-05-31 |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint.

| ID  | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice Questions product (MC + free-response coding sets per unit, with Solutions companion mirroring HS Math / IB Math HL pattern) | Needs Study Guide content first to anchor question scope. Open after ≥3 study guides ship. |
| DP-2 | AP CSP / AP CSA cross-reference cards on each guide | Format and feeder-mapping templates need a separate scoping pass; coordinate with the existing AP CSA product. |
| DP-3 | Per-province exam / culminating-task overlays (ON ICS4U project, BC Computer Studies) on top of the topic guides | Layer onto existing guides; deferred until Canadian audience demand is measured. |
| DP-4 | Per-language code renderings (Java / JavaScript alongside Python) for language-divergent curricula | Pseudocode + Python is the locked default; multi-language toggle is a richer-product feature. |
| DP-5 | Hardware / robotics / game-design topic bundle | Implementation-specific electives, not universal foundations; revisit if topic-set has reach. |
| DP-6 | Interactive code playground (run-in-browser) on each guide | Needs a sandboxed execution surface; well beyond the self-contained-HTML constraint. |

---

## How to update this file

When closing a sprint item, mark with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When a sprint clears,
collapse into a single line in `## Closed Sprints` and promote the
next sprint up.

When standing principles need revision, edit them here; route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_cs.md`](../rag/subjects/high_school_cs.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork
the contract.

When a unit ships, fill in its row of the cross-unit snapshot with
actual section / worked-example / quiz counts.
