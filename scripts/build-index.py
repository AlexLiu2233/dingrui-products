#!/usr/bin/env python3
"""Regenerate the card grid and hero chips in index.html from the filesystem.

Source of truth is each Study Guide HTML file's <title> tag, which must follow:

    <title>{Subject Long} — {Prefix}: {Topic} | Dingrui Scholars</title>

The Mandarin card title is pulled from the first `<h1>...<span data-lang="zh">...</span>...</h1>`
in the body. If the file has no `data-lang="zh"` markers at all, the card is
tagged `data-zh-ready="false"` and the landing page CSS hides it when the
ZH toggle is on.

The script walks <Subject>/Study Guides/*.html, parses each title, sorts the
units naturally (Unit 1 < Unit 2 < ... < Unit 10; Structure 1 < Reactivity 1;
Unit A < Unit A1 < Unit C), and writes cards into index.html between sentinel
comments:

    <!-- BEGIN cards:<SUBJECT_ID> -->
      <a class="card"> ... </a>
    <!-- END cards:<SUBJECT_ID> -->

For subjects listed in GROUP_BY_LETTER, the inside of the sentinel block
is instead a stack of `<details class="super-topic">` accordions, one per
leading-letter group (e.g. IB Math AA HL → A / B / C / D / E).

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

# (directory, display name shown in card chrome, chip CSS class)
SUBJECTS = [
    ("AP Calculus",      "AP Calculus AB/BC",       "chip-maroon"),
    ("AP Physics",       "AP Physics C: Mechanics", "chip-green"),
    ("IB Chemistry HL",  "IB Chemistry HL",         "chip-purple"),
    ("AP CSA",           "AP Computer Science A",   "chip-gold"),
    ("IB Math HL",       "IB Math AA HL",           "chip-maroon"),
    ("IB Physics HL",    "IB Physics HL",           "chip-green"),
    ("High School Math", "High School Math",        "chip-maroon"),
    ("High School Physics", "High School Physics",   "chip-green"),
    ("High School Chemistry", "High School Chemistry", "chip-purple"),
    ("High School Biology", "High School Biology",   "chip-gold"),
    ("High School Computer Science", "High School Computer Science", "chip-green"),
    ("University Calculus", "University Calculus",   "chip-maroon"),
]

# When a subject mixes prefix words (e.g. IB Chemistry's Structure/Reactivity),
# alphabetical sort isn't the curriculum order. This map sets explicit ordering.
WORD_PRIORITY = {
    "IB Chemistry HL": {"Structure": 0, "Reactivity": 1, "Tools": 2},
}

# Subjects whose units sub-group into super-topics (A1..A5, B1..B5, ...).
# Each entry maps the leading letter to (EN super-topic name, ZH super-topic name).
GROUP_BY_LETTER = {
    "IB Math HL": {
        "A": ("Algebra",                    "代数"),
        "B": ("Functions",                  "函数"),
        "C": ("Geometry & Trigonometry",    "几何与三角"),
        "D": ("Statistics & Probability",   "统计与概率"),
        "E": ("Calculus",                   "微积分"),
    },
    "University Calculus": {
        "A": ("Calculus I: Differential Calculus",   "微积分一 · 微分"),
        "B": ("Calculus II: Integral Calculus & Series", "微积分二 · 积分与级数"),
        "C": ("Calculus III: Multivariable & Vector", "微积分三 · 多元与向量"),
        "D": ("Calculus IV: Differential Equations", "微积分四 · 微分方程"),
    },
}

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)
# Two ZH hero patterns in the codebase:
#   (1) <h1><span data-lang="en">…</span><span data-lang="zh">…</span></h1>
#       — used by AP Calc / AP Physics / IB Chem HL / IB Math HL / IB Physics HL
#   (2) <h1 data-lang="en">…</h1><h1 data-lang="zh">…</h1>
#       — used by AP CSA
H1_ZH_DIRECT_RE = re.compile(r'<h1[^>]*data-lang="zh"[^>]*>(.*?)</h1>',
                             re.IGNORECASE | re.DOTALL)
H1_GENERIC_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
ZH_SPAN_RE = re.compile(r'<span[^>]*data-lang="zh"[^>]*>(.*?)</span>',
                        re.IGNORECASE | re.DOTALL)


def parse_title(html_text: str, file_path=None):
    """Return (prefix, topic) or None.

    Two title formats are supported:

    1. '{Subject} — {Prefix}: {Topic} | Dingrui Scholars' (canonical;
       used by AP / IB subjects where the prefix maps to a curriculum-
       defined unit identifier).
    2. '{Subject} — {Topic} | Dingrui Scholars' (HS Math convention
       locked 2026-05-27 — topic-organised subject, no "Unit N:" in the
       visible title). When no colon is present, the prefix is
       synthesised from the filename's `Unit_N_…` prefix so sort order
       and ZH chrome still work.

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
    if ":" in after:
        prefix, topic = after.split(":", 1)
        return prefix.strip(), topic.strip()
    # No-colon fallback for the topic-organised convention: derive prefix
    # from filename if it follows the `Unit_N_…` shape.
    if file_path is not None:
        m_unit = re.match(r"Unit_(\d+)_", file_path.name)
        if m_unit:
            return f"Unit {m_unit.group(1)}", after.strip()
    return None


