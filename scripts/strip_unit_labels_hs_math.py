#!/usr/bin/env python3
"""
HS Math: Drop the visible "Unit N" chrome from Units 1-6 files.

Convention locked 2026-05-27: filename keeps Unit_N_ for sort/link stability;
every VISIBLE "Unit N" / "UNIT N" / "N.X" label is stripped.

Touches 18 files: 6 Study Guides + 6 Practice + 6 Solutions.

Transformations (per file):
  1. <title>: strip "Unit N: "
  2. <meta description>: strip "Unit N: " or " Unit N "
  3. Hero <h1>: strip "Unit N: " prefix, drop optional <br> right after
  4. Hero chip "Unit N of 15": delete the whole <span>
  5. Nav badge UNIT N -> topic code from mapping
  6. Sidebar TOC visible text "N.X Topic" -> "Topic" (anchor stays)
  7. Section labels "Section N.X" -> "Section X"
  8. Worked Example labels "Worked Example N.X" -> "Worked Example X"
  9. Quiz numbers "N.X &middot; Q?" -> "&sect;X &middot; Q?"
 10. Cross-section refs "&sect;N.X" -> "&sect;X" (and "N.X-N.Y" / "N.X-Y" cases)
 11. Footer "Unit N: ..." -> drop the unit prefix
 12. Practice / Solutions chapter-tag "Unit N &middot; Practice/Solutions" -> just "Practice"/"Solutions"
 13. Practice / Solutions footer "Unit N Practice/Solutions" -> "Practice/Solutions"
 14. Quiz heading "Unit N Practice Quiz" -> "Practice Quiz"
"""

import os
import re
import sys
import subprocess

ROOT = r'C:/Users/liujp/OneDrive/Desktop/SWE/dingrui-products'
HSM = os.path.join(ROOT, 'High School Math')

TOPIC_CODE = {
    1: 'LINEAR',
    2: 'QUADRATIC',
    3: 'POLY',
    4: 'RATIONAL',
    5: 'EXP / LOG',
    6: 'SEQUENCES',
}

FILES = [
    'Study Guides/Unit_1_Linear_Functions_and_Systems.html',
    'Study Guides/Unit_2_Quadratic_Functions_and_Equations.html',
    'Study Guides/Unit_3_Polynomial_Functions.html',
    'Study Guides/Unit_4_Rational_and_Radical_Expressions.html',
    'Study Guides/Unit_5_Exponential_and_Logarithmic_Functions.html',
    'Study Guides/Unit_6_Sequences_and_Series.html',
    'Practice Questions/Unit_1_Linear_Functions_and_Systems_Practice.html',
    'Practice Questions/Unit_2_Quadratic_Functions_and_Equations_Practice.html',
    'Practice Questions/Unit_3_Polynomial_Functions_Practice.html',
    'Practice Questions/Unit_4_Rational_and_Radical_Expressions_Practice.html',
    'Practice Questions/Unit_5_Exponential_and_Logarithmic_Functions_Practice.html',
    'Practice Questions/Unit_6_Sequences_and_Series_Practice.html',
    'Practice Questions/Solutions/Unit_1_Linear_Functions_and_Systems_Solutions.html',
    'Practice Questions/Solutions/Unit_2_Quadratic_Functions_and_Equations_Solutions.html',
    'Practice Questions/Solutions/Unit_3_Polynomial_Functions_Solutions.html',
    'Practice Questions/Solutions/Unit_4_Rational_and_Radical_Expressions_Solutions.html',
    'Practice Questions/Solutions/Unit_5_Exponential_and_Logarithmic_Functions_Solutions.html',
    'Practice Questions/Solutions/Unit_6_Sequences_and_Series_Solutions.html',
]


