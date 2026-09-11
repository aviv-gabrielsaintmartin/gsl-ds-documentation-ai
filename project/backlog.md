# Backlog

_Everything that isn't the current task. Written for Gabriel to read — open it
whenever you want the whole picture. `status.md` holds only what's active._

_Nothing here is started without approval. Updated 11 September 2026._

---

## Tasks — things I can do

### How these are sorted

The objective is an agent that designs a compliant screen with **nobody having
to correct it**. So a task's worth is how badly the thing it fixes breaks that.

**Ask this first, before anything else: does it change what lands on the Figma
canvas?** The deadline is Figma output by the end of September. An agent
designing in Figma can place any component in the libraries — whether that
component is also built on web, iOS or Android changes nothing about the page it
draws. So a defect that only affects another platform cannot outrank a Figma one
before that date, however badly it fails on its own terms. Those tasks are real
and stay on the list; they sit below everything that reaches the canvas.

Then, among the tasks that do reach the canvas:

| What goes wrong today | Why it ranks there |
| --- | --- |
| **It ships wrong, and breaks no rule doing it** | Worst. Non-compliant output leaves with confidence, and you only catch it by opening the screen and looking. Exactly the failure this project exists to prevent |
| **It stops, or asks** | Real, but it announces itself. Nothing wrong ships — you just had to step in, so "nobody corrects it" still failed |
| **The output doesn't change at all** | Only our own files are affected. Worth nothing on its own |

Then how often it comes up, then how long it takes. A silent failure on every
listing beats one on a rare screen.

**Fear the ones where the agent breaks no rule.** A stuck agent tells you it's
stuck. A confidently wrong one doesn't.

Nothing here is started without your go.

### I can start these today

#### These reach the Figma canvas

| What | What goes wrong today | How often | How long |
| --- | --- | --- | --- |
| Extend the "when nothing fits" rule to cover *exists, is correct, and doesn't physically fit* | **Ships wrong, breaks no rule.** The donut chart is 373px wide inside a 360px frame. The agent switched off a mandatory part of it and broke no rule doing so. **Parked by Gabriel, 10 Sep** — it tangles three questions and he wants them separated first: is the Figma component missing a stacked variant, is the documentation wrong, or does the component itself need fixing? Don't pick this up until that is settled | Any chart in a narrow column — so all of mobile | Half a day |
| Say where a declaration physically lives | **Stops or asks.** The rules end every invention with "declare it — state, in the output, what you built and what you ruled out". They never say **where that statement goes**: a note on the Figma frame, a code comment, the reply itself. An agent that composes something correctly still has nowhere to put the record, so the record is what gets dropped — and the declaration is the only thing that makes an invention reviewable. The principle stays platform-neutral; the place is named per platform, the way *Platform limits* already works. **Agreed with Gabriel 11 Sep as the task after the simulator routing entry** | Every time anything is composed rather than selected | Half a day |
| Finish the colour ruleset's restricted list | **Stops or asks.** The pointer into the audit is **already gone** — removed while freeing the energy colours, so this is no longer a dead end. What remains: the list still says "and 28 others" and enumerates only about ten of them, so an agent asking about an unusual token gets no answer. The audit's own section is grouped by family too, so the per-token reasons have to be written, not copied | Any screen using an unusual colour token | Half an hour |
| Take the clickable audit links out of the six ruleset header lines | **Stops or asks, at worst.** Each ruleset opens with a line like *"Evidence and reasoning: color-usage-audit.md"* as a live link. An agent is told to read `-rules-ai` files and nothing else, so the top of the file offers a door it must not open — and labels it "reasoning", which is what an unsure agent goes looking for. No evidence any agent has followed one; the fix is to keep the sentence and drop the link | Every ruleset an agent opens | Half an hour |
| Fix the seven remaining places where a ruleset sends an agent to evidence it may not read | **Stops or asks.** Was nine, then eight; two are fixed — the rule that stopped mid-answer and said see the audit is gone. `scripts/check-links.py` names the rest exactly: **six are header credit lines** (their own row above) and **one is mid-file** — `shadow-rules-ai.md:113`, which does give the agent a fallback, so only the stray link needs removing. Do the header-lines row and this one is a five-minute job | Every time an agent follows a ruleset to the end | An hour, once the two rows above are done |
| Have a generating agent build from the three new rulesets and nothing else | Neither — it **finds** problems rather than fixing any. Same method found twelve defects in component selection. Run it *after* the fixes above, or we test rulesets we're about to rewrite. **Run it on Sonnet, not Opus** — not to save money, but because a stronger reader silently repairs ambiguity, so testing a spec meant to be unambiguous on the strongest available reader is the weakest version of the test | — | Half a day |

