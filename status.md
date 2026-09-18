# Status

_The only page you need. Everything else in this repo is reference material for
agents — looked up, never read through._

_Updated 18 September 2026._

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

**Done, 18 September: four more merged, and the merge script rebuilt.**
`date-picker` 21 images → 70, `media-upload` 7 → 46, `checkbox` 6 → 42,
`button` 18 → 52. No prose lost, none duplicated, no `zeroheight.com` link
gained, every picture on every page placed.

**The first run of those four looked clean and was not.** `checkbox` silently
lost its three error-state tables — 12 pictures — and the draft script still
reported 42 of 42 placed. Eleven faults came out of chasing it, all fixed and
all written into the skill.

**Two things nobody was checking, now checked on every run:**

- **What the page gave against what the doc holds.** This is the count that
  found the checkbox damage. Nothing had ever compared the two.
- **Whether a file is actually a picture.** **36 files across 12 components are
  Figma JSON saved under a `.png` name** and can never render.
  `scripts/check-links.py` cannot see them — it asks whether a file exists,
  never what it is. Three were `date-picker`'s and are gone; 33 remain, and
  they are in the backlog.

### Done: every merge, and the broken pictures with them

**All 25 components that had an image gap now carry every picture their
Zeroheight page holds.** Done 18 September in four batches, each read by you
before anything landed.

| | |
| --- | --- |
| Components merged | **25** |
| Pictures added | **371** |
| Sentences lost | **0**, on every one |
| Sentences duplicated | **0** |
| `zeroheight.com` links gained | **0** |

Biggest gains: `coach-mark` 3 pictures to 21, `floating-button-group` 3 to 14,
`info-state` 4 to 15, `counter-field` 4 to 19, `button-group` 7 to 38,
`date-picker` 21 to 70.

**The merge script took 28 fixes to get there, and the extractor one.** Nine of
those were found by you reading the drafts, not by any check. Two were found by
re-running components already merged — including one where a fix of mine
destroyed 12 pictures silently. Every fix is commented at the line that caused
it, naming the component and the damage.

**Three things also went, all from the old Confluence migration:**

- **36 files that were not pictures.** Figma node JSON saved under a `.png`
  name, each written into a doc as an image, each rendering broken. Eleven were
  replaced by the pages' own sections; 25 were removed outright, file and
  reference together. **None are left.**
- **60 `<!-- Source: …confluence… -->` lines.** Nothing read them.
- **Every H1.** Each doc opened by repeating its own filename, so you read the
  name twice. Gone from all 62 docs and from the template.

**What is left of this job:** three components — `select-card-group`,
`dropdown` and `modal-bottom-sheet` — were merged on 17 September, before any
of the 29 fixes. Re-running `modal-bottom-sheet` placed **2 pictures the old
run had left behind**. All three are in the backlog.

### Done: every doc now says which variant to pick

**57 of 57.** `floor-selection` and `listing-summary` were the last two blank; *Variant flow* is at 100%. Both written from each doc's own words, no Figma property named, so they stay platform-neutral.

**It came out of assessing the decision-tree article you sent.** The answer was no new trees — this repo already has both layers the article describes, as intent tables and axis lists. What it does **not** have is anything joining a doc's axis name to Figma's property name. That is now a question in the backlog.

**Those same two docs are also the only two of 57 with no `When to use` and no `When NOT to use`.** An hour's work, proposed in the backlog, not started.

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
