#!/usr/bin/env python3
"""Translation-coverage audit: for every in-scope HTML product (landing page +
High School and AP/IB subjects), count EN vs ZH bilingual spans and classify the
file's EN->ZH pairing status. This is the internal checklist behind the
"every English note must have a Chinese pair" philosophy.

Classification (raw data-lang span counts; the lang-toggle CSS contributes +1 to
each of en/zh in bilingual files, which cancels for the equality test):
  PAIRED      en == zh and en > 0   -> every EN note has a ZH pair
  PARTIAL     en != zh, both > 0    -> some EN notes lack a ZH pair
  EN-ONLY     zh == 0               -> no bilingual markup; full translation needed
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# In scope: landing page + High School + AP + IB. University tier excluded.
SUBJECTS = [
    "High School Math",
    "AP Calculus", "AP Physics", "AP CSA",
    "IB Chemistry HL", "IB Math HL", "IB Physics HL",
]
EXCLUDE_DIRS = {".git", ".claude", "_site", "rag", "scripts", "prompts",
                "Performance Update", "IB Math AI HL"}

EN = re.compile(r'data-lang="en"')
ZH = re.compile(r'data-lang="zh"')

def classify(en, zh):
    if zh == 0:
        return "EN-ONLY"
    if en == zh:
        return "PAIRED"
    return "PARTIAL"

def scan(p):
    txt = p.read_text(encoding="utf-8", errors="replace")
    en, zh = len(EN.findall(txt)), len(ZH.findall(txt))
    return en, zh, classify(en, zh)

def surface(rel):
    s = str(rel)
    if "Solutions" in s: return "S"
    if "Practice" in s:  return "P"
    if "Study Gu" in s:  return "SG"
    return "?"

# Landing page
print("== LANDING ==")
en, zh, st = scan(ROOT / "index.html")
print(f"index.html\tEN={en}\tZH={zh}\t{st}")

for subj in SUBJECTS:
    base = ROOT / subj
    if not base.exists():
        print(f"\n== {subj} ==  (folder missing)")
        continue
    print(f"\n== {subj} ==")
    rows = []
    for p in sorted(base.rglob("*.html")):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        en, zh, st = scan(p)
        rows.append((surface(p.relative_to(base)), st, en, zh, p.name))
    # summary line
    tot = len(rows)
    paired = sum(1 for r in rows if r[1] == "PAIRED")
    partial = sum(1 for r in rows if r[1] == "PARTIAL")
    enonly = sum(1 for r in rows if r[1] == "EN-ONLY")
    print(f"  TOTAL {tot}: PAIRED {paired} | PARTIAL {partial} | EN-ONLY {enonly}")
    for surf, st, en, zh, name in rows:
        flag = "" if st == "PAIRED" else "  <-- NEEDS WORK"
        print(f"  [{surf:2}] {st:8} en={en:<4} zh={zh:<4} {name}{flag}")
