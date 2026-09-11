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
   │ Run  Date    Wireframe          C3·Token  Hard fails  Quality│
   │ 002  12 Sep  listing-detail      88%          2       "close"│
   │ 004  15 Sep  listing-detail      94%          1       "good" │
   │ 007  19 Sep  listing-detail     100%          0       "ship" │
   └──────────────────────────────────────────────────────────────┘
                          ▲
                  read DOWN one wireframe
```

That's the whole answer, and you never opened a report.

Three things to hold on to while reading it:

- **Read down a single `Wireframe` label, never across the table.** Two runs are
  only comparable when that label matches. Comparing a search page against a
  form measures how hard the brief was, not how compliant the output was.
- **The hard-fails count outranks every percentage on its row.** A row reading
  *94% · 1 hard fail* is a worse run than one reading *88% · 0*. A hard fail
  means something forbidden made it onto the screen.
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
  2. Ask the six questions          Did it use real components?
         │                          Did it stay inside the tier it's allowed?
         │                          Is every colour and spacing a real token?
         │                          Did it use anything on a never-use list?
         │                          Did it declare whatever it invented?
         │                          (Layout — switched off for now)
         ▼
  3. Sort what it found into three piles
         │
         ├── HARD FAILS   something forbidden shipped
         ├── SCORES       a percentage per question
         └── FLAGS        odd, but no rule covers it either way
         ▼
  4. Write report.md               hard fails FIRST, above any percentage
         │
  5. Append two rows               run ledger · flag ledger
```

Three habits in there are deliberate. Two of them are about a human misreading
a report:

**Hard fails print above the scores, always.** A report opening with *"94%,
88%"* reads as broadly fine even when the screen contains something explicitly
forbidden. Percentages never get to appear before the gates they'd disguise.

**Every heading appears, including the empty ones.** A report saying
*Hard fails (0)* tells you nobody found any. A report with no such heading tells
you nothing — you can't tell whether there were none or whether nobody looked.
Same for the quality verdict: the heading stays, empty, because an empty heading
nags and a missing one doesn't.

And the third: **a check always gets called by its name, never its number** —
`C4 · Authorisation`, not `C4`. Six two-character codes are not memorable, and a
report written in them can only be read by whoever wrote it.

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
