# HS STEM — Deployment-Readiness Audit & Polish Sprint

**Checkpoint (2026-06-03).** All 66 HS STEM Study Guides are drafted and now sit
on a single branch **`hs_stem_complete`** (Math 15 + Physics 12 + Chemistry 14 +
Biology 12 + CS 13). In-guide diagrams/graphs were **scrapped** (the static-SVG
trial was not accurate enough; Manim/video conflicts with the constraints) —
guides are **prose + KaTeX only**. This sprint takes the corpus from "drafted"
to **a finished, marketable, bilingual digital product ready to deploy** to the
website.

## Goal
Audit every HS file and fix what's needed so the whole High School tier
(5 subjects) can fast-forward to `main` and deploy as a polished product — no
embedded pictures, just clean, correct, consistent, fully-bilingual guides that
surface properly on the landing page.

## Audit dimensions (find → fix in-sprint, log findings in each subject AUDIT)
1. **Content accuracy.** Per the verification rule: every syllabus-map code and
   exam claim traces to a fetched `rag/sources/` extract; formulas/worked
   examples correct; no fabricated codes. (Watch AB codes — OCR-scramble caveat.)
2. **Bilingual completeness & quality.** EN span count == ZH on every file (run
   `scripts/translation_coverage.py`); spot-check ZH translation quality and
   that quiz options / captions are paired.
3. **Consistency / chrome parity.** Title format, nav badge, hero (no "Unit N:"),
   syllabus-map (4 columns), region/paper chips, honors-flag usage, dual-goal
   sections, flashcards + readiness checklist present, footer — uniform across
   all 5 subjects.
4. **Link & anchor integrity.** Feeder-links resolve to files that exist (no
   broken hrefs); TOC anchors resolve; cross-references valid.
5. **Cross-platform polish.** Dark mode (no light-only colors), mobile @375px
   (no horizontal scroll), print preview clean, KaTeX renders. Document the
   benign odd-`$` validate WARN (KaTeX/JS `$`), not a defect.
6. **Copy / tone.** Consultant voice; **no em/en dashes in prose** (per the
   locked copy-tone rule); scrub AI-tells.
7. **`scripts/validate.sh`** exits clean on every HS file.

## Deployment integration (the "ship it" half)
- Add **HS Chemistry, HS Biology, HS Computer Science** to
  `scripts/build-index.py` `SUBJECTS` (unused chip colours) and add their
  **subject-group blocks** under the "High School Foundations" tier in
  `index.html`; re-run `build-index.py` so all 66 cards surface (EN + ZH).
  (HS Math + HS Physics are already wired in.)
- Confirm the High School Foundations tier renders all 5 subjects in both
  languages (the stale `data-zh-ready` gate was already lifted for HS Math +
  Physics; verify it covers the new subjects).

## Execution
- All work on **`hs_stem_complete`** (already holds every SG). Audit **subject by
  subject** (Math, Physics, Chemistry, Biology, CS) so each can be reviewed;
  fixes committed per subject.
- Use parallel subagents for the per-file audit sweep (read-only find), then
  apply fixes; re-validate. Keep the per-file gate: validate PASS + EN==ZH.

## Exit criteria (ready to deploy)
- All HS files validate clean; EN==ZH everywhere; no broken links; dark/mobile/
  print OK; tone rules satisfied.
- `build-index.py` regenerated; all 66 HS cards visible on the landing page in
  EN + ZH.
- Then: FF `hs_stem_complete` → `main` + `preview`, push (CI deploys). Practice +
  Solutions remain a later, separate wave.
