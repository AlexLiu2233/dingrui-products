#!/usr/bin/env python3
"""Cross-page language continuity (landing-fix issue #3).

Problem: the landing page lets you switch to Chinese, but clicking a Study
Guide link opens the ENGLISH guide. Target pages were deliberately stripped of
localStorage (the D4 audit fix) so every page defaults to English on a *direct*
visit. That rule stays — but an explicit click from a Chinese page should carry
the language across.

Fix: a tiny, idempotent `<script>` injected before `</body>` on every BILINGUAL
page (any file containing `data-lang="zh"`). It does two things, with NO
persistence:
  1. On load, if the URL carries `?lang=zh`, switch the page to Chinese
     (guarded so an English-only page can never flip to a broken ZH state).
     `?lang=en` or no param  ->  English default (D4 rule preserved).
  2. Capture-phase click handler: while the page is in Chinese, same-site
     relative links get `?lang=zh` appended (hash-safe) so navigation
     (landing -> guide -> guide, across HS / AP / IB) stays in Chinese.

External links, anchors, mailto/tel/js, and links that already carry a `lang`
param are left alone. Idempotent via the `dingrui-lang-link` marker.

Run:  python3 scripts/lang_link_continuity.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKER = "dingrui-lang-link"
# Internal dirs / non-product trees we never touch.
SKIP_PARTS = {".git", ".claude", "node_modules", "dist", "_site",
              "prompts", "rag", "scripts"}

SNIPPET = (
    '<script>/* dingrui-lang-link: cross-page language continuity via ?lang=zh;'
    ' no persistence, direct visits default English */\n'
    '(function(){\n'
    '  try{\n'
    "    var q=new URLSearchParams(window.location.search).get('lang');\n"
    "    if(q==='zh'&&document.querySelector('[data-lang=zh]'))document.body.classList.add('lang-zh');\n"
    "    else if(q==='en')document.body.classList.remove('lang-zh');\n"
    '  }catch(e){}\n'
    "  document.addEventListener('click',function(ev){\n"
    "    if(!document.body.classList.contains('lang-zh'))return;\n"
    "    var a=ev.target&&ev.target.closest?ev.target.closest('a[href]'):null;\n"
    '    if(!a)return;\n'
    "    var href=a.getAttribute('href');\n"
    '    if(!href)return;\n'
    '    if(/^(https?:)?\\/\\//i.test(href)||/^(#|mailto:|tel:|javascript:)/i.test(href))return;\n'
    '    if(/[?&]lang=/.test(href))return;\n'
    "    var hash='',i=href.indexOf('#');\n"
    '    if(i>=0){hash=href.slice(i);href=href.slice(0,i);}\n'
    "    a.setAttribute('href',href+(href.indexOf('?')>=0?'&':'?')+'lang=zh'+hash);\n"
    '  },true);\n'
    '})();</script>'
)


def should_skip(p: pathlib.Path) -> bool:
    return any(part in SKIP_PARTS for part in p.relative_to(ROOT).parts)


def main():
    injected = skipped_present = skipped_en_only = 0
    for p in sorted(ROOT.rglob("*.html")):
        if should_skip(p):
            continue
        with open(p, "r", encoding="utf-8", newline="") as f:
            txt = f.read()
        if 'data-lang="zh"' not in txt:
            skipped_en_only += 1
            continue
        if MARKER in txt:
            skipped_present += 1
            continue
        nl = "\r\n" if "\r\n" in txt else "\n"
        head, sep, tail = txt.rpartition("</body>")
        if not sep:
            print(f"WARN no </body>: {p.relative_to(ROOT)}")
            continue
        snippet = SNIPPET.replace("\n", nl)
        txt = head + snippet + nl + sep + tail
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        injected += 1
        print(f"INJECT  {p.relative_to(ROOT)}")
    print(f"\n{injected} injected, {skipped_present} already had it, "
          f"{skipped_en_only} EN-only (skipped)")


if __name__ == "__main__":
    main()
