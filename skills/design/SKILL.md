---
name: design
description: Turn a product idea into an interface built with the GSL Design System. Asks a few plain questions to define the problem, has the person validate the goals and acceptance criteria, then designs the screen from the design system's rules — never asking which component to use — and writes it as a platform-neutral spec. Builds it where the chat can build (the iOS repo today, through /prototype), and takes feedback in the same chat. Use on "/design", on a described product idea to turn into a screen, or on feedback about a screen designed this way.
metadata:
  author: Aviv
  version: "0.3.0"
  status: draft — written 2026-09-24, never yet run
---

# Design

Turns a product idea into a **spec** — one screen described in design-system
names only — then has it built where this chat can build.

**How to call it:** `/design`, then describe what you want in your own words.

```
/design Let buyers compare two listings side by side
```

`/design` alone asks one question: _"What do you want to build?"_

## The flow

```
   /design  <what you want, in your words>
        │
        ▼
   1. PROBLEM       spec opened · questions · goals + acceptance criteria
        │           the person validates ── "change this" ──► edit, show again
        ▼ yes
   2. INTERFACE     automatic · components and tokens from references/
        │           spec completed
        ▼
   3. BUILD         only where this chat can build:
        │
        ├── in the iOS repo          → /prototype, in this same chat
        ├── in the Android repo      → no build skill yet: stop at the spec
        ├── in the web repo          → no build skill yet: stop at the spec
        └── next to Figma            → no build skill yet: stop at the spec
        │
        ▼
   FEEDBACK         any later message about the screen, in this same chat
                    → the spec is edited → rebuilt
```

**Who decides what:**

| Decision | Made by |
| --- | --- |
| What the screen is for — goals and acceptance criteria | **The person**, validated in step 1 |
| Which components, variants, tokens and icons | **This skill**, from `references/`. Never asked |
| Whether the result is good | **The person**, looking at the built screen, through feedback |

The acceptance criteria check that the screen does what was asked. They never
check that it is good. Quality is the person's judgement.

## Where everything comes from

**This skill reads only its own `references/` folder.** It runs in other
repositories, where the design-system documentation it came from does not
exist. Every path below is relative to this skill's folder.

| File | Holds |
| --- | --- |
| `references/spec-rules-ai.md` | **The spec format.** Read it in full before writing a spec. When it and this file disagree, it wins, and the disagreement is a defect in this file |
| `references/components-rules-ai.md` | **Which component.** All of it: **Which component**, **Platform limits**, **Never select**, **The inventory**, **When nothing fits** |
| `references/component-variants.md` | Every component's **Variants & Modifiers** — the only place a variant name comes from. Headings sit one level lower than in the source doc |
| `references/color-rules-ai.md`, `typography-rules-ai.md`, `spacing-rules-ai.md`, `radius-rules-ai.md`, `shadow-rules-ai.md`, `border-width-rules-ai.md` | Which tokens are allowed. For colour, `color-rules-ai.md` picks the **family** only |
| `references/background.md`, `surface.md`, `border.md`, `content.md`, `scale.md` | **Which colour token inside a family**, by *When to use · Don't use for*. Value tables left out |
| `references/icons-rules-ai.md` | Icons |
| `references/components-ios-map.md`, `references/tokens-ios-map.md` | What iOS can build, and the iOS name of each design-system name |

**The references are generated, never edited here.** If one seems wrong, say so
in the hand-off. Do not work around it.

**Where `spec-rules-ai.md` sends you to a component's full doc**, use
`component-variants.md`: it holds every component's variants, and nothing else
from the doc is needed to write a spec.

**Where a spec is saved:** `~/gsl-specs/spec-NNN.md`, one folder outside every
repository, numbered as **Where specs live** in `spec-rules-ai.md` says. Never
inside the repo the chat is opened in: in the iOS repo that is a throwaway
prototype branch, and the spec is the one thing meant to last. Create the
folder if it does not exist.

## Who you are talking to

A product manager or a designer. **Not an engineer.**

- **Plain language.** Never a file path, a token name or a component name in a
  question. Say "the main button", not `Button` · `Emphasis: Primary`.
