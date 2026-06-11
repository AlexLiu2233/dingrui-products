#!/usr/bin/env python3
"""Quantitative quality sweep across every Study Guide (all tiers).

Emits a per-file metrics table + outlier flags so a content audit can target
the thinnest / least-complete guides. Measures EN-visible words (strips
data-lang="zh" spans) so bilingual (HS/AP/IB) and EN-only (University Calculus)
guides are compared on the same axis.

Signals per file:
  enwords  approx English body words (zh spans + tags removed)
  sec      <section class="section"> count (topic coverage / breadth)
  fc       flashcards (terse Q/formula recall cards)
  quiz     interactive quiz blocks (retrieval practice)
  wex      worked examples (<details> "Worked Example")
  deep     "Going deeper" depth blocks (full-mark theory)
  math     KaTeX $$ display blocks
  chk      checklist items
  iCTA     intro consult-CTA present (under read-me)  1/0
  eCTA     end consult-CTA present                    1/0

Run:  python scripts/sg_quality_sweep.py            # table for all subjects
      python scripts/sg_quality_sweep.py --csv      # CSV to stdout
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

SUBJECTS = [
    ("HS",  "High School Math"),
    ("HS",  "High School Physics"),
    ("HS",  "High School Chemistry"),
    ("HS",  "High School Biology"),
    ("HS",  "High School Computer Science"),
    ("AP",  "AP Calculus"),
    ("AP",  "AP Physics"),
    ("AP",  "AP CSA"),
    ("IB",  "IB Math HL"),
    ("IB",  "IB Chemistry HL"),
    ("IB",  "IB Physics HL"),
    ("UNI", "University Calculus"),
]

ZH_SPAN = re.compile(r'<span\s+data-lang=["\']zh["\'][^>]*>.*?</span>', re.S)
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def en_words(html: str) -> int:
    # Drop zh spans, then take the <body>, strip script/style, strip tags.
    body = html
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    if m:
        body = m.group(1)
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S | re.I)
    body = ZH_SPAN.sub(" ", body)
    body = TAG.sub(" ", body)
    body = WS.sub(" ", body)
    return len(body.split())


def metric(html: str):
    low = html.lower()
    wex = len(re.findall(r"worked example", low))
    deep = len(re.findall(r"going deeper", low))
    return {
        "enwords": en_words(html),
        "sec": low.count('class="section"'),
        "fc": low.count("flashcard"),
        "quiz": low.count('class="quiz"'),
        "wex": wex,
        "deep": deep,
        "math": html.count("$$") // 2,
        "chk": low.count("checklist-item") or low.count("checklist__item"),
        # number of consult-cta asides: 2 = intro(under read-me)+end (UC-compliant),
        # 1 = end only (needs the intro-CTA retrofit), 0 = none.
        "cta": len(re.findall(r'<aside class="consult-cta"', html)),
    }


def main() -> int:
    csv = "--csv" in sys.argv
    rows = []
    for tier, subj in SUBJECTS:
        d = ROOT / subj / "Study Guides"
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.html")):
            m = metric(f.read_text(encoding="utf-8", errors="replace"))
            rows.append((tier, subj, f.name, m))

    cols = ["enwords", "sec", "fc", "quiz", "wex", "deep", "math", "chk", "cta"]
    if csv:
        print("tier,subject,file," + ",".join(cols))
        for tier, subj, name, m in rows:
            print(f'{tier},"{subj}","{name}",' + ",".join(str(m[c]) for c in cols))
        return 0

    hdr = f'{"tier":4} {"subject":28} {"enwd":>5} {"sec":>3} {"fc":>3} {"quiz":>4} {"wex":>3} {"deep":>4} {"math":>4} {"chk":>3} {"cta":>3}  file'
    print(hdr)
    print("-" * len(hdr))
    for tier, subj, name, m in rows:
        flags = []
        if m["enwords"] < 3500: flags.append("THIN")
        if m["sec"] < 6: flags.append("FEW-SEC")
        if m["wex"] < 3: flags.append("FEW-WEX")
        if m["cta"] < 2: flags.append("needs-intro-CTA")
        mark = ("  <- " + ",".join(flags)) if flags else ""
        print(f'{tier:4} {subj[:28]:28} {m["enwords"]:5d} {m["sec"]:3d} {m["fc"]:3d} '
              f'{m["quiz"]:4d} {m["wex"]:3d} {m["deep"]:4d} {m["math"]:4d} {m["chk"]:3d} '
              f'{m["cta"]:3d}  {name[:42]}{mark}')

    # Per-tier summary
    print("\n=== per-subject EN-word summary (min / median / max) ===")
    from statistics import median
    bysubj = {}
    for tier, subj, name, m in rows:
        bysubj.setdefault((tier, subj), []).append(m["enwords"])
    for (tier, subj), ws in bysubj.items():
        ws.sort()
        print(f'  {tier:4} {subj[:28]:28} n={len(ws):2d}  min={ws[0]:5d}  med={int(median(ws)):5d}  max={ws[-1]:5d}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
