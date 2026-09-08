<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2740060239/Accordion | Last modified: Aug 13, 2026 -->

# Accordion

Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of information in a compact space.

![](images/wkNTz-LmYzzZ9oU95EBrLQ.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Ready ✅ |

[Accordion on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?m=auto&node-id=11-136048&t=k234WjfNSw8D6uVC-1) · [Accordion on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-accordion--docs)

---

## Usage

Accordions are typically used when screen real estate is limited, and there's a need to manage the visibility of large amounts of content. They enhance the user experience by presenting information in a structured, efficient manner, allowing users to access details as needed without having to navigate away from the current context.

### When to use

* Use accordions to shorten pages by grouping related information together and reduce scrolling for non-crucial content, especially on mobile interfaces, enhances the user experience.

### When NOT to use

* Be aware that when you use an accordion, you are hiding content from users.
* Accordions should not be used to display essential information, as hiding content behind an accordion can reduce users' awareness of that information.

### Variant Selection Flow

```
Border
├─ Needs visual prominence, or the page has competing content → With border (white background)
└─ Page has a solid, neutral background and readability is fine → Without border (transparent)

Header icon
├─ The icon clarifies or complements the header text → With icon
└─ Otherwise → Without icon

Title size
├─ Web → 22px or 16px — pick one, never both at once
└─ iOS / Android → 16px only

Content
└─ Text, images and other components are all allowed
   └─ Never nest another accordion inside
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/n-GQVeFzTx0wd-mXHwMxDg.svg) **DO:** Use accordions to contain secondary or supporting content that is complementary. This reduces screen clutter and makes it easier to quickly scan through content. | ![](images/8d7vOTBrOZaKpN3uTKitug.svg) **DON'T:** Don't put blocking crucial content inside an accordion where users can't move forward without digging into an accordion. Important messages should not be hidden inside an accordion. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Accordion** | — | Accordions are container that allow users to expand and collapse sections of content, making it easier to manage large amounts of information in a… | — |
| [**Card**](../card/card.md) | High | Cards are flexible containers used to visually group content. | Content should always be visible |
| [**Tabs**](../tabs/tabs.md) | High | Tabs are used to organize related content into different views and allow users to seamlessly switch between them. | Sections are mutually exclusive views |
| **Text button** | Medium | A distinct component from Button, for when full button weight is too heavy. | Text button redirects here when: The content collapses back into a persistent expandable list |

---

## Variants & Modifiers

### Border

The accordion is available with or without a border. The bordered version has a white background whereas the unbordered version has a transparent background.

| With border | Without border |
| --- | --- |
| ![](images/a79c0e81967a73f855d4fd.png) Accordions with borders are used when the accordion needs to be visually prominent, especially on pages with colored or patterned backgrounds. The white background improves readability by providing a clear contrast to the surrounding content, making it easier for users to focus on the accordion's text. | ![](images/d2db3470279f73bb39b1d9.png) Accordions without borders are used on pages with a solid, neutral background, where readability isn't an issue. |

### Modifiers

#### Icons

Icons are used to highlight and complement the text in the accordion's header.

| With icon | Without icon |
| --- | --- |
| ![](images/958cdda489108ac8e0cd01.png) | ![](images/d12eb90c64775f510dcab9.png) |

#### Title, body and description text

Title, body, and description text are optional elements that can be toggled on/off depending on the use case. The size of the title depends on the platform.

| Web | iOS/Android |
| --- | --- |
| ![](images/b3a81368bf117a570bbfb4.png) On Web to title sizes (22px and 16px) are available. | ![](images/e1d611d3177b72ea4eb10b.png) On iOS/Android only the smaller title size (16px) is available. |

| DO | DON'T |
| --- | --- |
| ![](images/76535cc8de9a7d6620445f.png) **DO:** Use only one title size and combine it with body or description text. | ![](images/c457073a5f3c1be05fc77a.png) **DON'T:** Don't use both titles at the same time. |

#### Content

All types of content, such as text, images, and other components, can be placed inside the accordion.

| DO | DON'T |
| --- | --- |
| ![](images/6b5bf842dff679c8c780a1.png) **DO:** Use text, images or other component inside the accordion. | ![](images/f76b408f5c1bfec6cc3ee1.png) **DON'T:** Don't nest other accordions inside the accordion component. This makes it confusing and makes the content difficult to access. |

---

## Behavior & Responsiveness

### Interactive States & Loading

* **Default / Hover / Pressed:** Accordions have the states default, hovered, pressed, and disabled.
* **Interaction:** The accordion can be collapsed or expanded by clicking on the header of the accordion. The chevron icon at the end indicates the current state, pointing down when collapsed and up when expanded.

| Expanding | Collapsing |
| --- | --- |
| ![](images/a32e2941459d269a19e651.png) | ![](images/1f57e65d5430328ac9a99f.png) |

* By default, accordions start in a collapsed state with all content panels closed. Starting in a collapsed state gives the user a high-level view of the information available.
* There may be a scenario where it is necessary to have a single panel open by default, while keeping the rest of the panels closed is helpful to surface content. This can allow users to notice information immediately and encourage them to explore the content of other panels.
* Accordions should never collapse due to interactions with other accordions. If there are a number of accordions in the same group, and a user expands the first accordion and then a second without collapsing the first, both accordions should remain expanded. Automatically collapsing accordions based on interactions with other accordions degrades usability and risks confusing the user about their location on the page.

| DO | DON'T | CAUTION |
| --- | --- | --- |
| ![](images/dTi-tqG-98xYqRsWV98DqA.svg) **DO:** By default, all content panels are closed. | ![](images/vSiHyk15Ay7dHlzXHv1RFA.svg) **DON'T:** Avoid displaying all accordion panels expanded by default. This can increase the length of the page and make it difficult to find each panel. | ![](images/A9-qCazONUmuj_D4I4KHbA.svg) **CAUTION:** In a case where there is a set list view of accordion panels, the first panel is set to open by default. |

### Touch Target & Layout

* **Width Adaptability:** The accordion adjusts to the width of its container, filling the available space based on the size of the container.

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

* **Capitalization:** Use sentence-style capitalization - capitalize only the first word.
* **Header Length:** An accordion header should give an idea of the content in the accordion panel. Keep headers short. By default, header content wraps to the next line at smaller widths, and multiple lines of text can be difficult to scan.

---

## Accessibility (a11y)

Not documented
