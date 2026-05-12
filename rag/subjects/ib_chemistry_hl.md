# Subject Spec — IB Chemistry HL

## Identity

- **Display (section heading):** IB Chemistry HL
- **Display (hero chip):** IB Chemistry HL
- **Directory:** `IB Chemistry HL/`
- **Audit:** `IB Chemistry HL/AUDIT.md`

## Official curriculum reference

IB Chemistry guide, **first assessment 2025**. The 2025 syllabus replaced
the previous topic-numbered structure with three themes: **Structure**,
**Reactivity**, and **Tools** — each with sub-topics. There is no longer a
"Unit 1, Unit 2, ..." numbering at the top level.

## Naming convention

```
IB Chemistry HL/Study Guides/Structure_N_Topic_Name.html
IB Chemistry HL/Study Guides/Reactivity_N_Topic_Name.html
IB Chemistry HL/Study Guides/Tools_N_Topic_Name.html
```

`N` is an integer (1, 2, 3) within each theme.

## Required `<title>` format

```
IB Chemistry — {Structure|Reactivity|Tools} N: {Topic} | Dingrui Scholars
```

## Theme list (Study Guide product)

| Theme | N | Topic | Status |
|---|---|---|---|
| Structure  | 1 | Models of the Particulate Nature of Matter | shipped |
| Structure  | 2 | Models of Bonding and Structure            | shipped |
| Structure  | 3 | Classification of Matter                   | **unbuilt** |
| Reactivity | 1 | What Drives Chemical Reactions?            | shipped |
| Reactivity | 2 | How Much, How Fast, How Far                | **unbuilt** |
| Reactivity | 3 | What are the Mechanisms?                   | **unbuilt** |
| Tools      | 1 | Experimental Techniques                    | **unbuilt** |
| Tools      | 2 | Technology                                 | **unbuilt** |
| Tools      | 3 | Mathematics                                | **unbuilt** |

The syllabus coverage gap is recorded in `IB Chemistry HL/AUDIT.md` as the
obvious first sprint.

## Exam structure (HL)

- **Paper 1:** Multiple-choice — 1h30m, no calculator, no data booklet.
- **Paper 2:** Short-answer + extended response — 2h30m, calculator + data
  booklet allowed.
- **Paper 3 (HL only):** Data-based questions covering experimental work +
  options — 1h30m.
- **Internal Assessment:** Scientific investigation.

## Ordering note for build-index.py

The script uses an explicit word-priority map (`WORD_PRIORITY` in
`scripts/build-index.py`) so themes render in syllabus order:

```
Structure -> Reactivity -> Tools
```

If a new theme is added to the IB syllabus, update that map.

## HL vs SL

IB Chemistry has SL and HL tiers. This repo targets **HL only**. Some
sub-topics include HL-extension material (e.g. additional content in
Structure 2, Reactivity 2). Mark HL-only content explicitly in each guide
using a `hl-flag` chip (see existing IB Math HL files for the pattern).
