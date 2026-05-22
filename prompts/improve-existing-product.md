# Improve Existing Product — Systematic Workflow

<task>
Outer-loop workflow for improving products that already exist. Pairs
with [`review-changes.md`](review-changes.md) (inner loop, per-file
edit review).

**Core idea:** every subject has an `AUDIT.md` that lists open work
tiered P0 / P1 / P2. The audit is the single source of truth. New
audit findings come from running
[`rag/study-guide-audit-checklist.md`](../rag/study-guide-audit-checklist.md)
against each shipped study guide; findings then land as sprint items
in the subject's `AUDIT.md`. Each cycle has two phases:

1. **Phase 0 — Improve `main`** (cross-cutting toolchain / infra).
   Lands on `main` before subject sprints open, because subject work
   depends on the toolchain working.
2. **Phase 1 — Branch off per subject sprint.** One active sprint per
   subject, scoped to items in that subject's `AUDIT.md`.
</task>

<decision_rules>

These three rules are the most consulted parts of this workflow.
Hoisted to the top so they're available at-a-glance; restated in
`<reminders>` at the tail.

### Is this Phase 0 or Phase 1?

- Touches `scripts/`, `serve.sh`, `.gitattributes`, `.github/`,
  `index.html`, `rag/`, or any toolchain → **Phase 0**, lands on `main`.
- Touches `<Subject>/Study Guides/*.html` or
  `<Subject>/Practice Questions/*.html` → **Phase 1**, lands on a
  sprint branch.
- Touches both → split into two commits; **Phase 0 first.**

### Is this item in scope for the current sprint?

- ✅ Listed in the Active Sprint table → yes.
- ❌ Listed only in P2 / Backlog → no, do not pull forward without user approval.
- ❌ Discovered mid-sprint as a new defect → log it under the
  appropriate tier in the audit, finish the current sprint first.

### Promote infra discovered mid-sprint?

If a sprint-internal fix surfaces a tooling bug (like the `serve.sh`
crash during Sprint 5):
- Log it as a new `I-<n>` entry in the current subject's audit
- Document the workaround so the sprint can continue
- Defer the fix to the next Phase 0 pass — **do not** expand sprint
  scope unless the bug actively blocks the sprint
</decision_rules>

<audit_framework>

Every `<Subject>/AUDIT.md` follows a fixed shape (see
`AP Physics/AUDIT.md` as the canonical example):

| Section | Purpose |
|---|---|
| **Tier definitions** | P0 = exam-readiness blocker; P1 = polish; P2 = nice-to-have |
| **Active Sprint** | Table of currently in-flight items. **One active sprint per subject.** |
| **Closed sprints** | Resolved items strikethrough'd with `**Resolved:** <sha> — <note>`, kept for traceability. Whole closed sprints collapse to a single line + date. |
| **Cross-Unit Snapshot** | At-a-glance table of unit coverage (widgets / ISEE / flashcards / quiz / etc.) |
| **Known Infra / Tooling Items** | Promoted to **Phase 0**. Don't sprint these alongside subject content. |
| **P2 — Future Work** | Subject-scoped but deferred. |
| **Digital Product Backlog** | Out-of-scope-for-study-guide ideas. **Don't accidentally pull into a sprint.** |

### Stable IDs

Each audit item gets an immutable ID:

- `S<sprint>-<item>` for sprint items, e.g. `S5-1`
- `P<tier>-<n>` for individual punch-list items, e.g. `P1-2`, `P0-1`
- `I-<n>` for infra items
- `DP-<n>` for Digital Product Backlog ideas

When an item moves between sprints (e.g. `S4-5` → `S5-1`),
**strikethrough the old row with a pointer to the new ID** — don't
reuse the slot.
</audit_framework>

<phase_0>

## Phase 0 — Improve `main` first

Before opening any subject sprint, run a cross-cutting pass. Short —
minutes to hours, not days.

### 0.1 — Survey infra surface
```bash
git checkout main && git pull
bash scripts/validate.sh                 # any warnings/errors anywhere?
bash serve.sh                            # does the preview server start?
python scripts/build-index.py            # idempotent? any diff?
```

