A navigation bar (app) is the persistent row of tabs moving a user between an app's top-level destinations.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Not applicable — never on web | Not established 🚧 | Not established 🚧 |

---

## Usage

The navigation bar sits at the foot of an app screen and stays there. It holds
three, four or five tabs. Each tab is one top-level destination, and exactly one
is active at a time.

It is **not** the web navigation bar. They are two different components with
similar names — see *When NOT to use*.

**It is placeable in Figma and will never ship on web.** A design agent working
in Figma may select it for an app screen. A web generating agent may not, because
there is nothing on web to generate. Gabriel, 21 September 2026.

### Platform

**iOS and Android only.** The component's own `Platform` property offers those
two and nothing else, and the three platform behaviours below differ enough that
choosing the wrong one produces a visibly wrong screen.

| | iOS | Android |
| --- | --- | --- |
| **Bar height** | **49 tall**, or **83 with the home indicator** | **80 tall**, always |
| **Home indicator** | Available, and adds a 34-tall strip below the tabs | **Not available** — Android draws no home indicator |
| **Label position, phone** | Below the icon | Below the icon |
| **Label position, tablet** | **Beside the icon** | Below the icon |
| **Tablet tab width** | Tabs stretch to fill the bar | **Tabs cap at 168** and do not stretch |

_Read live from the Figma component set, 21 September 2026. The Android tablet
cap is why a three-tab Android tablet bar does not fill its width, and a
three-tab iOS tablet bar does._

_**Every number on this page is a measurement in the platform's own unit** —
points on iOS, density-independent pixels on Android. They are not a shared
pixel, and 49 on iOS is not 49 on Android._

### When to use

* **Navigation Bar (App)** — moving between an app's top-level destinations.
* The destinations must stay reachable from every screen in the app.
* There are three, four or five of them.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The screen is on the web rather than in an app | **Navigation bar** |
| The user moves between views of the same content, not between destinations | **Tabs** |
| The bar carries the title and actions of one screen rather than global navigation | **Top bar** |
| The list is contextual actions rather than navigation | **Action menu** |

### Variant Selection Flow

