# Dingrui Scholars — Repo Status

**Internal status dashboard** (stripped from deploy via `.github/workflows/deploy.yml`).
Living doc — update as the product evolves. Last updated: **2026-06-09** (`main`=`preview`=`9edde7e`;
new work on branch `university_calculus_init`).

**🆕 NEW SUBJECT + NEW TIER OPENED 2026-06-09 — University Calculus (first-year-uni):** opens the top tier of
the HS → AP/IB → **first-year-uni** pipeline. Goal = lead-gen for *current* NA top-10 STEM undergrads (MIT/GT/
Princeton-tier) struggling with the calculus sequence; SEO long-tail is the primary acquisition channel.
**Scope (user-locked):** one subject, 4 course-groups A/B/C/D = Calc I/II/III/IV, **8 SGs each = 32 SGs**;
Calc IV = Ordinary Differential Equations; English-first (ZH later wave). **Grounding-first (user-requested):**
a source-of-record folder `rag/sources/University Calculus/` (target-school syllabi MIT 18.01/02/03 + GT MATH
1551/1552/2551/2552 + Princeton MAT, plus open content sources OCW/OpenStax/Strang/Paul's) + `SOURCES.md`
manifest is a gated Sprint 0 deliverable so every guide is checkable against a committed source.

**STATE (2026-06-09, branch `university_calculus_init`, NOT yet committed):** Sprints 0 + 1 + 2 ✅ DONE.
**ALL 32 Study Guides are drafted, validated, and indexed.** A1 Limits & Continuity is the USER-LOCKED
template (full epsilon-delta proofs; CTA under Read-me-first); A2 + A5 authored by me/an early agent; the
other 29 (A3-A8, B, C, D) authored by a 29-agent workflow through the `uc_build_unit.py` engine. Landing
Tier-03 "University" band is live with all 32 cards under 4 course accordions (Calc I/II/III/IV, 8 each);
all 32 in the sitemap; subject-group label reads "32 units". **Every file passes:** validate exit 0,
0 dash entities, 0 localStorage, 0 content data-lang, 0 AP leakage; uniform structure (7 sections + unit
quiz + checklist, 12 flashcards, BOTH consult CTAs, 8 checklist items). Content spot-checked = genuine
NA-top-10 rigor (real proofs, correct worked examples). **Plan-mode lesson:** the first workflow wave failed
because plan mode silently blocks subagent writes; ExitPlanMode + fresh re-run fixed it.

**HANDOFF — how to continue Sprint 2 (another chat picks up here):**
1. Bulk engine: `scripts/uc_build_unit.py` clones A1's verbatim CSS/logo/JS and wraps a per-unit content spec,
   baking in BOTH consult CTAs. Per-unit recipe (mirrors the deleted `scripts/_unit_A2.py`): write a runner with
   a `SPEC` dict (uid, slug, topic, overline, h1, sub, chips, readme, toc, sections HTML, flashcards, quiz HTML,
   checklist) and call `build_and_save(SPEC)`. Author genuine university rigor, grounded in
   `rag/sources/University Calculus/SOURCES.md`. English-first (no `data-lang`/toggle).
2. After each unit/wave: `python scripts/build-index.py && python scripts/build_sitemap.py`, bump the
   `subject-group__count` label in `index.html` (build-index does NOT auto-update it), and
   `bash scripts/validate.sh "University Calculus/Study Guides/<file>.html"`.
3. **SG layer is COMPLETE (32/32).** Remaining for the subject: **Sprint 3** = Mandarin ZH wave
   (`prompts/create-bilingual-translation.md`; the engine writes English-only, so ZH wraps each file's prose in
   `data-lang` span pairs, adds the toggle button + bilingual CSS/JS); **Sprint 4** = Practice + Solutions
   (32 pairs, `pair-key` + `dingrui:version` lock). Reusable bulk engine for any future UC SG work:
   `scripts/uc_build_unit.py`. Cadence: review-then-merge, branch → preview → FF to main. **✅ COMMITTED +
   MERGED TO `preview` + LIVE ON STAGING 2026-06-10** (`e830328`→PR #4→`preview` tip `d41229a`). Review at
   `…/dingrui-products/preview/University%20Calculus/Study%20Guides/Unit_A1_Limits_and_Continuity.html`. UC is
   on `preview` ONLY (prod still 404 for UC — correct); awaiting user's staging review → FF `preview`→`main`.
   **Next sprint (user-chosen):** Consult-CTA-under-Read-me-first retrofit across the 115 existing SGs.
   **⚠️ INFRA FIX same day:** the entire Pages site was 404 (prod+preview). Root causes fixed via `gh api`:
   (1) `preview` was missing from the `github-pages` env branch policy; (2) Pages was disabled — re-enabled with
   `build_type=workflow` (Source=GitHub Actions, per CLAUDE.md). Deploy now green; site restored. See
   `reference_pages_deploy_infra` memory.

**🆕 PLANNED CROSS-REPO SPRINT — "Consult CTA under Read-me-first" on EVERY Study Guide (user direction
2026-06-09):** the new convention (CTA directly beneath the hero "Read me first" intro, in addition to the
existing end-of-page CTA) must be retrofitted across all existing SGs (66 HS + 49 AP/IB = 115 SGs; P+S files
out of scope). Build a script modeled on `scripts/add_consult_cta.py` / `add_consult_cta_apib.py` that inserts
the intro CTA right after each guide's hero/read-me block, idempotently, bilingual where the file is bilingual.
University Calculus already complies (engine bakes it in). **Not started; sequence after the UC SG wave.**

**IB Physics HL Sprint 2 ✅ SHIPPED TO PROD — all 24 Study Guides now live** (23 new this session, cloned from
the locked A.1 template via 5 parallel subagent waves; index regenerated to 24 cards; sitemap 251 URLs;
landing count corrected 1→24 units EN+ZH). Earlier same day: **Sprint D — Get-Found / SEO ✅ SHIPPED TO PROD**
(sitemap/robots/meta-desc/JSON-LD/canonical). Prior day (2026-06-06)
shipped to prod: **CTA on every page** (66 HS + 131 AP/IB + landing) → **Sprint B funnel instrumentation**
(UTM tags + GA4 `G-SDVTGZ6RJ9`) → **OpenGraph share cards** (230 pages) → **B&W design refresh** matching
dingruischolars.com. Plus housekeeping (preserved 2 IB P+S pairs; D1–D3 link removal).

**Sprint D — Get-Found / SEO (2026-06-07, ✅ SHIPPED to `main`=`preview`=`909155e`):** the notes site had
zero crawl guidance. Added via 4 idempotent stripped-from-deploy scripts:
**`sitemap.xml`** (228 URLs, abs prod URLs, git-date lastmod; 2 student-named drafts excluded) +
**`robots.txt`** (Allow /, `Disallow: /preview/` so staging stays unindexed, Sitemap linked) —
both at repo root so they survive the deploy strip; **`<meta name="description">`** on the 116 pages
lacking one (dash-free, derived from title + doctype; og/twitter desc re-synced; 114 curated ones left
intact); **JSON-LD** `LearningResource` on all 230 pages (`EducationalOrganization` on landing) with
inLanguage/level/provider; **`<link rel="canonical">`** (self-ref absolute, consolidates `?lang=zh` +
`/preview/` duplicates). Gates: validate.sh exit 0, parity unchanged, sitemap well-formed XML, 230/230
JSON-LD valid JSON. Scripts: `build_sitemap.py`, `add_meta_description.py`, `add_jsonld.py`, `add_canonical.py`.
**Structural deploy confirmation (verified against `deploy.yml`):** root `sitemap.xml`/`robots.txt` are NOT in
`strip_internals` and the artifact is a raw static upload (no Jekyll), so both serve at the prod root
`…/dingrui-products/{sitemap.xml,robots.txt}`. **CAVEAT — robots.txt on a GH Pages PROJECT subpath is NOT
crawler-authoritative** (crawlers read `alexliu2233.github.io/robots.txt` at the host root, not the subpath):
so `Disallow:/preview/` + `Sitemap:` lines aren't auto-honored. Mitigated — `/preview/` de-dup is carried by
the canonical tags (stronger signal); **submit the sitemap URL directly in Google Search Console** for
discovery. To get full auto-discovery, add a `Sitemap:` line to an apex `alexliu2233.github.io` Pages repo if one exists.

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
| IB | IB Physics HL | 24 | — | — | ✅ EN/ZH | `main` ✅ SG-complete (P+S next) |
| IB | IB Math AI HL | — | — | — | — | retired |
| **UNI** | University Calculus | 32/32 | — | — | EN-first | `university_calculus_init` 🆕 **all 32 SGs drafted+validated** (uncommitted); P+S + ZH next |

**HS STEM total: 66 Study Guides** across 5 subjects (the focus of the current program).
**University Calculus (new first-year-uni tier):** 32 SGs planned (Calc I/II/III/IV × 8); A/B/C/D groups; ODE = Calc IV.

**🎯 Lead-gen funnel (business goal = leads for academic consulting):** A bilingual
"Book a free consult" CTA (EN → `dingruischolars.com/signup`, ZH → `/signup-ch`) is now live on
**EVERY notes page across the whole site** — 66 HS + 131 AP/IB (49 SGs + 82 P+S) + landing
hero/footer. Shipped in two waves 2026-06-06: P0 HS+landing (`b9f4321`) and Sprint A AP/IB
(`a3fd530`). This is the funnel's conversion surface. Injectors: `scripts/add_consult_cta.py`
(HS) + `scripts/add_consult_cta_apib.py` (AP/IB, 5 template variants).

**Shipped 2026-06-06 (all on `main`):** ✅ **Sprint B — funnel instrumentation**: UTM tags on all 200
CTAs (`utm_campaign=<subject>&utm_content=<unit>__<doctype>__<lang>`, `scripts/utm_tag_cta.py`) +
GA4 `G-SDVTGZ6RJ9` on all 230 pages (`scripts/add_ga_analytics.py`) → notes→click→signup funnel by
subject/unit/lang. ✅ **OpenGraph/Twitter share cards** on 230 pages (`scripts/add_og_tags.py`;
og:image=LOGO.png, swap a 1200×630 card → bump to summary_large_image). ✅ **B&W design refresh**
matching dingruischolars.com (`scripts/restyle_bw.py`; see `reference_design_system` memory).

**Next ≥P1:** (D) Get-Found / SEO ✅ SHIPPED 2026-06-07. (C, content half) IB Physics HL SG completion
✅ SHIPPED 2026-06-07 (24/24 SGs live — the urgent content hole is closed). **Remaining ≥P1: (C, copy half)
feeder-links-as-pitch** — reframe the existing outbound feeder links as a soft sales pitch (low-token copy/script
pass). Then **IB Physics HL Sprint 3 = Practice + Solutions (24 pairs)** per the IB Math HL P+S pattern (a large
fresh-budget sprint; the SGs now have a locked template to pair against). After GA4/GSC accrue ~2wk of data,
revisit **Convert-Better / landing CRO** (don't optimize the funnel blind). **IB/AP SG completion = P2–P3.**
**Open polish:** swap a designed 1200×630 OG card; consent/cookie banner if EU/PIPL needed;
`IBCHEMHL_ethanfinalpractice` is student-named + EN-only in prod (rename/unlist?); the 114 pre-existing
HS descriptions run long (>155 chars, get truncated in SERPs) — tighten in a future pass if desired.

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
- **`university_calculus_init` (opened 2026-06-09):** active branch for the new University Calculus subject/tier.
  Holds: grounding folder + spec + AUDIT + full pipeline registration + **all 32 Study Guides** (A1 locked
  template; the rest cloned via `scripts/uc_build_unit.py`) + index/sitemap wired (32 cards, "32 units").
  Gates green per the global invariants. **✅ Committed `e830328` (2026-06-10) + PR #4 → `preview`** (awaiting
  staging review → FF to main). Next: Consult-CTA-under-Read-me-first retrofit (115 SGs), then Sprint 3 (ZH) +
  Sprint 4 (P+S). See the STATE/HANDOFF block at the top.

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