#### These don't reach the canvas

Real defects, and they stay on the list. But none of them changes a Figma
page, so none can outrank the block above before the end of September.

| What | What goes wrong today | How often | How long |
| --- | --- | --- | --- |
| Generate the web availability list from the web code repo | **Ships wrong, breaks no rule — proven, not theorised.** The list built from the component docs was wrong for five of thirteen. `~/gsl-core-web-design-system` is ground truth: `libraries/ui/src/` and `libraries/patterns/`. The work is not the lookup but the name matching — Figma calls it `Bar graph`, the code calls it `barchart`; `Modal Bottom Sheet` maps to `Modal`; `Energy Tag` maps to neither `tag` nor `energyclassslider` cleanly. That matching is judgement, roughly 98 Figma names against 60 code directories | Every web screen | Half a day |
| Add the missing platform-readiness rows to three component docs | **Stops or asks.** `date-picker`, `phone-number-field` and `tabs` have no `Figma \| Web \| iOS \| Android` row at all, and the other 52 do. **Less urgent than it was:** the ruleset no longer singles them out — it now says web, iOS and Android are unestablished for *every* component, so these three are no longer a special case. It matters again the moment web availability is answered properly, and all three are in fact live on web | When web availability is next attempted | An hour, once the real statuses are known |
| Scale the availability table to iOS and Android | **Stops or asks.** Only **Figma** is answered completely. Web was attempted, found wrong, and reverted — it now says "not established, ask", the same as iOS and Android. The component docs record 22 components unavailable on iOS and 31 on Android, and none of it is in the ruleset. **Do not copy those rows in.** The web pass proved the docs' readiness rows are stale; there is no reason to think the iOS and Android columns are any better, and neither native code repo is on this machine to check against | Every iOS or Android screen | Unknown until a source is found |
| Fix two rules files that still name renamed files, and teach the link check to see bare filenames | **Stops or asks, and only ever a session working in this repo — never a shipped screen.** A defect we created ourselves: `.claude/rules/component-docs.md:22` tells a session the component index is `components.md`; it is `components-index.md`. `.claude/rules/token-docs.md:16` says the same about `tokens.md`. Both are live instructions naming files that no longer exist. `scripts/check-links.py` missed them because it only reads bracket-and-parenthesis links, not names in backticks — a rename check that only sees links is half a check. The same script also reads link syntax written *inside* backticks as a real link, so a row like this one can make the checker report a break that isn't there. It is worded around that today; the bug is still in the script, and a checker that cries wolf gets ignored | Every session that opens either rules file | Half an hour |

**The "Legend" task is done, and it did not settle the chart-sizing one.** They
looked like one fix — both "the component exists and is right, but I can't use
it in the form I need". They aren't. The legend was never placeable at all, so
the answer was to stop calling it a component. The donut is placeable and simply
too wide, which is still an open question about the component itself.

**The routing-entry task is done, and it did not settle the chart-sizing one
either.** It sends a simulator to compose-and-declare because no Pattern or
Experience is that block. The donut chart is the opposite case — the component
exists and is right, and simply does not fit the width. Compose-and-declare has
no answer for that, which is why the chart-sizing task is still parked and still
needs your three-way decision.

**Removing the leftover rule numbers in the spacing ruleset is not on this
list.** The file still says "Rules 6 and 7 are unverified" and "Rules 3–5" after
the renaming, which is untidy, but an agent's output doesn't change. It's a
rider on whatever next opens that file, not a task.

### Something is in the way

