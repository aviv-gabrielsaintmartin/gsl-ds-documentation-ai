# The design process today

**This is the design process as the designers mapped it, plus one thing added:
where AI would earn its place.**.

- _Built from the Guild Design AI workshop board and the `Brief stratégique —
Stratégie IA pour le Product Design`. 
- Written for a person. It describes how the
work happens today; it is never the source of truth for how anything is built.
Updated 15 September 2026._

**This is the long version.** The short page is
[the-project.md](the-project.md).

**In one line:** 

 Adesigner takes five steps Discovery → Definition → Solutioning → Validation → Follow-up. 

Each step has an objective, each objective raises questions, and this page holds all 36 of them. **Six have nothing answering them today. Eleven would change their step if AI answered them.**

---

## How this fits the France Product Playbook

**The playbook says which meeting, which tool, and who does what per phase. This
page says which questions a designer has to answer between those meetings.** Two
levels, one source each — the playbook is never restated here.

| Playbook phase | This page |
| --- | --- |
| 0. New idea | — |
| 1. Discovery | Discovery |
| 2. Definition | Definition · Solutioning · Validation |
| 3. Delivery | — |
| 4. Verification | Follow-up |

Three things that table says:

- **Discovery means the same thing in both.**
- **Definition is the nested one.** The playbook's single Definition phase holds
  three of this page's steps and 23 of its questions.
- **The playbook's Delivery phase has no step here at all.** That is where the
  seven gaps at the bottom of this page live — handoff, accessibility,
  design-to-code, visual QA.

---

## How to read this page

Every step has an objective. From the objective come the questions a designer
must answer before the step is finished.

Each sub-step gives you a table of its questions, then the detail folded away
underneath. **Scan the table. Open a question only when a row looks
interesting.**

### What the table holds

| Column | What it holds |
| --- | --- |
| **Question** | What the designer has to answer before the step is finished |
| **Answered today** | What answers it now, in one or two words. **Nothing** is a real answer and appears six times |
| **AI benefit** | *Not needed* · *Would help* · *Would change the step* |
| **Owner** | *Design* · *Product* · *Engineering* · *Research* · *Design + Product* · *Nobody* |

### What the folded detail holds

| Line | What it holds |
| --- | --- |
| **Answered today by** | The same answer, in full — the tool, document or person |
| **Designers said** | What was written on the board, translated from French. Absent means nobody raised a pain here — not that there isn't one |
| **Fixing it buys** | The board's own words: time, effectiveness, readability, understanding the data, project tracking |
| **What it would take** | *A prompt* · *A skill* · *A tool* · *A project*. Absent when AI is not needed |
| **Why** | Only on rows where AI is not needed, saying why |

**Each value appears in one place only.** AI benefit and owner live in the
table; everything else lives in the fold. Nothing to keep in sync.

A question ending in **(inferred)** came from the step's objective, not from a
card on the board. It is mine, and you should challenge those first.

### What each word means, and what it does not

| Term | What it is | What it is not |
| --- | --- | --- |
| **This page** | A description of how the work happens today | Not a process anyone has to follow, and never instructions |
| **A skill** | A written procedure an agent follows — reusable, no code | Not software, and not somebody's job |
| **Would change the step** | The designers named this as blocking or slow | Not a promise that AI can fix it |
| **Owner** | Who does it | Not who is accountable for it, and not who pays for it |
| **What it would take** | My guess at the cheapest thing that would answer the question | Not an estimate, and not a commitment |

### How AI benefit is decided

Not a judgment call. The rule, applied the same way every time:

- **Not needed** — no pain point on the board, or the answer is pure judgment
  that a person has to make.
- **Would help** — a pain point exists and the task is mechanical.
- **Would change the step** — the designers named it as blocking or slow.

### Two things to know about "What it would take"

- **Every value is a guess.** Nothing on the board says what building any of
  this would cost. It is ordered by difficulty: a prompt is minutes, a skill is
  hours, a tool is days, a project needs scoping before anyone can size it.
- **It says nothing about upkeep.** A tool keeps costing after it ships. A
  prompt does not.

### Three complaints repeat across the map

Named once here, so the same problem appearing in several cards doesn't read as
several problems.

| Heard                                           | Where                                                   | Times |
| ----------------------------------------------- | ------------------------------------------------------- | ----- |
| *"Which kind of workshop should I run?"*        | Product opportunities · UX hypothesis · First ideations | 3     |
| *"Which template should I use?"*                | Context · Journey map · User guide · Analyze            | 4     |
| *"Hard to access / find / understand the data"* | Identify the pain points                                | 3     |

