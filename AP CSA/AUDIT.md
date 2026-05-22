# AP Computer Science A — Audit

Open punch list for the AP CSA products (Study Guides + Practice Questions),
scored against `prompts/create-unit.md`, `rag/subjects/ap_csa.md`, and the
official AP Computer Science A Course and Exam Description (CED).

**Tier definitions**

- **P0** — content-correctness or coverage gap that blocks "shooting for a
  5" use of the product.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the two shipped products: the
*Study Guide* (`Study Guides/Unit_N_*.html`) and the *Practice Questions*
companion (`Practice Questions/Unit_N_*_Practice_Problems.html` + matched
`Solutions/` page). Anything that would require a Java runtime, MCQ
grading state, or other server / WASM work lives in the
[Digital Product Backlog](#digital-product-backlog).

Last reviewed: **2026-05-21** (`improve_study_guides` audit checkpoint —
Sprint 2 opened with worked-examples / exam-tips / sliders focus per
the user-locked 3-vector improvement direction).

**CED coverage status** — Units 1–4 ship with both Study Guide *and*
AP-style Practice Questions. AP CSA CED runs Units 1–10; Units 5–10
(Writing Classes, Array, ArrayList, 2D Array, Inheritance, Recursion) are
unbuilt on both surfaces. This is the headline gap.

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
| **S2-1** | All 4 units: per-section worked-example density audit (E1). U1 has 7 explicit "Worked Example" labels for 15 topics; U2/U3 have similar gaps. Many sections jump from concept-box to `<pre>` snippet without a labelled worked-example wrapper. Add labelled wrappers so the canonical exam application is discoverable per topic. | P1 | **Open** |
| **S2-2** | All 4 units: per-topic exam-tip callouts (E2). Existing "AP Trap" callouts are the model — extend to all 15/12/9/17 topics in U1/U2/U3/U4. Targeted at AP Java FRQ trap patterns: `==` vs `.equals()`, autoboxing, `null` checks, off-by-one in array traversals, integer division, pass-by-value-of-reference. | P1 | **Open** |
| **S2-3** | Slider widget candidate list (E3). AP CSA has zero slider widgets. Candidates (one slider, one concept each): traversal step-through (slider = array index), recursion depth tracer (slider = call count), iteration-vs-recursion comparison (slider = n), array growth visualizer. P2 because this is a new product surface, not a regression fix. | P2 | **Open** |

**Sprint 1 still active for separate workstream**: **S1-1** Units 5–10
CED coverage gap (P0). Pulls into a future sprint, not this one.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-1** | Ship Units 5–10 to close CED coverage gap (Writing Classes, Array, ArrayList, 2D Array, Inheritance, Recursion) on both surfaces | P0 | **Open** |
| **S1-2** | Standing principle: pick whether AP CSA needs a Code Sandbox surface, or worked-snippets are enough | P1 | **Open** |
| ~~**S1-3**~~ | ~~Practice Questions sub-product — none exist yet for this subject~~ | P1 | ✅ closed — U1 first cut `6b43af9`, refactored to exam-level `dd93b83`, U2/U3/U4 shipped `2239c20`, cross-linked from study guides `976ed5a` |

**Deferred to bilingual follow-up** (per English-first gate locked
2026-05-21):

- `localStorage.setItem('drs.lang', …)` in `toggleLang()` across all 4
  files — strip in translation follow-up.
- Code-comment translation cleanup (~168 instances of
  `<span class="cm" data-lang="zh">…</span>` siblings inside `<pre>`
  blocks across U1–U4; code comments don't translate per playbook).
- Title long-form normalization (`AP CSA` → `AP Computer Science A`).
- Quiz markup parity (U1 inner-span vs U2/U3/U4 paired-div).
- Unit 3 missing MCQ Patterns section.
- Flashcard terseness rewrites.
- Unit 3 CSS un-minify.

### Recently shipped (closed during Sprint 1)

Captured here for traceability — none of these were tracked items at
sprint open; they were ad-hoc polish runs that prepared the product for
the practice cut-over.

| Item | Commit |
|---|---|
| U1 Study Guide sellable polish (worked examples + AP-trap callouts + MCQ patterns) | `d8ae727` |
| U2 Study Guide sellable polish | `1fada52` |
| U3 Study Guide sellable polish | `6b80aab` |
| U4 Study Guide sellable polish | `e7be1fd` |
| U1/U2/U4 de-AI voice pass | `4358ed0` |
| U3 de-AI voice pass | `84f5ead` |
| U1 Practice + Solutions exam-level refactor | `dd93b83` |
| U2/U3/U4 Practice + Solutions shipped (15 AP MCQs each: 3 MED + 12 HARD) | `2239c20` |
| Study Guide → Practice Questions CTA links (U1–U4) | `976ed5a` |

---

## Standing Principles

Locked 2026-05-14 once Sprint 1 closed and the practice product became a
real surface.

### Code-snippet styling

AP CSA is the only subject in the repo that doesn't use KaTeX (Java code
only — `validate.sh` was patched to make the KaTeX check conditional).
Code blocks use the `JetBrains Mono` font, the cream-paper `#F8F6F1`
background in print contexts, and dark-mode-aware `--bg-code` in the
Study Guide chrome.

### Practice Questions product shape

Each shipped Practice Questions companion follows the U1 template:

1. **15 AP-style MCQs per unit**, weighted **3 MEDIUM + 12 HARD**. No
   "easy" tier — this is top-score prep, not a diagnostic.
2. **Code-trace heavy.** Most prompts present a fully-formed code
   segment and ask "what is printed / what is the value of."
3. **Realistic distractors with named traps.** Each Solutions page calls
   out the specific misconception each wrong option targets (off-by-one,
   missing `this.`, no-`break` "find-last," forgotten short-circuit,
   etc.).
4. **Paper-style chrome.** Same letter-sized print layout, brand chip,
   topic / difficulty / `[1]` mark pills, page-break before Q8 (so the
   first half fits on one printed page).
5. **Solutions are a separate file** in `Practice Questions/Solutions/`,
   with the correct option highlighted in a green band and a full
   rationale block under each question.

Any future practice-set additions (Sprint 2 onward) inherit this
contract.

### Cross-link contract

Every shipped study guide ends with a `#ap-practice` "Next Step" section
that links to the matching Practice Problems + Solutions HTML using
`%20`-encoded relative paths. Style uses existing `--accent` /
`--accent-light` / `--bg-card` tokens so dark mode + print both behave.

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | In-browser Java sandbox / runner | Requires a server or WASM Java runtime; well beyond the static-HTML envelope. |
| DP-2 | MCQ grader for AP-style practice | Stateful; needs answer storage and explanation reveal. The current Practice Questions PDF/print model deliberately skips this — the Solutions HTML is the answer-key surface. |
| DP-3 | Spaced-review deck across U1–U4 (flashcard SRS) | Stateful; out of single-HTML-file envelope. The in-page flashcards inside each study guide are the static stand-in. |
