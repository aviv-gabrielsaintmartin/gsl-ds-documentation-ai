<!-- GENERATED FILE — do not edit by hand. Re-run: python3 scripts/build-topic-map.py -->

# The design system — topic map

_Every design topic, and how far each one is. **Written by a script** on 5 October 2026: every mark is read out of a file. Never edit this page; re-run `scripts/build-topic-map.py`._

**This page shows what exists and what is missing.** It does not say the design system is finished.

---

## How to read it

| Mark | Meaning |
| --- | --- |
| ● Written | The rules for this topic are written down |
| ◐ Partial | Some material exists, and the rules do not, or not all of them |
| ○ Empty | Nothing is written |

**Written means the file exists.** It does not mean the rules are complete or correct.

A topic takes its mark from its sub-topics. All written gives written. All empty gives empty. Anything else gives partial.

---

## The whole picture

```
The design system
├── The parts  ◐
│   ├── Components  ◐ partial
│   ├── Tokens  ◐ partial
│   └── Icons  ● written
├── Making a screen  ◐
│   ├── Content and copy  ○ empty
│   ├── Layout  ◐ partial
│   ├── Responsive  ◐ partial
│   ├── Motion  ◐ partial
│   └── Edge cases  ○ empty
├── Writing it down  ●
│   └── The spec format  ● written
├── Building it  ◐
│   ├── Figma  ● written
│   ├── iOS  ● written
│   ├── Android  ○ empty
│   └── Web  ○ empty
└── Checking it  ●
    └── The scorecard  ● written
```

| Topic | Written | Partial | Empty |
| --- | --- | --- | --- |
| The parts | 1 | 2 | 0 |
| Making a screen | 0 | 3 | 2 |
| Writing it down | 1 | 0 | 0 |
| Building it | 2 | 0 | 2 |
| Checking it | 1 | 0 | 0 |

---

## The parts

What a screen is made of.

### Components

**Known limit:** what each variant option means is still open. Written by hand, from `status.md` of 2 October 2026.

| Sub-topic | What exists | Status |
| --- | --- | --- |
| A page for each component | 75 of 98 library entries have a page. 1 that an agent may pick has none | ◐ Partial |
| Which component to pick | [`components-rules-ai.md`](../components/components-rules-ai.md) | ● Written |
| Inside each page — Label Formula | Filled on 23% of the pages | ◐ Partial |
| Inside each page — Capitalization | Filled on 29% of the pages | ◐ Partial |
| Inside each page — a11y | Filled on 31% of the pages | ◐ Partial |
| Inside each page — Breakpoints | Filled on 33% of the pages | ◐ Partial |
| Inside each page — Length Limits | Filled on 36% of the pages | ◐ Partial |
| Inside each page — Platform | Filled on 52% of the pages | ◐ Partial |
| Inside each page — Modifiers | Filled on 67% of the pages | ◐ Partial |
| Inside each page — Variants | Filled on 69% of the pages | ◐ Partial |
| Inside each page — Touch target | Filled on 76% of the pages | ◐ Partial |
| Inside each page — Writing | Filled on 81% of the pages | ◐ Partial |
| Inside each page — States | Filled on 83% of the pages | ◐ Partial |
| Inside each page — Usage guidance | Filled on 89% of the pages | ◐ Partial |
| Inside each page — When to use | Filled on 100% of the pages | ● Written |
| Inside each page — When NOT to use | Filled on 100% of the pages | ● Written |
| Inside each page — Variant flow | Filled on 100% of the pages | ● Written |
| Inside each page — Related | Filled on 100% of the pages | ● Written |

A section is written when every page fills it, and empty when none does.

### Tokens

**6 of 12 kinds have a rules page.** A kind with values and no rules is partial.