---

## Discovery

**Objective — understand who we are building for, what the business wants, and
what hurts users today.**

### Context

**Objective — write down who the users are, what the goals are and how success
is measured, in one place everyone can find.**

| Question                                                                           | Answered today | AI benefit | Owner            |
| ---------------------------------------------------------------------------------- | -------------- | ---------- | ---------------- |
| Which space do I create this page in?                                              | Confluence     | Would help | Design + Product |
| Who is responsible for this page once it exists?                                   | **Nothing**    | Not needed | **Nobody**       |
| Which template do I use?                                                           | Confluence     | Would help | Design + Product |
| Who are the users, the goals, the OKRs, the metrics and the timeline? *(inferred)* | The PM         | Not needed | Product          |
| How do I know these goals line up with the business objectives?                    | **Nothing**    | Not needed | Product          |

<details>
<summary><strong>Which space do I create this page in?</strong></summary>

- **Answered today by** — Confluence
- **Designers said** — *"Which space do I create this page in?"*
- **Fixing it buys** — time
- **What it would take** — a skill

</details>

<details>
<summary><strong>Who is responsible for this page once it exists?</strong></summary>

- **Answered today by** — nothing
- **Designers said** — *"Who is responsible for this page?"*
- **Fixing it buys** — project tracking
- **Why** — It is an organisation question, not a generation one

</details>

<details>
<summary><strong>Which template do I use?</strong></summary>

- **Answered today by** — Confluence templates
- **Designers said** — *"Which template should I use?"*
- **Fixing it buys** — time, effectiveness
- **What it would take** — a skill

</details>

<details>
<summary><strong>Who are the users, the goals, the OKRs, the metrics and the timeline? <em>(inferred)</em></strong></summary>

- **Answered today by** — the PM, then written into Confluence
- **Fixing it buys** — effectiveness

</details>

<details>
<summary><strong>How do I know these goals line up with the business objectives?</strong></summary>

- **Answered today by** — nothing
- **Designers said** — *"Being aligned with the business objectives"*
- **Fixing it buys** — effectiveness
- **Why** — It is a conversation, not a task

</details>

**The board's own answer for this sub-step:** *"Suggest the template and the
rules to follow."*

### Identify the pain points, understand our users

**Objective — know what users actually do and what hurts them, using data we
already hold.**

| Question                                   | Answered today      | AI benefit                | Owner    |
| ------------------------------------------ | ------------------- | ------------------------- | -------- |
| What already exists on this surface?       | The live site       | Would help                | Design   |
| What does the quantitative data say?       | Four separate tools | **Would change the step** | Design   |
| What does the qualitative data say?        | Four separate tools | **Would change the step** | Design   |
| What does the customer journey look like?  | Miro                | Would help                | Design   |
| Where is the research that already exists? | Confluence          | **Would change the step** | Research |

<details>
<summary><strong>What already exists on this surface?</strong></summary>

- **Answered today by** — Preview, the live site
- **Fixing it buys** — time
- **What it would take** — a prompt

</details>

<details>
<summary><strong>What does the quantitative data say?</strong></summary>

- **Answered today by** — Google Analytics · Contentsquare · Confluence · Dovetail
- **Designers said** — *"Hard to get access to the tools"* · *"Hard to find the data"* · *"Hard to understand the data"*
- **Fixing it buys** — time, effectiveness, understanding the data
- **What it would take** — a tool

</details>

<details>
<summary><strong>What does the qualitative data say?</strong></summary>

- **Answered today by** — Contentsquare · Confluence · Dovetail · Modjo
- **Designers said** — the same three complaints
- **Fixing it buys** — time, effectiveness, understanding the data
- **What it would take** — a tool

</details>

<details>
<summary><strong>What does the customer journey look like?</strong></summary>

- **Answered today by** — Miro
- **Fixing it buys** — effectiveness
- **What it would take** — a skill

</details>

<details>
<summary><strong>Where is the research that already exists?</strong></summary>

- **Answered today by** — Confluence
- **Designers said** — *"It moved to Confluence … where is it?"*
- **Fixing it buys** — time
- **What it would take** — a tool

</details>

**The board's own answer for this sub-step is the most detailed on the whole
map:** *"Go and find the data itself, by questioning all our sources. List every
document and source. Summarise what it gathered. Link that research to my
problem."*

