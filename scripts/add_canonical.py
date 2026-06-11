#!/usr/bin/env python3
"""Add a self-referencing <link rel="canonical"> to every page (Get-Found / SEO).

Each notes page is reachable at several URLs that serve the same content:
  page.html, page.html?lang=zh, and the /preview/ staging mirror.
With no canonical tag, search engines may treat these as duplicates and split the
ranking signal. A canonical pointing at the production root URL (no query string)
consolidates all variants onto one address. The /preview/ copies inherit canonicals
that point back to production, so staging never competes with prod for ranking
(reinforcing robots.txt Disallow: /preview/).

Absolute URL built from BASE (production Pages root) + the page's repo-relative
path. Idempotent: pages already containing rel="canonical" are skipped. Inserts
immediately after the <title>.

Run:  python scripts/add_canonical.py
"""
import collections
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://alexliu2233.github.io/dingrui-products/"

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
    "University Calculus",
]


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if 'rel="canonical"' in t:
        return "skip-present"
    if t.count("</title>") != 1:
        return "SKIP-title"
    relpath = "index.html" if path == ROOT / "index.html" else str(path.relative_to(ROOT))
    url = BASE + urllib.parse.quote(relpath.replace("\\", "/"), safe="/")
    tag = f'\n<link rel="canonical" href="{url}">'
    t = t.replace("</title>", "</title>" + tag, 1)
    path.write_text(t, encoding="utf-8")
    return "canonical-added"


def main() -> int:
    files = [ROOT / "index.html"]
    for s in SUBJECTS:
        files.extend(sorted((ROOT / s).rglob("*.html")))
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
