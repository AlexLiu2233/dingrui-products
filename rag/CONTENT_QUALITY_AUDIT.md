# Study Guide Content Quality Audit + Improvement Plan

**Opened:** 2026-06-11 · **Owner:** content · **Instrument:** `scripts/sg_quality_sweep.py`
**Scope:** all 170 Study Guides across every tier (HS 66 / AP 21 / IB 51 / UNI 32).

> **The goal (user-stated):** every guide must serve *two* readers at once —
> **(a) cram-level**: night-before usability (key ideas + one clean worked example per
> concept, flashcards, quiz), and **(b) full-mark depth & breadth**: enough rigor,
> worked variety, edge-cases, and theory that a strong student can reach the top of
> the mark scheme / NA-top-10 standard. This audit measures how far each guide is from
> *both*.

---

## Method

1. **Quantitative sweep over all 170 files** (`sg_quality_sweep.py`): EN-visible word
   count (zh spans stripped so bilingual HS/AP/IB and EN-only UC are compared on the
   same axis), section count (breadth), worked examples, "going deeper" depth blocks,
   KaTeX display blocks, flashcards, quiz blocks, consult-CTA count.
2. **Qualitative deep-read** of a representative sample (UC A1 locked template + thin
   agent-authored UC guides B1/C6) to interpret what the numbers mean for actual rigor.

Re-run anytime: `python scripts/sg_quality_sweep.py` (table) or `--csv`.

---

## Headline findings

**1. University Calculus is the depth-deficit tier — confirmed quantitatively.**
EN-word **median by tier** (all EN-only counts, apples-to-apples):

| Tier / subject | n | min | median | max |
|---|--:|--:|--:|--:|
| HS Math | 15 | 6726 | **7588** | 8574 |
| HS Physics | 12 | 6534 | **7477** | 8378 |
| HS Chemistry | 14 | 6758 | **7686** | 9128 |
| HS Biology | 12 | 5446 | **6551** | 7510 |
| HS Computer Science | 13 | 4962 | **7111** | 8376 |
| AP Calculus | 10 | 2697 | **5007** | 6735 |
| AP Physics | 7 | 4611 | **5711** | 7337 |
| AP CSA | 4 | 4744 | **5313** | 7457 |
| IB Math HL | 23 | 3320 | **5479** | 10652 |
| IB Chemistry HL | 4 | 2981 | **3341** | 4792 |
| IB Physics HL | 24 | 4789 | **5493** | 7272 |
| **University Calculus** | **32** | **1699** | **3383** | **5035** |

UC sits at **~45% of the HS median** and **~60–65% of the leaner AP/IB unit-format
median**. Even UC's own best (A1, the hand-crafted locked template, ~5035) is at the
*top* of the UC range; the 31 agent-authored guides regress well below it. This matches
the user's read: the bulk drafts came out thin.

**2. The thinness is in DEPTH, not breadth.** Deep-read of UC C6 (Multiple Integrals,
2584 EN words) shows **complete topical breadth** — 7 sections (double integrals over
rectangles → general regions → polar → applications → triple → cylindrical/spherical →
change of variables), 8 worked examples, 3 going-deeper blocks, flashcards, quiz,
checklist. The structure and scaffolding are right. What's missing is *depth per
concept*: ~370 words/section means typically **one** worked example per subtopic where a
full-mark guide wants **two or three** plus edge-cases, common-error analysis, and a
fuller "going deeper" proof. **Verdict: UC is cram-level + breadth COMPLETE, but not yet
full-mark DEPTH.**

**3. Secondary thin outliers (non-UC), for a later pass:**
- AP Calculus Unit 9 (Parametric/Polar/Vectors) — 2697, the single thinnest non-UC guide.
- IB Chemistry HL (all 4) — median 3341; oldest tier, never depth-expanded.
- IB Math HL Unit B1 (Representation of Functions) — 3320, low end of an otherwise solid tier.

**4. HS / AP / IB are otherwise healthy** on depth (medians 5000–7700) — they are mature,
shipped, and audited. No systemic depth problem outside UC + the four outliers above.

---

## Plan — prioritized

