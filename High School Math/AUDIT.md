# High School Math — Audit

Open punch list for the High School Math product, scored against the
canonical generation prompt ([`prompts/create-unit.md`](../prompts/create-unit.md))
plus the subject-specific spec at
[`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md)
and the CCSSM High School standards.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  exam / SAT / AP-feeder use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only.
Practice Questions, SAT-prep cross-references, and bilingual translation
all live in the [Digital Product Backlog](#digital-product-backlog) until
those product surfaces spin up.

Last reviewed: **2026-05-16** (subject scaffolding only; no unit content yet).

---

## Active Sprint — what we're working on now

**Sprint 0 — Subject scaffolding.** Lay the groundwork so any of the
four courses (Algebra I, Geometry, Algebra II, Pre-Calculus) can be
opened as Sprint 1 without further bootstrap work.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S0-1**~~ | Author subject spec at `rag/subjects/high_school_math.md` | P0 | ✅ shipped 2026-05-16 |
| ~~**S0-2**~~ | Author this audit file with Sprint 0 framing | P0 | ✅ shipped 2026-05-16 |
| ~~**S0-3**~~ | Create empty `Study Guides/` and `Practice Questions/Solutions/` folders | P0 | ✅ shipped 2026-05-16 |
| **S0-4** | Decide which course opens as Sprint 1 (Algebra I is the default — most students enter the funnel there) | P0 | **Open** — awaiting user direction |
| **S0-5** | Lock the Practice Questions format for this subject (AP-style MCQ? IB-style short/extended? SAT mixed?). Defer until Sprint 1 ships at least one Study Guide. | P1 | Deferred |

Build order for next sprint: pick S0-4, then open a Sprint 1 for that
course (Sprint 1A for Algebra I, 1G for Geometry, etc. — letter suffix
keeps the four course sprints distinguishable in commit messages).

---

## Standing principles

- **Dual-goal contract** — every guide must serve both the
  test-tomorrow crammer (≥ pass) and the depth student (5 on the AP
  feeder course). Cram cheat-sheet on top, going-deeper proofs at the
  bottom. Locked from IB Math HL; canonical articulation in
  [`prompts/create-unit.md`](../prompts/create-unit.md).
- **CCSSM tagging optional but encouraged** — small chip near each
  section heading citing the standard (e.g. `HSF-LE.A.2`). Helps
  teachers map content to their pacing guides.
- **No HL flag** — there is no "HL only" tier in HS Math. Where a topic
  is honors-level in a typical US classroom, mark with an
  `honors-flag` chip (CSS to be defined when first used).
- **Pathway clarity** — units flag their AP feeder explicitly. Algebra II
  → AP Calculus, AP Statistics. Pre-Calculus → AP Calculus, AP Physics.
  Geometry → AP Computer Science Principles (logic-heavy).
- **Course-prefix in filenames** (locked in subject spec). Flat layout;
  no per-course sub-directories. Single `Study Guides/` and
  `Practice Questions/` directories per the existing convention.

---

## Cross-Course Snapshot

| Course | Units shipped | Sprint open |
|---|---|---|
| Algebra I       | 0 | — (Sprint 1A queued) |
| Geometry        | 0 | — |
| Algebra II      | 0 | — |
| Pre-Calculus    | 0 | — |

When the first unit in a course ships, list it here with section /
worked-example / quiz counts (mirror the IB Math HL audit table).

---

## Topic Scope Reminders (CCSSM, traditional pathway)

These are skeleton lists — verify against the official CCSSM scope
before drafting any sprint. The subject spec at
[`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md)
holds the canonical skeleton; copies here only as a quick reference.

### Algebra I (8–10 units typical)
Linear functions · Linear systems · Exponents & exponential functions ·
Polynomials & factoring · Quadratic functions · Quadratic equations ·
Rational & radical expressions · Statistics & data displays.

### Geometry (8–10 units typical)
Transformations · Congruence · Similarity · Right triangles &
trigonometry · Circles · Polygons & quadrilaterals · 3D figures &
volume · Coordinate geometry · Geometric proofs.

### Algebra II (8–10 units typical)
Functions review & transformations · Quadratic functions & complex
numbers · Polynomial functions · Rational functions · Radical functions
& relations · Exponential & logarithmic functions · Sequences & series
· Trigonometric functions · Statistics & data analysis.

### Pre-Calculus (8–10 units typical)
Functions & graphs · Polynomial & rational functions · Exponential &
logarithmic functions · Trigonometric functions · Analytic trigonometry
· Trig applications (vectors, polar, complex) · Systems & matrices ·
Conic sections · Sequences, series, & probability · Introduction to
limits.

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday
in a richer interactive product or follow-on sprint.

| ID  | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice Questions product (MC and FRQ-style sets per unit, with Solutions companion mirroring IB Math HL A3 pattern) | Needs Study-Guide content first to anchor question scope. Open after Sprint 1 ships ≥3 study guides in a single course. |
| DP-2 | SAT / ACT cross-reference cards on each guide | Format and question-pattern templates need a separate scoping pass. |
| DP-3 | ZH translation track (mirroring `ap_chinese_translation` for AP Calc) | Defer until the EN content stabilises. Translation churn on a moving target is wasteful. |
| DP-4 | Per-course pacing-guide / scope-and-sequence overview pages | Useful for teachers; needs all units in a course to ship first. |
| DP-5 | Honors-flag CSS chip and audit pass for honors-level topics in each course | Define CSS when the first honors topic is drafted. |

---

## How to update this file

When closing a sprint item, mark it with `~~strikethrough~~` and append
`✅ shipped YYYY-MM-DD — {one-line note}`. When the sprint clears,
collapse the section into a single "Sprint N closed YYYY-MM-DD" line in
a `## Closed Sprints` section and promote the next sprint up.

When standing principles need revision, edit them here, but route any
philosophy that applies subject-wide back to
[`rag/subjects/high_school_math.md`](../rag/subjects/high_school_math.md)
or [`prompts/create-unit.md`](../prompts/create-unit.md) — don't fork
the contract.

When a course's first unit ships, fill in its row of the cross-course
snapshot table with the actual section / worked-example / quiz counts.