---

## Definition

**Objective — turn what we learned into a stated hypothesis, a mapped journey,
and a view of what others do.**

### Product opportunities

**Objective — agree with PM and EM which opportunities are worth taking, and in
what order.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Which kind of workshop should I run? | **Nothing** | **Would change the step** | Design |
| Which opportunities do we take, and in what order? *(inferred)* | A workshop | Not needed | Product |

<details>
<summary><strong>Which kind of workshop should I run?</strong></summary>

- **Answered today by** — nothing
- **Designers said** — *"Which kind of workshop should I run?"*
- **Fixing it buys** — time
- **What it would take** — a skill

</details>

<details>
<summary><strong>Which opportunities do we take, and in what order? <em>(inferred)</em></strong></summary>

- **Answered today by** — a workshop with PM and EM, written up in Confluence
- **Fixing it buys** — time

</details>

**The board's own answer, which appears three times across the map:** *"A tool
that gives me workshop ideas suited to my subject and my objectives."*

### UX hypothesis

**Objective — state what we believe will change for the user, so it can be
tested later.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Which kind of workshop should I run? | A workshop | **Would change the step** | Design |
| What exactly is the hypothesis, in one testable sentence? *(inferred)* | Confluence | Would help | Design + Product |

<details>
<summary><strong>Which kind of workshop should I run?</strong></summary>

- **Answered today by** — a workshop with PM and EM
- **Designers said** — *"Which kind of workshop should I run?"*
- **Fixing it buys** — effectiveness
- **What it would take** — a skill

</details>

<details>
<summary><strong>What exactly is the hypothesis, in one testable sentence? <em>(inferred)</em></strong></summary>

- **Answered today by** — Confluence
- **Fixing it buys** — effectiveness
- **What it would take** — a prompt

</details>

### Journey map

**Objective — show the user's path end to end, so the gaps are visible.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Which template do I use? | Confluence | Would help | Design |
| How do I build it without missing a step? *(inferred)* | Confluence | Would help | Design |

<details>
<summary><strong>Which template do I use?</strong></summary>

- **Answered today by** — Confluence
- **Designers said** — *"Which template should I use?"*
- **Fixing it buys** — readability
- **What it would take** — a skill

</details>

<details>
<summary><strong>How do I build it without missing a step? <em>(inferred)</em></strong></summary>

- **Answered today by** — Confluence
- **Fixing it buys** — readability
- **What it would take** — a skill

</details>

**The board's own answer:** *"A tool to help me create it while respecting a
template."*

### Benchmark

**Objective — know what competitors do, direct and indirect.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Which competitors should I look at, direct and indirect? | **Nothing** | **Would change the step** | Design |
| How do I see their current interfaces? | Mobbin | Would help | Design |
| What do I keep from what I saw? *(inferred)* | The designer | Not needed | Design |

<details>
<summary><strong>Which competitors should I look at, direct and indirect?</strong></summary>

- **Answered today by** — nothing
- **Designers said** — *"Which ones do I look at?"* · *"It takes a lot of time"*
- **Fixing it buys** — time, effectiveness
- **What it would take** — a skill

</details>

<details>
<summary><strong>How do I see their current interfaces?</strong></summary>

- **Answered today by** — the sites and apps themselves · Mobbin
- **Designers said** — *"I don't have the access or the subscriptions"*
- **Fixing it buys** — time
- **What it would take** — a tool

</details>

<details>
<summary><strong>What do I keep from what I saw? <em>(inferred)</em></strong></summary>

- **Answered today by** — the designer
- **Fixing it buys** — effectiveness

</details>

**This sub-step has no answer of its own on the board.** Every other sub-step in
Definition carries one.

---

## Solutioning

**Objective — produce a solution worth testing: ideas, then screens, then
something clickable.**

### First ideations

**Objective — open the solution space with PM and dev before choosing.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Which kind of workshop should I run? | A workshop | **Would change the step** | Design |
| How do I get unstuck when the ideas don't come? | Figma | Would help | Design |
| How do I run a design critique that produces decisions? *(inferred)* | Confluence | Would help | Design |

<details>
<summary><strong>Which kind of workshop should I run?</strong></summary>

- **Answered today by** — a workshop with PM and dev, written up in Confluence
- **Designers said** — *"Which kind of workshop should I run?"*
- **Fixing it buys** — time
- **What it would take** — a skill

</details>

