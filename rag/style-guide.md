# Dingrui Scholars — Style Guide

## Design Tokens (CSS Variables)
```css
--bg: #F5F0EB;           /* Page background */
--bg-card: #FFFFFF;       /* Card/section background */
--text: #2C1B1F;          /* Primary text */
--text-secondary: #6B5058;/* Muted text */
--accent: #7A2E2E;        /* Maroon brand color */
--accent-light: #F2E4E4;  /* Accent tint */
--green: #2E6B4F;         /* Success/correct */
--orange: #A65E1A;        /* Warning/tip */
--red: #B03030;           /* Error/important */
--purple: #5E3D7A;        /* Highlight/proof */
--gold: #C4956A;          /* Decorative accent */
--border: #DDD0C8;
--radius: 12px;
--max-w: 860px;
```

## Typography
| Role       | Font                | Weight     |
|------------|---------------------|------------|
| Headings   | DM Serif Display    | 400, italic|
| Body       | Source Sans 3       | 300-700    |
| Code/Math  | JetBrains Mono      | 400-600    |

## External Dependencies
- Google Fonts: DM Serif Display, Source Sans 3, JetBrains Mono
- KaTeX 0.16.9 (CSS + JS + auto-render)

## Required Page Sections
1. **Header** — Subject, unit title, breadcrumb
2. **Table of Contents** — Sticky sidebar on desktop, collapsible on mobile
3. **Content Sections** — H2 per topic, H3 for subtopics
4. **Worked Examples** — Boxed, step-by-step with KaTeX
5. **Key Formulas** — Highlighted formula cards
6. **Quiz/Review** — Interactive show/hide answers
7. **Footer** — Dingrui Scholars branding

## Dark Mode
- Use `[data-theme="dark"]` selector to override all `--` variables
- Toggle button in header, persisted via `localStorage`

## Component Patterns

### Info Box
```html
<div class="box box--tip">
  <div class="box__title">Tip</div>
  <p>Content here</p>
</div>
```
Variants: `box--tip`, `box--warn`, `box--example`, `box--proof`

### Quiz Question
```html
<div class="quiz-q">
  <p class="quiz-q__prompt">Question text with $math$?</p>
  <div class="quiz-q__choices">
    <label><input type="radio" name="q1" value="a"> Option A</label>
    <!-- ... -->
  </div>
  <div class="quiz-q__answer" hidden>
    <p><strong>Answer:</strong> Explanation with $math$.</p>
  </div>
</div>
```

<!-- TODO: Add more component patterns as products evolve -->
