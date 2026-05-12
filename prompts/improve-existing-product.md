# Improve Existing Product — Systematic Workflow

Outer-loop workflow for improving products that already exist. Pairs with
`review-changes.md` (inner loop, single-file edit review).

**Core idea:** every subject has an `AUDIT.md` that lists open work tiered
P0/P1/P2. The audit is the single source of truth. Two phases per cycle:

1. **Phase 0 — Improve `main`** (cross-cutting toolchain/infra). Land on
   `main` before opening subject sprints, because subject work depends on
   the toolchain working.
2. **Phase 1 — Branch off per subject sprint**. One active sprint per
   subject, scoped to items in that subject's `AUDIT.md`.

---

## Audit Framework

Every `<Subject>/AUDIT.md` follows a fixed shape (see `AP Physics/AUDIT.md`
as the canonical example):

| Section | Purpose |
|---|---|
| **Tier definitions** | P0 = exam-readiness blocker; P1 = polish; P2 = nice-to-have |
| **Active Sprint** | Table of currently in-flight items. **One active sprint per subject.** |
| **Closed sprints** | Resolved items strikethrough'd with `**Resolved:** <sha> — <note>`, kept for traceability. Whole closed sprints collapse to a single line + date. |
| **Cross-Unit Snapshot** | At-a-glance table of unit coverage (widgets / ISEE / flashcards / quiz / etc.) |
| **Known Infra / Tooling Items** | Promoted to **Phase 0** of this workflow. Don't sprint these alongside subject content. |
| **P2 — Future Work** | Subject-scoped but deferred. |
| **Digital Product Backlog** | Out-of-scope-for-study-guide ideas. Don't accidentally pull into a sprint. |

**IDs**: each audit item gets a stable ID:
- `S<sprint>-<item>` for sprint items (e.g. `S5-1`)
- `P<tier>-<n>` for individual punch-list items (e.g. `P1-2`, `P0-1`)
- `I-<n>` for infra items
- `DP-<n>` for Digital Product Backlog ideas

IDs are immutable. When an item moves between sprints (e.g. `S4-5` → `S5-1`),
strikethrough the old row with a pointer to the new ID — don't reuse the slot.

---

## Phase 0 — Improve `main` first

Before opening any subject sprint, do a pass on cross-cutting concerns.
This is short — minutes to hours, not days.

### 0.1 — Survey infra surface
```bash
git checkout main && git pull
bash scripts/validate.sh                 # any warnings/errors anywhere?
bash serve.sh                            # does the preview server even start?
python scripts/build-index.py            # idempotent? any diff?
```

### 0.2 — Roll up every subject's "Known Infra / Tooling Items"
```bash
grep -r "^### I-" --include=AUDIT.md
```
These are infra problems each subject's audit logged but hasn't fixed. They
belong in Phase 0, not subject sprints.

### 0.3 — Fix in small focused commits on `main`
Phase 0 commits are usually one-file or two-file fixes. Use a feature branch
only if a fix is non-trivial (>~50 lines or touches >2 files).

Naming pattern from recent history:
- `Toolchain: <one-line>` — for `scripts/`, `.gitattributes`, `serve.sh`
- `Pipeline: <one-line>` — for CI / GitHub Pages config
- `Structure: <one-line>` — for repo-wide reorg (e.g. `Study Guides/` normalization)
- `RAG: <one-line>` — for `rag/` spec changes

### 0.4 — Close out
- Each infra fix lands directly on `main` (after user review of the diff).
- Update the relevant `AUDIT.md`'s "Known Infra / Tooling Items" section to
  strikethrough the I-N entry with `**Resolved:** <sha>`.

### 0.5 — Phase 0 exit criteria
- `bash scripts/validate.sh` passes with no NEW warnings
- `bash serve.sh` lists every subject without crashing
- All open `I-N` entries are either resolved or deliberately deferred with a
  workaround documented

Only then move to Phase 1.

---

## Phase 1 — Branch off per subject sprint

