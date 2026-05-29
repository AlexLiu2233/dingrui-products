"""One-shot mechanical fixer for the HS Math audit P0 + P1 pass (2026-05-28).

Three transformations applied across the HS Math corpus:

1. Broken feeder hyperlinks — 10 wrong filenames replaced with correct ones
   (Units 6, 8, 9, 11, 12, 13 SGs).
2. Em-dash sweep — `&mdash;` HTML entity replaced with `, ` everywhere
   (matches the no-em-dash tone rule). Literal `—` Unicode is NOT touched
   (it appears in the brand title `High School Math — Topic | Dingrui Scholars`).
   Three known literal-em-dash prose instances (Unit 7 line 306,
   Unit 9 lines 276 + 426) are handled by targeted Edit afterwards.
3. Stale phrasing — "(forthcoming)" / "(not yet published)" / "when it
   lands" / "(when it lands)" removed where flagged in the audit.

Judgement-level fixes (convention leaks in hero/feeder prose, broken
quizzes, mark-sum errors, hero chip "+ AB", honors flag wording,
Unit 13 N convention, Unit 12 literal placeholder text, Unit 11 KaTeX
braces) are handled via targeted Edit calls after this script runs.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SG = ROOT / "High School Math" / "Study Guides"
PQ = ROOT / "High School Math" / "Practice Questions"

# ---- 1. Broken hrefs (per audit) ----
HREF_FIXES = {
    SG / "Unit_6_Sequences_and_Series.html": [
        ("AP Calculus/Study Guides/Unit_10_Infinite_Sequences_and_Series.html",
         "AP Calculus/Study Guides/Unit_10_Sequences_and_Series.html"),
    ],
    SG / "Unit_8_Unit-Circle_Trig_and_Trigonometric_Functions.html": [
        ("AP Physics/Study Guides/Unit_6_Simple_Harmonic_Motion.html",
         "AP Physics/Study Guides/Unit_7_Oscillations.html"),
    ],
    SG / "Unit_9_Trigonometric_Identities_and_Equations.html": [
        ("AP Calculus/Study Guides/Unit_6_Integration_and_Accumulation_of_Change.html",
         "AP Calculus/Study Guides/Unit_6_Integration_Accumulation.html"),
    ],
    SG / "Unit_11_Combinatorics_and_the_Binomial_Theorem.html": [
        ("IB Math HL/Study Guides/Unit_A3_Counting_Principles_and_Binomial_Theorem.html",
         "IB Math HL/Study Guides/Unit_A3_Combinatorics.html"),
        ("AP CSA/Study Guides/Unit_2_Using_Objects.html",
         "AP CSA/Study Guides/Unit_1_Using_Objects_and_Methods.html"),
    ],
    SG / "Unit_12_Conic_Sections.html": [
        ("IB Math HL/Study Guides/Unit_B1_Functions_and_Equations.html",
         "IB Math HL/Study Guides/Unit_B1_Representation_of_Functions.html"),
        ("AP Calculus/Study Guides/Unit_9_Parametric_Equations_Polar_Coordinates_and_Vector-Valued_Functions.html",
         "AP Calculus/Study Guides/Unit_9_Parametric_Polar_and_Vectors.html"),
    ],
    SG / "Unit_13_Probability_and_Statistics_Foundations.html": [
        ("IB Math HL/Study Guides/Unit_D1_Counting_Probability_Statistics.html",
         "IB Math HL/Study Guides/Unit_D2_Probability.html"),
        ("AP CSA/Study Guides/Unit_2_Using_Objects.html",
         "AP CSA/Study Guides/Unit_2_Selection_and_Iteration.html"),
    ],
}

# ---- 3. Stale phrasing ----
# Each: (file, [(old, new), ...])
STALE_FIXES = {
    PQ / "Unit_5_Exponential_and_Logarithmic_Functions_Practice.html": [
        (" (forthcoming)", ""),
    ],
    PQ / "Unit_6_Sequences_and_Series_Practice.html": [
        (" (not yet published)", ""),
    ],
}


def main():
    summary = []

    # 1. Broken hrefs
    href_count = 0
    for path, fixes in HREF_FIXES.items():
        if not path.exists():
            summary.append(f"SKIP (missing): {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        before = text
        for old, new in fixes:
            text = text.replace(old, new)
        if text != before:
            path.write_text(text, encoding="utf-8")
            applied = sum(1 for o, _ in fixes if o in before)
            href_count += applied
            summary.append(f"HREF: {path.name} ({applied} fix(es))")
    summary.append(f"--- {href_count} href(s) fixed ---")

    # 2. Em-dash sweep — `&mdash;` to `,` corpus-wide on SG + PQ
    em_count = 0
    em_files = 0
    for d in (SG, PQ, PQ / "Solutions"):
        for p in d.glob("Unit_*.html"):
            text = p.read_text(encoding="utf-8")
            n = text.count("&mdash;")
            if n == 0:
                continue
            text = text.replace("&mdash;", ", ")
            p.write_text(text, encoding="utf-8")
            em_count += n
            em_files += 1
    summary.append(f"--- {em_count} &mdash; entities swept across {em_files} file(s) ---")

    # 3. Stale phrasing
    stale_count = 0
    for path, fixes in STALE_FIXES.items():
        if not path.exists():
            summary.append(f"SKIP (missing): {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        before = text
        for old, new in fixes:
            text = text.replace(old, new)
        if text != before:
            path.write_text(text, encoding="utf-8")
            stale_count += 1
            summary.append(f"STALE: {path.name}")
    summary.append(f"--- {stale_count} stale phrasing fix(es) ---")

    for line in summary:
        print(line)


if __name__ == "__main__":
    main()
