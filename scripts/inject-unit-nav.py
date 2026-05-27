#!/usr/bin/env python3
"""Inject (idempotently) a Previous / Next unit-nav widget into every Study
Guide HTML, so a student reading Unit A1 can advance to A2 without going back
to the landing page.

Order is the same natural sort used by `build-index.py` (so A1 < A2 < ... <
A5 < B1 < ... < E6 for IB Math HL; Unit 1 < ... < Unit 10 for AP Calc; etc.).
Prev / next links across super-topic boundaries: A5's next is B1, E5's next
is E6 (the last unit in the subject has no next).

Two markers wrap the injected HTML (idempotent on re-run):
    <!-- BEGIN unit-nav --> ... <!-- END unit-nav -->

The CSS lives in a paired marker block:
    <!-- BEGIN unit-nav-css --> ... <!-- END unit-nav-css -->

Run with:
    python3 scripts/inject-unit-nav.py
"""
import re
import sys
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

# Subjects to process. HS Math is excluded (English-only spec).
SUBJECTS = [
    "AP Calculus",
    "AP Physics",
    "IB Chemistry HL",
    "AP CSA",
    "IB Math HL",
    "IB Physics HL",
]

# Re-imported from build-index.py logic. Keep these in sync if you change one.
WORD_PRIORITY = {
    "IB Chemistry HL": {"Structure": 0, "Reactivity": 1, "Tools": 2},
}

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)
H1_ZH_DIRECT_RE = re.compile(r'<h1[^>]*data-lang="zh"[^>]*>(.*?)</h1>',
                             re.IGNORECASE | re.DOTALL)
H1_GENERIC_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
ZH_SPAN_RE = re.compile(r'<span[^>]*data-lang="zh"[^>]*>(.*?)</span>',
                        re.IGNORECASE | re.DOTALL)

NAV_CSS = """
<!-- BEGIN unit-nav-css -->
<style data-section="unit-nav">
.unit-nav {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  max-width: 980px;
  margin: 64px auto 32px;
  padding: 0 24px;
}
.unit-nav__link {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  padding: 18px 20px;
  background: var(--bg-card, #fff);
  border: 1px solid var(--border, #DDD0C8);
  border-radius: 12px;
  color: inherit;
  transition: transform 0.18s, border-color 0.18s, box-shadow 0.18s;
}
.unit-nav__link:hover {
  transform: translateY(-2px);
  border-color: var(--accent, #7A2E2E);
  box-shadow: 0 6px 16px -4px rgba(60, 20, 30, 0.12);
}
.unit-nav__link--next {
  flex-direction: row-reverse;
  text-align: right;
}
.unit-nav__arrow {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--accent, #7A2E2E);
  line-height: 1;
  flex: 0 0 auto;
}
.unit-nav__body { display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.unit-nav__hint {
  font-family: var(--font-mono, 'JetBrains Mono', monospace);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  color: var(--text-secondary, #6B5058);
}
.unit-nav__title {
  font-family: var(--font-display, 'DM Serif Display', Georgia, serif);
  font-style: italic;
  font-weight: 400;
  font-size: 1.05rem;
  line-height: 1.25;
  color: var(--text, #2C1B1F);
}
.unit-nav__placeholder {
  border: 1px dashed var(--border, #DDD0C8);
  border-radius: 12px;
  background: transparent;
  opacity: 0.6;
}
@media (max-width: 640px) {
  .unit-nav { grid-template-columns: 1fr; gap: 10px; margin-top: 48px; }
  .unit-nav__link--next { flex-direction: row; text-align: left; }
}
@media print { .unit-nav { display: none; } }
</style>
<!-- END unit-nav-css -->
""".strip()


def parse_title(html_text: str):
    m = TITLE_RE.search(html_text)
    if not m:
        return None
    t = m.group(1).strip()
    if t.endswith(" | Dingrui Scholars"):
        t = t[: -len(" | Dingrui Scholars")]
    if " — " not in t:
        return None
    _, after = t.split(" — ", 1)
    if ":" not in after:
        return None
    prefix, topic = after.split(":", 1)
    return prefix.strip(), topic.strip()


