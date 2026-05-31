#!/usr/bin/env python3
"""Sprint 6 fix: 7 HS Math Solutions files (Units 8-15 minus 13) received
bilingual data-lang spans + the language toggle button during the Sprint 6 ZH
bulk pass, but the subagent never emitted the toggleLang() <script>. The button
is therefore dead and ZH content is unreachable. Insert the canonical toggle
script (identical to the working Units 1-7 Solutions and all 15 Practice files)
immediately before </body>. Idempotent: skips files that already define it.
Line endings are preserved (newline='')."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOL = ROOT / "High School Math" / "Practice Questions" / "Solutions"

TARGETS = [
    "Unit_8_Unit-Circle_Trig_and_Trigonometric_Functions_Solutions.html",
    "Unit_9_Trigonometric_Identities_and_Equations_Solutions.html",
    "Unit_10_Function_Transformations_and_Composition_Solutions.html",
    "Unit_11_Combinatorics_and_the_Binomial_Theorem_Solutions.html",
    "Unit_12_Conic_Sections_Solutions.html",
    "Unit_14_Vectors_Solutions.html",
    "Unit_15_Introduction_to_Limits_and_Calculus_Solutions.html",
]

SCRIPT = (
    "<script>\n"
    "function toggleLang() { const isZh = document.body.classList.toggle('lang-zh'); "
    "try { localStorage.setItem('lang', isZh ? 'zh' : 'en'); } catch (e) {} }\n"
    "try { if (localStorage.getItem('lang') === 'zh') document.body.classList.add('lang-zh'); } catch (e) {}\n"
    "</script>\n\n"
)

for name in TARGETS:
    p = SOL / name
    with open(p, "r", encoding="utf-8", newline="") as f:
        txt = f.read()
    nl = "\r\n" if "\r\n" in txt else "\n"
    script = SCRIPT.replace("\n", nl)
    if "function toggleLang" in txt:
        print(f"SKIP (already has toggle): {name}")
        continue
    if "toggleLang()" not in txt:
        print(f"WARN (no button calling toggleLang): {name}")
    if "</body>" not in txt:
        print(f"WARN (no </body>): {name}")
        continue
    # insert before the LAST </body>
    head, sep, tail = txt.rpartition("</body>")
    new = head + script + sep + tail
    # preserve original line endings
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    print(f"FIXED: {name}")
