#!/usr/bin/env python3
"""UTM-tag every consult CTA link so signups attribute to the exact page (Sprint B).

Each CTA currently points at a bare signup URL, so the destination site's
analytics can't tell which note (or which language) drove a signup. This rewrites
every CTA href to carry UTM params derived from the file path + link language:

  utm_source = notes
  utm_medium = cta
  utm_campaign = <subject_slug>           e.g. hs_physics, ap_calculus, ib_math_hl, landing
  utm_content  = <unit>__<doctype>__<lang> e.g. unit_1_kinematics__sg__en, hero__landing__zh

Language is inferred from the URL itself (/signup = en, /signup-ch = zh), which is
unambiguous because the trailing quote (signup" vs signup-ch") disambiguates and the
print-CSS pseudo-text (…/signup)") never matches. index.html is special-cased so its
4 links (hero/footer × en/zh) get distinct utm_content. Idempotent: skips files
already containing utm_source. Parity-neutral (only href values change).

Run:  python scripts/utm_tag_cta.py
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

SUBJECT_SLUG = {
    "High School Math": "hs_math", "High School Physics": "hs_physics",
    "High School Chemistry": "hs_chemistry", "High School Biology": "hs_biology",
    "High School Computer Science": "hs_cs",
    "AP Calculus": "ap_calculus", "AP Physics": "ap_physics", "AP CSA": "ap_csa",
    "IB Math HL": "ib_math_hl", "IB Chemistry HL": "ib_chem_hl", "IB Physics HL": "ib_physics_hl",
}

EN_URL = "https://www.dingruischolars.com/signup"
ZH_URL = "https://www.dingruischolars.com/signup-ch"


def utm(campaign: str, content: str) -> str:
    return f"?utm_source=notes&utm_medium=cta&utm_campaign={campaign}&utm_content={content}"


def unit_slug(stem: str) -> str:
    s = stem
    for suf in ("_Practice_Problems", "_Practice", "_Solutions", "_ans"):
        if s.endswith(suf):
            s = s[: -len(suf)]
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def doctype(parts) -> str:
    if "Study Guides" in parts:
        return "sg"
    if "Solutions" in parts:
        return "solutions"
    if "Practice Questions" in parts:
        return "practice"
    return "page"


def tag_notes_file(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "utm_source" in t:
        return "skip-present"
    parts = path.parts
    subject = next((s for s in SUBJECT_SLUG if s in parts), None)
    if not subject:
        return "SKIP-no-subject"
    campaign = SUBJECT_SLUG[subject]
    content_base = f"{unit_slug(path.stem)}__{doctype(parts)}"
    new = t.replace(EN_URL + '"', EN_URL + utm(campaign, content_base + "__en") + '"')
    new = new.replace(ZH_URL + '"', ZH_URL + utm(campaign, content_base + "__zh") + '"')
    if new == t:
        return "SKIP-no-href"
    path.write_text(new, encoding="utf-8")
    return "tagged"


def tag_landing(path: pathlib.Path) -> str:
    t = path.read_text(encoding="utf-8")
    if "utm_source" in t:
        return "skip-present"
    # 4 distinct anchors: hero/footer x en/zh. Anchor on the unique prefix of each.
    subs = [
        (f'hero-cta__btn" data-lang="en" href="{EN_URL}"',
         f'hero-cta__btn" data-lang="en" href="{EN_URL}{utm("landing", "hero__landing__en")}"'),
        (f'hero-cta__btn" data-lang="zh" href="{ZH_URL}"',
         f'hero-cta__btn" data-lang="zh" href="{ZH_URL}{utm("landing", "hero__landing__zh")}"'),
        (f'Ready to start? <a href="{EN_URL}"',
         f'Ready to start? <a href="{EN_URL}{utm("landing", "footer__landing__en")}"'),
        (f'<a href="{ZH_URL}"',
         f'<a href="{ZH_URL}{utm("landing", "footer__landing__zh")}"'),
    ]
    n = 0
    for old, repl in subs:
        if old in t:
            t = t.replace(old, repl, 1); n += 1
    if n != 4:
        return f"SKIP-landing-matched-{n}/4"
    path.write_text(t, encoding="utf-8")
    return "tagged-landing"


def main() -> int:
    counts = collections.Counter()
    landing = ROOT / "index.html"
    print(f"  {tag_landing(landing):20s} index.html")
    counts[tag_landing.__name__] += 0
    files = [p for p in ROOT.rglob("*.html")
             if "consult-cta" in p.read_text(encoding="utf-8", errors="replace") and p.name != "index.html"]
    for f in sorted(files):
        st = tag_notes_file(f)
        counts[st] += 1
        if st.startswith("SKIP"):
            print(f"  !! {st:18s} {f.relative_to(ROOT)}")
    print(f"\nNotes files: {sum(counts.values())}")
    for k, v in sorted(counts.items()):
        print(f"  {v:3d}  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
