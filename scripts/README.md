# scripts/

Repo-level tools. Nothing here is part of the documentation an agent reads.

| Script | What it does |
| --- | --- |
| `check-links.py` | Checks every repo-relative link resolves, and that no ruleset points an agent at a file it may not read |
| `check-rules-docs.py` | Checks each component doc and its ruleset row name the same alternatives. Compares sets of component names, never prose |
| `check-tool-neutral.py` | Checks no component doc explains a component in terms of a tool — Figma, Zeroheight, Confluence, Storybook. A tool name is allowed in a link, nowhere else |
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

The third command takes three options, each for recording something a human
decided. The skill says when to reach for them.

| Option | What it does |
| --- | --- |
| `--place "Name=Target"` | Puts a source-only section under a different heading, at one level below it. Repeatable |
| `--table "Col\|Col=Section"` | Moves a finished table into a named section, for where the page and the doc divide the same content differently. Named by its column names. Repeatable |
| `--base=<doc>` | Merges against a copy of the doc instead of the one in `components/` |
| `--keep-zh-links` | Keeps incoming `zeroheight.com` links. By default they are unwrapped to their words |

**A section being cut from the doc is cut in a `--base` copy and the merge
re-run — never cut out of the finished draft.** The merge holds back any table
the doc already has, so a section removed afterwards takes the page's
replacement with it.

Nothing lands in `components/` until `--write` is passed to the third command,
and that waits until a human has read the result on their Desktop.

**A doc that does not exist yet** skips step three: the draft from step two is
the new doc, images and all.

**A doc that exists is always merged, never replaced.** Zeroheight has nothing
for `When to use`, `When NOT to use` or `Variant Selection Flow` — those are
written here, and a regeneration deletes them.

### What the report tells you

From `zeroheight-draft.py`:

| Line | What to do about it |
| --- | --- |
| `images found: N \| downloaded: N \| on disk: N` | From the extractor. **All three must agree**, and it exits non-zero when they do not. Run it again — the download is occasionally flaky |
| `images downloaded: N \| placed in the doc: N` | These two must match. A gap means an image has no home in the doc |
| `sections with nothing from the source` | The source genuinely had nothing. They are written as `Not documented` |
| `headings the source has and the template does not` | **A guess.** Each one was placed under the section that was open at the time. Check every line, and record each correction with `--place` |

From `zeroheight-merge.py`:

| Line | What to do about it |
| --- | --- |
| `all N source images are in the merged doc` | Nothing |
| `!! N of M source images are NOT in the merged doc` | **Chase every one.** Either a fault, or a decision that has to be written down. This is the line that caught `checkbox` losing 12 images while the draft script reported 42 of 42 placed |
| `!! N referenced files are NOT pictures` | The doc points at a file that cannot render. 36 such files exist — Figma JSON saved under a `.png` name. `check-links.py` cannot see them, because it asks whether a file exists, never whether it is a picture |
| `N cells re-pictured` | A cell whose words already matched the page was given the page's picture. Expected where the old migration put the wrong one in |
| `N cells re-pictured from the page` | The same, for a section the page has no counterpart for. The page files things differently; the sentences still match |
| `N repeated lines dropped` | The page said something the doc already said, and it was not written twice |
| `table moved into <Section>` | A `--table` instruction was carried out. `NOT MOVED` means the column names or the section name did not match anything |


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
