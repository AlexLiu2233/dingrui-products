# Study Guide Audit Checklist

Single source of truth for "is this study guide up to standard?"
Distilled from:

- `prompts/create-unit.md` — dual-goal contract (the locked pedagogical promise)
- `rag/style-guide.md` — design tokens, typography, component patterns
- `rag/template.html` — base HTML scaffold
- `prompts/create-bilingual-translation.md` — bilingual conventions (translated files only)
- Subject-specific philosophies recorded in each `<Subject>/AUDIT.md`

**How to use**: every shipped study guide is audited against this
checklist. Findings tier as **P0 / P1 / P2** and land in the subject's
`AUDIT.md` "Active Sprint" table or backlog.

---

## Current improvement focus (locked 2026-05-21)

User direction during the `improve_study_guides` audit pass:

> **Notes content is good.** Focus on **worked examples, exam tips,
> simple (one-slider-one-concept) interactive components**. English
> first — once an English revision is confirmed for a file, the
> Mandarin teaching translation lands as a follow-up commit on the
> same file. Bilingual is a gated post-English step, not parallel.

**What this means for audit findings:**

- ✅ **In scope:** missing worked examples, missing/weak exam-tip
  callouts, missing or over-loaded slider widgets (sliders that
  bundle multiple concepts), page-fill / layout-parity gaps, P0 math
  rendering bugs (KaTeX hygiene).
- ❌ **Out of scope:** "rewrite the prose," "expand the explanation,"
  "improve the wording" — notes content is locked. Do not log
  expository-rewrite findings.
- ⏸ **Gated:** any bilingual / translation polish (`<code>` glosses
  missed, terminology drift, ZH-side rewording) is **deferred until the
  English revision lands and is confirmed**. Then the bilingual
  follow-up addresses both at once.

---

## Section A — Formatting consistency (mechanical, checkable)

| ID | Check | How to verify | Tier if missing |
|---|---|---|---|
| A1 | `<title>` tag follows `{Subject Long} — {Prefix}: {Topic} \| Dingrui Scholars` | grep `<title>` | P1 — breaks `build-index.py` card text |
| A2 | `:root` defines canonical design tokens (`--bg`, `--bg-card`, `--accent`, `--text`, `--text-secondary`, `--green`, `--orange`, `--red`, `--purple`, `--gold`, `--border`) | grep `--accent:` in `:root` block | P1 |
| A3 | Typography vars: `--font-display: 'DM Serif Display'`, `--font-body: 'Source Sans 3'`, `--font-mono: 'JetBrains Mono'`. **Bilingual files**: `--font-body` also includes `'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei'` CJK fallback. | grep `font-display`, `font-body`, `PingFang SC` | P1 |
| A4 | External deps only: Google Fonts + KaTeX 0.16.9 CDN. No other CDN scripts. | grep `<script src=` / `<link rel="stylesheet" href=` | P0 if novel CDN |
| A5 | Dark mode: `[data-theme="dark"]` block redefines all major color vars; toggle button present. (Theme `localStorage` persistence is a P2 polish; absence does not block.) | grep `data-theme="dark"` | P1 if missing entirely |
| A6 | KaTeX delimiters: `$...$` inline, `$$...$$` display. **No unicode subscripts / superscripts / Greek / CJK characters inside `\text{}`** — they render with fallback glyphs or break math layout. Use `^{-1}`, `\mathrm{...}`, or move Chinese text outside the math entirely. | render check (open file) + grep `\\text{[^}]*[α-ωΑ-Ω₀-₉⁰-⁹⁻⁺一-龯]` | **P0 — math renders broken** |
| A7 | TOC anchor links all resolve to existing `id=`. | for each `href="#..."` in sidebar, find matching `id="..."` | P1 |
| A8 | `bash scripts/validate.sh <file>` exits 0. | run command | P0 |
| A9 | Quiz markup matches subject-canonical sibling. | diff against a same-subject sibling | P1 |
| A10 | Required sections present: hero, sticky TOC sidebar, footer, progress bar. | grep `class="hero"`, `class="sidebar"`, `class="footer"`/`site-footer`, `class="progress-` | P1 |
| A11 | `@media print` block present with no-clip rules. | grep `@media print` | P2 |
| A12 | Mobile responsive at 375px: `@media (max-width: 600px)` block present. | grep `max-width: 600px` | P1 |
| **A14** | **Page-fill / content-column parity.** `.main-wrap` (or equivalent) honors `--max-w: 860px` and renders at the same width as siblings. Hero / section / footer all sit inside that column without an extra narrower wrapper. Sidebar must be an overlay (transform-translateX), not a column-reserving sibling. | side-by-side screenshot vs a same-tier sibling; check `--max-w` value and `.main-wrap` margin/width rules; check whether sidebar mode shrinks main column | P1 — visible visual drift |
| A13 | **(Translated files)** Bilingual toggle infra: body.lang-zh CSS rules + `id="langToggle"` button + `function toggleLang()` JS + CJK font fallback. `toggleLang()` does NOT read or write `localStorage` (locked 2026-05-21). | the 4-grep panel + grep `localStorage.*lang` / `drs.lang` | P0 |

