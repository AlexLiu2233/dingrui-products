#!/usr/bin/env python3
"""Inject the lead-gen "Book a free consult" CTA into AP/IB notes (Sprint A).

Extends the HS conversion surface to the AP/IB tier. AP/IB files span several
templates, so this handles the variants detected by recon:

  Study Guides (49): --accent token system, bilingual toggle. Insert CSS before
    the first </style>; insert the bilingual CTA before <div class="footer-wrap">
    if present, else before </main>, else before </body>. var(--x, fallback)
    guards the handful of SGs missing --accent-dark/-light/--bg-card/--radius.

  Practice/Solutions (82): --maroon token system, <footer class="page-foot">.
    58 are bilingual (body.lang-zh present) -> bilingual CTA. 24 are EN-only
    (no toggle) -> EN-only CTA with NO data-lang spans (parity-neutral; a
    bilingual block would render both languages since there's no toggle CSS).
    --paper-bg/--muted/--font-sans are NOT universal here, so the P+S CSS uses
    hardcoded safe values + only the universal --maroon.

Parity-neutral: bilingual inserts add equal data-lang en/zh; EN-only inserts add
none. Idempotent: skips files already containing the CTA.
Run:  python scripts/add_consult_cta_apib.py
"""
import collections
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUBJECTS = ["AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL"]

# ---- Study Guide assets (--accent system) -------------------------------------
SG_CSS = """
/* consult-cta: lead-gen conversion surface (Sprint A) */
.consult-cta { background: linear-gradient(180deg, var(--accent-light, #F2E4E4) 0%, var(--bg-card, #fff) 100%); border: 2px solid var(--accent); border-radius: var(--radius, 12px); padding: 22px 26px; margin: 30px 0 8px; text-align: center; }
.consult-cta__lead { font-family: var(--font-display); font-size: 1.25rem; color: var(--accent); margin: 0 0 6px; }
.consult-cta__body { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.55; margin: 0 auto 16px; max-width: 48ch; }
.consult-cta__btn { display: inline-block; background: var(--accent); color: #fff; font-family: var(--font-body); font-weight: 700; font-size: 0.95rem; text-decoration: none; padding: 10px 26px; border-radius: 8px; transition: transform 0.15s, background 0.2s; }
.consult-cta__btn:hover { background: var(--accent-dark, #5A1E1E); transform: translateY(-1px); }
@media print { .consult-cta { border: 1px solid #999; background: #fff; } .consult-cta__btn { background: #fff !important; color: #000 !important; border: 1px solid #999; } .consult-cta__btn[data-lang="en"]::after { content: " (dingruischolars.com/signup)"; font-weight: 400; } .consult-cta__btn[data-lang="zh"]::after { content: " (dingruischolars.com/signup-ch)"; font-weight: 400; } }
"""

SG_HTML = """<!-- consult-cta: lead-gen conversion surface (Sprint A) -->
<aside class="consult-cta">
  <p class="consult-cta__lead"><span data-lang="en">Want to go further, faster?</span><span data-lang="zh">想走得更远、更快？</span></p>
  <p class="consult-cta__body"><span data-lang="en">Book a free 15-minute consult with a Dingrui Scholars tutor. We will help you master this unit and map your path into university.</span><span data-lang="zh">预约 Dingrui Scholars 导师的 15 分钟免费咨询。我们将帮助你掌握本单元，并规划通往大学的学习路径。</span></p>
  <a class="consult-cta__btn" data-lang="en" href="https://www.dingruischolars.com/signup" target="_blank" rel="noopener">Book a free consult &rarr;</a>
  <a class="consult-cta__btn" data-lang="zh" href="https://www.dingruischolars.com/signup-ch" target="_blank" rel="noopener">预约免费咨询 &rarr;</a>
</aside>

"""

