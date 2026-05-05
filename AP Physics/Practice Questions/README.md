# AP Physics C: Mechanics — Practice Questions

AP-style practice question sets for Units 1–7 of AP Physics C: Mechanics,
designed to be **standalone** but complementary to the matching study guides
in [`../Study Guides/`](../Study%20Guides/).

> **Status — rough draft.** This folder is being populated on the
> `improve_AP_Physics` branch. See [`../AUDIT.md`](../AUDIT.md) for the open
> punch list. Unit 1 is the first scaffolded unit.

Each unit will ship as both:

- **HTML** — KaTeX-rendered, print-styled at letter size. Open in a browser.
- **PDF** — pre-rendered "save as PDF" of the HTML for distribution.

Both versions will have:

- A **PART I — Multiple Choice** section (15–20 items) with topic labels,
  difficulty pills (`EASY` / `MEDIUM` / `HARD`), and `Calculator` /
  `No Calculator` tags matching AP exam conventions.
- A **PART II — Free-Response Questions** section (3–5 multi-part FRQs) with
  blank work areas sized to typical AP page lengths.
- A maroon name/period header and a "Topics N.X – N.Y" scope chip in the page
  header for at-a-glance scope identification.

---

## Index

| Unit | Title | Items | Scope | HTML | PDF |
|---|---|---|---|---|---|
| 1 | Kinematics | 18 MC + 4 FRQ ✓ | 1.1 – 1.5 | [Unit_1_Kinematics_Practice_Problems.html](Unit_1_Kinematics_Practice_Problems.html) | _pending_ |
| 2 | Force & Translational Dynamics | _pending_ | 2.1 – 2.10 | _pending_ | _pending_ |
| 3 | Work, Energy, & Power | _pending_ | 3.1 – 3.5 | _pending_ | _pending_ |
| 4 | Linear Momentum | _pending_ | 4.1 – 4.4 | _pending_ | _pending_ |
| 5 | Torque & Rotational Dynamics | _pending_ | 5.1 – 5.6 | _pending_ | _pending_ |
| 6 | Energy & Momentum of Rotating Systems | _pending_ | 6.1 – 6.6 | _pending_ | _pending_ |
| 7 | Oscillations | _pending_ | 7.1 – 7.5 | _pending_ | _pending_ |

> **Coverage target:** ≈ 130 MC + 28 FRQ across the seven units once complete.

---

## Style & Conventions

The practice files reuse the print-first CSS pattern from
[`../../AP Calculus/Practice Questions/`](../../AP%20Calculus/Practice%20Questions/):

- `@page { size: letter; margin: 0.6in 0.65in; }`
- Times New Roman body, DM Serif Display chapter title, Source Sans 3 pills
- Maroon `#7A2E2E` accent, no dark mode (print-targeted)
- KaTeX inline + display math
- `.q` cards with `.q-head` pills and `.q-body` content
- `.work` blank zones for student writing (sizes: `s` / `m` / `l` / `xl`)
- `.fig` SVG diagrams kept inline (no external assets)

Topic-pill convention for Mechanics: `N.X Short Topic Name`, e.g.
`1.3 Kinematic Equations`, `2.7 Drag Forces`, `5.4 Rolling Without Slipping`.

### Locked conventions (Sprint 4, 2026-05-04)

- **Question-only product.** No embedded answers, no `<details>` reveals,
  no answer keys inside the practice file itself. This matches the AP
  Calculus house style — the file is what the student receives. If
  teacher answer keys are needed, they ship as a separate
  `Unit_N_*_Answer_Key.html` companion (deferred — not yet a deliverable).
- **Typography for SI units:** use `\mathrm{...}` for unit composition
  (`\mathrm{m/s}`, `\mathrm{kg \cdot m^2/s}`), not `\text{...}`. Rationale:
  closer to AP exam typography, and avoids the unicode-in-`\text{}` annotation
  bug from study guides (see AUDIT.md S1-A). Variables remain in plain math
  mode (`v`, `\theta`, `m_1`).
- **Body math uses `~` for inter-unit spacing** (e.g. `5~\mathrm{m/s}`),
  not `\;` — `~` ties the value to its unit and prevents line breaks.

---

## Workflow

```bash
# Validate (uses the same script as study guides)
bash scripts/validate.sh "AP Physics/Practice Questions/Unit_N_*.html"

# Render PDF (browser "Save as PDF" — keep margins at default)
# or use Chromium headless: chrome --headless --print-to-pdf=Unit_N.pdf <file>
```

PDFs land alongside the HTML with the file name pattern
`Chapter N_ {Title} — AP-Style Practice.pdf` to match the AP Calculus
distribution shape.
