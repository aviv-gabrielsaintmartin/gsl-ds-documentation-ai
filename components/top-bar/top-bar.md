<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832695405/Top+bar | Last modified: Aug 21, 2026 -->

# Top bar

Top bars display navigation elements, titles and actions such as buttons or icons at the top of the screen.

![](images/O-ifxQ8--9J3s4P5GVBDpQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Partially available ⚠️ |

* [Top bar on Figma](https://www.figma.com/design/TSd5D0j4WIVxZTGk0ZgfK7/3.-Gemini-Patterns-Library?node-id=9-7268)
* [Top bar on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-navigation-topbar--docs)

---

## Usage

Top bars are navigational elements positioned at the top of the screen that provide page-specific context and actions. They typically include a title, icons, and buttons relevant to the current page, ensuring that users can quickly access key functions without losing context.

### Platform

We use platform-specific top bars that differ between Web, iOS, and Android. They differ in appearance and height, but offer similar options and functionality. Only the badge is currently not available in web.

| Web | Android | iOS |
| --- | --- | --- |
| ![](images/9eecfe8d303ef9fa659665.png) | ![](images/000737b94866f1bbe4cb9a.png) | ![](images/b0fb2c1dfcce160bb2e6bc.png) |

### When to use

**Top bar** — page-specific title, context, and actions.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| Global site navigation | **Navigation bar** |

### Variant Selection Flow

```
Size
├─ Primary pages, or sections that need more presence → Medium
└─ Compact layouts and secondary pages with limited vertical space → Small

Style
├─ Plain background → Default
└─ Sitting over an image → On picture

Icons and actions
├─ Icons alone → With icons
└─ Icons plus a call to action → With icon and button

Title
├─ Small top bar → Keep the title, so users know where they are
├─ Medium top bar → The small title is optional
└─ On-picture variant → The title may be hidden

Badge
└─ Notifications or updates → Badge next to the title
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/5d21a6277d396ed9b267be.png) **DO:** Use the top bar to display page-specific titles, actions or navigation. | ![](images/7c918ad0eb52a2be640ebc.png) **DON'T:** Don't use the top bar for global navigation. Use the navigation bar instead. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Top bar** | — | The top bar provides contextual and screen-specific actions or secondary navigation within a specific page or screen. | — |
| [**Navigation bar**](../navigation-bar/navigation-bar.md) | High | The navigation bar provides global navigation throughout the site and access to key destinations. | Global site navigation |
| [**Breadcrumb**](../breadcrumb/breadcrumb.md) | Medium | Breadcrumbs are navigation elements that consist of a list of links arranged in a hierarchical order. | Breadcrumb redirects here when: The primary need is page title and actions |

---

## Variants & Modifiers

### Size

Top bars are available in small and medium sizes. The small variant is best for compact layouts or secondary pages where vertical space is limited. The medium variant is ideal for primary pages or sections where emphasizing the title is important for clarity and hierarchy.

| Small | Medium |
| --- | --- |
| ![](images/9eecfe8d303ef9fa659665.png) | ![](images/cfb92fa3e4b27d71507932.png) |

### Style

Top bars come in two styles: default and on picture. The default style works well on plain backgrounds, providing a clean and simple appearance. The on picture style is designed for use over images or visual elements, maintaining readability while blending seamlessly with the background.

| Default | On picture |
| --- | --- |
| ![](images/9eecfe8d303ef9fa659665.png) | ![](images/6fe6d8e0bf31bf6453c02e.png) |

| DO |
| --- |
| ![](images/388ddfc5049ef525fb986c.png) **DO:** Use the default variant on pages with a plain background. |
| ![](images/961d931a84078f6e123932.png) **DO:** Use the on picture variant on top of images. |

### Modifiers

#### Icons and actions

The top bar contains optional icons and an optional button.

| With icons | With icons | With icon and button | Without icon or button |
| --- | --- | --- | --- |
| ![](images/248023b8596ea6cb9ee95e.png) | ![](images/3395ba60dec7f90a348c57.png) | ![](images/7f274a76a132b912cdf7ad.png) | ![](images/71867d15b6c213821e02c1.png) |

#### Title

The small title in the medium top bar is optional. We don't recommend hiding the title in the small top bar, except for the on-picture variant, to help users understand their current location.

| With small title | Without small title |
| --- | --- |
| ![](images/e7fefa90374699803bc105.png) | ![](images/7f97177c7e8a32956206ec.png) |

#### Badge

A badge can be placed next to the title. They can be used to indicate notifications or updates. For example, for messages or alerts.

![](images/d45a8d1ae6c18e16a2126c.png)
![](images/f6c5b40b1149d824460566.png)

---

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

### Scrolling

On the web, consumers can choose whether the top bar stays fixed at the top or scrolls with the content. On iOS and Android, the top bar always stays on top.

| Fixed on top | Scrolls with content |
| --- | --- |
| ![](images/5656af62d63b9dac494e32.png) Web and app | ![](images/cd2094e4857b736dad4862.png) Web only |

### Touch Target & Layout

* **Width Adaptability:** The top bar is full-width, stretching across the width of the screen.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Sentence case without punctuation, for both titles and buttons.
* **Label Formula:** Buttons should always lead with an action verb in the infinitive tense, using the {verb} + {noun} formula, except for common actions like "Done," "Close," "Cancel," or "OK."
* **Length Limits:** Titles should be short and concise. Buttons should be under 4 words and/or 30 characters maximum in English.

For more information, see the [UX Writing principles](https://zeroheight.com/626199550/p/324518-intro).

---

## Accessibility (a11y)

Not documented