def parse_zh_topic(html_text: str):
    if 'data-lang="zh"' not in html_text:
        return None
    body_start = html_text.lower().find("<body")
    body = html_text[body_start:] if body_start != -1 else html_text
    direct = H1_ZH_DIRECT_RE.search(body)
    if direct:
        inner = direct.group(1)
    else:
        h1 = H1_GENERIC_RE.search(body)
        if not h1:
            return None
        zh = ZH_SPAN_RE.search(h1.group(1))
        if not zh:
            return None
        inner = zh.group(1)
    text = re.sub(r"<[^>]+>", "", inner)
    text = text.strip()
    text = re.sub(r"\s+", "", text)
    return text or None


def split_zh_topic(zh):
    if not zh:
        return None
    for sep in ("：", ":"):
        if sep in zh:
            return zh.split(sep, 1)[1].strip()
    return zh


def sort_key(prefix, subject_dir):
    parts = prefix.rsplit(" ", 1)
    word = parts[0] if len(parts) == 2 else ""
    tail = parts[-1]
    letter = re.sub(r"\d", "", tail)
    number = int(re.sub(r"\D", "", tail) or 0)
    word_pri = WORD_PRIORITY.get(subject_dir, {}).get(word, 0)
    return (word_pri, word, letter, number)


def short_prefix_zh(prefix):
    """Mandarin equivalent of e.g. 'Unit A1' -> '单元 A1'; 'Structure 1' ->
    '结构 1'; 'Reactivity 2' -> '反应性 2'; 'Unit 5' -> '第 5 单元'."""
    parts = prefix.rsplit(" ", 1)
    if len(parts) != 2:
        return prefix
    head, tail = parts
    if head == "Unit" and tail.isdigit():
        return f"第 {tail} 单元"
    if head == "Unit":
        return f"单元 {tail}"
    if head == "Structure":
        return f"结构 {tail}"
    if head == "Reactivity":
        return f"反应性 {tail}"
    return prefix


