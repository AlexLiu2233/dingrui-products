# Create HS Practice + Solutions Set

<task>
Produce a bilingual **Practice + Solutions** HTML pair for one High
School STEM unit (Physics / Chemistry / Biology / Computer Science /
Math). The two files are locked to each other by a `dingrui:version`
tag that `scripts/validate.sh` enforces; bumping a version on one
without the other is a build error. This is the HS sibling of
[`create-ib-practice-and-solutions.md`](create-ib-practice-and-solutions.md)
— **read that first** for the question-card / solution-card CSS contract
and the version-pair invariant, which are identical here. This file
records only what HS does **differently**.
</task>

<inputs>
- **Subject**: {{SUBJECT}}              *e.g. `High School Physics`*
- **Unit (file stem N)**: {{UNIT_N}}    *sort key only — NEVER shown in chrome*
- **Topic**: {{TOPIC}}                  *e.g. `Kinematics`*
- **Companion SG**: {{SG_PATH}}         *the shipped Study Guide this pairs to*
- **Pair key**: `HS-<Subj>-<N>`         *e.g. `HS-Phys-1`, `HS-Chem-5`*
- **Version**: starts at `v1`; bump both files together
</inputs>

<what_is_different_from_ib>

The IB playbook is the structural base. HS diverges on **six** points —
these mirror the HS Study-Guide conventions (see `STATUS.md` "HS vs
AP/IB conventions"):

| # | IB | **HS** |
|---|---|---|
| 1 **Difficulty** | MED + HARD only, no EASY | **EASY + MED + HARD**, leaning MED (~4 : 7 : 4). HS is a foundations tier; a confidence-building EASY opener per Part is correct. |
| 2 **Exam framing** | Paper 1A / 1B / 2 | **Three Parts by response type**, not IB papers: **PART I Short Response** (SAT-style MCQ + ON/BC unit-test style) · **PART II Extended Response** (AP/IB-feeder FRQ + Honors) · **PART III Modeling / Applied** (Universal). |
| 3 **Region chips** | single syllabus | **US / ON / BC / AB** region pills per question (the 4-region crosswalk). Use the AB **Diploma-exam** style where the subject has one (Physics 30, Chem 30, Bio 30) — a genuine standardized hook. Math Unit 1 used 3 regions; add AB wherever the topic is in the AB course. |
| 4 **Honors stream** | HL purple flag | gold **`pill honors`** on the Extended-Response / beyond-grade-level items. Matches the SG honors-flag. |
| 5 **Bilingual** | retrofitted later | **bilingual-from-the-start.** Every visible string is a paired `<span data-lang="en">…</span><span data-lang="zh">…</span>`. **EN span count == ZH span count** in BOTH files is an exit gate (`scripts/translation_coverage.py` / the per-file sweep). Quiz options, Part headers, banner, marks legends, `answer-line`, `insight` — all paired. Math notation inside `$…$` is shared (not duplicated). |
| 6 **Title + tag** | `Unit A3 … colon` form, `v1.0` | **no-colon, no visible "Unit N"**: `<title>High School <Subject> — <Topic> — Practice \| Dingrui Scholars</title>`. Version is `v1` (not `v1.0`). Tag: `<!-- dingrui:version v1  dingrui:pair-key HS-<Subj>-<N>  dingrui:doc-type practice -->` (`solutions` on the other). |

Everything else — the `.q` / `.solution` card CSS, `answer-line`,
`marks-call` chips (`M1·A1`), the **`.insight` block on every solution**,
per-sub-part `[N]` marks that sum to the header pill, footer version
chip — is **identical to the IB contract**. Do not re-derive it.
</what_is_different_from_ib>

<contract>

- **Question count**: ~10–14 items. **Mark target ~80**, distributed
  PART I : II : III ≈ 25 : 30 : 25.
- **Coverage**: re-read the companion Study Guide's section list; every
  section must appear in at least one question. The Practice set is the
  exam-prep companion to that exact SG.
- **No EASY in Part III.** EASY lives only as the opener of Parts I/II.
- **Subject-specific notation**: Physics/Chem/Math use KaTeX `$…$`. **CS
  uses `<pre><code>`** (pseudocode + Python, **un-translated** — code is
  language-neutral) NOT KaTeX, exactly as the CS Study Guides do.
- **No interactive JS** beyond the locked language/theme toggles (same
  lock as the SGs). Practice has the student `.work` space; Solutions
  has static reveals only (no `<details>` quiz JS).
- **Honesty on syllabus fit**: if a topic is honors-only or absent from a
  region's course (e.g. no AB standalone kinetics, NGSS qualitative-only
  on some topics), don't fake a region chip — drop it or honors-flag it,
  matching what the SG's syllabus crosswalk already states.
