#!/usr/bin/env python3
"""Regenerate the card grid and hero chips in index.html from the filesystem.

Source of truth is each Study Guide HTML file's <title> tag, which must follow:

    <title>{Subject Long} — {Prefix}: {Topic} | Dingrui Scholars</title>

The script walks <Subject>/Study Guides/*.html, parses each title, sorts the
units naturally (Unit 1 < Unit 2 < ... < Unit 10; Structure 1 < Reactivity 1;
Unit A < Unit A1 < Unit C), and writes cards into index.html between sentinel
comments:

    <!-- BEGIN cards:<SUBJECT_ID> -->
      <a class="card"> ... </a>
    <!-- END cards:<SUBJECT_ID> -->

The first run on a freshly-edited index.html inserts the sentinels by
locating each <h2 class="section-title">{Subject}</h2> followed by
<div class="grid">. Subsequent runs only swap content between sentinels.
Run with:

    python3 scripts/build-index.py
"""
import re
import sys
from html import escape, unescape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

# (directory, display name shown in <h2> and hero chip, chip CSS class)
SUBJECTS = [
    ("AP Calculus",     "AP Calculus AB/BC",          "chip-maroon"),
    ("AP Physics",      "AP Physics C: Mechanics", "chip-green"),
    ("IB Chemistry HL", "IB Chemistry HL",         "chip-purple"),
    ("AP CSA",          "AP Computer Science A",   "chip-gold"),
    ("IB Math HL",      "IB Math AA HL",           "chip-maroon"),
]

# When a subject mixes prefix words (e.g. IB Chemistry's Structure/Reactivity),
# alphabetical sort isn't the curriculum order. This map sets explicit ordering.
WORD_PRIORITY = {
    "IB Chemistry HL": {"Structure": 0, "Reactivity": 1, "Tools": 2},
}

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)


def parse_title(html_text: str):
    """Return (prefix, topic) or None.

    Expected: '{Subject} — {Prefix}: {Topic} | Dingrui Scholars'
    'Subject' itself may contain a colon (e.g. 'AP Physics C: Mechanics'),
    so we split on the em dash first.
    """
    m = TITLE_RE.search(html_text)
    if not m:
        return None
    t = unescape(m.group(1)).strip()
    if t.endswith(" | Dingrui Scholars"):
        t = t[: -len(" | Dingrui Scholars")]
    if " — " not in t:
        return None
    _, after = t.split(" — ", 1)
    if ":" not in after:
        return None
    prefix, topic = after.split(":", 1)
    return prefix.strip(), topic.strip()


def sort_key(prefix: str, subject_dir: str):
    parts = prefix.rsplit(" ", 1)
    word = parts[0] if len(parts) == 2 else ""
    tail = parts[-1]
    letter = re.sub(r"\d", "", tail)
    number = int(re.sub(r"\D", "", tail) or 0)
    word_pri = WORD_PRIORITY.get(subject_dir, {}).get(word, 0)
    return (word_pri, word, letter, number)


def card_num(prefix: str) -> str:
    """Zero-pad 'Unit 1' -> 'Unit 01' for AP courses. Don't pad IB Chem's
    'Structure 1' / 'Reactivity 1' (the original style was unpadded there)."""
    parts = prefix.rsplit(" ", 1)
    if len(parts) == 2 and parts[0] == "Unit" and parts[1].isdigit() and int(parts[1]) < 10:
        return f"{parts[0]} 0{parts[1]}"
    return prefix


def study_guides(subject_dir: str):
    sg = ROOT / subject_dir / "Study Guides"
    return sorted(sg.glob("*.html")) if sg.is_dir() else []


def gen_cards(subject_dir: str) -> str:
    items = []
    for f in study_guides(subject_dir):
        pt = parse_title(f.read_text(encoding="utf-8", errors="ignore"))
        if not pt:
            print(f"WARN: cannot parse <title> in {f.relative_to(ROOT)}", file=sys.stderr)
            continue
        prefix, topic = pt
        href = quote(f.relative_to(ROOT).as_posix(), safe="/")
        items.append((sort_key(prefix, subject_dir), prefix, topic, href))
    items.sort()
    lines = []
    for _, prefix, topic, href in items:
        lines.append(
            f'    <a class="card" href="{href}">\n'
            f'      <div class="card__num">{escape(card_num(prefix))}</div>\n'
            f'      <h3 class="card__title">{escape(topic).replace("&amp;", "&amp;")}</h3>\n'
            f'      <span class="card__arrow">Open guide →</span>\n'
            f"    </a>"
        )
    return "\n".join(lines)


def subject_marker(subject_dir: str) -> str:
    return "cards:" + re.sub(r"\W+", "_", subject_dir)


def ensure_sentinels(text: str) -> str:
    """Idempotently inject BEGIN/END sentinel comments into the card grids and
    the hero chip block, locating them via the <h2 class="section-title"> and
    <div class="hero-meta"> structural anchors.
    """
    for subject_dir, display, _css in SUBJECTS:
        marker = subject_marker(subject_dir)
        if f"<!-- BEGIN {marker} -->" in text:
            continue
        # Match the grid's closing </div> specifically — non-greedy on the body
        # but anchor the close on `</a>\s*</div>` so we don't catch an inner
        # `<div class="card__num">…</div>` by mistake.
        pat = re.compile(
            r'(<h2 class="section-title"[^>]*>'
            + re.escape(display)
            + r'</h2>\s*<div class="grid">)([\s\S]*?</a>\s*)(</div>)',
            re.DOTALL,
        )
        m = pat.search(text)
        if not m:
            sys.exit(f"FAIL: cannot find grid section for '{display}' in index.html")
        body = m.group(2).rstrip("\n ")
        replacement = (
            m.group(1)
            + f"\n    <!-- BEGIN {marker} -->"
            + body
            + f"\n    <!-- END {marker} -->\n  "
            + m.group(3)
        )
        text = text[: m.start()] + replacement + text[m.end():]
    return text


def replace_between(text: str, marker: str, body: str, body_indent: str = "    ") -> str:
    open_tag = f"<!-- BEGIN {marker} -->"
    close_tag = f"<!-- END {marker} -->"
    pat = re.compile(re.escape(open_tag) + r"[\s\S]*?" + re.escape(close_tag))
    repl = f"{open_tag}\n{body}\n{body_indent}{close_tag}"
    new_text, n = pat.subn(repl, text, count=1)
    if n != 1:
        sys.exit(f"FAIL: marker '{marker}' not found in index.html")
    return new_text


def main():
    text = INDEX.read_text(encoding="utf-8")
    text = ensure_sentinels(text)
    for subject_dir, _display, _css in SUBJECTS:
        text = replace_between(text, subject_marker(subject_dir), gen_cards(subject_dir))
    INDEX.write_text(text, encoding="utf-8")
    print(f"Wrote {INDEX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
