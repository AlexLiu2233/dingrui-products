# Dingrui Scholars - AP Physics C Study Guide Generation Prompt

> **Purpose**: Master specification for generating interactive, single-file HTML study guides from RAG-supplied AP course content. Use this document as the system prompt when generating new units or editing existing ones.

---

## 1. Product Overview

**Brand**: Dingrui Scholars (鼎睿学苑)
**Current Course**: AP Physics C: Mechanics (7 units)
**Format**: Self-contained `.html` files — all CSS and JavaScript inline; no build step
**Audience**: AP students preparing for the College Board exam
**Tone**: Premium academic — authoritative yet approachable, exam-focused

---

## 2. File Naming Convention

```
Unit_{N}_{Title_With_Underscores}.html
```

Examples:
- `Unit_1_Kinematics.html`
- `Unit_5_Torque_and_Rotational_Dynamics.html`

---

## 3. External Dependencies (CDN)

Every unit **must** load these in `<head>`:

```html
<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500;600&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">

<!-- KaTeX (math rendering) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
```

**Optional** (include when unit needs interactive math plots):
```html
<!-- JSXGraph (interactive graphing) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/jsxgraph@1.8.0/distrib/jsxgraph.css">
<script src="https://cdn.jsdelivr.net/npm/jsxgraph@1.8.0/distrib/jsxgraphcore.js"></script>
```

---

## 4. Head Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AP Physics C: Mechanics — Unit {N}: {Title} | Dingrui Scholars</title>
<meta name="description" content="AP Physics C: Mechanics — Unit {N}: {Title} | Dingrui Scholars. Polished AP Physics C notes from Dingrui Scholars with worked examples, interactive review, quizzes, dark mode, and print-friendly formatting.">
<meta name="theme-color" content="#7A2E2E">
<meta name="color-scheme" content="light dark">
{CDN links from Section 3}
<style>
{Inline CSS — see Section 5}
</style>
</head>
```

---

## 5. Design System — CSS Variables (Canonical)

All units **must** use this exact token set. Do not deviate.

```css
:root {
  --bg: #F5F0EB;
  --bg-card: #FFFFFF;
  --bg-code: #1E1418;
  --text: #2C1B1F;
  --text-secondary: #6B5058;
  --accent: #7A2E2E;
  --accent-light: #F2E4E4;
  --accent-dark: #5A1E1E;
  --green: #2E6B4F;
  --green-light: #DFF0E8;
  --orange: #A65E1A;
  --orange-light: #FBF0E0;
  --red: #B03030;
  --red-light: #FCEAEA;
  --purple: #5E3D7A;
  --purple-light: #EDE4F5;
  --gold: #C4956A;
  --gold-light: #FDF5EC;
  --border: #DDD0C8;
  --shadow: 0 4px 6px -1px rgba(60,20,30,0.06), 0 2px 4px -1px rgba(60,20,30,0.04);
  --shadow-lg: 0 10px 15px -3px rgba(60,20,30,0.10);
  --radius: 12px;
  --font-display: 'DM Serif Display', Georgia, serif;
  --font-body: 'Source Sans 3', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --max-w: 860px;
  --toc-w: 260px;
}
[data-theme="dark"] {
  --bg: #151010;
  --bg-card: #1E1618;
  --bg-code: #0D0A0B;
  --text: #E8E0DC;
  --text-secondary: #A89098;
  --accent: #C87070;
  --accent-light: #3A1818;
  --accent-dark: #E08080;
  --green: #5CB88A;
  --green-light: #1A2E24;
  --orange: #D4944A;
  --orange-light: #2E2010;
  --red: #E07070;
  --red-light: #301515;
  --purple: #A888C8;
  --purple-light: #201828;
  --gold: #D4A870;
  --gold-light: #2A2018;
  --border: #352828;
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.4);
}
```

### Important rules
- `--shadow` and `--shadow-lg` are **full** `box-shadow` values. Use `box-shadow: var(--shadow);` directly — never prepend offsets.
- Color semantic roles: `--accent` (maroon) = primary, `--green` = correct/positive, `--red` = incorrect/warning, `--orange` = caution/highlight, `--purple` = special/advanced, `--gold` = meta/info.
- Hover backgrounds: use `var(--accent-light)`.

---

## 6. Page Structure (top to bottom)

Every unit follows this exact region order:

### 6.1 Skip Link (accessibility)
```html
<a class="skip-link" href="#main-content">Skip to content</a>
```

### 6.2 Top Navigation (`.top-nav`)
Fixed header at `height: 56px`, `z-index: 100`, glass-blur background.
Contains:
- **Left**: TOC toggle button (`#tocToggle`), brand logo (`.nav-logo`), unit badge (`.nav-badge`)
- **Right**: Theme toggle button (`#themeToggle`)

