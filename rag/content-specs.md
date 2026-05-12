# Content Specifications — Index

Per-subject specs live in `rag/subjects/`. Each file documents:

- official curriculum reference,
- directory + filename conventions,
- the required `<title>` format that `build-index.py` parses,
- unit list with ship status,
- exam structure (Papers, calculator policy, etc.),
- standing principles or HL/SL conventions.

## Subjects

| Subject | Spec | Audit |
|---|---|---|
| AP Calculus BC               | [`subjects/ap_calculus_bc.md`](subjects/ap_calculus_bc.md)             | [`AP Calculus/AUDIT.md`](../AP%20Calculus/AUDIT.md) |
| AP Physics C: Mechanics      | [`subjects/ap_physics_c_mechanics.md`](subjects/ap_physics_c_mechanics.md) | [`AP Physics/AUDIT.md`](../AP%20Physics/AUDIT.md) |
| AP Computer Science A        | [`subjects/ap_csa.md`](subjects/ap_csa.md)                             | [`AP CSA/AUDIT.md`](../AP%20CSA/AUDIT.md) |
| IB Chemistry HL              | [`subjects/ib_chemistry_hl.md`](subjects/ib_chemistry_hl.md)           | [`IB Chemistry HL/AUDIT.md`](../IB%20Chemistry%20HL/AUDIT.md) |
| IB Math AA HL                | [`subjects/ib_math_aa_hl.md`](subjects/ib_math_aa_hl.md)               | [`IB Math HL/AUDIT.md`](../IB%20Math%20HL/AUDIT.md) |

## Content Depth Guidelines (cross-subject)

- Each section: concept explanation + 1–2 worked examples.
- Proofs / derivations included where pedagogically valuable, behind a
  `box--proof` or `<details>` so crammers can skip them.
- Real-world context where applicable.
- Quiz questions test both conceptual understanding and computation.

## Adding a New Subject

1. Create `<Subject>/Study Guides/` and `<Subject>/Practice Questions/`.
2. Copy `rag/AUDIT_TEMPLATE.md` to `<Subject>/AUDIT.md`.
3. Add a per-subject spec to `rag/subjects/`.
4. Add a row to the Subjects table above.
5. Register the subject in `scripts/build-index.py`'s `SUBJECTS` list
   (and `WORD_PRIORITY` if it uses non-`Unit` prefix words).
6. Run `python scripts/build-index.py` to wire the new subject into
   `index.html` cards and hero chips.
