#!/usr/bin/env python3
"""University Calculus bulk Study-Guide assembler (internal; stripped from deploy).

Clones the LOCKED A1 template's chrome (verbatim <style> blocks, base64 logo, and
the quiz/flashcard/theme JS) and wraps fresh English-only content around it, so every
unit is a faithful sibling of the locked template. Each unit carries the consult CTA
twice: once directly under the hero "Read me first" box, and once before the flashcards
(the standing CTA-after-readme convention, see University Calculus/AUDIT.md).

USAGE (handoff): write a per-unit spec and call build_and_save(spec). See _unit_A2.py
for a worked example. Then run:  python scripts/build-index.py && python scripts/build_sitemap.py
and validate:  bash scripts/validate.sh "University Calculus/Study Guides/<file>.html"

SPEC keys (all required unless noted):
  uid       e.g. "A2"                         group letter + index
  slug      e.g. "Unit_A2_The_Derivative"     filename stem (no .html)
  topic     e.g. "The Derivative"             card/title topic text
  overline  e.g. "University Calculus · Calculus I"
  h1        e.g. "Unit A2: The<br>Derivative" (raw HTML allowed)
  sub       hero subtitle (plain text, no dashes)
  chips     list[str]
  readme    "Read me first" paragraph (plain text, no dashes)
  toc       list[(href, label)] for the section links (Overview/Flashcards/Quiz/Checklist appended)
  sections  raw HTML string: the <section class="section" id="sN"> ... </section> blocks
  flashcards list[(front_html, back_html)]
  quiz      raw HTML string: the <section class="section" id="unit-quiz"> ... </section> block
  checklist list[str] (each becomes an <li onclick="toggleCheck(this)">)
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "University Calculus" / "Study Guides" / "Unit_A1_Limits_and_Continuity.html"
OUTDIR = ROOT / "University Calculus" / "Study Guides"
BASE = "https://alexliu2233.github.io/dingrui-products/University%20Calculus/Study%20Guides/"


def _chrome():
    t = TEMPLATE.read_text(encoding="utf-8")
    style = t[t.index("<style>"): t.index('<script type="application/ld+json">')].rstrip()
    m = re.search(r'<img[^>]*src="data:image[^"]*"[^>]*>', t)
    logo = m.group(0)
    js = t[t.index("</main>") + len("</main>"): t.index("</body>")].strip()
    return style, logo, js


def _cta(slug, lead="Stuck on this in your first-year course?"):
    utm = slug.lower() + "__sg__en"
    return (
        '<aside class="consult-cta">\n'
        f'  <p class="consult-cta__lead">{lead}</p>\n'
        '  <p class="consult-cta__body">Book a free 15-minute consult with a Dingrui Scholars tutor. '
        'We will get you unstuck before your next midterm.</p>\n'
        '  <a class="consult-cta__btn" href="https://www.dingruischolars.com/signup'
        f'?utm_source=notes&utm_medium=cta&utm_campaign=university_calculus&utm_content={utm}" '
        'target="_blank" rel="noopener">Book a free consult &rarr;</a>\n'
        '</aside>'
    )


def assemble(spec):
    style, logo, js = _chrome()
    slug, topic, uid = spec["slug"], spec["topic"], spec["uid"]
    canon = BASE + slug + ".html"
    desc = (f"University Calculus Unit {uid}: {topic}. Rigorous first-year university notes to the "
            "MIT, Georgia Tech, and Princeton standard, with worked examples, proofs, quizzes, "
            "dark mode, and print-friendly formatting from Dingrui Scholars.")
    title = f"University Calculus — Unit {uid}: {topic} | Dingrui Scholars"

    head = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'<meta name="description" content="{desc}">\n'
        '<meta name="theme-color" content="#7A2E2E">\n<meta name="color-scheme" content="light dark">\n'
        f'<title>{title}</title>\n<link rel="canonical" href="{canon}">\n'
        '<!-- Google tag (gtag.js) -->\n'
        '<script async src="https://www.googletagmanager.com/gtag/js?id=G-SDVTGZ6RJ9"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
        "gtag('js',new Date());gtag('config','G-SDVTGZ6RJ9');</script>\n"
        '<!-- OpenGraph / Twitter share cards -->\n'
        '<meta property="og:type" content="article">\n<meta property="og:site_name" content="Dingrui Scholars">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="{canon}">\n'
        '<meta property="og:image" content="https://alexliu2233.github.io/dingrui-products/LOGO.png">\n'
        '<meta property="og:locale" content="en_US">\n<meta name="twitter:card" content="summary">\n'
        f'<meta property="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        '<meta name="twitter:image" content="https://alexliu2233.github.io/dingrui-products/LOGO.png">\n'
        '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=JetBrains+Mono:wght@400;500;600&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">\n\n'
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">\n'
        '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>\n'
        '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: \'$$\', right: \'$$\', display: true}, {left: \'$\', right: \'$\', display: false}]});"></script>\n'
    )

    jsonld = (
        '<script type="application/ld+json">\n{\n'
        '  "@context": "https://schema.org",\n  "@type": "LearningResource",\n'
        f'  "name": "University Calculus — Unit {uid}: {topic}",\n'
        f'  "description": "{desc}",\n  "url": "{canon}",\n'
        '  "inLanguage": [\n    "en"\n  ],\n  "learningResourceType": "Study Guide",\n'
        '  "educationalLevel": "University",\n  "isAccessibleForFree": true,\n'
        '  "provider": {\n    "@type": "EducationalOrganization",\n    "name": "Dingrui Scholars",\n'
        '    "url": "https://www.dingruischolars.com"\n  }\n}\n</script>'
    )

    toc_links = '\n'.join(f'  <a href="{h}">{lbl}</a>' for h, lbl in spec["toc"])
    chips = '\n'.join(f'    <span class="chip">{c}</span>' for c in spec["chips"])
    fcs = '\n'.join(
        '    <div class="flashcard" onclick="flipCard(this)"><div class="flashcard-inner">'
        f'<div class="flashcard-front">{f}</div><div class="flashcard-back">{b}</div></div></div>'
        for f, b in spec["flashcards"]
    )
    checks = '\n'.join(f'    <li onclick="toggleCheck(this)">{c}</li>' for c in spec["checklist"])
    n_fc = len(spec["flashcards"])
    n_ck = len(spec["checklist"])

    body = f"""<body>
