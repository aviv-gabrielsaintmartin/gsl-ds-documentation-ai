<!-- Generated from `components/components-ios-map.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

# Component names on iOS

_Joins each component name in [components-rules-ai.md](components-rules-ai.md)
to the SwiftUI name that builds it on iOS. Created 24 September 2026._

## What this file is for

A design agent writes a spec using the component names in
`components-rules-ai.md`. An iOS agent reads this file to find the SwiftUI name
for each one.

**This file never decides which component to use.** `components-rules-ai.md`
decides that. This file only translates a name that was already chosen.

**The spec keeps the neutral name.** An iOS name never appears in the spec, the
ruleset or a component doc.

## Where the iOS names come from

| Field | Value |
| --- | --- |
| Repository | `gsl-ios` |
| Branch and commit | `origin/develop`, commit `f488b6040a`, dated 24 September 2026 |
| Folder searched | `Packages/aviv_design_system_ios/Sources/`, the whole design-system package |
| Folder not searched | App code outside that package. A component built only inside one app is not in this file |
| How | `git grep` for every public `struct`, `class` and `ds…` view modifier, then each doc comment read where the pairing was not obvious |

**Read the remote branch, never a local working copy.** On 24 September 2026 the
local `gsl-ios` checkout was 21 design-system commits behind `origin/develop`.

## How to read the Confidence column

| Confidence | What it means | What was checked |
| --- | --- | --- |
| **proved** | The iOS name exists, and its folder name or its doc comment names the same component | The name was found in the package at the commit above. The folder or doc comment was read |
| **guessing** | The iOS name exists. The pairing is a judgement from its name and doc comment | Nobody on the iOS team has confirmed the pairing |
| **not found** | No iOS name was found for this component in the package | The package was searched at the commit above. **This does not prove the app lacks it** — app code was not searched |
| **not for iOS** | `components-rules-ai.md` already limits this component to web, or to desktop widths | The limit comes from the ruleset, not from the iOS code |

**An iOS name written as `.dsSomething(…)` is a view modifier**, attached to
another view. **Every other iOS name is a view**, placed on its own.

## Components library

| Component | iOS name | Confidence | Note |
| --- | --- | --- | --- |
| `Accordion` | `DSAccordion` | proved | |
| `Action Menu` | — | not for iOS | The ruleset limits it to SM breakpoint and above. On iOS, use `Modal Bottom Sheet Menu` |
| `Alert` | `.dsAlert(…)` | proved | `DSAlert` is the view the modifier presents |
| `Autocomplete` | — | not found | |
| `Avatar` | `DSAvatar` | proved | |
| `Badge` | `DSBadge` | proved | |
| `Badge Store` | — | not found | |
| `Button` | `DSButton` | proved | |
| `Button Bar` | `DSButtonBar`, or `.dsButtonBar(…)` | proved | |
| `Button Group` | `DSButtonGroup` | proved | |
| `Card` | `DSCard` | proved | |
| `Carousel` | — | not for iOS | The ruleset limits it to web |
| `Checkbox` | `DSCheckbox` | proved | |
| `Checkbox Group` | `DSCheckboxGroup` | proved | |
| `Chip` | `DSChip` | proved | |
| `Chip Group` | — | not found | No group type exists. Only the single `DSChip` was found |
| `Coachmark` | `.dsCoachMark(…)` | proved | |
| `Counter Field` | `DSIncrementalCounter` | proved | It sits in the folder `CounterField` |
| `Divider` | `DSDivider` | proved | |
| `Dropdown` | `DSDropdown` | proved | |
| `Energy Tag` | `DSEnergyTagList` | proved | Its doc comment: a horizontal list of `EnergyTagView`. A single tag is one item in that list |
| `Feedback Messages` | `DSFeedbackMessage` | proved | |
| `Feedback Thumb Buttons` | — | not for iOS | The ruleset limits it to web |
| `Floating Button Group` | `DSFloatingMenu` | guessing | Its doc comment shows a menu icon that opens icon actions. It may be a different component |
| `Image Slider` | `DSImageSlider` | proved | |
| `Link` | `DSLink`, or `DSLinkText` for a link inside running text | proved | |
| `Loading State` | `DSLoader` | guessing | Its doc comment: a circular progress view with an optional title and subtitle. `DSContentPlaceholder(isLoading: true)` is the other candidate |
| `Modal Bottom Sheet` | `.dsSheet(…)` | proved | It sits in the folder `BottomSheet` |
| `Modal Bottom Sheet Menu` | `.dsSheet(isPresented:menuItems:onDismiss:onTapItem:)` | proved | The doc comment of `DSMenu` names this modifier as the pre-built bottom sheet that uses it |
| `Navigation Bar (App)` | `DSTabView`, with `.dsTabItem(…)` on each destination | guessing | It configures the system tab bar. No doc comment names it |
| `Pagination` | — | not for iOS | The ruleset limits it to web |
| `Pop-up` | `.dsPopup(…)` | proved | Its doc comment: `DSPopupContentView` is the style `.dsPopup(…)` uses. Prefer the modifier |
| `Progress Bar` | `DSProgressBar` | proved | |
| `Progress Circle` | `DSProgressCircle` | proved | |
| `Radio Button Group` | `DSRadioGroup` | proved | `DSRadioButton` is one option inside it |
| `Rating` | `DSRatingView` | proved | |
| `Score Tag` | — | not found | The only `Score` in the package is a colour token group, not a component |
| `Segmented Control` | `DSSegmentedControl` | proved | |
| `Select Card Group` | `DSSelectCardGroup` | proved | `DSSelectCard` is one option inside it |
| `Slider` | `DSSingleSlider` | proved for a single value | **A range between two values was not found.** A spec asking for a range has no iOS name |
| `Snackbar` | `.dsSnackbar(…)` | proved | |
| `State Message` | `DSStateMessage` | proved | |
| `Tabs` | `DSTabs` | proved | |
| `Tag` | `DSTag`, or `DSTagList` for several | proved | |
| `Text Area` | `DSTextArea` | proved | |
| `Text Button` | `DSTextButton` | proved | |
| `Text Field` | `DSTextField` | proved | `DSPasswordTextField` and `DSFormattedTextField` also exist. Use them for a password or a formatted value |
| `Toggle` | `DSSwitch` | proved | It sits in the folder `Toggles` |
| `Toggle Group` | `DSSwitchGroup` | proved | It sits in the folder `Toggles` |
| `Tooltip` | `.dsTooltip(…)` | proved | |

## Patterns library

| Component | iOS name | Confidence | Note |
| --- | --- | --- | --- |
| `Bar graph` | — | not found | |
| `Breadcrumb` | — | not for iOS | The ruleset limits it to web |
| `Burger menu` | — | not found | |
| `Date Field` | `DSDateField` | proved | |
| `Date Picker` | `DSCalendarDatePicker` | guessing | Paired by name. It sits in `TechnicalComponents`, not beside the other components |
| `Donut chart` | — | not found | |
| `Feedback Bar` | — | not found | |
| `Filter bar` | — | not found | |
| `Info State` | `DSInfoState` | proved | |
| `KPI` | — | not found | |
| `Line chart` | `DSLineChart` | proved | |
| `Media Upload` | — | not found | |
| `Mega menus` | — | not found | |
| `Navigation bar` | — | not for iOS | The ruleset says this one is web. On iOS, use `Navigation Bar (App)` |
| `Top Bar` | `.dsNavigationBar(…)`, inside `DSNavigationView` | guessing | Paired by what it does: a title and actions at the top of the screen |
| `Wizard` | — | not found | |

## Experiences library

| Component | iOS name | Confidence | Note |
| --- | --- | --- | --- |
| `Estimation card` | — | not found | |
| `Floor selection` | — | not found | |
| `Listing Card` | `DSListingCard` | proved | |
| `Listing summary` | `DSListingSummary` | proved | |
| `Map template` | — | not found | Parts exist: `MapPinView`, `MapLayerButton`, `.dsMapLayerSheet(…)`. No whole template was found |
| `Phone Number Field` | — | not found | Only its tokens, `PhoneNumberDesignTokens`, were found. No view was found |
| `Table` | — | not found | |

## Never select, with an iOS name

`components-rules-ai.md` marks every component below as never select. It allows
two of them inside a container, so their iOS names are recorded here.

| Component | iOS name | Confidence | When it may appear |
| --- | --- | --- | --- |
| `Cell Content` | `DSCellContent` | proved | Only as a row inside a container, as `components-rules-ai.md` says |
| `Content Placeholder` | `DSContentPlaceholder` | proved | Only inside its parent, as `components-rules-ai.md` says |

Every other never-select component in the inventory has no entry here. None of
them is ever placed, so none needs an iOS name.

## In the iOS package, with no name in the inventory

These exist on iOS and have no name in `components-rules-ai.md`. **No rule
covers them. Whether a spec may use them is not decided.** They are listed so
an agent does not rebuild one by hand without knowing it exists.

| iOS name | What its doc comment or name says |
| --- | --- |
| `DSVStack`, `DSHStack`, `DSSpacer` | Layout containers with design-system spacing |
| `DSIconButton` | An icon-only button |
| `DSCloseButton`, `DSFavoriteButton`, `DSShareButton`, `DSReloadButton`, `DSRemoveButton`, `DSCopyPasteboardButton`, `DSLocationButton` | Buttons with one fixed purpose each |
| `DSGauge` | A sliding selector that picks one of several values |
| `DSHighlightCard` | A card with an illustration, a title, a subtitle and a description |
| `DSServiceCard`, `DSLocationCard`, `DSPreviewListingCard` | Cards with one fixed purpose each |
| `DSPriceComparisonView` | Named for a price comparison. Doc comment not read |
| `DSGalleryView`, `DSZoomableImage` | Image gallery and zoomable image |
| `DSEmptyListView` | An empty list |
| `DSRichText`, `DSMarkdownText` | Formatted running text |
| `DSCodeView` | Named for a code entry. Doc comment not read |
| `.dsPopover(…)`, `.dsToolbar(…)`, `.dsOverlay(…)` | View modifiers |

## Counts

Counted by script on 24 September 2026. The same script proved that every
selectable name in the inventory of `components-rules-ai.md` has exactly one
row above, and that no row names something outside it.

| Group | Count |
| --- | --- |
| Selectable components mapped above | 73 |
| proved | 44 |
| guessing | 5 |
| not found | 18 |
| not for iOS | 6 |
