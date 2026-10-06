# Status

_Your one page. One screen, never longer. Everything else is in
[project/backlog.md](project/backlog.md). Updated 6 October 2026._

---

## The finish line

**An app demo, on iOS and Android, shown to the CPO next week.**

- One product idea goes in. A working screen in the app comes out.
- It is built from the GSL Design System, with nobody correcting it.
- **The Figma milestone is parked.** Its definition stays in
  [project/the-project.md](project/the-project.md) until you rewrite it.

---

## The five stations

```
 1. Understand  ──►  2. Choose   ──►  3. Write   ──►  4. Build     ──►  5. Check
    the need         the parts        the spec        the screen        the result
```

| Station | What exists | What is missing |
| --- | --- | --- |
| **1. Understand the need** | `/design` asks questions; you validate goals | No rule for what a screen should say |
| **2. Choose the parts** | Components ruled; colour ruled; iOS name maps | Five token kinds; variant meanings; illustrations |
| **3. Write the spec** | `specs/spec-rules-ai.md`; `spec-001`, `spec-002` | No field for where a block goes |
| **4. Build the screen** | iOS: `/prototype`. Android: `/vibe`. **Figma: `/design` itself, 2 Oct** | iOS and Android don't read a spec yet. Figma: illustration and card padding still open |
| **5. Check the result** | A scorecard, written for Figma | Nothing checks an app build |

**One brief has gone through stations 1 to 4, on iOS.** Proved: `spec-002`,
24 September. It has never gone through all five.

**New, 5 October:** [project/topic-map.md](project/topic-map.md) shows every
topic as written, partial or empty.

---

## The next task

**Audit the live web site: surfaces, cards, block titles.** Detail page,
market insights, estimation, at mobile and desktop widths. It unblocks
**Task C**, whose card and title rules you held back on 25 September:
Figma, iOS and Android alone were not enough. Your idea to test: grey is set
by contrast with the white base, not by content.

**Test 2, 25 September:** all PRD content on screen, both cases working. What
is left is rules and the iOS build. Nine gaps logged for the CPO plan.

**Yours, 6 October: rerun the schools PRD in `~/gsl-ios`, for the recorded
demo.** Three rules were written from your rulings: rows on white only, a
block title that is never a row, a larger title above titled rows. Not tested
until that run. Start with `/prototype-cleanup`, then `/design`.

---

## How we work

```
pick the next task ─► I explain it, you approve ─► I do it ─► we check it
                                                               │
                                          passed: log, save ◄──┴──► failed: fix it first
```

- **`/task-next`** proposes one task and waits for your go.
- **`/task-check`** checks it worked, then saves it.
- Nothing changes without your approval. The exceptions are in `CLAUDE.md`.
- Every finding goes into the backlog, never only into chat.