- **One question per message.** Wait for the answer before the next one.
- **"I don't know" is a full answer.** Record it as an `open` assumption and
  move on. **Never stall**, and never ask the same thing twice.
- **Never ask which component to use.** A preference the person volunteers is
  recorded word for word in **Source** and treated as a wish: follow it when the
  rules allow it, and add an assumption saying so either way.
- **Every interface word in the idea is a wish, never a constraint** — "banner",
  "pop-up", "card", "list", "dropdown", whether or not it names a real
  component. People describe ideas in interface words. **Such a word never rules
  a component out.** Design from the need behind it: what the user must see,
  do, and when.

## Step 1 — the problem

**This step decides what the screen is for. It never names a component, a
token, a layout or a screen element.**

### Open the spec first

Before any question, create `~/gsl-specs/spec-NNN.md` with the header table and
**Source**. **Status** is `draft`. **Source** is the person's words quoted in
full, or a link to the file they gave. **Word for word — never reworded, never
tidied, never completed.** Tell the person the spec number.

**Why first:** a source written down after the answers exist drifts towards
them, and then nothing measures the spec against what was asked.

### Find out where this chat can build

Check before asking anything. It answers the platform question for most people.

| Check | Means |
| --- | --- |
| `SeekerApps/SeLoger/SeLoger.xcodeproj/project.pbxproj` exists in the current folder | **iOS.** The build is `/prototype`, in this chat |
| Anything else | No build is possible here. Ask question 9 to choose components for the right platform, then stop at the spec |

### The questions

Ask **only the questions the source does not already answer**, in this order.
Skip a question the source answers, and say which of their sentences answered
it. **Never more than nine.**

| # | Ask, in plain words | Lands in |
| --- | --- | --- |
| 1 | Who will use this? A buyer, a renter, a seller, an agent… | **Assumptions**, and the wording of every goal |
| 2 | What problem does it solve for them? What happens today instead? | **Goals** |
| 3 | When it works, what can they do that they cannot do now? | **Goals** — one goal per thing they can do |
| 4 | Is there any data or research behind this — numbers, feedback, a study? | **Assumptions**, in the **Why** column of the goals it supports. No data is recorded as `open` |
| 5 | Where does it live — a new screen, or part of an existing one? What is on that screen today? | **Assumptions** |
| 6 | What must it show? Which real information does it use? | **Assumptions** now, **Data** in step 2 |
| 7 | Looking at the finished screen, what would tell you it works? | **Acceptance criteria** |
| 8 | Which brand? | Header **Brand**. `SeLoger` when unanswered, as an `open` assumption |
| 9 | Which platform is this for — iOS, Android, web, or Figma? **Skipped when the check above found one** | One assumption, and header **Width** |

**Question 7 must yield things visible on the screen.** A business metric — "more
leads" — cannot be checked by looking at a screen. Record it as an assumption
about the goal it supports, then ask one follow-up: _"What would someone see on
the screen that makes that likely?"_ The follow-up does not count towards the
nine. With no answer, write the criterion yourself and mark it `assumed`.

**The platform shapes the choices in step 2. It never enters the spec.** Record
it as one assumption: `Components were chosen to be buildable on <platform>`.
**Width:** iOS and Android are `mobile` unless the person says tablet. Web and
Figma use `mobile`, as an `open` assumption.

### Where the answers go

- **The answers are part of the source.** Append them to **Source** as a quoted
  list headed `Answers given on YYYY-MM-DD`, each answer word for word after its
  question. What they state counts as `source` in the **From** column.
- **Anything you infer is `assumed`**, and has a row in **Assumptions**.
- Write **Goals**, **Acceptance criteria** and **Assumptions** exactly as
  `spec-rules-ai.md` defines them. Every goal has at least one criterion.
- **Screen** and **Inventions** say `None.` for now. Add the change log's
  creation row. **Save the file before validating** — a person who leaves at
  validation leaves a spec that can be resumed.

### Validate

Show, in plain words, with no component or token names:

- each goal, as one sentence of what the user can do
- under each goal, its acceptance criteria
- the assumptions that change a goal or a criterion — leave out the rest

