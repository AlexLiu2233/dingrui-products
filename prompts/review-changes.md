# Review Changes (Before/After Diff)

Systematic review of HTML product changes using visual screenshots and code diff.

## Inputs
- **File**: {{FILE_PATH}}
- **Change Description**: {{DESCRIPTION}}

## Workflow

### Step 1 — Capture Before State
```bash
# Light + dark screenshots before changes
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/before.png --both
# Optional: mobile view
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/before_mobile.png --both --mobile
```

### Step 2 — Make Changes
Apply the requested modifications to the file.

### Step 3 — Validate
```bash
bash scripts/validate.sh "{{FILE_PATH}}"
```

### Step 4 — Capture After State
```bash
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/after.png --both
bash scripts/screenshot.sh "{{FILE_PATH}}" /tmp/after_mobile.png --both --mobile
```

### Step 5 — Compare & Report

View each screenshot pair and check for:

**Layout**
- [ ] No unintended layout shifts or overflow
- [ ] Spacing/margins consistent with surrounding sections
- [ ] Mobile layout still works (no horizontal scroll)

**Typography & Colors**
- [ ] Fonts render correctly (DM Serif Display headings, Source Sans 3 body)
- [ ] Colors match design tokens (no hardcoded hex outside the system)
- [ ] Text contrast adequate in both light and dark mode

**Math Rendering**
- [ ] All KaTeX expressions render (no raw `$...$` visible)
- [ ] Display math centered, inline math flows with text
- [ ] No overflow on complex equations

**Interactive Elements**
- [ ] Quiz data-answer indices are correct
- [ ] Worked examples expand/collapse properly
- [ ] Flashcards have front and back content

**Dark Mode**
- [ ] Compare light vs dark screenshots
- [ ] No elements with hardcoded light-only colors
- [ ] Borders and shadows adapt properly

**Code Diff**
```bash
git diff "{{FILE_PATH}}"
```
- [ ] Only intended lines changed
- [ ] No accidental whitespace or formatting changes
- [ ] No removed features or broken structure

### Step 6 — Summary
Report findings as:
```
PASS: [what looks good]
WARN: [minor issues, non-blocking]
FAIL: [must fix before committing]
```
