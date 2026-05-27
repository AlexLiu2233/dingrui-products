# prompts/ — Task playbook index

Each file in this directory is a **locked playbook** for a recurring
SWE task on the Dingrui Scholars HTML products. Playbooks are written
so a model can load one as context and produce shippable output
without ad-hoc clarification rounds.

<routing>

Pick the playbook from the work request:

| If the request is to… | Load |
|---|---|
| **Build a brand-new Study Guide** for a unit that doesn't exist yet | [`create-unit.md`](create-unit.md) |
| **Edit / fix / extend one existing HTML file** (one-off change) | [`modify-unit.md`](modify-unit.md) |
| **Translate** an English study guide / practice / solutions to bilingual EN↔ZH | [`create-bilingual-translation.md`](create-bilingual-translation.md) |
| **Author a Practice + Solutions pair** for an IB unit | [`create-ib-practice-and-solutions.md`](create-ib-practice-and-solutions.md) |
| **Review** a single-file change before commit (screenshot + diff loop) | [`review-changes.md`](review-changes.md) |
| **Run a sprint** through a subject's `AUDIT.md` (multi-item, multi-commit cycle) | [`improve-existing-product.md`](improve-existing-product.md) |

If the request doesn't match a row, ask the user which playbook fits
**before** improvising. Do not invent a new workflow on the fly — log
a gap and propose adding a playbook for it.
</routing>

<playbook_anatomy>

Every playbook in this directory follows the same XML-tagged shape so
the model can navigate by section. Sections used (in order):

| Tag | Purpose |
|---|---|
| `<task>` | One paragraph: what the model is doing and who it serves |
| `<inputs>` | Slot fields (`{{NAME}}`) the user fills in |
| `<contract>` / `<locked_design>` | Non-negotiable invariants (the "locked" content) |
| `<workflow>` | Numbered build steps |
| `<examples>` | One to three literal in / out pairs — the spec, not paragraphs about the spec |
| `<output_format>` | Exact file path, comment header, commit shape, report shape |
| `<acceptance>` / `<exit_criteria>` | Checklist that runs at the end |
| `<negative_space>` | "Do not" rules, scoped to behaviors that were actual past mistakes |
| `<reminders>` | Key invariants restated at the tail (tail-position attention) |
</playbook_anatomy>

<conventions>

- **Slot syntax** is `{{UPPER_SNAKE_CASE}}`. The user fills these in
  when invoking; the model does not invent values.
- **Cross-file references** use relative links to other prompts or to
  `rag/*` files. Never absolute paths.
- **Locked example commits** are cited by short SHA next to the
  decision they justify. If a convention changes, the cited commit is
  superseded, never silently rewritten.
- **Negative-space rules are scoped.** Each "do not" trails a reason
  (the past incident, the actual cost). Generic prohibitions are
  banned because they create the behavior they warn against.
</conventions>

<global_invariants>

Five rules that bind every authoring playbook in this directory.
Stated here so playbooks don't restate them. If a playbook contradicts
one of these, treat the playbook as out of date and route a fix.

1. **Tone.** Load [`_tone.md`](_tone.md) before writing prose. No em
   or en dashes (`—`, `–`, `&mdash;`, `&ndash;`, `&#8212;`,
   `&#8211;`) anywhere in student-facing product prose. Pre-LLM
   textbook voice (Stewart / Spivak / Cambridge revision register),
   not coaching prose. Math notation is exempt. Sweep the file for
   all six dash characters before declaring done. The only
   exemption is the `<title>` tag separator (`build-index.py` splits
   on `" — "`).
2. **`dingrui:version` + `dingrui:pair-key` lock paired files.**
   Practice + Solutions sets must carry identical version + pair-key
   tags. `scripts/validate.sh` is the gate.
3. **`data-lang` parity is the bilingual gate.** Every
   `<span data-lang="en">` has a sibling `<span data-lang="zh">` in
   bilingual files. `grep -c` counts must match. `index.html`'s ZH
   toggle relies on this contract; non-paired strings disappear in
   one language.
4. **`scripts/validate.sh` exits 0 before shipping.** Catches odd-`$`
   parity, mismatched marks, missing dingrui pair tags, broken TOC
   anchors. Run it.
5. **`scripts/build-index.py` runs after any change that adds, removes,
   or renames a Study Guide.** It writes the landing-page cards from
   the unit `<title>` tags + hero `<h1>` ZH spans.

Each playbook's `<reminders>` tail repeats only the playbook-specific
items. The five above are global; cite [`_tone.md`](_tone.md) or this
section instead of inlining the rule.
</global_invariants>

<cross_references>

Pairs with the broader project context:

- `../CLAUDE.md` — repo-level conventions, deploy flow, scripts catalog.
- `../rag/style-guide.md` — design tokens, component patterns.
- `../rag/content-specs.md` — per-subject specs (curriculum, naming, exam).
- `../rag/AUDIT_TEMPLATE.md` — scaffold for new subject audits.
- `../<Subject>/AUDIT.md` — the single source of truth for each subject's open work.
</cross_references>