### 0.2 — Roll up every subject's "Known Infra / Tooling Items"
```bash
grep -r "^### I-" --include=AUDIT.md
```
These are infra problems each subject's audit logged but hasn't fixed.
They belong in Phase 0, not subject sprints.

### 0.3 — Fix in small focused commits on `main`
Phase 0 commits are usually one-file or two-file fixes. Use a feature
branch only if a fix is non-trivial (>~50 lines or touches >2 files).

**Commit naming patterns from recent history:**

| Prefix | For |
|---|---|
| `Toolchain: <one-line>` | `scripts/`, `.gitattributes`, `serve.sh` |
| `Pipeline: <one-line>` | CI / GitHub Pages config |
| `Structure: <one-line>` | Repo-wide reorg (e.g. `Study Guides/` normalization) |
| `RAG: <one-line>` | `rag/` spec changes |

### 0.4 — Close out
- Each infra fix lands directly on `main` (after user review of the diff).
- Update the relevant `AUDIT.md`'s "Known Infra / Tooling Items"
  section: strikethrough the `I-<n>` entry with `**Resolved:** <sha>`.

### 0.5 — Phase 0 exit criteria
- `bash scripts/validate.sh` passes with no NEW warnings
- `bash serve.sh` lists every subject without crashing
- All open `I-<n>` entries are either resolved or deliberately
  deferred with a documented workaround

Only then move to Phase 1.
</phase_0>

<phase_1>

## Phase 1 — Branch off per subject sprint

### 1.1 — Read the AUDIT first
```bash
cat "<Subject>/AUDIT.md"
```
Identify:
- Which sprint is **Active**? (Un-collapsed table near the top.)
- Tier mix of open items? (P0 first, then P1, then P2.)
- Any items that should actually be infra? (Promote to Phase 0 and stop here.)

### 1.2 — Branch
```bash
git checkout main && git pull
git checkout -b sprint<N>_<short_topic>
```
Naming examples from history:
- `sprint2_content_gaps`
- `sprint3_p1_polish`
- `sprint4_phase2_units`
- `sprint5_pdf_render`

### 1.3 — Per-item cycle (inner loop)

For each audit item in the sprint, follow [`review-changes.md`](review-changes.md):

1. **Capture before state** — `screenshot.sh <file> /tmp/before.png --both`
2. **Edit — English only** — minimal diff, address the audit item only.
   Even if the file is bilingual, the English revision lands first; do
   not touch the Chinese side in this commit.
3. **Validate** — `validate.sh <file>`
4. **Capture after state** — `screenshot.sh <file> /tmp/after.png --both`
5. **Compare** — diff before/after; check layout, math, dark mode
6. **Commit** — one logical commit per audit item, format:
   ```
   Sprint <N> <item-id>: <one-line summary>

   <2–4 sentence body: what changed, why, subtle decisions.>

   Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
   ```
7. **Wait for user review** — **never push or merge without explicit approval.**
8. **Bilingual follow-up (gated, locked 2026-05-21).** Once the user
   confirms the English revision for the file, add the Mandarin
   teaching translation in a **separate follow-up commit** per the
   locked playbook in
   [`create-bilingual-translation.md`](create-bilingual-translation.md).
   The follow-up commit also picks up any Section D findings (gloss
   gaps, terminology drift) from the same audit. Do NOT bundle the
   English revision and the bilingual update in one commit.

### 1.4 — Acceptance criteria per item
Pulled from the audit item itself. Common shapes:
- `grep -rn "<pattern>" "<Subject>/Study Guides/"` returns 0 hits
- Visual diff shows no regressions in non-affected examples
- Specific file:line references in the audit now satisfy the new convention

### 1.5 — Closing the sprint
When every item in the Active Sprint table is resolved, do a
**close-out commit**:

```
Sprint <N> close-out: mark <items> resolved in AUDIT.md
```

