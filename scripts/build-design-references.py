#!/usr/bin/env python3
"""Generate the `references/` folder of the design skill, `skills/design/`.

The design skill is written here and run elsewhere — from the iOS repo, the
Android repo, the web repo or next to Figma. It cannot read this repo, so it
carries a copy of what it chooses from. **This script makes that copy.** Its
`SKILL.md` is written by hand and rarely changes; `references/` is regenerated
whenever the rules change, and never edited by hand.

What it copies:

| Reference | From |
| --- | --- |
| The component, token and icon rulesets | Every `-rules-ai.md` an agent generates from |
| The spec format | `specs/spec-rules-ai.md` |
| Which icons exist | `icons/icons-index.md` |
| What iOS can build | The three iOS name maps — components, tokens and icons |
| Each component's variants | The `## Variants & Modifiers` section of every component doc, extracted into one file |
| Which colour token inside a family | The five colour family pages, cut before `## Tokens` — their *When to use · Don't use for* tables, without the value tables |
| How Figma places each name | The `figma/*.json` registries, laid out as one table per kind in `figma-map.md`: library, key, node ID |

**Only copying and extracting. Nothing is rewritten for meaning.** Three
mechanical changes, both because the copy leaves the repo:

- A link to a file that is also in `references/` points at the copy.
- Every other link keeps its text and loses its target. Outside this repo the
  target does not exist, and a dead link is worse than none.
- Images are removed. They live in each component's `images/` folder, which is
  not copied.

    python3 scripts/build-design-references.py

Re-run it after changing any file listed in SOURCES, or any component doc's
variants. It deletes and rewrites `skills/design/references/` whole.
"""

import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "skills" / "design" / "references"

# Each source, copied under its own filename.
SOURCES = [
    "specs/spec-rules-ai.md",
    "components/components-rules-ai.md",
    "tokens/color/color-rules-ai.md",
    "tokens/typography/typography-rules-ai.md",
    "tokens/spacing/spacing-rules-ai.md",
    "tokens/radius/radius-rules-ai.md",
    "tokens/shadow/shadow-rules-ai.md",
    "tokens/border-width/border-width-rules-ai.md",
    "icons/icons-rules-ai.md",
    "icons/icons-index.md",
    "components/components-ios-map.md",
    "tokens/tokens-ios-map.md",
    "icons/icons-ios-map.md",
]
VARIANTS_FILE = "component-variants.md"

# `color-rules-ai.md` picks the family; these pages pick the token inside it.
# Copied under their own names so the ruleset's links to them still resolve.
# Everything from `## Tokens` down is values and is left out.
COLOUR_FAMILY_PAGES = [
    "tokens/color/background.md",
    "tokens/color/surface.md",
    "tokens/color/border.md",
    "tokens/color/content.md",
    "tokens/color/scale.md",
]

FIGMA_MAP_FILE = "figma-map.md"
# Registry file, and the library tier it describes, for each component registry.
FIGMA_COMPONENT_REGISTRIES = [
    ("figma/figma-components-registry.json", "components"),
    ("figma/figma-patterns-registry.json", "patterns"),
    ("figma/figma-experiences-registry.json", "experiences"),
    ("figma/figma-foundations-components-registry.json", "foundations"),
]

IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")


