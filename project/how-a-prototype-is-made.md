# How a prototype is made

_Written for a person, not for an agent. It **explains** how the pieces fit. It
never **specifies** anything: every rule lives in the file this page links to.
Two copies of a rule drift, and then there are two answers._

_Written 24 September 2026. Update it whenever a task changes what it describes._

---

## Start here: what this is for

**The goal: a product manager can try an idea on the real app, fast.**
They describe the idea. An agent turns it into an interface, then builds it on
the iOS simulator.

The prototype is **throwaway**. It is for ideation and testing, never for
production. **What lasts is the spec**, the written description of the interface.

---

## The flow, end to end

```
   idea, brief or PRD                          ← written by a PM or a designer
          │
          ▼
   PM skill (not built yet)                    ← asks questions, writes acceptance criteria
          │   optional: skip it for a quick idea
          ▼
   design skill (not built yet)                ← picks components and tokens from the rules
          │
          ▼
   specs/spec-NNN.md                           ← the spec: the one fixed contract
          │
          ▼
   /prototype (Aviv's iOS skill)               ← builds it in SwiftUI, on a throwaway branch
          │   looks up every name in the two iOS maps
          ▼
   the simulator  ──── "make the price bigger" ────►  back to the design skill,
                                                       which edits the spec
```

**Feedback always edits the spec, never the Swift code.** A change made only in
the code is lost at the next rebuild. The spec would also stop describing what
anyone saw.

---

## What exists today, and what does not

| Piece | State | Where |
| --- | --- | --- |
| The spec format | ✅ Done, 24 Sep | [specs/spec-rules-ai.md](../specs/spec-rules-ai.md) |
| A worked example | ✅ Done, 24 Sep | [specs/spec-001.md](../specs/spec-001.md) |
| Component names on iOS | ✅ Done, 24 Sep | [components/components-ios-map.md](../components/components-ios-map.md) |
| Token names on iOS | ✅ Done, 24 Sep | [tokens/tokens-ios-map.md](../tokens/tokens-ios-map.md) |
| `/prototype` | ✅ Exists, owned by Aviv | `~/.claude/skills/ios-prototyping/`, outside this repo |
| The design skill | ❌ Next task | — |
| The PRD format | ❌ Not started | — |
| The PM skill | ❌ Not started | — |

The order of work lives in [backlog.md](backlog.md), under *The iOS demo*.

---

## What each file is for

### The spec — `specs/`

| File | What it is | Who uses it |
| --- | --- | --- |
| [spec-rules-ai.md](../specs/spec-rules-ai.md) | **The format.** What a spec contains, where each name comes from, how feedback is applied | The design skill follows it. A build agent reads specs written in it |
| [spec-001.md](../specs/spec-001.md) | `brief-001` written as a spec. The worked example | Anyone learning the format |
| `spec-NNN.md` | One spec per idea. A round of feedback edits the same file | Written by the design skill |

**What a spec holds**, in this order:

- **Source:** the brief or idea, never reworded.
- **Goals:** what the user must be able to do.
- **Acceptance criteria:** how to tell, by looking at the screen, that a goal is met.
- **Assumptions:** everything the source did not say. This is what makes a
  fast spec safe: nothing invented is hidden.
- **Screen:** blocks and elements, top to bottom. Each element has a stable
  ID, such as `finance.monthly-estimate`, so feedback can point at one row.
- **Inventions:** anything built outside the design system, declared.
- **Change log:** one row per round of feedback.

**A spec uses design-system names only.** No iOS name, no Figma name, no hex
colour. That is what lets Android reuse the same spec later.

### The iOS maps

| File | What it translates | How it was made |
| --- | --- | --- |
| [components-ios-map.md](../components/components-ios-map.md) | `Text Button` → `DSTextButton` | By hand, from the iOS code. 44 proved, 5 guessed |
| [tokens-ios-map.md](../tokens/tokens-ios-map.md) | `Content/Light/Default` → `designSystem.colors.content.light` | **By a script.** 248 of 283 proved, none guessed |

**Neither map decides anything.** The rulesets decide which component or
token to use. A map only translates a name already chosen.

---

## The script, and when to run it

`tokens/scripts/extract_ios_token_map.py` writes `tokens/tokens-ios-map.md`.

**Run it when the iOS team changes its design system.** From the repo root:

```
python3 tokens/scripts/extract_ios_token_map.py --ios-repo ~/gsl-ios
```

Add `--check` to see whether the map is out of date, without writing anything.
An iOS commit that changes no token does not count as out of date.

**How it proves a match**, in plain terms:

- **Colours:** the iOS code fills each colour from an asset named after the GSL
  token. `Content/Light/Default` is filled from `contentLightDefault`. A match
  on that name is the iOS team's own wiring, so it counts as proved.
- **Spacing, radius and shadow:** the values are equal on both sides.
- **Text styles:** the size and the weight both exist on iOS.

**It reads the iOS code from the remote branch, never your local copy.**
Your local copy was 21 commits behind on 24 September.

---

## What is not proved yet

- **No agent has written or built from a spec yet.** The design skill will be
  the first real test. **Not tested.**
- **No iOS engineer has confirmed either map.** Five component names are
  guesses, and they need a person on the iOS team.
- **35 tokens have no iOS name.** Examples: `Spacing/64`, `Radius/Rounded`,
  the border widths. A spec naming one cannot be built by name on iOS.
  Which side is right is an open question in the backlog.

---

## Where the decisions are recorded

Why it is shaped this way — no Figma, throwaway prototypes, two skills chained —
is in [decisions.md](decisions.md), under 24 September 2026.