This commit edits **only** the `AUDIT.md`:
- Strikethrough each resolved item: `~~**S<N>-<i>**~~ ✅ closed — <sha>`
- Append `**Resolved:** <sha> — <one-line note>` to detailed sections
- Collapse the whole sprint to a single line if every item closed:
  `**Sprint N closed YYYY-MM-DD** — all items landed on <branch>.`
- Promote the next sprint up from the backlog into the Active Sprint table

### 1.6 — Merge
After user approval of the full sprint:
```bash
git checkout main
git merge --ff-only sprint<N>_<short_topic>
# optionally:
git branch -d sprint<N>_<short_topic>
```

For staging review before merging to `main` (per CLAUDE.md deploy flow):
```bash
git checkout preview
git merge --ff-only sprint<N>_<short_topic>
git push origin preview
# review the rendered /preview/ URL, then fast-forward preview → main
```
</phase_1>

<inputs>

When invoking this workflow, fill in:

- **Subjects to improve** (in order): `{{SUBJECTS}}`
  *e.g. `AP Physics, IB Chemistry HL`*
- **Phase 0 scope** (open infra items to address first): `{{INFRA_ITEMS}}`
  *e.g. `I-2 in AP Physics/AUDIT.md (serve.sh crash)`*
- **Phase 1 sprints** (which active sprint per subject): `{{SPRINTS}}`
  *e.g. `AP Physics S5-1, IB Chemistry HL S1 (TBD — audit not yet scoped)`*
</inputs>

<examples>

### Example — Phase 0 then Phase 1, one cycle

> User: "Time for the next round on AP Physics."

**Step 1 — Phase 0 sweep.** Check `AP Physics/AUDIT.md` for any
`I-<n>` entries. Discover `I-2`: `serve.sh` crashes on subjects with
spaces in the folder name. Workaround documented in audit.

**Step 2 — Decision rule check.** Touches `serve.sh` → **Phase 0**.
Lands on `main`.

**Step 3 — Fix on `main`:**
```
Toolchain: serve.sh — quote folder names so spaces don't break the discover loop
```
User reviews the diff, approves, lands.

**Step 4 — Update audit:**
```diff
- ### I-2 — serve.sh crashes on subjects with spaces in folder name
+ ### ~~I-2~~ — **Resolved:** 8a3f912 — serve.sh quotes folder names
```

**Step 5 — Open Phase 1.** Read `AP Physics/AUDIT.md`, find Active
Sprint `S6 — Worked-example polish`. Branch:
```bash
git checkout -b sprint6_worked_example_polish
```

**Step 6 — Per-item cycle.** Each `S6-N` item follows
`review-changes.md`. One commit per item. Wait for user review on each.

### Example — out-of-scope creep (what NOT to do)

While fixing `S5-3` (a TOC link bug in Unit 4), you notice Unit 5 has
the same bug.

**Wrong:** Fix both, commit them together.

**Right:** Fix only `S5-3` (the item in scope). Log Unit 5's bug as a
new `S5-4` or `P1-N` in the audit. Mention it during user review. The
user decides whether to pull it into the current sprint or defer.
</examples>

<exit_criteria>

End-of-workflow checklist:

- [ ] Every Active Sprint table item has a resolved sha next to it,
      OR has been deliberately deferred with a one-line audit note
- [ ] `bash scripts/validate.sh` passes for every touched file
- [ ] No uncommitted changes outside `dist/` or other gitignored paths
- [ ] Each subject's `AUDIT.md` "next sprint" pointer is up to date
- [ ] Auto-memory's sprint-state files reflect the new checkpoint
</exit_criteria>

<reminders>
The four rules most often violated mid-sprint — restated at the tail:

1. **Phase 0 before Phase 1.** Toolchain fixes land on `main` first.
   A subject sprint that depends on broken tooling will block.
2. **One active sprint per subject.** Don't open `S6` while `S5` has
   open items. Close it out first.
3. **Out-of-scope discoveries log, not fix.** Sprint scope = the
   Active Sprint table. Surprises go in the audit, not the diff.
4. **User reviews every commit before merge.** No exceptions, no
   batch-merge. The cadence is locked.
</reminders>
