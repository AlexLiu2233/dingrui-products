# Create New Unit

You are creating a new Dingrui Scholars HTML product unit.

## Inputs
- **Subject**: {{SUBJECT}}
- **Unit Number**: {{UNIT_NUMBER}}
- **Unit Title**: {{UNIT_TITLE}}
- **Topics**: {{TOPICS_LIST}}

## Instructions
1. Read `rag/style-guide.md` for design tokens, layout patterns, and required sections.
2. Read `rag/template.html` for the base HTML structure.
3. Read an existing unit in the same subject folder for tone and depth reference.
4. Generate the full self-contained HTML file with:
   - All sections from the topic list
   - Worked examples with KaTeX math per section
   - 2-3 quiz questions per major section
   - Proper dark mode support
   - Print-friendly layout
5. Save to `{{SUBJECT}}/Unit_{{UNIT_NUMBER}}_{{UNIT_TITLE_SNAKE}}.html`
6. Run `bash scripts/validate.sh` on the output.

## Quality Checks
- All KaTeX delimiters properly escaped
- Quiz answers are hidden until revealed
- Mobile responsive at 375px+
- Dark mode toggling works
- No broken internal links
