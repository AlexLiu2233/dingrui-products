# University Calculus — Audit

Open punch list for the University Calculus study guides, scored against
[`prompts/create-unit.md`](../prompts/create-unit.md) (the dual-goal contract), the subject spec at
[`rag/subjects/university_calculus.md`](../rag/subjects/university_calculus.md), and the grounding
source-of-record at [`rag/sources/University Calculus/SOURCES.md`](../rag/sources/University%20Calculus/SOURCES.md)
(MIT / Georgia Tech / Princeton syllabi + OpenStax / Strang / Paul's Online Notes).

**Tier definitions**

- **P0** — content-correctness, rigor, or coverage gap that blocks genuine university-level use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but not correctness.
- **P2** — nice-to-have / future work.

**Scope** — this audit covers the *Study Guide*, *Practice Questions*, and *Solutions* products for University
Calculus. This is a NEW subject and NEW tier (first-year university) opened 2026-06-09, the top of the
HS to AP/IB to first-year-uni pipeline. AP Calculus (the high-school AP product) has its own audit at
`AP Calculus/AUDIT.md` and is a distinct, lower-rigor subject.

Last reviewed: **2026-06-09** (Sprint 0 + Sprint 1 + Sprint 2 all closed: **all 32 Study Guides drafted,
validated, and indexed** on branch `university_calculus_init`, uncommitted. Next: Sprint 3 ZH wave, Sprint 4
Practice+Solutions; commit + PR to preview awaiting user go.).

---

## Active Sprint — what we're working on now

### Sprint 0 — Subject genesis / scaffolding (opened 2026-06-09, branch `university_calculus_init`)

**Goal.** Establish the University Calculus subject + first-year-uni tier in the repo. Grounding folder, subject
spec, audit, directory structure, and full build-pipeline registration, so the subject is born indexed,
instrumented (CTA/GA4/SEO), and crawlable.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S0-ground** | Build `rag/sources/University Calculus/` grounding folder (MIT/GT/Princeton syllabi + OpenStax/Strang/Paul's content extracts) + `SOURCES.md` manifest mapping all 32 SGs to source sections | P0 | ~~Open~~ **Resolved** — 7 files (6 extracts + SOURCES.md, 355 lines). Note: open-license binary PDFs were S3/redirect-gated in this env, so sources are URL-referenced markdown extracts (house pattern); drop raw PDFs later if wanted. |
| **S0-spec** | Author `rag/subjects/university_calculus.md` subject spec | P0 | ~~Open~~ **Resolved** |
| **S0-audit** | Author this `University Calculus/AUDIT.md` in PM/sprint format | P0 | ~~Open~~ **Resolved** |
| **S0-dirs** | Create `Study Guides/`, `Practice Questions/`, `Practice Questions/Solutions/` | P0 | ~~Open~~ **Resolved** |
| **S0-index** | Register subject in `scripts/build-index.py` (SUBJECTS + GROUP_BY_LETTER A/B/C/D) and `index.html` (activate Tier-03 band + subject-group sentinels) | P0 | ~~Open~~ **Resolved** — Tier-03 live; A1 card renders under the "Calculus I" group; index.html validates. |
| **S0-inject** | Add `University Calculus` to the 8 injector scripts (CTA-apib, GA4, OG, meta-desc, JSON-LD, canonical, sitemap; UTM slug) + `add_jsonld.py` `level()` branch | P0 | ~~Open~~ **Resolved** — all 8 scripts edited + py_compile clean; A1 born with SEO/CTA/GA4 baked in so injectors no-op on it. |

### Sprint 1 — Draft + LOCK the A1 template Study Guide

**Goal.** Build and lock the canonical template that all other 31 SGs clone from. Locking before bulk prevents
propagating template defects 31 times (the IB Physics HL lesson).

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-A1** | Draft `Unit_A1_Limits_and_Continuity.html` to the full dual-goal contract, English-first, NA-top-10 rigor (epsilon-delta done properly), grounded against the S0-ground sources; re-key SEO/CTA tags; validate exit 0 | P0 | ~~Open~~ **Resolved** — 1,472 lines; 7 sections (incl. full epsilon-delta linear + quadratic proofs), 12 flashcards, 6-item unit quiz, readiness checklist; validate exit 0; gates clean (0 em/en dashes in prose, 0 localStorage, 0 content data-lang, 0 AP leakage). Built by reusing the donor CSS/JS verbatim with cleaned English-only JS. |
| **S1-lock** | User reviews A1 and signs it off as the canonical template | P0 | ~~Open~~ **Resolved 2026-06-09** — user approved A1 ("I like the A1!"), with one change folded in: a consult CTA now sits directly under the hero "Read me first" box (see Standing Principles). A1 is the locked template. |

### Sprint 2 — bulk-draft the remaining 31 Study Guides (opened 2026-06-09)

**Goal.** Clone the locked A1 chrome into the other 31 SGs (A2-A8, B1-B8, C1-C8, D1-D8), English-first,
authoring genuine university-rigor content per unit. **Build tooling (handoff):** use the engine
`scripts/uc_build_unit.py` (`build_and_save(spec)`), which extracts A1's verbatim `<style>` blocks + logo + JS
and wraps a per-unit content spec, baking in BOTH consult CTAs (under Read-me-first and before the flashcards).
Per-unit recipe: write a runner like the (now-deleted) `scripts/_unit_A2.py` defining a `SPEC` dict
(uid, slug, topic, overline, h1, sub, chips, readme, toc, sections HTML, flashcards list, quiz HTML, checklist),
run it, then `python scripts/build-index.py && python scripts/build_sitemap.py`, bump the `subject-group__count`
label in `index.html`, and `bash scripts/validate.sh` the new file. Per-unit content is grounded against
`rag/sources/University Calculus/SOURCES.md`.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-A2** | `Unit_A2_The_Derivative.html` | P0 | ~~Open~~ **Resolved 2026-06-09** — 1,398 lines, validate exit 0, gates clean, indexed + in sitemap. |
| **S2-rest** | Draft A3-A8, B1-B8, C1-C8, D1-D8 (29 SGs) via the engine, in waves by course group | P0 | ~~Open~~ **Resolved 2026-06-09** — all 29 authored by a 29-agent workflow through `uc_build_unit.py`. **SG layer complete: 32/32.** Every file: validate exit 0, 0 dash entities, 0 localStorage, 0 content data-lang, 0 AP leakage; uniform structure (7 sections + unit quiz + checklist, 12 flashcards, 2 CTAs, 8 checklist items). |
| **S2-count** | Keep the `index.html` University Calculus `subject-group__count` label in sync each wave | P1 | ~~Open~~ **Resolved** — label now "32 units"; 4 course groups show 8 each. |

**Note (lesson learned 2026-06-09):** the first workflow wave failed silently because the session was still in
plan mode, which propagates to subagents and blocks all writes (28/29 agents returned plans instead of files).
Clearing plan mode (ExitPlanMode) fixed it; the re-run authored all 29 cleanly. If a future bulk wave returns
"plan mode active" notes, exit plan mode and re-run fresh (cached failed results will not re-execute on resume).

**Sprint 1 deliverable contract** — the A1 Study Guide:
- Hero + "Read me first" intro + sticky TOC sidebar
- ≥6 content sections, each layering: cheat-sheet box -> 1-2 worked examples -> going-deeper/proof block -> recall+synthesis quiz mix
- 8+ flashcards in the locked terse style
- Readiness checklist / self-assessment block at end
- English-only (no `data-lang` span pairs, no language-toggle button); ZH is the Sprint 3 wave
- Prose + KaTeX only (no figures/widgets); reveal-on-click quiz + flashcard flip + theme toggle are the only scripted behaviors
- `<title>` = `University Calculus — Unit A1: Limits and Continuity | Dingrui Scholars`
- Self-referencing SEO tags (canonical/OG/JSON-LD/meta-desc point at the University Calculus path, zero AP-Calc-URL leakage); CTA `utm_campaign=university_calculus`; GA4 present
- No em/en dashes in prose; no `localStorage`; no unicode in `\text{}`
- `bash scripts/validate.sh` exit 0

---

## Cross-Unit Snapshot — 32 study guides

Status legend: `⬜` unbuilt · `🔨` in progress · `✅` shipped

### Group A — Calculus I: Single-Variable Differential Calculus
| ID | Topic | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|
| **A1** | Limits and Continuity | ✅ (locked template) | ⬜ | ⬜ | ⬜ |
| **A2** | The Derivative: Definition and Interpretation | ✅ | ⬜ | ⬜ | ⬜ |
| **A3** | Differentiation Rules (Product, Quotient, Chain) | ✅ | ⬜ | ⬜ | ⬜ |
| **A4** | Derivatives of Transcendental Functions | ✅ | ⬜ | ⬜ | ⬜ |
| **A5** | Implicit Differentiation and Related Rates | ✅ | ⬜ | ⬜ | ⬜ |
| **A6** | Linear Approximation, Differentials, and L'Hopital's Rule | ✅ | ⬜ | ⬜ | ⬜ |
| **A7** | Curve Sketching and Optimization | ✅ | ⬜ | ⬜ | ⬜ |
| **A8** | Antiderivatives and the Definite Integral | ✅ | ⬜ | ⬜ | ⬜ |

### Group B — Calculus II: Single-Variable Integral Calculus & Series
| ID | Topic | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|
| **B1** | Integration Techniques I: Substitution and Integration by Parts | ✅ | ⬜ | ⬜ | ⬜ |
| **B2** | Integration Techniques II: Trig Integrals, Trig Substitution, Partial Fractions | ✅ | ⬜ | ⬜ | ⬜ |
| **B3** | Improper Integrals and Numerical Integration | ✅ | ⬜ | ⬜ | ⬜ |
| **B4** | Applications of Integration: Area, Volume, Arc Length | ✅ | ⬜ | ⬜ | ⬜ |
| **B5** | Further Applications: Work, Center of Mass, Probability | ✅ | ⬜ | ⬜ | ⬜ |
| **B6** | Sequences and Infinite Series | ✅ | ⬜ | ⬜ | ⬜ |
| **B7** | Power Series, Taylor and Maclaurin Series | ✅ | ⬜ | ⬜ | ⬜ |
| **B8** | Parametric Equations and Polar Coordinates | ✅ | ⬜ | ⬜ | ⬜ |

### Group C — Calculus III: Multivariable & Vector Calculus
| ID | Topic | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|
| **C1** | Vectors and the Geometry of Space | ✅ | ⬜ | ⬜ | ⬜ |
| **C2** | Vector-Valued Functions and Curves | ✅ | ⬜ | ⬜ | ⬜ |
| **C3** | Partial Derivatives and the Gradient | ✅ | ⬜ | ⬜ | ⬜ |
| **C4** | Directional Derivatives, Tangent Planes, and Linearization | ✅ | ⬜ | ⬜ | ⬜ |
| **C5** | Optimization and Lagrange Multipliers | ✅ | ⬜ | ⬜ | ⬜ |
| **C6** | Multiple Integrals | ✅ | ⬜ | ⬜ | ⬜ |
| **C7** | Vector Fields, Line Integrals, and Green's Theorem | ✅ | ⬜ | ⬜ | ⬜ |
| **C8** | Surface Integrals, Stokes' Theorem, and the Divergence Theorem | ✅ | ⬜ | ⬜ | ⬜ |

### Group D — Calculus IV: Ordinary Differential Equations
| ID | Topic | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|
| **D1** | First-Order ODEs: Separable and Linear Equations | ✅ | ⬜ | ⬜ | ⬜ |
| **D2** | First-Order Models and Exact Equations | ✅ | ⬜ | ⬜ | ⬜ |
| **D3** | Second-Order Linear ODEs: Homogeneous | ✅ | ⬜ | ⬜ | ⬜ |
| **D4** | Nonhomogeneous Second-Order ODEs | ✅ | ⬜ | ⬜ | ⬜ |
| **D5** | Mechanical and Electrical Vibrations | ✅ | ⬜ | ⬜ | ⬜ |
| **D6** | The Laplace Transform | ✅ | ⬜ | ⬜ | ⬜ |
| **D7** | Systems of First-Order Linear ODEs | ✅ | ⬜ | ⬜ | ⬜ |
| **D8** | Series Solutions and Numerical Methods | ✅ | ⬜ | ⬜ | ⬜ |

**Total deliverables planned: 32 SG × {SG, Practice, Solutions, ZH} = 128.**

---

## Standing Principles

**Dual-goal contract** (inherited from the repo canon; phrased for this tier). Every guide serves two readers
at once:

1. **The struggling student** opening the guide before a midterm. Target: pass. They lift the cheat-sheet
   boxes and the canonical worked examples and walk into the exam.
2. **The mastery reader** studying for depth, an A, or to teach the material. Target: full command. They want
   the derivations, proofs, edge cases, and the *why*.

Concretely, every section layers: cheat-sheet element on top -> 1-2 worked examples -> going-deeper/proof
block (clearly labeled so the crammer skips cleanly) -> quiz mix (recall + synthesis). The full contract lives
in [`prompts/create-unit.md`](../prompts/create-unit.md); edit it there, not here.

**Rigor.** This is genuine university level. Limits get epsilon-delta done properly, theorems get real proofs
or proof sketches, ODE methods get derivations. This is the differentiator versus the AP Calculus subject.

**English-first.** SGs ship English-only; Mandarin is a later wave per `prompts/create-bilingual-translation.md`.

**Grounding.** Every SG is checkable against a committed source in `rag/sources/University Calculus/`. New or
revised content cites its grounding section.

**Consult CTA placement (locked 2026-06-09, user direction).** Every Study Guide carries the consult CTA
**twice**: once directly under the hero "Read me first" box (catches the reader at the top, before they bounce)
and once before the flashcards (catches the reader who finished). The `uc_build_unit.py` engine bakes both in
automatically. This "CTA under Read-me-first" rule is a **repo-wide convention**, not just University Calculus,
and the retrofit across all existing AP/IB/HS Study Guides is tracked as a planned sprint in the root `STATUS.md`.

---

## Known Infra / Tooling Items

(None yet — greenfield. Pipeline registration is tracked as S0-index / S0-inject above.)

---

## P2 — Future Work

(None yet.)

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Practice + Solutions products (32 pairs) | Scoped as Sprint 4, a large fresh-budget sprint, after the SG layer ships and locks. Uses the `pair-key` + `dingrui:version` lock per the IB Math HL / IB Physics HL P+S pattern. |

---

## How to Update This File

When closing a sprint item, mark it with `~~strikethrough~~` and append `**Resolved:** {commit-sha} — {note}`.
When a sprint clears, collapse it into a single "Sprint N closed YYYY-MM-DD" line and promote the next sprint up.
When a unit ships, flip its row in the cross-unit snapshot. The dual-goal contract is edited in
`prompts/create-unit.md`, not here.
