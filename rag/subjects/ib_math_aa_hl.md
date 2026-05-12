# Subject Spec — IB Math AA HL

## Identity

- **Display (section heading):** IB Math AA HL
- **Display (hero chip):** IB Math AA HL
- **Directory:** `IB Math HL/`
- **Audit:** `IB Math HL/AUDIT.md` (rich — Sprint 1 active, dual-goal
  contract locked)

## Official curriculum reference

IB Mathematics: Analysis and Approaches HL guide, **first exams 2021**.
The "AA" track is distinct from "AI" (Applications and Interpretation) —
this repo targets AA HL.

## Naming convention

The syllabus organizes content under five topic letters: **A** Number &
Algebra, **B** Functions, **C** Geometry & Trigonometry, **D** Statistics
& Probability, **E** Calculus. Each is being refactored into focused
sub-units:

```
IB Math HL/Study Guides/Unit_X.html        # topic letter alone (legacy monolith)
IB Math HL/Study Guides/Unit_XN.html       # focused sub-unit (e.g. Unit_A1)
IB Math HL/Practice Questions/Unit_XN_Topic_Practice.html
```

Sub-unit refactor status is tracked in `IB Math HL/AUDIT.md`.

## Required `<title>` format

```
IB Math AA HL — Unit {X|XN}: {Topic} | Dingrui Scholars
```

Examples:
- `IB Math AA HL — Unit A1: Sequences & Series | Dingrui Scholars`
- `IB Math AA HL — Unit C: Geometry | Dingrui Scholars`

## Unit list (Study Guide product)

| Unit | Topic | Status |
|---|---|---|
| A   | Number and Algebra (monolith — being refactored)  | shipped (will retire) |
| A1  | Sequences & Series                                | shipped |
| A2  | Exponents and Logarithms                          | **unbuilt** |
| A3  | Combinatorics                                     | shipped |
| A4  | Complex Numbers (HL)                              | **unbuilt** |
| A5  | Proof                                             | **unbuilt** |
| A6  | Algebra and Systems                               | **unbuilt** |
| B   | Functions                                         | **unbuilt** |
| C   | Geometry & Trigonometry                           | shipped |
| D   | Statistics & Probability                          | **unbuilt** |
| E   | Calculus                                          | **unbuilt** |

## Exam structure (HL)

- **Paper 1:** No calculator — short and extended response, 2h.
- **Paper 2:** Calculator allowed — short and extended response, 2h.
- **Paper 3 (HL only):** Two extended problem-solving investigations, 1h.
- **Internal Assessment:** Mathematical exploration.

## Standing principle — dual-goal contract

Every guide serves two students at once: the **crammer** (last-ditch pass
the night before) and the **7-chaser** (going deep for top score). The
canonical articulation is in `prompts/create-unit.md`. Each section
should layer: cheat-sheet at top -> worked example(s) -> "going deeper"
proof/derivation. Quiz items mix recall and synthesis.

Flashcards (when present) follow the locked terse style from A1/A3:
question on front, `$$formula$$` on back, no prose.

## HL flagging

HL-only sub-topics use the `hl-flag` chip (see A1, A3 for the pattern).
A reader should be able to tell at a glance which content is HL-extension
material.
