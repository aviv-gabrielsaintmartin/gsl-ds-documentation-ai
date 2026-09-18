---
name: zeroheight-merge
description: Bring a component doc up to date with its Zeroheight page by merging, never replacing — extract the live page, lay it out against the template, then merge section by section so the repo's own hand-written content survives. Triggers on requests to update/refresh/sync a component doc's images from Zeroheight, to close a component's image gap, or on "merge <component> with Zeroheight".
metadata:
  author: Aviv
  version: "1.2.0"
  status: production
---

# Zeroheight → repo merge

**Read this whole file before running anything.** Every trap below was paid for
in a session that had to undo its own work. Each one looks like the obvious
approach until you check the output.

## Objective

A component doc in `components/<name>/<name>.md` and its Zeroheight page hold
**different halves of the same documentation**. Bring the page's half in
without losing the repo's.

## The one rule everything else serves

**Never replace a doc with a regenerated one. Merge.**

Measured on `select-card-group`, 17 September 2026, section by section:

| Section | In the repo | On Zeroheight |
| --- | --- | --- |
| When to use | 14 words | **nothing** |
| When NOT to use | 21 words | **nothing** |
| Variant Selection Flow | 53 words, a hand-written decision tree | **nothing** |
| Related Components | 134 words, with Priority and Example Scenario | 100 words, two columns |
| Icons and illustration | 21 words, **0 images** | 27 words, **6 images** |
| Interactive States | 29 words, **0 images** | 31 words, **8 images** |

Zeroheight fills the visual sections. The repo fills the ones a generating
agent reads. **A regeneration deletes the second set**, including decision trees
no export can produce.

One more reason, easy to miss: the repo links a related component by its path
inside this repo. A regenerated doc links `zeroheight.com` instead. **The migration exists to retire
those links** — 43 docs still carry one.

## The three steps

```bash
# 1. read the live page — renders it, scrolls it, downloads every image
node scripts/zeroheight-extract.mjs "<zeroheight url>" <out-dir>

# 2. lay it out against components/component-template.md
python3 scripts/zeroheight-draft.py <out-dir> --name "Component Name"

# 3. merge it into the repo's doc — writes a .merged.md, changes nothing
python3 scripts/zeroheight-merge.py <component> <out-dir>/<component>.md
```

Add `--write` to step 3 only after a human has read the result.

### Four options, and when each is the right answer

Each one records something a human decided. **Write the decision into the
command, never into the finished draft** — by hand it is lost on the next run,
and nobody afterwards knows a human ever decided it.

| Option | Use it when |
| --- | --- |
| `--place "Name=Target"` | The draft script printed a guessed placement, you checked it, and it was wrong. Repeatable. A placed section takes its level from the heading it goes under, which is what keeps it off the drift report |
| `--table "Col\|Col=Section"` | The page and the doc divide the same content differently, so a finished table is under the wrong heading. `button-group` documents single- and multi-select under `Selection`; the page keeps those pictures inside its states block. Name the table by its column names |
| `--base=<doc>` | A section of the repo's doc has to go before the merge, not after. **See the rule below; getting this backwards costs pictures** |
| `--keep-zh-links` | Rarely. By default a `zeroheight.com` link in the incoming text is unwrapped to its words, because the migration exists to retire those links and a merge that adds more works against its own point |

**A section of the repo's doc that is being cut must be cut in a `--base` copy
and the merge re-run — never cut out of the finished draft.** Measured on
`date-picker`, 18 September 2026: the merge withholds any table the repo
already has, so the repo's `Date field` and `Date picker` subsections were
holding back the page's own `Day` and `Current day` tables. Cutting those two
subsections from the finished draft would have taken **eight pictures** with
them. Cutting them first and re-merging brought all ten state tables in, each
correctly named.

A `--place` or `--table` correction is a decision. Record it in the run's own
command so the next session can see what was decided and why the section is not
where the draft script put it.

**Get the URL from `components/components-index.md`'s own links, or from the
styleguide index page** (`/626199550/p/43e0c4-index`), which is a table of every
component with a Documentation column. Never guess a slug — a wrong one returns
a page with zero images and no error.

## The Desktop step is not optional

Copy the merged draft, the current doc as `<component>.CURRENT.md`, and every
image both need into `~/Desktop/<component>-merged/`, and **wait**.