<details>
<summary><strong>How do I get unstuck when the ideas don't come?</strong></summary>

- **Answered today by** — Figma
- **Designers said** — *"Unblocking my creativity"*
- **Fixing it buys** — effectiveness
- **What it would take** — a prompt

</details>

<details>
<summary><strong>How do I run a design critique that produces decisions? <em>(inferred)</em></strong></summary>

- **Answered today by** — Confluence
- **Fixing it buys** — effectiveness
- **What it would take** — a skill

</details>

### Sketching

**Objective — turn the chosen idea into screens and a prototype people can react
to.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| How do I keep my Figma file and my components organised? | Figma | Would help | Design |
| Which components and tokens do I use, and which variant? *(inferred)* | The GSL rulesets | **Would change the step** | Design |
| How do I build a faithful prototype without losing days to it? | Figma, Figma Make | **Would change the step** | Design |
| What status does this prototype have — exploration, test, or ready for delivery? *(inferred)* | **Nothing** | Would help | Design + Product |

<details>
<summary><strong>How do I keep my Figma file and my components organised?</strong></summary>

- **Answered today by** — Figma
- **Designers said** — *"How do I keep my Figma and my components organised?"*
- **Fixing it buys** — effectiveness
- **What it would take** — a skill

</details>

<details>
<summary><strong>Which components and tokens do I use, and which variant? <em>(inferred)</em></strong></summary>

- **Answered today by** — the GSL rulesets. This is the seven-step sequence in [the-project.md](the-project.md), deliberately not restated here
- **Fixing it buys** — time, effectiveness
- **What it would take** — a project

</details>

<details>
<summary><strong>How do I build a faithful prototype without losing days to it?</strong></summary>

- **Answered today by** — Figma · Figma Make · Lovable
- **Designers said** — *"I can spend a lot of time making a faithful prototype"*
- **Fixing it buys** — time, effectiveness
- **What it would take** — a project

</details>

<details>
<summary><strong>What status does this prototype have — exploration, test, or ready for delivery? <em>(inferred)</em></strong></summary>

- **Answered today by** — nothing
- **Fixing it buys** — project tracking
- **What it would take** — a skill
- **Note** — this is the strategy brief's **prototype passport**. It has no step on the board today

</details>

**The board's own answer for this sub-step:** *"Make prototyping easier."*

---

## Validation

**Objective — prove or disprove the hypothesis before anything is developed.**

**The ROI row is empty for every sub-step of Validation.** Nobody filled it in on
the day, so no card here says what fixing it buys.

### Testing plan

**Objective — choose how the solution gets tested.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| User test or A/B test? | The PM | Would help | Design + Product |
| How do I set this test up properly? | The PM | **Would change the step** | Research |

<details>
<summary><strong>User test or A/B test?</strong></summary>

- **Answered today by** — a point with the PM
- **Designers said** — *"Is it the right choice?"*
- **What it would take** — a prompt

</details>

<details>
<summary><strong>How do I set this test up properly?</strong></summary>

- **Answered today by** — a point with the PM
- **Designers said** — *"How do I set this test up properly?"*
- **What it would take** — a skill

</details>

**The board's own answers:** *"A tool to help me make the right decision"* and
*"A tool to help me create an A/B test."*

### Success metrics

**Objective — agree what result would count as success.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| How do I define the success metrics? | The PM, Confluence | Would help | Product |

<details>
<summary><strong>How do I define the success metrics?</strong></summary>

- **Answered today by** — a point with the PM and dev · Confluence
- **Designers said** — *"How do I define it properly?"*
- **What it would take** — a skill

</details>

**The board's own answer:** *"A tool to help me create them."*

### User guide

**Objective — write the guide the test moderator follows.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| How do I write a user guide? | Researchers, Confluence | Would help | Research |
| Which template do I use? | Confluence | Would help | Research |

<details>
<summary><strong>How do I write a user guide?</strong></summary>

- **Answered today by** — work with the PM and UX researchers · Confluence
- **Designers said** — *"How do I write a good user guide?"*
- **What it would take** — a skill

</details>

<details>
<summary><strong>Which template do I use?</strong></summary>

- **Answered today by** — Confluence
- **Designers said** — *"Which template should I use?"*
- **What it would take** — a skill

</details>

**The board's own answer:** *"A tool to help me create it — content and
format."*

### Analyze

**Objective — turn the test into findings someone can act on.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| How do I run the analysis properly? | Researchers, Dovetail | **Would change the step** | Research |
| Which template do I use? | Confluence | Would help | Research |