def parse_zh_topic(html_text: str):
    """Pull ZH hero text from the first matching pattern.

    Two patterns supported (see H1_ZH_DIRECT_RE / H1_GENERIC_RE).
    Returns the ZH text after stripping inner tags and whitespace.
    Returns None if the file has no ZH markers at all.
    """
    if 'data-lang="zh"' not in html_text:
        return None
    body_start = html_text.lower().find("<body")
    body = html_text[body_start:] if body_start != -1 else html_text
    # Pattern 2 first: <h1 data-lang="zh">…</h1>
    direct = H1_ZH_DIRECT_RE.search(body)
    if direct:
        inner = direct.group(1)
    else:
        # Pattern 1: <h1>…<span data-lang="zh">…</span>…</h1>
        h1 = H1_GENERIC_RE.search(body)
        if not h1:
            return None
        zh = ZH_SPAN_RE.search(h1.group(1))
        if not zh:
            return None
        inner = zh.group(1)
    text = re.sub(r"<[^>]+>", "", inner)
    text = unescape(text).strip()
    text = re.sub(r"\s+", "", text)
    return text or None


def split_zh_topic(zh: str, prefix: str):
    """Given a full ZH hero title like '单元 A1：数列与级数' or '反应性 1：…',
    strip the unit prefix and the colon, returning just the topic part."""
    if not zh:
        return None
    # Common separators in ZH: '：' (fullwidth colon) and ':'
    for sep in ("：", ":"):
        if sep in zh:
            return zh.split(sep, 1)[1].strip()
    return zh


def sort_key(prefix: str, subject_dir: str):
    parts = prefix.rsplit(" ", 1)
    word = parts[0] if len(parts) == 2 else ""
    tail = parts[-1]
    letter = re.sub(r"\d", "", tail)
    number = int(re.sub(r"\D", "", tail) or 0)
    word_pri = WORD_PRIORITY.get(subject_dir, {}).get(word, 0)
    return (word_pri, word, letter, number)


def card_num(prefix: str) -> tuple:
    """Return (en, zh) labels for the card__num chip.

    Zero-pad 'Unit 1' -> 'Unit 01' for AP courses; leave letter-prefix
    units ('Unit A1') unpadded; leave IB Chem's 'Structure 1' / 'Reactivity 1'
    unpadded (the original style).
    """
    parts = prefix.rsplit(" ", 1)
    if len(parts) == 2 and parts[0] == "Unit" and parts[1].isdigit() and int(parts[1]) < 10:
        en = f"{parts[0]} 0{parts[1]}"
        zh = f"第 0{parts[1]} 单元"
    elif len(parts) == 2 and parts[0] == "Unit":
        # Unit A1, Unit B2, Unit C, etc. — keep tail verbatim, ZH wraps with 单元.
        en = prefix
        zh = f"单元 {parts[1]}"
    elif len(parts) == 2 and parts[0] == "Structure":
        en = prefix
        zh = f"结构 {parts[1]}"
    elif len(parts) == 2 and parts[0] == "Reactivity":
        en = prefix
        zh = f"反应性 {parts[1]}"
    else:
        en = prefix
        zh = prefix
    return en, zh


def super_topic_letter(prefix: str) -> str:
    """Return 'A' for 'Unit A1', 'B' for 'Unit B2', 'C' for 'Unit C', etc.
    Returns '' if the prefix tail has no leading letter."""
    parts = prefix.rsplit(" ", 1)
    if len(parts) != 2:
        return ""
    tail = parts[1]
    letters = re.match(r"^([A-Z])", tail)
    return letters.group(1) if letters else ""


def study_guides(subject_dir: str):
    sg = ROOT / subject_dir / "Study Guides"
    return sorted(sg.glob("*.html")) if sg.is_dir() else []


def render_card(prefix, topic_en, topic_zh, href, zh_ready) -> str:
    en_num, zh_num = card_num(prefix)
    if topic_zh:
        title_block = (
            f'      <h3 class="card__title">'
            f'<span data-lang="en">{escape(topic_en)}</span>'
            f'<span data-lang="zh">{escape(topic_zh)}</span>'
            f'</h3>\n'
        )
    else:
        # ZH title not extractable — fall back to EN both sides.
        title_block = f'      <h3 class="card__title">{escape(topic_en)}</h3>\n'
    zh_attr = "" if zh_ready else ' data-zh-ready="false"'
    return (
        f'    <a class="card"{zh_attr} href="{href}">\n'
        f'      <div class="card__num">'
        f'<span data-lang="en">{escape(en_num)}</span>'
        f'<span data-lang="zh">{escape(zh_num)}</span>'
        f'</div>\n'
        f'{title_block}'
        f'      <span class="card__arrow">'
        f'<span data-lang="en">Open guide →</span>'
        f'<span data-lang="zh">查看指南 →</span>'
        f'</span>\n'
        f"    </a>"
    )