| What | What goes wrong today | What's in the way | How long once clear |
| --- | --- | --- | --- |
| Add the missing legend-position property to `Donut chart`, then re-record it | **Stops or asks.** The donut's shape would allow its legend beside the chart, not only below, and that property does not exist in the Figma library. The ruleset now tells an agent plainly that the option isn't there, so nothing ships wrong — but it's an option the design genuinely wants. **Two halves:** the Figma edit is yours or the library owner's, then `figma-sync-component-sets` is re-run on the Patterns library so the new property is recorded and the "not available" line comes out of the ruleset. Skipping the second half is how a Figma fix goes undocumented | **The Figma edit being made** | Half an hour for the sync, once it is |
| Check whether `.Legend` is used loose anywhere in the Figma files | **Ships wrong, breaks no rule.** The ruleset now forbids placing a dot-prefixed part. If a designer has already dropped `.Legend` beside a chart somewhere, that file disagrees with the rule, and an agent copying an existing screen would inherit the mistake. Unknown either way today | **A session running off `~/.claude/`, with Figma Desktop open.** This one has no Figma tools | An hour |
| Check `Energy Tag`'s 48 Figma variants against the corrected energy mapping | **Ships wrong, breaks no rule.** The French DPE class-to-colour mapping now in the colour ruleset is verified against web source code and has never been checked against Figma. `Energy Tag` is recorded with 48 variants and no property names, so nothing local can answer it. If Figma assigns classes differently from web, one of the two is wrong and a generating agent is following whichever we wrote down. Hits every French listing | **A session running off `~/.claude/`, with Figma Desktop open.** This one has no Figma tools | Half a day |
| Record the Figma text-field names for each component | **Ships wrong, breaks no rule.** An agent can place a component but has no way to put words into it, so it ships with the default placeholder text still in place — which breaks nothing. Every string in the test came from reading Figma live, not from this repo | **A session running off `~/.claude/`, plus Figma Desktop open.** The Figma plugin is installed in that config only; a session on `~/.claude-personal/` has no Figma tools at all. Check the bridge responds before starting, not after | A day |
| Check the page-layout rules against real screens | Unknown, and that's the problem — margins and rhythm are written but have never been checked against a real screen | **You naming 3–5 Figma screens** to check them against | Unknown |
| Write up the test run properly | The output doesn't change. Findings are already safe in `project/archive/handoff.md` and in this file's notes | Nothing — you parked it | Half a day |

## Questions — only you can answer these

Around two dozen, collected from the audit files where they'd been piling up
unseen. I'll bring them **one at a time**, with a recommendation. Listed here so
you can see the whole set.

### The heavy one

| Question | Why it matters |
| --- | --- |
| **The energy filter slider ships on web and was never added to the Figma libraries. Do we get it added, or tell agents to compose it from existing components?** | A design agent asked to build an energy filter has working web code it cannot use and no Figma component to place. Composing it by hand is the failure this project exists to prevent, so "compose it" needs to be a deliberate decision with a declaration rule, not a default |

**The DPE colour question that sat here is answered.** It asked who owns the
energy colours and what an agent does when a legally required element has no
compliant component. The premise was wrong: a GSL component does consume those
colours, our own ruleset was the only thing forbidding them, and the French
class-to-colour mapping is now written and verified against web code. The one
loose end — whether Figma's `Energy Tag` agrees — is a task, not a question.

### About how the rules are organised

| Question | Why it matters |
| --- | --- |
| **Should Figma get its own ruleset file, instead of a fenced Figma section inside the neutral one?** | Raised 10 Sep while fixing the Legend rule. Today one file holds the platform-neutral "which component" rules plus a fenced section per platform, and the Figma section overrides the neutral part. It works, and it keeps the contract in one place. A separate file would separate them harder but means two files to keep in step. **Recommendation: not before the end of September** — revisit after the deadline |
| **Should the "three things we name that aren't components" table move out of *Platform limits*?** | Same underlying question, found the same day. That table holds "Card grid", "Infinite scroll" and now "Legend" — none of which is a component on *any* platform, so the content is platform-neutral and it is sitting inside a platform section. It is there for a mechanical reason: *Platform limits* overrides *Which component*, so anything inside it wins, which is exactly what a "never place this" needs. Moving it out means restating that precedence explicitly. **Recommendation: leave it until after September**, then decide both organisation questions together |

