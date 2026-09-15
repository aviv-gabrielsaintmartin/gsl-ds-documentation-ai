# The project

_One page for anyone who needs to follow this work. What it is, what "done"
means in September, and where it stands._

_Written for a person. It describes the project; it is never the source of truth
for how anything is built. Updated 15 September 2026._

---

## What this is for

The GSL Design System is written for people. This project rewrites it so an AI
agent can read it too.

The goal is an agent that designs a screen using the right components and the
right colours, with nobody correcting it.

_This section is deliberately thin. Gabriel will enrich it — the business case
is his to write._

---

## What "done" means by end September 2026

A date says when. It does not say what. So the deadline has an objective, and it
can be verified by someone who did not build any of this.

> **An agent builds a screen from a brief it has never seen. A second, separate
> agent scores it. Nothing breaks a design-system rule, except inventions the
> builder declared. Two briefs, both unseen, both clean.**

Three words in that sentence have a precise meaning here:

| Word | What it means |
| --- | --- |
| **Brief** | The screen described in words — its purpose and its content. No design decisions, no layout |
| **Unseen** | Written after the documentation was, so nothing was written to suit it |
| **Clean** | Every question on the score sheet answers "no rule broken". Inventions are allowed when declared |

Two briefs rather than one, on purpose. Passing once may prove the documentation
covers that screen. Passing on a second, different screen is what suggests it
covers the design system.

### What this deadline does not include

Stated so nobody assumes otherwise:

- **Design quality.** Only "did it use the right things" is judged. Whether the
  screen is any good comes later, and is not yet written down anywhere.
- **The two content steps.** Deciding what a screen should say, and checking what
  it says, are untouched.
- **Web, iOS and Android.** Figma only.
- **A tool anyone can run alone.** Each run is still driven by hand.

---

## What has to be true

_Under review. These seven steps cover designing a screen inside the design
system. The project's real scope is wider — enabling AI across the design
process — and this table will widen with it._

Designing a screen is a sequence. Each step needs the ones before it, so an
unwritten early step blocks everything after it.

| The step                                        | Where it stands                                                                          |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Define the content, from the user need          | **Nothing written**                                                                      |
| Choose the components, and which variant        | Written, and tested cold three times. **What the variant options mean is still unknown** |
| Decide what has to be built new                 | **Written.** Anything invented must be declared before it is scored                      |
| Choose the tokens — colour, text style, spacing | Seven of twelve kinds have rules an agent may read. Five do not                          |
| Put them on the screen                          | An agent can place a component. It cannot yet put words inside one                       |
| Place them per the design guidance              | Written, but never checked against a real screen                                         |
| Check the content                               | **Nothing written.** The score sheet cannot see copy or tone either                      |

Each step is judged by yes-or-no questions on a score sheet. Four of the seven
steps have questions. Three have none, and the sheet says so.

**Three runs have happened so far, all on the same brief. The most recent broke
no rule** — the first to do so.

---

## What we need from others

Everything here needs a change in Figma, or a decision. None of it can be fixed
by writing documentation.

| What                                                                                                                    | Why it blocks                                                                                               | Who                                          |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **The donut chart's legend cannot sit below the chart**, and its gap to the chart is fixed at 56 — above the 48 maximum | The legend cannot fit a phone width. Every agent so far has worked around it by hand                        | Figma library owner                          |
| **Switching the donut chart's data parts off does nothing.** The properties report as applied and change nothing        | An agent asked for a three-part chart gets a five-part one, and is told it worked                           | Figma library owner                          |
| **There is no component for a GES rating.** The energy tag covers only the DPE ladder                                   | A French listing shows two ratings. An agent building one either misuses the energy tag or invents a ladder | Figma library owner                          |
| **The energy filter slider ships on web and is not in the Figma libraries**                                             | An agent asked for one has working code it cannot use and nothing to place                                  | A decision: add it, or let agents compose it |

This section is empty whenever nothing is blocked.

---

## Where the detail lives

| For | Read |
| --- | --- |
| Where the project is this week | [status.md](../status.md) |
| Every task, question and finding | [backlog.md](backlog.md) |
| Why the project is shaped this way | [decisions.md](decisions.md) |
| How a generation run becomes a report | [how-a-run-is-reported.md](how-a-run-is-reported.md) |
