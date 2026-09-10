---
name: task-next
description: Propose and run the next single task on this project, following Gabriel's do-check-next loop. Reads status.md and project/backlog.md, proposes one task in plain language with what/why/how long, waits for explicit approval, does it, then reports what changed in three lines. Triggers on "/task-next", "what's next", "next task", or a request to pick up the next piece of work.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Task — next

Runs **one turn** of Gabriel's loop. One task. Never two.

```
   pick the next task
          │
          ▼
   explain it: what, why, how long  ──►  Gabriel approves
          │
          ▼
   do it
          │
          ▼
   report what changed, in three lines
          │
          ▼
   he runs /task-check
```

Doing and checking are deliberately separate skills. He can walk away in
between — that is the normal case, not an edge case.

## Who this is for

Gabriel works design-side, not as a full-time engineer, and is the sole owner of
this repo. He has said plainly that scattered findings and private vocabulary
are what make this project hard to hold. Everything below exists to fix that.

## Step 1 — read, don't guess

Read `status.md` first, then `project/backlog.md`. Those two files are the
current state of the project. Never reconstruct it from anything in
`project/archive/` — that folder is history.

**Then run `git status`.** Gabriel edits and deletes files by hand between
sessions, and a deletion he hasn't mentioned is the one that bites: nothing in
this repo checks links, so a ruleset can end up pointing at a file that no
longer exists. An agent following a dead link is the failure this project
exists to prevent.

| What `git status` shows | Do this |
| --- | --- |
| Deleted files | Find what referenced them — `grep -rn "<filename>" .` — and say so before proposing anything. If a `-rules-ai` file pointed at it, fixing that *is* the next task |
| Uncommitted edits | Say what's unsaved in one line. Don't commit it — you don't know whether it was finished |
| Clean | Say nothing. Carry on |

This is a **check, not a task.** It costs one command; report only what it finds.

## Step 2 — propose exactly one task

Post it in this shape, and nothing longer:

| Field | Rule |
| --- | --- |
| **What** | One plain sentence. What will be different afterwards |
| **Why** | What goes wrong today. Concrete, not abstract — say which of the three failures below it is |
| **How long** | Rough. "Half a day", "twenty minutes" |
| **Needs you?** | Either "nothing from you" or the one decision required |

Then stop and wait.

**Picking which task:** take the top item from *I can start these today* in the
backlog. That list is already sorted, and the sorting rule is in the file above
it — worth re-reading rather than assuming, because it decides what you propose:

| What goes wrong today | Rank |
| --- | --- |
| **It ships wrong, and breaks no rule doing it** | Highest. Non-compliant output leaves with confidence and is only caught by looking at the screen |
| **It stops, or asks** | Middle. Nothing wrong ships, but a human had to step in |
| **The output doesn't change at all** | Nothing. Not a task — a rider on whatever next opens that file |

Then how often it comes up, then how long it takes.

**Fear the ones where the agent breaks no rule.** A stuck agent tells you it's
stuck; a confidently wrong one doesn't. Effort is the tie-breaker, never the
sort — a cheap tidy-up is not a task however cheap it is.

If an item's rank looks wrong to you, say so and re-sort the backlog before
proposing. The order is a judgement, not a fact, and it may be stale.

If the honest answer is that the next task needs a decision from him first,
propose the **question** instead of the task. One question, with a
recommendation attached.

## Step 3 — wait for approval

**Nothing is written until he says go.** Reading, searching and inspecting are
free and need no permission. Any file change does — with one standing exception:
`status.md` and `project/backlog.md` may always be updated, otherwise logging a
finding would itself need permission.

If he pushes back, take the correction and re-propose. Do not defend the
original.

## Step 4 — do it

One task. Do not fold in adjacent improvements that "are right there" — those
become backlog rows, not silent extras.

## Step 5 — report in three lines

What changed, what it means, what the check will be. Then tell him to run
`/task-check`.

## The rules that make this readable

- **No codes, ever.** Not `2b`, not `C3`, not `Rule 0`. Describe things by what
  they do: *"the check that stops the agent hand-building something that already
  exists as a component."* This applies in chat exactly as much as in files.
- **Plain language.** Short sentences. If a term needs a glossary, rewrite the
  sentence.
- **Findings go in the backlog, not in the conversation.** Anything that surfaces
  mid-task and is not the task gets written as a backlog row. Say one line in
  chat pointing at it. Never a paragraph.
- **Tables for anything compared across the same dimensions.**
- **One task at a time.** A second task in the same turn defeats the point.

## Where things get written

| File | Role |
| --- | --- |
| `status.md` | Gabriel's one page. The current task, what's next, the top question. **Never longer than one screen** |
| `project/backlog.md` | Everything else. He reads it when he wants the whole picture; overflow from `status.md` lives here |