### 6.3 Progress Bar (`.progress-track` / `.progress-fill`)
Fixed at `top: 56px`, `height: 3px`, scroll-linked via JS. ID: `#progressFill`.

### 6.4 Sidebar TOC (`#sidebar`)
- Fixed left panel, `width: var(--toc-w)`, hidden by default, toggled with `.open` class
- Contains section links with `href="#sN-X"` and review section links
- Active link highlighted via IntersectionObserver in JS

### 6.5 Main Content Wrapper
```html
<main class="main-wrap" id="main-content">
```
Margin-left offset by `var(--toc-w)`, responsive collapse on mobile.

### 6.6 Hero Section (`#hero`)

**Locked schema (Sprint 3, 2026-05-09).** All 7 Mechanics units conform.
Order is fixed: Exam Weight → Class Periods → Topics. Numbers are bare —
no `<strong>` wrappers (the `.chip` font weight is already 600).

```html
<section class="hero" id="hero">
  <div class="hero-overline">AP Physics C: Mechanics</div>
  <h1>Unit {N}: {Title}</h1>
  <p>{1-2 sentence unit overview}</p>
  <div class="hero-meta">
    <span class="chip chip-maroon">{X-Y}% Exam Weight</span>
    <span class="chip chip-green">~{X-Y} Class Periods</span>
    <span class="chip chip-gold">{N} Topics</span>
  </div>
</section>
```

### 6.7 Core Topic Sections
Each section:
```html
<section class="section" id="s{N}-{X}">
  <div class="section-label">Section {N}.{X}</div>
  <h2>{Topic Title}</h2>
  {Content: paragraphs, concept-boxes, formula-boxes, worked examples, tables, details}
</section>
```

Section IDs follow the pattern `s{unit}-{topic}` (e.g., `s5-3` for Unit 5 Topic 3).

### 6.8 Interactive Widgets
Canvas-based explorations with sliders:
```html
<div class="formula-explorer" id="{name}-widget">
  <div class="explorer-title">{Widget Title}</div>
  <div class="explorer-subtitle">{Brief description}</div>
  <div class="explorer-sliders">
    <div class="slider-group">
      <label>{Param}: <span class="val" id="{id}_val">{default}</span></label>
      <input type="range" id="{id}" min="..." max="..." value="..." step="...">
    </div>
    ...
  </div>
  <canvas id="{name}Canvas" width="920" height="440"></canvas>
  <div class="explorer-results">
    <div class="result-card">
      <div class="result-label">{Label}</div>
      <div class="result-value" id="{id}_result">—</div>
      <div class="result-unit">{unit}</div>
    </div>
    ...
  </div>
</div>
```

Widget ID pattern: `{shortname}-widget` (e.g., `shm-widget`, `torque-widget`)
Canvas ID pattern: `{shortname}Canvas` (e.g., `shmCanvas`, `torqueCanvas`)

### 6.9 Review Sections

**Exam Strategy** (`#exam-strategy`):
- MC tips card (`.card` with `.card-icon.icon-accent`)
- FR tips card (`.card` with `.card-icon.icon-green`)
- Common mistakes in a `.concept-box.red`

**Flashcards** (`#flashcards`):
- 6-10 cards in `.flashcard-grid`
- Each card: `.flashcard` > `.flashcard-inner` > `.flashcard-front` + `.flashcard-back`
- Flip on click: `onclick="this.classList.toggle('flipped')"`
- Front: question in accent color; Back: answer on accent background