| Kind | Values listed | Rules page | Checked against real use | Status |
| --- | --- | --- | --- | --- |
| Border width | [`border-width-tokens.md`](../tokens/border-width/border-width-tokens.md) | [`border-width-rules-ai.md`](../tokens/border-width/border-width-rules-ai.md) | No | ● Written |
| Breakpoint | [`breakpoint-tokens.md`](../tokens/breakpoint/breakpoint-tokens.md) | None | No | ◐ Partial |
| Colour | [`color-tokens.md`](../tokens/color/color-tokens.md) | [`color-rules-ai.md`](../tokens/color/color-rules-ai.md) | Yes | ● Written |
| Grid | [`grid-tokens.md`](../tokens/grid/grid-tokens.md) | None | No | ◐ Partial |
| Motion | [`motion-tokens.md`](../tokens/motion/motion-tokens.md) | None | No | ◐ Partial |
| Opacity | [`opacity-tokens.md`](../tokens/opacity/opacity-tokens.md) | None | No | ◐ Partial |
| Radius | [`radius-tokens.md`](../tokens/radius/radius-tokens.md) | [`radius-rules-ai.md`](../tokens/radius/radius-rules-ai.md) | Yes | ● Written |
| Shadow | [`shadow-tokens.md`](../tokens/shadow/shadow-tokens.md) | [`shadow-rules-ai.md`](../tokens/shadow/shadow-rules-ai.md) | Yes | ● Written |
| Sizing | [`sizing-tokens.md`](../tokens/sizing/sizing-tokens.md) | None | No | ◐ Partial |
| Spacing | [`spacing-tokens.md`](../tokens/spacing/spacing-tokens.md) | [`spacing-rules-ai.md`](../tokens/spacing/spacing-rules-ai.md) | Yes | ● Written |
| Typography | [`typography-tokens.md`](../tokens/typography/typography-tokens.md) | [`typography-rules-ai.md`](../tokens/typography/typography-rules-ai.md) | Yes | ● Written |
| Z-index | [`z-index-tokens.md`](../tokens/z-index/z-index-tokens.md) | None | No | ◐ Partial |

### Icons

| Sub-topic | What exists | Status |
| --- | --- | --- |
| The list of every icon | [`icons-index.md`](../icons/icons-index.md) | ● Written |
| Which icon to pick | [`icons-rules-ai.md`](../icons/icons-rules-ai.md) | ● Written |

---

## Making a screen

How the parts become a screen. A topic is written once it has a rules page.

| Topic | Rules page | Values listed | Inside the component pages | Status | Known limit |
| --- | --- | --- | --- | --- | --- |
| Content and copy | None | None | Writing 81%, Length Limits 36%, Capitalization 29%, Label Formula 23% | ○ Empty | No rule says what a screen should say |
| Layout | None | [`grid-tokens.md`](../tokens/grid/grid-tokens.md) | — | ◐ Partial | Card and block-title rules are held back |
| Responsive | None | [`breakpoint-tokens.md`](../tokens/breakpoint/breakpoint-tokens.md) | Breakpoints 33% | ◐ Partial | — |
| Motion | None | [`motion-tokens.md`](../tokens/motion/motion-tokens.md) | — | ◐ Partial | — |
| Edge cases | None | None | States 83% | ○ Empty | — |

**Inside the component pages** is how many pages fill the sections touching that topic. It never changes the status.

---

## Writing it down

The spec is the written description of a screen, the same for every platform.

| Sub-topic | What exists | Status | Known limit |
| --- | --- | --- | --- |
| The spec format | [`spec-rules-ai.md`](../specs/spec-rules-ai.md). 1 spec saved in `specs/` | ● Written | No field for where a block goes |

---

## Building it

A name map gives each component, token and icon its name on a platform. A platform is written once it has all three.

| Platform | What exists | Status | Known limit |
| --- | --- | --- | --- |
| Figma | 3 of 3 name maps | ● Written | `/design` builds. Illustration and card padding are still open |
| iOS | 3 of 3 name maps | ● Written | `/prototype` builds. It does not read a spec yet |
| Android | 0 of 3 name maps | ○ Empty | `/vibe` builds. It does not read a spec yet |
| Web | 0 of 3 name maps | ○ Empty | — |

**The skills that do the work:** 10 run inside this repo, in `.claude/skills/`. 2 run outside it, in `skills/`.

---

## Checking it

| Sub-topic | What exists | Status | Known limit |
| --- | --- | --- | --- |
| The scorecard | [`compliance-scorecard.md`](../compliance/compliance-scorecard.md). 1 brief, 3 runs scored | ● Written | Written for Figma. Nothing checks an app build |

---

## Added later

Part of the design system, and not on this map yet. Gabriel, 5 October 2026: generating a screen comes first.

- Research
- Problem definition
- Testing
- Prototyping guides

---

## What this page is built from

| Topic | Read from |
| --- | --- |
| Components | [`components-coverage-ledger.md`](../components/components-coverage-ledger.md). Re-run `components/coverage.py` first |
| Tokens | The files in each folder under `tokens/` |
| Icons | The files in `icons/` |
| Making a screen | Whether a rules page exists for the topic |
| Writing it down | The files in `specs/` |
| Building it | The name maps, and the registries in `figma/` |
| Checking it | The files in `compliance/` |

**Every *Known limit* is written by hand**, from `status.md` of 2 October 2026. A file count cannot see them. They live in the script and go stale unless someone updates them there.
