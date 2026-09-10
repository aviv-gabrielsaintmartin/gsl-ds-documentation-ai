# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 10 September 2026._

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

**Say which components can actually be built on web, using the web code as the
source.**

The last attempt at this list came from the component docs and was wrong for
five of thirteen. The web repo is on your machine and is ground truth. The real
work is name matching — Figma says `Bar graph`, the code says `barchart`.

Half a day. Nothing needed from you.

Tasks are ordered by **what goes wrong if we don't fix it**, not by what's
quickest. **Fear the ones where the agent breaks no rule** — a stuck agent tells
you it's stuck; a confidently wrong one doesn't.

**Worth carrying forward.** The component docs' `Figma | Web | iOS | Android`
readiness rows are stale — five of thirteen wrong against the web source code.
Don't trust that row anywhere.

---

## The question I'd like answered first

The energy-colour question that sat here is **largely answered** — the colours
are permitted and the French mapping is written and verified. What's left is a
check against Figma, not a question for you.

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
