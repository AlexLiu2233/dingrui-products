# Student Checklist Portal — Design Spec (v0.1, plan-only)

**Status:** plan-only, not yet built. Captures the product surface,
inputs/outputs, data-source layer, and the two implementation paths
on the table. User decides which one to commit to in a follow-up
sprint. This document was created 2026-05-26 alongside the landing-page
ZH translation + IB Math AA HL accordion work, in response to:

> For the existing high school files, plan an upcoming Checklist page on
> the landing page (or some portal/chatbot) so that a student in some
> grade can get a checklist for the topics they need.
> e.g. Grade 9 BC, wishes to do STEM career
> e.g. Grade 10 ON, wishes to just get it done for business school
> The study guides + PQ/Solutions are by topic, meant to cover all
> meaningful topics (starting with math) that a student would take in
> the public system, flawed as it may be.

---

## 1. What the product does (one paragraph)

A student lands on Dingrui Scholars not knowing which Study Guides
they actually need. They are in some grade (9/10/11/12), in some
province or state, and pursuing some kind of post-secondary plan
(STEM, business, arts, trades, minimum pass). The Checklist Portal
asks them those three things, then returns a personalised, ordered
list of Study Guide sections and Practice/Solutions sets — the topics
their specific track will hit before graduation, ordered by when
they're examinable, with the topics they can defer or skip explicitly
called out. The portal does not generate new content; it filters and
orders the existing topic-organised corpus that already encodes the
grade-by-region nav inside every Study Guide.

## 2. Inputs (the three dimensions)

| Dim | Values (initial scope) | Notes |
|---|---|---|
| **Grade** | 9, 10, 11, 12 | The student's current grade. Used to flag sections they need *now* vs. that come up *later*. |
| **Region** | 🇨🇦 BC, 🇨🇦 ON, 🇨🇦 AB, 🇺🇸 US Common Core | Same four columns as the Syllabus Map in every HS Math unit. The grade-by-region nav inside each Study Guide already encodes the per-region grade alignment (e.g. "🇨🇦 ON Grade 9 — MPM1D"). |
| **Goal** | STEM-track (calculus-feeder), Business-track (data/stats-heavy), Arts/Humanities-track (minimum), General/Undecided | Maps the post-secondary intent onto the topic emphasis. STEM students need trig + intro calculus + sequences; Business students need stats + probability + financial-math touches; Arts students need the literacy/numeracy minimum; Undecided gets the union. |

