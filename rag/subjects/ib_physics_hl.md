# Subject Spec — IB Physics HL

## Identity

- **Display (section heading):** IB Physics HL
- **Display (hero chip):** IB Physics HL
- **Directory:** `IB Physics HL/`
- **Audit:** `IB Physics HL/AUDIT.md` (Sprint 1 = subject genesis — scope TBD after spec review)
- **IB-authoritative source:** `rag/sources/IB Physics HL/` (Subject Brief + Subject Guide, first assessment **2025**) — **TODO**: drop PDFs into this directory once obtained from the IB store; spec below is best-effort against published structure.

## Official curriculum reference — 2025 syllabus

**IB Diploma Physics, first assessment 2025.** The 2025+ guide replaced
the 2016 syllabus's "Topics 1–12 + Options" structure with **5 Themes
(A–E)** common to both SL and HL, plus HL-extension sub-topics flagged
inline. Options were removed entirely.

SL students take a strict subset of the Themes; HL students take the
full subset plus HL-only super-topics within each Theme.

## Naming convention

Units are named after their 2025 super-topic ID — the consumer-facing
student can match any super-topic reference in the IB Physics guide
directly to one of our units.

```
IB Physics HL/Study Guides/Unit_<SuperID>_<Slug>.html
IB Physics HL/Practice Questions/Unit_<SuperID>_<Slug>_Practice.html
IB Physics HL/Practice Questions/Solutions/Unit_<SuperID>_<Slug>_Solutions.html
```

`<SuperID>` is one of the 22 2025 super-topic identifiers (`A.1`, `A.2`,
…, `E.5`). The IB guide uses dotted form `A.1` (with period); for
filename purposes we collapse to `A1` (no period) to match the AP
Physics + IB Math HL filename pattern already in this repo. So:
2025 super-topic A.1 "Kinematics" → `Unit_A1_Kinematics.html`.

## Required `<title>` format

```
IB Physics HL — Unit {SuperID}: {Super-topic Title} | Dingrui Scholars
```

Example: `IB Physics HL — Unit A1: Kinematics | Dingrui Scholars`.

## Exam structure — 2025 first assessment

- **Paper 1 (1h30 SL / 2h HL):** MCQs + data response (Section A
  multiple-choice, Section B data-based).
- **Paper 2 (1h30 SL / 2h30 HL):** Short-answer + extended-response,
  free-response. Calculator + data booklet allowed on every paper.
- **Internal Assessment:** Scientific investigation, 10 hours (SL & HL).

Total external assessment: SL 3h / HL 4h30 (80% of final grade).

> **Practice-question chrome implication.** Unlike IB Math AA, every
> physics paper is calculator-allowed. There is no "no-calc" vs "calc"
> split to encode. Practice files should use the **Paper 1 MC** /
> **Paper 1 Data** / **Paper 2 Short** / **Paper 2 Extended** pill
> taxonomy (or simply Paper 1A / 1B / 2A / 2B with EMH).

## Standing principle — dual-goal contract

Every guide serves two students at once: the **crammer** (last-ditch
pass the night before, aiming for ≥4) and the **7-chaser** (going deep
for top score). Canonical articulation in `prompts/create-unit.md`.
Each section layers: cheat-sheet at top → worked example(s) →
"going deeper" derivation / data-booklet trace. Quiz items mix recall
and synthesis.

Flashcards (when present) follow the locked terse style: prompt on
front, `$$formula$$` or single-line answer on back, no prose.

## HL flagging

HL-only super-topics (A.4 Rigid body mechanics, A.5 Galilean & special
relativity, B.4 Thermodynamics, D.4 Induction, E.2 Quantum physics)
carry the `hl-flag` chip at unit level. Within a mixed SL/HL
super-topic, individual sections carry `hl-flag` chips per the pattern
already used in IB Math HL units.

A reader should see at a glance which content is HL-extension material.

---

## Unit list — 2025 super-topic enumeration (22 units total — TBD verify against guide)

Hours figures TBD until the IB guide PDF is in `rag/sources/`.

Status legend:
- ✅ **shipped** — Study Guide live on `main`.
- ⬜ **unbuilt** — no coverage in the repo yet.

### Theme A — Space, time and motion (5 super-topics)

