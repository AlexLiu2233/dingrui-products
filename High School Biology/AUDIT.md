# High School Biology — Audit

Open punch list for the High School Biology product, scored against the
canonical generation prompt ([`prompts/create-unit.md`](../prompts/create-unit.md))
plus the subject-specific spec at
[`rag/subjects/high_school_biology.md`](../rag/subjects/high_school_biology.md).

**Strategic posture (locked 2026-05-31):** One topic-organised study-guide
set serving the **US NGSS High School Life Sciences (HS-LS)** standard
(primary commercial target) and the top three Canadian provincial
curricula — Ontario, BC, Alberta — implicitly through universal topic
coverage. Genuine curriculum differences are called out *inside* each
guide via Syllabus Map and Syllabus Note callouts, not by forking
content. See spec for details.

> **NUANCE — NGSS, not Common Core.** There is **no Common Core for
> science** (Common Core covers Mathematics and ELA only). The US science
> standard is the **Next Generation Science Standards (NGSS)**; the
> biology slice is the **Life Sciences (LS)** domain: HS-LS1, HS-LS2,
> HS-LS3, HS-LS4. Cite NGSS performance-expectation codes
> (e.g. `HS-LS1-1`), never a "Common Core" science code.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / AP-feeder / provincial-exam use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity
  but not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product as the