### 1.1 — Read the AUDIT first
```bash
cat "<Subject>/AUDIT.md"
```
Identify:
- Which sprint is **Active**? (Look for the un-collapsed table near the top.)
- What's the tier mix of open items? (P0 first, then P1, then P2.)
- Any items that should actually be infra (promote to Phase 0 and stop here).

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

For each audit item in the sprint, follow `prompts/review-changes.md`:

1. **Capture before state** — `screenshot.sh <file> /tmp/before.png --both`
2. **Edit** — minimal diff, address the audit item only
3. **Validate** — `validate.sh <file>`
4. **Capture after state** — `screenshot.sh <file> /tmp/after.png --both`
5. **Compare** — diff before/after; check layout, math, dark mode
6. **Commit** — one logical commit per audit item, message format:

```
Sprint <N> <item-id>: <one-line summary>

<2–4 sentence body: what changed, why, and any subtle decisions.>

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

7. **Wait for user review** — never push or merge without explicit approval.

### 1.4 — Acceptance criteria per item
Pulled from the audit item itself. Common shapes:
- `grep -rn "<pattern>" "<Subject>/Study Guides/"` returns 0 hits
- Visual diff shows no regressions in non-affected examples
- Specific file:line references in the audit now satisfy the new convention

### 1.5 — Closing the sprint
When all items in the Active Sprint table are resolved, do a **close-out commit**:

```
Sprint <N> close-out: mark <items> resolved in AUDIT.md
```

This commit edits **only** the AUDIT.md:
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
# optionally: git branch -d sprint<N>_<short_topic>
```

For staging review before merging to `main` (CLAUDE.md deploy flow):
```bash
git checkout preview
git merge --ff-only sprint<N>_<short_topic>
git push origin preview
# review the rendered /preview/ URL, then fast-forward preview → main
```

---

## Decision rules

**Is this Phase 0 or Phase 1?**
- Touches `scripts/`, `serve.sh`, `.gitattributes`, `.github/`, `index.html`,
  `rag/`, or any toolchain → **Phase 0**, lands on `main`.
- Touches `<Subject>/Study Guides/*.html` or `<Subject>/Practice Questions/*.html`
  → **Phase 1**, lands on a sprint branch.
- Touches both → split into two commits; Phase 0 first.

**Is this item in scope for the current sprint?**
- ✅ Listed in the Active Sprint table → yes.
- ❌ Listed only in P2/Backlog → no, do not pull forward without user approval.
- ❌ Discovered mid-sprint as a new defect → log it under the appropriate
  tier in the audit, finish the current sprint first.

**Promote infra discovered mid-sprint?**
If a sprint-internal fix surfaces a tooling bug (like the `serve.sh` crash
during Sprint 5):
- Log it as a new `I-<n>` entry in the current subject's audit
- Document the workaround so the sprint can continue
- Defer the fix to the next Phase 0 pass — do **not** expand sprint scope
  unless the bug actively blocks the sprint

**When to add `data-theme` or refresh other shared specs?**
- Any change to repo-wide conventions (typography, hero schema, naming) goes
  through `GENERATION_PROMPT.md` or `rag/`. Lock the spec **before** rolling
  it out to multiple files (cf. Sprint 3 P1-2 hero schema lock).

---

## Inputs for a single run of this workflow

When invoking this template, fill in:

- **Subjects to improve** (in order): {{SUBJECTS}}
  *e.g. `AP Physics, IB Chemistry HL`*
- **Phase 0 scope** (open infra items to address first): {{INFRA_ITEMS}}
  *e.g. `I-2 in AP Physics/AUDIT.md (serve.sh crash)`*
- **Phase 1 sprints** (which active sprint per subject): {{SPRINTS}}
  *e.g. `AP Physics S5-1, IB Chemistry HL S1 (TBD — audit not yet scoped)`*

---

## End-of-workflow exit criteria

- Every Active Sprint table item has a resolved sha next to it, OR has been
  deliberately deferred with a one-line note in the audit.
- `bash scripts/validate.sh` passes for every touched file.
- No uncommitted changes outside `dist/` or other gitignored paths.
- Each subject's AUDIT.md "next sprint" pointer is up to date.
- Auto-memory's sprint-state files reflect the new checkpoint.