<nav class="top-nav">
  <div class="nav-left">
    {logo}
    <span class="nav-brand">Dingrui Scholars</span>
  </div>
  <div class="nav-right">
    <button class="nav-btn" id="tocToggle" onclick="document.getElementById('sidebar').classList.toggle('open')" title="Contents">Contents</button>
    <button class="nav-btn" id="themeToggle" onclick="toggleTheme()" title="Toggle dark mode">Dark</button>
  </div>
</nav>
<div class="progress-bar"><div id="progressFill"></div></div>

<aside class="sidebar" id="sidebar">
  <div class="sidebar-title">Table of Contents</div>
  <a href="#hero">Overview</a>
{toc_links}
  <a href="#flashcards">Flashcards</a>
  <a href="#unit-quiz">Unit Quiz</a>
  <a href="#checklist">Readiness Checklist</a>
</aside>

<main class="main-wrap">
<section class="hero" id="hero">
  <div class="hero-overline">{spec["overline"]}</div>
  <h1>{spec["h1"]}</h1>
  <p class="hero-sub">{spec["sub"]}</p>
  <div class="hero-meta">
{chips}
  </div>
  <div class="concept-box">
    <strong>Read me first.</strong>
    {spec["readme"]}
  </div>
</section>

{_cta(slug)}

{spec["sections"]}

{_cta(slug)}

<section id="flashcards">
  <h2>Flashcards</h2>
  <div class="flashcard-toolbar">
    <span class="fc-count" id="fcCount">0 / {n_fc} flipped</span>
    <div>
      <button class="nav-btn" onclick="shuffleFlashcards()">Shuffle</button>
      <button class="nav-btn" onclick="resetFlashcards()">Reset</button>
    </div>
  </div>
  <div class="flashcard-grid" id="flashcardGrid">
{fcs}
  </div>
</section>

{spec["quiz"]}

<section class="section" id="checklist">
  <div class="section-label">Before You Move On</div>
  <h2>Readiness Checklist</h2>
  <p>Tap each item you can do without notes. <span id="checkProgress">0 / {n_ck} mastered</span></p>
  <ul id="checklistUl" class="checklist">
{checks}
  </ul>
</section>

</main>
"""
    return head + style + "\n" + jsonld + "\n" + body + js


def build_and_save(spec):
    html = assemble(spec)
    out = OUTDIR / (spec["slug"] + ".html")
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} ({html.count(chr(10))+1} lines)")
    return out
