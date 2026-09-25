<!-- Generated from `icons/icons-ios-map.md` on 2026-09-25 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

# Icon names on iOS

_Joins each icon name in [icons-index.md](icons-index.md) to the SwiftUI path
that draws it on iOS. Created 25 September 2026._

## What this file is for

A design agent writes a spec using the icon names in `icons-index.md`. An iOS
agent reads this file to find the SwiftUI path for each one.

**This file never decides which icon to use.** [icons-rules-ai.md](icons-rules-ai.md)
decides that. This file only translates a name that was already chosen.

**The spec keeps the neutral name.** An iOS path never appears in the spec, the
ruleset or the index.

**Most names follow one rule.** This file states the rule, then lists every name
the rule gets wrong. A name that is not in any table below follows the rule.

## Where the iOS names come from

| Field | Value |
| --- | --- |
| Repository | `gsl-ios` |
| Branch and commit | `origin/develop`, commit `ccb15356ed`, dated 25 September 2026 |
| Files read | `Packages/aviv_design_system_ios/Sources/DesignSystem/Foundation/Icons/IconsDescription/`, every file. Each property was followed to the image asset it draws |
| Files not read | App code outside the design-system package |
| How | A script listed every public property in each category file, and the asset name it points at. Each asset name was turned back into an index name and compared. The mismatches in *Paths the rule gets wrong* were then read by hand in the source |

**Read the remote branch, never a local working copy.** The local checkout can be
behind `origin/develop`.

**Measured on 25 September 2026:** iOS exposes **401 icon properties**. The rule
below gives the right path for **374** of them. The other 27 are listed in this
file. **58 index names have no iOS path at all.**

## The rule

```
\.<category>.<name>[.<shape>].<fill>
```

| Part | How to write it | Example |
| --- | --- | --- |
| `<category>` | The index category, in lowerCamelCase, with `&` dropped. **Two differ** — see *Categories* | `Nature & Food` → `natureAndFood` |
| `<name>` | The index name, in lowerCamelCase. Split on each hyphen and each space | `magnifying-glass` → `magnifyingGlass` |
| `<shape>` | Only when the icon has `Circle`, `Square` or `Triangle` in the index. `.default` for the plain shape, `.circle`, `.square` or `.triangle` otherwise | `info` in a square → `.square` |
| `<fill>` | `.unfilled` for `Filled` = `Off`. `.filled` for `Filled` = `On` | |

**Proved** from app code on the same commit: `\.actionAndSettings.gear.unfilled`,
`\.actionAndSettings.magnifyingGlass.filled`,
`\.alertAndFeedback.info.square.unfilled`,
`\.alertAndFeedback.star.default.unfilled`.

**Some parts have no fill choice.** When an icon has only one drawing on iOS, its
path stops without `.filled` or `.unfilled`. 108 of the 401 properties are like
this — `\.natureAndFood.snowflake` is one. The same can happen to one shape of an
icon: `\.brands.facebook.circle` has no fill. **Build the path, and drop `<fill>`
when the Swift type is `Image`.** An iOS agent reads the type from
`IconsDescription+<Category>.swift`.

## Categories

| Index category | iOS category |
| --- | --- |
| `Map` | `maps` |
| `Navigation & Menu` | `menuAndNavigation` |
| Every other index category | The rule: lowerCamelCase, `&` dropped |

**iOS has one category the index does not have:** `others`, holding `ellipse`
and `language`.

**Fifteen icons sit in a different category on iOS.** The path uses the iOS
category:

| Index name | Index category | iOS path, before `<shape>` and `<fill>` |
| --- | --- | --- |
| `cc-amazon-pay` · `cc-amex` · `cc-apple-pay` · `cc-diners-club` · `cc-discover` · `cc-jcb` · `cc-mastercard` · `cc-paypal` · `cc-stripe` · `cc-visa` | Brands | `\.documentAndContent.<name>` — for example `\.documentAndContent.ccVisa` |
| `charging-station` | Transportation | `\.furnitures.chargingStation` |
| `garage-car` | Place & Property | `\.furnitures.garageCar` |
| `stairs` | Place & Property | `\.home.stairs` |
| `pen` | Editor | `\.lifestyle.pen` — see *Paths the rule gets wrong* |
| `ellipse` | Action & Settings | `\.others.ellipse` |

## Paths the rule gets wrong

### The name is spelled differently

