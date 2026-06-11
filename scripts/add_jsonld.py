#!/usr/bin/env python3
"""Inject JSON-LD LearningResource structured data into every page (Get-Found / SEO).

Zero of the 234 pages currently carry structured data, so search engines see only
generic HTML. A schema.org LearningResource per page tells Google exactly what this
is (an educational resource, its level, its language, who provides it), which makes
the pages eligible for richer results and better topical ranking.

Per page, derived from its <title>, meta description, path, and bilingual detection:
  @type LearningResource, name, description, url (absolute), inLanguage [en(,zh)],
  learningResourceType (Study Guide / Practice problems / Solutions), educationalLevel
  (High School / AP / IB), isAccessibleForFree, provider Organization (Dingrui Scholars).

Idempotent: pages already containing application/ld+json are skipped. Inserts the
<script type="application/ld+json"> block immediately before </head>.

Run:  python scripts/add_jsonld.py
"""
import collections
import html
import json
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://alexliu2233.github.io/dingrui-products/"
PROVIDER_URL = "https://www.dingruischolars.com"

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
    "University Calculus",
]

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="(.*?)"', re.S)


def level(relpath: str) -> str:
    if relpath.startswith("High School"):
        return "High School"
    if relpath.startswith("AP"):
        return "AP"
    if relpath.startswith("IB"):
        return "IB"
    if relpath.startswith("University"):
        return "University"
    return "Mixed"


def restype(relpath: str) -> str:
    p = relpath.replace("\\", "/").lower()
    if "/solutions/" in p or p.endswith("_solutions.html"):
        return "Solutions"
    if "/practice questions/" in p or "practice" in p.rsplit("/", 1)[-1]:
        return "Practice problems"
    return "Study Guide"


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "application/ld+json" in t:
        return "skip-present"
    if t.count("</head>") != 1:
        return "SKIP-head"
    relpath = "index.html" if path == ROOT / "index.html" else str(path.relative_to(ROOT))
    m = TITLE_RE.search(t)
    if not m:
        return "SKIP-title"
    name = html.unescape(re.split(r"\s*\|\s*", m.group(1).strip())[0])
    dm = DESC_RE.search(t)
    desc = html.unescape(dm.group(1).strip()) if dm else name
    url = BASE + urllib.parse.quote(relpath.replace("\\", "/"), safe="/")
    langs = ["en", "zh"] if 'data-lang="zh"' in t else ["en"]

    if relpath == "index.html":
        data = {
            "@context": "https://schema.org",
            "@type": "EducationalOrganization",
            "name": "Dingrui Scholars",
            "url": BASE,
            "description": desc,
            "sameAs": [PROVIDER_URL],
        }
    else:
        data = {
            "@context": "https://schema.org",
            "@type": "LearningResource",
            "name": name,
            "description": desc,
            "url": url,
            "inLanguage": langs,
            "learningResourceType": restype(relpath),
            "educationalLevel": level(relpath),
            "isAccessibleForFree": True,
            "provider": {
                "@type": "EducationalOrganization",
                "name": "Dingrui Scholars",
                "url": PROVIDER_URL,
            },
        }

    payload = json.dumps(data, ensure_ascii=False, indent=2)
    block = f'\n<script type="application/ld+json">\n{payload}\n</script>\n'
    t = t.replace("</head>", block + "</head>", 1)
    path.write_text(t, encoding="utf-8")
    return "jsonld-added"


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