## Section B — Dual-goal contract (pedagogical, per-section) — standing principle

Every major topic section must serve **both** a crammer (last-ditch
pass, ≥4 IB / ≥3 AP) and a top-score chaser (going for 7 IB / 5 AP).

| ID | Check | What to look for | Tier if missing |
|---|---|---|---|
| B1 | **Cheat-sheet at top of each topic section.** Formula card, "Key formula" / "What you must know" / `box--tip` / `concept-box` / `qref` block — liftable in <1 minute. | First child of each `<section>` is a cheat-sheet element | P0 |
| B2 | **≥1 worked example per major topic.** Boxed steps with KaTeX, canonical exam application. Worked examples must be **visible by default** — not collapsed inside `<details>` (the crammer can't lift collapsed content in <1 minute). | grep `worked-example` / `worked-solution` per section; check none are inside `<details>` | P0 |
| B3 | **Going-deeper / proof / derivation block** for topics with non-trivial derivations. `box--proof` or `<details>` — crammer skips, top-score chaser dives in. | At least one `<details>` or `box--proof` per section that derives a formula or theorem | P1 (was P0; demoted because notes content is good — this is enhancement, not blocker) |
| B4 | **Quiz mix recall + synthesis.** Each section's quiz items include at least one recall-level question AND at least one synthesis / multi-step question. | Read each `<div class="quiz">` cluster | P1 |
| B5 | **Flashcard deck — 8+ cards.** Count gate only. Style is locked ("FLASHCARDS ARE BEAUTIFUL" — terse Q / `$$formula$$` back) but does not block; rewrites of existing decks are out of scope. | Count `.flashcard` elements | P1 if <8 cards; otherwise pass |
| B6 | **Hero "Read me first" / overview intro present.** Crammer's entry point — single paragraph framing the unit. | First section after hero has prose intro | P1 |
| B7 | **Readiness checklist / self-assessment block** (where established in subject siblings, e.g. IB Math HL). | grep `readiness-checklist` / `self-assess` / similar | P1 if siblings have one, P2 otherwise |

## Section E — Active improvement vectors (this sprint's primary lens)

These three are the user-locked focus for the current pass. Findings
in this section tier higher than equivalent gaps in Section B.

| ID | Check | What to look for | Tier |
|---|---|---|---|
| **E1** | **Worked-example density.** Every major topic section has ≥1 visible-by-default worked example. Sections with no worked example (only prose + concept box) fail. Sections where the only example is collapsed inside `<details>` fail. | grep `worked-example` / `worked-solution` per section; verify not collapsed | **P0** for each section missing one |
| **E2** | **Exam-tip / strategy callout per major topic.** Concrete, exam-specific guidance: paper splits (Paper 1 vs Paper 2 calc/no-calc), trap patterns, time-saver moves, what graders look for, common rubric loss points. Distinct from "concept box" (which explains the concept). | grep `exam-tip` / `exam-strategy` / `AP Trap` / paper-split chips per section | **P1** for each section missing one |
| **E3** | **Slider widget appropriateness.** Where the topic has a parameter-sweep insight (one parameter → one observable response), there should be a slider widget. Existing widgets must obey the Interactive Component Philosophy: **one slider, one key concept per widget**. Multi-concept widgets fail. | inspect each `*-widget` block; count slider count + concept count | **P1** for missing widget on a slider-friendly topic; **P0** for widgets bundling >1 concept (regression of Sprint 6 lock) |

**Interactive Component Philosophy (cross-subject standard, lifted
from AP Physics audit):**

1. **Sliders only.** No text inputs, number inputs, checkboxes,
   radios, selects, textareas. A widget either responds to slider
   movement or it is a static formula box.
2. **One key thing per widget.** If a single widget illustrates ideal
   SHM AND damping AND driving (e.g. `shm-widget` regression), split
   it. If a widget bundles a tabular table AND a phase-space plot AND
   parameter sliders, split it.
3. **Result cards are read-only.** Sliders go in; computed values
   come out. No round-trip editing.

## Section C — Subject-specific philosophy

| ID | Subject | Check | Tier |
|---|---|---|---|
| C1 | **AP Physics** | Interactive Component Philosophy (now cross-subject standard — see E3). | P1 |
| C2 | **IB Math HL** | HL-only content flagged inline with chip / callout so SL students can skip cleanly. | P1 |
| C3 | **IB Chemistry HL** | Paper 1 (MCQ, no calc) / Paper 2 (Extended Response) splits called out where relevant. HL extensions visible. | P2 |
| C4 | **AP Calculus** | AB/BC split annotated for BC-only topics (parametric, polar, vector, series). | P2 |
| C5 | **AP CSA** | Java keywords / type names stay literal (`int`, `String`, `ArrayList`, `boolean`, `Math.random()`). No localization of code. Code comments inside `<pre>` blocks **do not translate** — student types them in English on exam. | P1 |

## Section D — Bilingual quality (translated files only) — GATED

**Important workflow rule (locked 2026-05-21):** translation polish is
a follow-up to the English revision, not a parallel concern. When
auditing a translated file, do not log D-section findings in the
"active" sprint table. Instead:

1. The English revision lands first (worked examples / exam tips /
   sliders / page-fill / hygiene).
2. User confirms the English on that file.
3. **Then** the translation pass addresses D-section gaps for the
   same file, as a separate follow-up commit.

| ID | Check | How to verify | Tier (when bilingual phase opens) |
|---|---|---|---|
| D1 | `data-lang` parity — `grep -c 'data-lang="en"'` == `grep -c 'data-lang="zh"'` | bash | P0 |
| D2 | Exam-term glosses — every locked English exam term from the subject's glossary block in `prompts/create-bilingual-translation.md` appears in `<code>` at first Chinese mention per section. | grep for each glossary term inside Chinese spans | P1 |
| D3 | Locked terminology corrections applied (no regressions): AP Physics `转折点` not `折返点`, `标量积` not `点积` (as primary), `路程` not `路径长度`, `溃缩区` not `缓冲溃缩区`, `动量定理` not `冲量—动量定理`. | grep for forbidden terms | P0 if regression found |
| D4 | `toggleLang()` does not read or write `localStorage` — every page defaults to English on load (locked 2026-05-21). | grep `localStorage.*lang` / `drs.lang` | P0 if found |

---

## Tier definitions (from `rag/AUDIT_TEMPLATE.md`)

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "going for top score" use of the guide. Also: rendering bugs (broken
  math, broken anchors).
- **P1** — consistency, polish, or hygiene gap that affects feel/parity
  but not exam readiness.
- **P2** — nice-to-have / future work.

## Output format for audit findings

When this checklist surfaces a gap, log it in the subject's `AUDIT.md`
under a new sprint or backlog block, using this row shape:

```
| **<ID>-N** | <File>: <one-line gap> | P<tier> | **Open** |
```

The checklist item that caught it (e.g. `E1`, `A14`, `A6`) goes in the
description body.

## Workflow

1. Run audit on a subject (typically one agent per subject) using this
   checklist.
2. Score every shipped study guide on every applicable check.
3. Collate findings into the subject's `AUDIT.md` as a new sprint
   block — naming convention: **"Sprint N — Worked examples / exam
   tips / sliders"** (the three active improvement vectors).
4. User reviews the new sprint. On approval, fix sprints execute
   English-first per the locked review-then-merge cadence.
5. Bilingual follow-up pass happens **after** the user confirms the
   English revision for each file. Translation findings (Section D)
   from the same audit are picked up at that gate, not earlier.

**Audit-only branches** (like `improve_study_guides`): no study guide
HTML files are edited. Only the PM markdowns (`rag/`, `prompts/`,
`<Subject>/AUDIT.md`) change. Fixes happen in subsequent subject
sprints.
