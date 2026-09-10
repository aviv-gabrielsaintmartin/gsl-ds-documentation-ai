# What is in this folder

A guide to the files, for anyone opening `tokens/` and wondering what all of it
is. For the *content*, start at [tokens-index.md](tokens-index.md) — this page is only about
which file does what.

**One folder per token category**, the same way `components/` works. Everything
about shadow is in `shadow/`, everything about colour is in `color/`.

## The four kinds of file

**The filename suffix tells you what a file is.** Inside any category folder:

| Suffix | What it is | Written by | Edit by hand? |
| --- | --- | --- | --- |
| `-tokens.md` | The token page — what exists, values, when to use each | a human | yes |
| `-rules-ai.md` | The ruleset — what an agent may reach for | a human, from the audit | yes |
| `-usage-audit.md` | The audit — why, and what was rejected | a human, from evidence | yes |
| `-usage-ledger.md` | The raw evidence table the audit cites | **a script** | **no — re-run the script** |
| `-usage-ledger.json` | The same data for the scripts. Not committed | **a script** | **no** |

A **token page** says what exists. A **ruleset** says what you're allowed to
reach for. An **audit** says why, and records what was rejected. A **ledger** is
the raw table both were built from — every token, and every component that binds
it. Only three categories were big enough to need a ruleset and a ledger.

Note the pair `-usage-audit.md` and `-usage-ledger.md`: the audit is written by a
person and safe to edit; the ledger is script output and will be overwritten.

## At the top level

| File | What it is |
| --- | --- |
| [tokens-index.md](tokens-index.md) | The index. Every category, its page, and its headline finding. What an AI agent reads first. |
| [review-progress.md](review-progress.md) | Running record of which categories have been reviewed. |
| `README.md` | This file. |

## The category folders

| Folder | Holds | Covers |
| --- | --- | --- |
| [color/](color/) | 13 files | Colour — the only category needing several pages |
| [typography/](typography/) | page · ruleset · audit · ledger | Text styles, 32 per brand |
| [spacing/](spacing/) | page · ruleset · audit · ledger | Padding, gaps, margins. Its ruleset, audit and ledger also cover sizing |
| [sizing/](sizing/) | page | Fixed widths and heights. Code-only — not a Figma property |
| [radius/](radius/) | page · audit | Corner radius |
| [shadow/](shadow/) | page · audit | Elevation |
| [border-width/](border-width/) | page | Stroke widths |
| [breakpoint/](breakpoint/) | page | Viewport tiers, and how components respond to them |
| [grid/](grid/) | page | Column grid. Figma and product pages only — no component uses it |
| [motion/](motion/) | page | Animation durations and easings |
| [opacity/](opacity/) | page | Opacity scale |
| [z-index/](z-index/) | page | Stacking order |

## Inside `color/`

Colour is the one category with more than three files, because it has seven
family pages rather than one.

| File | What it is |
| --- | --- |
| [color-tokens.md](color/color-tokens.md) | Index for the seven family pages |
| `background.md` | The page canvas |
| `surface.md` | Component fills |
| `border.md` | Strokes and outlines |
| `content.md` | Text and icon colours |
| `symbols.md` | Illustration/icon fills — Figma-only, not used in web code |
| `scale.md` | DPE and CO₂ colours — France, classes A to G. Used by every energy component |
| `native.md` | iOS/Android colours — never web |
| [color-rules-ai.md](color/color-rules-ai.md) | The ruleset |
| [color-usage-audit.md](color/color-usage-audit.md) | The evidence |
| `surface-border-combination-audit.md` | Draft: which surface/border pairs work together. Not yet a ruleset |

## `scripts/` — how the evidence stays true

Four Python scripts. They only **read** the design-system code repo and never
change it. Run them to refresh the **Used by** columns after the code changes —
without them, the evidence in these docs slowly goes stale.

| File | What it does |
| --- | --- |
| `extract_color_usage.py` | Reads every colour token and component binding, writes the colour ledger |
| `extract_typography_usage.py` | The same for text styles |
| `extract_spacing_usage.py` | The same for spacing and sizing, and checks two documented spacing rules |
| `annotate_family_pages.py` | Rewrites the **Used by** column in the four colour family pages. Safe to re-run — it replaces the column rather than adding another |

Typical refresh, from the repo root:

```
python3 tokens/scripts/extract_color_usage.py --code-repo ../gsl-core-web-design-system
python3 tokens/scripts/annotate_family_pages.py
```

Add `--check` to `annotate_family_pages.py` to see what *would* change without
writing anything.

## A note on the generated files

`color/color-usage-ledger.md`, `typography/…` and `spacing/…` are written by the
scripts, and sit alongside the hand-written files they support. They are the
evidence the audits link to: every token, its value, and which components bind
it — plus, for colour, the role/state consistency tables and the light-mode
collision analysis.

They give the **per-component** view ("what does `chip` bind?"), which the token
pages don't — those are organised per token.

**Don't edit them.** If one looks wrong, fix the script or re-run it. The `.json`
beside each is the same data in machine form, is not committed, and is
regenerated on demand.
