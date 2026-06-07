#!/usr/bin/env python3
"""Re-skin Study Guides + landing to the dingruischolars.com vibe (design-refresh sprint).

Direction (signed off): black/white base, maroon (logo color) for brand/headings,
blue (#0099FF, the site link color) as the pop, near-black pill CTA (matches the
site's primary button). Serif headings kept. Practice/Solutions already use a
white/black/maroon print palette, so they're left as-is.

Per file it rewrites ONLY the two token blocks (light :root, dark [data-theme=dark])
in place -- light gets neutral B&W values, dark gets neutral dark values, so dark-mode
text is NOT blackened. Adds --pop/--pop-light/--ink. De-warms nav glass + shadows.
Canonicalizes .consult-cta__btn to the near-black pill (auto-inverts via var(--ink)/
var(--bg-card)) and points inline content links at --pop. Idempotent.

Run:  python scripts/restyle_bw.py
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUBJECTS = [
    "High School Math", "High School Physics", "High School Chemistry",
    "High School Biology", "High School Computer Science",
    "AP Calculus", "AP Physics", "AP CSA", "IB Math HL", "IB Chemistry HL", "IB Physics HL",
]

HEX = r"#[0-9A-Fa-f]{3,6}"

LIGHT = {"--bg": "#FAFAFA", "--bg-card": "#FFFFFF", "--bg-code": "#0F0F0F",
         "--text": "#0F0F0F", "--text-secondary": "#585858", "--border": "#E6E6E6",
         # alt-template token names (AP Calc U7-U8)
         "--bg-primary": "#FAFAFA", "--bg-secondary": "#F2F2F2", "--bg-sidebar": "#FAFAFA",
         "--text-primary": "#0F0F0F", "--text-tertiary": "#888888", "--text-inverse": "#FFFFFF"}
DARK = {"--bg": "#0F0F0F", "--bg-card": "#1A1A1A", "--bg-code": "#000000",
        "--text": "#FAFAFA", "--text-secondary": "#A0A0A0", "--border": "#2A2A2A",
        "--bg-primary": "#0F0F0F", "--bg-secondary": "#1A1A1A", "--bg-sidebar": "#141414",
        "--text-primary": "#FAFAFA", "--text-tertiary": "#9A9A9A", "--text-inverse": "#0F0F0F"}
HERO_LIGHT = "--bg-hero: linear-gradient(135deg, #FFFFFF 0%, #F4F4F4 100%)"
HERO_DARK = "--bg-hero: linear-gradient(135deg, #141414 0%, #1A1A1A 100%)"

# Warm rgba borders/shadows unique to the alt template -> neutral
EXTRA = [
    ("rgba(36, 24, 24,", "rgba(0,0,0,"),
    ("rgba(58, 32, 32,", "rgba(0,0,0,"),
    ("rgba(244, 236, 232,", "rgba(255,255,255,"),
    # de-warm the hero wash (light-maroon -> neutral) shared by landing + SGs
    ("linear-gradient(180deg, var(--accent-light) 0%, transparent 100%)",
     "linear-gradient(180deg, #F4F4F4 0%, transparent 100%)"),
    ("rgba(122,46,46,0.06)", "rgba(0,0,0,0.03)"),
    ("rgba(200,112,112,0.06)", "rgba(255,255,255,0.04)"),
]

CTA_BTN = (".consult-cta__btn { display: inline-block; background: var(--ink); "
           "color: var(--bg-card); font-family: var(--font-body); font-weight: 600; "
           "font-size: 0.95rem; text-decoration: none; padding: 12px 22px; "
           "border-radius: 12px; transition: transform 0.15s, opacity 0.2s; }")
CTA_HOVER = ".consult-cta__btn:hover { opacity: 0.88; transform: translateY(-1px); }"
LINKS = ("/* design-refresh links */ .card a:not(.feeder-link), .concept-box a, "
         ".going-deeper a, .section > p a { color: var(--pop); text-underline-offset: 2px; }")


def sub_tokens(block: str, mapping: dict) -> str:
    for tok, val in mapping.items():
        block = re.sub(re.escape(tok) + r":\s*" + HEX, f"{tok}: {val}", block)
    return block


def restyle(text: str) -> str:
    # light :root
    m = re.search(r":root\s*\{.*?\}", text, re.S)
    if m:
        nl = sub_tokens(m.group(0), LIGHT).replace("rgba(60,20,30,", "rgba(0,0,0,")
        nl = re.sub(r"--(?:bg-hero|hero-gradient):\s*linear-gradient\([^;]*\)", HERO_LIGHT, nl)
        if "--pop:" not in nl:
            nl = re.sub(r"(--accent:\s*#7A2E2E;)",
                        r"\1 --pop: #0099FF; --pop-light: #E8F4FF; --ink: #0F0F0F;", nl, count=1)
        text = text.replace(m.group(0), nl, 1)
    # dark :root (exact `[data-theme="dark"] {` block, not the `.hero` descendant rules)
    m = re.search(r'\[data-theme="dark"\]\s*\{.*?\}', text, re.S)
    if m:
        nd = sub_tokens(m.group(0), DARK)
        nd = re.sub(r"--(?:bg-hero|hero-gradient):\s*linear-gradient\([^;]*\)", HERO_DARK, nd)
        if "--pop:" not in nd:
            nd = re.sub(r"(--accent:\s*" + HEX + r";)",
                        r"\1 --pop: #4DB2FF; --pop-light: #12283A; --ink: #FAFAFA;", nd, count=1)
        text = text.replace(m.group(0), nd, 1)
    # de-warm nav glass
    text = text.replace("rgba(245, 240, 235, 0.92)", "rgba(255, 255, 255, 0.85)")
    # CTA -> near-black pill + inline-link pop (canonicalize; idempotent)
    text = re.sub(r"\.consult-cta__btn \{ display: inline-block;[^}]*\}", CTA_BTN, text, count=1)
    text = re.sub(r"\.consult-cta__btn:hover \{[^}]*\}", CTA_HOVER, text, count=1)
    if "design-refresh links" not in text and CTA_HOVER in text:
        text = text.replace(CTA_HOVER, CTA_HOVER + "\n" + LINKS, 1)
    for old, new in EXTRA:
        text = text.replace(old, new)
    return text


def main() -> int:
    files = [ROOT / "index.html"]
    for s in SUBJECTS:
        files.extend(sorted((ROOT / s).glob("Study Guides/*.html")))
    c = collections.Counter()
    for f in files:
        t = f.read_text(encoding="utf-8")
        nt = restyle(t)
        if nt != t:
            f.write_text(nt, encoding="utf-8"); c["restyled"] += 1
        else:
            c["nochange"] += 1
    print(f"Processed {sum(c.values())} files:", dict(c))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
