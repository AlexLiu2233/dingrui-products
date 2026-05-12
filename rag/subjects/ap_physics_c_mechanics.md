# Subject Spec — AP Physics C: Mechanics

## Identity

- **Display (section heading):** AP Physics C: Mechanics
- **Display (hero chip):** AP Physics C
- **Directory:** `AP Physics/`
- **Audit:** `AP Physics/AUDIT.md` (rich — locked Interactive Component
  Philosophy and Sprint history)
- **Generation reference:** `AP Physics/GENERATION_PROMPT.md`

## Official curriculum reference

College Board AP Physics C: Mechanics Course and Exam Description (CED).
Note that AP Physics C is split into two separate AP exams — Mechanics and
Electricity & Magnetism. This repo only covers **Mechanics** so far; E&M is
unbuilt.

## Naming convention

```
AP Physics/Study Guides/Unit_N_Topic_Name.html
AP Physics/Practice Questions/Unit_N_Topic_Name_Practice_Problems.html
```

`N` is an integer 1–7.

## Required `<title>` format

```
AP Physics C: Mechanics — Unit N: {Topic} | Dingrui Scholars
```

The subject phrase contains a colon — `build-index.py` splits on the em
dash first, then on the first colon after it, so this format parses
correctly.

## Unit list (Study Guide product)

| Unit | Topic |
|---|---|
| 1 | Kinematics |
| 2 | Force & Translational Dynamics |
| 3 | Work, Energy, and Power |
| 4 | Linear Momentum |
| 5 | Torque & Rotational Dynamics |
| 6 | Energy & Momentum of Rotating Systems |
| 7 | Oscillations |

## Exam structure

- **AP exam (Mechanics):** 40 MCQ + 4 FRQ, 1h30m. Calculator and AP-supplied
  equations sheet both allowed throughout.

## Standing principle — Interactive Component Philosophy

Sliders only; one key thing per widget; no tutorial chrome; no
`localStorage` state. See `AP Physics/AUDIT.md` § Interactive Component
Philosophy for the locked rules. Widget ideas that don't fit go to the
Digital Product Backlog.
