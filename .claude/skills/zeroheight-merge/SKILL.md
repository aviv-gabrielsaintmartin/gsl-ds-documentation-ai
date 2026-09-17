---
name: zeroheight-merge
description: Bring a component doc up to date with its Zeroheight page by merging, never replacing — extract the live page, lay it out against the template, then merge section by section so the repo's own hand-written content survives. Triggers on requests to update/refresh/sync a component doc's images from Zeroheight, to close a component's image gap, or on "merge <component> with Zeroheight".
metadata:
  author: Aviv
  version: "1.0.0"
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
| Both have it | **Keep the repo's words. Add the source's pictures** |
| Only the repo has it | Leave it untouched |
| Only the source has it | Add it **under the heading it sits under in the source** — appending put `Error` after `Accessibility`, reading as a new top-level topic |
| The source section's content is **already on the page under another heading** | Do not add the section. Put its pictures where the words already are |
| **The page hero** | **Always a replacement, never an addition** |

### The hero needs its own exception, every time

Three separate bugs came from treating the hero as an ordinary image:

1. Appending it gave the page **two heroes**, the wrong one first.
2. The loose-image cleanup **deleted it**, because a hero also sits directly
   above a table — the readiness table.
3. The do/don't placer added a second one before the same rule was written down.

If you touch image placement, check the hero first.

## Known traps

| Trap | What it produced |
| --- | --- |
| **Matching a table by image hash** | The source reuses one image across blocks, so it finds the wrong table. `toggle` came out as `\| Left \| Hover \| Right \| Disabled selected \|` — two positions and two states in one row, saying something false. **Match by column name instead** |
| **Replacing an image reference as text** | The docs reuse one picture across cells — `button-card` uses a single file in **seven**. One decision changed all seven. **Address the cell by line and column index** |
| **Classifying a heading by its name** | `Width`, `Labels`, `Device`, `Horizontal scroll` all look like misfiled sections and are real variant categories. `Overflow content` is behaviour in `text-area` and genuinely writing guidance in `radio-button-group`. **Read the section. A name decides nothing** |
| **Checking only a section's first sentence** for whether the page already has it | Four sections open with an image or a caption, so the check missed them and the page printed the same paragraph twice. **Ask how much of the section is already there** |
| **Forcing `.png` on every download** | 30 of `tables`' 35 images are SVG. They landed as `name.svg.png` and matched nothing, and the gap report claimed 31 images had vanished from the source. Fixed in the extractor; the lesson is that a filename mismatch is usually a bug, not a missing file |
| **Trusting a filename to identify an image** | Three corruptions exist: an SVG under a `.png` name, a leading underscore dropped by the Confluence migration (`_YsTHg…` → `YsTHg…`), and a character inserted (`0d**f**ceb07…` against `0dceb07…`). Normalise before comparing |
| **A stable image count meaning a complete page** | `phone-number-field` returned 4 images from a page holding 40, twice running. The extractor now sweeps until as many images have loaded as the page declares, and exits non-zero if it never gets there |

## After a merge is applied

1. Delete images nothing points at — they are the pictures the merge replaced.
2. `python3 scripts/check-links.py` — must be clean.
3. `python3 components/coverage.py` and `python3 components/template-drift.py`.
4. Commit. One component, one commit.

## What this replaces

`zeroheight-confluence-transfer` describes the older route — Zeroheight export
staged in Confluence, then written to a Confluence page. **That route is not used
for repo docs any more.** This skill reads Zeroheight directly. Use the old skill
only when the target really is a Confluence page.
