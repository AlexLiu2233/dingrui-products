# Modify Existing Unit

<task>
Apply a targeted edit to one existing Dingrui Scholars HTML product
file. The edit must not regress any of the file's existing
features — dark mode, KaTeX rendering, quiz interactivity, print
styles, mobile responsiveness — and must not introduce new design
tokens, new external dependencies, or new global JS.
</task>

<inputs>
- **File**: {{FILE_PATH}}             *e.g. `IB Math HL/Study Guides/Unit_A4_Complex_Numbers.html`*
- **Change request**: {{DESCRIPTION}}  *one to three sentences, scoped*
</inputs>

<workflow>
1. **Read the full file.** Not just the section you're about to touch —
   the rest of the file holds the conventions (CSS variable names, quiz
   markup shape, language-toggle data attributes) you must match.
2. **Cross-reference `rag/style-guide.md`** if the edit involves design
   tokens, colors, typography, or any new component.
3. **Edit.** Smallest possible diff. Preserve indentation and the
   surrounding markup style — if the file uses `data-lang="en"/"zh"`
   pairs, your edit ships both. If the file uses `[data-theme="dark"]`
   overrides, your edit ships the dark variant.
4. **Validate** — `bash scripts/validate.sh {{FILE_PATH}}` must pass.
5. **Visual check** — if the edit changes anything rendered, follow
   [`review-changes.md`](review-changes.md) for the before/after
   screenshot loop. Skip only for invisible edits (e.g. fixing a typo
   in a `<title>` tag).
</workflow>

<constraints>
- Do not introduce CSS variables that aren't already in `:root`.
- Do not add external dependencies (no new CDN, font, or library).
- Do not change `dingrui:version` or `dingrui:pair-key` comment tags
  unless the change request specifically authorizes a version bump.
- Do not rewrite sections that are out of scope, even if you spot
  bugs. Log them and ask — surprise refactors break review-then-merge.
- Do not strip or reshape JS-generated text (`toggleCheck`, language
  toggle, theme toggle); the wiring is load-bearing.
</constraints>

<examples>

### Example 1 — Typo fix in a quiz prompt (trivial)

**Change request:** "Quiz question 3 in §2 has `recieve` — fix the typo."

**Diff:**
```diff
-      <p class="quiz-q__prompt">Which expression will recieve the highest value?</p>
+      <p class="quiz-q__prompt">Which expression will receive the highest value?</p>
```

Validate. No screenshot needed (text-only, no layout impact).

### Example 2 — Add a worked example to §3 (medium)

**Change request:** "§3 (Chain Rule) only has one worked example. Add a
second example with a trig outer function."

**What to do:**
1. Locate the existing `<div class="worked-example">` in §3, mirror its
   structure exactly (same heading shape, same step-numbering pattern,
   same KaTeX delimiters: `$…$` inline, `$$…$$` display).
2. If the file is bilingual, ship both `<div data-lang="en">` and
   `<div data-lang="zh">` siblings. The Chinese block uses the
   `<code>english term</code>` gloss pattern at first mention.
3. Math in `$$…$$` only; no unicode super/subscripts inside `\text{}`.
4. Validate, then screenshot before/after in both light and dark mode.

### Example 3 — Out-of-scope creep (what NOT to do)

**Change request:** "Fix the broken anchor link in the TOC for §4."

**Wrong:** Fix the anchor, *and* refactor the TOC into a `<details>`
element because you noticed the markup is inconsistent.

**Right:** Fix the anchor. If the TOC inconsistency is worth raising,
log it as a P1/P2 entry in the subject's `AUDIT.md` and ask the user
before pulling it into scope.
</examples>

<acceptance>
Run through this checklist before reporting done:

- [ ] `bash scripts/validate.sh {{FILE_PATH}}` exits 0
- [ ] KaTeX delimiters intact (`$…$` inline, `$$…$$` display); no raw
      `$` visible in render
- [ ] Dark mode still toggles cleanly (use the page's existing toggle;
      no element renders with a light-only hardcoded color)
- [ ] Bilingual files: equal counts of `data-lang="en"` and
      `data-lang="zh"` after the edit
      (`grep -c 'data-lang="en"' {{FILE_PATH}}` ==
       `grep -c 'data-lang="zh"' {{FILE_PATH}}`)
- [ ] Mobile (375px) layout: no horizontal scroll, no clipped equation
- [ ] Diff contains only the lines the change request authorizes
</acceptance>

<reminders>
The four invariants this file must protect — restated at the tail
because they're the ones most often regressed by a quick edit:

1. **`validate.sh` is the gate.** If it fails, the edit is not done.
2. **Dark mode parity.** Every visible new element has a
   `[data-theme="dark"]` story.
3. **KaTeX delimiters.** Display math = `$$…$$`. Inline = `$…$`. Never
   mixed.
4. **Bilingual parity** (if the file has the language toggle): every
   new English string ships its Chinese sibling.
</reminders>
