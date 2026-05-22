# AP Calculus AB/BC — Audit

Open punch list for the AP Calculus AB/BC study guides and practice questions,
scored against `prompts/create-unit.md`, `rag/subjects/ap_calculus_bc.md`,
and the official AP Calculus AB/BC Course and Exam Description (CED).

**Tier definitions**

- **P0** — content-correctness or coverage gap that blocks "shooting for a
  5" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only. Practice
question files and any future digital products are out of scope.

Last reviewed: **2026-05-21** (`improve_study_guides` audit checkpoint —
Sprint 2 opened with worked-examples / exam-tips / sliders focus per
the user-locked 3-vector improvement direction).

---

## Active Sprint — what we're working on now

### Sprint 2 — Worked examples / exam tips / sliders (opened 2026-05-21)

Audit-driven sprint per the user-locked 3-vector improvement focus
(see `rag/study-guide-audit-checklist.md` Section E). **English-first**:
each item lands as an English revision commit, user reviews, then the
Mandarin follow-up commit picks up the same file per
`prompts/create-bilingual-translation.md`.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S2-1** | **U6** `Unit_6_Integration_Accumulation.html`: CJK characters inside `\text{...}` at lines 1850 (`\text{分子}`, `\text{分母}`) and 2056 (`\text{A 段}`, `\text{B 段}`) — math renders broken (A6 hygiene). Replace with `\mathrm{}` or move Chinese outside math. | P0 | **Open** |
| **S2-2** | **U8** `Unit_8_Applications_of_Integration.html`: CJK in `\text{}` at lines 390 (`\text{净流入量}`) and 917 (`\text{其中 }`). Same fix (A6). | P0 | **Open** |
| **S2-3** | **U5** `Unit_5_Analytical_Applications_of_Differentiation.html`: topics 5.3–5.10 and 5.12 have **no worked example** (only prose + concept boxes). Add ≥1 visible worked example per topic (E1 dual-goal). | P0 | **Open** |
| **S2-4** | **U9** `Unit_9_Parametric_Polar_and_Vectors.html`: worked examples in topics 9.2, 9.3, 9.5, 9.8 are collapsed inside `<details>` — crammer can't lift in <1 min. Surface them (E1 / B2). | P0 | **Open** |
| **S2-5** | **U10** `Unit_10_Sequences_and_Series.html`: all 14 worked examples are collapsed inside `<details>` — same structural inversion. Surface them (E1 / B2). | P0 | **Open** |
| **S2-6** | **U8** stub topic 8.5 (formula box + 2 sentences, no example); topic 8.12 (washer about other axes) has no worked example. Fill in (E1). | P0 | **Open** |
| **S2-7** | **U7** `Unit_7_Differential_Equations.html`: topics 7.2 (slope fields), 7.3 (exponential), 7.4 (logistic) — only 4 worked examples for 9 topics. Add 2–3 more (E1). | P1 | **Open** |
| **S2-8** | Cross-corpus exam-tip callouts (E2): add `box--tip` / "AP Trap" / paper-strategy boxes for trap patterns (U-sub sign flip, FTC subtle conditions, BC parametric/polar conversions, infinite-series convergence-test choice). Currently scattered; missing on most topics. | P1 | **Open** |
| **S2-9** | Slider widget candidates (E3): AP Calc has fewer interactive widgets than AP Physics. High-leverage one-slider-one-concept candidates: limit explorer (h → 0), Riemann sum (n rectangles), Taylor polynomial (n terms), logistic curve (carrying-capacity slider). Each = single slider, one observable. | P2 | **Open** |

**Deferred to bilingual follow-up** (per English-first gate locked
2026-05-21):

- `localStorage.setItem('drs.lang', …)` in `toggleLang()` across 9 of 10
  files (U8 already clean) — strip in translation follow-up.
- Quiz markup convergence (A9 — U3 / U7 / U8 diverge from sibling pattern).
- Per-section quiz coverage gaps (B4 — U5/U7/U8/U9/U10 push most quizzes
  to end-of-unit).
- Going-deeper proof block density (B3 — demoted to P1 per new checklist;
  not in this sprint).
- Section-ID convention drift (A9 — `topic-4-N` vs `s4-N` etc.).
- TOC anchor orphans (common-mistakes, mvt-explorer not linked from sidebars).

---

## Closed Sprints

### Translation Sprint — closed 2026-05-18

All 10 AP Calc study guides made bilingual EN↔ZH; commit `3ab03d5` on
`main`. Translation philosophy and locked conventions captured in
`prompts/create-bilingual-translation.md`. Per-file audit table is the
section immediately below.

---

## Translation audit (per-file, post-ship)

**Audit target.** All 10 AP Calc study guides bilingualized to support a
Mandarin-Chinese-language student writing the AP exam in English. Chinese
is a *teaching translation* — explains the concept; English exam-rubric
terms remain in `<code>` inline so the student recognizes them on the
exam paper.

**Audit method.** (1) Structural — count `data-lang="en"` vs
`data-lang="zh"` attributes; they must be equal. (2) Lexical — verify
core AP-Calc terminology is consistently rendered across files
(glossary in `prompts/create-bilingual-translation.md`). (3)
Pedagogical — spot-read sample concept-boxes / worked-examples in each
file; check the Chinese explains rather than literally translates.
(4) Validation — `scripts/validate.sh` passes on each file.

### Per-file scorecard

