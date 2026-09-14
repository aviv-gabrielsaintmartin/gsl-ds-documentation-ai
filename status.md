# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 12 September 2026._

---

## What we're building

A written description of the GSL Design System complete enough that an AI agent
can read it and design a screen in Figma using the right components and the
right colours, with nobody correcting it.

**Deadline: end of September 2026.** Only "did it use the right things" counts.
"Is it a good design" comes later, on purpose.

---

## Where we are

Designing a screen is seven steps. **One of them is fully written.**

| The step | Written? |
| --- | --- |
| Define the content — from the user need | ❌ **Nothing.** No rule, no doc, no task |
| Define the components to use, and which variant | ✅ Written, and tested cold three times |
| Define what needs to be built | ✅ **Written.** An invention is declared in the run's own report, before it is scored |
| Choose the tokens — colour, text style, spacing | 🟡 **Seven of twelve kinds** have a ruleset. Five don't |
| Put them on the screen | 🟡 An agent can place a component, but can't put words in one |
| Place them per the design guidance | ❌ Written, but never checked against a real screen |
| Check the content | ❌ **Nothing**, and the scorecard can't see copy or tone either |

Plus a scoring sheet, now laid out as the same seven steps. Each step asks a
short list of yes-or-no questions; four steps have questions, three have none and
say so. Never yet used on a real run.

---

## The next task

**Done: run-002's eight findings are ruled, four fixed the same day.** Three
`ruleset gap`, two `agent error`, two `accepted`, one `library defect`. Ruled
cold, in a chat that saw neither the one that built the run nor the one that
scored it. Three verdicts came out differently from what the report expected.

**Waiting on you in Figma:** `Donut chart` cannot place its legend below, and
its gap to the chart is fixed at 56 — above the 48 ceiling you set. On the list.

**Next: icons — 455 of them, none documented.** Two more run-002 findings landed
on one `info` icon: right icon, wrong variant, and no button around it. Nothing
in any ruleset covers either. **Smaller than it looked** — 454 of 455 names are
unique, so it's an index plus eight flagged names, not a catalogue. Three tasks:
the index, the rule that an icon is never interactive alone, and what the
variant axes are for.

**Then: settle whether `Spacing/56` is a page-rhythm token or a forbidden one.**
Twenty minutes. The spacing ruleset says both, 83 lines apart — and the donut
appears to use 56 internally, which would make "no component does" false.

**Then: give grid and breakpoint a ruleset an agent may read.** Half a day, and
it finishes the last thing an agent needs.

How tasks are sorted, and why, is at the top of
[the backlog](project/backlog.md).

---

## The question I'd like answered first

> **Still open: the energy filter slider ships on web and was never added to the
> Figma libraries.** An agent asked to build one has working web code to copy
> and no Figma component to place. Get it added, or tell agents to compose it?

Around two dozen questions are waiting, all in
[project/backlog.md](project/backlog.md). I'll bring them one at a time.

---

## How we work

```
   pick the next task
          │
          ▼
   I explain it: what, why, how long  ──►  you approve
          │
          ▼
   I do it
          │
          ▼
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

Two commands drive it:

| Type this | What happens |
| --- | --- |
| **`/task-next`** | I propose one task — what, why, how long, whether it needs you. **I wait for your go.** Then I do it and report in three lines |
| **`/task-check`** | I verify it actually worked and tell you pass or fail. Passed → logged, saved, next task named. Failed → a sub-task to fix it becomes next |

**One task, one chat.** Start each task in a new conversation with `/task-next`.
You never have to watch anything — `/task-check` finishing is the signal. Stay
put within a task, and for conversations like this one.

**Nothing is written without your approval.** Reading and searching are free.
The handful of exceptions — this page, the backlog, and adding a file's name to
a list of files — are written down in one place, `CLAUDE.md`.

### How the work gets saved

**One task = one commit.** No branches, no pull requests — you work alone, and
the loop already does what a branch was doing.

| When | What happens |
| --- | --- |
| The check **passes** | I commit and push straight away. That's your backup — if the laptop dies, the work exists |
| The check **fails** | Nothing is committed, and I'll tell you the work isn't saved yet |

Committing and pushing only ever **add** — they can't lose anything, which is
why they don't need your approval. The operations that could lose something —
undoing, deleting, rewriting history — **always ask you first, every time.**

**Anything that surfaces mid-task gets written into the backlog, not into the
conversation** — as a task I can do, a question only you can answer, or a note.
That's the rule that stops findings from disappearing into chat.

---

## Two files, and that's all

| File | What it's for |
| --- | --- |
| **`status.md`** — this page | Where we are, what's next. Never longer than one screen |
| [**`project/backlog.md`**](project/backlog.md) | Everything else — every task, every open question, every finding. Open it whenever you want the whole picture |
