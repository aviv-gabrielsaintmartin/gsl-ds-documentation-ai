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

Four steps. Two are done by you, two by agents.

```
        YOU
         │  write the brief, save it as prompt-run-001.md
         ▼
  ┌─────────────┐
  │  1. BRIEF   │   prompt-run-001.md   saved BEFORE anything is generated
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │ 2. GENERATE │   the building agent draws the screen in Figma
  └─────────────┘   you take screenshots of what it actually made
                    it writes down anything it built by hand
                                            → report-run-001.md, part one
         │
         ▼
  ┌─────────────┐
  │  3. SCORE   │   a SECOND agent opens the Figma file and looks.
  │             │   It has never seen the building conversation.
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │  4. REPORT  │   report-run-001.md — what it found, then the
  │             │   verdict, below what the builder already wrote
  └─────────────┘
         │
         ├──────►  one line appended to the run ledger   (so runs can be compared)
         └──────►  every oddity appended to the flag ledger (so repeats show up)
```

### Why the scoring agent has to be a different agent

This is the step that makes the verdict worth anything.

The scorecard is a file. Any agent can read it, which means the agent that built
the screen knows every question before it is asked.

Ask it to report on its own work and it will report truthfully and selectively.
It never has to state a falsehood to produce a flattering picture. It only has
to choose what to mention.

So the scoring agent is started fresh. It never sees the building conversation,
and it never asks the builder anything. It opens the Figma file and looks.

```
   the builder                the scorer
   knows the questions        knows the questions
   knows what it did          knows only what it can see
        │                          │
        └──► writes ONE section ───┴──► writes everything else
             what it built by hand      what it found, and the verdict
```

### What this deliberately does not do

An earlier design put a translator between the two — it would read the Figma
file and write out everything it found as data, so the scoring rules never
touched Figma at all. That made the rules portable to web and iOS for free, and
it left a stored record that a future rule could be re-tested against.

It was removed on 14 September 2026 as too advanced for the end-of-September
deadline. Two consequences worth knowing:

- **The scoring agent is Figma-only.** A second platform needs a second scoring
  agent. The questions themselves are still written in design-system words, so
  they carry over unchanged.
- **Nothing is stored but the report.** You cannot change a question in six
  months and ask an old run whether it would have been caught. The screenshots
  and the written findings are the record.

---

## The three files a run leaves behind

A finished run is a folder with three things in it. All three are required — a
folder missing one is a run that cannot be trusted later.

| The file | Who writes it | When | Why it has to exist |
| --- | --- | --- | --- |
| `prompt-run-001.md` — the brief | **You** | **Before** generating | So the brief can never be quietly reworded afterwards to match whatever came out |
| `*.png` — the screenshots | Whoever ran it | Right after generating | The only human-readable proof. A Figma file keeps changing under you; a screenshot doesn't |
| `report-run-001.md` — the verdict | **Two writers** — see below | Twice | The answer. Readable on its own, sendable to anyone |

**Every file carries its run number, and the folder says it too.** That looks
like saying it twice, and it is deliberate: the moment a file is opened in a tab
or attached to a message, the folder is gone and the name is all you have. The
screenshots are the exception — `block-1-energy-and-conditions.png` tells you
what you are looking at, which matters more than which run drew it.

The exact shape of the report — which headings, in which order — is
[The template](../compliance/compliance-scorecard.md#the-template). It is not
repeated here on purpose.

### The report is written by two different agents

Most of the report is the verdict, written last by the checking agent. But the
report **opens** with a section the checking agent never touches.

When an agent cannot find a component that fits, it is allowed to build the
thing by hand — and it then has to say so. It writes what it built, which
problem it was solving, and which existing components it looked at and rejected.
That is a **declaration**, and it is what separates a considered decision from
an agent that simply didn't look.

The declaration goes at the top of the run's report, written by the generating
agent **before anything is scored**. Then the checking agent opens the same file
and writes the verdict underneath.

The order is the point. A brief is saved before generating so nobody can reword
it to match the output; a declaration is written before scoring for the same
reason — so it can't be quietly improved once the agent sees it failed. A
declaration added after the verdict isn't one.

There is nowhere else it could go. A note on the Figma frame is thrown away with
the file, and a sentence in the agent's reply disappears when the conversation
does.

### The report is the only record

Nothing else survives a run except the screenshots. The scoring agent writes
down what it found, above its verdict, and that written account is the evidence.

The cost is stated plainly in [what this deliberately does not
do](#what-this-deliberately-does-not-do): change a question in six months and
you cannot ask an old run whether it would have been caught. You run a new
screen instead.

---

## Where it all lands

After a few runs, the folder reads like a diary:

```
compliance/
│
├── compliance-scorecard.md      THE RULER — the questions and the template
├── compliance-run-ledger.md     THE TABLE — one line per run, compare here
├── compliance-flag-ledger.md    THE ODDITIES — things no rule covers yet
│
└── runs/
    ├── run-001/                 ← the one we already have
    │   ├── prompt-run-001.md
    │   ├── block-1-energy-and-conditions.png
    │   └── block-2-finance.png    (no report — see below)
    │
    ├── run-002/
    │   ├── prompt-run-002.md
    │   ├── screen.png
    │   └── report-run-002.md      ← a complete run looks like this
    │
    └── run-003/
        ├── prompt-run-003.md
        ├── screen.png
        └── report-run-003.md
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
  something moved; `runs/run-NNN/report-run-NNN.md` tells you *what*.

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
  1. Open the screen                the Figma file, and the builder's
         │                          declarations. Nothing else.
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
  4. Write the report              one row per question, in step order,
         │                          underneath the declarations already there
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
screenshots and **no verdict at all** — no report.

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
| The **generating skill** | Gabriel's to build. It will produce both the screen and the report. It deliberately came second: a skill can't be built against a format that isn't settled |
| The **two ledgers agreeing** | Nothing checks that a report's scores match its ledger row. Two files, kept in step by hand |
| The **layout check** | Switched off. The layout rules have never been tested against a real screen |

---

## Where to read further

| For | Go to |
| --- | --- |
| The rules themselves — the questions, the report template, what a scoring agent must be able to see | [compliance/compliance-scorecard.md](../compliance/compliance-scorecard.md) |
| The comparison table across runs | [compliance/compliance-run-ledger.md](../compliance/compliance-run-ledger.md) |
| Oddities seen across runs, so a repeat can be spotted | [compliance/compliance-flag-ledger.md](../compliance/compliance-flag-ledger.md) |
| **Why** it was built this way, and what it cost | [project/decisions.md](decisions.md) — the entry dated 11 September 2026 |
