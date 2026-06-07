# Dingrui Scholars — Style Guide

## Design Tokens (CSS Variables)
```css
/* Base is black & white to match dingruischolars.com; maroon = brand, blue = pop. */
--bg: #FAFAFA;            /* Page background (near-white) */
--bg-card: #FFFFFF;       /* Card/section background */
--text: #0F0F0F;          /* Primary text (near-black) */
--text-secondary: #585858;/* Muted text */
--accent: #7A2E2E;        /* Maroon (logo color): headings, labels, rules, brand chrome */
--accent-light: #F4E8E8;  /* Accent tint */
--pop: #0099FF;           /* Site link blue: inline links, the "pop" accent */
--pop-light: #E8F4FF;     /* Blue tint */
--ink: #0F0F0F;           /* Near-black CTA pill (matches site's primary button) */
--green: #2E6B4F;         /* Success/correct */
--orange: #A65E1A;        /* Warning/tip */
--red: #B03030;           /* Error/important */
--purple: #5E3D7A;        /* Highlight/proof */
--gold: #B07A2E;          /* Decorative accent */
--border: #E6E6E6;
--radius: 12px;
--max-w: 860px;
/* Dark mode ([data-theme="dark"]) is the neutral inverse: --bg #0F0F0F, --text #FAFAFA,
   --ink #FAFAFA (CTA pill inverts to near-white). CTA text uses var(--bg-card) so it
   stays legible in both themes. */
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