| ID | Super-topic | SL/HL | Status |
|---|---|---|---|
| **A.1** | Kinematics | SL + HL | ⬜ |
| **A.2** | Forces and momentum | SL + HL | ⬜ |
| **A.3** | Work, energy and power | SL + HL | ⬜ |
| **A.4** | Rigid body mechanics | HL only | ⬜ |
| **A.5** | Galilean and special relativity | HL only | ⬜ |

### Theme B — The particulate nature of matter (5 super-topics)

| ID | Super-topic | SL/HL | Status |
|---|---|---|---|
| **B.1** | Thermal energy transfers | SL + HL | ⬜ |
| **B.2** | Greenhouse effect | SL + HL | ⬜ |
| **B.3** | Gas laws | SL + HL | ⬜ |
| **B.4** | Thermodynamics | HL only | ⬜ |
| **B.5** | Current and circuits | SL + HL | ⬜ |

### Theme C — Wave behaviour (5 super-topics)

| ID | Super-topic | SL/HL | Status |
|---|---|---|---|
| **C.1** | Simple harmonic motion | SL + HL | ⬜ |
| **C.2** | Wave model | SL + HL | ⬜ |
| **C.3** | Wave phenomena | SL + HL | ⬜ |
| **C.4** | Standing waves and resonance | SL + HL | ⬜ |
| **C.5** | Doppler effect | SL + HL | ⬜ |

### Theme D — Fields (4 super-topics)

| ID | Super-topic | SL/HL | Status |
|---|---|---|---|
| **D.1** | Gravitational fields | SL + HL | ⬜ |
| **D.2** | Electric and magnetic fields | SL + HL | ⬜ |
| **D.3** | Motion in electromagnetic fields | SL + HL | ⬜ |
| **D.4** | Induction | HL only | ⬜ |

### Theme E — Nuclear and quantum physics (5 super-topics)

| ID | Super-topic | SL/HL | Status |
|---|---|---|---|
| **E.1** | Structure of the atom | SL + HL | ⬜ |
| **E.2** | Quantum physics | HL only | ⬜ |
| **E.3** | Radioactive decay | SL + HL | ⬜ |
| **E.4** | Fission | SL + HL | ⬜ |
| **E.5** | Fusion and stars | SL + HL | ⬜ |

**Total: 24 super-topics, 6 HL-only.**

> **Verification note.** The above super-topic numbering reflects the
> 2025+ syllabus structure as published by IB. Before opening Sprint 1
> for any specific SG, verify the sub-bullet enumeration against the
> Subject Guide PDF (when in `rag/sources/IB Physics HL/`). Sub-bullet
> numbering may shift slightly between exam years.

---

## Cross-subject conventions

- Match the design tokens (maroon accent, DM Serif headings, Source Sans
  body, JetBrains Mono code) used by AP Physics + IB Math HL.
- Bilingual EN+ZH **built in from initial draft** (the IB Math HL B/C/E
  P+S burst of 2026-05-25 established this as the locked default).
  Inline `<span data-lang="en">…</span><span data-lang="zh">…</span>`
  pairs throughout; locked toggle infra (`#langToggle` button, no
  `localStorage`, CJK font fallback).
- Mirror the IB Math HL P+S structure: per-question pill chrome (qnum,
  difficulty, paper, topic, marks), M1/A1/R1/AG mark callouts in
  Solutions, insight blocks per question (exam-trap level, not
  platitudes). Reference: `IB Math HL/Practice Questions/Solutions/Unit_B1_Representation_of_Functions_Solutions.html`.

## Data booklet

The IB Physics data booklet ships with every paper. Solutions should
cite data-booklet formulas by name + `<code>` reference where used
(e.g. "from the data booklet, `T = 2π√(L/g)`"). This is the
physics-specific equivalent of citing exam-rubric terms.

## Forbidden-term watchlist (initial)

To be extended once Wave 1 translation lands. Likely candidates from
AP Physics terminology audit (2026-05-19):
- `折返点` (turning point — old) → `转折点` (correct)
- `点积` (dot product — set-theoretic) → `标量积` (scalar product, physics)
- `路径长度` (path length — generic) → `路程` (physics path length)
- `缓冲溃缩区` → `溃缩区` (crumple zone)
- `冲量—动量定理` → `动量定理` (impulse-momentum theorem)

Verify alignment with the AP Physics terminology in
`AP Physics/AUDIT.md` translation section.
