<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832302192/Breadcrumb | Last modified: Aug 21, 2026 -->

# Breadcrumb

Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. They help users keep track of their location and allow them to navigate between pages.

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ (owned by Header/Footer team) | Ready ✅ | N/A — web only | N/A — web only |

![](images/s2zn6HK7lOC00HX1f3MQBw.png)

* [Breadcrumb on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7262)

---

## Usage

Breadcrumbs are a navigational aid that displays the user's current location within a hierarchy and allows them to trace their path back to previous sections. They help improve navigation by providing a clear trail of links, making it easier to understand the structure and move between different levels of content.

![](images/f6f41424415d817f97af08.png)

### Platform

Breadcrumbs are only used on the web. On iOS/Android, other navigation concepts are used, such as using the navigation bar or simply a back button.

### When to use

**Breadcrumb** — showing hierarchical location and allowing navigation up the hierarchy. **Web only**.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| The primary need is page title and actions | **Top bar** |
| Top-level global navigation | **Navigation bar** |

### Variant Selection Flow

```
Icon
├─ The icon leads the label → Icon left
├─ The icon trails the label → Icon right
└─ The crumb leaves the site → External-link icon
```

### Usage Guidance

| DO |
| --- |
| ![](images/d88b947b6ee723182fa156.png) **DO:** Use breadcrumbs when content is organized hierarchically or has deep navigation layers, to help users understand their location and easily backtrack through the structure. |
| ![](images/6d367f294855dc3c30210b.png) **DO:** Use breadcrumbs when users are likely to have landed on the page from external sources, such as search engines, to provide context and improve SEO. |

| DON'T |
| --- |
| **DON'T:** Don't rely on breadcrumbs as your primary navigation. Use the navigation bar (header) instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Breadcrumb** | — | Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. | — |
| [**Top bar**](../top-bar/top-bar.md) | High | Top bars display navigation elements, titles and actions such as buttons or icons at the top of the screen. | The primary need is page title and actions |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | Navigation bars provide quick access to key pages within the site, helping users to navigate efficiently. | Top-level global navigation |

---

## Variants & Modifiers

### Modifiers

#### Icons

Breadcrumb links are available with an icon to the left or right. External links should be marked with the external link icon.

| Icon left | Icon right | External link icon |
| --- | --- | --- |
| ![](images/32cb32741639724dda630f.png) | ![](images/82df68c65e8b2cc32b525f.png) | ![](images/1d4f82f14625b2335e32df.png) |

---

## Behavior & Responsiveness

### Interactive States & Loading

All links in the breadcrumbs have the states default, hover and pressed. We don't recommend disabling links, as this defeats their purpose of providing easy navigation through the site's structure.

| Default | Hover | Pressed |
| --- | --- | --- |
| ![](images/d4051d3ce591556df40d5a.png) | ![](images/22bdb53cd602e152f92e33.png) | ![](images/5973ef7001534731a2d4ba.png) |

Every link in the breadcrumb is clickable, except the current page.

![](images/81f37a17859c370f1c714b.png)

### Touch Target & Layout

If the path is too long, it is possible to hide links and replace them with an ellipsis to save space and maintain clarity. This can be done in two ways: hide links in the middle of the path, allowing users to see the start and end points, or hide links at the beginning, giving priority to the most recent navigation steps.

| No hidden links | Hidden links in the middle | Hidden links in the beginning |
| --- | --- | --- |
| ![](images/823e225146c5be93bfe942.png) | ![](images/3dc020d53db26f1e4f1a94.png) | ![](images/4f33067c47830d96158770.png) |

The default font size for the breadcrumbs is 16px. We recommend using the same size across the platform, but it can be adjusted if needed.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* Link texts should be clear and inciting. Our users should be able to anticipate where the links lead to.
* Use consistent language and terminology throughout the breadcrumbs to reinforce the structure of the site and help users become familiar with navigation patterns.
* Use short, concise phrases for each breadcrumb link to avoid overwhelming users. Aim for clarity and brevity to improve readability.
* For more information on content guidelines, please refer to the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