<details>
<summary><strong>How do I run the analysis properly?</strong></summary>

- **Answered today by** — work with the PM and UX researchers · Confluence · Dovetail
- **Designers said** — *"How do I run a good analysis?"*
- **What it would take** — a tool

</details>

<details>
<summary><strong>Which template do I use?</strong></summary>

- **Answered today by** — Confluence
- **Designers said** — *"Which template should I use?"*
- **What it would take** — a skill

---

</details>

## Follow-up

**Objective — find out whether the shipped solution actually worked, and fix it
if it didn't.**

**The ROI row is empty here too.**

### Data — does the solution work?

**Objective — read the live data against the success metrics agreed earlier.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| Is the tracking in place, and is it correct? | The PM | Would help | Engineering |
| Who actually looks at the data after release? | The PM | Not needed | Product |

<details>
<summary><strong>Is the tracking in place, and is it correct?</strong></summary>

- **Answered today by** — the PM
- **Designers said** — *"The tracking isn't done properly"*
- **What it would take** — a tool

</details>

<details>
<summary><strong>Who actually looks at the data after release?</strong></summary>

- **Answered today by** — the PM, in principle
- **Designers said** — *"Often the PM doesn't do it"*

</details>

### Iteration

**Objective — decide what to change next, from what the data says.**

| Question | Answered today | AI benefit | Owner |
| --- | --- | --- | --- |
| What do we change next, and does it need the whole process again? *(inferred)* | **Nothing** | Not needed | Design + Product |

<details>
<summary><strong>What do we change next, and does it need the whole process again? <em>(inferred)</em></strong></summary>

- **Answered today by** — nothing

</details>

**The board holds nothing at all under Iteration** — no task, no tool, no pain,
no ROI. Either it was never discussed, or nobody does it.

---

## What the board does not cover

Seven gaps, and most of them are design-system work. They are not oversights by
the designers — they are steps that happen after the board's last column, or
inside a card that says only *Prototype*.

- **Defining the content and the words.** No step, anywhere.
- **Accessibility.** Neither in design nor in development.
- **Responsive behaviour.** Named nowhere.
- **Handoff to development.**
- **Checking what shipped against what was designed.**
- **Documenting the design system**, and auditing conformity to it.
- **The prototype's status** — exploration, test, or ready for delivery.

---

## What the strategy brief already lists, per step

The brief names eighteen AI use cases, each with a maturity. Mapping them onto
the steps shows what is already claimed to exist, and what has no candidate at
all.

**The maturity labels are the brief author's assessment. Nothing here measured
them.**

| Step | Use cases the brief lists | Maturity it claims |
| --- | --- | --- |
| **Discovery** | Interview synthesis linked to its sources · Search across the research repository · Continuous analysis of CSAT, NPS, Care and Sales | Deployed · Deployed · Being industrialised |
| **Definition** | Benchmarks and patterns · Hypotheses and alternatives | Tried · Validated as an assistant |
| **Solutioning** | Flows and edge cases · Functional prototype built on the design system · Testable variants | Promising · Strongly validated · Validated |
| **Validation** | Research plans and guides · Synthetic users · AI-moderated research | Tried · Experimental · Emerging |
| **Follow-up** | Nothing | — |
| **No step on the board** | UX writing and states · Localisation and text expansion · Responsive versions · Design system documentation · Design system conformity audit · Contextualised design to code · Visual design-code QA | Mature · Mature · Validated with review · Validated · Being industrialised · Progressing fast · Rolling out |

**Seven of the eighteen have no step on the board, and six of those seven are
design-system work.** That is the clearest argument on this page for where you
take the lead: the process map stops at the prototype, and everything between
the prototype and the shipped screen is unmapped and already yours.

---

## Where the detail lives

| For | Read |
| --- | --- |
| The short version, and what "done" means in September | [the-project.md](the-project.md) |
| Every task, question and finding | [backlog.md](backlog.md) |
| The seven steps of designing a compliant screen | [the-project.md](the-project.md), *What has to be true* |

### Sources this page was built from

Named, not linked — nobody has given me the URLs yet, and this repo never
invents one.

- **Guild Design AI** — the workshop board the designers filled in.
- **Brief stratégique — Stratégie IA pour le Product Design** — the AI strategy
  written for the Design Director.
- **🇫🇷 France Product Playbook** — the product organisation's own phases,
  rituals and ownership.