### About components

| Question |
| --- |
| `Image Ratio` and `Brand Logo` exist in two libraries under different keys — which should an agent use? |
| Seven components can be selected but are described nowhere. What are they for? |
| Is `Badge` something you pick on its own, or only ever attached to a host? |
| Is `Filter button` pickable on its own, or only inside `Filter bar`? |
| `Tab Bar` is being rebuilt — confirm agents should not use it meanwhile |
| `Footer` is Figma-only and owned by another team — confirm it stays out of scope |
| Is `Flag` just an asset, or a real component for country and locale? |
| Four documented components are missing from the selection guide |
| Does anything follow "Identity and media" on the live Confluence page? |
| 24 components can be selected but have no documentation and no routing entry. Add entries for them? |
| `Floor selection` has one named part and needs two to qualify. What's the second? |
| How do we catch an agent that hand-builds an empty state instead of using the real one? |

### About colours

| Question |
| --- |
| Should borders gain a genuinely transparent token? |
| What exactly belongs to the `Decorative` colour family? Its boundary is too vague to apply |
| Two surface colours (`Accent/Light` and `Active`) resolve to the same value — deliberate? |
| The colour table still needs completing against Figma |

### About text, shadow, borders and grid

| Question |
| --- |
| No rule separates the two middle shadow levels. Both are used by similar floating components |
| The `Display` text style was never seen on any screen we sampled. Is it actually used? |
| Does the "emphasis plus container size" mechanism hold beyond the three screens checked? |
| A text style renders differently from its recorded value — worth telling whoever owns that Figma file |
| `Energy tag`'s border can't be confirmed; the Figma link we were given pointed at `Checkbox` |
| Is it still true that there's no live grid layout system? |

---

## Notes — recorded, no action needed

Things that turned out to be true and are worth not rediscovering.

