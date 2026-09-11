# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 11 September 2026._

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

**Done: a simulator now has a routing entry.** A block of controls that computes
a live result is no Pattern and no Experience — all 21 and all 11 were checked,
not assumed — so the rules say compose it and declare it. Saved and pushed.

**Next: say where a declaration physically lives.** Every invention rule ends
with "declare it — say what you built and what you ruled out". None of them says
**where that statement goes**: a note beside the Figma frame, a code comment,
the reply itself. So the record is the part that gets dropped — and the record
is the only thing that makes an invention reviewable. Half a day, and **one
decision from you**: what counts as "the output" in Figma.

The chart-sizing task you parked is still parked. Neither the Legend fix nor
this one settled it — both looked like they might, both were near misses, and
the reasons are written out in the backlog.

**Tasks are sorted by one question first: does it change what lands on the Figma
canvas?** That's the only deadline. Within that, **fear the ones where the agent
breaks no rule** — a stuck agent tells you it's stuck, a confidently wrong one
doesn't.

---

## The question I'd like answered first

The energy-colour question that sat here is answered; what's left of it is a
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
