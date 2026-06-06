#!/usr/bin/env python3
"""Inject the lead-gen "Book a free consult" CTA into HS Study Guides (P0 sprint).

The CTA is the conversion surface for the academic-consulting funnel: every HS
notes page now ends with a bilingual call-to-action linking to the signup flow
(EN -> /signup, ZH -> /signup-ch). Print-friendly (white box + visible URL so a
shared printout still carries the link). Parity-neutral: each insert adds 3
data-lang="en" and 3 data-lang="zh" elements, so the bilingual gate stays balanced.

Idempotent: re-running skips files that already contain the CTA.
Run:  python scripts/add_consult_cta.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SG_DIRS = [
    "High School Math/Study Guides",
    "High School Physics/Study Guides",
    "High School Chemistry/Study Guides",
    "High School Biology/Study Guides",
    "High School Computer Science/Study Guides",
]

CSS_BLOCK = """
/* consult-cta: lead-gen conversion surface (P0) */
.consult-cta { background: linear-gradient(180deg, var(--accent-light) 0%, var(--bg-card) 100%); border: 2px solid var(--accent); border-radius: var(--radius); padding: 22px 26px; margin: 30px 0 8px; text-align: center; }
.consult-cta__lead { font-family: var(--font-display); font-size: 1.25rem; color: var(--accent); margin: 0 0 6px; }
.consult-cta__body { color: var(--text-secondary); font-size: 0.95rem; line-height: 1.55; margin: 0 auto 16px; max-width: 48ch; }
.consult-cta__btn { display: inline-block; background: var(--accent); color: #fff; font-family: var(--font-body); font-weight: 700; font-size: 0.95rem; text-decoration: none; padding: 10px 26px; border-radius: 8px; transition: transform 0.15s, background 0.2s; }
.consult-cta__btn:hover { background: var(--accent-dark); transform: translateY(-1px); }
@media print { .consult-cta { border: 1px solid #999; background: #fff; } .consult-cta__btn { background: #fff !important; color: #000 !important; border: 1px solid #999; } .consult-cta__btn[data-lang="en"]::after { content: " (dingruischolars.com/signup)"; font-weight: 400; } .consult-cta__btn[data-lang="zh"]::after { content: " (dingruischolars.com/signup-ch)"; font-weight: 400; } }
"""

HTML_BLOCK = """<!-- consult-cta: lead-gen conversion surface (P0 sprint) -->
<aside class="consult-cta">
  <p class="consult-cta__lead"><span data-lang="en">Want to go further, faster?</span><span data-lang="zh">想走得更远、更快？</span></p>
  <p class="consult-cta__body"><span data-lang="en">Book a free 15-minute consult with a Dingrui Scholars tutor. We will map your path from this unit through AP and IB and into university.</span><span data-lang="zh">预约 Dingrui Scholars 导师的 15 分钟免费咨询。我们将为你规划从本单元出发，贯通 AP 与 IB 直至大学的学习路径。</span></p>
  <a class="consult-cta__btn" data-lang="en" href="https://www.dingruischolars.com/signup" target="_blank" rel="noopener">Book a free consult &rarr;</a>
  <a class="consult-cta__btn" data-lang="zh" href="https://www.dingruischolars.com/signup-ch" target="_blank" rel="noopener">预约免费咨询 &rarr;</a>
</aside>

"""

STYLE_ANCHOR = "</style>"
FOOTER_ANCHOR = '<div class="footer-wrap">'


def process(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "consult-cta" in text:
        return "skip (already present)"
    if text.count(STYLE_ANCHOR) != 1 or text.count(FOOTER_ANCHOR) != 1:
        return f"SKIP (anchor mismatch: style={text.count(STYLE_ANCHOR)} footer={text.count(FOOTER_ANCHOR)})"
    text = text.replace(STYLE_ANCHOR, CSS_BLOCK + STYLE_ANCHOR, 1)
    text = text.replace(FOOTER_ANCHOR, HTML_BLOCK + FOOTER_ANCHOR, 1)
    path.write_text(text, encoding="utf-8")
    return "injected"


def main() -> int:
    files = []
    for d in SG_DIRS:
        files.extend(sorted((ROOT / d).glob("*.html")))
    if not files:
        print("No HS Study Guide files found.", file=sys.stderr)
        return 1
    counts = {}
    for f in files:
        status = process(f)
        counts[status] = counts.get(status, 0) + 1
        print(f"  {status:28s} {f.relative_to(ROOT)}")
    print("\nSummary:", ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