Then ask one question: **_"Is this what the screen must do?"_**

| Answer | Do this |
| --- | --- |
| **Yes** | Add a change log row: `Goals and acceptance criteria validated`, the person's words quoted, every goal in **IDs**. Set any assumption behind an `assumed` goal or criterion to `confirmed — <person>, <date>`. Go to step 2 **without asking again** |
| **A change** | Edit what it names. Add a change log row. Show the whole list again and ask the same question |
| **The person leaves** | Stop. The spec stays with **Screen** `None.`, which `spec-rules-ai.md` allows. `/design ~/gsl-specs/spec-NNN.md` resumes here |

**Validation is never implied.** Silence, or "looks fine so far", is not a yes
to the whole list. Ask again.

## Step 2 — the interface

**Automatic. Ask the person nothing in this step.**

**Never read anything outside `references/`** to choose — not the repo you are
in, not its components, not the web. A component the current repo happens to
contain is not a design-system component unless `components-rules-ai.md` lists
it in **The inventory**.

### Choosing for the platform

`components-rules-ai.md` says, under **Web, iOS and Android**: _if your target
platform is web, iOS or Android, ask before selecting._ The build check and
question 9 are that ask. Apply this table to every component and token chosen.

**For iOS**, look up the name's status in the iOS maps:

| Status in the map | Do this |
| --- | --- |
| `proved` | Use it |
| `guessing` | Use it. Add an `open` assumption: `<name> is assumed to exist on iOS; the pairing is unconfirmed` |
| `not found` | **Choose another component or token the rules allow for the same problem, if one fits.** If none fits, keep it and add an `open` assumption: `<name> may not exist on iOS`. The map says `not found` does not prove the app lacks it |
| `not for iOS` | **Never select it.** Use the replacement the rules or the map name |

**For Android or web**, no name map exists yet. Apply **Platform limits** in
`components-rules-ai.md` only, and add one `open` assumption:
`No name map exists for <platform>; whether each component exists there was not checked`.

**For Figma**, apply the **Figma** part of **Platform limits**.

### Choosing components and tokens

**Reuse before invention.** Use an existing component wherever one fits. Build
something new only when nothing does, and declare it.

1. For each goal, find its problem under **Which component** in
   `components-rules-ai.md`, and pick from what that problem names. **Match the
   need, never the person's wording**: "a banner that greets them on arrival" is
   a short message, shown on arrival, that can be closed — look it up as that.
2. Set only the variants that differ from the default, or that the rules
   require stating. Names come from `component-variants.md`, never invented.
3. A library component's **Tokens** cell is `—`. Tokens are chosen only for
   `text` and `composed` rows, from the token rulesets. **Colour takes two
   reads:** `color-rules-ai.md` for the family, then that family's page for the
   token, by its *When to use* and *Don't use for*. A token its page marks
   **Not used** is never chosen.
4. **Before writing any `composed` element, name the component the rules give
   for its need**, under **Which component**, and check it against the need.
   Only a reason found in the need rules it out — what the user must see, do,
   or when. **"The source says banner" is never a reason.** If the rules' answer
   fits, use it: an existing component always beats a built one.
5. Anything still built from parts is `composed`, with an **Inventions** entry
   holding all three parts **When nothing fits** requires. A missing part means
   the whole invention is undeclared. Its **Ruled out** names the component from
   point 4 first, with its reason from the need.
6. **Copy you wrote is an assumption.** Copy quoted from the source is not. No
   rule covers copy yet: write plain, short, sentence-case strings and flag each.
7. **Every validated criterion must be true of the screen.** If one cannot be,
   never drop it quietly — say so at hand-off, naming it.

Add a change log row for the screen, naming every block ID.

### Check your own spec before building