### Workstream 1 (mechanical, in flight): Intro consult-CTA retrofit
- **Scope correction:** **138** SGs need the intro CTA (66 HS + 72 AP/IB), NOT the
  "115" in old STATUS notes (that predated IB Physics HL +24 and IB Math expansion).
  UC's 32 already carry both CTAs (engine-baked).
- Insert the consult-CTA directly under each guide's hero/read-me block (mirroring UC's
  `</section><aside class="consult-cta">` placement); keep the existing end CTA.
- Idempotent injector modeled on `add_consult_cta_apib.py`; bilingual where the file is.
- **Gate:** validate exit 0, EN==ZH parity unchanged, run `lang_link_continuity.py`.
- **Pilot first:** 1 HS + 1 AP/IB for placement sign-off, then sweep all 138.

### Workstream 2 (content, the real quality lift): **UC Depth Expansion sprint** — ✅ DONE 2026-06-11
The headline finding. Bring the 31 sub-template UC guides up to (and above) the A1 depth bar.
**SHIPPED to branch `uc_depth_expansion` (`af7b187`), awaiting user review → PR to preview.**
Method chosen: multi-agent workflow (Option b), target "higher than A1". A 62-agent
`expand -> adversarial verify` pipeline (Opus) deepened all 31 guides in place. Result:
UC EN-word **median 3383 -> 5979** (min now 2801 = the untouched A1, max 7661); every
expanded guide clears the old A1 number. Verify caught 4 isolated arithmetic errors in
new examples (B3, C1, C5, D8) — all hand-fixed and re-checked; all 32 UC SGs validate
exit 0. **Note:** A1 (2801, user-locked) is now the *thinnest* UC guide — open question
for the user whether to expand it too or keep it locked.
- **Target:** ~5000–6000 EN words/guide (A1 standard), achieved by **adding depth, not
  padding**: a 2nd/3rd worked example per major subtopic, common-error/"why this is
  wrong" notes, and fuller "going deeper" proofs. Breadth already exists — do not add
  sections, deepen them.
- **Sequencing by thinness** (from the sweep; thinnest first): B1 (2562), C6 (2584),
  C2 (2773), B7 (3019), A8 (3054), B6 (3140), B4 (3171), D6 (3276)… up through the
  ~3400–3800 band. The ~4000–5035 guides (A1/A3/A7/C1/C7/D3/D4) are closest to bar.
- **Per-guide recipe:** re-open against `rag/sources/University Calculus/SOURCES.md`;
  keep the locked A1 structure; add depth; re-validate; keep EN-only (ZH is a later wave).
- **Method options (user picks):** (a) I expand them sequentially in waves, reviewed
  per wave; or (b) a multi-agent workflow fans out one agent per guide against the A1
  template + SOURCES, with an adversarial "is this actually full-mark depth?" verify
  pass. Option (b) is far faster but spends materially more tokens — needs explicit opt-in.

### Workstream 3 (content, smaller): non-UC thin outliers — P2
AP Calc U9, IB Chem HL ×4, IB Math B1. Depth-expand to their tier median. Low urgency
(mature tiers, isolated cases).

### Out of scope here (tracked elsewhere)
- UC Practice + Solutions (32 pairs) and UC ZH translation — separate sprints (see STATUS).
- CJK-in-EN sweep on P+S/AP/IB — see STATUS watch-list.

---

## Decision log
- 2026-06-11: audit opened; UC depth deficit established. Awaiting user's pick on
  Workstream-2 method (sequential waves vs multi-agent workflow) and on whether the
  full-mark target is "match A1 (~5–6k words)" or higher.
- 2026-06-11: user picked **multi-agent workflow** + **higher than A1**. Ran a 62-agent
  expand+verify workflow over the 31 guides (`af7b187` on `uc_depth_expansion`); UC median
  3383 -> 5979 words; 4 verify-flagged math errors fixed; all validate exit 0. Workstream 2
  closed. Discovered A1's real count is 2801 (not the 5035 first reported — that was D4),
  so A1 is now the thinnest UC guide; flagged to user. WS1 intro-CTA already on preview (PR #8).