**Unit Quiz** (`#unit-quiz`):
- 4-8 multiple-choice questions
- Each: `.quiz[data-answer="{correct_index}"]` > `.quiz-q` + `.quiz-options` > `.quiz-opt[data-idx]`
- Include `.quiz-explain.correct-exp` and `.quiz-explain.wrong-exp`
- Include 2-3 ISEE worked examples (see Section 7)

### 6.10 Footer
```html
<div style="text-align: center; padding: 40px 0; color: var(--text-secondary); font-size: 0.85rem;">
  <p style="font-family: var(--font-display); font-size: 1.1rem; margin-bottom: 4px;">鼎睿学苑 · Dingrui Scholars</p>
  <p>AP Physics C: Mechanics — Unit {N} {Title} · {Year} Edition</p>
</div>
</main>
```

### 6.11 Back-to-Top Button
```html
<button class="backtotop" id="backToTop" aria-label="Back to top">↑</button>
```
Visibility toggled via JS when `scrollY > 400`.

---

## 7. ISEE Worked Examples (FRQ Style)

Embed inside `<details class="isee-example">` blocks. Structure:

```html
<details class="isee-example">
  <summary>Worked Example — {Title} (FRQ Style)</summary>
  <div class="isee-body">
    <p class="worked-problem">{Problem statement with KaTeX math}</p>

    <div class="isee-identify">
      <div class="isee-tag">Identify</div>
      <p><strong>Principle:</strong> {Physics principle}</p>
      <p><strong>Constraint:</strong> {Key constraints}</p>
      <div class="isee-given">
        <span>{Given 1}</span><span>{Given 2}</span>...
      </div>
      <p><strong>Find:</strong> {Target quantities}</p>
    </div>

    <div class="isee-setup">
      <div class="isee-tag">Set Up</div>
      {Coordinate system, diagram description, equation setup}
    </div>

    <div class="isee-execute">
      <div class="isee-tag">Execute</div>
      <div class="worked-steps">
        <div class="worked-step">
          <div class="step-label">{Step Name}</div>
          <div class="step-math">$${algebra}$$</div>
          <div class="step-text">{Explanation}</div>
        </div>
        ...
      </div>
    </div>

    <div class="isee-evaluate">
      <div class="isee-tag">Evaluate</div>
      <div class="isee-check">{Limiting case check} ✓</div>
      <div class="isee-check">{Units check} ✓</div>
      <div class="isee-check">{Reasonableness check} ✓</div>
    </div>
  </div>
</details>
```

### ISEE Principles
- **Identify**: State the physics principle, list knowns, define the target.
- **Set Up**: Choose coordinates, draw (describe) the free-body diagram, write governing equations.
- **Execute**: Algebraic manipulation with every step shown. Use `\boxed{}` for the final answer.
- **Evaluate**: Check limiting cases, verify units, sanity-check magnitudes.

---

## 8. Content Components Reference

### Concept Box
```html
<div class="concept-box {variant}">
  <strong>{LABEL}</strong>
  {Content with KaTeX}
</div>
```
Variants: (none) = maroon, `green`, `orange`, `red`, `purple`, `gold`

### Formula Box
```html
<div class="formula-box">
  <div class="formula-label">{FORMULA NAME}</div>
  $${LaTeX}$$
</div>
```

### Expandable Details
```html
<details>
  <summary>{Click to expand title}</summary>
  <div class="detail-body">{Content}</div>
</details>
```

### Table
```html
<div class="table-wrap">
  <table>
    <tr><th>{Header 1}</th><th>{Header 2}</th></tr>
    <tr><td>{Data}</td><td>{Data}</td></tr>
  </table>
</div>
```

### Card
```html
<div class="card">
  <div class="card-header">
    <div class="card-icon {icon-variant}">{Short Label}</div>
    <div class="card-title">{Title}</div>
  </div>
  {Content}
</div>
```

---

## 9. JavaScript Architecture