| # | Unit | EN/ZH balance | Glossary fit | Pedagogical | Validates | Notes |
|---|---|---|---|---|---|---|
| 1  | Limits & Continuity                            | 340 / 340 ✅ | ✅ | ✅ | ✅ | Direct-substitution + indeterminate-form glosses applied. Limit-laws section reads cleanly. |
| 2  | Differentiation: Definition & Properties       | 250 / 250 ✅ | ✅ | ✅ | ✅ | "商的法则" (not "商法则") — extended form; consistent with rest of corpus. |
| 3  | Composite, Implicit, & Inverse Functions       | 237 / 237 ✅ | ✅ | ✅ | ✅ | Chain Rule + implicit differentiation glosses applied throughout. |
| 4  | Contextual Applications of Differentiation     | 258 / 258 ✅ | ✅ | ✅ | ✅ | Particle-motion section: 速度 / 加速度 / 速率 with English glosses inlined. Related-rates worked examples translated cleanly with step labels. |
| 5  | Analytical Applications of Differentiation     | 292 / 292 ✅ | ✅ | ✅ | ✅ | MVT / EVT / IVT glosses applied; extrema terminology consistent. |
| 6  | Integration & Accumulation                     | 254 / 254 ✅ | ✅ | ✅ | ✅ | LRS / RRS / MRS / trapezoidal glosses inside Chinese tables. Riemann-sum widget text bilingualized via Form A inline pairs. Antiderivative → 原函数 (standard math term, consistently). |
| 7  | Differential Equations                         | 304 / 304 ✅ | ✅ | ✅ | ✅ | Separation of variables; logistic ODEs; slope-field terminology. |
| 8  | Applications of Integration                    | 232 / 232 ✅ | ✅ | ✅ | ✅ | Volume-of-revolution, washer / disk / shell terminology preserved as exam terms in English with Chinese explanation. |
| 9  | Parametric, Polar, & Vector-Valued Functions   | 202 / 202 ✅ | ✅ | ✅ | ✅ | Parametric / polar / vector consistently rendered. |
| 10 | Infinite Sequences & Series                    | 405 / 405 ✅ | ✅ | ✅ | ✅ | Taylor / Maclaurin / convergence / divergence — full glossary applied. |

### Findings — corpus-wide

- **All 10 files have perfectly balanced `data-lang="en"` / `data-lang="zh"`
  attribute counts.** Every English block has a Chinese pair; zero orphans.
- **Glossary is consistent across all 10 files.** Spot-checked 20 core terms
  (limit / derivative / integral / Chain Rule / Product Rule / Quotient Rule /
  MVT / FTC / Riemann sum / antiderivative / parametric / polar / vector /
  Taylor / Maclaurin / converge / diverge / implicit / related rates /
  continuous) — every appearance uses the same Chinese rendering.
- **Exam-term gloss pattern applied across all units.** English exam
  vocabulary appears parenthesised in `<code>` inside the Chinese text.
  Density varies by topic (U10 / U7 highest, U5 lowest — matches the
  natural density of exam terms in each topic).
- **Math notation untouched.** All LaTeX renders identically in both
  languages — Chinese flip changes only the prose.
- **Bilingual infrastructure is identical across all 10 files.** Both CSS
  rules (`body:not(.lang-zh)…` and `body.lang-zh…`) present;
  `toggleLang()` JS present with `localStorage` persistence under
  `drs.lang`; nav button between Contents and Dark in every file.
- **CJK font fallback** present in `--font-body` for all 10 files —
  PingFang SC → Hiragino Sans GB → Microsoft YaHei cascade.
- **`scripts/validate.sh` passes on all 10.** The `WARN: odd number of $`
  warnings in U5 / U6 / U9 are pre-existing heuristic noise (escaped `\$`
  and CSS dollar-signs in font-family declarations) — not real
  unclosed-math issues.

### Findings — none requiring follow-up

The translation work is **publish-ready**. No P0 / P1 translation issues
found.

### Optional refinements (P2 — not blocking)

| ID | Item | Why P2 |
|---|---|---|
| TR-1 | Add a `lang="en"` / `lang="zh"` attribute (HTML standard) on the toggled spans/divs to enhance screen-reader behavior (currently the toggle is purely visual via CSS `display: none`) | A11y polish; current behavior works fine for sighted users which is the dominant use case |
| TR-2 | Print stylesheet: decide whether `@media print` should default to EN or to the currently-toggled language. Today print follows the screen toggle, which is fine. | Edge case; consult once a Chinese-language student requests printable practice |
| TR-3 | Translation of `<title>` tags so browser tab reads in Chinese when in zh mode (currently `<title>` is EN-only) | Minor browser-chrome polish |

---

## Standing Principles

*To be locked once a content sprint begins.* Candidates:

- Dual-goal contract (crammer + 5-chaser) — same as IB Math HL.
- Worked-example density: ≥ 2 per concept section.
- **Translation contract (locked 2026-05-18):** Chinese is a teaching
  translation, not literal. English exam-rubric terminology stays in
  `<code>` inline. Math notation untouched. See
  [`prompts/create-bilingual-translation.md`](../prompts/create-bilingual-translation.md).

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | AP Calculus Practice Questions bilingual pass | The Practice files (`Unit_1_*_Practice_Problems.html`–`Unit_10`) are not yet bilingualized; lower leverage than the Study Guides for first-pass Mandarin audience. Reopen if a Chinese-language pilot user requests it. |