# ---- Practice/Solutions assets (--maroon system, hardened fallbacks) -----------
PP_CSS = """
  /* consult-cta: lead-gen conversion surface (Sprint A) */
  .consult-cta{border:1.5px solid var(--maroon);border-radius:8px;padding:12px 16px;margin:22px 0 6px;text-align:center;background:#FBECEC;break-inside:avoid;}
  .consult-cta__lead{display:block;font-family:'Source Sans 3',-apple-system,'Segoe UI',sans-serif;font-weight:700;font-size:11pt;color:var(--maroon);}
  .consult-cta__body{display:block;font-family:'Source Sans 3',-apple-system,'Segoe UI',sans-serif;font-size:9.5pt;color:#555;margin:3px 0 6px;}
  .consult-cta__btn{display:inline-block;font-family:'Source Sans 3',-apple-system,'Segoe UI',sans-serif;font-weight:700;font-size:10pt;color:var(--maroon);text-decoration:underline;}
"""

PP_HTML_BILINGUAL = """<!-- consult-cta: lead-gen conversion surface (Sprint A) -->
<aside class="consult-cta">
  <span class="consult-cta__lead"><span data-lang="en">Stuck, or want to go further?</span><span data-lang="zh">遇到困难，或想更进一步？</span></span>
  <span class="consult-cta__body"><span data-lang="en">Book a free 15-minute consult with a Dingrui Scholars tutor:</span><span data-lang="zh">预约 Dingrui Scholars 导师的 15 分钟免费咨询：</span></span>
  <a class="consult-cta__btn" data-lang="en" href="https://www.dingruischolars.com/signup" target="_blank" rel="noopener">dingruischolars.com/signup</a>
  <a class="consult-cta__btn" data-lang="zh" href="https://www.dingruischolars.com/signup-ch" target="_blank" rel="noopener">dingruischolars.com/signup-ch</a>
</aside>

"""

PP_HTML_EN = """<!-- consult-cta: lead-gen conversion surface (Sprint A) -->
<aside class="consult-cta">
  <span class="consult-cta__lead">Stuck, or want to go further?</span>
  <span class="consult-cta__body">Book a free 15-minute consult with a Dingrui Scholars tutor:</span>
  <a class="consult-cta__btn" href="https://www.dingruischolars.com/signup" target="_blank" rel="noopener">dingruischolars.com/signup</a>
</aside>

"""

PAGEFOOT = '<footer class="page-foot">'
FOOTWRAP = '<div class="footer-wrap">'
STYLE = "</style>"


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "consult-cta" in t:
        return "skip-present"
    if t.count(STYLE) < 1:
        return "SKIP-no-style"

    if PAGEFOOT in t:  # Practice / Solutions
        bilingual = "body.lang-zh" in t
        css, html = PP_CSS, (PP_HTML_BILINGUAL if bilingual else PP_HTML_EN)
        t = t.replace(STYLE, css + STYLE, 1)
        t = t.replace(PAGEFOOT, html + PAGEFOOT, 1)
        kind = "PP-bi" if bilingual else "PP-en"
    else:  # Study Guide
        css, html = SG_CSS, SG_HTML
        t = t.replace(STYLE, css + STYLE, 1)
        if FOOTWRAP in t:
            t = t.replace(FOOTWRAP, html + FOOTWRAP, 1); anchor = "footwrap"
        elif "</main>" in t:
            t = t.replace("</main>", html + "</main>", 1); anchor = "main"
        elif "</body>" in t:
            t = t.replace("</body>", html + "</body>", 1); anchor = "body"
        else:
            return "SKIP-no-anchor"
        kind = "SG-" + anchor

    path.write_text(t, encoding="utf-8")
    return kind


def main() -> int:
    files = []
    for s in SUBJECTS:
        for sub in ["Study Guides", "Practice Questions", "Practice Questions/Solutions"]:
            files.extend(sorted((ROOT / s / sub).glob("*.html")))
    counts = collections.Counter()
    for f in files:
        st = process(f)
        counts[st] += 1
        if st.startswith("SKIP"):
            print(f"  !! {st:16s} {f.relative_to(ROOT)}")
    print(f"\nProcessed {len(files)} files:")
    for k, v in sorted(counts.items()):
        print(f"  {v:3d}  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