All JS is inline in a single `<script>` block after `</main>`. Required modules:

### 9.1 Theme Toggle
```javascript
function toggleTheme() {
  var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  document.documentElement.setAttribute('data-theme', isDark ? '' : 'dark');
  document.getElementById('themeToggle').textContent = isDark ? 'Dark' : 'Light';
  // Redraw all canvases here
}
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.setAttribute('data-theme', 'dark');
  document.getElementById('themeToggle').textContent = 'Light';
}
```

### 9.2 Sidebar Toggle
```javascript
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('open');
  const btn = document.getElementById('tocToggle');
  if (btn) btn.classList.toggle('active', sidebar.classList.contains('open'));
}
// Click-outside-to-close and Escape key handlers
```

### 9.3 Progress Bar
```javascript
window.addEventListener('scroll', function() {
  var h = document.documentElement.scrollHeight - window.innerHeight;
  document.getElementById('progressFill').style.width =
    (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
});
```

### 9.4 Active TOC Highlighting
Uses `IntersectionObserver` with `rootMargin: '-80px 0px -60% 0px'` to highlight the current section link in the sidebar.

### 9.5 Quiz Logic
Iterates `.quiz` elements, reads `data-answer`, handles click to show correct/wrong styling and explanation.

### 9.6 Flashcard Flip
Handled inline via `onclick="this.classList.toggle('flipped')"` on each `.flashcard`.

### 9.7 Canvas Helpers
```javascript
function isDark() { return document.documentElement.getAttribute('data-theme') === 'dark'; }
function getColors() {
  var d = isDark();
  return {
    bg: d ? '#1E1618' : '#FFFFFF',
    grid: d ? '#2A2022' : '#EDE6E0',
    axis: d ? '#A89098' : '#6B5058',
    curve: d ? '#C87070' : '#7A2E2E',
    fill: d ? 'rgba(200,112,128,0.15)' : 'rgba(107,45,62,0.1)',
    green: d ? '#5CB88A' : '#2E6B4F',
    orange: d ? '#D4A870' : '#A65E1A',
    red: d ? '#E07070' : '#B03030',
    purple: d ? '#A888C8' : '#5E3D7A',
    text: d ? '#A89098' : '#6B5058',
    marker: d ? '#D4A870' : '#A65E1A',
  };
}
function setupCanvas(canvas, W, H) {
  var dpr = window.devicePixelRatio || 1;
  canvas.width = W * dpr; canvas.height = H * dpr;
  canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
  var ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return ctx;
}
```

### 9.8 Back-to-Top
```javascript
var backBtn = document.getElementById('backToTop');
if (backBtn) {
  window.addEventListener('scroll', function() {
    backBtn.classList.toggle('show', window.scrollY > 400);
  });
  backBtn.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
```

---

## 10. Accessibility & Responsive Requirements

- **Skip link**: First element in `<body>`
- **Focus outlines**: `button:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }`
- **Reduced motion**: `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }`
- **Print styles**: Hide nav, sidebar, widgets; force black-on-white; page-break-avoid on cards and details
- **Mobile** (`max-width: 600px`): Stack slider grids to single column, collapse sidebar, reduce hero font size
- **Selection**: `::selection { background: var(--accent-light); color: var(--accent-dark); }`

---

## 11. Preserved IDs (Do Not Rename)

These IDs are wired to JavaScript and must be preserved across all units:

### Global (every unit)
```
tocToggle, themeToggle, progressFill, sidebar, main-content, hero,
exam-strategy, flashcards, unit-quiz, backToTop
```

### Per-Unit Section IDs
Pattern: `s{N}-{X}` where N = unit number, X = section number within unit.

### Per-Unit Widget/Canvas IDs
Each unit defines its own widget and canvas IDs. These are documented in the existing HTML files. When creating a new unit, follow the naming pattern: `{shortname}-widget` and `{shortname}Canvas`.

---

## 12. Generation Workflow (for LLMs)

### Input Required
You will receive **RAG-extracted course content** containing:
1. Unit number and title
2. Topic list with descriptions (from College Board CED or equivalent)
3. Key formulas and equations
4. Common misconceptions
5. Exam format guidance (MC/FRQ patterns)

