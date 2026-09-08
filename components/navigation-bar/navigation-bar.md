<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832466011/Navigation+bar | Last modified: Aug 21, 2026 -->

# Navigation bar

Navigation bars provide quick access to key pages within the site, helping users to navigate efficiently.

![](images/qks62yjHepW5gBaS2cSk7g.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | N/A | N/A |

**Figma only** (owned by Header/Footer team). The figma component shows a future version that has not yet been developed.
* [Navigation bar (Web) on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7267)

---

## Usage

Navigation bars are located at the top of the site and provide global navigation and quick access to key pages. Clicking on an entry opens the menu.

### Platform

Web only. The Figma design is owned by the Header/Footer team and currently shows a future version of the component that has not yet been developed.

### When to use

**Navigation bar** — global navigation to top-level site destinations (web).

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Sub-pages and flows | **Top bar** |
| In-app navigation | **Navigation Bar (App), mobile only** |

### Variant Selection Flow

```
Number of entries
├─ Up to 7 → Standard
└─ More than 7 → Only when SEO requires it

Controls
├─ All brands → Button and icon buttons
└─ Immoweb only → Language menu

Reduced variant
└─ Funnels and other focused pages → Logo and language menu only
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/8367562cdc0d02a828549c.png) **DO:** Use the navigation bar for global web navigation. | ![](images/216a9c51965146647752e1.png) **DON'T:** Don't use the navigation bar to display page-specific titles or actions. Use the top bar instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Navigation bar** | — | The navigation bar provides global navigation throughout the site and access to key destinations. | — |
| [**Top bar**](../top-bar/top-bar.md) | High | The top bar provides contextual and screen-specific actions or secondary navigation within a specific page or screen. | Sub-pages and flows |
| [**Tabs**](../tabs/tabs.md) | Medium | Tabs are used to organize related content into different views and allow users to seamlessly switch between them. | Tabs redirects here when: Switching between top-level destinations |
| [**Breadcrumb**](../breadcrumb/breadcrumb.md) | Medium | Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. | Breadcrumb redirects here when: Top-level global navigation |

---

## Variants & Modifiers

### Modifiers

#### Entries and buttons

![](images/f63f4e714a528e99cf7eff.png)

The number of entries depends on the brand. We don't recommend using more than 7 entries unless it's necessary for SEO reasons.

The button and icon buttons are used on all brands, the language menu is currently only used on immoweb.

A reduced navigation bar with only the logo and the language menu can be used on pages such as funnels.

---

## Behavior & Responsiveness

### Opening menu

#### Desktop

Clicking on an entry in the navigation bar opens the mega menu on desktop. Leaving the menu with the pointer closes it.

![](images/05944b3108c53337d57917.png)
Opening menu: clicking an entry.

![](images/06c6d5eeaf6a3118a33187.png)
Closing menu: leaving the menu.

#### Phone and tablets

Tapping on the burger menu icon, opens the burger menu. Tapping on the x-button or tapping outside the menu, closes the burger menu.

![](images/4fc8786ec2c32ee6cdccab.png)
Opening menu: tapping the burger menu icon.

![](images/ad4a3996260cef65b474b0.png)
Closing menu: tapping the x-button.

![](images/835b9b896377e66cc03ca5.png)
Closing menu: tapping outside the menu.

### Icon tooltip

Hovering over the icon buttons will display a tooltip showing the label.

![](images/f9107e20d681eb301a3fac.png)
Favourites

![](images/b62d3ab0b005b5f831fb6a.png)
Account

### Language menu

The language menu opens a dropdown list from which the language can be selected.

![](images/be1c04ce72132af1f0c4d3.png)

### Arrows

Arrows are displayed to allow the user to navigate through the entries if not all entries can be displayed on smaller devices.

![](images/b74e842e9550e83404183f.png)

### Breakpoints & Platform Adaptations

The appearance of the navigation bar changes depending on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![](images/18da9907a09cf4c4afdb0e.png)
Web: XXS to XS (0 - 599 px)

![](images/48cfe54f461ae89d841c9f.png)
Web: SM (600 - 767 px)

![](images/e6eec3063c1e9c3d25d1ea.png)
Web: MD (768 - 1023 px)

![](images/bb8194739fdf3edde214fb.png)
Web: LG (1024 - 1279 px)

![](images/5ab43c96d41aacf531adb2.png)
Web: XL (1280 - 1535 px)

![](images/b6632c89df3184dea4bb9f.png)
Web: XXL (1536 - 1919 px)

![](images/37f27d8c08c3ce1332899b.png)
Web: XXXL (> 1920 px)

---

## Content & UX Writing

Use short and concise (1-3 words) labels for navigation entries. Start with a capital letter. Use consistent terminology and capitalization across all menu entries.

For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