def gather_items(subject_dir: str):
    """Returns list of (sort_key, prefix, topic_en, topic_zh, href, zh_ready)."""
    items = []
    for f in study_guides(subject_dir):
        text = f.read_text(encoding="utf-8", errors="ignore")
        pt = parse_title(text, f)
        if not pt:
            print(f"WARN: cannot parse <title> in {f.relative_to(ROOT)}", file=sys.stderr)
            continue
        prefix, topic_en = pt
        zh_full = parse_zh_topic(text)
        topic_zh = split_zh_topic(zh_full, prefix) if zh_full else None
        zh_ready = "data-lang=\"zh\"" in text
        href = quote(f.relative_to(ROOT).as_posix(), safe="/")
        items.append((sort_key(prefix, subject_dir), prefix, topic_en, topic_zh, href, zh_ready))
    items.sort()
    return items


def gen_cards_flat(subject_dir: str) -> str:
    items = gather_items(subject_dir)
    return "\n".join(render_card(p, te, tz, h, z) for _, p, te, tz, h, z in items)


def gen_cards_grouped(subject_dir: str) -> str:
    """Emit one <details class="super-topic"> block per leading-letter group."""
    items = gather_items(subject_dir)
    groups = GROUP_BY_LETTER[subject_dir]
    # Bucket by letter; preserve item order within each bucket.
    buckets = {letter: [] for letter in groups}
    misc = []
    for entry in items:
        _, prefix, *_ = entry
        letter = super_topic_letter(prefix)
        if letter in buckets:
            buckets[letter].append(entry)
        else:
            misc.append(entry)
    out = []
    for letter, (name_en, name_zh) in groups.items():
        bucket = buckets[letter]
        if not bucket:
            continue
        count = len(bucket)
        out.append(
            f'      <details class="super-topic">\n'
            f'        <summary class="super-topic__toggle">\n'
            f'          <span class="super-topic__chevron" aria-hidden="true">&rsaquo;</span>\n'
            f'          <span class="super-topic__letter">{letter}</span>\n'
            f'          <span class="super-topic__title">'
            f'<span data-lang="en">{escape(name_en)}</span>'
            f'<span data-lang="zh">{escape(name_zh)}</span>'
            f'</span>\n'
            f'          <span class="super-topic__count">'
            f'<span data-lang="en">{count} unit{"s" if count != 1 else ""}</span>'
            f'<span data-lang="zh">{count} 个单元</span>'
            f'</span>\n'
            f'        </summary>\n'
            f'        <div class="super-topic__body">\n'
            f'          <div class="grid">\n'
            + "\n".join(render_card(p, te, tz, h, z) for _, p, te, tz, h, z in bucket)
            + "\n          </div>\n"
            f'        </div>\n'
            f'      </details>'
        )
    # Misc cards (legacy Unit_C_Geometry.html etc.) sit at the bottom outside the groups.
    if misc:
        out.append(
            f'      <div class="grid super-topic__misc">\n'
            + "\n".join(render_card(p, te, tz, h, z) for _, p, te, tz, h, z in misc)
            + "\n      </div>"
        )
    return "\n".join(out)


def gen_cards(subject_dir: str) -> str:
    if subject_dir in GROUP_BY_LETTER:
        return gen_cards_grouped(subject_dir)
    return gen_cards_flat(subject_dir)


def subject_marker(subject_dir: str) -> str:
    return "cards:" + re.sub(r"\W+", "_", subject_dir)


def ensure_sentinels(text: str) -> str:
    """Idempotently inject BEGIN/END sentinel comments into the card grids.
    Supports two structural anchors:
      1. Legacy `<h2 class="section-title">{display}</h2><div class="grid">`
      2. Tiered `<span class="subject-group__title">{display}</span>` inside a
         `<details class="subject-group">` block, with `<div class="grid">`
         nested under `<div class="subject-group__body">`.
    """
    for subject_dir, display, _css in SUBJECTS:
        marker = subject_marker(subject_dir)
        if f"<!-- BEGIN {marker} -->" in text:
            continue
        # Try legacy pattern first.
        pat_legacy = re.compile(
            r'(<h2 class="section-title"[^>]*>'
            + re.escape(display)
            + r'</h2>\s*<div class="grid">)([\s\S]*?</a>\s*)(</div>)',
            re.DOTALL,
        )
        m = pat_legacy.search(text)
        if not m:
            # Tiered pattern (subject-group with inner grid).
            pat_tiered = re.compile(
                r'(<span class="subject-group__title">'
                + re.escape(display)
                + r'</span>[\s\S]*?<div class="grid">)([\s\S]*?)(</div>)',
                re.DOTALL,
            )
            m = pat_tiered.search(text)
        if not m:
            sys.exit(f"FAIL: cannot find grid section for '{display}' in index.html")
        body = m.group(2).rstrip("\n ")
        replacement = (
            m.group(1)
            + f"\n        <!-- BEGIN {marker} -->"
            + body
            + f"\n        <!-- END {marker} -->\n      "
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
