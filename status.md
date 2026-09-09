# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 9 September 2026._

---

## What we're building

A written description of the GSL Design System complete enough that an AI agent
can read it and design a screen in Figma using the right components and the
right colours, with nobody correcting it.

**Deadline: end of September 2026.** Only "did it use the right things" counts.
"Is it a good design" comes later, on purpose.

---

## Where we are

Teaching the agent four things. Two and a half are done.

| What the agent needs to know | Done? |
| --- | --- |
| **Which component to use** — that a label-and-price pair is a Cell Content row, not a hand-drawn box | ✅ Written, and tested cold three times |
| **Which version of it** — which size, which state | ✅ Written |
| **Which colours, text styles and spacings it may use** | 🟡 **Seven of twelve kinds.** Colour, text, spacing, sizing, corner radius, shadow and border thickness are done. Five kinds still have no rules |
| **How the page is laid out** — margins, rhythm, column widths | ❌ Written, but never checked against a real screen |

Plus a scoring sheet that marks a finished screen against all of the above.
Written, never yet used on a real run.

---

## The next task

**Record the Figma text-field names for each component.**

Today an agent can place a Cell Content row but cannot put words into it. Not one
GSL component exposes a text property — every string has to be typed into a
nested layer whose name appears in no ruleset and no registry. In the test, every
piece of text came from reading Figma live, not from this repo.

A day's work. **Needs Figma Desktop open**, so tell me when that suits you.

After that: archive the eight old files, then fix the three component entries
that currently dead-end into a file agents aren't allowed to open.

---

## The question I'd like answered first

> **Who owns the energy-rating (DPE) colours?** A French property listing must
> show a seven-step energy scale. No GSL component does that, the colours belong
> to another team, and our own rules point agents at a colour family they also
> forbid. In the test the agent produced a grey ladder — technically compliant,
> legally and visually wrong.

There are around two dozen questions waiting in total. They're all listed in
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

**Nothing is written without your approval.** Reading and searching are free.

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

Three commands are all you ever need:

```
git status            # what's changed but not saved
git log --oneline -5  # the last five things that happened
git revert <id>       # safely undo one of them
```

**Anything that surfaces mid-task gets written into the backlog, not into the
conversation** — as a task I can do, a question only you can answer, or a note.
That's the rule that stops findings from disappearing into chat.

---

## Two files, and that's all

| File | What it's for |
| --- | --- |
| **`status.md`** — this page | Where we are, what's next. Never longer than one screen |
| [**`project/backlog.md`**](project/backlog.md) | Everything else — every task, every open question, every finding. Open it whenever you want the whole picture |
