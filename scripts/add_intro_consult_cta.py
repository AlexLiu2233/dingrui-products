#!/usr/bin/env python3
"""Insert the INTRO consult-CTA directly under each Study Guide's read-me block.

The end-of-page consult-CTA already ships on every SG (P0 + Sprint A). This adds
a SECOND CTA up top, under the hero "Read me first" intro, mirroring how the
University Calculus engine bakes it in. Conversion surface at the moment of
highest intent (the reader just landed).

Placement (matches UC: CTA sits after the read-me, before the first content):
  - if a `<section ... id="how-to-use">` ("Read me first") block exists, insert
    the aside right after that section closes;
  - else insert right after the hero `</section>`.

The `.consult-cta` CSS already exists in these files (end-CTA sprint), so only
the <aside> is inserted. UTM uses `__sg_intro__<lang>` (vs the end CTA's
`__sg__<lang>`) so the funnel can separate intro-placement clicks. Campaign +
unit slug are reused from the file's existing end CTA for consistency.

Idempotent: skips any file that already contains `__sg_intro__`.
Bilingual where the file is; EN-only otherwise (parity-neutral).

Run:  python scripts/add_intro_consult_cta.py [--only SUBPATH ...]   # default: all
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA",
    "IB Math HL", "IB Chemistry HL", "IB Physics HL",
]  # University Calculus already compliant (engine-baked) -> excluded.

END_CTA_RE = re.compile(
    r"utm_campaign=([a-z0-9_]+)&utm_content=([a-z0-9_]+)__sg__en", re.I)
HOWTO_RE = re.compile(r'<section[^>]*id="how-to-use"[^>]*>.*?</section>', re.S | re.I)
HERO_RE = re.compile(r'<section[^>]*class="hero"[^>]*>.*?</section>', re.S | re.I)
# Fallback for templates whose hero is a <div> (some AP Physics units): drop the
# CTA right before the first content <section>. Only reached when neither a
# how-to-use section nor a <section class="hero"> exists, so this <section> is
# guaranteed to be the first content block, not the hero.
FIRST_SEC_RE = re.compile(r'<section\b', re.I)

BASE = "https://www.dingruischolars.com/signup"


def cta_html(campaign: str, slug: str, bilingual: bool) -> str:
    en = f'{BASE}?utm_source=notes&utm_medium=cta&utm_campaign={campaign}&utm_content={slug}__sg_intro__en'
    zh = f'{BASE}-ch?utm_source=notes&utm_medium=cta&utm_campaign={campaign}&utm_content={slug}__sg_intro__zh'
    if bilingual:
        return (
            '\n<!-- consult-cta(intro): lead-gen conversion surface under read-me -->\n'
            '<aside class="consult-cta consult-cta--intro">\n'
            '  <p class="consult-cta__lead"><span data-lang="en">Aiming for the top of the mark scheme?</span>'
            '<span data-lang="zh">想冲刺满分？</span></p>\n'
            '  <p class="consult-cta__body"><span data-lang="en">Book a free 15-minute consult with a Dingrui '
            'Scholars tutor. We will help you master this unit and map your path forward.</span>'
            '<span data-lang="zh">预约 Dingrui Scholars 导师的 15 分钟免费咨询。我们将帮助你掌握本单元，并规划下一步的学习路径。</span></p>\n'
            f'  <a class="consult-cta__btn" data-lang="en" href="{en}" target="_blank" rel="noopener">Book a free consult &rarr;</a>\n'
            f'  <a class="consult-cta__btn" data-lang="zh" href="{zh}" target="_blank" rel="noopener">预约免费咨询 &rarr;</a>\n'
            '</aside>\n')
    return (
        '\n<!-- consult-cta(intro): lead-gen conversion surface under read-me -->\n'
        '<aside class="consult-cta consult-cta--intro">\n'
        '  <p class="consult-cta__lead">Aiming for the top of the mark scheme?</p>\n'
        '  <p class="consult-cta__body">Book a free 15-minute consult with a Dingrui Scholars tutor. '
        'We will help you master this unit and map your path forward.</p>\n'
        f'  <a class="consult-cta__btn" href="{en}" target="_blank" rel="noopener">Book a free consult &rarr;</a>\n'
        '</aside>\n')


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "__sg_intro__" in t:
        return "skip-present"
    m = END_CTA_RE.search(t)
    if not m:
        return "SKIP-no-end-cta"
    campaign, slug = m.group(1), m.group(2)
    bilingual = "body.lang-zh" in t or 'data-lang="zh"' in t
    html = cta_html(campaign, slug, bilingual)

    anchor = HOWTO_RE.search(t)
    where = "after-readme"
    if not anchor:
        anchor = HERO_RE.search(t)
        where = "after-hero"
    if anchor:
        t = t[: anchor.end()] + "\n" + html + t[anchor.end():]
    else:
        # div-hero fallback: insert before the first content <section>
        anchor = FIRST_SEC_RE.search(t)
        if not anchor:
            return "SKIP-no-anchor"
        t = t[: anchor.start()] + html + "\n" + t[anchor.start():]
        where = "before-section"

    path.write_text(t, encoding="utf-8")
    return where


def main() -> int:
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    files = []
    if only:
        files = [ROOT / p for p in only]
    else:
        for s in SUBJECTS:
            files.extend(sorted((ROOT / s / "Study Guides").glob("*.html")))
    counts = collections.Counter()
    for f in files:
        st = process(f)
        counts[st] += 1
        tag = "  !!" if st.startswith("SKIP") else "  ok"
        if only or st.startswith("SKIP"):
            print(f"{tag} {st:16s} {f.relative_to(ROOT)}")
    print(f"\nProcessed {len(files)} files:")
    for k, v in sorted(counts.items()):
        print(f"  {v:3d}  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
