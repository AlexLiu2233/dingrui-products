# Tone — global authoring rules

Loaded by every authoring playbook (`create-unit.md`,
`create-ib-practice-and-solutions.md`, `create-bilingual-translation.md`,
and the forthcoming `create-practice-and-solutions-hs-math.md`).
Single source of truth for the no-dash sweep and the pre-LLM textbook
voice spec. If you change the rule, change it here.

## No em or en dashes anywhere in prose (locked 2026-05-21, extended 2026-05-24)

**The rule.** Every dash character is suspect. Specifically:

| Character | U+ | Allowed in prose? |
|---|---|---|
| em dash `—` | U+2014 | **Never** |
| en dash `–` | U+2013 | **Never** |
| hyphen-minus `-` | U+002D | Only in compound modifiers ("first-principles derivation", "second-derivative test") |
| minus sign inside math | inside `$...$` | Fine |

This applies to **all student-facing product prose**: Study Guides, Practice
Questions, Solutions, AUDIT notes, landing copy. Math notation is
exempt because the minus signs inside `$\sqrt{x} - 1$` are operators,
not stylistic dashes.

HTML entity equivalents (`&mdash;`, `&ndash;`, `&#8212;`, `&#8211;`)
are the same offence in escaped form. Sweep for them too.

**Rewrites** (the four moves that replace 90% of em-dashes):

| Em-dash use | Replace with |
|---|---|
| Aside or parenthetical: "the proof — which uses induction — finishes the argument" | Parentheses: "the proof (which uses induction) finishes the argument" |
| Sentence break for emphasis: "She studied for weeks — and still failed" | Two sentences: "She studied for weeks. Still, she failed." |
| Definition or restatement: "Let $f$ be continuous — that is, $\lim_{x \to a} f(x) = f(a)$" | Colon: "Let $f$ be continuous: $\lim_{x \to a} f(x) = f(a)$" |
| List intro before a clause: "Three methods work — substitution, factoring, rationalising" | Colon + list: "Three methods work: substitution, factoring, and rationalising" |

If the sentence really resists the rewrite, that is a sign the
sentence is too clever. Break it into two sentences.

## Pre-LLM textbook voice (positive spec)

The prose should read like Stewart's Calculus, Spivak, the IB course
companion, or a Cambridge revision guide. Concretely:

- **Formal connectives.** "Therefore", "Hence", "Consequently", "It
  follows that", "We conclude that". Not "so basically" or "which
  means".
- **Named, numbered results.** "Theorem 1", "Definition 2", "Example
  3.4", "Lemma 5.1". Worked examples in the existing template already
  carry "Worked Example E1.1a" style labels; keep that.
- **Conventional textbook structure.** Definition, then theorem, then
  proof or worked example, then remark. Avoid the LLM tic of opening
  with "Let's break this down" or "Think of it this way".
- **Direct exposition, not conversational coaching.** Write "The
  derivative gives the slope of the tangent." Not "Think of the
  derivative as the slope of the tangent (pretty cool, right?)".
- **Standard callout phrases.** "Remark.", "Note that...", "We have
  shown that...", "By the previous theorem,", "Conversely,",
  "It is straightforward to verify that...".
- **Symbols over words where convention prefers.** "$\therefore$"
  closes a proof. "$\Box$" or "$\blacksquare$" ends a proof. "iff"
  in informal exposition, "if and only if" in theorem statements.
- **No marketing punctuation.** No exclamation marks. No emoji. No
  "Pro tip:" or "Heads up:" headers. Use the existing
  `.concept-box.red` or `.cram-cheat` containers; they already carry
  the warning register without needing rhetorical flair in the prose.

## Sweep before declaring done

Search the file for `—`, `–`, `&mdash;`, `&ndash;`, `&#8212;`,
`&#8211;`. All six should return zero hits **except in one structural
location**: the `<title>` tag, which `scripts/build-index.py` parses
by splitting on `" — "` (see `parse_title` in that file). Until the
title separator is migrated to a non-dash character across all
shipped units, the em dash in `<title>` stays.

Then re-read one section out loud. If it sounds like a blog post or
a sales pitch, rewrite to textbook register.
