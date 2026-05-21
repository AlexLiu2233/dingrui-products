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

Last reviewed: **2026-05-21** (Translation Sprint opened following the
IB Math HL Translation Sprint close; coverage status refreshed —
Reactivity 2 has shipped since the original 2026-05-11 stub).

**Syllabus coverage gap** — current shipped: Structure 1, Structure 2,
Reactivity 1, Reactivity 2. Missing: Structure 3, Reactivity 3,
Tools 1–3 (plus all option topics if HL-specific extensions become a
target).

---

## Active Sprint — what we're working on now

**Translation Sprint — Bilingual EN↔ZH for shipped study guides
(opened 2026-05-21).** All 4 currently-shipped IB Chemistry HL study
guides (Structure 1, Structure 2, Reactivity 1, Reactivity 2)
bilingualizing EN↔ZH against the locked playbook in
[`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).
Sequential, one file at a time, review-then-merge per file. Same
methodology as the IB Math HL Translation Sprint (closed
2026-05-21, commits `cdca220` / `ea3124d` / `12dc6ad` / `ebf8d11`).

| ID | Item | Tier | Status |
|---|---|---|---|
| **T-1** | Structure 1 Particulate Nature of Matter bilingual translation | P1 | **Open** — first up |
| **T-2** | Structure 2 Bonding & Structure bilingual translation | P1 | **Open** |
| **T-3** | Reactivity 1 What Drives Chemical Reactions bilingual translation | P1 | **Open** |
| **T-4** | Reactivity 2 How Much How Fast How Far bilingual translation | P1 | **Open** |

**Audience contract** — Mandarin-Chinese-language students preparing
to write the IB Chemistry HL exam in English. Chinese is a *teaching
translation*; English exam-rubric terminology (atom / molecule /
bonding / electronegativity / Lewis structure / molar / equilibrium /
enthalpy / entropy / Gibbs / etc.) stays in `<code>` inline. Math /
chemical notation untouched.

**Glossary extension required.** Playbook does not yet have an IB
Chemistry HL block. Add one as Structure 1 ships, then extend through
Structure 2 → Reactivity 1 → Reactivity 2 — same incremental approach
that locked AP Physics terminology after U1–U7.

Sprint closes when (a) all 4 files ship, (b) per-file scorecard passes
four axes (EN/ZH balance + glossary fit + pedagogical + validates) for
all 4, (c) no P0/P1 translation issues remain. Structure 3, Reactivity
3, Tools 1–3 will be translated as they ship (separate Translation
Sprint Wave 2 to be opened when those files land).

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
