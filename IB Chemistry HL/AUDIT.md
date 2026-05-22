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

Last reviewed: **2026-05-21** (Translation Sprint closed same day as
opened; all 4 shipped IB Chem HL study guides bilingualized EN↔ZH on
branch `ib_chem_hl_translation`, 4 commits T-1..T-4 awaiting user
review before fast-forward to main).

**Syllabus coverage gap** — current shipped: Structure 1, Structure 2,
Reactivity 1, Reactivity 2. Missing: Structure 3, Reactivity 3,
Tools 1–3 (plus all option topics if HL-specific extensions become a
target).

---

## Translation Sprint — CLOSED 2026-05-21

Bilingual EN↔ZH translation of all 4 shipped IB Chemistry HL study
guides on branch `ib_chem_hl_translation` against the locked playbook
in [`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md)
(IB Chem HL glossary block added to the playbook at sprint open;
mirrors the AP Physics audit-locked terminology pattern). All 4 files
pass the four-axis scorecard (EN/ZH balance + glossary fit +
pedagogical + validates).

| ID | Item | Tier | Status | Parity | Lines (before → after) |
|---|---|---|---|---|---|
| **T-1** | Structure 1 Particulate Nature of Matter | P1 | **Shipped** | 175/175 | 1172 → 1304 |
| **T-2** | Structure 2 Bonding & Structure | P1 | **Shipped** | 138/138 | 1069 → 1208 |
| **T-3** | Reactivity 1 What Drives Chemical Reactions | P1 | **Shipped** | 167/167 | 1144 → 1216 |
| **T-4** | Reactivity 2 How Much How Fast How Far | P1 | **Shipped** | 270/270 | 1320 → 1459 |

**Audience contract** — Mandarin-Chinese-language students preparing
to write the IB Chemistry HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terminology stays in `<code>`
inline; chemical formulas, state symbols, KaTeX math untouched.

**Locked terminology** — IB Chem HL glossary block in
`prompts/create-bilingual-translation.md` covers Structure 1/2,
Reactivity 1/2. Wave 2 (Structure 3, Reactivity 3, Tools 1–3) will
extend the same tables as those files ship.

**Commits on `ib_chem_hl_translation` branch (awaiting user review +
fast-forward to main):**

- `9630110` — T-1 Structure 1 Particulate Nature of Matter
- `54ac31b` — T-2 Structure 2 Bonding & Structure
- `1c7f483` — T-3 Reactivity 1 What Drives Chemical Reactions
- `e855c1e` — T-4 Reactivity 2 How Much How Fast How Far

**Next**: Structure 3, Reactivity 3, Tools 1–3 to be drafted in
Sprint 1 (queued below) — those will be bilingual from the start.

### Sprint 1 (queued) — Syllabus coverage gap

Once the Translation Sprint closes, this Sprint picks up the
unshipped syllabus topics. Original P0 work; preserved here so it
isn't lost.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-1** | Draft `Structure_3_Classification_of_Matter.html` | P0 | **Open** |
| **S1-2** | Draft `Reactivity_3_What_are_the_Mechanisms.html` (organic + electron transfer) | P0 | **Open** |
| **S1-3** | Draft Tools 1–3 study guides (experimental, technology, math/data) | P0 | **Open** |
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
