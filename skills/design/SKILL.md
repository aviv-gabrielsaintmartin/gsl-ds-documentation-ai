---
name: design
description: Turn a product idea into an interface built with the GSL Design System. Asks a few plain questions to define the problem, has the person validate the goals and acceptance criteria, then designs the screen from the design system's rules — never asking which component to use — and writes it as a platform-neutral spec. Builds it where the chat can build (the iOS repo through /prototype, or Figma through figma-cli), and takes feedback in the same chat. Use on "/design", on a described product idea to turn into a screen, or on feedback about a screen designed this way.
metadata:
  author: Aviv
  version: "0.4.0"
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
        ├── figma-cli connected      → built in the open Figma file
        ├── in the Android repo      → no build skill yet: stop at the spec
        └── in the web repo          → no build skill yet: stop at the spec
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
| `references/icons-rules-ai.md` | Which icons are allowed, and how to choose one |
| `references/icons-index.md` | **Every icon that exists, by exact name.** An icon name in a spec comes from here and nowhere else |
| `references/components-ios-map.md`, `references/tokens-ios-map.md`, `references/icons-ios-map.md` | What iOS can build, and the iOS name of each design-system name |
| `references/figma-map.md` | The Figma library and key of every component, token and icon. **Read only in step 3, when building in Figma.** It never decides which one to use |

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
| Otherwise, `cd ~/figma-cli && node src/index.js status` reports the daemon running | **Figma, probably.** Confirm it with question 9 — figma-cli being installed does not mean the person wants Figma. The plugin is checked in step 3, not here |
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
| 9 | Which platforms will this be built on — iOS, Android, web, Figma? More than one is a full answer. **When the check above found one**, ask only: _"Will it also be built anywhere else?"_ | One assumption, and header **Width** |

**Question 7 must yield things visible on the screen.** A business metric — "more
leads" — cannot be checked by looking at a screen. Record it as an assumption
about the goal it supports, then ask one follow-up: _"What would someone see on
the screen that makes that likely?"_ The follow-up does not count towards the
nine. With no answer, write the criterion yourself and mark it `assumed`.

**The platforms shape the choices in step 2. They never enter the spec.**
Record them as one assumption, every target named:
`Components were chosen to be buildable on <platform>, <platform>`.
**One spec serves every target.** It is built on each in any order, never
rewritten per platform. Gabriel, 2 October 2026.
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
question 9 are that ask. Apply this table to every component and token chosen,
**once per target platform**. A component must pass on every target. When one
fails on any target, choose another the rules allow for the same problem.

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
Translate its component, token and icon names with <this skill's
references/components-ios-map.md>, <references/tokens-ios-map.md> and
<references/icons-ios-map.md>.
Build every row of its Screen section in order. Place each block inside the
screen the spec names, where it says — never as an overlay on the whole app,
never over the splash screen or a system prompt. Report anything you could not
build by its element ID. Never change the spec.
```

**In Figma:** follow **Figma**, below, in this same chat.

**Anywhere else:** stop at the spec. Tell the person which repo to open this
chat in to build it, and that `/design ~/gsl-specs/spec-NNN.md` picks it up
there. For Android and web, say plainly that no build exists yet.

Then tell the person, in plain words:

- the spec number, and how many assumptions are still `open` — the two or three
  that matter most
- anything the build reported it could not build
- that **quality is theirs to judge**, and they can say what to change right here

## Figma

**Builds the spec in the Figma file the person has open, through figma-cli.**
Every component, token and icon is placed from the GSL libraries by its key in
`references/figma-map.md`. Nothing is drawn by hand that a library holds.

**When the spec's platform assumption does not name Figma**, check each
component against the **Figma** part of **Platform limits** in
`components-rules-ai.md` before drawing. Build anyway, and report each one that
fails by element ID. Never change the spec.

### What to place, in this order

```
 a row of the spec
        │
        ▼
 1. GSL library component      the spec names it ──► import by key, place it
        │ the row is text or composed
        ▼
 2. Built from GSL tokens      text, and the layout that arranges components
