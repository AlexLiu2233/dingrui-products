# Subject Spec — AP Computer Science A

## Identity

- **Display (section heading):** AP Computer Science A
- **Display (hero chip):** AP Computer Science A
- **Directory:** `AP CSA/`
- **Audit:** `AP CSA/AUDIT.md`

## Official curriculum reference

College Board AP Computer Science A Course and Exam Description (CED).
Language is Java (specifically the subset documented in the CED's quick
reference).

## Naming convention

```
AP CSA/Study Guides/Unit_N_Topic_Name.html
AP CSA/Practice Questions/Unit_N_Topic_Name_Practice_Problems.html
```

`N` is an integer 1–10. No `Practice Questions/` files exist yet.

## Required `<title>` format

```
AP CSA — Unit N: {Topic} | Dingrui Scholars
```

## Unit list (Study Guide product)

| Unit | Topic | Status |
|---|---|---|
| 1  | Using Objects and Methods | shipped |
| 2  | Selection and Iteration   | shipped |
| 3  | Class Creation            | shipped |
| 4  | Data Collections          | shipped |
| 5  | Writing Classes           | **unbuilt** |
| 6  | Array                     | **unbuilt** |
| 7  | ArrayList                 | **unbuilt** |
| 8  | 2D Array                  | **unbuilt** |
| 9  | Inheritance               | **unbuilt** |
| 10 | Recursion                 | **unbuilt** |

The CED coverage gap is recorded in `AP CSA/AUDIT.md` as the obvious first
sprint.

## Exam structure

- **AP exam:** 40 MCQ + 4 FRQ, 3h. Each FRQ is a Java code-writing problem
  (Methods, Class, ArrayList, 2D Array). Java Quick Reference provided.

## Conventions specific to AP CSA

- **No KaTeX.** AP CSA contains no math notation. `scripts/validate.sh`
  detects this and skips the KaTeX requirement when no math delimiters
  appear in the file.
- **Code blocks:** use JetBrains Mono per the design system. Syntax
  highlighting is optional but, if present, must work without JS
  dependencies beyond what's already inlined.
