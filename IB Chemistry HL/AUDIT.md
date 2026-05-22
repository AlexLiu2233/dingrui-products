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

Last reviewed: **2026-05-21** (`improve_study_guides` audit checkpoint —
Sprint 2 opened with worked-examples / exam-tips / sliders + page-fill
focus per the user-locked 3-vector improvement direction).

**Syllabus coverage gap** — current shipped: Structure 1, Structure 2,
Reactivity 1, Reactivity 2. Missing: Structure 3, Reactivity 3,
Tools 1–3 (plus all option topics if HL-specific extensions become a
target).

---

## Active Sprint — what we're working on now

### Sprint 2 — Worked examples / exam tips / sliders + page-fill (opened 2026-05-21)

Audit-driven sprint per the user-locked 3-vector improvement focus
(see `rag/study-guide-audit-checklist.md` Section E + A14).
**English-first**: each item lands as an English revision commit, user
reviews, then the Mandarin follow-up commit picks up the same file
per `prompts/create-bilingual-translation.md`.

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S2-1**~~ | ~~**Reactivity 1**: unicode superscripts `⁻¹` / `⁻³` inside `\text{...}` at lines 625, 644, 701, 720, 912, 1067 — math renders broken (A6 hygiene). Replace with `\mathrm{J\,mol^{-1}}` or `\text{J mol}^{-1}`.~~ | P0 | ✅ closed — `bb6c557` |
| **S2-2** | **Structure 2**: only 1 worked example across 4 topic sections. Add worked examples to 2.1 (ionic), 2.3 (metallic), 2.4 (materials) (E1 dual-goal). | P0 | **Open** |
| ~~**S2-3**~~ | ~~**Page-fill / column parity (A14, user-flagged).** All 4 IB Chem HL files render narrower than sibling subjects do. Diagnose: check `--max-w` value, `.main-wrap` width/margin rules, whether sidebar reserves a column vs. overlays. Side-by-side screenshot vs an AP Physics or IB Math HL sibling at the same viewport. Fix to match.~~ | P1 | ✅ closed — `88a32b5` (added `@media (min-width: 1100px)` block to all 4 files; matches IB Math HL / AP Calc convention) |
| **S2-4** | **Structure 1** add worked example to 1.1 Particulate Nature. **Reactivity 1** add to 1.3 Energy from Fuels. (E1) | P1 | **Open** |
| **S2-5** | **Reactivity 2**: add `#unit-quiz` section with 3 MCQs (sibling parity — other 3 files have one). | P1 | **Open** |
| **S2-6** | All 4 files: per-major-topic exam-tip callout (E2). Currently every file has *one* Exam Strategy section at the bottom. Distribute the strategy guidance to each topic — Paper 1 (no calc) vs Paper 2 framing, mark-allocation cues, "data booklet" reminders, common rubric-loss traps. | P1 | **Open** |
| **S2-7** | **Structure 1, Structure 2, Reactivity 1**: adopt Reactivity 2's "Guiding Question" `concept-box` opener at the top of every topic section (B1 cheat-sheet pattern parity). | P1 | **Open** |
| **S2-8** | Slider widget candidates (E3): IB Chem has zero widgets. Candidates (one slider, one observable each): Maxwell-Boltzmann distribution (temperature slider → visualize tail above $E_a$), equilibrium shift (Le Chatelier — T or [reactant] slider → K change), rate-vs-concentration (order-of-reaction visualizer), Gibbs sign predictor (T slider with $\Delta H$, $\Delta S$ presets). | P2 | **Open** |

**Deferred to bilingual follow-up** (per English-first gate locked
2026-05-21):

- Missing `<code>` glosses in Structure 1 (Avogadro's constant,
  limiting reagent, theoretical yield, percent yield, stoichiometry,
  Aufbau principle, Hund's rule, Pauli exclusion principle, quantum
  number, emission spectrum, absorption spectrum).
- Theme button implementation drift (P2 — Structure 1 uses CSS-only;
  others use JS helper).
- Worked-example markup form drift between files (P2).
- Section-label bilingualization in Structure 2.
- Anchor naming `#s1-1` reuse between Structure 1 and Reactivity 1.