```
1. Which platform is the screen?
   ├── iOS ─────> Platform=iOS
   └── Android ─> Platform=Android

2. Which device?
   ├── Phone ──> Device=Phone
   └── Tablet ─> Device=Tablet
       └── On iOS the label moves beside the icon. On Android it stays below

3. How many top-level destinations?
   └── Tabs = 3, 4 or 5. There is no other option, and no overflow behaviour

4. Does the screen show the home indicator?
   ├── Android ─> not offered. Skip this step
   └── iOS ─────> Home Indicator = true adds a 34-tall strip below the tabs
                   Set it to match the device frame you are drawing on

Per tab, set separately on the exposed tab, not on the bar:
   State   = Active on exactly one tab, Inactive on the rest
   Badge   = true only where the destination has something to report
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Mark exactly one tab active. | **DON'T:** Leave every tab inactive, or mark two. The bar's whole job is saying where the user is. |
| **DO:** Keep the tab count between three and five. | **DON'T:** Design a sixth destination into the bar. There is no overflow variant. |
| **DO:** Match the home indicator to the device frame. | **DON'T:** Set it on an Android screen. Android does not draw one, and the property is not offered there. |
| **DO:** Give every tab a label. | **DON'T:** Ship icon-only tabs. The label is part of the tab, and the icon alone is not a name. |

_Illustrations not yet drawn._

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Navigation Bar (App)** | — | Persistent in-app navigation between top-level destinations. | Search, Favourites, Messages, Profile |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | The **web** equivalent — global navigation to top-level site destinations. A different component with a similar name. | The header on a desktop site |
| [**Tabs**](../tabs/tabs.md) | High | Switching between views of the same content, inside one screen. | "For sale" and "To rent" over one results list |
| [**Top bar**](../top-bar/top-bar.md) | Medium | One screen's title and its actions, rather than global navigation. | A back arrow and a share button |
| [**Badge**](../badge/badge.md) | Low | The marker a tab carries when its destination has something to report. | An unread count on Messages |

## Variants & Modifiers

### Platform and device

#### Platform, Device, Tabs, Home Indicator

Four properties on the bar, giving **18 variants**.

| Property | Options | Default |
| --- | --- | --- |
| **Platform** | `Android`, `iOS` | `Android` |
| **Device** | `Phone`, `Tablet` | `Phone` |
| **Tabs** | `3`, `4`, `5` | `3` |
| **Home Indicator** | `true`, `false` | `false` |

**18, not 24, and the gap is deliberate.** `Platform=Android` never carries
`Home Indicator=true`, because the home indicator is an iOS element. Gabriel,
21 September 2026.

### Modifiers

#### The tab

Each tab is an exposed instance of a shared base component. **Its properties are
set on the tab, not on the bar** — the bar's own properties do not reach them.

| Tab property | Options | What it does |
| --- | --- | --- |
| **State** | `Active`, `Inactive` | Which destination the user is on |
| **Badge** | `true`, `false` | Shows a badge on the tab's icon |
| **Platform** | `Android`, `iOS` | Follows the bar's platform |
| **Label Position** | `Below`, `Side` | Follows the platform and device |

A tab is a 24 icon above or beside a label, with an optional 16 badge on the
icon. Its internal spacing is 4 between icon and label, with 12 above and 16
below.

## Behavior & Responsiveness

### Interactive States & Loading

* **Active / Inactive:** set per tab through the tab's own `State` property.
  Exactly one tab is active.
* **Hover / Pressed / Focus / Disabled:** Not documented. The component set
  carries no such states, and no app implementation was read.
* **Loading:** Not documented. The bar has no loading state.

### Touch Target & Layout

* **Touch Target:** the full tab is the target. On a phone the shortest tab is
  72 wide by 49 tall on iOS, and 72 wide by 80 tall on Android.
* **Width Adaptability:** the bar is full-width. Tabs divide that width equally
  on phone, on both platforms.
* **Tablet side padding:** 32 on each side, on both platforms.
* **Tablet tab width:** stretches to fill on iOS; **capped at 168 on Android**,
  so a three- or four-tab Android tablet bar leaves space at the edges.

### Breakpoints & Platform Adaptations

| Platform / Device | Layout & Width Behaviour |
| --- | --- |
| **iOS, phone** | 360 × 49. No side padding. Label below the icon |
| **iOS, phone, home indicator** | 360 × 83 — 49 of tabs plus a 34 indicator strip |
| **iOS, tablet** | 768 × 49. 32 side padding. **Label beside the icon.** Tabs stretch |
| **iOS, tablet, home indicator** | 768 × 83, same split as the phone |
| **Android, phone** | 360 × 80. No side padding. Label below the icon |
| **Android, tablet** | 768 × 80. 32 side padding. Label below the icon. **Tabs capped at 168** |

## Content & UX Writing

* **Capitalization:** Not documented
* **Label Formula:** Not documented. Each label names a destination, not an
  action.
* **Length Limits:** No count is stated. A phone tab is as narrow as 72 at five
  tabs, which is the practical limit on the label.

### Every tab is labelled

The label is part of the tab and is not optional in the component. An icon on
its own does not name a destination.

## Accessibility (a11y)

* **Screen Readers:** Not documented. No app implementation was read, and the
  Figma component carries no accessibility data.
* **Keyboard Navigation:** not applicable in the usual sense — this is an app
  component, not a web one.
* **Touch target size:** the shortest tab is 72 wide by 49 tall on iOS, and 72
  by 80 on Android. Both clear the 44-to-48 minimum the two platforms publish.
  **Not verified against either platform's own guidance** — the numbers are
  measured from the Figma component, and the comparison is mine.
* **Colour alone:** the active tab is distinguished by the tab's `State`
  property. **What that changes visually was not read**, so whether colour is
  the only signal is **not established**.