On the round that did this for `dropdown` and `modal-bottom-sheet`, **three of
the four defects found were found by the human reading the draft**, not by any
check. They were invisible to a diff and obvious to an eye.

## How the source is shaped

Getting this wrong cost two rounds.

| Block type | Carries | Use it for |
| --- | --- | --- |
| `gallery` | each item has a **`name`** — `Default empty`, `Hover`, `Android` | Matching a table column by name |
| `dosdonts` | each item has a **`label`** (Do / Don't / Caution) and a **`caption`** — and **no name** | Building a DO/DON'T table |
| `image` | a bare image, usually the page hero | The hero slot |
| `table` | cells that may hold images | Straight conversion |

**A do/don't item reads as unnamed if you look at `name`.** Six images were
reported as unplaceable for exactly this reason. They were identifiable the
whole time.

## What the merge does, in order

| Situation | Action |
| --- | --- |
| The repo's section is empty and the source has it | Take the source's, whole |
| The repo's section is empty **but its sub-sections are full** | **Not an empty section.** Keep the repo's words, add the source's pictures |
| Both have it | **Keep the repo's words. Add the source's pictures** |
| Only the repo has it | Leave it untouched |
| Only the source has it | Add it **under the heading it sits under in the source** — appending put `Error` after `Accessibility`, reading as a new top-level topic |
| The source section's content is already on the page under another heading, **and it brings no unseen picture** | Skip the section |
| The source section's content is already on the page under another heading, **and it brings pictures nobody has** | **Add the section.** Drop any sentence of it already on the page, sentence by sentence |
| A repo cell's words match the source's, and the source's cell has a picture | **Take the source's picture**, by row and column index |
| A section's only picture is one bare unnamed image, and the source has one too | **Replacement, never an addition** — the same rule as the hero, one level down |
| **The page hero** | **Always a replacement, never an addition** |

### The hero needs its own exception, every time

Three separate bugs came from treating the hero as an ordinary image:

1. Appending it gave the page **two heroes**, the wrong one first.
2. The loose-image cleanup **deleted it**, because a hero also sits directly
   above a table — the readiness table.
3. The do/don't placer added a second one before the same rule was written down.

If you touch image placement, check the hero first.

## Read the three report lines before anything else

The merge prints three things that decide whether the draft is worth reading.

| Line | What it means | What to do |
| --- | --- | --- |
| `images found: N \| downloaded: N \| on disk: N` | From the extractor. **All three must agree** | If they do not, it exits non-zero and says so. Run it again — one `avatar` run reported 37 found and 36 downloaded, with nothing failed, and the second got all 37 |
| `all N source images are in the merged doc` | Every picture downloaded from the page has a home | Nothing |
| `!! N of M source images are NOT in the merged doc` | A picture was downloaded and dropped | **Chase every one.** It is either a fault or a decision, and a decision has to be written down |
| `!! N referenced files are NOT pictures` | The doc points at a file that cannot render | See below |

**The first of those exists because nothing was looking.** `checkbox` reported
`42 of 42 placed` from the draft script and still lost **12** in the merge —
three whole error-state tables — and no line said so. Counting what the page
gave against what the doc holds is the check that finds real damage.

### A file can be named `.png` and not be a picture

**Proved by reading the bytes, 18 September 2026: 36 files across 12 components
are Figma node JSON saved under a `.png` name**, left by the old Confluence
migration. Each begins `{"id":"4211:7239","name":"datepicker_opening_05"…` and
each renders as a broken image.

`scripts/check-links.py` cannot see this. It asks whether a file exists, never
whether it is a picture.

Where the fault sits decides what to do:

- **In a section the page also documents** — the merge replaces the section and
  the dead file goes with it. Nothing to do.
- **In a section somebody wrote here** — the merge has nothing to put in its
  place. **Stop and ask.** Choosing a replacement means reading the Zeroheight
  page and deciding which picture that cell wants, and that is not a rule.

## Known traps

| Trap | What it produced |
| --- | --- |
| **Matching a table by image hash** | The source reuses one image across blocks, so it finds the wrong table. `toggle` came out as `\| Left \| Hover \| Right \| Disabled selected \|` — two positions and two states in one row, saying something false. **Match by column name instead** |
| **Replacing an image reference as text** | The docs reuse one picture across cells — `button-card` uses a single file in **seven**. One decision changed all seven. **Address the cell by line and column index** |
| **Classifying a heading by its name** | `Width`, `Labels`, `Device`, `Horizontal scroll` all look like misfiled sections and are real variant categories. `Overflow content` is behaviour in `text-area` and genuinely writing guidance in `radio-button-group`. **Read the section. A name decides nothing** |
| **Checking only a section's first sentence** for whether the page already has it | Four sections open with an image or a caption, so the check missed them and the page printed the same paragraph twice. **Ask how much of the section is already there** |
| **Forcing `.png` on every download** | 30 of `tables`' 35 images are SVG. They landed as `name.svg.png` and matched nothing, and the gap report claimed 31 images had vanished from the source. Fixed in the extractor; the lesson is that a filename mismatch is usually a bug, not a missing file |
| **Trusting a filename to identify an image** | Three corruptions exist: an SVG under a `.png` name, a leading underscore dropped by the Confluence migration (`_YsTHg…` → `YsTHg…`), and a character inserted (`0d**f**ceb07…` against `0dceb07…`). Normalise before comparing |
| **Treating a placeholder as a prefix** | `empty()` used `startswith`, so `tag`'s "Not applicable. This component does not respond to touch or pointer interaction…" read as an empty section. The page's version replaced it and **a sentence was destroyed** — the one gate that must never move. **A placeholder is the WHOLE text or it is not a placeholder** |
| **Giving a picture-only row an identity** | A row that is two pictures and no words signs as `("","")`, and so does every other picture-only row, so each matched all the others and was pruned as a repeat. Cost `tabs` 8 pictures and `chip-group` 6. **A row is only ever compared when it has words** |
| **Pairing rows by position** | Where there is no text to match on, position is the only thing left — and `media-upload` has FOUR tables headed `Default empty \| Hover empty \| …`. All four were given the first one's pictures, **destroying 12 of them silently**. **Pair by position only when exactly one table on each side has those column names** |
| **Counting a table's header row as a shared row** | Every DO/DON'T table is headed `DO \| DON'T`, so every one matched every other and was dropped as a duplicate. `phone-number-field` lost the page's country-code guidance and its DON'T picture. **Compare data rows only** |
| **Letting a picture-only table replace one whose cells carry sentences** | `action-menu` keeps three columns of guidance with pictures inside; the page has the same three columns holding pictures alone. Treating them as one threw away all three pictures |
| **De-duplicating on only one of the four paths** | The path taken when the doc's section is empty and the page's is not brought the page's words in **without** checking whether the doc already said them. `card` and `filter-bar` each printed a sentence twice. **There is one de-duplicator and every path uses it** |
| **Requiring a repeat to be long** | 40 characters was too high a bar. `feedback-message` writes "On iOS the alignment is done manually." — 31 once flattened — and it printed twice |
| **Comparing a link with its URL attached** | `cell-content` writes "wrapped in a [card](https://…)" where the page writes "wrapped in a card". Two identical sentences looked different and the paragraph printed twice. **A link is its words, everywhere a comparison happens** |
| **Matching a section on its depth as well as its name** | The page and the doc rarely agree on depth. `coach-mark` keeps `Position` as an H4 where the page has an H3, and ended with TWO `Position` sections — the doc's empty, the page's holding all 12 pictures. **Match on name when the depth differs — but only when the page uses that name once**, because `action-menu` and `info-state` each have two different sections sharing a name |
| **Comparing a caption with its markup on** | The caption under a loose picture is bold — `**Date field**`, never `Date field`. `date-picker` kept three stale pictures above the table that replaced them, and one of the three was not even an image |
| **A DO/DON'T table counting as a replacement for a loose illustration** | Guidance is not a comparison of the same thing. `phone-number-field` lost the picture of its 448px form container |
| **Leaving a header behind when every row of a table is pruned** | A bare `\| DO \| DON'T \|` under a heading says nothing. Three in `chip-group`, one in `button-group`, found by eye. **A table goes whole when nothing is left under its rule** |
| **Matching cells only when the wording is identical** | `button-group`'s CAUTION reads "clearly communicate its meaning" in the doc and "clearly comunicate it's meaning" on the page. The cell never found its picture. Long sentences are now matched allowing for that — **and the doc's wording is what stays; only the picture moves** |
| **Assuming the page and the doc shape a table the same way** | The doc keeps `DO \| DON'T \| CAUTION` in one table where the page uses two. Row matching then finds nothing. **A picture follows its sentence, whatever table shape holds it** |
| **Keeping a heading after everything under it proved to be a repeat** | `phone-number-field` was left with a bare `### Overflow content` and nothing beneath it |
| **Judging "the page already says this" on words alone** | `checkbox`'s three error-state tables — **12 pictures** — were thrown away because the one sentence at the foot of that section happened to sit in `Touch Target & Layout`. The page had the sentence. It had none of the error states. **A section bringing pictures nobody has is not already on the page, whatever its words say** |
| **Reading a section's own body and calling it empty** | `date-picker` keeps its states under `Date field` and `Date picker`, so the parent read as empty, the source's whole states block was dropped in above them, and **eight sentences appeared twice**. **A section with full sub-sections is not an empty section** |
| **Dropping a picture block because *any* picture in it is already here** | The `date-picker` DO/DON'T row went because its DON'T was already present, taking the DO picture with it. Same on `button`, three times. **Drop a block only when EVERY picture in it is already here** |
| **Judging a table's sameness against the whole page** | `checkbox`'s error tables have the same column names as its neutral ones — `Default \| Hover \| Pressed \| Disabled` — so a whole-page check called them duplicates. **Scope the comparison to the section the pictures are going into** |
| **Giving a bold label to the first table under it only** | When that first table is dropped as already-present, the next one inherits the label above and **says something false**: `date-picker` ended with a `Day — selected` table standing under **Error**. **A label belongs to a group of tables. Write it above the first survivor of its group** |
| **Comparing a caption with its markup on** | The caption under a loose picture is bold on the page — `**Date field**`, never `Date field`. Comparing it unstripped matched nothing, and `date-picker` kept three stale pictures above the table that replaced them. **One of the three was not even an image** |
| **Sweeping every loose picture the moment a table arrives** | `button` lost its `Proportion of emphasis` figure, which has a caption of its own and nothing replacing it. **Remove a loose picture only when the caption directly under it is one of the arriving table's column names** |
| **De-duplicating line by line** | `button`'s repo doc carries the whole of the source's `Read more button` paragraph on one line, reworded in the middle. The line never matched; two of its sentences did, and both printed twice. **Compare sentence by sentence** — and once a sentence on a line has gone as a repeat, the short ones beside it are repeats too, whatever the length threshold says |
| **Inserting a sibling at the start of its parent's block** | The draft script flattens the page's heading levels, so a child often shares its parent's level. "The end of the parent's block" then means "just before the sibling added last", and `date-picker`'s three width sections came out back to front. **Insert after the last section already placed under that parent** |
| **A stable image count meaning a complete page** | `phone-number-field` returned 4 images from a page holding 40, twice running. The extractor now sweeps until as many images have loaded as the page declares, and exits non-zero if it never gets there |
| **Trusting the extractor's own tally of what it wrote** | One `avatar` run printed `found: 37 \| downloaded: 36 \| failed: 0` — arithmetic that loop cannot produce — and **exited zero**. A second run got all 37, and it has never been reproduced. **The count is now taken from the files on disk**, and a short page cannot exit zero. Do not replace that with a counter the code increments |

## Before the draft goes to a human

Four numbers, and three of them must be zero. Report all four, per component.

| Number | Must be |
| --- | --- |
| Sentences in the current doc missing from the draft | **0** |
| Sentences the merge made appear more often than either input had them | **0** |
| `zeroheight.com` links gained | **0** |
| Source images not in the draft | **0**, or each one explained |

**Count a duplicate against both inputs, not just the repo's doc.** A page
repeats itself: `media-upload` says the same sentence under `Empty drop zone`,
`Filled with image` and `Filled with file`. Counting against the repo alone
reported four duplicates that the merge had not created.

**Compare a link by its words, not its markup.** Unwrapping a `zeroheight.com`
link changes the text, and a checker that misses that reports the sentence as
new.

## After a merge is applied

1. Delete images nothing points at — they are the pictures the merge replaced.
2. `python3 scripts/check-links.py` — must be clean. **It cannot tell you
   whether a file is a picture**; the merge's own report does that.
3. `python3 components/coverage.py` and `python3 components/template-drift.py`.
4. Commit. One component, one commit.

## What this replaces

`zeroheight-confluence-transfer` describes the older route — Zeroheight export
staged in Confluence, then written to a Confluence page. **That route is not used
for repo docs any more.** This skill reads Zeroheight directly. Use the old skill
only when the target really is a Confluence page.
