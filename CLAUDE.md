# Dingrui Scholars — HTML Product Workspace

## What This Repo Is
Self-contained `.html` educational products (AP courses). Each file is a single-page app with KaTeX math, dark mode, quizzes, and print-friendly styling.

## Repo Structure
```
AP Calculus/          # Calculus unit HTML files
AP Physics/           # Physics unit HTML files
AP CSA/               # Computer Science A unit HTML files
IB Chemistry HL/      # IB Chemistry HL unit HTML files
IB Math HL/           # IB Math AA HL unit HTML files
prompts/              # Claude prompt templates for SWE tasks
rag/                  # Reference docs, style guides, content specs
scripts/              # Tooling: visual diff, validation, screenshots
.github/workflows/    # CI: GitHub Pages deploy (main → /, preview → /preview/)
.claude/              # Claude Code settings
```

## Deploy Workflow

**Production** is served from `main` at the site root.
**Staging** is served from the `preview` branch at `/preview/`.

Both URLs live on the same GitHub Pages site:
```
https://<user>.github.io/dingrui-products/          # main
https://<user>.github.io/dingrui-products/preview/  # preview branch
```

Cadence:
1. Do work on a feature branch (e.g. `ib_math_hl_units`).
2. PR feature branch → `preview`. CI redeploys `/preview/`. Review the rendered staging URL.
3. After user approval, fast-forward `preview` → `main`. CI redeploys the site root.

CI lives in `.github/workflows/deploy.yml`. It checks out both branches, runs
`scripts/validate.sh` (strict for prod, warn-only for preview), strips internal
files (`AUDIT.md`, `prompts/`, `rag/`, `scripts/`, `CLAUDE.md`, `.claude/`,
`GENERATION_PROMPT.md`, `README.md`) from the published tree, and deploys via
`actions/deploy-pages@v4`.

**One-time GitHub setting:** repo Settings → Pages → Source must be set to
**GitHub Actions** (not "Deploy from a branch").

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

# Create new unit from template (Prefix:Topic form lets build-index parse it)
bash scripts/new-unit.sh "AP Physics" "Unit 8: Magnetic Fields"

# Regenerate index.html cards + hero chips from filesystem
python scripts/build-index.py

# Local preview server (discovers all subjects' Study Guides + Practice Questions)
bash serve.sh [port]
```

## Adding a New Unit

Each Study Guide HTML's `<title>` tag is the source of truth for card text:

```html
<title>{Subject Long} — {Prefix}: {Topic} | Dingrui Scholars</title>
```

Examples:
- `AP Physics C: Mechanics — Unit 1: Kinematics | Dingrui Scholars`
- `IB Chemistry — Structure 1: Models of the Particulate Nature of Matter | Dingrui Scholars`
- `IB Math AA HL — Unit A1: Sequences & Series | Dingrui Scholars`

To add a new unit:
1. Drop the HTML into `<Subject>/Study Guides/` with a conformant `<title>` tag.
2. Run `python scripts/build-index.py` — index.html cards and hero chip
   counts regenerate automatically. The script is idempotent.

## When Modifying HTML Products
1. Read the target file fully before making changes
2. Check `rag/style-guide.md` for design tokens and patterns
3. Run `scripts/validate.sh` after changes
4. Use `scripts/screenshot.sh` before & after for visual diff