| Date | Note |
| --- | --- |
| 11 Sep 2026 | **The Patterns and Experiences libraries have been listed end to end, and there are fewer of them than the inventory suggests** — 21 Patterns and 11 Experiences, read straight from `figma/figma-patterns-registry.json` and `figma/figma-experiences-registry.json`. Worth not re-deriving: the next time a rule needs to claim "no higher-tier component is this", the whole set is small enough to check by eye rather than to assume. Patterns: `Bar graph`, `Breadcrumb`, `Burger menu`, `Burger menu (profil)`, `Date Field`, `Date Picker`, `Donut chart`, `Feedback Bar`, `Filter bar`, `Filter button`, `Filter dropdown container`, `Footer`, `Info State`, `KPI`, `Line chart`, `Media Upload`, `Mega menus`, `Menus`, `Navigation bar`, `Top Bar`, `Wizard`. Experiences: `Estimation card`, `Floor selection`, `Listing Card`, `Listing summary`, `Map Polygon`, `Map Polygon backdrop`, `Map template`, `Phone Number Field`, `Table`, `mapPinsV2_IWT`, `mapPinsV2_SL` |
| 11 Sep 2026 | **The component ruleset now describes `Estimation card` in one place and calls it undescribed in two others.** The new simulator rule says what it is — a finished estimate with price range, confidence, and a selling-or-renting type, all sourced from its registry entry. Two older lines still read `⚠︎ undescribed, see audit`. They are not wrong in fact: they mean *there is no usage doc page*, which is still true. But an agent reading a description and then being told the thing is undescribed has been given two answers. Not a defect worth its own task — a rider on whatever next opens that file, alongside the leftover rule numbers in the spacing ruleset |
| 11 Sep 2026 | **A task that corrects a file can leave behind a sentence saying it hasn't been corrected.** The colour ruleset carried *"The audit file still says 83"* — true when written, falsified hours later by the same task, which fixed the number in seven places across the audit but not the sentence pointing at it. Both files had said 73 for a day. The harm is specific: an agent reads the ruleset and may **not** open the audit, so it was being told a correct figure is disputed with no way to check. Worth watching for whenever a correction spans two files — fix the claim *about* the other file, not just the number in it |
| 11 Sep 2026 | **Graphify is retired, and the graph is archived outside the repo.** It cost 990,970 tokens to maintain a knowledge graph over a 172,818-word corpus — 4.2× what reading the whole repo costs — and was queried exactly once, by the session that built it. A targeted grep answers the same questions for about 220 tokens, and this repo is already hand-indexed by the filename grammar, the routing pages and the where-to-look table. The graph, its config and the full reasoning now live in `~/Desktop/ai/gsl-ds-graphify-archive/`; the decision is in `project/decisions.md`. `CLAUDE.md` says plainly not to rebuild it, because the skill is installed globally and will otherwise offer itself to a future session as if nobody had set it up yet |
| 10 Sep 2026 | **Splitting work between a planning model and a cheaper executing model was considered and dropped — for now.** The idea: Opus writes an unambiguous spec, a cheaper worker carries it out, Opus checks. It is possible — a sub-agent is defined by one file in `.claude/agents/` that pins its own model, and it appears as a block inside the same chat, nothing to switch and nothing to remember. A hook **cannot** do it: hooks can only block a model switch someone else asked for, never start one, so there is no way to flip the session model automatically. Dropped because only three open rows qualify, all half-hour jobs, and deciding it cost more than it would ever have saved. **What would reverse it: a task with real fan-out** — the Figma registry syncs (~455 icons, ~98 component sets), or matching 98 Figma names against 60 code directories. On one of those a pinned worker pays for itself inside a single task, and it should be raised then. **The test for whether a task can be handed over at all:** needing a lot of *files* is fine — the worker reads them in its own context, which is the win. Needing a lot of *the conversation* disqualifies it. If writing the spec means writing down the thinking, the thinking is the task and there is nothing to hand over |
| 10 Sep 2026 | **The task list was sorted by damage but never by deadline, and it put a web defect next on a Figma project.** Fixed 10 Sep: the first question is now whether a task changes what lands on the Figma canvas. An agent designing in Figma can place any component in the libraries, so whether one is also built on web changes nothing about the page it draws. Seven tasks reach the canvas, four do not |
| 10 Sep 2026 | **Five backlog rows had gone stale in a single session, three of them falsified by the task being logged at the time.** Adding new findings was in the check skill; re-reading existing rows was not. `task-check` now corrects rows about files the task touched — `status.md` and the backlog directly, anything else reported and asked about first |
| 10 Sep 2026 | **The French energy ladder in `scale.md` was wrong for five of its seven classes, and the error had a shape.** The German scale was recorded correctly, then the French column was filled in by walking the same palette from the start and taking the first seven steps. France does not work that way — seven classes still have to span green to red, so the code samples across the palette, skipping `Green300` and `Yellow200` and reaching `Red100`/`Red200` at the bottom. Measured on the hex values: the old ladder ended at a warmth of +44 at class G, which is where class **E** sits on the corrected scale. G — the worst rating — was an amber |
| 10 Sep 2026 | **Audits get corrected in the same task that disproves them; the decision log never does.** Gabriel's call, 10 Sep: raise it while you are already in the topic rather than filing it for later — and still ask before touching the file, exactly like any other change. The convention sets *when* it is raised, not whether it needs approval. Written into `CLAUDE.md`. The line is what the file is for — an audit describes the system, so a figure known to be wrong is just wrong; `project/decisions.md` records what was believed on a date, and correcting that destroys its only purpose. First application: the colour audit's "83 tokens have no consumer" corrected to 73 in seven places |
| 10 Sep 2026 | **The colour ruleset's claim that nothing consumes the energy colours is false.** It lists `Scale/*` under **Never use** — *"consumed by an external team, not by any GSL component"*. `libraries/patterns/energyclassslider/src/EnergyScale.tsx` in the GSL web repo binds `scales.energy.green100` through `scales.energy.red200` directly. A GSL component consumes them. The audit's headline "83 of 218 tokens have no consumer" is overstated by at least the 12 energy tokens |
| 10 Sep 2026 | **The energy filter slider ships on web and was never added to the Figma libraries** — Gabriel, 10 Sep. It lets someone filter listings by energy range (A to C). So a design agent asked to build a search filter has working web code to copy and no Figma component to place. Colour varies by country; France is the only target, and brand makes no difference |
| 10 Sep 2026 | **The component docs' platform-readiness rows are stale, and building anything on them produces confident wrong answers.** Checked all 13 web statuses against the web code repo at `~/gsl-core-web-design-system`: five components the docs call `To Do`/`WIP`/`In progress` on web are shipping today — `Bar graph` (`libraries/patterns/barchart`), `Coachmark`, `Line chart` (`libraries/patterns/linechart`), `Segmented Control` and `Slider`. All three docs with no readiness row at all — `Tabs`, `Date Picker`, `Phone Number Field` — are also live on web. Gabriel spotted this from memory before any check was run |
| 10 Sep 2026 | **The web code repo is the real answer to "does this component exist on web", and it is already on this machine** — `~/gsl-core-web-design-system`, components at `libraries/ui/src/` and `libraries/patterns/`. `tokens/scripts/` already reads that repo to generate the token ledgers, so a generated availability list follows a pattern this repo has used before. A hand-copied list drifts; a generated one cannot |
| 10 Sep 2026 | **The web repo's per-component agent files are auto-generated, and not the finished contract they look like.** `ds-bundle/components/<area>/<Component>/<Component>.prompt.md` is one file per component with variants and a typed prop interface — but read in full, `Tabs.prompt.md` mixes 13 real props with 14 generic layout passthroughs (`marginTop`, `zIndex`, `order`) each carrying the same meaningless comment, and its **"Variants" list is padded with Storybook interaction tests** — *Should Handle Selection With Keyboard*, *Should Not Select Disabled Tabs* — presented exactly like real design variants. An agent would choose a test as a variant. Useful as evidence of what exists on web; unsafe as a contract. The earlier note here called it "what we're writing by hand", which overstated it |
| 10 Sep 2026 | **An energy scale exists in web code** — `libraries/patterns/energyclassslider/src/EnergyScale.tsx`, alongside `EnergyClassSlider.tsx`. The energy-rating (DPE) colour question is the highest-impact open item on this page and was framed as *no GSL component does this*. That framing may be wrong for web. Worth reading before answering the question |
| 10 Sep 2026 | **`Navigation Bar (App)` and `Navigation bar` are two different components — checked, and they do not contradict each other.** The ruleset's platform table says `Navigation Bar (App)` is mobile-only; `navigation-bar.md` says Ready on web. Those looked like the same component stated two opposite ways. They are not: the inventory carries both, the app one with no doc. Recorded because the near-identical names invite exactly this mistake, and it was made here once already |
| 9 Sep 2026 | **"Widen the `audit` branch category" was deleted from the task list, not done.** It only ever named one skill, and branches are gone from this repo entirely. Recorded here in case it ever needs bringing back |
| 10 Sep 2026 | **There are two Claude config folders on this machine, and they do not share their tools.** `~/.claude/` holds the four personal skills and the Figma plugin; `~/.claude-personal/` is a second, complete config with neither. Whichever a session runs off decides what it can do — one cause behind both today's missing pieces. Gabriel worked this out; the earlier note here blamed background sessions, which was wrong |
| 10 Sep 2026 | **The skills half is fixed:** `~/.claude-personal/skills` is now a link to `~/.claude/skills`, so both configs see the same four. Takes effect in new sessions, not ones already running. **Figma is not fixed** — plugins carry install state and an `enabledPlugins` setting the second config lacks, so the same trick is riskier and was left alone |
| 9 Sep 2026 | Corner radius is applied in Figma as a plain number, never as a bound variable — confirmed across the component library and three real screens. A generating agent must set the value, and a checker must not flag it as an unbound token |
| 9 Sep 2026 | Border thickness has no separate evidence file; its rules come from the notes inside its own token page. Honest, but it is the one ruleset without a sibling audit |
| 9 Sep 2026 | The "Newest" sort control on the real results-list screen is a hand-built frame, not a real Button — spotted during the radius audit. Exactly the failure this project exists to prevent, in a shipped screen |
| 9 Sep 2026 | **Only three files knew about the new way of working** — `CLAUDE.md`, `status.md` and this one. The rules file for `project/` still specified the old four-step ritual and loads automatically, so a future session would have been handed the old process. Became the next task |
| 9 Sep 2026 | **The corner-radius and shadow rules already existed and were already verified** — radius against nine components and three screens, shadow against eight components. The gap was only that they sit in files agents are told not to read as rules. Turned that task from research into moving text |
| 9 Sep 2026 | Twelve brand PDFs in `design-language/` were deleted by another session; Gabriel confirmed the removal. The folder is gone |
| 10 Sep 2026 | `status.md` is back inside its one-screen budget at 897 words, after the three git commands were cut. The next thing added to it still has to push something else out |
| 10 Sep 2026 | **The graph was rebuilt scoped and now passes the test the old one failed.** 583 things, 822 connections, 57 groups, from 143 files. Asked the same question — what does `-rules-ai` mean and who reads it — every source it returned is a live file: the decision log, `CLAUDE.md`, `README.md`, `tokens/README.md`. No archived briefs, no deleted PDF, and the retired four-step ritual is gone. The 9 Sep graph answered the same question citing all four |
| 10 Sep 2026 | **Scoping bought accuracy, not money.** The rebuild cost 814,930 tokens against the first run's 998,164 — 18% less, for 92% less text. Reading is not where the cost sits; the number of separate things to reason about is. Assume roughly this much again for any full rebuild, and use `--update` for anything smaller |
| 10 Sep 2026 | **49 of 936 connections point at something that isn't in the graph.** Six agents read the repo in parallel and split on what to do about links crossing between their batches — two emitted them, two deliberately did not. So whether a "Related components" link survives depends on which batch happened to hold that file. Never read a missing connection as "these two things are unrelated" |
| 10 Sep 2026 | **A dated entry in `project/decisions.md` still names `components.md`, and should stay that way.** It records what was true in August. Rewriting a decision log so it matches today makes it useless as a record — the point of the log is that it says what was believed when |
| 10 Sep 2026 | **Renaming a path-scoped rules file does not break it.** Verified live: after `.claude/rules/components.md` became `component-docs.md`, reading a file in `components/` still loaded it. The frontmatter `paths:` block does the work; the filename is free |
| 10 Sep 2026 | **Nothing in this repo checks that links resolve.** Deleting a file by hand can leave a ruleset pointing at something that no longer exists, and only reading catches it. `/task-next` now runs `git status` first and traces what referenced anything deleted — that covers a deletion you haven't committed yet, not one already committed |
| 10 Sep 2026 | **`internal/git-basics-tutorial.md` is about branches, which this repo stopped using on 9 Sep.** Starting a topic, worktrees, which branch a chat is on — none of it applies any more. It also only ever covered `git status`, not `git log` or `git revert`. Nothing depends on it, so nothing is broken, but it now describes a workflow that no longer exists |
| 9 Sep 2026 | The eight human-facing files totalled 15,400 words — about 60 pages. That, not the 120 machine files, is what made the project unreadable |