### Translation Sprint Wave 2 — Practice Questions & Solutions — CLOSED 2026-05-22

Bilingual EN↔ZH pass over the IB Chemistry HL Practice Questions and
Solutions surfaces, extending Wave 1 (Study Guides) which closed
2026-05-21. **Second subject to close Wave 2** (after IB Math HL).
Reactivity 2 Practice + Solutions pair shipped on branch
`wave2_ib_chem_hl`.

| ID | Item | Tier | Status | EN/ZH balance |
|---|---|---|---|---|
| ~~**W2-EN**~~ | ~~EN hygiene sweep across Reactivity_2 Practice + Solutions~~ | P1 | ✅ **No-op** — zero CJK characters across both files (no `\text{...}` collision risk); chemical formulas / state symbols / em dashes are paper-chrome convention. No changes needed. | — |
| ~~**W2-1**~~ | ~~`Practice Questions/Reactivity_2_How_Much_How_Fast_How_Far_Practice.html`~~ | P1 | ✅ closed — `29dd0ae` | 96 / 96 ✅ |
| ~~**W2-2**~~ | ~~`Practice Questions/Solutions/Reactivity_2_How_Much_How_Fast_How_Far_Solutions.html`~~ | P1 | ✅ closed — `a6329da` | 138 / 138 ✅ |

**Audience contract** — Mandarin-Chinese-language students preparing
to write the IB Chemistry HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terms remain in `<code>` glosses
inside the Chinese prose. Chemical formulas, state symbols, KaTeX
math untouched.

**Form choice** — Both files use inline `<span data-lang="en">…</span><span data-lang="zh">…</span>`
pairs throughout. The Solutions file's compact bullet-style rationales
fit Form A cleanly (no need for Form B parallel rationale blocks).

**`scripts/validate.sh`** passes on both files.

**Glossary check** — IB Chem HL Wave 1 terminology applied as-is.
Reactivity-2-specific kinetics terms locked inline via `<code>`
glosses: reaction rate / collision theory / collision frequency /
activation energy / catalyst / Maxwell–Boltzmann distribution /
energy profile / intermediate / transition state / order of reaction
/ rate equation / rate constant / mechanism / rate-determining step
/ molecularity / unimolecular / Arrhenius equation / enolisation /
colorimetry / spectrophotometer / Beer–Lambert / systematic vs
random error.

**Commits on `wave2_ib_chem_hl`:**

- `29dd0ae` — W2-1 Reactivity 2 Practice ZH translation (96/96, +109/−96)
- `a6329da` — W2-2 Reactivity 2 Solutions ZH translation (138/138, +151/−138)

**Note — out of Wave 2 scope (build, not translate).** Practice + Solutions
companions for Structure 1, Structure 2, Reactivity 1 do not exist yet;
they join a Wave 2 extension as they ship. Structure 3, Reactivity 3,
Tools 1–3 are covered by Sprint 1 (Syllabus coverage gap) and will land
bilingual end-to-end under the locked English-first → ZH cadence.

---

### Sprint 1 (still queued) — Syllabus coverage gap

Original P0 work; preserved here so it isn't lost.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-1** | Draft `Structure_3_Classification_of_Matter.html` | P0 | **Open** |
| **S1-2** | Draft `Reactivity_3_What_are_the_Mechanisms.html` (organic + electron transfer) | P0 | **Open** |
| **S1-3** | Draft Tools 1–3 study guides (experimental, technology, math/data) | P0 | **Open** |
| **S1-4** | Standing principle: dual-goal contract or domain-specific philosophy | P1 | **Open** |

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

**Commits on `main` (fast-forwarded 2026-05-21):**

- `9630110` — T-1 Structure 1 Particulate Nature of Matter
- `54ac31b` — T-2 Structure 2 Bonding & Structure
- `1c7f483` — T-3 Reactivity 1 What Drives Chemical Reactions
- `e855c1e` — T-4 Reactivity 2 How Much How Fast How Far
- `03e6834` — AUDIT close-out

**Sprint 1 (Syllabus coverage gap — Structure 3, Reactivity 3,
Tools 1–3) and Sprint 2 (Worked examples / exam tips / sliders + page-fill)
both promoted to the Active Sprint section above.**

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
