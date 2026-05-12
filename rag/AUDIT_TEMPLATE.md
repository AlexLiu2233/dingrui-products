# {Subject Display Name} — Audit

Open punch list for {Subject}, scored against the canonical generation prompt
(see `prompts/create-unit.md` plus any subject-specific spec in
`rag/subjects/`) and the official curriculum reference.

**Tier definitions**

- **P0** — content-correctness, philosophy, or coverage gap that blocks
  "going for top score" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only.
Anything that belongs in a richer interactive surface lives in the
[Digital Product Backlog](#digital-product-backlog) at the bottom of this
file and is **out of scope** until that product spins up.

Last reviewed: **YYYY-MM-DD**.

---

## Active Sprint — what we're working on now

**Sprint {N} — {one-line description}**

| ID | Item | Tier | Status |
|---|---|---|---|
| **S{N}-1** | {Work item} | P{0/1/2} | **Open** |
| **S{N}-2** | {Work item} | P{0/1/2} | **Open** |

Build order: {S{N}-1 -> S{N}-2 -> ...}

---

## Standing Principles

> Subject-specific philosophy. Examples from existing audits:
>
> - **IB Math HL** uses the dual-goal contract (cram cheat-sheet on top,
>   going-deeper proofs at the bottom). See `prompts/create-unit.md`.
> - **AP Physics** uses the Interactive Component Philosophy (sliders only,
>   one key thing per widget). See `AP Physics/AUDIT.md` § Interactive
>   Component Philosophy.

Lock standing principles here. Anything that deviates routes to the Digital
Product Backlog rather than the Study Guide.

---

## Closed Sprints

> Move sprints here when all items ship. Preserves traceability without
> bloating the Active Sprint section.

### Sprint {N-1} — closed YYYY-MM-DD

| ID | Item | Tier | Status |
|---|---|---|---|
| ~~**S{N-1}-1**~~ | ~~{Work item}~~ | P0 | closed |

---

## Digital Product Backlog

Items that don't fit the Study Guide surface but should be built someday in
a richer interactive product.

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | {Idea} | {Reason — usually: requires interaction beyond a slider, or stateful student progress, or grading} |
