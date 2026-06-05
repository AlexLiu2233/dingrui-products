# Dingrui Scholars — Repo Status

**Internal status dashboard** (stripped from deploy via `.github/workflows/deploy.yml`).
Living doc — update as the product evolves. Last updated: **2026-06-03** (HS STEM shipped to production).

---

## Product inventory (Study Guides / Practice / Solutions)

| Tier | Subject | SG | P | S | Bilingual | Where |
|---|---|---|---|---|---|---|
| **HS** | High School Math | 15 | 15 | 15 | ✅ EN/ZH | `main` |
| **HS** | High School Physics | 12 | — | — | ✅ EN/ZH | `main` |
| **HS** | High School Chemistry | 14 | — | — | ✅ EN/ZH | `main` ✅ live |
| **HS** | High School Biology | 12 | — | — | ✅ EN/ZH | `main` ✅ live |
| **HS** | High School Computer Science | 13 | — | — | ✅ EN/ZH | `main` ✅ live |
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

- **`main`** = `preview` — production (auto-deploys to site root). Holds **all 66 HS STEM SGs**
  (Math 15 + Physics 12 + Chemistry 14 + Biology 12 + CS 13) + all AP/IB. Shipped: **HS STEM 2026-06-03**;
  **landing fixes 2026-06-04** (accordion default-closed, count 15, cross-page `?lang=zh` continuity);
  **SG bilingual hygiene + HS-Phys Unit 1 Kinematics P+S template 2026-06-05**.
- **SG bilingual hygiene (2026-06-05):** purged all Chinese from `data-lang="en"` spans across the 66 SGs
  (488 fixed; kept only the toggle buttons + the CS U9 UTF-8 lesson example); replaced 301 cryptic
  `*_extract.md` Source citations with readable curriculum names (mapping in `source-extracts` memory).
  EN-in-ZH is allowed (course examined in English). Not yet applied to P+S / AP / IB files (HS SGs only).
- **Branches fully consolidated 2026-06-05.** Only `main` + `preview` exist on origin. All stale/merged
  local + remote branches deleted (incl. `hs_stem_complete`, `landing_page_refresh`, `sg_bilingual_hygiene`,
  `hs_physics_practice`, and 8 fully-merged `origin/*`). `english_to_chinese_translation` + `sprint_3_unit_specs`
  deleted (superseded/redundant, 0 unique work vs main).
- **Repo fully consolidated: only `main` + `preview` exist** (locally and on origin). The last branch,
  `ib_chem_reactivity2_challenge_practice` (IB Chem Reactivity 2.2 Challenge P+S, v1.1), was gated, given the
  `?lang=zh` snippet, merged to main, and deleted (2026-06-05).

---

## Current program: HS STEM → marketable bilingual product

**Goal:** complete, self-contained, bilingual HS STEM Study-Guide library (5 subjects, topic-organised,
4-region syllabus crosswalk US/ON/BC/AB, honors-flag stream, feeder links to AP/IB) — the bottom tier of
the HS → AP/IB → first-year-uni pipeline.

**Status:** all 66 SGs drafted, **audited, fixed, integrated, and SHIPPED to production**
(`main`=`eca6b0e`, 2026-06-03). In-guide pictures scrapped; prose + KaTeX only. Final gate passed:
66/66 validate, 0 EN/ZH imbalances, 0 localStorage, 0 CJK-in-`\text{}`, all 66 toggles defined,
`index.html` validates, all 39 new cards (Chem/Bio/CS) surface. **HS STEM SG program COMPLETE.**

**Sequence (DONE → next):**
1. ✅ **Deployment-Readiness Audit** — ran `rag/study-guide-audit-checklist.md` per subject; findings in each `<Subject>/AUDIT.md`.
2. ✅ **Fix sprint** — D1 dead-toggle + D4 localStorage normalized (all 66); A6 CJK-in-math cleared (25 files); favicon path; Chem U4/U5 going-deeper. (`1b749f3`…`fcaf19e`)
3. ✅ **build-index + landing** — HS Chemistry/Biology/CS wired into `build-index.py` + landing subject-groups; 39 cards live EN+ZH. (`dedd2d3`)
4. ✅ **FF → `main` + `preview` → deploy** — rebased onto main (absorbed cherry-picked deploy-fix), FF'd, pushed; validate exits 0 so the prod gate passes. (`eca6b0e`, 2026-06-03)
5. ✅ Post-FF cleanup — 23 merged + 3 redundant branches deleted; 3 unmerged + `landing_page_refresh` kept.
6. 🔨 **IN PROGRESS — HS Practice + Solutions sprint** (HS Physics first). Playbook: `prompts/create-hs-practice-and-solutions.md`. **Unit 1 Kinematics P+S template (`HS-Phys-1`) is LOCKED + on `main`** (12 Qs/81 marks, verified). **Remaining: waves A/B/C for Units 2-12** (re-branch off main; Sonnet copy-then-edit from the locked Unit 1 pair). Then Chem/Bio/CS/Math-retro. Plan detail in `High School Physics/AUDIT.md` Sprint 3.

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
6. **Lang continuity** — run `python scripts/lang_link_continuity.py` after creating ANY new bilingual page
   (SG or Practice/Solutions) so cross-page `?lang=zh` continuity covers it. Idempotent; parity-neutral
   (uses `[data-lang=zh]`, no quoted literal). Without it, a ZH-landing click opens the EN version. Direct
   visits with no `?lang` param still default to English (the D4 rule).

Design system: maroon `#7A2E2E`; DM Serif Display / Source Sans 3 / JetBrains Mono; dark mode +
language/theme toggles; self-contained single-file HTML (Google Fonts + KaTeX CDN only).

## HS vs AP/IB conventions (quick ref)
HS = topic-organised (no visible "Unit N"), no-colon title, 4-column syllabus crosswalk, region chips,
gold honors-flag, bilingual-from-start, outbound feeder links. AP/IB = curriculum-unit framing, colon
title, single syllabus, paper-style chips, purple HL flag (IB), retrofitted bilingual.

## Known debt / watch-list
- AP Calculus (8 Practice) + AP Physics (14 P+S) still EN-only (translation tail; see
  `project_translation_coverage` memory).
- HS Practice+Solutions: 36 HS Math P+S exist (bilingual); other 4 HS subjects have no P+S yet. Playbook
  authored (`prompts/create-hs-practice-and-solutions.md`); Physics-first sprint planned (HS Physics AUDIT Sprint 3).
  **P+S-sprint finding:** `High School Math/Practice Questions/Solutions/Unit_4_Rational_and_Radical_Expressions_Solutions.html`
  has an EN/ZH parity off-by-one (en=310/zh=311) — pre-existing, fix during the Math leg of the P+S sprint.
- **CJK-in-EN rule** enforced on HS SGs (2026-06-05) but NOT yet swept across P+S / AP / IB files. Apply
  the same rule (no Chinese in `data-lang="en"` spans; toggle + deliberate examples exempt) when those are next touched.
- Two untracked stray drafts in `IB Chemistry HL/Practice Questions/` (`IBCHEMHL_ethanfinalpractice*`) sit in the working tree; not committed, not deployed. Decide keep/remove later.
- `sources.txt`: AB Math 20-1 standards un-fetched (`[!]`).