| Index name | iOS path, before `<shape>` and `<fill>` | Why |
| --- | --- | --- |
| `maginifying-glass-spark` | `\.actionAndSettings.magnifyingGlassSpark` | iOS fixed the typo. The index keeps it |
| `alert-on` | `\.alertAndFeedback.alert` | iOS drops `-on` |
| `wifi-slash` | `\.deviceAndCommunication.wifiSplash` | iOS misspells it `Splash` |
| `location-Xmark` | `\.maps.locationXMark` | Capital `M` on iOS |
| `plot-space` | `\.placeAndProperty.plotspace` | No capital `S` on iOS |
| `face-sunglasses-light` | `\.usersAndPeople.faceSunglasses` | iOS drops `-light` |
| `face-grin-hearts-light` | `\.usersAndPeople.faceGrinHearts` | iOS drops `-light` |
| `language` | `\.others.language` | In `others` on iOS, not `editor` |
| `apple`, the company, in Brands | `\.brands.apple` | The fruit is `\.natureAndFood.apple`, by the rule |

### The shape is written differently

| Index name | iOS path | Why |
| --- | --- | --- |
| `star` with `Half` = `On` | `\.alertAndFeedback.starHalf` | A separate property on iOS, with no fill choice |
| `star`, every other variant | `\.alertAndFeedback.star.<shape>.<fill>` | By the rule. Listed because the iOS assets carry no `star` in their name |
| `facebook` · `google-plus` · `pinterest` | `\.brands.<name>.default`, `.circle` or `.square` | No fill choice on any shape |
| `instagram` · `linkedin` · `twitter` · `whatsapp` · `xing` · `youtube` | `\.brands.<name>.default` or `.square` | No fill choice. These six have a `Square` shape on iOS that the index does not list |
| `share` | `\.actionAndSettings.share` | **Not the index's `share` glyph.** It draws an asset named `share-platform-i-os`, which is the iOS share symbol. **Guessing** it is the right one to use on iOS. Nobody has compared the two drawings |

### The path draws a different icon

**These paths exist but draw the wrong picture.** Proved by reading each line of
the source on the commit above. An iOS agent that follows the rule for these
names builds a screen with the wrong icon, and nothing fails.

| Index name | iOS path the rule gives | What it actually draws |
| --- | --- | --- |
| `location-arrow` | `\.maps.locationArrow` | `user` |
| `grip-dots-vertical` | `\.menuAndNavigation.gripDotsVertical` | `grid` |
| `bicycle` | `\.transportation.bicycle` | `route` |
| `biking` | `\.transportation.biking` | `route` |
| `pen`, filled | `\.lifestyle.pen.filled` | `pen-line`, filled. The unfilled one is `pen` |

**Treat these five as having no iOS path.** `pen` unfilled is the exception: it
draws `pen`.

### iOS names with no index name

| iOS path | What it draws |
| --- | --- |
| `\.alertAndFeedback.security` | `alert-on` — the same drawing as `\.alertAndFeedback.alert` |
| `\.maps.mapBackground` | An asset named `map-background`. It is not in the index |

**Never place either from a spec.** Neither is a name the spec can hold.

## Index names with no iOS path

**58 names.** The package has no public property for any of them. Some exist as
image assets inside the package but are not exposed — `shower` and `agency` are
two. An app outside the package cannot reach an unexposed asset. **Guessing**
from the Swift access level; not tested by building.

| Index category | Names |
| --- | --- |
| Action & Settings | `radio-button` · `resize` |
| Alert & Feedback | `double-check` · `light-bulb` |
| Brands | `google-play-store` · `tiktok` |
| Navigation & Menu | `double-chevron-up-down` |
| Users & People | `assistance` · `user-minus` |
| Map | `location-slash` · `map-compass` · `map-france` · `two-dimensional` |
| Transportation | `drone` · `gas-station` · `RER-paris` |
| Device & Communication | `scanner` · `virtual-staging` |
| Editor | `camera-professional` · `image ai` · `smart edit` · `smart fill` · `smart search` · `two-three-dimensional-draw` |
| Document & Content | `file-cdd` · `file-cdi` · `no-file` · `paper-clip` · `paper-clip-vertical` · `three-dimensional-view` · `unarchive` |
| Finance | `zero-percent` |
| Nature & Food | `lake-view` · `sea-view` · `tractor-tree` |
| Lifestyle | `medal` · `plate-cutlery` · `towel` |
| Furnitures | `dishwasher` · `shower` · `unfurnished` |
| Place & Property | `basement` · `bidet` · `cellar` · `duplex-car` · `house-staging` · `load-dock` · `pantry` · `property-insurance` · `RDC` · `underground-car` · `urinal` |
| Real Estate | `agency` · `house-insurance` · `house-key` · `house-search` · `square-meter` · `three-six-zero-view` |

**Add the five paths that draw a different icon**, in the table above, to this
list. They have no correct iOS path either.
