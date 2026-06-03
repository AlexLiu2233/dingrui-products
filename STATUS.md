# Dingrui Scholars — Repo Status

**Internal status dashboard** (stripped from deploy via `.github/workflows/deploy.yml`).
Living doc — update as the product evolves. Last updated: **2026-06-03**.

---

## Product inventory (Study Guides / Practice / Solutions)

| Tier | Subject | SG | P | S | Bilingual | Where |
|---|---|---|---|---|---|---|
| **HS** | High School Math | 15 | 15 | 15 | ✅ EN/ZH | `main` |
| **HS** | High School Physics | 12 | — | — | ✅ EN/ZH | `main` |
| **HS** | High School Chemistry | 14 | — | — | ✅ EN/ZH | `hs_stem_complete` |
| **HS** | High School Biology | 12 | — | — | ✅ EN/ZH | `hs_stem_complete` |
| **HS** | High School Computer Science | 13 | — | — | ✅ EN/ZH | `hs_stem_complete` |
| AP | AP Calculus AB/BC | 10 | 8 | — | partial | `main` |
| AP | AP Physics C: Mechanics | 7 | 7 | 7 | partial | `main` |
| AP | AP Computer Science A | 4 | 4 | 4 | ✅ EN/ZH | `main` |
| IB | IB Math AA HL | 23 | 22 | 22 | ✅ EN/ZH | `main` |
| IB | IB Chemistry HL | 4 | 1 | 1 | ✅ EN/ZH | `main` |
| IB | IB Physics HL | 1 | — | — | ✅ EN/ZH | `main` (scaffolding) |
| IB | IB Math AI HL | — | — | — | — | retired |

**HS STEM total: 66 Study Guides** across 5 subjects (the focus of the current program).

---

## Branches & deploy state

- **`main`** — production (auto-deploys to site root). Has HS Math, HS Physics, all AP/IB.
- **`preview`** — staging (`/preview/`). Kept in sync with main.
- **`hs_stem_complete`** ← **active branch / source of truth.** Holds ALL 66 HS STEM SGs
  (main + Chemistry + Biology + CS merged in). NOT yet on main. ~26 commits ahead.
- **`landing_page_refresh`** — LP-1 (EN/ZH pairing checklist + `translation_coverage.py`); paused.
- **~26 stale local branches** (old sprints, subject-SG backups `hs_chemistry_sg`/`hs_biology_sg`/
  `hs_cs_sg`/`hs_physics_studyguides`, landing experiments) — **delete post-FF**, keep as backups
  until `hs_stem_complete` reaches `main`. Do NOT delete the 3 unmerged: `english_to_chinese_translation`,
  `ib_chem_reactivity2_challenge_practice`, `sprint_3_unit_specs`.

---

## Current program: HS STEM → marketable bilingual product

**Goal:** complete, self-contained, bilingual HS STEM Study-Guide library (5 subjects, topic-organised,
4-region syllabus crosswalk US/ON/BC/AB, honors-flag stream, feeder links to AP/IB) — the bottom tier of
the HS → AP/IB → first-year-uni pipeline.

**Status:** all 66 SGs drafted, **audited, fixed, and integrated** on `hs_stem_complete` —
**DEPLOY-READY** (2026-06-03). In-guide pictures scrapped; prose + KaTeX only. Final gate: 66/66
validate, 0 EN/ZH imbalances, 0 localStorage, 0 CJK-in-`\text{}`, all 66 toggles defined,
`index.html` validates, all 39 new cards (Chem/Bio/CS) surface. Not yet on `main`.

**Sequence (where we are → next):**
1. ✅ **Deployment-Readiness Audit** — ran `rag/study-guide-audit-checklist.md` per subject; findings in each `<Subject>/AUDIT.md`.
2. ✅ **Fix sprint** — D1 dead-toggle + D4 localStorage normalized (all 66); A6 CJK-in-math cleared (25 files); favicon path; Chem U4/U5 going-deeper. (`1b749f3`…`fcaf19e`)
3. ✅ **build-index + landing** — HS Chemistry/Biology/CS wired into `build-index.py` + landing subject-groups; 39 cards live EN+ZH. (`dedd2d3`)
4. ⏳ **FF `hs_stem_complete` → `preview` → `main` → deploy** (awaiting user go).
5. Post-FF cleanup (delete merged branches/remotes; prune).
6. **Later sprint:** HS Practice + Solutions (author `create-practice-and-solutions-hs-math.md` playbook first).

**Known carry-over:** AP/IB SGs share the same `../LOGO.png` favicon bug (fixed only for HS) — future cross-subject pass.

---

## Pre-sprint review key findings (2026-06-03 workflow)

- **An audit/improvement workflow already exists — use it, don't reinvent:**
  `rag/study-guide-audit-checklist.md` (canonical instrument, Sections A/B/D, tiered P0/P1/P2),
  `prompts/improve-existing-product.md` (outer loop), `prompts/review-changes.md` (per-file gate),
  `prompts/modify-unit.md` (smallest-diff fixes).
- **HS-STEM audit adjustments** (in `rag/hs-stem-deploy-audit.md`): EXCLUDE the checklist's interactive/
  slider vectors (E3, C1) — superseded by the no-interactive lock; ADD a no-stray-`<svg>`/img/chart/JS
  sweep; A1 title = HS **no-colon** form; Section D bilingual parity (D1 EN==ZH) is an **active** gate.
- **`create-unit.md <subject_notes>` has no HS entry** — HS conventions live in AUDITs + feedback notes.

---

## Global invariants (bind every subject) — see `prompts/README.md` `<global_invariants>`
1. **Tone** — consultant/textbook voice; no em/en dashes in prose (`prompts/_tone.md`).
2. **P/S pairing** — `dingrui:version` + `pair-key` lock Practice↔Solutions.
3. **Bilingual gate** — `data-lang="en"` count == `data-lang="zh"` count per file.
4. **Ship gate** — `bash scripts/validate.sh` exits 0.
5. **Index** — run `python scripts/build-index.py` after any SG add/remove/rename.

Design system: maroon `#7A2E2E`; DM Serif Display / Source Sans 3 / JetBrains Mono; dark mode +
language/theme toggles; self-contained single-file HTML (Google Fonts + KaTeX CDN only).

## HS vs AP/IB conventions (quick ref)
HS = topic-organised (no visible "Unit N"), no-colon title, 4-column syllabus crosswalk, region chips,
gold honors-flag, bilingual-from-start, outbound feeder links. AP/IB = curriculum-unit framing, colon
title, single syllabus, paper-style chips, purple HL flag (IB), retrofitted bilingual.

## Known debt / watch-list
- `hs_stem_complete` not yet on `main` (3 subjects only live there).
- AP Calculus (8 Practice) + AP Physics (14 P+S) still EN-only (translation tail; see
  `project_translation_coverage` memory).
- HS Practice+Solutions: 36 HS Math P+S are EN-only; other HS subjects have no P+S yet; no HS P+S playbook.
- `sources.txt`: AB Math 20-1 standards un-fetched (`[!]`).
