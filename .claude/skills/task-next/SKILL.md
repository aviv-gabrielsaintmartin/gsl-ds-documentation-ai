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
| **Why** | What goes wrong today. Concrete, not abstract — name the step of designing it stops, and what happens instead |
| **How long** | Rough. "Half a day", "twenty minutes" |
| **Needs you?** | Either "nothing from you" or the one decision required |

Then stop and wait.

**Picking which task:** the backlog's tasks sit under the step of designing they
break, in order. The next task is the **earliest step's topmost row that is due
by September and has an empty *Blocked by***.

The sequence is the sort, because each step needs the ones before it:

| | Step |
| --- | --- |
| | Define the content — from the user need |
| | Define the components to use, and which variant, in one move |
| | Define what needs to be built |
| | Choose the tokens — colour, text style, spacing |
| | Put them on the screen |
| | Place them according to the design guidance |
| | Check the content |

Three groups sit outside the steps. **Every step** holds rows that break
reaching the rules, whichever step you are on. **Scoring a finished screen**
holds rows that break finding out which step broke. **Keeping the repo usable** holds
real work that changes nothing an agent designs — it changes whether a person or
a session can find their way around.

**A row names the step that fails, not the kind of file being fixed** — sort by
the symptom, not by the folder.

Two tie-breakers decide between rows at the same step, and neither is ever the
sort: **how bad it is when it goes wrong** (worst is a wrong screen with nothing
to tell you — the agent obeyed every rule we wrote and the output still isn't
compliant, so you only find out by looking), then **how often it happens**.

**Fear the silent ones.** An agent that stops tells you it stopped; a
confidently wrong one doesn't. **Effort is never a reason** — a cheap tidy-up is
not a task however cheap it is, and a hard task is not demoted for being hard.

**Two steps have no rows.** That is a gap, not a clean bill of health — nothing
has looked at them. Don't quietly treat an empty step as done.

If a row looks like it sits under the wrong step, say so and re-place it before
proposing. Which step a row breaks is a judgement, not a fact, and it may be
stale — or the step it really breaks may not be written yet, which is worth
saying out loud.

If the honest answer is that the next task needs a decision from him first,
propose the **question** instead of the task. One question, with a
recommendation attached.

## Step 3 — wait for approval

**Nothing is written until he says go.** Reading, searching and inspecting are
free and need no permission. Any file change does, apart from the short list in
*What may be changed without asking* in `CLAUDE.md` — the only place that list
is written.

If he pushes back, take the correction and re-propose. Do not defend the
original.

## Step 4 — do it

One task. Do not fold in adjacent improvements that "are right there" — those
become backlog rows, not silent extras.

## Step 5 — report in three lines

What changed, what it means, what the check will be. Then tell him to run
`/task-check`.

## The rules that hold here

- **Findings go in the backlog, not in the conversation.** Anything that surfaces
  mid-task and is not the task gets written as a backlog row. Say one line in
  chat pointing at it. Never a paragraph.
- **One task at a time.** A second task in the same turn defeats the point.

**How to write any of it** — the proposal, the report, every line of chat — is
*How to write* in `CLAUDE.md`. That section is the only place those rules live.

## Where things get written

| File | Role |
| --- | --- |
| `status.md` | Gabriel's one page. The current task, what's next, the top question. **Never longer than one screen** |
| `project/backlog.md` | Everything else. He reads it when he wants the whole picture; overflow from `status.md` lives here |
