# The input agent — your idea, and what it is worth

_A record of one conversation, 16 September 2026. **It decides nothing.** The
tasks it produced live in [backlog.md](backlog.md); the scope question it raised
is still open. Written so you can pick this up months from now without the chat._

---

## Reopening the conversation

| | |
| --- | --- |
| **Session id** | `0b3fd8fc-ca61-4964-ba01-e24f30ca8021` |
| **How to reopen it** | `claude --resume 0b3fd8fc-ca61-4964-ba01-e24f30ca8021` |
| **Date** | 16 September 2026 |

**Proved:** the id is this session's own, read from its scratchpad path.
**Not tested:** whether the transcript will still resume months later. Claude
Code keeps transcripts on this machine, so it depends on that machine and on how
long they are kept. This page is the durable copy; the chat is not.

---

## What you asked

You had just tested a generation in Figma, using Figma's own internal design
agent. It has its own habits, different from the agents used here.

Your point, in your words:

> If we have a canonical documentation, then batched and reformated in different
> format for different tools, juding the color and components usage is hard
> because it's hard to differentiate bad documentation from bad execution or bad
> prompting or bad tooling.

And your proposal:

> We should have an "input agent" that will ask some questions to the user, then
> based on that will define the specifications, then the associated prompt next
> executed by the design or prototyping or coding agent on the designated
> platform.

You expected three things from it: consistent prompting, easier comparison
between runs, and updates in almost one place — the canonical documentation.

---

## The workflow, drawn

```
   user need
       │
       ▼
   interview  ──►  spec (platform-neutral)  ──►  you confirm
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Figma prompt    web prompt     iOS prompt
          │              │              │
          ▼              ▼              ▼
      build agent    build agent    build agent
                         │
                         ▼
                   score  ──►  ledger verdict
```

---

## Where things stand

| | Today | With an input agent |
| --- | --- | --- |
| The prompt | Written fresh per run, per platform | Generated from one spec |
| Causes of a bad score | Doc, execution, prompting, tooling — four | Doc, execution, tooling — three |
| Platform difference | Handled inside each run, by hand | Handled once, in the emitter |
| What a run records | Brief, output, score | Spec, prompt, output, score |

---

## Why the idea is sound

- **The confound is real.** A bad screen has four possible causes and you can
  only act on one of them at a time.
- **Freezing the prompt removes one cause.** That is the whole of the value, and
  it is worth having.
- **You already do this one level up.** `generate-and-score` saves the brief
  before anything is built. **Proved** — it is the skill's first step. The spec
  is the same move, earlier and platform-aware.
- **It fills your emptiest step.** `status.md` and
  [design-process-map.md](design-process-map.md) both say *Define the content —
  from the user need* has nothing answering it. The interview is that step.

---

## What the idea claims, and does not deliver

- **Platform adjustment does not disappear.** It moves into the emitter. One
  file instead of many is a genuine win. It is centralising, not removing, and
  the difference matters when you measure.
- **Tooling stays uncontrolled.** Figma's internal agent and `figma-cli` have
  different reach. Identical words still produce different failures. Each
  platform needs a stated note on what its agent can and cannot do.

---

## What is risky

- **The input agent becomes an unlogged variable of its own.** Change its
  questions and every run before that change stops being comparable. The spec
  and the generated prompt have to be saved into the run folder, the way the
  brief already is.
- **Human answers add variance.** Two people answer the same need differently.
  A measured run wants a fixed spec and no interview at all.
- **It is a fourth artefact to keep true**, and five of twelve token kinds still
  have no ruleset.
- **On its own it does not fix the pain it was proposed for.** What separates a
  documentation failure from an execution failure is the ledger verdict. It has
  four values — `agent error`, `ruleset gap`, `library defect`, `accepted`.
  Neither prompting nor tooling is one of them. **Proved**, read from
  `compliance/compliance-flag-ledger.md` on 16 Sep.

---

## What was recommended, in order

1. **Add two verdicts to the flag ledger** — one for the prompt or spec, one for
   a tooling limit. It measures the confusion before anything is built against
   it.
2. **Fix a spec format.** `compliance/briefs/brief-001/brief-001.md` is already
   most of the shape: objective, content, constraints.
3. **One prompt template per platform**, wrapping the spec unchanged, plus that
   platform's capability note.
4. **Build the interview after September.** It adds a front door, never
   accuracy.

---

## What you decided

- **September is about documentation, not about a platform.** Document as much
  as possible, flag every missing piece of content and every documentation
  defect, and keep it platform-agnostic. The process and the mapping are part of
  it.
- **Figma's internal design agent is the next target** for a prompt template.
- **Tools change, so documentation comes first.** That is the reason the
  agnostic layer is the priority and not the per-platform wrapper.

---

## What is still open

**One question, and it is in [backlog.md](backlog.md) under *About what
September means*.**

[the-project.md](the-project.md) defines September as two unseen briefs, built
and scored, with no rule broken. What you described on 16 September is wider and
has no stated end state. The two rank the work differently, so the answer
changes what gets done first. That page was deliberately left unchanged.

---

## Where the work went

| Backlog section | Row |
| --- | --- |
| *Define the content* | Build the input agent — not due by September |
| *Scoring a finished screen* | Add two verdicts to the flag ledger |
| *Scoring a finished screen* | Fix a spec format, and build only from it |
| *Scoring a finished screen* | One prompt template per platform |
| *Questions* | About what September means |
| *Notes*, 16 Sep | The assessment in short |