primary surface. Practice Questions and their Solutions companions live
in the [Digital Product Backlog](#digital-product-backlog) until the
Study Guide corpus anchors their scope. **Bilingual (EN/ZH) is NOT a
backlog item** — it is locked into every Study Guide from the first
commit (see Standing principles).

Last reviewed: **2026-06-02** (**all 12 Study Guides shipped** —
bilingual from start, source-grounded, validate PASS, balanced EN/ZH
spans — on branch `hs_biology_sg`, awaiting review/FF to main. Practice +
Solutions and the static-visual upgrade are later waves.)

---

### Sprint — Deployment-Readiness Audit — 2026-06-03 (findings; audit-only)

**✅ RESOLVED 2026-06-03 (fix sprint on `hs_stem_complete`):** D1 dead-toggle + D4 localStorage normalized across all 66 SGs (`1b749f3`); A6 CJK-in-`	ext{}` cleared in all 25 affected SGs (`4ff2b62`, `5a7c0c3`); P2 favicon `../LOGO.png`→`../../LOGO.png` (`e580250`); B3 going-deeper added to Chem U4/U5 (`b644a18`). Findings below retained as the audit record.

> **Correction:** the Biology Unit 12 "D1 mismatch (374/375)" was a FALSE POSITIVE — the file is balanced **434/434**; no fix needed (its A6 was real and is fixed).


Scored against `rag/study-guide-audit-checklist.md` Sections **A**, **B**,
**D1** with the HS-STEM deploy adjustments (`rag/hs-stem-deploy-audit.md`):
E3 / C1 / interactivity EXCLUDED (figures + interactivity scrapped
2026-06-03 — prose + KaTeX only); "no stray visual/JS" sweep ADDED; HS
no-colon title + 4-column syllabus map + no-feeder-link conventions treated
as correct (not flagged); Section **D1 (EN==ZH) is an active hard gate**.
**Audit-only — no `.html` edited.** Scope: all 12 SGs in
`High School Biology/Study Guides/*.html`.

**Mechanical results (all 12):** `validate.sh` exits 0 on every file
(A8 PASS; odd-`$` WARN benign per deploy doc). Titles all conform to the HS
no-colon form `High School Biology — <Topic> | Dingrui Scholars` (A1 PASS).
Design tokens (`--accent`), CJK font fallback (A3), dark-mode
(`[data-theme="dark"]`), `@media print`, and `@media (max-width: 600px)`
blocks present on every file (A2/A5/A11/A12 PASS). Bilingual toggle infra
(`lang-zh` CSS + `id="langToggle"` + `toggleLang()`) present on every file
(A13 infra PASS). Required structural sections (hero, sticky sidebar TOC,
footer, progress bar, 4-column syllabus map US-NGSS/ON/BC/AB) present on all
12 (A10 PASS). TOC anchors all resolve — the lone "unresolved" hit per file
is the `${e.target.id}` template literal inside the IntersectionObserver JS,
a false positive (A7 PASS). **No stray visuals:** 0 `<svg>` / `<img>` /
`<canvas>` anywhere; each file carries exactly 3 `<script>` tags — 2 KaTeX
0.16.9 CDN (A4 allowed) + 1 inline quiz/toggle script — no chart/non-quiz JS
(no-stray-visual/JS sweep PASS). **No feeder `<a>` links** exist (correct —
no IB/AP Biology product; feeders are prose; not flagged). Worked-example
density healthy (7–12 per file). Flashcard decks ≥ 8 (B5 PASS).

| Finding | File: gap | Tier | Status |
|---|---|---|---|
| **D1-1** | Unit 12 Population Biology: `data-lang` span count mismatch EN=374 / ZH=375 — malformed nesting at lines 596–603 (an `en` span wraps a nested `<ul>` whose `<li>`s each carry their own en/zh pairs, then a separate `zh` span at line 603 duplicates that summary), leaving one unpaired span. Hard-gate D1 failure — blocks deploy. | P0 | Open |
| **A6-1** | Unit 12 Population Biology: CJK characters inside `\text{}` in the ZH math spans — `\text{出生率}`, `\text{死亡率}` (line 459) and `\text{增长率}` (line 512). KaTeX renders these with fallback glyphs / broken layout; move the Chinese outside the math (e.g. `$r = b - d$` with the gloss in prose). | P0 | Open |
| **D4-1** | All 12 files: `toggleLang()` both writes (`localStorage.setItem('lang', …)`) and reads (`localStorage.getItem('lang')`) language state (script lines ~945–946), violating the locked 2026-05-21 rule that every page defaults to English on load and `toggleLang()` does not touch `localStorage`. Repo-wide pattern; flag for a single sweep fix. | P1 | Open |
| **A1-fav** | All 12 files: favicon `<link rel="icon" href="../LOGO.png">` resolves to `High School Biology/LOGO.png`, which does not exist (the asset lives only at repo root `./LOGO.png`; correct relative path is `../../LOGO.png`). Cosmetic broken favicon, not an `<a>` feeder link; identical convention error in HS Math siblings, so repo-wide, not Biology-specific. | P2 | Open |

**Per-file verdict:**

| File | Verdict |
|---|---|
| Unit 1 Cell Structure | **Clean** (A1-fav P2 only) |
| Unit 2 Biochemistry | **Clean** (A1-fav P2 only) |
| Unit 3 Cellular Energetics | **Clean** (A1-fav P2 only) |
| Unit 4 Cell Division | **Clean** (A1-fav P2 only) |
| Unit 5 Mendelian Genetics | **Clean** (A1-fav P2 only) |
| Unit 6 Molecular Genetics | **Clean** (A1-fav P2 only) |
| Unit 7 Evolution | **Clean** (A1-fav P2 only) |
| Unit 8 Biodiversity/Taxonomy | **Clean** (A1-fav P2 only) |
| Unit 9 Ecology | **Clean** (A1-fav P2 only) |
| Unit 10 Anatomy & Physiology | **Clean** (A1-fav P2 only) |
| Unit 11 Homeostasis | **Clean** (A1-fav P2 only) |
| Unit 12 Population Biology | **FAIL** — D1-1 (P0 span mismatch) + A6-1 (P0 CJK-in-`\text{}`) |

The D4-1 (P1) and A1-fav (P2) findings apply to all 12 uniformly and are
not unit-specific defects.

**Overall verdict: NOT deploy-ready — 1 file blocks.** 11 of 12 SGs are
clean and deploy-ready (modulo the two repo-wide P1/P2 sweeps). **Unit 12
Population Biology fails the deploy gate** on two P0s: the D1 EN/ZH span
parity mismatch and CJK characters inside `\text{}`. Fix Unit 12's two P0s
(re-balance the lines 596–603 span nesting; pull Chinese out of the three
`\text{}` blocks at lines 459/512), then the corpus clears. **Totals: P0 = 2
(both in Unit 12), P1 = 1 (D4-1, repo-wide), P2 = 1 (A1-fav, repo-wide).**

---

## Active Sprint — what we're working on now

### Sprint 1 — source-grounding + 12 bilingual Study Guides — **CLOSED 2026-06-02** (branch `hs_biology_sg`, awaiting FF to main)

**Shipped:** all 4 curricula source-grounded (NGSS HS-LS, ON SBI3U/4U, BC
Life Sci 11 + A&P 12, AB Bio 20/30 — extracts + cached PDFs in `rag/sources/`),
Unit 1 Cell Structure drafted as the bilingual template lock (cloned from the
Physics SG chrome), then Units 2-12 bulk-drafted via Sonnet copy-then-edit.
All 12 SGs ~929-1022 lines, balanced EN/ZH spans, validate PASS. **No feeder
links** (no IB/AP Biology product exists in the repo — "what this feeds into"
is prose). Divergence syllabus-notes baked in: Hardy-Weinberg quantitative is
AB-only (Bio 30; NGSS excludes); taxonomy absent from NGSS; biochemical-pathway
depth deepest in SBI4U; human A&P/homeostasis concentrated in Gr-12 streams
(honors-flagged).

| Unit | Topic | Spans (EN=ZH) | Unit | Topic | Spans |
|---|---|---|---|---|---|
| 1 | Cell Structure (template) | 418 | 7 | Evolution | 407 |
| 2 | Biochemistry | 399 | 8 | Biodiversity/Taxonomy | 501 |
| 3 | Cellular Energetics | 425 | 9 | Ecology | 435 |
| 4 | Cell Division | 470 | 10 | Anatomy & Physiology | 416 |
| 5 | Mendelian Genetics | 451 | 11 | Homeostasis | 435 |
| 6 | Molecular Genetics | 404 | 12 | Population Biology | 434 |

**Next:** build-index + landing integration (12 Bio cards), then CS SGs (last
subject), then static-visual upgrade + P+S across all four.

#### Original Sprint 1 plan (historical)

### Sprint 1 — source-grounding + Unit 1 SG template lock — (historical)

First real sprint. Two goals, in order: (1) fetch the priority source
documents and write verbatim `*_extract.md` slices so the Syllabus Map
can cite real codes; (2) draft the **Unit 1 (Cell Structure and
Function)** bilingual Study Guide to lock the HS Biology template — the
same way HS Math locked its template on its first full unit.

**Locked decisions (2026-05-31):**

- **4 curriculum columns from the start:** 🇺🇸 US NGSS (HS-LS),
  🇨🇦 Ontario, 🇨🇦 BC, 🇨🇦 Alberta. (HS Math shipped 3 columns first and
  retrofitted AB; HS Biology ships 4 from Unit 1.)
- **Bilingual-from-start.** Unit 1 SG ships with paired EN/ZH spans +
  `toggleLang()` in the same commit. Non-negotiable for this subject.
- **Inherit HS Math chrome verbatim** — `syllabus-map`, `syllabus-note`,
  `honors-flag`, `feeder-link`, grade-by-region nav table, region/paper
  chip taxonomy. No new CSS design work; reuse the locked HS Math classes.
- **honors-flag** marks the harder provincial stream (Biology 30 / SBI4U
  / Anatomy & Physiology 12).
- **Feeder pointers** to IB Biology / AP Biology are **plain text** until
  those products exist — do not link to non-existent files.

**Sprint 1 deliverable contract:**

- Priority sources fetched (NGSS HS-LS + at least one provincial doc per
  region) into `rag/sources/<region>/`, each with a verbatim
  `*_extract.md` slice scoped to Cell Structure & Function.
- Unit 1 (Cell Structure and Function) bilingual SG: 7 content sections
  satisfying the dual-goal contract, 8-row grade-by-region nav, Syllabus
  Map cited verbatim from the extracts (4 columns), honors-flag pattern,
  feeder pointer to IB/AP Biology (plain text), 12+ flashcards, 10+ item
  readiness checklist, balanced EN/ZH spans + working `toggleLang()`.
- `scripts/validate.sh` exit 0.
- `scripts/build-index.py` updated to discover the new subject; HS
  Biology card visible on the landing page (EN + ZH).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-sources** | Fetch NGSS HS-LS + one provincial doc per region (ON SBI3U/SBI4U, BC Life Sci 11, AB Bio 20/30); write Cell-Structure `*_extract.md` slices | P0 | open |
| **S1-SG** | Draft `Unit_1_Cell_Structure_and_Function.html` bilingual SG (locks the HS Biology template) | P0 | open |
| **S1-index** | Update `scripts/build-index.py` SUBJECTS (pick unused chip colour) + seed index.html subject-group block; surface Unit 1 card | P1 | open |

Build order: **S1-sources → S1-SG → S1-index.** Source-grounding gates
the SG (cannot cite a Syllabus Map without the extracts).

Sprint 2 candidates (after Unit 1 template locks): bulk-draft Units 2-6
bilingual SGs from the Unit 1 template via parallel subagents; continue
source-grounding for the remaining units.

---

## Standing principles

- **Topic-indexed, single set.** One unit per biological topic, not per
  US/provincial course. Filename `Unit_N_Topic.html`, sequential `N`
  across the whole subject. Title format and naming locked in
  [`rag/subjects/high_school_biology.md`](../rag/subjects/high_school_biology.md).
- **Multi-syllabus crosswalk inside each guide.** Every unit ships with a
  Syllabus Map callout near the top listing the matching codes in US NGSS
  (HS-LS), Ontario, BC, and Alberta. Genuine divergences get an inline
  Syllabus Note — sparingly, only where it matters.
- **Dual-goal contract** — every guide serves both the test-tomorrow
  crammer and the depth student. Cram cheat-sheet on top, going-deeper
  detail at the bottom. Locked from IB Math HL via HS Math; canonical
  articulation in [`prompts/create-unit.md`](../prompts/create-unit.md).
- **Bilingual-from-start — LOCKED (user 2026-05-31).** Every SG ships
  with paired `<span data-lang="en">` + `<span data-lang="zh">` markup
  and a working `toggleLang()` script in the same commit. Non-negotiable
  for new subjects. HS Biology does **not** repeat HS Math's
  English-first / retroactive-ZH detour.
- **Verification rule:** any syllabus-specific claim cites a fetched
  source PDF in `rag/sources/`. Training-data recall is not an acceptable
  citation. The spec enforces this.
- **honors-flag** chip for the harder provincial stream (Biology 30 /
  SBI4U / Anatomy & Physiology 12) so a foundation-track student can skip
  cleanly.
- **AP / IB feeder pointers** — flag the IB Biology / AP Biology units a
  topic feeds into. Hyperlink only once the target exists in this repo;
  plain text until then.

---

## Cross-Unit Snapshot

Every proposed unit is listed; all unbuilt. Fill in actual section /
worked-example / quiz counts when a unit ships.

| Unit | Topic | SG | P | S | Status |
|---|---|---|---|---|---|
| 1  | Cell Structure and Function          | &mdash; | &mdash; | &mdash; | **Sprint 1 — template lock (open)** |
| 2  | Biochemistry (Molecules of Life)     | &mdash; | &mdash; | &mdash; | unbuilt |
| 3  | Cellular Energetics (Photosynthesis & Respiration) | &mdash; | &mdash; | &mdash; | unbuilt |
| 4  | Cell Division and the Cell Cycle     | &mdash; | &mdash; | &mdash; | unbuilt |
| 5  | Mendelian Genetics and Heredity      | &mdash; | &mdash; | &mdash; | unbuilt |
| 6  | Molecular Genetics (DNA, RNA, Protein Synthesis) | &mdash; | &mdash; | &mdash; | unbuilt |
| 7  | Evolution and Natural Selection      | &mdash; | &mdash; | &mdash; | unbuilt |
| 8  | Biodiversity and Classification      | &mdash; | &mdash; | &mdash; | unbuilt |
| 9  | Ecology and Ecosystems               | &mdash; | &mdash; | &mdash; | unbuilt |
| 10 | Human Anatomy and Physiology (systems) | &mdash; | &mdash; | &mdash; | unbuilt |
| 11 | Homeostasis                          | &mdash; | &mdash; | &mdash; | unbuilt |
| 12 | Population Biology                    | &mdash; | &mdash; | &mdash; | unbuilt |

Unit count and ordering are **draft** — may shift once sources are read
(e.g. Population Biology may fold into Ecology; Human A&P may split
across system-specific units). See spec for the per-unit 4-curriculum
mapping.

---

## Source-grounding state

**All PENDING.** No source PDFs or extracts fetched yet. Sprint 1
S1-sources closes the priority rows. Official URLs live in the spec.

| Region | Course / doc | Course code | PDF fetched? | Extract written? | Status |
|---|---|---|---|---|---|
| 🇺🇸 US | NGSS High School Life Sciences PEs | HS-LS1 / HS-LS2 / HS-LS3 / HS-LS4 | no | no | **PENDING** |
| 🇨🇦 ON | Biology, Grade 11 (University) | SBI3U | no | no | **PENDING** |
| 🇨🇦 ON | Biology, Grade 12 (University) | SBI4U | no | no | **PENDING** |
| 🇨🇦 ON | Science, Grade 10 (foundations) | SNC2D | no | no | **PENDING** |
| 🇨🇦 BC | Life Sciences 11 | — | no | no | **PENDING** |
| 🇨🇦 BC | Anatomy and Physiology 12 | — | no | no | **PENDING** |
| 🇨🇦 BC | Science 10 (foundations) | — | no | no | **PENDING** |
| 🇨🇦 AB | Biology 20 | — | no | no | **PENDING** |
| 🇨🇦 AB | Biology 30 | — | no | no | **PENDING** |
| 🇨🇦 AB | Science 10 (foundations) | — | no | no | **PENDING** |

**Extraction tool note** (inherited from HS Math): use `pdftotext
-layout` from Poppler (`/mingw64/bin/pdftotext` inside the sandbox) for
PDF source-grounding — the Read tool's `pdftoppm` dependency is absent.
For NGSS, the HS-LS performance expectations are also browsable on
<https://www.nextgenscience.org/> if a clean PDF is hard to source.

---

## Closed Sprints

### Sprint 0 — subject scaffolding — closed 2026-05-31

Subject opened, mirroring HS Math conventions. Spec authored, audit
seeded, empty folder structure created. No Study Guide content drafted
(scaffolding/planning only).

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec `rag/subjects/high_school_biology.md` | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-2**~~ | Author this audit | P0 | ✅ shipped 2026-05-31 |
| ~~**S0-3**~~ | Create empty folder structure (Study Guides + Practice Questions/Solutions) | P0 | ✅ shipped 2026-05-31 |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint. **Bilingual EN/ZH is
deliberately NOT here** — it is locked into every SG from the first
commit.

| ID  | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice Questions product (MC + FRQ-style sets per unit, with Solutions companion mirroring IB Math HL / HS Math pattern) | Needs Study Guide content first to anchor question scope. Open after ≥3 study guides ship. |
| DP-2 | Per-province exam-prep overlays (BC provincial-style, AB Diploma Biology 30) on top of the topic guides | Layer onto existing guides; deferred until Canadian audience demand is measured. |
| DP-3 | IB Biology / AP Biology subjects (feeder targets) | Out of scope for HS Biology; once they exist, convert HS Biology feeder pointers from plain text to hyperlinks. |
| DP-4 | Diagram / figure assets (cell organelle maps, Punnett squares, ecosystem energy pyramids) — biology leans visual | Scoping pass for inline SVG vs. KaTeX-only approach needed; HS Math was formula-heavy, Biology is diagram-heavy. |
| DP-5 | Lab-skills / inquiry-practice cross-reference cards (NGSS science-and-engineering practices) | Format templates need a separate scoping pass. |

---

## How to update this file

When closing a sprint item, mark with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When a sprint clears, collapse
into a single line in `## Closed Sprints` and promote the next sprint up.

When standing principles need revision, edit them here; route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_biology.md`](../rag/subjects/high_school_biology.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork the
contract.

When a unit ships, fill in its row of the cross-unit snapshot with actual
section / worked-example / quiz counts, and update the source-grounding
table as PDFs/extracts land.
