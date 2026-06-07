#!/usr/bin/env python3
"""Add OpenGraph + Twitter share-card meta to every deployable page (get-shared sprint).

When a notes URL is dropped into WeChat / iMessage / a group chat / social, the
platform currently shows a bare link. These tags make it render a branded card
(title + description + Dingrui logo), turning every shared link into advertising.

Per page, derived from its own <title> + meta description (or a templated default):
  og:type/site_name/title/description/url/image/locale (+ alternate zh_CN if bilingual)
  twitter:card=summary (+ title/description/image)

og:image + og:url must be ABSOLUTE -> built from BASE (production GitHub Pages root).
If a custom domain is later adopted, change BASE and re-run against a clean tree.
Idempotent: skips pages already containing og:title. Inserts right after </title>.

Run:  python scripts/add_og_tags.py
"""
import html
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://alexliu2233.github.io/dingrui-products/"  # production Pages root
LOGO = BASE + "LOGO.png"

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
]

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="(.*?)"', re.S)


def esc(s: str) -> str:
    return html.escape(html.unescape(s.strip()), quote=True)


def derive(t: str, relpath: str):
    raw_title = TITLE_RE.search(t).group(1).strip()
    topic = re.split(r"\s*\|\s*", raw_title)[0].strip()  # drop "| Dingrui Scholars"
    m = DESC_RE.search(t)
    desc = m.group(1).strip() if m else f"{topic}. Worked examples, practice, and solutions from Dingrui Scholars."
    url = BASE + urllib.parse.quote(relpath.replace("\\", "/"), safe="/")
    bilingual = 'data-lang="zh"' in t
    return esc(raw_title), esc(desc), url, bilingual


def block(title, desc, url, bilingual):
    alt = '\n<meta property="og:locale:alternate" content="zh_CN">' if bilingual else ""
    return (
        "\n<!-- OpenGraph / Twitter share cards -->"
        '\n<meta property="og:type" content="article">'
        '\n<meta property="og:site_name" content="Dingrui Scholars">'
        f'\n<meta property="og:title" content="{title}">'
        f'\n<meta property="og:description" content="{desc}">'
        f'\n<meta property="og:url" content="{url}">'
        f'\n<meta property="og:image" content="{LOGO}">'
        '\n<meta property="og:locale" content="en_US">' + alt +
        '\n<meta name="twitter:card" content="summary">'
        f'\n<meta name="twitter:title" content="{title}">'
        f'\n<meta name="twitter:description" content="{desc}">'
        f'\n<meta name="twitter:image" content="{LOGO}">'
    )


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "og:title" in t:
        return "skip-present"
    if t.count("</title>") != 1:
        return "SKIP-title"
    title, desc, url, bil = derive(t, str(path.relative_to(ROOT)))
    t = t.replace("</title>", "</title>" + block(title, desc, url, bil), 1)
    path.write_text(t, encoding="utf-8")
    return "og-added"


def main() -> int:
    files = [ROOT / "index.html"]
    for s in SUBJECTS:
        files.extend(sorted((ROOT / s).rglob("*.html")))
    import collections
    c = collections.Counter()
    for f in files:
        st = process(f)
        c[st] += 1
        if st.startswith("SKIP"):
            print("  !!", st, f.relative_to(ROOT))
    print(f"Processed {sum(c.values())} files:", dict(c))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