</contract>

<workflow>

1. **Read the companion Study Guide first** (`{{SG_PATH}}`). List every
   section; the Practice must cover them and the Solutions may use only
   notation/results the SG introduced.
2. **COPY-THEN-EDIT — do not write from scratch.** A full bilingual P+S
   pair is ~1000 lines and exceeds the 32k single-write cap. Clone the
   locked HS Math Unit 1 pair (it already carries the full bilingual
   chrome: region/exam pills, 3-Part scaffold, banner, footer, toggle):
   ```
   cp "High School Math/Practice Questions/Unit_1_Linear_Functions_and_Systems_Practice.html" \
      "<Subject>/Practice Questions/Unit_<N>_<Topic>_Practice.html"
   cp "High School Math/Practice Questions/Solutions/Unit_1_Linear_Functions_and_Systems_Solutions.html" \
      "<Subject>/Practice Questions/Solutions/Unit_<N>_<Topic>_Solutions.html"
   ```
   Then transform per-section with small Edits: `<title>`, the
   `dingrui:` tag (pair-key + doc-type), banner, the subject framing,
   and each question/solution card. Keep the chrome; swap the content.
3. **Draft the question list before writing cards** — one line each:
   Part, difficulty, region(s), topic/skill, marks, and the *concept
   extension* it tests (HS still extends beyond recall on MED/HARD).
4. **Verify every answer before writing the Solutions file.** Compute
   concrete numbers, check units (Physics/Chem), trace code (CS). A
   Solutions file with arithmetic errors is worse than none.
5. **Write Practice first, Solutions second**; sub-part labels and marks
   match exactly across the pair.
6. **Per-file gate before commit** (same as the SG waves):
   - `bash scripts/validate.sh "<file>"` → PASS on both
   - EN span count == ZH span count on both (the recurring off-by-one
     causes: `data="en"` typo, doubled span, an unwrapped quiz option /
     Part header / marks legend — fix with a focused Edit)
   - leftover-grep ≈ 0 (no source-topic terms bleeding through from the
     cloned Math Unit 1: `linear|slope|intercept|系统|斜率`)
   - per-question marks sum to the header pill; pair-key + version agree
     across banner, footer chip, and the `dingrui:` comment
   - dash sweep per [`_tone.md`](_tone.md) (`—`, `–`, `&mdash;`,
     `&ndash;`, `&#8212;`, `&#8211;`) — math operators exempt
</workflow>

<execution_at_scale>

Building a whole subject's P+S end-to-end (the locked sprint shape):

1. **Lock Unit 1 as the template** — fully build + validate one pair,
   user reviews, THEN fan out. (Mirrors how each SG subject started.)
2. **Waves of ~4** Sonnet subagents (`model: sonnet`), copy-then-edit
   from the locked Unit 1 of *this* subject (not Math) once it exists —
   each agent reads the companion SG + Unit 1 pair, transforms, runs the
   per-file gate. Commit per wave so an API outage costs ≤ one wave.
3. After all pairs land + validate: `python scripts/build-index.py` (so
   the Practice cards surface), review-then-merge per the locked cadence
   (`feedback_review_merge_pattern`), FF to `preview` then `main`.
</execution_at_scale>

<reminders>
The HS-specific invariants most often missed, restated:

1. **Bilingual parity is an exit gate.** EN == ZH spans on BOTH files,
   every visible string paired. This is the #1 HS-vs-IB difference.
2. **No visible "Unit N".** Topic-only title + chrome; the `Unit_N_`
   filename is a sort key, never shown.
3. **EASY allowed (HS), but never in Part III**, and the set still leans
   MED with a HARD/Honors tail.
4. **`dingrui:version v1` + `pair-key HS-<Subj>-<N>` match on both files.**
   `validate.sh` is the gate.
5. **`.insight` block on every solution** — the differentiator from a
   vanilla answer key (same as IB).
6. **CS code is un-translated `<pre><code>`, not KaTeX.**
</reminders>

<cross_references>
- Structural base (read first): [`create-ib-practice-and-solutions.md`](create-ib-practice-and-solutions.md)
- Study-Guide companion contract: [`create-unit.md`](create-unit.md)
- Refresh (numbers change, skeleton locked): `feedback_practice_refresh` memory
- Per-file edit gate: [`review-changes.md`](review-changes.md)
- Tone / dash sweep: [`_tone.md`](_tone.md)
- HS conventions + program state: root `STATUS.md`, `project_hs_stem_program` memory
- Reference pattern build: HS Math Unit 1 pair (`HS-Math-1`); this sprint
  locks HS Physics Unit 1 (`HS-Phys-1`) as the STEM template.
</cross_references>
