# Dingrui Scholars — HTML Product Workspace

## What This Repo Is
Self-contained `.html` educational products (AP courses). Each file is a single-page app with KaTeX math, dark mode, quizzes, and print-friendly styling.

## Repo Structure
```
AP Calculus/          # Calculus unit HTML files
AP Physics/           # Physics unit HTML files
prompts/              # Claude prompt templates for SWE tasks
rag/                  # Reference docs, style guides, content specs
scripts/              # Tooling: visual diff, validation, screenshots
.claude/              # Claude Code settings
```

## Conventions
- **File naming**: `Unit_N_Topic_Name.html` (underscores, no spaces in new files)
- **Self-contained**: Each HTML has all CSS/JS inline. External deps: Google Fonts, KaTeX CDN only.
- **Design system**: Maroon accent `#7A2E2E`, DM Serif Display headings, Source Sans 3 body, JetBrains Mono code.
- **Required features**: Dark mode toggle, KaTeX math, interactive quizzes, print styles, mobile responsive.

## Workflow Commands
```bash
# Validate HTML files
bash scripts/validate.sh [file.html]

# Visual screenshot for comparison
bash scripts/screenshot.sh <file.html> [output.png]

# Create new unit from template
bash scripts/new-unit.sh "AP Subject" "Unit N Topic Name"
```

## When Modifying HTML Products
1. Read the target file fully before making changes
2. Check `rag/style-guide.md` for design tokens and patterns
3. Run `scripts/validate.sh` after changes
4. Use `scripts/screenshot.sh` before & after for visual diff
