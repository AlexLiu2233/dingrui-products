# IB Chemistry HL — Audit

Open punch list for the IB Chemistry HL study guides, scored against
`prompts/create-unit.md`, `rag/subjects/ib_chemistry_hl.md`, and the IB
Chemistry HL syllabus (first exams 2025).

**Tier definitions**

- **P0** — content-correctness or coverage gap that blocks "going for a 7"
  use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only.

Last reviewed: **2026-05-11** (audit stub created during workflow
standardization; content not yet inventoried).

**Syllabus coverage gap** — current shipped: Structure 1, Structure 2,
Reactivity 1. Missing: Structure 3, Reactivity 2, Reactivity 3, Tools 1–3
(plus all option topics if HL-specific extensions become a target).

---

## Active Sprint — what we're working on now

**No active sprint.** Closing the syllabus coverage gap is the obvious
first sprint.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-1** | Draft `Structure_3_Classification_of_Matter.html` | P0 | **Open** |
| **S1-2** | Draft `Reactivity_2_How_Much_How_Fast_How_Far.html` (kinetics + equilibrium) | P0 | **Open** |
| **S1-3** | Draft `Reactivity_3_What_are_the_Mechanisms.html` (organic + electron transfer) | P0 | **Open** |
| **S1-4** | Standing principle: dual-goal contract or domain-specific philosophy | P1 | **Open** |

---

## Standing Principles

*To be locked once a sprint begins.* IB Chemistry HL uses the IB's
syllabus-theme structure (Structure / Reactivity / Tools) rather than
numbered units — `build-index.py` has an explicit word-priority map that
honors this. Don't switch to "Unit N" naming without updating that map.

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | Interactive periodic-table widget for trend exploration | Beyond slider-only interaction philosophy. |
| DP-2 | Mechanism arrow-pushing builder | Drawing UI; stateful; far beyond static HTML. |
