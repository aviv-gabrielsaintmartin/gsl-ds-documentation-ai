# scripts/

Repo-level tools. Nothing here is part of the documentation an agent reads.

| Script | What it does |
| --- | --- |
| `check-links.py` | Checks every repo-relative link resolves, and that no ruleset points an agent at a file it may not read |
| `zeroheight-extract.mjs` | Renders one Zeroheight component page, scrolls it, and saves its blocks plus every content image |
| `zeroheight-draft.py` | Turns one extraction into a draft component doc, laid out against `components/component-template.md` |
| `zeroheight-merge.py` | Merges that draft into the doc the repo already has, section by section, so nothing hand-written is lost |

## Updating a component from Zeroheight

**Read `.claude/skills/zeroheight-merge/SKILL.md` first.** It carries the
reasoning and the traps; this is only the command sequence.

```bash
node scripts/zeroheight-extract.mjs <zeroheight-page-url> <out-dir>
python3 scripts/zeroheight-draft.py <out-dir> --name "Component Name"
python3 scripts/zeroheight-merge.py <component> <out-dir>/<component>.md
```

Nothing lands in `components/` until `--write` is passed to the third command,
and that waits until a human has read the result on their Desktop.

**A doc that does not exist yet** skips step three: the draft from step two is
the new doc, images and all.

**A doc that exists is always merged, never replaced.** Zeroheight has nothing
for `When to use`, `When NOT to use` or `Variant Selection Flow` — those are
written here, and a regeneration deletes them.

### What the report tells you

| Line | What to do about it |
| --- | --- |
| `images downloaded: N \| placed in the doc: N` | These two must match. A gap means an image has no home in the doc |
| `sections with nothing from the source` | The source genuinely had nothing. They are written as `Not documented` |
| `headings the source has and the template does not` | **A guess.** Each one was placed under the section that was open at the time. Check every line |

### Put the draft in front of a human

Copy the merged draft, the current doc as `<component>.CURRENT.md`, and every
image both files need into `~/Desktop/<component>-merged/`.

This is not ceremony. On the round that did `dropdown` and `modal-bottom-sheet`,
**three of the four defects found were found by reading the draft** — a picture
the new table had replaced, a duplicated table, and sub-titles that needed
bolding. No check caught any of them.

### Why it needs a browser

The Zeroheight page is client-rendered, so `curl` returns an empty shell. Images
load only once they enter the viewport, and the page scrolls inside
`.page--wrapper`, not the window — scrolling the window gets you a page with two
images on it and no error.

### Dependency

`zeroheight-extract.mjs` needs `puppeteer-core` and a local Chrome. It is the
only thing in this repo that needs Node.

```bash
npm install --prefix scripts puppeteer-core
```

Chrome is found at the usual macOS path; override with `CHROME_PATH` if yours is
elsewhere.
