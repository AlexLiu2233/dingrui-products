#!/usr/bin/env python3
"""Generate sitemap.xml + robots.txt for the notes site (Get-Found / SEO sprint).

The whole lead-gen funnel depends on search engines actually finding these 234
notes pages. Until now there was zero crawl guidance: no sitemap, no robots.txt.
This emits both at the repo root so they deploy to the production Pages root
(root files are NOT stripped by .github/workflows/deploy.yml).

  sitemap.xml  -> every deployable page, absolute URL off BASE, <lastmod> from
                  the file's last git commit date (falls back to mtime).
  robots.txt   -> allow all, Disallow /preview/ (keep staging out of the index),
                  point crawlers at the sitemap.

Scope note: this sitemap covers the NOTES site only (this GitHub Pages product),
not the marketing site dingruischolars.com. BASE is the production Pages root; if
a custom domain is adopted, change BASE and re-run on a clean tree.

Idempotent: overwrites both files from the current filesystem each run.

Run:  python scripts/build_sitemap.py
"""
import datetime
import pathlib
import subprocess
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://alexliu2233.github.io/dingrui-products/"  # production Pages root

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
]

# Student-named / unlisted drafts kept out of the public sitemap (flagged in STATUS).
EXCLUDE_SUBSTR = ["ethanfinalpractice"]


def lastmod(path: pathlib.Path) -> str:
    """Last git commit date (YYYY-MM-DD); fall back to filesystem mtime."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        ).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    ts = path.stat().st_mtime
    return datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")


def collect():
    files = [ROOT / "index.html"]
    for s in SUBJECTS:
        files.extend(sorted((ROOT / s).rglob("*.html")))
    pages, skipped = [], []
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if any(sub in rel.lower() for sub in EXCLUDE_SUBSTR):
            skipped.append(rel)
            continue
        pages.append(f)
    return pages, skipped


def main() -> int:
    pages, skipped = collect()
    rows = []
    for f in pages:
        rel = f.relative_to(ROOT).as_posix()
        url = BASE + urllib.parse.quote(rel, safe="/")
        prio = "1.0" if rel == "index.html" else "0.8"
        rows.append(
            "  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{lastmod(f)}</lastmod>\n"
            f"    <priority>{prio}</priority>\n"
            "  </url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    robots = (
        "# Dingrui Scholars notes site\n"
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /preview/\n"
        "\n"
        f"Sitemap: {BASE}sitemap.xml\n"
    )
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")

    print(f"sitemap.xml: {len(pages)} URLs written")
    print("robots.txt: written (Disallow /preview/, Sitemap linked)")
    for s in skipped:
        print(f"  excluded (unlisted/student-named): {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
