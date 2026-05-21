# Review Changes (Before / After Diff)

<task>
Systematically review a change to one Dingrui Scholars HTML product
using paired screenshots and a code diff. Produce a structured
PASS/WARN/FAIL report so the user can decide in one read whether to
commit, request fixes, or revert.

This is the **inner loop** that pairs with the outer-loop sprint
workflow in [`improve-existing-product.md`](improve-existing-product.md).
One file. One change. One report.
</task>

<inputs>
- **File**: {{FILE_PATH}}
- **Change description**: {{DESCRIPTION}}   *what was edited and why*
</inputs>

<workflow>

### Step 1 — Capture before state
```bash
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/before.png --both
# optional mobile pass:
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/before_mobile.png --both --mobile
```
`--both` shoots light + dark. Run mobile pass when the edit touches
layout, typography, or any element that wraps.

### Step 2 — Apply the edit
Make the change per the inputs. Smallest possible diff. Do not bundle
unrelated cleanup — that breaks the diff signal in Step 6.

### Step 3 — Validate
```bash
bash scripts/validate.sh "{{FILE_PATH}}"
```
Exit 0 is a hard gate. If it fails, fix and re-run before screenshotting.

### Step 4 — Capture after state
```bash
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/after.png --both
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/after_mobile.png --both --mobile
```

### Step 5 — Compare against the six categories
View each pair side-by-side, run the checks below.

### Step 6 — Diff
```bash
git diff "{{FILE_PATH}}"
```
Only intended lines changed. No incidental whitespace, no removed
features, no shifted IDs that break anchors.

### Step 7 — Emit the report
Use the exact shape in `<output_format>` below.
</workflow>

<checklist>

**Layout**
- [ ] No unintended shifts / overflow
- [ ] Spacing consistent with surrounding sections
- [ ] Mobile (375px) — no horizontal scroll, no clipped equations

**Typography & color**
- [ ] DM Serif Display headings, Source Sans 3 body, JetBrains Mono code render correctly
- [ ] Colors trace back to `:root` design tokens — no new hardcoded hex
- [ ] Contrast adequate in both light and dark

**Math (KaTeX)**
- [ ] Every `$…$` and `$$…$$` rendered — no raw `$` visible
- [ ] Display math centered, inline math flows in line
- [ ] No overflow on long equations
- [ ] No unicode super/subscripts or Greek inside `\text{}`

**Interactive elements**
- [ ] Quiz `data-answer` indices correct, reveal/hide works
- [ ] `<details>` toggles open and close
- [ ] Flashcards have both front and back content
- [ ] Language toggle (if bilingual file): "中文" / "EN" round-trips,
      reloads keep the choice (`localStorage` key `drs.lang`)

**Dark mode**
- [ ] No element renders with a light-only hardcoded color
- [ ] Borders and shadows adapt
- [ ] Toggle persists across reload

**Code diff**
- [ ] Only intended lines changed
- [ ] No whitespace-only / line-ending noise
- [ ] No removed features
- [ ] Anchor IDs (`id="…"`) referenced by TOC still resolve
</checklist>

<output_format>

Report the result in this exact shape. Three labelled buckets, one
finding per line. Empty buckets get a single `(none)` line.

```
PASS:
- <one-line statement of what looks correct>
- <…>

WARN:
- <one-line non-blocking issue with file:line if applicable>
- <…>

FAIL:
- <one-line blocking issue with file:line>
- <…>

Recommendation: <commit | request-fix | revert>
```

**Bucket definitions** — do not bend these:

| Bucket | Means | Example |
|---|---|---|
| PASS | Verified working, no concern | `Dark mode parity intact — new card uses --bg-card / --text only` |
| WARN | Works, but a smell | `Worked-example numbering jumps 3→5 in §2 (file.html:412)` |
| FAIL | Breaks an invariant or a feature | `validate.sh exit 1 — unbalanced data-lang counts (en=42, zh=41)` |

The recommendation maps mechanically: any FAIL → `request-fix`; only
WARN or PASS → `commit`; structural damage (broken anchors, removed
toggle wiring) → `revert`.
</output_format>

<examples>

### Example — minimal report after a typo fix

```
PASS:
- Typo fixed in §2 quiz prompt 3 (recieve → receive)
- validate.sh exit 0
- Diff is one line, text-only, no layout impact

WARN:
- (none)

FAIL:
- (none)

Recommendation: commit
```

### Example — report after adding a worked example

```
PASS:
- New worked example matches §3 sibling structure (step numbering,
  KaTeX delimiters, dark-mode tokens)
- Light + dark screenshots show no regression in surrounding sections
- Bilingual parity: data-lang en/zh counts both increased by 1

WARN:
- Mobile screenshot shows the new $$\sin(g(x))$$ display equation
  rendering at the page edge with 2px right-side clearance — visually
  fine, but tight (Unit_4_Chain_Rule.html:387)

FAIL:
- (none)

Recommendation: commit
```

### Example — report that blocks the commit

```
PASS:
- Quiz answer index updated correctly
- Light-mode screenshot matches expectation

WARN:
- (none)

FAIL:
- validate.sh exit 1 — unbalanced data-lang counts (en=42, zh=41).
  Missing Chinese sibling for the new "Try Again" button label
  (Unit_A4_Complex_Numbers.html:1204)
- Dark-mode screenshot: new explanation card uses #FFF background
  instead of var(--bg-card), reads as a white blob on dark
  (Unit_A4_Complex_Numbers.html:1198)

Recommendation: request-fix
```
</examples>

<reminders>
Three things to re-check before emitting the report — these are the
most common false-PASS modes:

1. **Did you actually look at both light AND dark screenshots?**
   `--both` shoots both; opening only one defeats the purpose.
2. **Did `validate.sh` exit 0?** Re-state it in PASS. A missing
   validate line is suspicious.
3. **Did you read the full `git diff`, not just the section you
   edited?** Editor auto-format, encoding changes, and stray tabs
   show up only in the diff.
</reminders>
