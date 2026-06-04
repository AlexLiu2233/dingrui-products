# Translation Coverage — EN ↔ ZH Pairing Checklist

**Internal tracker.** Lives in `rag/` so it is stripped from the deployed site.
Regenerate the live numbers anytime with `python scripts/translation_coverage.py`.

## Philosophy (locked 2026-05-31)

**Every English note must have a Chinese pair.** For every `data-lang="en"`
span the page renders, there must be a matching `data-lang="zh"` span carrying
the faithful Simplified-Chinese counterpart. This applies to:

1. **The landing page** (`index.html`) — the storefront. It must read fully in
   both languages, with no English string left unpaired.
2. **Every content file created in a sprint** — Study Guides, Practice, and
   Solutions ship bilingual-from-start (or get a retro pass) so they surface in
   ZH mode the moment they land.

Mechanism: `body.lang-zh` CSS toggle + a `toggleLang()` script + back-to-back
`<span data-lang="en">…</span><span data-lang="zh">…</span>` pairs. A file is
**PAIRED** when its EN and ZH span counts are equal and non-zero.

Scope of this tracker: **High School → AP/IB only.** University tier is out of
scope for now.

---

## Internal checklist — current state (2026-05-31)

| Surface | Files | PAIRED | EN-only (needs ZH) | Notes |
|---|---|---|---|---|
| **Landing** `index.html` | 1 | ✅ 1 | 0 | 236/236 spans paired |
| **High School Math** | 45 | 44 | 0 | 1 benign PARTIAL (see below) |
| **AP CSA** | 12 | ✅ 12 | 0 | fully paired |
| **IB Chemistry HL** | 6 | ✅ 6 | 0 | fully paired |
| **IB Math HL** | 67 | ✅ 67 | 0 | fully paired |
| **IB Physics HL** | 1 | ✅ 1 | 0 | A.1 only (subject still scaffolding) |
| **AP Calculus** | 18 | 10 | **8** | all SGs paired; **8 Practice EN-only** |
| **AP Physics** | 21 | 7 | **14** | all SGs paired; **7 Practice + 7 Solutions EN-only** |
| **TOTAL in scope** | 150 | 128 | **22** | |

**Benign PARTIAL (no action):** `High School Math / … / Unit_4_Rational_and_Radical_Expressions_Solutions.html`
is 310 EN / 311 ZH by design — a ZH word-order split places prose on both sides
of an inline `<code>HSN-RN.A.1</code>` where English only needs it before. Both
languages render correctly.

---

## Files needed — the 22 EN-only files (the only real gaps)

### AP Calculus — 8 Practice Problems files (no separate Solutions files exist)
- `Unit_1_Limits_and_Continuity_Practice_Problems.html`
- `Unit_2_Differentiation_Practice_Problems.html`
- `Unit_3_Composite_Implicit_Inverse_Practice_Problems.html`
- `Unit_4_Applications_of_Differentiation_Practice_Problems.html`
- `Unit_5_Curve_Sketching_Optimization_Practice_Problems.html`
- `Unit_6_Integration_and_Accumulation_Practice_Problems.html`
- `Unit_7_Differential_Equations_Practice_Problems.html`
- `Unit_8_Applications_of_Integration_Practice_Problems.html`

(AP Calc Units 9–10 have Study Guides only — no Practice — and the SGs are paired.)

### AP Physics — 14 files (7 Practice + 7 Solutions, Units 1–7)
- `Unit_1_Kinematics_Practice_Problems.html` + `…_Solutions.html`
- `Unit_2_Force_and_Dynamics_…` (P + S)
- `Unit_3_Work_Energy_Power_…` (P + S)
- `Unit_4_Linear_Momentum_…` (P + S)
- `Unit_5_Torque_and_Rotational_Dynamics_…` (P + S)
- `Unit_6_Energy_and_Momentum_of_Rotating_Systems_…` (P + S)
- `Unit_7_Oscillations_…` (P + S)

These 22 files are the tail of **Translation Wave 2** (the original 31-file wave;
AP CSA, IB Chem HL, and IB Math HL P+S have since been closed).

---

## Active Sprint — LP-1: Landing Page Refresh + Pairing Lock

Branch: `landing_page_refresh` (off `main` @ `170940f`).

| ID | Item | Tier | Status |
|---|---|---|---|
| **LP1-improve** | Improve `index.html` (scope to be confirmed with user — candidates: hero/value-prop clarity, subject-card layout & tier framing, mobile responsiveness, nav discoverability). | P0 | open — awaiting scope |
| **LP1-pairing-verify** | Confirm the landing page's 236/236 pairing is not just count-equal but content-faithful; any new copy added during LP1-improve ships with its ZH pair in the same commit. | P0 | open |

---

## Proposed next sprints (to close the 22-file translation tail)

Sequence after LP-1, each its own branch, FF-merged after review:

1. **Sprint 7-Phys-PS** — AP Physics 14 P+S files → ZH. Largest single block;
   closes the AP Physics translation that Wave 1 (SGs) started.
2. **Sprint 7-Calc-P** — AP Calculus 8 Practice files → ZH. Smaller, finishes
   AP Calculus to fully paired.

(These two together close Translation Wave 2 entirely. They can also be run as
one combined "Wave 2 close" sprint of 22 files if token budget allows.)

Separately tracked, not translation: **HS Math Sprint 7** carries the two
items deferred from HS Math Sprint 6 — S6-PS-mark-normalize (P1) and
S6-P2-polish (P2). See `High School Math/AUDIT.md`.

---

## How to refresh this checklist

```bash
python scripts/translation_coverage.py
```

Prints the per-file EN/ZH span matrix and a PAIRED / PARTIAL / EN-ONLY tally per
subject. Re-run after any translation sprint and update the table above.
