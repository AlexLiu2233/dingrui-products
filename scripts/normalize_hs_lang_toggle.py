#!/usr/bin/env python3
"""Deployment-audit fix (D1 + D4): normalize the language toggle across ALL High
School Study Guides to the canonical, locked form — NO localStorage, defaults to
English on load. Closes two audit findings in one sweep:
  - D4: 62 SGs used `localStorage` to persist language (violates the locked rule).
  - D1: 4 HS Math SGs (Units 2-5) had the toggle BUTTON but no `toggleLang()`
        function defined (dead button, ZH unreachable).

Canonical toggle:  function toggleLang() { document.body.classList.toggle('lang-zh'); }
No on-load localStorage restore -> every page opens in English.

Idempotent; preserves line endings (newline='')."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUBJECTS = ["High School Math", "High School Physics", "High School Chemistry",
            "High School Biology", "High School Computer Science"]
CANON = "function toggleLang() { document.body.classList.toggle('lang-zh'); }"

changed = skipped = injected = 0
for subj in SUBJECTS:
    d = ROOT / subj / "Study Guides"
    if not d.exists():
        continue
    for p in sorted(d.glob("*.html")):
        with open(p, "r", encoding="utf-8", newline="") as f:
            txt = f.read()
        nl = "\r\n" if "\r\n" in txt else "\n"
        before = txt
        lines = txt.split(nl)
        out = []
        for ln in lines:
            if "localStorage.getItem('lang')" in ln:
                continue  # drop the on-load restore line -> defaults English
            if "function toggleLang()" in ln and "localStorage.setItem" in ln:
                # preserve leading indentation, swap the body for the canonical one
                indent = ln[:len(ln) - len(ln.lstrip())]
                out.append(indent + CANON)
                continue
            out.append(ln)
        txt = nl.join(out)
        # 4 dead files: function missing entirely -> inject before the last </body>
        if "function toggleLang" not in txt:
            inject = "<script>" + nl + CANON + nl + "</script>" + nl + nl
            head, sep, tail = txt.rpartition("</body>")
            txt = head + inject + sep + tail
            injected += 1
        if txt != before:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(txt)
            # sanity: no localStorage left, function present
            assert "localStorage" not in txt, p
            assert "function toggleLang" in txt, p
            changed += 1
            print(f"FIXED   {p.relative_to(ROOT)}")
        else:
            skipped += 1
            print(f"SKIP    {p.relative_to(ROOT)} (already canonical)")

print(f"\n{changed} changed ({injected} had function injected), {skipped} already canonical")
