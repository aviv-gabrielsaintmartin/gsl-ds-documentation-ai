# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 17 September 2026._

---

## What we're building

A written description of the GSL Design System complete enough that an AI agent
can read it and design a screen in Figma using the right components and the
right colours, with nobody correcting it.

**Deadline: end of September 2026.** What "done" means that day is defined in
one place — [project/the-project.md](project/the-project.md). Short version: two
unseen briefs, both built and scored with no rule broken.

---

## Where we are

Designing a screen is seven steps. **One of them is fully written.**

| The step | Written? |
| --- | --- |
| Define the content — from the user need | ❌ **Nothing.** No rule, no doc, no task |
| Define the components to use, and which variant | 🟡 Components written, tested cold three times. Icons now have an index and a ruleset. **What the variant axes mean is still unknown** — to you as well |
| Define what needs to be built | ✅ **Written.** An invention is declared in the run's own report, before it is scored |
| Choose the tokens — colour, text style, spacing | 🟡 **Seven of twelve kinds** have a ruleset. Five don't |
| Put them on the screen | 🟡 An agent can place a component, but can't put words in one |
| Place them per the design guidance | ❌ Written, but never checked against a real screen |
| Check the content | ❌ **Nothing**, and the scorecard can't see copy or tone either |

Plus a scoring sheet laid out as those same seven steps — four ask yes-or-no
questions, three have none and say so. **First used on run-002**, whose eight
findings are now ruled.

---

## The next task

**Done, 17 September: every component doc matches the template.** 59 of 59, from
8 that morning. 115 off-template headings are now 0 — and 64 of those 115 were
never drift at all, just the report not knowing that
`### [Variant Category Name]` is a slot that takes any name.

**Done: `Content & UX Writing` has a fixed core and a free slot.** Three rules —
`Capitalization`, `Label Formula`, `Length Limits` — are now asked of every
component and scored individually, so an audit can ask one question of all 57.
That is why the coverage figure fell from 70% to 62%: `Label Formula` is
answered by 12 docs of 57. Nothing got worse, it became visible.

**Done: three components merged with their Zeroheight pages.**
`select-card-group` 3 images → 30, `dropdown` 6 → 36,
`modal-bottom-sheet` 10 → 40. **No prose lost on any of them.**

### Then: the remaining 21 merges

**22 of 54 components now carry every image their Zeroheight page has.** The
rest are the same job, and the method is written down —
`.claude/skills/zeroheight-merge/SKILL.md`. Read it before starting; the traps
in it each cost a round of undoing.

The order, worst first:

| Component | Has | Live | Missing |
| --- | --- | --- | --- |
| date-picker | 21 | 70 | **52** |
| media-upload | 7 | 46 | **42** |
| checkbox | 6 | 42 | **36** |
| button | 18 | 52 | **34** |
| button-group | 7 | 38 | **32** |
| tabs | 9 | 35 | **30** |
| phone-number-field | 12 | 37 | 26 |
| chip-group | 6 | 32 | 26 |
| cell-content | 8 | 33 | 25 |
| action-menu | 12 | 36 | 24 |
| feedback-message | 5 | 25 | 20 |
| coach-mark · chip | 3 · 7 | 21 · 25 | 18 each |
| tag · filter-bar | 18 · 6 | 25 · 21 | 17 each |
| checkbox-group · card | 6 · 7 | 22 · 23 | 16 each |
| counter-field · carousel | 4 · 6 | 19 · 21 | 15 each |
| toggle-group · info-state · floating-button-group | 6 · 4 · 3 | 17 · 15 · 14 | 11 each |
| modal-bottom-sheet-menu · link | 17 · 17 | 21 · 21 | 9 each |
| avatar | 32 | 37 | 5 |

**Do three or four at a time.** Extract, draft, merge, then the drafts go to
your Desktop and you read them before anything lands. On the last round, three
of the four defects found were found by you reading, not by a check.

**Then: settle whether `Spacing/56` is page rhythm or forbidden.** The ruleset
says both, 83 lines apart — and the donut appears to use 56 internally.

**Then: give grid and breakpoint a ruleset an agent may read.** Half a day, and
it finishes the last thing an agent needs.

**Waiting on you in Figma:** `Donut chart` cannot place its legend below, and its
gap to the chart is fixed at 56 — above the 48 ceiling you set.

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
