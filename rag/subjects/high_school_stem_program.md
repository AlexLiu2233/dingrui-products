# High School STEM — Program Roadmap

**Goal (locked 2026-05-31).** Complete the entire **High School Foundations
STEM tier**: one topic-organised, bilingual study-guide set per subject,
serving the four target curricula — **US, BC, Ontario, Alberta**. High School
Math is done; this program adds **Physics, Chemistry, Biology, and Computer
Science** to parity.

This is the cross-subject plan of record. Each subject also has its own spec
(`rag/subjects/high_school_<subject>.md`) and audit
(`High School <Subject>/AUDIT.md`).

## Depth & conventions (locked)

- **Study Guides first.** Bulk-draft bilingual SGs across every unit first;
  Practice + Solutions follow in a later catch-up wave per subject. (This is
  the arc HS Math actually took.)
- **Bilingual-from-start.** Every new SG ships with paired
  `<span data-lang="en">` + `<span data-lang="zh">` markup + the `toggleLang()`
  script in the same commit. New subjects do **not** repeat HS Math's
  English-first / retroactive-ZH detour (which cost Sprints 5–6).
- **Template inheritance.** Mirror the locked HS Math chrome: 8-row
  grade-by-region nav, `syllabus-map` (4 columns US/ON/BC/AB), region +
  paper-style chips, `honors-flag` (harder provincial stream), `feeder-link`
  (to the AP/IB college-credit tier), 7 content sections (dual-goal contract),
  flashcards, readiness checklist. No "Unit N:" in visible chrome.
- **US standard is curriculum-specific, NOT "Common Core" for science/CS:**
  - Science (Physics/Chem/Bio): **NGSS** (HS-PS / HS-LS performance expectations).
  - Computer Science: **CSTA K-12 Level 3** + **AP CSP** framework.
  - (Math keeps CCSSM — that is the one subject where US = Common Core.)
- **Source-grounding gate.** Per the standing verification rule, every
  syllabus-specific claim (course code, topic placement, exam emphasis) must
  cite a fetched curriculum document before that unit's SG content locks.
  Unit lists below are **draft, pending per-unit source verification**.

## Subjects & scope

| Subject | Spec | Audit | Units (draft) | Status |
|---|---|---|---|---|
| High School Math | `high_school_math.md` | `High School Math/AUDIT.md` | 15 | ✅ complete — full bilingual triplet |
| High School Physics | `high_school_physics.md` | `High School Physics/AUDIT.md` | 12 | scaffolded — SGs pending |
| High School Chemistry | `high_school_chemistry.md` | `High School Chemistry/AUDIT.md` | 14 | scaffolded — SGs pending |
| High School Biology | `high_school_biology.md` | `High School Biology/AUDIT.md` | 12 | scaffolded — SGs pending |
| High School Computer Science | `high_school_cs.md` | `High School Computer Science/AUDIT.md` | 13 | scaffolded — SGs pending |

New SG corpus to produce: **~51 bilingual Study Guides** (Physics 12 +
Chemistry 14 + Biology 12 + CS 13), then per-subject Practice + Solutions.

## Sprint sequence (proposed)

Each subject follows the proven HS Math arc. Run subjects sequentially so each
gets a clean review gate (per the review-then-merge cadence); within a subject,
bulk-draft SGs via parallel subagents.

1. **STEM-Phys** — Physics: source-ground 4 curricula → lock Unit 1 SG template
   → bulk-draft remaining 11 SGs (bilingual). Branch `hs_physics_sg`.
2. **STEM-Chem** — Chemistry: same arc, 14 SGs. Branch `hs_chemistry_sg`.
3. **STEM-Bio** — Biology: same arc, 12 SGs. Branch `hs_biology_sg`.
4. **STEM-CS** — Computer Science: same arc, 13 SGs (language-agnostic;
   pseudocode + Python). Branch `hs_cs_sg`.
5. **Index + landing integration** — at each subject's first SG ship, add it to
   `scripts/build-index.py` SUBJECTS (unused chip colour) and add a subject
   group to the "High School Foundations" tier in `index.html`. Keep the
   landing page fully EN/ZH paired (see `rag/translation-coverage.md`).
6. **P+S catch-up waves** — per subject, after its SGs ship.

Order rationale: Physics and Chemistry have the densest curriculum overlap with
the existing Math/IB Chem corpus (most reusable chrome + feeder-links), so they
go first; Biology and CS follow.

## Open decisions for the user

- **Subject order** — proposed Physics → Chemistry → Biology → CS. Adjust if a
  different subject is higher commercial priority.
- **Source-grounding depth** — fetch + extract all four curricula per subject
  before drafting (highest fidelity, slower), or draft from the standards-
  informed unit lists now and grounding-verify before merge? HS Math fetched
  PDFs first; recommend the same for exam-claim fidelity.

## Cross-references

- Per-subject specs: `rag/subjects/high_school_{physics,chemistry,biology,cs}.md`
- Template subject: `rag/subjects/high_school_math.md`
- Unit generation contract: `prompts/create-unit.md`
- Translation pairing checklist: `rag/translation-coverage.md`
- Style tokens: `rag/style-guide.md`
