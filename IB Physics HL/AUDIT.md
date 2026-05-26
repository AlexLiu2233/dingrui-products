# IB Physics HL — Audit

Open punch list for the IB Physics HL study guides, scored against
[`prompts/create-unit.md`](../prompts/create-unit.md) (the dual-goal
contract) and the IB Physics 2025+ syllabus (first assessment 2025).

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "going for a 7" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity
  but not exam readiness.
- **P2** — nice-to-have / future work.

**Scope** — this audit covers the *Study Guide*, *Practice Questions*,
and *Solutions* products for IB Physics HL. AP Physics has its own
audit at `AP Physics/AUDIT.md`. Subject spec at
[`rag/subjects/ib_physics_hl.md`](../rag/subjects/ib_physics_hl.md).

Last reviewed: **2026-05-25** (SUBJECT GENESIS: directory + spec
scaffolding created on `ib_physics_hl_init`. Sprint 1 scope TBD pending
user review.

---

## Active Sprint — what we're working on now

### Sprint 1 — Subject genesis + first Study Guides (opened 2026-05-25, branch `ib_physics_hl_init`)

**Goal.** Establish the IB Physics HL subject in the repo, parallel to
IB Math HL. Subject spec + audit + first Study Guide(s) to validate the
template before bulk drafting.

**Scope decisions — TBD pending user review:**

1. Drop the IB Physics 2025 Subject Brief + Guide PDFs into
   `rag/sources/IB Physics HL/`. Re-verify the super-topic numbering
   against the actual guide once it's in.
2. Pick the first Study Guide(s) to draft. Recommended: **A.1
   Kinematics** as the foundational topic (most-tested, parallel to A1
   Sequences in IB Math HL). Then bulk-draft the remaining 23 SGs in
   parallel via foreground subagents — the pattern proven on
   2026-05-24 (IB Math HL SG sprint 9 in parallel).
3. After SGs land, follow the IB Math HL Sprint 3 / 4 / 5 sequence:
   Practice + Solutions drafts → audit-driven v1.1 polish →
   ZH translation pass (or bilingual built-in from initial draft per
   the 2026-05-25 IB Math HL pattern).

**Sprint 1 deliverable contract** — each Study Guide:
- ≥6 content sections, each with cheat-sheet → worked example → going-deeper
- Hero "Read me first" intro + sticky TOC sidebar
- 8+ flashcards in the locked terse style
- Quiz mix (recall + synthesis) per section
- Readiness checklist / self-assessment block at end
- Bilingual EN+ZH built in (Form A inline span pairs)
- `<title>` per spec
- HL-flag chips on HL-only sections / units
- Data-booklet references where formulas come from it (`<code>` glosses)
- `bash scripts/validate.sh` exit 0

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-spec** | Drop IB Physics 2025 Subject Guide PDF into `rag/sources/IB Physics HL/`; verify super-topic numbering | P0 | **Open** |
| **S1-A1** | Draft `Unit_A1_Kinematics.html` Study Guide (foundational, most-tested) | P0 | **Open** |
| **S1-bulk** | Bulk-draft remaining 23 Study Guides in parallel (post-A1 review) | P0 | **Open — blocked on A1 review** |

---

## Cross-Unit Snapshot — 24 super-topics

Status legend: `⬜` unbuilt · `✅` shipped

### Theme A — Space, time and motion (5 super-topics)

| ID | Super-topic | SL/HL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **A.1** | Kinematics | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **A.2** | Forces and momentum | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **A.3** | Work, energy and power | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **A.4** | Rigid body mechanics | HL only | ⬜ | ⬜ | ⬜ | ⬜ |
| **A.5** | Galilean and special relativity | HL only | ⬜ | ⬜ | ⬜ | ⬜ |

### Theme B — The particulate nature of matter (5 super-topics)

| ID | Super-topic | SL/HL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **B.1** | Thermal energy transfers | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B.2** | Greenhouse effect | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B.3** | Gas laws | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **B.4** | Thermodynamics | HL only | ⬜ | ⬜ | ⬜ | ⬜ |
| **B.5** | Current and circuits | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |

### Theme C — Wave behaviour (5 super-topics)

| ID | Super-topic | SL/HL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **C.1** | Simple harmonic motion | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **C.2** | Wave model | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **C.3** | Wave phenomena | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **C.4** | Standing waves and resonance | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **C.5** | Doppler effect | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |

### Theme D — Fields (4 super-topics)

| ID | Super-topic | SL/HL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **D.1** | Gravitational fields | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **D.2** | Electric and magnetic fields | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **D.3** | Motion in electromagnetic fields | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **D.4** | Induction | HL only | ⬜ | ⬜ | ⬜ | ⬜ |

### Theme E — Nuclear and quantum physics (5 super-topics)

| ID | Super-topic | SL/HL | Study Guide | Practice | Solutions | ZH |
|---|---|---|---|---|---|---|
| **E.1** | Structure of the atom | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E.2** | Quantum physics | HL only | ⬜ | ⬜ | ⬜ | ⬜ |
| **E.3** | Radioactive decay | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E.4** | Fission | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |
| **E.5** | Fusion and stars | SL + HL | ⬜ | ⬜ | ⬜ | ⬜ |

**Total deliverables planned: 24 × 4 = 96.**

---

## Dual-Goal Philosophy

**Status:** standing principle, inherited from IB Math HL / AP Physics
canon. Every IB Physics HL study guide must serve two students at once:

1. **The crammer** — the student opening the guide the night before
   Paper 1 or Paper 2. Target: a last-ditch pass (≥4 on the 1–7 scale).
   They skim the cheat-sheet boxes, scan the worked examples, and walk
   into the exam.
2. **The 7-chaser** — the student studying in depth. Target: a 7. They
   want the *why* — derivations, edge cases, HL-only subtleties, data-
   booklet traces.

Concretely, every section layers:

- **Cheat-sheet element at the top** — key formulas / "what you must
  know" callout. Lift-able in under a minute.
- **Worked examples** — canonical exam applications. Identify / Set Up
  / Execute / Evaluate, with data-booklet references inline.
- **Going-deeper block** — derivation, proof, or HL extension. Clearly
  labeled (`box--proof`, expandable `<details>`, or a separate "Why"
  subsection) so the crammer can skip cleanly.
- **Quiz mix** — recall items (crammer-pass) + synthesis items
  (7-chaser).

The full contract lives in [`prompts/create-unit.md`](../prompts/create-unit.md);
edit it there, not here.

### HL vs. SL

The guides are HL-targeted but SL students may use them. Flag HL-only
content with an inline chip or callout so SL students know what they
can skip without missing core material.

---

## Known Infra / Tooling Items

(None yet — Sprint 1 is greenfield.)

---

## P2 — Future Work

(None yet.)

---

## Digital Product Backlog

(None yet.)

---

## How to Update This File

When closing a sprint item, mark it with `~~strikethrough~~` and append
`**Resolved:** {commit-sha} — {one-line note}`. When the sprint clears,
collapse the section into a single "Sprint N closed as of {date}" line
and promote the next sprint up.

When the dual-goal contract needs revision, edit it in
[`prompts/create-unit.md`](../prompts/create-unit.md) and reference the
revision here — don't fork the contract.

When a unit ships, fill in its row of the cross-unit snapshot table
with actual section/worked-example/flashcard/quiz counts.