def transform(text: str, n: int) -> str:
    """Apply all 14 transformations for a specific Unit N file."""
    code = TOPIC_CODE[n]
    N = str(n)

    # --- 1. <title> tag ---
    text = re.sub(
        rf'(<title>[^<]*?)\bUnit {N}: ',
        r'\1',
        text,
    )

    # --- 2. <meta description> --- two flavors observed:
    #     (a) 'High School Math Unit 1: Linear Functions ...'  -> drop 'Unit N: '
    #     (b) ' Unit N ' standalone (unlikely but safe)
    text = re.sub(
        rf'(<meta name="description"[^>]*?content="[^"]*?)\bUnit {N}: ',
        r'\1',
        text,
    )
    text = re.sub(
        rf'(<meta name="description"[^>]*?content="[^"]*?) Unit {N} ',
        r'\1 ',
        text,
    )

    # --- 3. Hero <h1>: "Unit N: Topic<br>Rest"  ->  "Topic<br>Rest" (br preserved)
    #     Some have "Unit N: Topic</h1>" (no <br>) -> simpler form.
    #     Drop the "Unit N: " prefix. Keep the rest, including any <br>.
    text = re.sub(
        rf'(<h1[^>]*>)Unit {N}: ',
        r'\1',
        text,
    )

    # --- 4. Hero "Unit N of 15" chip --- delete whole span (and any leading whitespace + newline)
    text = re.sub(
        rf'\s*<span class="chip chip-maroon">Unit {N} of 15</span>\n?',
        '\n',
        text,
    )

    # --- 5. Nav badge: <span class="nav-badge">UNIT N</span>  ->  topic code
    text = re.sub(
        rf'(<span class="nav-badge">)UNIT {N}(</span>)',
        rf'\1{code}\2',
        text,
    )

    # --- 6. Sidebar TOC: <a href="#s-N-X">N.X Topic</a>  ->  <a href="#s-N-X">Topic</a>
    #     Only strip the leading "N.X " (where X is one digit). Anchor stays intact.
    text = re.sub(
        rf'(<a href="#s-{N}-(\d)">){N}\.\2 ',
        r'\1',
        text,
    )

    # --- 7. Section labels: "Section N.X &middot;"  ->  "Section X &middot;"
    text = re.sub(
        rf'\bSection {N}\.(\d)\b',
        r'Section \1',
        text,
    )

    # --- 8. Worked Example labels: "Worked Example N.X"  ->  "Worked Example X"
    text = re.sub(
        rf'\bWorked Example {N}\.(\d)\b',
        r'Worked Example \1',
        text,
    )

    # --- 9. Quiz numbers: "N.X &middot; Q?"  ->  "&sect;X &middot; Q?"
    #     The reference Unit 7 uses '&sect;X &middot; Q?' format.
    text = re.sub(
        rf'\b{N}\.(\d) &middot; Q',
        r'&sect;\1 &middot; Q',
        text,
    )

    # --- 10. Cross-section refs ---
    #     (a) "&sect;N.X-N.Y"  ->  "&sect;X-Y" (range with both halves N-prefixed)
    text = re.sub(
        rf'&sect;{N}\.(\d)-{N}\.(\d)',
        r'&sect;\1-\2',
        text,
    )
    #     (b) "&sect;N.X-Y"  (range with only the second half a bare digit, e.g. &sect;1.5-7)
    text = re.sub(
        rf'&sect;{N}\.(\d)-(\d)\b',
        r'&sect;\1-\2',
        text,
    )
    #     (c) "&sect;N.X"  ->  "&sect;X"  (single ref)
    text = re.sub(
        rf'&sect;{N}\.(\d)',
        r'&sect;\1',
        text,
    )

    # --- 11. Footer: "High School Math &middot; Unit N: <Topic> &middot; v1" -> drop "Unit N: "
    text = re.sub(
        rf'(High School Math &middot; )Unit {N}: ',
        r'\1',
        text,
    )

    # --- 12. Practice/Solutions chapter-tag: "Unit N &middot; Practice/Solutions"
    text = re.sub(
        rf'<div class="chapter-tag">Unit {N} &middot; (Practice|Solutions)</div>',
        r'<div class="chapter-tag">\1</div>',
        text,
    )

    # --- 13. Practice/Solutions footer: "Unit N Practice/Solutions" -> just "Practice/Solutions"
    text = re.sub(
        rf'\bUnit {N} (Practice|Solutions)\b',
        r'\1',
        text,
    )

    # --- 14. Quiz heading: "Unit N Practice Quiz" -> "Practice Quiz"
    # (already covered by #13 since "Unit N Practice" is the match — but Quiz heading is
    # "Unit N Practice Quiz", which the #13 substitution turns into "Practice Quiz". Good.)

    return text


def main():
    report = []
    overall_bytes_removed = 0
    for rel in FILES:
        path = os.path.join(HSM, rel.replace('/', os.sep))
        fname = os.path.basename(path)
        m = re.match(r'Unit_(\d+)_', fname)
        if not m:
            report.append((rel, 'SKIP: cannot parse unit number', 0, 0))
            continue
        n = int(m.group(1))
        if n not in TOPIC_CODE:
            report.append((rel, f'SKIP: unit {n} not in mapping', 0, 0))
            continue

        with open(path, 'r', encoding='utf-8') as f:
            before = f.read()
        after = transform(before, n)

        size_before = len(before.encode('utf-8'))
        size_after  = len(after.encode('utf-8'))
        delta = size_before - size_after
        overall_bytes_removed += delta

        if before == after:
            report.append((rel, 'NO-OP', size_before, 0))
            continue

        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(after)

        # Count line diff
        line_before = before.count('\n')
        line_after  = after.count('\n')
        report.append((rel, 'OK', size_before, delta, line_before - line_after))

    print('\n=== REFACTOR REPORT ===')
    for row in report:
        if len(row) == 5:
            rel, status, sz, db, dl = row
            print(f'  {status:6}  {db:+6} bytes  {dl:+3} lines  {rel}')
        else:
            rel, status, sz, db = row
            print(f'  {status:6}  {db:+6} bytes              {rel}')
    print(f'\nTotal bytes removed: {overall_bytes_removed}')
    print(f'Files modified: {sum(1 for r in report if r[1] == "OK")} / {len(FILES)}')


if __name__ == '__main__':
    main()