**Out of scope for v1:**
- US state-level refinement (treats all US students as one CCSSM cohort).
- Per-district / per-board ON/BC nuances (BC's School District 38 vs. 39 — assume curriculum is the lever, not the board).
- AP/IB feeder layer (a STEM-track Grade 11 student "should also look at" AP Calc Unit 1 — this is an obvious follow-on but adds another data layer; see §6 Phase 2).

## 3. Output (what the student sees)

A single page with three sections, all keyed to the existing corpus:

### 3.1 "Required topics" (the spine)
An ordered list of Study Guide sections the student must hit before
graduating, in roughly the order their curriculum presents them. Each
row carries:

- A hyperlink to the section anchor inside the relevant Study Guide
  (e.g. `High%20School%20Math/Study%20Guides/Unit_1_...html#sec-1-3`).
- A status pill: `Now` (current grade), `Soon` (next grade), `Later`,
  `Done` (the student can mark complete; localStorage).
- The matching syllabus code from the student's region
  (e.g. `MPM1D · LR1.04`).
- A one-line "why this matters" hook drawn from the existing section
  preamble or the goal-track mapping.

### 3.2 "You can defer / skip" (the negative space)
Sections the existing topic-organised corpus covers but the student's
grade × region × goal combination does not require. Drawn from the
honors-flag pattern + the per-section region chips already present in
the SGs. Useful so the student doesn't feel they have to study every
unit.

### 3.3 "Practice path"
Linked Practice + Solutions sets that pair with each required topic.
Re-uses the Practice question chip taxonomy (`region` + `paper-style`)
so the student can drill the exam-style their goal calls for
(SAT-style MCQ for STEM US, ON Provincial-style for ON, etc.).

## 4. Data source

**The data already exists in the corpus.** Every HS Math Study Guide
ships with:

1. A top-of-unit `<aside class="syllabus-map">` callout (3-column
   US/ON/BC; AB added once extracts are written).
2. An 8-row grade-by-region nav table inside the "How to use this
   guide" section, telling each (grade × region) student which
   sections to focus on and which to defer.
3. Per-section `region-chip` honors-flag tagging (e.g.
   `🇨🇦 BC PC12 honors`, `🇺🇸 not in CCSSM — AP/IB feeder`).
4. Practice files: `region` + `paper-style` chips on every question
   (`🇺🇸 US` / `🇨🇦 ON` / `🇨🇦 BC` + `SAT-style MCQ` / `AP-feeder FRQ`
   / `ON Provincial-style` / `BC Provincial-style`).

The Checklist Portal harvests these into a single JSON manifest. The
build script (proposed: `scripts/build-checklist-manifest.py`) walks
`High School Math/Study Guides/*.html`, parses the syllabus-map +
per-section region chips, and emits something like:

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-05-26",
  "subjects": ["High School Math"],
  "topics": [
    {
      "subject": "High School Math",
      "unit_number": 1,
      "unit_title": "Linear Functions and Systems",
      "unit_url": "High School Math/Study Guides/Unit_1_Linear_Functions_and_Systems.html",
      "sections": [
        {
          "id": "sec-1-3",
          "title": "Slope and y-intercept",
          "regions": {
            "US":  { "grade": 9,  "code": "HSF-LE.A.2",    "required_for": ["stem", "business", "general"] },
            "ON":  { "grade": 9,  "code": "MPM1D · LR2.05", "required_for": ["stem", "business", "general"] },
            "BC":  { "grade": 10, "code": "FMP&PC10",       "required_for": ["stem", "business", "general"] },
            "AB":  { "grade": 10, "code": "Math 10C — RF",  "required_for": ["stem", "business", "general"] }
          },
          "honors": false,
          "feeder_into": ["AP Calculus Unit 1", "IB Math HL B1"]
        }
      ]
    }
  ]
}
```

**The manifest is the contract.** Whatever UI ships against it,
ship-time is a JSON-rebuild step. Same idempotency story as
`build-index.py`.

## 5. Architecture — two paths

### Path A — Static decision-tree portal (recommended for v1)

A new HTML page (`student-checklist.html`) styled to match the
landing-page chrome. Three radio-group steps (Grade · Region · Goal)
+ a "Show my checklist" button. Below, the filtered manifest renders
into the three output sections from §3. Pure client-side: load the
JSON, filter by the three inputs, render.

**Pros.**
- Ships in days, not weeks.
- Zero recurring cost (no API calls).
- Works offline once the page is loaded; same self-contained-HTML
  philosophy as the rest of the product.
- Filtering logic is auditable in the diff; we control exactly what
  topics get recommended.

**Cons.**
- No conversational refinement ("what if I'm in BC but doing the
  Foundations stream not Pre-Calc?").
- Three radio dimensions feels rigid; some edge cases (Grade-12
  student catching up on Grade-10 algebra) need extra UX work.

**Build effort: ~3-5 days** including manifest generation, UI, and
landing-page integration.

### Path B — Chatbot portal (LLM-driven)

A chat surface that takes free-form input and, under the hood, sends
the manifest as context to a Claude API call (per the
[[claude-api]] skill). The LLM extracts the three dimensions from
conversation, filters the manifest, and returns the same output.

**Pros.**
- Handles edge cases conversationally ("I'm in BC, doing the regular
  stream, want to switch into Pre-Calc by Grade 11" — the LLM can
  infer the implication).
- Extensible to "explain this topic to me" or "give me the next
  question to practise" without UI rework.

**Cons.**
- Recurring API cost per session (Sonnet or Haiku tier — Haiku
  probably fine for this routing task).
- Latency on first response (~1-2s).
- Requires backend / proxy or exposes the API key (the static product
  has no backend today).
- Prompt-injection surface to manage.

**Build effort: ~2-3 weeks** including auth gating, rate limiting,
prompt engineering against the manifest.

### Recommendation

**Ship Path A as v1.** It uses content that already exists, has zero
recurring cost, and lands in a sprint. Path B becomes a Phase 2
upgrade IF Path A's funnel data shows students bouncing on the radio
UI or asking for explanation. The static portal also produces the
manifest, which Path B would need anyway, so the work composes.

## 6. Build path (proposed sprint structure)

### Phase 1 — Manifest extraction (one sprint)
1. Write `scripts/build-checklist-manifest.py` that walks
   `High School Math/Study Guides/*.html`, parses the syllabus-map +
   the grade-by-region nav table + per-section chips, and emits
   `data/checklist-manifest.json`.
2. Verify against Units 1-6 of the shipped corpus. If a topic doesn't
   parse cleanly, harden the markup in the SGs themselves (don't
   special-case in the script).

### Phase 2 — Static portal UI (one sprint)
1. New `student-checklist.html` page styled to landing-page chrome.
2. Three radio-group steps; bilingual EN/ZH; URL state in
   `?grade=10&region=ON&goal=stem` so a guidance counsellor can
   bookmark a profile.
3. Landing-page integration: a new tier-nav pill or a top-nav button
   "Find my path" / "找到我的路径".
4. localStorage for the "Done" status per section.

### Phase 3 — Coverage expansion (one sprint, optional)
1. Extend manifest extraction to AP Calc / AP Physics / AP CSA / IB
   Math AA HL / IB Chem HL / IB Physics HL. Each subject's `<title>`
   tag + hero overline + (future) per-section data attributes feed in.
2. The portal now recommends AP/IB units as feeder rows for STEM
   Grade-11/12 students.

### Phase 4 — Chatbot upgrade (deferred until funnel data justifies)
See §5 Path B.

## 7. Open decisions (asks for the user)

| # | Question | Decider |
|---|---|---|
| 1 | Does "Goal" use the four buckets in §2, or a different taxonomy (e.g. by post-secondary discipline: engineering / med / commerce / liberal arts)? | Product |
| 2 | Where does the portal entry point live in the landing page IA? New tier-nav pill, top-nav button, or hero-CTA button? | Product |
| 3 | Does v1 include AP/IB feeder rows (so a Grade-12 STEM student sees AP Calc Unit 1 in their queue), or stay strictly HS-Math for the first ship? | Product |
| 4 | Bilingual on day 1, or EN-first then ZH catch-up (matches landing-page pattern)? | Product |
| 5 | Counsellor / parent mode (printable PDF of the checklist for a parent-teacher meeting)? | Product |

## 8. Risk and edge cases

- **Curriculum drift.** Provincial curricula update on multi-year
  cycles. The manifest carries `generated_at` so a stale recommendation
  is easy to spot. Rebuild on each Sprint close.
- **Grade-12 catch-up.** A Grade-12 student who didn't take algebra
  seriously needs to start at Grade 9 content. The portal must
  surface "you should also revisit X" without making them feel they
  picked the wrong inputs.
- **The "Undecided" goal** is the default and the highest-coverage
  output; some students will pick it just to see everything. That's
  fine — the union of all goals *is* the existing topic-organised
  corpus.
- **Region overlap.** A student in Grade 11 BC who is doing the
  Foundations stream (not Pre-Calc) is a real cohort but not the one
  the SGs target. Path A handles this by carrying a "stream" sub-input
  for BC; Path B handles it conversationally.

## 9. References

- HS Math product spec: [`subjects/high_school_math.md`](subjects/high_school_math.md)
- HS Math audit (sprint state): [`../High School Math/AUDIT.md`](../High%20School%20Math/AUDIT.md)
- Build-index conventions: [`../scripts/build-index.py`](../scripts/build-index.py)
- Unit-nav generator (reused logic): [`../scripts/inject-unit-nav.py`](../scripts/inject-unit-nav.py)
- Landing-page chrome (ZH toggle, accordion patterns): [`../index.html`](../index.html)
- Sources (verbatim provincial curricula extracted for the syllabus-map): [`sources/`](sources/)
