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

**Those same two docs were also the only two with no `When to use` and no `When NOT to use`. Both are now written.** Three sections stand at 57 of 57: *When to use*, *When NOT to use*, *Variant flow*.

**`listing-summary`'s `Related Components` table is written too.** **Four sections now stand at 57 of 57** — *When to use*, *When NOT to use*, *Variant flow*, *Related*. Every component doc answers when to use it, when not, which variant, and what to use instead.

### Done: all 57 variant flows audited

**Nine faults found, seven fixed.** Two were real contradictions, four were an axis-wide rule trapped inside one branch, one was on the wrong branch, one was a gap the source had too.

**The surprise is which flows are weak.** Not the custom components — `energy-tag`, `tables`, `modal-bottom-sheet` and `listing-card` have the best ones. The weak flows are the simple components, and `phone-number-field` is the worst: its whole flow lists runtime states, so the section that should say which variant to pick says nothing. Three task rows in the backlog.

**`radio-button-group`'s contradiction is settled, your way.** The limit is readability, not a number: up to 5 in one column, 6 to 10 in two columns when labels fit 2 lines on mobile, `Dropdown` above 10. Changed in all eight places that stated the old cap.

### Done: five thin flows filled, from their own pages

**The material was already in the docs.** The flows were thin because nobody had read past `Usage`, not because the source was empty. `filter-bar`, `media-upload`, `legend` and `chip-group` gained real axes; `phone-number-field` was rewritten outright, since all four of its axes were runtime states.

**Four invented conditions were cut the same hour.** They are now visible *not documented* lines, in one backlog row — an agent that reads *not documented* asks; one that reads a plausible invention follows it.

**`Phone number field`'s breakpoint table was inverted, and you confirmed it.** Fixed in both the table and the flow: bottom sheet on narrow, dropdown on wide, matching the rest of the system.

### Done: four more components can now be reached

**`State message`, `Score tag`, `Date field` and `Floating button group` have a rule row**, each built from words already in the repo. Components with no rule: 16 → 12.

**Then three more, after you pushed back.** `Image slider`, `Loading state` and `Burger menu` are routed; `Burger menu (profil)` is forbidden on your word. **You were right about the first two** — the web code repo has real standalone components for both, which the repo's own docs never mentioned. ### Done: the check that stops the two sides drifting

**`scripts/check-rules-docs.py` compares each doc's *When NOT to use* against its ruleset row.** Sets of component names, never prose — the doc is meant to rephrase.

**It found 12 disagreements the day it was written, and five were made that same afternoon** by the new rules. All five closed. Seven predate it and are a backlog row.

**Also done:** asking the user has its own ruleset section, and `Feedback bar` versus `Feedback thumb buttons` is now your rule — a notation against a like — replacing my guess. Two open questions in `components-audit.md` are struck through and answered.

**`Button Bar` has a doc — the first written from web code, not Zeroheight.** You read it and approved the shape; the one Figma mention is cut, because a component doc is platform-neutral. **Documented: 57 → 58.**

**Fifteen selectable components still have no doc.** Five more have web code and can be written the same way. The last ten have a rule row and nothing else, and need Figma.

**Components with no rule: 16 → 0.** Every component in the four libraries can now be reached by a rule, or is forbidden on purpose with the reason written down.

**You described five of the last six from memory.** The sixth came out of its Figma properties. Two things are recorded as unknown rather than guessed: the thumb buttons have no usage rules, and the boundary between the two feedback components is read from Figma, not from any rule.

**`Menus` is forbidden provisionally, not permanently.** Your reason is in the ruleset with the date, and a backlog row carries the trigger to revisit — a provisional entry with nothing scheduled to re-open it is just a permanent one that reads as temporary.

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