def rewrite_links(text: str, copied: set[str]) -> str:
    """Point links at copies when they exist; otherwise keep only the text."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence:
            line = IMAGE.sub("", line)

            def fix(m: re.Match) -> str:
                label, target = m.group(1), m.group(2)
                name = target.split("#")[0].split("/")[-1]
                if target.startswith("#"):
                    return m.group(0)
                if name in copied:
                    anchor = target[len(target.split("#")[0]):]
                    return f"[{label}]({name}{anchor})"
                return label

            line = LINK.sub(fix, line)
        out.append(line)
    return "\n".join(out) + "\n"


def header(source: str) -> str:
    return (
        f"<!-- Generated from `{source}` on {date.today().isoformat()} by "
        "scripts/build-design-references.py. Never edit here: edit the source "
        "and re-run the script. -->\n\n"
    )


def usage_only(text: str) -> str:
    """A colour family page without its opening evidence note and its values."""
    text = re.split(r"^## Tokens\s*$", text, maxsplit=1, flags=re.M)[0]
    lines = text.splitlines()
    while lines and (lines[0].startswith(">") or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines).rstrip() + "\n"


def extract_variants() -> str:
    """One section per component: its H1 title, then its Variants & Modifiers."""
    parts = [
        "# Component variants\n\n"
        "Every component's **Variants & Modifiers** section, extracted from its "
        "own doc. A spec takes variant axes and values from here and nowhere "
        "else. Headings sit one level lower than in the source doc: an axis "
        "that is `###` there is `####` here.\n"
    ]
    for doc in sorted((ROOT / "components").glob("*/*.md")):
        if doc.stem != doc.parent.name:
            continue  # only the component's own doc, never its -figma.md
        text = doc.read_text()
        title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), doc.stem)
        m = re.search(r"^## Variants & Modifiers\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        body = m.group(1).strip() if m else "_This doc has no Variants & Modifiers section._"
        body = re.sub(r"^(#{3,5}) ", lambda h: h.group(1) + "# ", body, flags=re.M)
        parts.append(f"\n## {title}\n\n_From `{doc.relative_to(ROOT)}`._\n\n{body}\n")
    return "".join(parts)


def inventory_names() -> list[str]:
    """Every component name in `## The inventory` of components-rules-ai.md."""
    text = (ROOT / "components" / "components-rules-ai.md").read_text()
    m = re.search(r"^## The inventory\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return re.findall(r"^\| `([^`]+)`", m.group(1), re.M) if m else []


def cell(value) -> str:
    return f"`{value}`" if value else "—"


def figma_map() -> str:
    """One table per kind — components, tokens, icons — from the Figma registries."""
    tiers = json.loads((ROOT / "figma" / "figma-libraries-registry.json").read_text())["tiers"]
    parts = [
        "# Figma names and keys\n\n"
        "Joins each design-system name a spec uses to the Figma key that places "
        "it. Generated from the `figma/*.json` registries.\n\n"
        "**This file never decides which component or token to use.** "
        "`components-rules-ai.md` and the token rulesets decide that. This file "
        "only finds, in Figma, a name that was already chosen.\n\n"
        "**The spec keeps the design-system name.** A key or a node ID never "
        "appears in a spec.\n\n"
        "## Libraries\n\n"
        "| Tier | Figma library name |\n| --- | --- |\n"
    ]
    parts += [f"| {tier} | `{t['name']}` |\n" for tier, t in tiers.items()]

    parts.append(
        "\n## How to read a key\n\n"
        "| Kind | What the key is | How to import it |\n| --- | --- | --- |\n"
        "| Component with variants | The **component set** key | "
        "`figma.importComponentSetByKeyAsync(key)`, then pick the variant. "
        "If it throws *not found*, try `figma.importComponentByKeyAsync(key)` "
        "— the key is then a single component |\n"
        "| Icon | The **component set** key. **Proved 14 September 2026**: "
        "`importComponentByKeyAsync` throws *not found* on these keys | "
        "`figma.importComponentSetByKeyAsync(key)` |\n"
        "| Colour, spacing, radius, border width | A **variable** key | "
        "`figma.variables.importVariableByKeyAsync(key)`, then bind it |\n"
        "| Text style, shadow | A **style** key | `figma.importStyleByKeyAsync(key)` |\n"
    )

    known: set[str] = set()
    parts.append(
        "\n## Components\n\n"
        "**Pattern 2** means the component has an exposed inner slot. Set the "
        "slot's own properties on the nested instance, found by its main "
        "component key in **Exposed slots** — never through the parent's "
        "properties.\n\n"
        "| Name | Library | Key | Node ID | Pattern | Variants |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
    )
    slots = []
    for path, tier in FIGMA_COMPONENT_REGISTRIES:
        entries = json.loads((ROOT / path).read_text())["components"]
        for name, e in sorted(entries.items()):
            known.add(name)
            parts.append(
                f"| `{name}` | {tier} | {cell(e.get('key'))} | {cell(e.get('nodeId'))} "
                f"| {e.get('pattern', '—')} | {e.get('variantCount', '—')} |\n"
            )
            for s in e.get("exposedSubComponents", []):
                slots.append(
                    f"| `{name}` | {', '.join(f'`{x}`' for x in s.get('exposedAs', []))} "
                    f"| {cell(s.get('name'))} | {cell(s.get('key'))} |\n"
                )

    missing = [n for n in inventory_names() if n.split(" ⚠︎")[0] not in known]
    parts.append(
        "\n**Names in The inventory with no Figma key here:** "
        + (", ".join(f"`{n}`" for n in missing) if missing else "none")
        + ". Find one of these by name in its library, and report that it had "
        "no key.\n"
    )

    parts.append(
        "\n### Exposed slots\n\n"
        "| Parent | Exposed as | Nested component | Nested key |\n"
        "| --- | --- | --- | --- |\n" + "".join(slots)
    )

    tokens = json.loads((ROOT / "figma" / "figma-tokens-registry.json").read_text())
    parts.append(
        "\n## Tokens\n\n"
        "**A colour in a spec may omit the leading `Color/`.** `Content/Default/Default` "
        "in a spec is `Color/Content/Default/Default` here. Every other kind "
        "is written the same in both.\n\n"
        "**Never write a raw value where a token exists.** Bind the variable or "
        "apply the style, so a brand or theme switch still works.\n"
    )
    for kind, c in tokens["categories"].items():
        parts.append(
            f"\n### {kind}\n\n_Collection: `{c['collection']}`._\n\n"
            "| Figma name | Key |\n| --- | --- |\n"
        )
        parts += [f"| `{t['name']}` | `{t['key']}` |\n" for t in c["tokens"]]

    icons = json.loads((ROOT / "figma" / "figma-icons-registry.json").read_text())
    parts.append(
        "\n## Icons\n\n"
        "Every icon key is a component set key. Set `Filled`, `Circle` and "
        "`Square` only when the spec asks: all three default to `Off`.\n\n"
        "| Name | Category | Key |\n| --- | --- | --- |\n"
    )
    for category, c in icons["categories"].items():
        parts += [f"| `{i['name']}` | {category} | `{i['key']}` |\n" for i in c["icons"]]
    return "".join(parts)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    copied = {Path(s).name for s in SOURCES + COLOUR_FAMILY_PAGES} | {VARIANTS_FILE, FIGMA_MAP_FILE}

    for source in SOURCES:
        text = (ROOT / source).read_text()
        (OUT / Path(source).name).write_text(header(source) + rewrite_links(text, copied))

    for source in COLOUR_FAMILY_PAGES:
        note = (
            "_Which token to use inside this colour family. The value tables "
            "are left out: a spec never holds a raw value._\n\n"
        )
        text = usage_only((ROOT / source).read_text())
        (OUT / Path(source).name).write_text(header(source) + note + rewrite_links(text, copied))

    variants = rewrite_links(extract_variants(), copied)
    (OUT / VARIANTS_FILE).write_text(header("components/*/*.md") + variants)

    (OUT / FIGMA_MAP_FILE).write_text(header("figma/*.json") + figma_map())

    print(f"Wrote {len(SOURCES) + len(COLOUR_FAMILY_PAGES) + 2} files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
