---
name: task-check
description: Check whether the task just done actually worked, then either log it and name the next task, or create a sub-task to fix it. Second half of Gabriel's do-check-next loop; updates status.md and project/backlog.md. Triggers on "/task-check", "did that work", "check the task", or a request to verify and close out the last piece of work.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Task — check

The second half of the loop. Answers one question: **did that actually work?**

```
   we check it worked
          │
     ┌────┴────┐
    yes        no
     │          │
     ▼          ▼
   log it    sub-task to fix it ──┐
     │                            │
     └────►  next task  ◄─────────┘
```

## Step 1 — verify it yourself first

**Verification is not a question to ask Gabriel.** Decide the depth, run it,
report what it found. Only bring him the result.

Check the actual thing, not the intention:

| Kind of task | How to check it |
| --- | --- |
| A rule was written for an agent | Read it back cold. Could an agent act on it with nothing else? |
| A file was moved or restructured | Every link that pointed at it still resolves |
| Something was deleted | Nothing left in the repo describes it as still present |
| A registry was synced | Spot-check entries against the live source |

If a claim can't be verified, say so plainly rather than reporting it as done.

## Step 2 — report the verdict

Three lines. What was checked, what was found, pass or fail. Include the
evidence — the count, the file and line, the command output. Never a bare
"done".

**Report failure as clearly as success.** A check that only ever passes is not a
check.

## Step 3a — if it worked

1. Log it. One line in `project/backlog.md`, moved to the done list with the date.
2. Update `status.md` — the current task becomes done, the next one moves up.
3. **Commit and push.** One task, one commit, straight to `main`. No permission
   needed — see the git section of `CLAUDE.md`. Commit and push only ever add,
   so nothing can be lost; he already approved the task and the check just
   verified it.
4. Name the next task in one sentence. Do not start it. He runs `/task-next`
   when he's ready.

## Step 3b — if it didn't

1. **Commit nothing.** Say plainly that the work is not yet saved.
2. Write the sub-task: what specifically failed, and what would fix it.
3. It becomes the **next** task, above everything else.
4. Do not attempt the fix in this turn. Propose, then wait.

If he wants to stop for the day with a check still failing, commit then — losing
a day's work is worse than an imperfect commit. Ask him first.

A failed check is normal and is information. Do not apologise for it, do not
re-litigate the original task, and do not quietly widen the fix.

## Step 4 — sweep the findings

Before finishing, ask: **did anything surface during this task that isn't
recorded?** Each one goes into `project/backlog.md` as exactly one of three:

| Kind | Where it goes | Example |
| --- | --- | --- |
| **I can fix it** | Task list, marked *proposed* | "Move the radius rules into the file agents read" |
| **Only Gabriel can decide** | Question list, with a recommendation | "Who owns the energy-rating colours?" |
| **Neither — just true** | Note list, closed | "The radius rules already existed and were verified" |

This is the step that stops findings from evaporating into chat. It is not
optional, and it is why Gabriel asked for this skill.

## The rules that make this readable

- **No codes, ever.** Describe things by what they do.
- **Plain language, short sentences, tables for comparisons.**
- **`status.md` never exceeds one screen.** Overflow goes to the backlog.
- **Never report something as done that wasn't verified.**
