# How a run gets reported

_Written for a person, not for an agent. It **explains** how the reporting
works; it never **specifies** anything. Every rule it describes lives somewhere
else, and this page links to it rather than repeating it — two copies of a rule
drift, and then there are two answers._

_Written 11 September 2026._

---

## Start here: what a "run" is

**One run is one go at the machine.** You hand an agent a written brief — *build
the energy and conditions block of a listing page, on mobile* — and it produces
a screen. That is a run. If it drew three screens from that one brief, that is
still one run.

Every run gets **scored**, and the scoring produces a **report**: a short
document saying what the agent got right, what it got wrong, and what it did
that nobody has a rule about yet.

The one thing worth knowing before anything else: **the report is a saved file,
not something you look at once.** A run whose screen exists but whose report
does not is an unfinished run, not a good one. We learned that the expensive way
— see [what already went wrong](#what-already-went-wrong-once) at the bottom.

---

## The flow, end to end

Five steps. Two of them are done by a person, three by machines.

```
        YOU
         │  write the brief, save it as prompt.md
         ▼
  ┌─────────────┐
  │  1. BRIEF   │   prompt.md          saved BEFORE anything is generated
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │ 2. GENERATE │   the agent draws the screen in Figma
  └─────────────┘   you take screenshots of what it actually made
         │
         ▼
  ┌─────────────┐
  │ 3. TRANSLATE│   the "adapter" reads the Figma file and writes down
  │             │   what is there, in design-system words:
  └─────────────┘   "this is a Listing Card"  ·  "this colour is Surface/Brand"
         │                                          → facts.json
         ▼
  ┌─────────────┐
  │  4. SCORE   │   the checking agent compares those facts
  │             │   against the rules. It never looks at Figma.
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │  5. REPORT  │   report.md — the verdict, saved beside everything above
  └─────────────┘
         │
         ├──────►  one line appended to the run ledger   (so runs can be compared)
         └──────►  every oddity appended to the flag ledger (so repeats show up)
```

### Why step three exists at all

It is the step people skip when they explain this, and it is the one that makes
the whole thing portable.

The scoring machinery **never touches Figma**. In between sits a translator —
we call it the *adapter* — whose only job is to read the output on its own
platform and restate everything in design-system vocabulary. It makes no
judgements. It says *"there is a component here and its name is Button"*; it
never says *"and that was the wrong one"*.

That separation is what lets one set of rules judge a Figma screen today and a
web page or an iOS app later. A new platform needs a new translator, never new
rules.

```
   Figma          ─┐
   Web            ─┤──►  a translator  ──►  the same facts  ──►  the same rules
   iOS            ─┤      per platform         in the same          for everyone
   Android        ─┘                           words
```

The full list of what a translator must report is
[Required facts](../compliance/compliance-scorecard.md#required-facts) in the
scorecard.

---

## The four files a run leaves behind

A finished run is a folder with four things in it. All four are required — a
folder missing one is a run that cannot be trusted later.

| The file | Who writes it | When | Why it has to exist |
| --- | --- | --- | --- |
| `prompt.md` — the brief | **You** | **Before** generating | So the brief can never be quietly reworded afterwards to match whatever came out |
| `*.png` — the screenshots | Whoever ran it | Right after generating | The only human-readable proof. A Figma file keeps changing under you; a screenshot doesn't |
| `facts.json` — what was found | The translator | During scoring | Kept, not thrown away, so a *future* rule can be tested against an *old* run |
| `report.md` — the verdict | The checking agent | Last | The answer. Readable on its own, sendable to anyone |

The exact shape of the report — which headings, in which order — is
[The template](../compliance/compliance-scorecard.md#the-template). It is not
repeated here on purpose.

### The one that surprises people: keeping `facts.json`

It looks like scratch paper. It isn't.

Because it's kept, you can change a rule in six months and ask the old runs a
question you couldn't ask at the time: **"would this new rule have caught that
old mistake?"** — without regenerating a single screen. Throw it away and every
rule change orphans every run that came before it.

---

## Where it all lands

After a few runs, the folder reads like a diary:

```
compliance/
│
├── compliance-scorecard.md      THE RULER — the rules, thresholds, template
├── compliance-run-ledger.md     THE TABLE — one line per run, compare here
├── compliance-flag-ledger.md    THE ODDITIES — things no rule covers yet
│
└── runs/
    ├── run-001/                 ← the one we already have
    │   ├── prompt.md
    │   ├── block-1-energy-and-conditions.png
    │   └── block-2-finance.png          (no facts, no report — see below)
    │
    ├── run-002/
    │   ├── prompt.md
    │   ├── screen.png
    │   ├── facts.json
    │   └── report.md            ← a complete run looks like this
    │
    └── run-003/
        ├── prompt.md
        ├── screen.png
        ├── facts.json
        └── report.md
```

Run numbers are **never reused, never reordered, never renumbered** after the
fact. `run-007` means the same run forever, in every conversation and every
ledger row.

### Why the ruler and the record are separate files

This is the shape most worth understanding, because it repeats all over this
repo.

| The scorecard | The ledgers |
| --- | --- |
| **The ruler.** What the rules are, what counts as passing | **The record.** What actually happened, on which date |
| Rewritten whenever a rule or a threshold changes | **Appended to, never rewritten** |

If both lived in one file, then editing a rule would mean opening a file that
also holds history — and sooner or later someone tidies a row from March while
changing a rule in September. The rules have to be free to change; the evidence
has to be frozen. One file cannot do both.

---

## Walkthrough one — you, three weeks from now

You've run the thing eight times. You want to know one thing: **is it getting
better?**

```
   You open ONE file:  compliance/compliance-run-ledger.md

   ┌──────────────────────────────────────────────────────────────┐
   │ Run  Date    Wireframe        Components  Build  Tokens  Qual│
   │ 002  12 Sep  listing-detail        2        1      3    close│
   │ 004  15 Sep  listing-detail        1        0      1     good│
   │ 007  19 Sep  listing-detail       ok       ok     ok     ship│
   └──────────────────────────────────────────────────────────────┘
                          ▲
                  read DOWN one wireframe
```

Each number is **how many questions that step answered `yes` to** — how many
things went wrong. `ok` means none did. That's the whole answer, and you never
opened a report.

Three things to hold on to while reading it:

- **Read down a single `Wireframe` label, never across the table.** Two runs are
  only comparable when that label matches. Comparing a search page against a
  form measures how hard the brief was, not how compliant the output was.
- **Nothing is a percentage, on purpose.** Every rule behind these questions says
  *never* — never write a raw colour, never use a deny-listed token. There is no
  such thing as 88% of never, and writing it that way made a broken rule look
  like a good score.
- **Open a report only when a row looks wrong.** The ledger tells you *that*
  something moved; the report in `runs/run-NNN/report.md` tells you *what*.

And one column no machine can fill: **Quality** is your sentence, in your words,
about whether the screen is actually any good. Compliance can tell you the agent
used permitted colours. It cannot tell you the screen is worth shipping. That
column is the only place that judgement is ever recorded — which is also why it
is the one most likely to be left blank.

---

## Walkthrough two — the checking agent, on its next run

Same pipeline, from the machine's side. The agent has just been handed a
freshly generated screen.

```
  1. Take the facts                 reads facts.json — never opens Figma
         │
  2. Ask the questions, step by step
         │
         │   the components step    Was anything hand-built?
         │                          Was anything never-select used?
         │                          Was a name used that's in no registry?
         │   what needs building    Was anything hand-built undeclared?
         │   choosing the tokens    Was any value written as a literal?
         │                          Was a component's own styling overridden?
         │                          Was a deny-listed token used?
         │                          Was a token used that isn't ours?
         │   placing them           (switched off for now)
         │   the three others       (no question yet — they say so)
         ▼
  3. Every answer is yes or no
         │
         ├── no    compliant. Nothing more recorded
         ├── yes   a finding. The report says what, and where
         └── FLAGS odd, but no rule covers it either way
         ▼
  4. Write report.md               one row per question, in step order
         │
  5. Append two rows               run ledger · flag ledger
```

Three habits in there are deliberate.

**Every question is phrased so that `no` is the good answer.** You read one
column and look for `yes`. That is the whole of reading a report — there is no
pass mark to remember and no arithmetic to do.

**Every row appears, including the empty ones.** A row reading `no` tells you the
question was asked and nothing was found. A missing row tells you nothing — you
can't tell whether there was nothing to find or whether nobody looked. Same for
the three steps that have no question at all, and for the quality verdict: the
heading stays, empty, because an empty heading nags and a missing one doesn't.

**Nothing has a code.** The questions used to be `C1` to `C6`, and keeping them
readable cost a standing rule to write the name beside the number everywhere.
They are grouped under the step of designing each one guards instead, and a step
already has a name.

---

## What already went wrong once

`run-001` is sitting in that folder right now with its brief and its
screenshots and **no verdict at all** — no `facts.json`, no `report.md`.

Nothing failed. The rules simply described a report as something you *look at*,
and never as something that is *saved*. So a real run happened, was looked at,
and the judgement evaporated with the conversation it happened in. Whether the
original Figma file still exists, nobody has checked — scoring `run-001`
properly is still on the backlog, waiting on someone with Figma open.

That single missing file is the reason the whole arrangement on this page
exists.

---

## What doesn't exist yet

Worth being straight about, so the page doesn't read as more finished than it
is.

| Thing | State today |
| --- | --- |
| The **translator** (step three) | **Not built.** Until it is, `facts.json` is written by hand — and a hand-written facts file is exactly the sort of thing that quietly stops matching what the rules expect |
| The **generating skill** | Gabriel's to build. It will produce both the screen and the report. It deliberately came second: a skill can't be built against a format that isn't settled |
| The **two ledgers agreeing** | Nothing checks that a report's scores match its ledger row. Two files, kept in step by hand |
| The **layout check** | Switched off. The layout rules have never been tested against a real screen |

---

## Where to read further

| For | Go to |
| --- | --- |
| The rules themselves — thresholds, the report template, what a translator must report | [compliance/compliance-scorecard.md](../compliance/compliance-scorecard.md) |
| The comparison table across runs | [compliance/compliance-run-ledger.md](../compliance/compliance-run-ledger.md) |
| Oddities seen across runs, so a repeat can be spotted | [compliance/compliance-flag-ledger.md](../compliance/compliance-flag-ledger.md) |
| **Why** it was built this way, and what it cost | [project/decisions.md](decisions.md) — the entry dated 11 September 2026 |