### Steps to Generate a New Unit

1. **Create the `<head>`** using the template from Section 4. Determine if JSXGraph is needed (interactive plots beyond simple canvas).

2. **Write all CSS** starting with the canonical variables (Section 5), then the full component styles. Copy the CSS structure from an existing unit file (e.g., Unit 5 or Unit 6) as a base.

3. **Build the HTML body** in the order specified in Section 6:
   - Skip link
   - Top nav with unit-specific badge text
   - Progress bar
   - Sidebar with all section + review links
   - Hero with correct chip counts
   - Core topic sections (one per CED topic)
   - Interactive widgets (at least 2 per unit)
   - Review sections: Exam Strategy, Flashcards (8+), Quiz (6+)
   - Footer with unit info
   - Back-to-top button

4. **Write the `<script>` block** with all required JS modules (Section 9) plus unit-specific widget logic.

5. **Include 2-3 ISEE worked examples** in the quiz section, based on realistic AP FRQ scenarios.

### Content Quality Standards
- All physics must be **correct** and at the AP Physics C: Mechanics level (calculus-based).
- Use `$...$` for inline math and `$$...$$` for display math (KaTeX syntax).
- Every formula box should contain a key equation that students must memorize.
- Concept boxes should highlight definitions, theorems, and key distinctions.
- Flashcard questions should target the most commonly tested facts.
- Quiz questions should mirror actual AP MC format with 4 choices and explanations.
- Worked examples should demonstrate the systematic ISEE approach to FRQs.

### Canvas Widget Standards
- Default canvas size: `920 x 440` (adjust height as needed).
- Always support dark mode: read colors from `getColors()` helper.
- Use `setupCanvas()` for DPI-aware rendering.
- Provide 2-4 sliders per widget with real-time visual feedback.
- Show computed results in `.result-card` elements below the canvas.
- Redraw on theme toggle (call draw functions inside `toggleTheme()`).

---

## 13. Existing AP Physics C: Mechanics Units

| Unit | File | Sections | Widgets | Features |
|------|------|----------|---------|----------|
| 1 | `Unit_1_Kinematics.html` | s1-1 to s1-5 | freefall-widget, projectile-widget | Canvas explorers |
| 2 | `Unit_2_Force_and_Dynamics.html` | s2-1 to s2-10 | circExplorer, dragExplorer, fmaExplorer, inclineExplorer, springExplorer | 5 canvas widgets |
| 3 | `Unit_3_Work_Energy_Power.html` | s3-1 to s3-5 | workExplorer, uxExplorer, springExplorer | Canvas explorers |
| 4 | `Unit_4_Linear_Momentum.html` | s4-1 to s4-4 | impulseExplorer, collisionExplorer, energyExplorer | Canvas explorers |
| 5 | `Unit_5_Torque_and_Rotational_Dynamics.html` | s5-1 to s5-6 | linrot-widget, rolling-widget, rotkin-widget, torque-widget | JSXGraph, ISEE examples |
| 6 | `Unit_6_Energy_and_Momentum_of_Rotating_Systems.html` | s6-1 to s6-6 | torquework-widget, angmom-widget, rolling6-widget, orbit-widget | JSXGraph, ISEE examples |
| 7 | `Unit_7_Oscillations.html` | s7-1 to s7-5 | shm-widget (+ shmPhaseCanvas) | JSXGraph, ISEE, phase-space, damping controls |

---

## 14. Extending to Other AP Courses

This generation system is designed to be **course-agnostic**. To generate study guides for a different AP course:

1. Replace `AP Physics C: Mechanics` in the title, description, and hero overline.
2. Supply the new course's CED (Course and Exam Description) topics via RAG.
3. Adapt widget types to the subject (e.g., graphing calculators for Calculus, circuit simulators for Physics E&M).
4. Keep all design system tokens, CSS components, JS architecture, and accessibility standards identical.

The design system, component library, and interactive framework are universal. Only the **content** changes.
