# Missing images

_Images a doc still points at by remote URL, because the file itself was never
in the repo. **Two left of the original six.**_

---

## Where things stand

| | Count |
| --- | --- |
| Recorded when this page was written | 6, across 5 components |
| **Fixed 17 September 2026** | **4** |
| **Still pointing at a remote URL** | **2** |

A doc with one of these renders the image only for someone logged into
Confluence. For anyone else — and for an agent reading the repo — there is
nothing there.

---

## Still missing

| Component | Filename | Why it is still open |
| --- | --- | --- |
| [Phone number field](phone-number-field/phone-number-field.md) | `z4fLAt6uS1qLwK_92x3F2A.png` | A standalone image, not in a table, so it has no column name to match on |
| [Tag](tag/tag.md) | `3a6c28b5-6a93-47bd-89be-6ca7ad848112.png` | Same — standalone, no column name |

---

## Fixed on 17 September 2026

| Component | Filename | Replaced by |
| --- | --- | --- |
| Progress bar | `317f2597405101a14c67aa.png` | The `Default` image from its Zeroheight gallery |
| Progress bar | `95a7f115-4d70-4a3d-a70f-bfd24f54e73e.png` | The `4px` image |
| Snackbar | `056490bc-c129-4c67-86c8-6fb091b82192.png` | The `Phone (above button bar)` image |
| Text field | `0dfceb07a896e570f3ee01c.png` | The `Default empty` image |

---

## What this page said before, and why it was wrong

It said these images had been uploaded straight to Confluence after the bulk
Zeroheight sync, so no local copy existed. **The first half was right and the
conclusion was not.** The images are on Zeroheight. They were not found because
they were looked for by filename, and **the filenames are corrupted in three
different ways**:

| Corruption | Example |
| --- | --- |
| An SVG downloaded under a `.png` name | `name.svg` saved as `name.svg.png` — a bug in `scripts/zeroheight-extract.mjs`, fixed 17 Sep |
| A leading underscore dropped by the Confluence migration | `_YsTHgKXfLGgIAn8KlxOBA` became `YsTHgKXfLGgIAn8KlxOBA` |
| A character inserted | `0dfceb07a896e570f3ee01c` here, `0dceb07a896e570f3ee01c` on Zeroheight |

**What found them instead was the column name.** A doc's table says
`| Default empty | …` and the Zeroheight gallery names an image `Default empty`.
That match survives a renamed file; a filename match does not.

The two left have no table around them, so there is no name to match. They need
a person to look at the Zeroheight page and say which image it is.