---

## Done

| Date | What |
| --- | --- |
| 11 Sep 2026 | **A block of controls that computes a live result now has a routing entry.** In the test the agent hand-built a mortgage simulator and then said it couldn't tell whether it should have. **Which component** now carries *Computing a figure from user input*, and it answers: no Pattern and no Experience is this block — checked against all 21 Patterns and all 11 Experiences in the registries, not assumed — so build the controls from `Slider`, `Counter Field` or `Text Field`, show the result with `KPI`, and follow **When nothing fits** to the end, declaration included. `Estimation card` is named as the near miss it is: it presents a finished estimate and carries no controls, so a simulator whose result is a price estimate is two halves — the Experience for the result, composed and declared for the controls. Verified: every component named exists in **The inventory**, the `Estimation card` description matches its registry entry, and the link check stayed at zero broken |
| 10 Sep 2026 | **A legend is switched on, not placed — and no internal part is ever placed.** The rules named `Legend` in the routing table like any other component, but all three charts carry it as a boolean and the underlying piece is private in Figma, so an agent went looking for something that cannot exist. It now says place the chart and switch its legend on. Two rules that were missing arrived with it: a Figma name starting with a dot is an internal part, reached through its parent and never placed or rebuilt — the first time that convention appears anywhere an agent reads it — and `Donut chart` has no side-placement option today, so nobody hunts for one. The first check **failed**: the Figma section still said "if it's named, you may place it", and it outranks the routing table, so permission beat the prohibition. Fixed by adding `Legend` to the short list of names that aren't components and narrowing that sentence. Figma vocabulary stayed inside the Figma section; the neutral rules stayed neutral |
| 10 Sep 2026 | **The energy colours are usable, and the mapping we held was wrong for five of seven classes.** `Scales/Energy` and `Scales/CO2` moved out of **Never use** into the colour ruleset with the French DPE classes mapped to exact tokens — verified against `EnergyScale.tsx`, the only production consumer. The old French column walked the palette from the start; France samples across it, so class G came out amber where it must be red. Corrected in the ruleset, the token page, the audit (83 orphans → 73, in seven places) and `tokens/README.md`. The ruleset now says where each rule came from and that Figma has never been checked |
| 10 Sep 2026 | **"Can I use this component here?" now has one answer for Figma, and an honest "ask" everywhere else.** Platform limits was three sources contradicting each other, seventeen spellings of readiness, and a rule that stopped mid-answer and pointed at a file agents may not read. Figma is now answered completely from the registries. The web list built from the component docs was **thrown away before it shipped** — checked against the web source code, it was wrong for five of thirteen, so web, iOS and Android now say plainly that nothing is established and the agent must ask. The dead end is gone, every component name matches the inventory, and the docs' readiness row is marked do-not-read on every platform |
| 10 Sep 2026 | **Two files called `tokens.md` and two called `components.md` — no longer.** The rules files became `token-docs.md` and `component-docs.md`, each now opening with a line saying it is an instruction for Claude, not design-system content. Nothing linked to them by name, so nothing broke. `figma-registries.md` already set the precedent that rules files are named for their subject |
| 10 Sep 2026 | **`-index` added to the filename grammar**, and the two routing pages renamed to `tokens-index.md` and `components-index.md`. They were the only two files in the repo whose names didn't follow the rule `CLAUDE.md` states. 13 links moved and the link check proves none broke. `tokens-index.md` also gained the title it never had |
| 10 Sep 2026 | **`scripts/check-links.py` written** — the repo's first repo-wide check. It answers two questions: is the file there, and is the agent allowed to read it. First run: 1,378 links, **zero broken**, nine dead ends now listed exactly instead of estimated at three |
| 9 Sep 2026 | **The retired files moved to `project/archive/`** — the old plan, the handoff note and all four briefs, with a README saying why each was retired. `decisions.md` and `README.md` deliberately stayed: one holds why the project is shaped this way, the other is the map |
| 9 Sep 2026 | **One task, one chat** — each task starts in a fresh conversation. Written into `CLAUDE.md`, `status.md` and the check skill. Not about context limits; a session that built something is the worst judge of whether it reads clearly to someone who wasn't there |
| 9 Sep 2026 | **Corner radius, shadow and border thickness now have rulesets** an agent is allowed to read — seven of twelve token kinds covered, up from three. Verified: every value matches its token page, 57 links resolve, and all three failures from the test run are now answered, including "a card is not elevated, give it a border" |
| 9 Sep 2026 | **Git simplified: one task = one commit, straight to `main`.** No branches, no pull requests. A passing check now commits and pushes automatically; undoing, deleting and rewriting always ask first. Overrides Gabriel's personal one-task-one-branch rule, for this repo only. `audit/run-001` merged into `main` and deleted; `main` is now the only branch |
| 9 Sep 2026 | The repo now describes the new way of working — the rules file for `project/` carries the loop instead of the old ritual, `README.md` opens on `status.md`, and the plan, briefs and handoff note are marked superseded. Verified: 27 links resolve, no stale skill count, no surviving instruction to write briefs |
| 9 Sep 2026 | `status.md` created — one page replacing eight |
| 9 Sep 2026 | `design-language/` removed, and the two files that described it corrected |
| 8 Sep 2026 | The rules in all four rulesets lost their numbers and gained names |
| 8 Sep 2026 | The component parts list became machine-readable |
| 8 Sep 2026 | The compliance scoring sheet written |
| 8 Sep 2026 | Component selection written and tested cold, three rounds |
