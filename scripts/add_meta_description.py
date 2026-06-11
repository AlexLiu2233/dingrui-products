#!/usr/bin/env python3
"""Add a <meta name="description"> to every page missing one (Get-Found / SEO).

116 of 234 pages already have a description; 118 do not. With no description tag,
search engines invent a snippet from page text (often KaTeX or nav noise), which
reads badly and converts worse. This writes a clean, keyword-bearing, dash-free
(per copy-tone) description derived from each page's <title> + its doc type, and
re-syncs og:description / twitter:description to match so the share card agrees.

Description is English (the site defaults to English; meta description does not
toggle). Capped near 155 chars at a word boundary.

Idempotent: pages that already have name="description" are skipped untouched.
Inserts the new tag immediately after the <title>.

Run:  python scripts/add_meta_description.py
"""
import collections
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAXLEN = 155

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
    "University Calculus",
]

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta\s+name="description"', re.I)
OGDESC_RE = re.compile(r'(<meta\s+property="og:description"\s+content=")(.*?)(">)', re.S)
TWDESC_RE = re.compile(r'(<meta\s+name="twitter:description"\s+content=")(.*?)(">)', re.S)


def esc(s: str) -> str:
    return html.escape(html.unescape(s.strip()), quote=True)


def clip(s: str, n: int = MAXLEN) -> str:
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0].rstrip(",.;:")
    return cut + "."


def doctype(relpath: str) -> str:
    p = relpath.replace("\\", "/").lower()
    if relpath == "index.html":
        return "index"
    if "/solutions/" in p or p.endswith("_solutions.html"):
        return "solutions"
    if "/practice questions/" in p or "practice" in p.rsplit("/", 1)[-1]:
        return "practice"
    return "guide"


def describe(raw_title: str, relpath: str) -> str:
    if relpath == "index.html":
        return ("Dingrui Scholars: bilingual study guides, practice questions, and worked "
                "solutions for High School, AP, and IB math and science. Book a free consult.")
    # {Subject} — {Topic}[ — Practice|Solutions] | Dingrui Scholars
    head = re.split(r"\s*\|\s*", html.unescape(raw_title))[0]
    parts = [p.strip() for p in re.split(r"\s+[–—]\s+", head) if p.strip()]
    subject = parts[0] if parts else head
    mids = parts[1:]
    if mids and mids[-1].lower() in ("practice", "solutions", "practice questions"):
        mids = mids[:-1]
    topic = " ".join(mids).strip() or subject

    dt = doctype(relpath)
    if dt == "solutions":
        body = f"Worked solutions for {topic} in {subject}."
        tail = "Step by step answers from Dingrui Scholars."
    elif dt == "practice":
        body = f"Practice questions for {topic} in {subject}."
        tail = "Exam style problems with full worked solutions from Dingrui Scholars."
    else:
        body = f"Study guide for {topic} in {subject}."
        tail = "Clear explanations, worked examples, and practice from Dingrui Scholars."
    return clip(f"{body} {tail}")


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    relpath = "index.html" if path == ROOT / "index.html" else str(path.relative_to(ROOT))
    if DESC_RE.search(t):
        return "skip-present"
    m = TITLE_RE.search(t)
    if not m or t.count("</title>") != 1:
        return "SKIP-title"
    desc = describe(m.group(1).strip(), relpath)
    esc_desc = esc(desc)
    tag = f'\n<meta name="description" content="{esc_desc}">'
    t = t.replace("</title>", "</title>" + tag, 1)
    # Re-sync share-card descriptions so they match the new meta description.
    t = OGDESC_RE.sub(lambda mm: mm.group(1) + esc_desc + mm.group(3), t, count=1)
    t = TWDESC_RE.sub(lambda mm: mm.group(1) + esc_desc + mm.group(3), t, count=1)
    path.write_text(t, encoding="utf-8")
    return "desc-added"


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
