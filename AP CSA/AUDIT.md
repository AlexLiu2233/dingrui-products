# AP Computer Science A — Audit

Open punch list for the AP CSA study guides, scored against
`prompts/create-unit.md`, `rag/subjects/ap_csa.md`, and the official AP
Computer Science A Course and Exam Description (CED).

**Tier definitions**

- **P0** — content-correctness or coverage gap that blocks "shooting for a
  5" use of the guide.
- **P1** — consistency, polish, or hygiene gap that affects feel/parity but
  not exam readiness.
- **P2** — nice-to-have / future work.

**Scope boundary** — this audit covers the *Study Guide* product only. Any
practice-runner / grader for Java code lives in the
[Digital Product Backlog](#digital-product-backlog).

Last reviewed: **2026-05-11** (audit stub created during workflow
standardization; content not yet inventoried).

**CED coverage gap** — current shipped: Units 1–4. AP CSA CED runs Units
1–10. Units 5–10 (Writing Classes, Array, ArrayList, 2D Array, Inheritance,
Recursion) are unbuilt.

---

## Active Sprint — what we're working on now

**No active sprint.** When this subject becomes a priority, the obvious
first move is the CED coverage gap.

| ID | Item | Tier | Status |
|---|---|---|---|
| **S1-1** | Ship Units 5–10 to close CED coverage gap (Writing Classes, Array, ArrayList, 2D Array, Inheritance, Recursion) | P0 | **Open** |
| **S1-2** | Standing principle: pick whether AP CSA needs a Code Sandbox surface, or worked-snippets are enough | P1 | **Open** |
| **S1-3** | Practice Questions sub-product — none exist yet for this subject | P1 | **Open** |

---

## Standing Principles

*To be locked once a sprint begins.* AP CSA is the only subject in the repo
that doesn't use KaTeX (Java code only — `validate.sh` was patched to make
the KaTeX check conditional). Any principles around code-snippet styling
should go here.

---

## Digital Product Backlog

| ID | Item | Why it's not in scope here |
|---|---|---|
| DP-1 | In-browser Java sandbox / runner | Requires a server or WASM Java runtime; well beyond the static-HTML envelope. |
| DP-2 | MCQ grader for AP-style practice MCQ | Stateful; needs answer storage and explanation reveal. |
