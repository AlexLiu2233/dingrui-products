# Subject Spec — AP Calculus AB/BC

## Identity

- **Display (section heading):** AP Calculus AB/BC
- **Display (hero chip):** AP Calculus AB/BC
- **Directory:** `AP Calculus/`
- **Audit:** `AP Calculus/AUDIT.md`

## Official curriculum reference

College Board AP Calculus AB/BC Course and Exam Description (CED). The
in-repo content tracks the **BC** scope. AB-shared Unit 1 may carry a
"AB &amp; BC" subject phrase in its `<title>` tag — that is intentional.

## Naming convention

```
AP Calculus/Study Guides/Unit_N_Topic_Name.html
AP Calculus/Practice Questions/Unit_N_Topic_Name_Practice_Problems.html
```

`N` is an integer 1–10. Topic name uses underscores; commas become `__`
and " &amp; " becomes `____` in filenames (historical — when adding a new
unit, prefer rephrasing to avoid this).

## Required `<title>` format

```
AP Calculus AB/BC — Unit N: {Topic} | Dingrui Scholars
```

`build-index.py` reads this verbatim to generate the card on the home
page. Drift here will surface as a parse warning.

## Unit list (Study Guide product)

| Unit | Topic |
|---|---|
| 1  | Limits and Continuity |
| 2  | Differentiation: Definition and Fundamental Properties |
| 3  | Composite, Implicit, and Inverse Functions |
| 4  | Contextual Applications of Differentiation |
| 5  | Analytical Applications of Differentiation |
| 6  | Integration and Accumulation of Change |
| 7  | Differential Equations |
| 8  | Applications of Integration |
| 9  | Parametric Equations, Polar Coordinates, and Vector-Valued Functions |
| 10 | Infinite Sequences and Series |

## Exam structure

- **AP exam:** 45 MCQ + 6 FRQ across two papers, ~3h15m. Calculator
  permitted on parts of each section.
- **No Paper 3** equivalent — single integrated test.

## HL-style flags / special conventions

None — AP Calculus has a single tier.