def gather_units(subject_dir):
    sg = ROOT / subject_dir / "Study Guides"
    if not sg.is_dir():
        return []
    items = []
    for f in sorted(sg.glob("*.html")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        pt = parse_title(text)
        if not pt:
            print(f"WARN: cannot parse <title> in {f.relative_to(ROOT)}", file=sys.stderr)
            continue
        prefix, topic_en = pt
        zh_full = parse_zh_topic(text)
        topic_zh = split_zh_topic(zh_full)
        items.append((sort_key(prefix, subject_dir), f, prefix, topic_en, topic_zh))
    items.sort()
    return items


def render_link(direction, target):
    """direction is 'prev' or 'next'. target is an (filepath, prefix, topic_en, topic_zh)
    tuple or None (boundary)."""
    if target is None:
        return f'  <div class="unit-nav__placeholder unit-nav__link unit-nav__link--{direction}" aria-hidden="true"></div>'
    f, prefix, topic_en, topic_zh = target
    href = quote(f.name)
    arrow = "&larr;" if direction == "prev" else "&rarr;"
    hint_en = "Previous unit" if direction == "prev" else "Next unit"
    hint_zh = "上一单元" if direction == "prev" else "下一单元"
    if topic_zh:
        title_html = (
            f'<span data-lang="en">{escape(prefix)}: {escape(topic_en)}</span>'
            f'<span data-lang="zh">{escape(short_prefix_zh(prefix))}：{escape(topic_zh)}</span>'
        )
    else:
        title_html = f'{escape(prefix)}: {escape(topic_en)}'
    return (
        f'  <a class="unit-nav__link unit-nav__link--{direction}" href="{href}">\n'
        f'    <span class="unit-nav__arrow" aria-hidden="true">{arrow}</span>\n'
        f'    <span class="unit-nav__body">\n'
        f'      <span class="unit-nav__hint">'
        f'<span data-lang="en">{hint_en}</span>'
        f'<span data-lang="zh">{hint_zh}</span>'
        f'</span>\n'
        f'      <span class="unit-nav__title">{title_html}</span>\n'
        f'    </span>\n'
        f'  </a>'
    )


def render_nav(prev_target, next_target):
    return (
        '<!-- BEGIN unit-nav -->\n'
        '<nav class="unit-nav" aria-label="Course navigation">\n'
        + render_link("prev", prev_target) + "\n"
        + render_link("next", next_target) + "\n"
        + '</nav>\n'
        '<!-- END unit-nav -->'
    )


NAV_BLOCK_RE = re.compile(
    r"<!-- BEGIN unit-nav -->[\s\S]*?<!-- END unit-nav -->\n?",
    re.IGNORECASE,
)
NAV_CSS_BLOCK_RE = re.compile(
    r"<!-- BEGIN unit-nav-css -->[\s\S]*?<!-- END unit-nav-css -->\n?",
    re.IGNORECASE,
)


FOOTER_WRAP_RE = re.compile(r'(<div\s+class="footer-wrap")', re.IGNORECASE)
MAIN_CLOSE_RE = re.compile(r'(</main\s*>)', re.IGNORECASE)


def inject_nav(text, nav_block, css_block):
    # Strip any existing nav block first so the new one always lands at the
    # preferred location (inside .main-wrap, before .footer-wrap).
    text = NAV_BLOCK_RE.sub("", text)
    # Preferred: before the footer-wrap brand block (keeps nav inside .main-wrap
    # so it lines up with the article column, not the fixed sidebar).
    m = FOOTER_WRAP_RE.search(text)
    if m:
        text = text[:m.start()] + nav_block + "\n\n" + text[m.start():]
    else:
        # Fallback: just before </main>.
        m = MAIN_CLOSE_RE.search(text)
        if m:
            text = text[:m.start()] + nav_block + "\n" + text[m.start():]
        else:
            close = text.lower().rfind("</body>")
            if close == -1:
                print("WARN: no </body> tag found; appending nav at EOF", file=sys.stderr)
                text = text.rstrip() + "\n\n" + nav_block + "\n"
            else:
                text = text[:close] + nav_block + "\n" + text[close:]
    if NAV_CSS_BLOCK_RE.search(text):
        text = NAV_CSS_BLOCK_RE.sub(css_block + "\n", text, count=1)
    else:
        close_head = text.lower().rfind("</head>")
        if close_head == -1:
            print("WARN: no </head> tag found; CSS not injected", file=sys.stderr)
        else:
            text = text[:close_head] + css_block + "\n" + text[close_head:]
    return text


def process_subject(subject_dir):
    items = gather_units(subject_dir)
    if not items:
        print(f"  [skip] {subject_dir} — no units")
        return 0
    if len(items) == 1:
        print(f"  [skip] {subject_dir} — only 1 unit, no nav meaningful")
        return 0
    n = 0
    for i, item in enumerate(items):
        _, f, prefix, topic_en, topic_zh = item
        prev_t = None if i == 0 else (
            items[i - 1][1], items[i - 1][2], items[i - 1][3], items[i - 1][4])
        next_t = None if i == len(items) - 1 else (
            items[i + 1][1], items[i + 1][2], items[i + 1][3], items[i + 1][4])
        nav_block = render_nav(prev_t, next_t)
        text = f.read_text(encoding="utf-8", errors="ignore")
        new_text = inject_nav(text, nav_block, NAV_CSS)
        if new_text != text:
            f.write_text(new_text, encoding="utf-8")
            n += 1
    print(f"  [done] {subject_dir} — wrote nav into {n}/{len(items)} files")
    return n


def main():
    total = 0
    for s in SUBJECTS:
        total += process_subject(s)
    print(f"\nUpdated {total} unit files across {len(SUBJECTS)} subjects.")


if __name__ == "__main__":
    main()
