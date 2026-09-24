# How a prototype is made

_Written for a person, not for an agent. It **explains** the workflow. It never
**specifies** anything: every rule lives in the file this page links to. Two
copies of a rule drift, and then there are two answers._

_Rewritten 24 September 2026, once the design skill existed. Update it whenever
a task changes the workflow._

---

## What this is for

**A product manager or a designer tries an idea on the real app, fast.** They
describe it in their own words. They get a screen built with the design system,
running on the simulator.

The prototype is **throwaway**. **What lasts is the spec**: the written
description of the screen.

---

## The workflow

```
   YOU                                 THE DESIGN SKILL                 /prototype
   ───                                 ────────────────                 ──────────

 1. IDEA ──── /design <your idea> ───► saves your words, word for word
                                              │
 2. QUESTIONS ◄──── up to 9, one at a time ───┤
                                              │
 3. VALIDATE ◄──── goals + criteria ──────────┤
    "yes" ───────────────────────────────────►│
                                              │
 4.                                    DESIGN, automatic
                                       components + tokens from the rules
                                              │
 5.                                           └──── the spec ────────►  BUILD
                                                                        on the simulator
 6. FEEDBACK ◄───────────────────────── you look at the screen ◄────────────┘
    "make the title bigger" ─────────► edits the spec ──── rebuild ───►
```

**Everything happens in one chat**, opened in the `gsl-ios` folder.

---

## Each step: what happens, and why

### 1 · Idea

| What | Who |
| --- | --- |
| `/design`, then the idea in your own words. Example: `/design Let buyers compare two listings side by side` | You |
| Your words are saved as they are, before anything else | The skill |

**Why saved first:** the spec is judged against what you asked. Words written
down afterwards drift towards the answer.

### 2 · Questions

| What | Who |
| --- | --- |
| Who uses it, what problem, what they can do after, what data, where it lives, what it shows, how you'd know it works, which brand, which platform | The skill asks, you answer |

- **Only what your idea didn't already say.** At most nine, one per message.
- **"I don't know" is a fine answer.** It becomes an open assumption.
- **The platform is often skipped:** in the `gsl-ios` folder, the skill knows it is iOS.
- **Never "which component?"** Most people have no view. The rules decide.

**Why:** this step defines the problem, not the interface.

### 3 · Validate

| What | Who |
| --- | --- |
| The goals, and how to tell each is met, in plain words | The skill shows |
| "Is this what the screen must do?" — yes, or what to change | You |

**Why:** no screen is designed before the *what* is agreed. The criteria check
the screen does what you asked. Whether it is *good* stays your judgement.

### 4 · Design

| What | Who |
| --- | --- |
| Components, variants, colours, text styles, spacing, icons — chosen from the design system's rules, then written as the spec | The skill, automatically |

- **Reuse before invention.** Anything built outside the design system is declared.
- **Only what iOS can build.** Components iOS lacks are avoided.
- **Every guess is written down** as an assumption. Nothing invented is hidden.

**Why automatic:** the rules already answer these questions. Asking you would
only slow you down.

### 5 · Build

| What | Who |
| --- | --- |
| The spec is handed to `/prototype`, which builds it in SwiftUI on a throwaway branch | `/prototype`, in the same chat |

**Outside the iOS repo**, the skill stops at the spec. Android, web and Figma
have no build yet.

### 6 · Feedback

Say what to change, in the same chat. **The spec is edited, then the screen is
rebuilt from it — never the code directly.** A change made only in the code is
lost at the next rebuild.

| You say | What happens |
| --- | --- |
| "Make the title bigger" | Changed and rebuilt. No question |
| "Add a share button" | Changed and rebuilt, with one line saying what was added |
| "Also let them book a visit" | One question: add it to this screen's goals, or start a new idea? |

"Bigger" means the next size the design system allows, never a made-up size.

---

## Where things live

```
 THIS REPO (gsl-ds-documentation-ai)            the design system, written down
   │
   │  scripts/build-design-references.py         copies the rules into the skill
   ▼
 skills/design/                                  the design skill
   ├── SKILL.md                                  how it works — rarely changes
   └── references/                               the rules — regenerated, never edited
          │
          │  linked into ~/.claude/skills/, so it runs from any folder
          ▼
 gsl-ios  ── /design + /prototype, in one chat ──►  simulator
          │
          ▼
 ~/gsl-specs/spec-NNN.md                         every spec, outside every repo
```

**Why specs live outside every repo:** `/prototype` deletes its branch at
cleanup. A spec saved there would go with it. One folder also lets the same
spec be built on Android later.

### What each file is for

| File | What it is |
| --- | --- |
| [skills/design/SKILL.md](../skills/design/SKILL.md) | The design skill |
| [specs/spec-rules-ai.md](../specs/spec-rules-ai.md) | **The spec format**: what a spec holds, where every name comes from |
| [specs/spec-001.md](../specs/spec-001.md) | A worked example |
| [components/components-ios-map.md](../components/components-ios-map.md) | Component names on iOS. `Text Button` → `DSTextButton`. By hand: 44 proved, 5 guessed |
| [tokens/tokens-ios-map.md](../tokens/tokens-ios-map.md) | Token names on iOS. By a script: 248 of 283 proved, none guessed |

**The maps never decide.** The rules choose a component or a token. A map only
translates the name for iOS, and tells the skill what iOS lacks.

---

## Keeping it up to date

| When | Run, from this repo's root |
| --- | --- |
| **Any rule changes** — a ruleset, a colour family page, a component's variants | `python3 scripts/build-design-references.py` |
| **The iOS team changes its design system** | `python3 tokens/scripts/extract_ios_token_map.py --ios-repo ~/gsl-ios` |

Add `--check` to the second one to see whether the token map is out of date,
without writing anything. It reads the iOS code from the remote branch, never
your local copy.

---

## What is not proved yet

- **The design skill has never run.** The first real run is the next task.
- **`/prototype` has not been taught to read a spec.** It is pointed at the file
  in plain words. **Guessing** it follows it well.
- **No iOS engineer has confirmed either map.** Five component names are guesses.
- **35 tokens have no iOS name**, such as `Spacing/64` and the border widths.
- **No rule covers copy.** Every text the skill writes is an assumption.

---

## Where the decisions are recorded

Why it is shaped this way is in [decisions.md](decisions.md), under 24 September
2026 — two entries: the spec as the contract, then the design skill's workflow.
