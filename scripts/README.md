# scripts/

Repo-level tools. Nothing here is part of the documentation an agent reads.

| Script | What it does |
| --- | --- |
| `check-links.py` | Checks every repo-relative link resolves, and that no ruleset points an agent at a file it may not read |
| `zeroheight-extract.mjs` | Renders one Zeroheight component page, scrolls it, and saves its blocks plus every content image |
| `zeroheight-draft.py` | Turns one extraction into a draft component doc, laid out against `components/component-template.md` |

## Extracting a component from Zeroheight

Two steps, both writing outside `components/`. Nothing lands in the repo until
a human moves it there.

```bash
node scripts/zeroheight-extract.mjs <zeroheight-page-url> <out-dir>
python3 scripts/zeroheight-draft.py <out-dir> --name "Component Name"
```

The result is `<out-dir>/<slug>.md` plus `<out-dir>/images/`. Move both into
`components/<slug>/` once the report below has been read.

### What the report tells you

| Line | What to do about it |
| --- | --- |
| `images downloaded: N \| placed in the doc: N` | These two must match. A gap means an image has no home in the doc |
| `sections with nothing from the source` | The source genuinely had nothing. They are written as `Not documented` |
| `headings the source has and the template does not` | **A guess.** Each one was placed under the section that was open at the time. Check every line |

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
