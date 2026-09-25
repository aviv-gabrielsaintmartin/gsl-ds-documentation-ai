# Status

_Your one page. One screen, never longer. Everything else is in
[project/backlog.md](project/backlog.md). Updated 25 September 2026._

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
| **4. Build the screen** | iOS: `/prototype`. Android: `/vibe` | Neither reads a spec yet. One iOS run misplaced the block |
| **5. Check the result** | A scorecard, written for Figma | Nothing checks an app build |

**One brief has gone through stations 1 to 4, on iOS.** Proved: `spec-002`,
24 September. It has never gone through all five.

---

## The next task

**Task A — fix the rules Test 1 exposed.** Icons into the design skill, a tag
rule by role, then regenerate the skill. Details in the backlog.

**Then Task B:** the schools PRD with its content, and Test 2 on iOS.

**Test 1, 25 September:** same structure as the designer's screen. The gaps
were in the PRD's content and in two rules.

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
