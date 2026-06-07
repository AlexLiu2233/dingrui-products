#!/usr/bin/env python3
"""Inject the GA4 gtag snippet into every deployable page (Sprint B, half 2).

Completes funnel instrumentation: page_view (auto) + outbound CTA clicks (auto via
GA4 enhanced measurement, which fires on links leaving github.io for the signup
domain) land in the SAME property the signup site uses (G-SDVTGZ6RJ9), so the
UTM-tagged CTAs resolve into a notes -> click -> signup funnel sliced by
subject / unit / language.

Inserted right after </title> (high in <head>, as GA recommends). Idempotent:
skips pages already containing the gtag loader.

Run:  python scripts/add_ga_analytics.py
"""
import collections
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GA_ID = "G-SDVTGZ6RJ9"

SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
]

SNIPPET = (
    "\n<!-- Google tag (gtag.js) -->"
    f'\n<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>'
    "\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
    f"gtag('js',new Date());gtag('config','{GA_ID}');</script>"
)


def process(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "googletagmanager.com/gtag" in t:
        return "skip-present"
    if t.count("</title>") != 1:
        return "SKIP-title"
    t = t.replace("</title>", "</title>" + SNIPPET, 1)
    path.write_text(t, encoding="utf-8")
    return "ga-added"


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