- [ ] All eight sections present, in order. An empty one says `None.`
- [ ] Every component name is in **The inventory** of `components-rules-ai.md`.
- [ ] Every variant axis and value is in `component-variants.md` under that component.
- [ ] Every token is allowed by its ruleset, and colour is in slash form.
- [ ] No raw value, no platform name, no destination, no file path inside an app.
- [ ] Every element serves a goal. Every goal has a criterion.
- [ ] Every `composed` element's **Ruled out** starts with the component the rules give for its need, ruled out by the need — never by the person's wording.
- [ ] A block that goes on an existing screen says which screen, and what it sits above or below.
- [ ] Every validated criterion is true of the screen.
- [ ] Every decision the source did not make is in **Assumptions**.

**This check is yours, and it is not proof.** No script checks a spec yet.

## Step 3 — build

**In the iOS repo:** run `/prototype` in this same chat, with this request —
absolute paths filled in:

```
Build the screen described in <~/gsl-specs/spec-NNN.md, absolute>.
Translate its component and token names with <this skill's
references/components-ios-map.md> and <references/tokens-ios-map.md>.
Build every row of its Screen section in order. Place each block inside the
screen the spec names, where it says — never as an overlay on the whole app,
never over the splash screen or a system prompt. Report anything you could not
build by its element ID. Never change the spec.
```

**Anywhere else:** stop at the spec. Tell the person which repo to open this
chat in to build it, and that `/design ~/gsl-specs/spec-NNN.md` picks it up
there. For Android, web and Figma, say plainly that no build exists yet.

Then tell the person, in plain words:

- the spec number, and how many assumptions are still `open` — the two or three
  that matter most
- anything the build reported it could not build
- that **quality is theirs to judge**, and they can say what to change right here

## Feedback — in this same chat

**Once a spec has been designed in this chat, every later message about the
screen is feedback on that spec**, until the person asks for something new.
Feedback edits the spec, then the screen is rebuilt from it. **Never edit the
built screen directly** — a change made only there is lost at the next rebuild.

Size the request first. **Only the largest asks anything.**

| Size | Example | Do this |
| --- | --- | --- |
| **Adjust one thing** | "Make the title bigger" · "Change the button text" | Change that row. Rebuild. **No question**, and say what changed in one line after |
| **Add or remove something** | "Add a share button" · "Remove the map" | Change the rows. Rebuild. Then one line saying what was added or removed |
| **Change what the screen is for** | "Also let them book a visit" | One question: **_"Should I add this to this screen's goals, or start a new idea?"_** Then do what they say — new goals are validated as in step 1 |

For every size, follow **How feedback is applied** in `spec-rules-ai.md`: find
the element by its ID, change only its row, add a change log row quoting the
person, update **Last changed**. The person never sees the change log. It costs
them nothing.

**"Bigger", "bolder", "more space" mean the next allowed step, never a raw
value.** A title gets the next text style up that `typography-rules-ai.md`
allows. If no allowed step exists, say so, and say what the closest one is.

**A library component's own look cannot be changed** — its tokens are `—` by
rule. When feedback asks for that, say so in plain words, and offer the
component's variants that come closest.

**Status becomes `agreed` only when the person says the spec is agreed.**
Validating the goals is not agreeing the spec.

## What this skill never does

- **Never reads outside `references/`** to choose a component or a token.
- **Never rewords the source**, and never writes one.
- **Never asks which component, token or layout to use.**
- **Never rules a component out because of the person's wording**, and never builds what an existing component already does.
- **Never designs a screen before the goals are validated.**
- **Never writes a platform name into a spec**, even though it read one in a map.
- **Never edits the built screen**, only the spec.
- **Never saves a spec inside the repo it runs in.**

## Known gaps

Stated so nobody reads this file as more finished than it is.

- **Never run.** Everything here is reasoning. Expect the first run to find
  defects, and fix them in the source this skill is generated from.
- **`/prototype` does not read specs yet.** The request above points it at the
  file in plain language. **Guessing** that it follows it well.
- **Only iOS can build.** Android, web and Figma stop at the spec.
- **Links inside `references/` were removed** where their target was not
  copied. The text remains; the target does not.
- **No script checks a spec.** The self-check is the only check.
- **No rule covers copy or content.** Every string this skill writes is an
  assumption.
- **Spacing guidance is unverified.** A block's gap and padding are the
  skill's choice, not a checked rule.