```

**Nothing else is placed.** Gabriel, 2 October 2026.

- **Never a component from the open file**, from a screen already in it, or
  from a library other than GSL. A file can hold an outdated copy of a GSL
  component under the same name. **Proved on 2 October 2026:** the reference
  screen in *Claude to Figma* holds a `Card` whose key is not the library's.
- **Never copy a part from an existing screen**, even one that looks right.
  Import it from the library by its key instead.
- **Why only two steps:** in the first four specs, 19 rows were library
  components, 12 were text and 9 were built. Seven of the nine were layout
  arranging library components. The other two were an illustration, which no
  rule yet lets a spec choose. No spec needed a product team's component.

figma-cli lives at `~/figma-cli` and is not on the PATH. Every command below
runs from that folder: `cd ~/figma-cli && node src/index.js <command>`.

### Before drawing — four checks

Run all four, in order. **Never draw until all four pass.**

| # | Check | How | If it fails |
| --- | --- | --- | --- |
| 1 | **The daemon is running** | `node src/index.js status` | Run `node src/index.js daemon start`, then check again. Still failing: tell the person figma-cli is not set up on this machine, and stop at the spec |
| 2 | **The plugin is attached** | `node src/index.js eval 'JSON.stringify({name: figma.root.name})'` returns the open file's name | **`Error: fetch failed` means the plugin is detached, not that the daemon is down.** **`✗ Not connected to Figma`** means Figma Desktop is closed or the plugin was never started — seen 2 October 2026 with the daemon running. Either way, ask the person to open the file to draw in, then run `Plugins → Development → FigCli`. Wait, then check again |
| 3 | **The open file is not a GSL library** | Compare the file name from check 2 with **Libraries** in `figma-map.md` | **Never draw inside a library file.** Ask the person to open or create a working file, then repeat check 2 |
| 4 | **The GSL libraries reach this file** | Import `Button` by its key from `figma-map.md` | *Not found* means the libraries are not enabled in this file. **Guessing**: no other cause has been seen. Ask the person to enable the four GSL libraries in this file, then check again |

Then tell the person, in one line, which file you will draw in. **Ask nothing
more.** They opened it.

### How to send code to Figma

- **Write each script to a file and run it:** `node src/index.js run <file>`.
  Put the file in a temporary folder, never in a repo.
- **One block per script.** A long script that fails halfway leaves half a
  block and no error you can trust.
- **A script must end by returning a value**, such as the IDs it created. Never
  open a script with a comment, and never end it with an `if/else`: the plugin
  then returns nothing, even when the script wrote something. **An empty result
  is a failure until the file proves otherwise.**
- **Wrap every script in `try/catch` and return the error.** Without it, a
  failing script returns nothing, and you cannot tell what failed.
- **Start every script by removing what it is about to create**, found by its
  ID-based name. **A failing script left three copies of its partial work**,
  seen twice on 2 October 2026. **Guessing:** the daemon retries a failed script
  three times. Read the page back after any failure, and remove what you made.
- **Use the async APIs only.** These throw in a working file, proved on 2
  October 2026:

  | Throws | Use instead |
  | --- | --- |
  | `getLocalVariables()` | `getLocalVariablesAsync()` |
  | `node.mainComponent` | `await node.getMainComponentAsync()` |
  | `node.textStyleId = id` | `await node.setTextStyleIdAsync(id)` |
  | `figma.getNodeById(id)` | `await figma.getNodeByIdAsync(id)` |
- **The plugin detaches when Figma switches files.** If a script returns
  `Error: fetch failed` mid-build, repeat check 2 before anything else.

### Where to draw

- **Create one new top-level frame** on the current page, to the right of
  everything already there. Name it `spec-NNN — <spec title>`.
- **The frame's fill is a `Background` colour token, bound, never a raw
  colour.** Choose it by role, from `background.md`. **`Background/Default` is
  the usual answer**: the base canvas behind all content. Another `Background`
  token only when the spec asks for what its *When to use* describes.
  Gabriel, 2 October 2026.
- **Never move, edit or delete anything else in the file.**
- **Width:** `mobile` 360, `tablet` 768, `desktop` 1440. **No rule sets these
  yet.** Mobile is 360 because the reference detail page in the
  *Claude to Figma* file is 360 wide, proved on 2 October 2026. Tablet and
  desktop are guesses. Say so at hand-off, as one line. Height grows with the
  content.
- **A block placed on an existing screen** goes into a **copy** of that
  screen, never the original. Gabriel, 2 October 2026. Ask the person which
  frame is the screen when the file holds more than one candidate. Duplicate
  it, place the copy to the right of everything, name it
  `spec-NNN — <spec title>`, and insert the block where the spec says.
  **A part of the copied screen is never reused** for the spec's own rows.
- **When the file has no such screen**, draw the block on its own.

### How to draw each row

**Every block** is an auto-layout frame named by its block ID. Its **Stack**,
**Gap** and **Padding** are bound to the spacing variables the spec names.

**Every element** is named by its element ID, and nested in the element its
**Inside** column names.

| Component column | Do this |
| --- | --- |
| **A library component** | Import it by its key, as **How to read a key** in `figma-map.md` says. Create an instance. Set each variant from the **Variants** column with `setProperties`, as **Matching a variant** below says. A **Pattern 2** slot is set on the nested instance, found by its key under **Exposed slots** |
| **`text`** | Create a text node. Import its text style by key and apply it. Load the style's font before writing. Import its colour variable and bind the fill. Write the copy exactly as the spec quotes it |
| **`composed`** | Build what its **Inventions** entry describes under **What is built**, part by part. Every token it names is bound, never typed as a value |
| **An icon** | Import it by its key from **Icons** in `figma-map.md`. Leave `Filled`, `Circle` and `Square` at `Off` unless the spec sets them |
| **An icon inside a component** — a button's icon, for example | Import the icon as above. Set it through the component's own icon property, the instance-swap property whose name holds `Icon`, to the icon's default variant. Never place the icon beside the component |

**A variant the spec leaves unset takes the component doc's default, never
Figma's.** Gabriel, 2 October 2026. They differ: `Button`'s doc default height is
40, and Figma's default instance is 48. Read the default from that component's
section in `component-variants.md`, and set it. When the doc names no default,
keep Figma's, and report it at hand-off.

**Matching a variant.** The spec's axis and value names come from the
component docs. **Figma's names often differ**, proved on 2 October 2026: the
spec's `Emphasis: Tertiary` is Figma's `Type: Tertiary`, and `Radius: 16px` is
`Radius: 16`. Read the instance's `componentProperties`, then match in this
order:

| Case | Do this |
| --- | --- |
| Same axis, same value | Set it |
| Same value, differing only in case or a unit | Set Figma's spelling. `Primary light` is `Primary Light`; `16px` is `16` |
| The value exists under exactly one axis with another name | Set it there. Report the renamed axis at hand-off |
| The value exists nowhere, or under several axes | **Set nothing.** Report it by element ID. Never choose a near value |

**Content inside a component's slot.** A slot such as `Card`'s `Content` is an
instance-swap property. Content cannot be placed inside an instance directly.

1. Build the content as a **local component**, in a section named
   `spec-NNN — local parts` to the right of the frame. Name it by its element ID.
2. **Swap the slot straight to that local component.** Never through a
   placeholder taken from another screen.
3. **`Card`'s `Padding` and `Slots` are not Figma properties.** The library
   `Card` holds only an empty `Content placeholder`, proved on 2 October 2026.
   - `Padding: With padding` is 8 px in the card doc. Bind `Spacing/8` as the
     local component's padding. `Without padding` binds none.
   - `Slots` needs nothing: the local component's own layout arranges the
     content.
   Report both as set on the local component, not the card.
4. After the swap, set the swapped content and every parent to hug vertically:
   `layoutSizingVertical = "HUG"`. **Proved:** without this, a slot keeps its
   old height and the text runs past the card's edge.

**Measure after layout.** A size that depends on another element, such as an
illustration as tall as the text beside it, is set only once the text has its
final width.

**Copy inside a library component** goes into that component's text
property. Never edit a text layer inside an instance by hand.

**The Behaviour column is not drawn.** A static frame cannot show it.

**Never, in Figma:**

- **Never type a raw colour, size or spacing** where a token exists. Bind the
  variable, or apply the style. A raw value breaks every brand and theme switch.
- **Never detach an instance.**
- **Never edit inside an instance** beyond its own properties and exposed
  slots. If the component cannot do what the spec asks, report it by element
  ID. Do not work around it.
- **Never draw a lookalike of a library component.** A component that fails to
  import is reported, never redrawn.

### Check the build

After the last block, read the frame back and check:

- [ ] Every element ID in the spec is a node in the frame, exactly once.
- [ ] Every library row is an instance whose main component key matches `figma-map.md`.
- [ ] No instance anywhere in the frame comes from outside the GSL libraries, except the spec's own local parts.
- [ ] Every `text` and `composed` fill, text style and spacing is bound to a token.
- [ ] Nothing outside the new frame and its local parts changed, and no stray copy of a failed script is left on the page.
- [ ] **Look at the export.** Nothing runs past its container, and nothing is cut off.

Then export the frame: `node src/index.js export node <frame-id> -o
~/gsl-specs/screens/spec-NNN.png`. Create the folder if it does not exist.

**At hand-off**, add to the lines step 3 already gives:

- the file name and the frame's name
- every element ID that could not be built as the spec says, and why
- the frame width used, since no rule sets it yet

**This check is yours, and it is not proof.** A second agent scoring the frame
against the design system is not part of this skill.

## Feedback — in this same chat

**Once a spec has been designed in this chat, every later message about the
screen is feedback on that spec**, until the person asks for something new.
Feedback edits the spec, then the screen is rebuilt from it. **In Figma,
rebuild means redrawing the block that holds the changed row**, replacing the
old one in the same frame. **Never edit the
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
- **iOS and Figma can build.** Android and web stop at the spec.
- **The Figma build has never been run** by anyone but its author.
- **No rule sets a Figma frame's width.** The widths in **Where to draw** are defaults.
- **Links inside `references/` were removed** where their target was not
  copied. The text remains; the target does not.
- **No script checks a spec.** The self-check is the only check.
- **No rule covers copy or content.** Every string this skill writes is an
  assumption.
- **Spacing guidance is unverified.** A block's gap and padding are the
  skill's choice, not a checked rule.
