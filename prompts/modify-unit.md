# Modify Existing Unit

You are editing an existing Dingrui Scholars HTML product.

## Inputs
- **File**: {{FILE_PATH}}
- **Change Request**: {{DESCRIPTION}}

## Instructions
1. Read the full target HTML file.
2. Read `rag/style-guide.md` for design consistency.
3. Make the requested changes while preserving:
   - Existing design tokens and CSS variables
   - Dark mode compatibility
   - Quiz functionality
   - KaTeX math rendering
   - Print styles
4. Run `bash scripts/validate.sh {{FILE_PATH}}` after changes.

## Before Submitting
- Verify no existing features were broken
- Confirm KaTeX delimiters are intact
- Test that changes render in both light and dark mode contexts
