<!-- Generated from `components/*/*.md` on 2026-09-24 by scripts/build-design-references.py. Never edit here: edit the source and re-run the script. -->

# Component variants

Every component's **Variants & Modifiers** section, extracted from its own doc. A spec takes variant axes and values from here and nowhere else. Headings sit one level lower than in the source doc: an axis that is `###` there is `####` here.

## accordion

_From `components/accordion/accordion.md`._

#### Border

The accordion is available with or without a border. The bordered version has a white background whereas the unbordered version has a transparent background.

| With border | Without border |
| --- | --- |
|  Accordions with borders are used when the accordion needs to be visually prominent, especially on pages with colored or patterned backgrounds. The white background improves readability by providing a clear contrast to the surrounding content, making it easier for users to focus on the accordion's text. |  Accordions without borders are used on pages with a solid, neutral background, where readability isn't an issue. |

#### Modifiers

##### Icons

Icons are used to highlight and complement the text in the accordion's header.

| With icon | Without icon |
| --- | --- |
|  |  |

##### Title, body and description text

Title, body, and description text are optional elements that can be toggled on/off depending on the use case. The size of the title depends on the platform.

| Web | iOS/Android |
| --- | --- |
|  On Web to title sizes (22px and 16px) are available. |  On iOS/Android only the smaller title size (16px) is available. |

| DO | DON'T |
| --- | --- |
|  **DO:** Use only one title size and combine it with body or description text. |  **DON'T:** Don't use both titles at the same time. |

##### Content

All types of content, such as text, images, and other components, can be placed inside the accordion.

| DO | DON'T |
| --- | --- |
|  **DO:** Use text, images or other component inside the accordion. |  **DON'T:** Don't nest other accordions inside the accordion component. This makes it confusing and makes the content difficult to access. |

---

## action-menu

_From `components/action-menu/action-menu.md`._

#### Modifiers

##### Trigger

The action menu can be opened with the following button types: tertiary icon button, floating icon button and text button.

If you use a different trigger, please share your use case with us so we can improve our guidelines and documentation.

| Tertiary icon button | Floating icon button | Text button |
| --- | --- | --- |
|  Use icon buttons when space is limited or the action is commonly recognized, such as the three-dot menu icon. |  Use a floating icon button when the action menu is on top of an image or map. |  Use a text button when the action needs to be explicitly clear, especially for less common or more complex tasks. Use it to filter pages. |

| Tertiary icon button | Floating icon button | Text button |
| --- | --- | --- |
|  |  |  |

##### Icons

Icons can be added to the dropdown list. They act as visual cues to provide clarity to the user. On Web/Android the default icons are on the left and the external link icon on the right. On iOS all icons are on the right.

| DO | DON'T |
| --- | --- |
|  **DO:** If some items don't have an icon, remove all icons. |  **DON'T:** Don't mix menu items with and without icons, as it reduces readability. |

| Web/Android | iOS |
| --- | --- |
|  |  |

##### Menu items

Menu items can be actions or links. If the menu item is a link, the external link icon is displayed.

| DO | DON'T |
| --- | --- |
|  **DO:** Links are marked with the external link icon. |  **DON'T:** Don't hide the link icon, as it can be misleading to the user. |

---

## alert

_From `components/alert/alert.md`._

#### Modifiers

##### Icon/Illustration

Alerts can be used with an icon, a spot illustration, or neither. You can't use them with an icon and an illustration at the same time.

| Icon | Illustration | No icon/illustration |
| --- | --- | --- |
|  |  |  |


##### Title and description

Titles are optional, but recommended for clarity. Descriptions are optional and are used when additional context or detail is needed.

| With title and description | Without description | Without title |
| --- | --- | --- |
|  |  |  |

##### Buttons

Alerts can be used with one to three buttons. If two buttons are used, we recommend combining the primary and tertiary buttons.

| 1 button | 2 buttons | 3 buttons |
| --- | --- | --- |
|  |  |  |

---

## autocomplete

_From `components/autocomplete/autocomplete.md`._

#### Modifiers

##### Dropdown list

The dropdown list consists of a mandatory label and an optional caption on the right. The number of displayed rows is defined by the consumer, with no fixed limit. The list rows are available in small and large heights.

| Small rows | Large rows |
| --- | --- |
|  |  |

The dropdown list includes an optional text button. The button is positioned at the end of the list.



| DO |
| --- |
|  **DO:** Use the button for geolocation tracking. |
|  **DO:** Use the button to help users when they can't find the result they expect. |

The dropdown list also includes optional icons on the left and right.



##### Text field

The autocomplete contains a text field. See the text field documentation to learn more about the modifiers of this component.

##### Modal

On iOS/Android tablets, the autocomplete appears in a modal. See the modal bottom sheet documentation to learn more about this component's modifiers.

##### Top bar

The autocomplete on phones contains a top bar. See the top bar documentation to learn more about the modifiers of this component.

---

## avatar

_From `components/avatar/avatar.md`._

#### Shapes and sizes

The avatar is available as a circle or square in sizes between 24 and 128px.

##### Circle

| 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 104 | 128 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

##### Square

| 24 | 32 | 40 | 48 | 56 | 64 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

| 72 | 80 | 104 | 128 |
| --- | --- | --- | --- |
|  |  |  |  |

##### Rectangular, flexible

| Rectangular without stroke | Rectangular with padding and stroke | Rectangular with stroke |
| --- | --- | --- |
|  |  |  |

| DO | DON'T |
| --- | --- |
|  **DO:** Use the avatar in one of the available sizes and shapes. |  **DON'T:** Don't scale or change the shape of the avatar. |

| DO |
| --- |
|  **DO:** Use the circle for individuals such as agents, seekers, and private owners. Use the square for agencies. |

#### No padding

All avatar sizes are available with and without padding.

| With padding | Without padding |
| --- | --- |
|  |  |

#### No border

All avatar sizes are available with and without border.

| With border | Without border | With border | Without border |
| --- | --- | --- | --- |
|  |  |  |  |

#### Icons and initials

Icons or initials can be used as a fallback if no image or logo is available.

| DO | DON'T |
| --- | --- |
|  **DO:** If an image is not available, use icons or initials. We recommend using the building icons for agencies and the user icon or initials for individuals such as agents, private sellers, or seekers. |  **DON'T:** Don't use any other illustrations or emojis. |

| Icon | Initials |
| --- | --- |
|  |  |

#### Rectangular, adaptive avatar

This Avatar variant's goal is to, within certain limits, adapt to the logo ratio of AVIV Intermediary agents. That way the agent's logo can be better represented within the AVIV platform without size or ratio constraint limitations.

##### Specs

The avatar size and ratio adapts to the user's choice of image (in this case, logo). However, to ensure a stable experience, we've introduced a set of maximum and minimum width and height — depending on the logo ratio, if either the width or the height hits the maximum or minimum, it will stay at that size.



Max. and min. sizes



Examples with real logos



**DON'T:** Rectangular avatars don't have icons or initials fallback.

---

#### Modifiers

Not documented

## badge

_From `components/badge/badge.md`._

#### Size

##### 16 and 24

Two sizes, `16` and `24`, being the badge's height in pixels. Default `24`.
Minimum width equals the height, so a single-character badge renders as a
circle. No rule for choosing between them is documented.

#### Colour variant

##### Primary and secondary

Two variant names, each with its own set of background behaviours:

| Variant | Background behaviours |
| --- | --- |
| **Primary** | `default`, `inverted` |
| **Secondary** | `default`, `inverted`, `constant`, `onPrimary`, `onSecondary` |

Each combination sets a background, a content colour and a border colour, and
carries its own disabled trio. Default is `primary` with the `default`
background behaviour.

#### Modifiers

Not documented

_The size and colour axes above are the whole of what a badge can be set to,
beyond the disabled state described below._

## badge-store

_From `components/badge-store/badge-store.md`._

**Four axes, 24 variants.** `Type`, `Platform`, `Theme` and `Language`.

#### Store

##### App Store, Google Play

**Which store the badge points at.** Two options, and they are not
interchangeable — each is that company's own badge. The axis is named
`Platform`, and it means the app store, never the build platform.

| Store | Width | Height |
| --- | --- | --- |
| **App Store** | 120, and **126 in French** | 40 |
| **Google Play** | 135 | 40 |

_The French App Store badge is wider because its wording is longer. Nothing
else changes size._

#### Type

##### Filled, Outline

**Two drawings of the same badge**, differing in weight.

| Type | What it is | Colour |
| --- | --- | --- |
| **Filled** | The solid badge, the one each store publishes as its default. | The store's own colours. Fixed, and not drawn from design-system tokens. |
| **Outline** | The lighter drawing — wordmark and logo on an outlined container, no solid fill. | Design-system tokens. See the table below. |

**`Filled` exists on a light theme only.** Sixteen `Outline` variants cover both
themes; eight `Filled` variants cover `Light`. That is 24 rather than 32, and
**it is deliberate** — Gabriel, 21 September 2026. The filled badge is drawn to
sit on any surface, so it needs no dark counterpart.

#### Theme

##### Light, Dark

**Which surface the badge is sitting on**, for the `Outline` type.

| Theme | Outline colour | Wordmark colour |
| --- | --- | --- |
| **Light** | `Color/Border/Subdued/Default` | `Color/Content/Default/Default` |
| **Dark** | `Color/Border/Light/Default` | `Color/Content/Default/Default` |

_**The theme changes the outline, not the wordmark.** Both themes bind the same
content token; only the border token differs, so the wordmark stays legible
while the container adapts to the surface behind it._

#### Language

##### English, French, German, Dutch

**Four languages, and the wording is drawn rather than typed.** "Download on the
App Store" and "Get it on Google Play" are supplied by the stores in each
language.

**Nothing translates this for you.** The wording is part of the artwork, so it
does not follow a page's locale, and it cannot be edited or replaced. Pick the
language when you place the badge.

#### Modifiers

Not documented

_The component has no modifiers. Everything about it is set by the four axes
above — there is no size option, no icon slot, and no text to swap._

## breadcrumb

_From `components/breadcrumb/breadcrumb.md`._

#### Modifiers

##### Icons

Breadcrumb links are available with an icon to the left or right. External links should be marked with the external link icon.

| Icon left | Icon right | External link icon |
| --- | --- | --- |
|  |  |  |

---

## burger-menu

_From `components/burger-menu/burger-menu.md`._

#### Breakpoint and bottom bar

##### Four variants

| Property | Options | Default |
| --- | --- | --- |
| **Breakpoint** | `320 px`, `768 px` | `320 px` |
| **Bottom bar** | `Off`, `On` | `Off` |

2 × 2 = 4. The full grid.

**`Burger menu (profil)` carries exactly the same two axes and the same four
variants.** The two differ in content only — which is why one is selectable and
the other is not.

#### Modifiers

Not documented

_The component carries no booleans, no instance swaps and no slots. Both axes
are variants._

##### Anatomy

The variant is a device-sized canvas holding two things: a **backdrop** over the
page, and the **menu panel** itself.

| Part | What it is |
| --- | --- |
| **Backdrop** | The dimmed page behind the panel |
| **Close button** | 40 × 40, at the top of the panel |
| **Rows** | The navigation entries, 56 tall, padded 16 all round |
| **Dividers** | A 1-tall rule between rows |

At 768 the panel is 392 wide against a 768 canvas, with 56 of padding above the
first row. **The panel does not fill the width** — the backdrop stays visible
beside it.

## button

_From `components/button/button.md`._

#### Emphasis

These different types of buttons are based on the level of emphasis we want to give to various actions. The most important aspect is to establish a visual hierarchy among the buttons in your UI. Keep these best practices in mind.


Proportion of emphasis used across AVIV products

| Emphasis | Purpose |
| --- | --- |
| Primary | For the main call to action on the page. Primary buttons should only appear once per section. |
| Secondary | For secondary actions on each page. Secondary buttons can be used in conjunction with a primary button. |
| Tertiary | For less prominent, and sometimes independent, actions. Tertiary buttons can be used in isolation or paired with a primary button when there are multiple calls to action. Tertiary buttons can also be used for sub-tasks on a page where a primary button for the main and final action is present. |
| Danger | Reserved for destructive actions. These actions normally delete user's data and cannot be reverted. Depending on the severity of the action a confirmation modal can follow a Danger button action. |

| DO | DON'T |
| --- | --- |
|  **DO:** Use only one primary button per section. |  **DON'T:** Don't use more than one primary button per section. |

| DO |
| --- |
|  **DO:** You can use secondary and tertiary buttons without the need to include a primary one. |
|  **DO:** You can group multiple secondary and tertiary buttons. |

| CAUTION |
| --- |
|  **CAUTION:** Be cautious using a standalone tertiary button as without context these buttons could be overlooked as actions. |

Data tracking showed that the button change from secondary to tertiary initially caused a short-term drop in engagement but led to a sustained long-term increase. It is now performing the same / slightly better.

| Primary | Secondary | Tertiary | Danger |
| --- | --- | --- | --- |
|  |  |  |  |

#### Size

At AVIV we use our 40px height button as the default but there's no strict rule that prevents designers from using the 48px or 32px height one, however when using the different sizes be mindful of the white space around them: the more white space around a button or a group of buttons you'll have, the more chances to use a bigger button.

| DO | DON'T |
| --- | --- |
|  **DO:** Use the same size of the button or field aside. | **DON'T:** Do not use a different size between two buttons aside or the field next to the button. |

#### Context

Buttons change appearance depending on their context and background to better adapt to the environment, maintaining the same level of accessibility and usability.

| DO |
| --- |
|   <!-- order-inferred, please verify --> **DO:** Use the floating variant for buttons that overlap images. |
|  **DO:** Use the floating variant for buttons that overlap images. |

#### Modifiers

##### Icons

Icons are used to emphasize the action stated in the label of the button. By default we use the left aligned button. Icon-only buttons should contain icons that easily depict the action intended.

| DO | DON'T |
| --- | --- |
|  **DO:** Icons that serve an interactive function must be placed within an icon-only button. This ensures accessibility, and clear affordance for user interactions. |  **DON'T:** Icons should not be added to layouts with the intent of being interactive. Icons themselves do not support different states or interactions and must be placed within appropriate interactive components, such as buttons, to ensure usability and accessibility. |

| Icon only | Icon left | Icon right |
| --- | --- | --- |
|  |  |  |

##### Badge

Badges in buttons are used to display dynamic information that grabs the user's attention. They can be used for things like notifications, alerts, or filtering.

---

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
|  |  |  |

## button-bar

_From `components/button-bar/button-bar.md`._

Not documented

#### Modifiers

##### Display mode

Two modes, `page` and `modal`. They differ only in the vertical padding applied
from the `md` breakpoint up; below it both use the phone padding.

## button-card

_From `components/button-card/button-card.md`._

#### Alignment

Button cards are available with vertical and horizontal alignment. Which one to use depends on the content inside the card, the available space on the screen, and the overall visual design of the page.

##### Single button card

| Vertical | Horizontal |
| --- | --- |
|  |  |

##### Button card group

| Horizontal | Vertical |
| --- | --- |
|  |  |

#### Modifiers

##### Icons and illustrations

Use icons or illustrations to make the button cards more prominent and emphasize the action stated in the label.

| With illustration | With icon | Without illustration or icon |
| --- | --- | --- |
|  |  |  |

| DO | DON'T |
| --- | --- |
|  **DO:** Only use one type of button card in the same section. |  **DON'T:** Don't mix icons and illustrations in the same section. |

---

## button-group

_From `components/button-group/button-group.md`._

#### Number of items

The button group contains 2 to 9 items. Button groups with more than 7 items are mainly used for energy selection on desktop.

| DO |
| --- |
|  **DO:** Limit button group items to 7 or fewer for most cases to avoid accessibility problems. |
|  **DO:** If you want to display more than 7 options use chip groups for multi-select and dropdowns for single-select instead. |

| CAUTION |
| --- |
|  **CAUTION:** More than 7 items are only used in the energy selection. |

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- |
|  |  |  |  |

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- |
|  |  |  |  |

#### Modifiers

##### Icons

Icons can be added as visual cues to provide clarity to the user. The icon is always to the left of the label.

| DO | DON'T | CAUTION |
| --- | --- | --- |
|  **DO:** Combine icons with text for clarity. |  **DON'T:** Avoid mixing different combinations. |  **CAUTION:** Make sure icons clearly communicate its meaning when they are used without a label. |

| Icon only | Icon left | No icon |
| --- | --- | --- |
|  |  |  |

##### Border highlight

The highlight is used for energy and co2 selection.

| &nbsp; | &nbsp; |
| --- | --- |
|  |  |

##### Header

When the button group is used in a form add the header and use a clear and concise label. Go to the form guidelines for more information.



##### Helper Text

Include a helper text to improve accessibility. Go to the form guidelines for more information.

| Left helper text | Left and right |
| --- | --- |
|  |  |

#### Selection

For single selection, the button group allows users to select one item. For multiple selection, users can select multiple items.

| DO | DON'T |
| --- | --- |
|  **DO:** Use checkboxes, radio buttons, or chip groups to avoid having both single- and multi-select button groups on the same page. |  **DON'T:** Avoid mixing single-select and multi-select. |

| Single-select | Multi-select |
| --- | --- |
|  |  |

---

## card

_From `components/card/card.md`._

#### Color

The card is available with 4 different background colors. Choose the color according to how much attention you want to draw to the card.

| DO |
| --- |
|  **DO:** Use different background colors to create visual hierarchy. |

| Default | Light | Primary light | Primary strong |
| --- | --- | --- | --- |
|  |  |  |  |

#### Radius

Cards are available with a radius of 4, 8 or 16px. Choose the radius according to the size of the card. The bigger the card, the bigger the radius should be.

| 4px | 8ps | 16px |
| --- | --- | --- |
|  |  |  |

#### Padding

The card can be used with 8px padding or without padding. Choose the padding according to the content you want to put inside.

| DO |
| --- |
|  **DO:** Use the card with padding to separate content from the edge. |
|  **DO:** When you wrap clickable cell contents inside cards, no padding is needed because the cell contents already contain padding. This makes the entire card clickable. |

| With padding | Without padding |
| --- | --- |
|  |  |

#### Slots

The content placeholder in the card is available with 1 to 5 slots. You can use the slots as a helper to structure the content inside.

---

| 1 slot | 2 slots | 3 slots | 4 slots | 5 slots |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

#### Modifiers

Not documented

## carousel

_From `components/carousel/carousel.md`._

#### Arrow position

Arrows can be positioned inside or above the content. We recommend using the inside arrows for visually focused content and large images. Use the top arrows when you want to avoid covering content, or when the design has interactive elements that need to remain visible.

| CAUTION |
| --- |
|  **CAUTION:** Make sure the arrows don't cover relevant information or interactive elements. If they do, use arrows above the content. |

For accessibility reasons arrows are **mandatory** on the web (desktop and mobile).

| Inside | Above |
| --- | --- |
|  |  |

#### Dots

Dots are optional progress indicators that show the current slide. They can be placed inside or outside the content. We recommend placing dots inside the content when space is limited or the design is more focused on visuals, and outside the content when you want to avoid content overlap and improve readability. If the dots are placed inside, change the style of the dots to "contrast".

| CAUTION |
| --- |
|  **CAUTION:** Make sure that dots don't cover relevant information. Use outside dots if they don't. |

| Inside | Outside | No dots |
| --- | --- | --- |
|  |  |  |

#### Clipped content

It's possible to show or clip the content that exceeds the carousel container.

| DO |
| --- |
|  **DO:** Use the carousel with clipped content if you want to align the content with other content on the page. |

| DO |
| --- |
|  **DO:** Use the carousel without clipped content if you want the content to reach the edge. |

| Clipped content | Visible content |
| --- | --- |
|  |  |

#### Modifiers

##### Title and description

Title and description are both optional. We recommend using the title as the primary identifier, and adding a description when additional clarity or explanation is needed. We don't recommend using the description alone.

| Title and description | Only title | No title or description |
| --- | --- | --- |
|  |  |  |

#### Carousel items

Carousel items hold the content. The carousel can be set to automatically adjust the number of items displayed per slide based on the available screen width, or it can be configured to display a fixed number of items per slide. The number of items displayed can also change at different screen sizes (breakpoints), so that more items are displayed when more space is available.


---

## cell-content

_From `components/cell-content/cell-content.md`._

#### Alignment

Cell contents are available with horizontal and vertical alignment. Which one to use depends on the available space, the amount of content, and the overall visual design of the page.

| DO |
| --- |
|  **DO:** Use the horizontal layout when there is plenty of horizontal space and the content in the cell is longer. |
|  **DO:** Use the vertical layout where horizontal space is limited but vertical space is available, such as in grid structures. Allows compact display of information in tight spaces. |

| Horizontal | Vertical |
| --- | --- |
|  |  |

#### Padding

The cell content is available with 0, 8 and 16px padding. Which one to use depends mainly on the visual design of the container in which the cell content is placed. For narrower designs where space is limited, use 8px; for wider designs, use 16px. Use 0 when the container already supplies the inset and the cell content has to sit flush inside it.

Padding applies to all four sides. It changes the outer inset only — the gaps between icon, text and trailing icon are unchanged, and the height stays driven by the content.

**0 padding is for non-clickable cell contents only.** The clickable combinations were removed from the component set, so only the non-clickable one offers it. The web component still accepts 0 on a clickable cell content — never use it there. Hover, pressed and disabled would paint right up to the edge of the content, with no margin around it.

| 8px | 16px |
| --- | --- |
|  |  |

#### Modifiers

##### Title, body and description

All text elements in the cell content are optional and can be freely combined. We recommend using the title as the primary identifier, and adding the body and description when additional clarity or explanation is needed. In tables, for example, it's possible to use the body text alone. We don't recommend using the description alone.

| Only title | Title and description | Title and body | Only body | Title, body and description |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

##### Icons and image

The cell content contains optional icons and images. Icons and images are available on the left. On the right, only icons are available.

**Link and action icons:** If a link or action is applied to the cell content, the chevron is displayed by default. If an external link is applied, the external link icon is displayed.

How the leading icon sits against the text is a separate setting — see *Icon alignment* below.

| Icon left and right | Icon left | Icon right |
| --- | --- | --- |
|  |  |  |

| No icon | Image and icon | Only image |
| --- | --- | --- |
|  |  |  |

**Link and action icons**

| Action and internal link | External link |
| --- | --- |
|  |  |

##### Icon alignment

Controls how the leading icon sits against the text. **Horizontal layouts only.** Vertical layouts are unaffected and have no such setting.

| Setting | What it does |
| --- | --- |
| **Middle** — the default | The 24×24 leading icon is centred against the whole title, body and description block. |
| **Top** | The leading icon is centred against the first line of text — the 24px title line when there is a title. |

Top does not mean top-edge alignment. The icon and the first line of text are centred against each other, never lined up by their top edges.

**Measured on the live component** (horizontal, 16px padding, title + body + description): under `Middle` the 24×24 icon's centre sits on the centre of the whole text block; under `Top` it sits on the title's own centre. The trailing icon's centre stays on the whole-block centre under both. With a 24px title the icon's top edge lands on the title's top edge as well — that follows from both being 24px tall, and is not the rule.

**With no title, the icon should centre on the first body line. That is design intent and has not been measured** — the title is a toggle rather than a variant, so the behaviour cannot be read off the component set.

The trailing icon is always centred against the whole content block, under both settings.

**If a trailing icon is shown, the leading icon must be Middle.** Nothing prevents Top in that combination — not the component, not the build — so the rule holds by convention alone. A top-aligned leading icon beside a centred trailing icon sits the two visuals on different lines and unbalances the row.

The setting governs the leading placeholder slot, which can hold an icon or an image. An image can stand in for the icon anywhere the icon is used, to build a list or a similar row. **What `Top` does with an image rather than a 24×24 icon is not documented**, and no rule for it exists.

##### Badge

An optional badge can be placed next to the title in the cell content.

| DO |
| --- |
|  **DO:** Use badges to indicate notifications or updates. For example, for messages or alerts. |



##### Tag

An optional tag can be placed next to the title in the cell content.



##### Clickable

The cell content can be either clickable or non-clickable.

---

## charts

_From `components/charts/charts.md`._

_This doc has no Variants & Modifiers section._

## checkbox

_From `components/checkbox/checkbox.md`._

#### Border

Checkboxes can be used with or without a border. Add a border when you want to emphasize the options more clearly. Borders can also help to distinguish each checkbox.

| Without border | With border |
| --- | --- |
|  |  |

#### Label

Checkboxes should be used with a label in most cases. Only in a few exceptions, when the context is clear, can checkboxes be used without labels. For example, in tables.

| With label | Without label |
| --- | --- |
|  |  |

#### Modifiers

Checkboxes have the same elements as all form components:

* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the checkbox

See the form guidelines for more information.

---

| Required | Required | Optional |
| --- | --- | --- |
|  |  |  |

| Optional | Tooltip | Tooltip |
| --- | --- | --- |
|  |  |  |

## checkbox-group

_From `components/checkbox-group/checkbox-group.md`._

#### Alignment

Checkbox groups can be aligned vertically or horizontally, depending on the use case and layout structure. For better readability, arrange radio buttons vertically whenever possible.

| Vertical | Horizontal |
| --- | --- |
|  |  |

#### Modifiers

##### Border

Like standalone checkboxes, checkbox groups can also be used with or without a border. Add a border if you want to emphasize the options more clearly. Borders can also help to distinguish each checkbox.

| DO                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **DO:** Use checkboxes without borders when the checkbox group is simple and the options are easily distinguishable without added visual emphasis.                                                                                 |
|  **DO:** Use borders around checkbox groups when you want to clearly distinguish options, especially in complex forms. Borders help visually separate each option, making it easier for users to scan and understand their choices. |

| Without border | With border |
| --- | --- |
|  |  |

##### Columns

Vertical checkbox groups are available in one or two columns.

| One column | Two columns |
| --- | --- |
|  |  |

##### Header

Like all form components, checkbox groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the form guidelines for more information.

---



## chip

_From `components/chip/chip.md`._

#### Type

##### Filter chips

Filter chips are used to represent filters in a set of options. They allow users to toggle selections on and off, providing a way to dynamically apply or remove filters.

| DO |
| --- |
|  **DO:** Use filter chips to filter content. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
|  |  |  |

##### Input chips

Input chips represent user input, selections, or entries within a form. They can be removed with the close icon.

| DO |
| --- |
|  **DO:** Use input chips to select items or enter information into a field. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
|  |  |  |

##### Action chips

Action chips trigger actions when clicked, often performing contextual tasks that enhance the primary functionality of a page. They are lightweight, intuitive, and designed for quick, secondary actions.

| DO | DON'T |
| --- | --- |
|  **DO:** Use action chips when users need a lightweight, dynamic way to perform quick actions relevant to their current task. |  **DON'T:** Don't use action chips as primary navigation or for critical actions. Don't use them to move to the next/previous step or to complete/progress in a user journey. Use buttons instead. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

#### Modifiers

##### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the chip more intuitive and easier to understand.

---

| With icon | Without icon |
| --- | --- |
|  |  |

#### Filter chips

| Unselected | Selected |
| --- | --- |
|  |  |

#### Input chips

| Unselected | Selected |
| --- | --- |
|  |  |

#### Action chips

| Default |
| --- |
|  |

## chip-group

_From `components/chip-group/chip-group.md`._

#### Type

##### Filter chips

Filter chips are used to represent filters in a set of options. They allow users to toggle selections on and off, providing a way to dynamically apply or remove filters.

| DO |
| --- |
|  **DO:** Use filter chips to filter content. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
|  |  |  |

##### Input chips

Input chips represent user input, selections, or entries within a form. They can be removed with the close icon.

| DO |
| --- |
|  **DO:** Use input chips to select items or enter information into a field. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

| Default selected | Hover selected | Pressed selected |
| --- | --- | --- |
|  |  |  |

##### Action chips

Action chips trigger actions when clicked, often performing contextual tasks that enhance the primary functionality of a page. They are lightweight, intuitive, and designed for quick, secondary actions.

| DO | DON'T |
| --- | --- |
|  **DO:** Use action chips when users need a lightweight, dynamic way to perform quick actions relevant to their current task. |  **DON'T:** Don't use action chips as primary navigation or for critical actions. Don't use them to move to the next/previous step or to complete/progress in a user journey. Use buttons instead. |

| Default | Hover | Pressed |
| --- | --- | --- |
|  |  |  |

#### Modifiers

##### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the chips more intuitive and easier to understand.

---

| With icon | Without icon |
| --- | --- |
|  |  |

#### Filter chips

| Unselected | Selected |
| --- | --- |
|  |  |

#### Input chips

| Unselected | Selected |
| --- | --- |
|  |  |

#### Action chips

| Default |
| --- |
|  |

## coach-mark

_From `components/coach-mark/coach-mark.md`._

#### Boolean

Only the title and the close icon are mandatory. All other elements can be hidden, offering a variety of layout.

| Full | Simple |
| --- | --- |
|  |  |

#### Tag position

To ensure a perfect readability, the tag can be aligned with the title or placed on top when the title is on two lines. It's up to the consumer.

| Horizontally aligned | On-top |
| --- | --- |
|  |  |

#### Modifiers

Not documented

---

## counter-field

_From `components/counter-field/counter-field.md`._

#### Modifiers

##### Header

Like all form components, counter fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.

---



## date-field

_From `components/date-field/date-field.md`._

#### Platform, state, content and error

##### The four axes

**32 variants — the full grid**, with nothing missing.

| Property | Options | Default |
| --- | --- | --- |
| **Platform** | `Web/iOS`, `Android` | `Web/iOS` |
| **State** | `Default`, `Hover`, `Active`, `Disabled` | `Default` |
| **Content** | `Empty`, `Filled` | `Empty` |
| **Error** | `No`, `Yes` | `No` |

2 × 4 × 2 × 2 = 32. **Every combination exists**, including `Disabled` with
`Error=Yes`.

#### Modifiers

##### The switches

Six booleans, set independently of the variant.

| Switch | Default | What it adds |
| --- | --- | --- |
| **Required** | off | An asterisk beside the label |
| **Optional** | off | The word "(optional)" beside the label |
| **Tooltip** | off | An info icon beside the label, in its own 40 touch zone |
| **Helper Text** | off | A line of guidance under the field |
| **State Message** | **on** | The feedback line under the field — where an error's reason goes |
| **Clear icon** | **on** | Clears what has been typed |

_Both `Helper Text` and `State Message` render a `state_message` instance. They
are the same component in two roles: guidance before, feedback after._

##### The calendar button, and an open question

**The field carries a calendar button** — a 40-wide button holding a calendar
icon, at the right-hand end of the input.

**This appears to contradict the rule that sends you here.** The rule says to
choose a date field when *no calendar is offered*, and to choose `Date picker`
when one is. The component has a calendar affordance anyway.

**Not tested** — nobody has established whether that button opens a calendar, is
decorative, or is a leftover from the `Date picker` it shares a page with. Until
it is answered, **follow the rule, not the button**.

## date-picker

_From `components/date-picker/date-picker.md`._

#### Modifiers

##### Header

Like all form components, date pickers contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.



---

## divider

_From `components/divider/divider.md`._

#### Orientation

The divider is only available in horizontal orientation. We currently don't offer vertical dividers or dividers with different widths or styles in Gemini.



| DON'T |
| --- |
|  **DON'T:** Don't create dividers with different width or styles. |

---

#### Modifiers

Not documented

## dropdown

_From `components/dropdown/dropdown.md`._

#### Modifiers

##### Header

Like all form components, dropdowns contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.



##### Icons

Icons can be added to the field and the dropdown list. They act as visual cues to provide clarity to the user. All icons are non-clickable.

| DO | DON'T |
| --- | --- |
|  **DO:** If some items don't have an icon, remove all icons. |  **DON'T:** Don't mix list items with and without icons, as it reduces readability. |

##### Suffix

The suffix can be added to provide additional context.

---



## energy-tag

_From `components/energy-tag/energy-tag.md`._

#### Country

Energy tags vary by country and region, reflecting local standards for energy efficiency. Please note that in Belgium there are three different systems for Brussels, Wallonia and Flanders.

##### France

      

##### Germany

        

##### Austria

       

##### Brussels (Belgium)

      

##### Flanders (Belgium)

      

##### Wallonia (Belgium)

        

We don't currently support energy tags for other countries, such as Switzerland.

#### Modifiers

Not documented

---

## estimation-card

_From `components/estimation-card/estimation-card.md`._

**Three axes, 16 variants.** `Size`, `State` and `Type`. Twenty-four
combinations are possible and eight do not exist — see the grid below.

#### Size

##### Large, Medium, Small, Horizontal

**How much room the card has**, and how much of the estimate it can show.

| Size | Collapsed | Expanded | Shape |
| --- | --- | --- | --- |
| **Large** | 320 wide | **447 wide** | The only size that widens when expanded |
| **Medium** | 288 wide | 288 wide | Grows downward only |
| **Small** | 288 wide | **none** | Summary only |
| **Horizontal** | 438 × 156 | **none** | A wide, short strip |

_**`Large` is the only size that changes width between its two states.** Every
other size keeps its width and grows taller. Budget for the extra 127 before
choosing `Large` in a fixed column._

#### State

##### Collapsed, Expanded

**Whether the detail behind the figure is shown.** Collapsed gives the headline
figure, the range and the confidence reading. Expanded adds the breakdown and
the feedback question.

**Two sizes have no expanded form.** `Small` and `Horizontal` exist as
`Collapsed` only. Choosing either is a decision that the detail will never be
reachable from this card.

#### Type

##### Selling price, Renting price, Sell and Rent price

**Which estimate the card carries.**

| Type | What it shows |
| --- | --- |
| **Selling price** | One estimate, what the property would sell for |
| **Renting price** | One estimate, what it would rent for |
| **Sell and Rent price** | Both, switched between on the card itself |

_**`Sell and Rent price` is about 60 taller than the other two**, at every size
and state. It carries a second figure and the control that switches between
them._

#### The grid, and the eight combinations that do not exist

| Size | Selling / Renting / Sell and Rent, Collapsed | …Expanded |
| --- | --- | --- |
| **Large** | all three | all three |
| **Medium** | all three | all three |
| **Small** | all three | **none** |
| **Horizontal** | **`Selling price` only** | **none** |

**`Horizontal` is a single variant.** Collapsed, selling price, and nothing
else. A horizontal card cannot show a renting price, cannot show both, and
cannot expand.

_**Whether these eight absences are deliberate is not tested.** Nobody has been
asked. Three other short grids in the system were confirmed deliberate on
21 September 2026; these were not among them._

#### Modifiers

**The card's parts can each be set**, and they are reachable when you place it.

##### Price range

**How the lowest and highest price are presented.** Four options: as text, or
with icons at three sizes.

##### Confidence indicator

**How firm the estimate is.** Five levels, from most to least confident:
**High**, **Good**, **Medium**, **Mediocre**, **Low**.

_Five levels, not three. A card showing a figure without one is presenting an
estimate as though it were a fact._

##### Estimation details

**The breakdown behind the figure**, shown when the card is expanded. Two
presentations: with icons, or as text.

##### Feedback module

**The question asking whether the estimate was useful.** Three forms — a thumbs
score at two text sizes, or a form.

**The thumbs form places `Feedback thumb buttons`.** That component is built by
a team outside the design system and has never been adopted into it; this card
is a place it is genuinely used. See
`feedback-thumb-buttons`.

## feedback-bar

_From `components/feedback-bar/feedback-bar.md`._

#### Orientation and container

##### Four variants

| Property | Options | Default |
| --- | --- | --- |
| **Orientation** | `Horizontal`, `Vertical` | `Horizontal` |
| **Container** | `NO`, `YES` | `NO` |

2 × 2 = 4. The full grid.

| Variant | Size |
| --- | --- |
| Horizontal, no container | 689 × 82 |
| Horizontal, with container | 689 × 82 |
| Vertical, no container | 360 × 268 |
| Vertical, with container | 360 × 640 |

_The vertical pair differ in height because the container version is drawn at
full mobile height, not because the content changes._

#### Modifiers

##### Pre-title

On by default. A line of text above the title, inside the same block.

##### Illustration

On by default, and **swappable** — the component exposes an illustration slot
rather than fixing one. The illustration is 50 × 50 in the horizontal variant.

##### The scale

The row of numbers is a **button group**, exposed so its buttons can be set
individually — each carries `Type`, `State` and `Selected`.

**The scale is one to five.** The group is configured with seven slots and
**two of them are hidden**, which is a leftover in the library rather than a rule.
**Do not read seven buttons into it**; five are visible and numbered 1 to 5.

Each button is 73 × 40, and they are laid out with a -1 gap so their borders sit
on top of one another rather than doubling.

## feedback-message

_From `components/feedback-message/feedback-message.md`._

#### Type

Feedback messages come in the following types: info, success, warning, and error.

| Info | Success | Warning | Error |
| --- | --- | --- | --- |
|  |  |  |  |

#### Floating and corner radius

Feedback messages can be floating and non-floating. The floating version floats above the content, the non-floating one is used inline with the content.

Feedback messages are available with and without corner radius. The version without corner radius is manly used to create floating banner at the top of the page.

| Floating | Non-floating |
| --- | --- |
|  |  |

| 16px corner radius | Without corner radius |
| --- | --- |
|  |  |

##### Breakpoints

We recommend displaying the floating feedback message with rounded corners on desktop and without corners (as a banner) on tablet and phones.

#### Modifiers

##### Title and description

Titles are optional, but recommended for clarity. Descriptions are mandatory.

| With title | Without title |
| --- | --- |
|  |  |

##### Buttons

Feedback messages are available with 1 - 2 buttons or without buttons.

| 1 button | 2 buttons | Without button |
| --- | --- | --- |
|  |  |  |

##### Close button

Dismissible messages have a close button (x-icon), non-dismissible messages don't. Whether a message should be dismissible or not depends on the information you want to communicate. For example, critical global messages should stay displayed permanently, and errors should stay displayed until the problem that caused the error is fixed. A simple success confirmation, on the other hand, can be dismissible.

| DO | DON'T |
| --- | --- |
|  **DO:** Use close buttons when the feedback message provides non-critical information that users can dismiss after reading. This helps reduce visual clutter and allows users to focus on other important tasks without being repeatedly reminded of the same message. |  **DON'T:** Don't use close buttons for feedback that requires ongoing action. Keeping it visible ensures that the reminder stays in place until addressed. |

---

| With close button | Without close button |
| --- | --- |
|  |  |

## feedback-thumb-buttons

_From `components/feedback-thumb-buttons/feedback-thumb-buttons.md`._

**One axis, two variants.** `Device`.

#### Device

##### Desktop, Mobile

**The width the pair is laid out for.** Both are web breakpoints. Neither is a
native platform.

| Device | Each button | The pair | How the buttons size |
| --- | --- | --- | --- |
| **Desktop** | 48 × 48, square | 120 × 48 | Each hugs its icon |
| **Mobile** | 48 high, half the row | 48 high, full row | Each fills half the available width |

_**`Mobile` is not a fixed 328 wide.** Both buttons are set to fill, so the pair
takes whatever width it is given and splits it evenly between them. 328 is what
that comes to at the default placement, not a size the component holds._

**Both options use exactly the same button underneath.** The only thing `Device`
changes is whether the two buttons hug their icons or stretch to fill the row.

#### Modifiers

Not documented

_The component has one property, `Device`. There is no size option, no state, no
label slot, and the two icons cannot be swapped._

##### What the two buttons are fixed to

Each thumb is a **Button**, configured identically in both variants: type
**Secondary**, style **Default**, **icon only**, size **48**, loading **No**.
One carries the `thumbs-up` icon, the other `thumbs-down`, each drawn at 24.

**Neither button is exposed.** Placing the pair gives you no way through to the
button underneath — you cannot change its type, set a state, or replace an
icon. The pair is all-or-nothing.

## filter-bar

_From `components/filter-bar/filter-bar.md`._

#### Size

The filter bar is available with a height of 40 and 48px.

| 40px | 48px |
| --- | --- |
|  |  |

#### Modifiers

Not documented

---

##### Show/hide filters button (desktop only)

All the filters button can be shown or hidden.

| All filters visible | Hidden filters |
| --- | --- |
|  |  |

##### Show/hide primary button

Since the primary button is not a validation button, it is optional and can be hidden.

| With primary button | Without primary button |
| --- | --- |
|  |  |

## floating-button-group

_From `components/floating-button-group/floating-button-group.md`._

#### Buttons

The floating button group is available with 2 - 3 buttons.

| 2 buttons | 3 buttons |
| --- | --- |
|  |  |

#### Alignment

The floating button group is available with a vertical and horizontal alignment.

| Vertical | Horizontal |
| --- | --- |
|  |  |

#### Modifiers

Not documented

---

## floor-selection

_From `components/floor-selection/floor-selection.md`._

#### Modifiers

##### Header

Like all form components, floor selections contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the form guidelines for more information.



We recommend using the default helper text to help the user understand how to enter the ground floor.

## image-slider

_From `components/image-slider/image-slider.md`._

#### Aspect ratio

##### 3/2, 4/3, 16/9, 21/9

Four ratios. **The ratio is required and has no default.** It fixes the frame's
height against its width, so every image in the set is shown in the same shape.
No rule for choosing one is documented.

#### Corners

##### Square and rounded

Two corner treatments, square by default. No rule for choosing is documented.

#### Modifiers

##### Image loading

Three behaviours, controlling when the browser fetches each image:

| Setting | Behaviour |
| --- | --- |
| **Unset** | The current image loads immediately, along with the one before and the one after |
| **First** | The first image loads, then the one before and after it. From then on it behaves as unset |
| **All** | Every image loads only when it becomes visible |

Once an image has been shown, it stays loaded.

##### Counter offset

The counter sits at the bottom right. Its distance from the bottom edge is 16px
or 32px, 16px by default. No rule for choosing is documented.

##### Icon markers

Up to two icons may be placed beside the counter, each rendered as a tag. They
are hidden from assistive technology, so each one must be described in the
slider's accessibility label.

##### Vertical scrolling

By default a vertical drag scrolls the page rather than swiping the slider, and
pinch-to-zoom is off. It can be set to allow the browser's full default
behaviour instead.

## info-state

_From `components/info-state/info-state.md`._

Not documented

---

#### Modifiers

Not documented

##### Illustration/Icon

Info states can be used with an icon, an illustration, or neither. You can't use them with an icon and an illustration at the same time.

If you use an illustration we recommend the usage of hero illustrations.

| With illustration | With icon | No icon/illustration |
| --- | --- | --- |
|  |  |  |


##### Title and description

Both title and description are mandatory.



##### Buttons

Info states can be used with 1-2 buttons, or without any. If two buttons are used, we recommend combining the primary and tertiary buttons.

They should be used when they provide clear next steps or actions for users, such as retrying after an error, navigating to another page, or resolving an issue.

| With two buttons | With one button | Without buttons |
| --- | --- | --- |
|  |  |  |

## kpi

_From `components/kpi/kpi.md`._

#### Layout

You can change the alignment to horizontal or vertical when an additional indicator is shown.

| Horizontal | Vertical |
| --- | --- |
|  |  |

#### Display Context

| With a graph | Independent |
| --- | --- |
|  |  |

#### Modifiers

Not documented

##### Elements



| Element | Description | Mandatory | Customisable |
| --- | --- | --- | --- |
| Title | Concise KPI title | Yes | Yes |
| KPI | Unique number highlighting important data or conclusion | Yes | Yes |
| Additional indicator | Messages provide context or additional data, usually trending or comparing with other data. Use a state message or a tag to highlight more of the data. | No | Yes |

---

## link

_From `components/link/link.md`._

#### Type

Links can be standalone or inline. Both types can be used to link to internal or external pages or files.

| Standalone | Inline |
| --- | --- |
|  |  |

##### Standalone



Standalone links are used on their own. They should not be used within a sentence or paragraph.

##### Inline



Inline links are used within a sentence or paragraph.

#### Size

**Standalone:** The standalone links have a font size of 16px.

**Inline:** The inline link automatically adapts to the font size of the text in which it's placed.

#### Context

Links change their appearance depending on their context and background to better adapt to the environment while maintaining the same level of accessibility and usability.

| Default | Inverted | On-primary | On-secondary |
| --- | --- | --- | --- |
|  |  |  |  |

#### Modifiers

##### Icons

Icons are used to emphasize the text content in the link label.

**Standalone link:** The standalone link can have a left, right, or external icon to indicate external links.

| No icon | Icon left | Icon right | External icon |
| --- | --- | --- | --- |
|  |  |  |  |

| DO |
| --- |
|  **DO:** Use icons in standalone links. |

**Inline link:** To ensure readability, the inline link doesn't have any icons other than the external link icon.

| No icon | External icon |
| --- | --- |
|  |  |

| DO | DON'T |
| --- | --- |
|  **DO:** Use inline links without icons to ensure readability. Use only the external link icon for external inline links. |  **DON'T:** Don't add other icons to inline links. |

---

## listing-card

_From `components/listing-card/listing-card.md`._

#### Layout

* **Vertical layout** is reserved for mobile devices Listing Cards, both Web and App versions, except the S - carousel version.
* **Horizontal layout** is used on larger devices like tablets and desktop sizes. It can be used in combination with S - carousel.
* **Ribbon** is an add-on to bring more attention to the listing and use it as a promotion.

| Vertical | Horizontal | Overview |
| --- | --- | --- |
|  |  |  |

#### S Carousel

##### S - carousel

The listing card size S only comes in vertical alignment, this is because it is only meant to be displayed inside carousels. These carousels can be added to your page as sponsored listings, suggested similar listings, etc.

The Image slider inside the Listing card is disabled so the user can't slide through the images, however, the slide counter is displayed with the numbers so the user can see the amount of images the listing contains.



There are two ways of displaying these carousels:

##### Fixed width Listing Card S

This listing card has a fixed width of 280px so the overflowing cards can be cut out of the carousel. They all have a fixed margin of 24px in between cards and the carousel can slide these cards individually.




*The fourth card in this carousel is clipped.*

##### Responsive width Listing Card S

This listing card has a minimum width of 280px but they grow horizontally to fit the carousel width in stacks of 3 to 5 cards. They all have a fixed margin of 24px in between cards and the carousel can slide these cards in groups of 3 to 5 cards.




*Listing cards grow horizontally to fit the carousel's width.*

##### Carousel Card Height

In the context of carousel cards, where cards are placed side by side, variations in content length can result in inconsistent card heights. To maintain a uniform height for better readability and visual consistency, S Carousel cards can have a fixed height.

| DO | DON'T |
| --- | --- |
|  **DO:** Carousel cards should have a fixed height to ensure better readability and visual consistency, as content length may vary between cards. |  **DON'T:** Avoid using relative heights for carousel cards, as this can result in inconsistent card heights, making them harder to read and disrupting the visual balance. Use a fixed height instead to ensure readability and uniformity. |

#### Modifiers



| Sub-component | Enable/Disable capability | Quantity | Sizes | Other |
| --- | --- | --- | --- | --- |
| Image slider | N/A | N/A | S: 16:9 · M: 16:9 · L: 3:2 · XL: 16:9 + two 16:9 thumbnails half the height of main image · Map: 21:9 | Gradients on top and bottom are managed by the Image slider component. Size is linked to the size of the Card itself. |
| Top bar tags | Yes | 1, 2, 3 | N/A | — |
| Bottom bar tags | Yes | N/A | N/A | — |
| Price tag + Price €/m2, €/month | Yes: as a whole · Yes: Price €/m2, €/month · No: Price tag only | N/A | Price tag: Headline 24 (default), Headline 22. Price €/m2, €/month: Body 14 (default), Body 12 | — |
| Title | Yes | N/A | 16 (default), 14, Headline 24 | — |
| Feature list | Yes | 3, 4 | 12, 14 (default), 16 | Icons enabled/disabled: 12 size (16px icon), 14 size (16px icon), 16 size (20px icon) |
| Location | Yes | N/A | 12, 14 (default), 16 | — |
| Actions | Yes | 1, 2 | Button size 40 | — |
| Provider | Yes | N/A | M: Avatar size 48px · L: Avatar size 56px · XL: Avatar size 72px · Private owner: Avatar size 24px | They are linked to the size of the Card itself. The divider on top is deleted when no provider. |
| *SEO text block | Yes | N/A | Text size: 12px | **Only needed for Web version of the card** |
| *Partner link | Yes | N/A | Text size: 14px | **Only needed for SeLoger** |

---

## listing-summary

_From `components/listing-summary/listing-summary.md`._

Listing Summaries come with two default variants that change the position of the thumbnail. However, using the Listing Summary component, you can create an infinite number of custom variants.

| Listing summary (Thumbnail on the left) | Listing summary (Thumbnail on top) |
| --- | --- |
|  |  |

#### Modifiers

##### Sub-components

While Listing Summaries provide a high degree of flexibility, enabling designers to customize and organize them according to specific needs, they come with a default set of elements.



| Sub-component | Enable/Disable capability | Quantity | Sizes | Other |
| --- | --- | --- | --- | --- |
| Thumbnail | Yes | N/A | Width: 64, 72, 84, 96, 104, 112, 128, 256 | Aspect ratio: 1:1, 4:3, 3:2<br>Alignment: Left, Top |
| Tags | Yes | 1,2,3 | N/A |   |
| Price tag | Yes | N/A | Headline 24 / €m2 14 (default)<br>Headline 20 / €m2 12 |   |
| Title | Yes | N/A | 16 (default), 14, Headline 24 |   |
| Feature list | Yes | 3, 4 | 12 (default), 14, 16 | Icons enabled/disabled<br>12 Size (16px icon)<br>14 Size (16px icon)<br>16 Size (20px icon) |
| Location | Yes | N/A | 12 (default), 14, 16 |   |
| Helper text | Yes | N/A | 12 (default), 14, 16 |   |
| Action | Yes | 1,2 | Button size 40 |   |

## loading-state

_From `components/loading-state/loading-state.md`._

#### Spinner size

##### 24 and 32

Two sizes, `24` and `32`, being the spinner's size in pixels. Default `32`. No
rule for choosing between them is documented.

#### Colour

##### Dark and light

Two colours, `dark` and `light`, default `dark`. **The colour applies to the
whole component** — the spinner, the title and the description all take it. No
rule for choosing is documented.

#### Modifiers

##### Title

Optional. A single line of text below the spinner, centred, with a gap above it.

##### Description

Optional and independent of the title. Text below the title, centred, with its
own gap above it, in a smaller style than the title.

## map-template

_From `components/map-template/map-template.md`._

**Three axes and two switches, 27 variants.** Thirty-six combinations are
possible and nine do not exist.

#### Map platform

##### Web, iOS, Android

**Which platform the map is drawn for.** It changes the provider's attribution
and the control styling, not the layout.

_The axis is misspelled in the library. It is typed as written, and the
misspelling is recorded on the tool page rather than corrected here._

#### Zoom level

##### Away, Close, Very zommed / 3D

**How close the map sits.** `Away` shows a city or region, `Close` a street, and
the third option drops right down with buildings in three dimensions.

**Android has no closest zoom.** The third option exists for web and iOS only.

#### Style

##### Standard, Dark Mode, Satellite, Price Map

**How the map surface looks.**

| Style | What it is | Where it exists |
| --- | --- | --- |
| **Standard** | The default map | Everywhere |
| **Satellite** | Aerial imagery | Everywhere |
| **Dark Mode** | A dark map surface | **iOS and Android only** |
| **Price Map** | Prices drawn as a layer over the map | **Not at the closest zoom** |

#### The grid, and the nine combinations that do not exist

Three rules account for all nine.

| Rule | Combinations lost |
| --- | --- |
| **Web has no dark map** | 3 — one at each zoom |
| **Android has no closest zoom** | 4 — one per style |
| **The closest zoom has no price map** | 2 — web and iOS |

_**Whether these are deliberate is not tested.** Nobody has been asked. A web
map with no dark surface is the one worth querying, since web is the only
platform missing a style every other platform has._

#### Modifiers

##### The two switches

| Switch | Default | What it controls |
| --- | --- | --- |
| **CTA** | on | The floating actions sitting over the map |
| **Listing Card** | on | The card for the selected property |

_Both are on when you place the template. Switch off what the screen does not
need before detaching, rather than deleting it afterwards._

##### The parts that arrive with it

| Part | What it is |
| --- | --- |
| **Map surface** | The map itself, following the three axes above |
| **Provider attribution** | The map provider's mark, required by the provider |
| **Floating actions** | The actions over the map, controlled by the `CTA` switch |
| **Map controls** | Zoom and locate, stacked at the edge |
| **Price pins** | The price markers on the map — **superseded, see below** |
| **Listing card** | The selected property's card, controlled by its switch |

##### The price pins that arrive are the superseded set

**Every one of the 27 variants carries the old price pins.** Three per variant,
81 in all, and the current pin sets are used nowhere in the template.

**What that means when you place it:** a detached copy inherits the old pins,
and they will not match a screen built from the current ones. Replace them after
detaching.

_**Proved by reading all 27 variants, 22 September 2026.** The exact names, and
the same problem in the floating actions, are on the tool page._

##### The polygon layers

Two layers draw an area on the map rather than a point: one outlines the shape,
the other dims everything outside it. **Both belong to the template and are
never selected on their own.**

The outline draws either a simple area or district boundaries. The dimming layer
follows a shape or a radius, and offers a light, a dark and a price-map form —
though **a radius has no price-map form**.

## media-upload

_From `components/media-upload/media-upload.md`._

#### Modifiers

##### Header

Like all form components, media uploads contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.



##### Illustration

The empty drop zone contain a illustration placeholder. We recommend adding a pictogram.


---

##### File counter

The media upload includes an optional counter. In most cases, we recommend using the counter to give the user a clear idea of how many files they can upload.

| With counter | Without counter |
| --- | --- |
|  |  |

##### Filename

The image/file preview includes an optional filename. In most cases, we recommend displaying the filename to give the user more clarity about what files they can upload. Since the file preview (non-image) only displays a generic illustration, the filename will still be displayed below the icon even if the filename is hidden.

The default filename includes the file extension, e.g. bathroom.jpg. The filename (caption) can be changed using the action menu.

| With filename | Without filename | With filename | Without filename |
| --- | --- | --- | --- |
|  |  |  |  |

##### Cover photo tag

The image/file preview includes an optional cover tag. This tag can be used to mark the cover image. The cover image can be changed in the action menu or by dragging and dropping an image to the first position. The tag can be applied to any type of file.

| With cover image tag | Without cover image tag |
| --- | --- |
|  |  |

## mega-menus

_From `components/mega-menus/mega-menus.md`._

#### Brand, breakpoint and menu

##### 96 variants, three axes

| Property | Options | Default |
| --- | --- | --- |
| **Brand** | `Default`, `Immonet`, `Immoweb`, `Immowelt`, `Logic-Immo`, `Meilleurs agents`, `SeLoger` | `Default` |
| **Breakpoint** | `1024 px`, `1366 px`, `1536 px` | `1024 px` |
| **Menu** | That brand's own menu names | `Default` |

**The Menu axis is content, not configuration.** Its options read as real site
navigation — *SL • To rent*, *SL • Offices & Shops*, *IWT • Property prices*,
*IMT • Real estate appraisal*, *IWB • Valuate*, *MA • Choose an agency*.

**The grid is sparse on purpose.** 96 variants, far fewer than every brand
crossed with every menu, because a brand only has the menus it has.

#### Modifiers

Not documented

_The component carries no booleans, no instance swaps and no slots. Everything
is selected through the three variant axes._

##### One panel, columns inside

A mega menu is a full-width row of link columns. At 1536 the panel is 192 tall,
padded 24 top and bottom and 80 on each side, with 24 between columns; each
column is 326 wide.

**The column count is what the breakpoint changes**, not the type size or the
padding.

## menus

_From `components/menus/menus.md`._

#### Content, type and brand

##### Seven variants

| Property | Options | Default |
| --- | --- | --- |
| **Content** | `Profil`, `Language` | `Profil` |
| **Type** | `Default`, `Simple` | `Default` |
| **Brand** | `Default`, `SeLoger`, `Immonet`, `Immowelt`, `Meilleurs Agents`, `Immoweb` | `Default` |

**The grid is sparse and the pattern is readable:**

| Content | Type | Brands | Variants |
| --- | --- | --- | --- |
| **Profil** | `Default` | All six | 6 |
| **Language** | `Simple` | `Default` only | 1 |

**`Type` is not a free choice.** It tracks the content: a profile menu is
`Default`, a language menu is `Simple`. No variant pairs them otherwise.

**The profile menu is branded, the language menu is not.** Profile options differ
per brand; the language list does not.

#### Modifiers

Not documented

_No booleans, no instance swaps, no slots. All three properties are variants._

##### Anatomy

The panel is **320 wide**, padded 8 above and below, and built from rows.

| Part | Size |
| --- | --- |
| **Header row** | 320 × 56, padded 16 all round |
| **Entry** | 280 × 48, padded 12 above and below, **48 on the left** |
| **Rule** | A full-width line between groups |

**The 48 of left padding on an entry is an indent**, which is what makes an
entry read as sitting under its header rather than beside it.

## modal-bottom-sheet

_From `components/modal-bottom-sheet/modal-bottom-sheet.md`._

Not documented

#### Modifiers

Not documented

---

##### Padding

The modal bottom sheet can be used with or without padding.

| With padding | Without padding |
| --- | --- |
|  |  |

| DO |
| --- |
| <br>**DO:** Use the modal bottom sheet with padding for most use cases. The padding helps separate text, illustrations and components from the border. |
| <br>**DO:** Use the modal bottom sheet without padding when you want to display maps or images in full width. |

##### Header and footer

The modal bottom sheet contains an optional header and footer.

| Header and footer | Only footer | Only header |
| --- | --- | --- |
|  |  |  |

**Header**

The header has a close button on the left, a title in the middle and either a secondary button or up to 2 icons on the left. All elements of the header are optional.

| Header with button | Header with 1 - 2 icons |
| --- | --- |
|  |  |

ℹ️ If a close button is needed, it should be on the left. Please don't change the position in the top bar.

**Footer**

The footer (bottom bar) has 1 - 2 buttons. They can be aligned horizontally or vertically. We recommend vertical alignment only if there is not enough space to align them side by side.

| Footer with 1 button | Footer with 2 horizontal buttons | Footer with 2 vertical buttons |
| --- | --- | --- |
|  |  |  |

#### Sizes

The modal bottom sheet is available in different heights.

| Default (hug content) | Full-Height | Full-Screen |
| --- | --- | --- |
|  |  |  |

| DO |
| --- |
| <br>**DO:** Use the default size when the modal contains a small amount of content. Since the height adjusts to fit the content, it's ideal for compact information or simple actions that don't require scrolling. |
| <br>**DO:** Use the full-height size when the modal contains a large amount of content and may require scrolling. The fixed height ensures consistency within flows. |
| <br>**DO:** Use full-screen size for extensive content or detailed data entry. Full-screen modals are ideal when users need to focus solely on the modal content without distractions. It's useful for displaying maps or full-width images. |

## modal-bottom-sheet-menu

_From `components/modal-bottom-sheet-menu/modal-bottom-sheet-menu.md`._

#### Modifiers

##### Badges

Badges can be added to the right of the menu entries to highlight new features or updates.



##### Header

The modal bottom sheet menu contains a title. On Web, an optional subtitle can be added. The title is mandatory, but can be hidden if the context is clear.


---

##### Trigger

Like the action menu, the modal bottom sheet menu can be opened with the following button types: tertiary icon button, floating icon button and text button.

If you use a different trigger, please share your use case with us so we can improve our guidelines and documentation.

| Tertiary icon button | Floating icon button | Text button |
| --- | --- | --- |
|  |  |  |

##### Icons

Icons can be added to the menu list. They act as visual cues to provide clarity to the user.

| With icons | Without icons |
| --- | --- |
|  |  |

**Title & body text**

Each menu item contains a body text and an optional title.

| Body text | Title and body text |
| --- | --- |
|  |  |

##### Actions & links

Menu items can be actions or links. If the menu item is a link, the external link icon is displayed.



## navigation-bar

_From `components/navigation-bar/navigation-bar.md`._

#### Modifiers

##### Entries and buttons



The number of entries depends on the brand. We don't recommend using more than 7 entries unless it's necessary for SEO reasons.

The button and icon buttons are used on all brands, the language menu is currently only used on immoweb.

A reduced navigation bar with only the logo and the language menu can be used on pages such as funnels.

---

## navigation-bar-app

_From `components/navigation-bar-app/navigation-bar-app.md`._

#### Platform and device

##### Platform, Device, Tabs, Home Indicator

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

#### Modifiers

##### The tab

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

## pagination

_From `components/pagination/pagination.md`._

Not documented

---

#### Modifiers

Not documented

## phone-number-field

_From `components/phone-number-field/phone-number-field.md`._

Not documented

#### Modifiers

Not documented

---

##### Header

Like all form components, phone number fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the form guidelines for more information.

| Web / iOS | Android |
| --- | --- |
|  |  |

Phone Number fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

## progress-bar

_From `components/progress-bar/progress-bar.md`._

#### Styles

| Default | Inverted (on dark background) | Neutral | Success |
| --- | --- | --- | --- |
|  |  |  |  |

#### Size

| 4px | 8px (default) | 12px |
| --- | --- | --- |
|  |  |  |

**4px:** Only recommended when the progress bar has a small hierarchy in the interface.

#### Width

The width can be adapted to the context.

| Fixed | Full width |
| --- | --- |
|  |  |

#### Labels

The progress bar alone does not provide sufficient information to be accessible. It should be accompanied by a numerical progress label (e.g. 75% or 1/5). Both the positioning and size can be customized to suit your needs, depending on the context.

| Left | Right |
| --- | --- |
|  |  |

#### Modifiers

Not documented

---

## progress-circle

_From `components/progress-circle/progress-circle.md`._

#### Styles

| Default | On-dark |
| --- | --- |
|  |  |

#### Size

| 64px | 96px | 128px |
| --- | --- | --- |
|  |  |  |

#### Labels

The progress bar alone does not provide sufficient information to be accessible. It should be accompanied by a numerical progress label (e.g. 75% or 1/5). Label position can't be changed.

#### Modifiers

Not documented

---

## radio-button-group

_From `components/radio-button-group/radio-button-group.md`._

#### Alignment

Radio button groups can be aligned vertically or horizontally, depending on the use case and layout structure. For better readability, arrange radio buttons vertically whenever possible.

| Vertical | Horizontal |
| --- | --- |
|  |  |

#### Modifiers

##### Border

Radio button groups can also be used with or without a border. Add a border if you want to emphasize the options more clearly. Borders can also help to distinguish each radio button.

| Without border | With border |
| --- | --- |
|  |  |

| DO |
| --- |
|  **DO:** Use radio buttons without borders when the radio button group is simple and the options are easily distinguishable without added visual emphasis. |
|  **DO:** Use borders around radio button groups when you want to clearly distinguish options, especially in complex forms. Borders help visually separate each option, making it easier for users to scan and understand their choices. |

##### Columns

Vertical radio button groups are available in one or two columns.

| One column | Two columns |
| --- | --- |
|  Single columns are used for concise layouts with fewer options, especially on mobile devices or when vertical space is limited. |  The two-column layout is used when presenting more options (6 or more) to efficiently use space, improve scannability, and facilitate comparison. It is especially useful for desktop interfaces. |

##### Header

Like all form components, radio button groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the form guidelines for more information.



---

## rating

_From `components/rating/rating.md`._

#### Size

The rating is available in two different sizes. The choice of size depends on the layout and the desired prominence of the rating.

| L | S |
| --- | --- |
|  |  |

#### Condensed display

The rating can be condensed to a single star or shown in full with all the stars. Which version you use depends on how much space is available in the layout.

| Full | Condensed |
| --- | --- |
|  |  |

| DO |
| --- |
|  **DO:** Use the condensed variant when space is limited. |
|  **DO:** Use the full version when enough space is available. |

| DON'T |
| --- |
|  **DON'T:** Don't hide the rating amount when using the condensed variant. |

#### Modifiers

The following elements are optional and can be hidden: Number of ratings, user rating and maximum rating (e.g., "/5"). When hiding elements, make sure the context is still understandable.

| All elements | Hidden maximum amount of rating | Hidden rating | Hidden reviews | Hidden rating and reviews |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

---

## score-tag

_From `components/score-tag/score-tag.md`._

#### Type

##### Diamond, Gold, Silver, Bronze

Four variants. **The tier sets the icon, the label text and both colours
together.** Icon and colour cannot be set apart from the tier on either
platform; only the label can be replaced, and only on web.

**The design and the build disagree on the default.** The component set opens on
`Diamond`; the web build defaults to `bronze`. Neither is wrong, and **set the
tier explicitly rather than rely on either default.**

| Type | Icon | Label | Surface token | Content token |
| --- | --- | --- | --- | --- |
| **Diamond** | `gem` | Diamond | `color.surface.score.diamond` | `color.content.score.diamond` |
| **Gold** | `trophy` | Gold | `color.surface.score.gold` | `color.content.score.gold` |
| **Silver** | `medal` | Silver | `color.surface.score.silver` | `color.content.score.silver` |
| **Bronze** | `award` | Bronze | `color.surface.score.bronze` | `color.content.score.bronze` |

_Each variant binds its surface and content colour to the token named above._

#### Modifiers

Not documented

_The component has one property, `Type`. There is no size, no emphasis and no
icon slot. The label cannot be hidden; on web it can be replaced._

##### What the inner Tag is fixed to

Every tier wraps the same `Tag` configuration: **Primary**, font size **14**,
hierarchy **Strong**, with the left icon shown and the label shown.

**The inner `Tag` is not exposed.** A designer placing a score tag cannot reach
those settings through the parent, which is what makes the four tiers fixed
rather than merely conventional.

## segmented-control

_From `components/segmented-control/segmented-control.md`._

#### Modifiers

##### Icons

Icons can be added as visual cues to provide clarity to the user. The icon is always to the left of the label.

| Icon only | Icon left | No icon |
| --- | --- | --- |
|  |  |  |

| DO | DON'T |
| --- | --- |
|  **DO:** Combine icons with text for clarity. |  **DON'T:** Avoid mixing different combinations. |

##### Badges

A badge can be placed next to the label.





---

## select-card-group

_From `components/select-card-group/select-card-group.md`._

#### Group

Select cards are available as a group or individual select cards.

| In a group | Individual card |
| --- | --- |
|  |  |

#### Type

Select cards are available as single or multi-selection component. The multi-selection variant contains a checkbox, the single-selection one doesn't contain an indicator.

| Single-select (radio) | Multi-select (checkbox) |
| --- | --- |
|  |  |

#### Alignment

The content inside select cards can be in a vertical or horizontal alignment, depending on the use case and layout structure.

| Vertical | Horizontal |
| --- | --- |
|  |  |

#### Modifiers

##### Icons and illustration

Select cards contain optional icons and illustrations. The illustrations are available in the size 40 and 64px. If you use an illustration we recommend the usage of pictograms.

| Icon | 40px illustration | 64px illustration |
| --- | --- | --- |
|  |  |  |

| Icon | 40px illustration | 64px illustration |
| --- | --- | --- |
|  |  |  |

##### Title and description

The select cards contain a mandatory title and an optional description, that can be added to provide additional explanations.

---

| With description | Without description |
| --- | --- |
|  |  |

## slider

_From `components/slider/slider.md`._

#### Modifiers

##### Display the selected value

The slider value should always be visible to the user. By default, it can be displayed on the top right of the component.

The value can be hidden if displayed in another place on the screen or if the selection value is visible in live such as when cropping an image.




##### Display the min and max value

The minimum and maximum selectable value can be displayed on the left and right of the slider.

Those values are mandatory when selecting a numeric value but not for other use cases such as sound level selection slider.




##### Display the steps marks

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.




##### Display the steps values

If your slider only allow predefined value, they should be displayed. Additionally, you can display the steps value.




##### Display the text fields

When a numeric value is selectable, you can display the text field, allowing user to write directly the requested value. This is strongly recommend when a precise value such as the monthly revenue. When the text field is displayed, the selected value is hidden.




##### Display the header

When used as a form element, you can display the form header, including the tooltip trigger, required and/or optional mentions and the helper text.




---

## snackbar

_From `components/snackbar/snackbar.md`._

#### Type

Snackbars come in the following types: info, success, warning, and error. These variations help users quickly understand the nature of the message, whether it's informational, confirms success, issues a warning, or highlights an error.

| Info | Success | Warning | Error |
| --- | --- | --- | --- |
|  |  |  |  |

The icons associated with each snackbar type are standardized and shouldn't be changed to ensure consistency and clarity across our products.

#### Actions

Snackbars contain optional action buttons. Short actions appear on the same line as the snackbar message, longer actions appear below the snackbar message.

| Short action | Long action | Without action |
| --- | --- | --- |
|  |  |  |

#### Modifiers

Not documented

---

## state-message

_From `components/state-message/state-message.md`._

#### Type

##### Helper, Information, Success, Warning, Error

Five types. `Helper` is the default. **The type sets three things at once** — the
icon, the content colour, and the gap between icon and text.

| Type | Icon | Colour token |
| --- | --- | --- |
| **Helper** | **None** | `stateMessage.color.helper.content` |
| **Information** | Filled circle, info | `stateMessage.color.info.content` |
| **Success** | Filled circle, check | `stateMessage.color.success.content` |
| **Warning** | Filled circle, exclamation | `stateMessage.color.warning.content` |
| **Error** | Filled circle, close | `stateMessage.color.error.content` |

_The design and the build agree on all five. The design's `Helper` form holds a
16 spacer where the others hold an icon; the web build renders nothing there._

**The gap is per type**, not a single value — the component reads
`stateMessage.spacing.<type>.gap`. As drawn, the row's gap is 8.

#### Modifiers

##### Icon

**The icon is not selectable.** It follows the type, and there is no way to
change it, remove it from a type that has one, or add one to `Helper`.

Icon size is 20, bound to `sizing.20` on web, for the four types that have one.

## tables

_From `components/tables/tables.md`._

Table variants are either Device or Feature driven so it adapts to different use cases:
* **Device:** Desktop, Phone/Tablet
* **Selectable rows:** Functionality to enable rows that can be selected individually or in bulk from the Header
* **Expandable rows:** Functionality to enable rows that can be expanded thanks to a button so it displays a bigger panel with more contextual data
* **Horizontal scroll:** Functionality to enable data sets within columns to overflow the Table container and scroll horizontally
* **Full width (Phone/Tablet only):** Reserved for Phone and Tablet devices — to maximize screen real estate the Table component gets "unboxed" so it can be expanded to the full width of the screen

#### Device


There is a Desktop and a Phone/Tablet version of the Table

Tables for mobile devices have two ways of presenting the data within the rows:

| Horizontally distributed | Stacked |
| --- | --- |
|  |  |

But also can be aligned to the full-width of the device, making the most out of the available space:

| Horizontally distributed full-width | Stacked full-width |
| --- | --- |
|  |  |

##### Phone / Tablet Guidelines

| DO |
| --- |
|  **DO:** Tables can have the same appearance as on Desktop devices, having a boxed Table as one of our Phone/Tablet views. |
|  **DO:** To make the most out of the space on the screen, mobile device Tables can be aligned to the full-width of the screen. |
|  **DO:** As normally the content of the tables won't fit in smaller devices, besides scrolling horizontally to display more data, optionally you can stack the content of a whole row vertically. |
|  **DO:** Also expand the Table to the full-width for better readability. |
|  **DO:** When using the full-width Table for mobile devices, make sure that in case you have the footer, you must have the padded version. |

| DON'T |
| --- |
|  **DON'T:** You can't combine the stacked row view with the horizontal scroll. |

#### Selectable rows

To facilitate the selection of rows you can implement the selectable rows variant.



| DO | DON'T |
| --- | --- |
|  **DO:** When adding the functionality of selecting rows in a table, it is implemented to all rows by default. |  **DON'T:** The Header of the table should have a Checkbox to facilitate selecting/unselecting all rows — don't randomize the functionality of selecting rows in a table, without context users won't be able to understand why some rows can be selected and others don't. |

#### Expandable row

You might need rows that can expand in order to show and hide contextual data. For this purpose you can use the Expandable row variant, which is NOT available for mobile Tables as the interaction of this type of row might be difficult to interact with on smaller devices.



| DO |
| --- |
|  **DO:** When adding expandable rows, try to have the same functionality for all rows. |

| CAUTION |
| --- |
|  **CAUTION:** Without context, users might not know why some rows can't be expanded. Only mix the functionality when you know why. |

#### Horizontal scroll

For very complex data sets that need a large number of columns to display, this variant allows the content of the rows to overflow the container — a shadow on the edges appears to depict the overflowing content.



| DO |
| --- |
|  **DO:** When the content of the Table can't be fitted inside the Table container, enable "horizontal scroll" — a shadow will appear to help the user notice there's more content underneath. |

#### Modifiers

##### Sub-components and padding

There are a few types of Tables, but the primary elements that constitute the Table component are as follows:



| Sub-component | Enable/Disable capability | Padding |
| --- | --- | --- |
| Header row | Yes | Left, Right: 12px, 16px, 20px |
| Header cell | Yes | Left, Right: 12px, 16px, 20px |
| Sorting button | Yes | N/A |
| Additional info button | Yes | N/A |
| Table row | N/A | Top, Down, Left, Right: 12px, 16px, 20px |
| Table cell | Yes | Left, Right: 12px, 16px, 20px |
| Footer | Yes | Left, Right: 0px, 16px |
| Footer Legend | Yes | N/A |
| Pagination | Yes | N/A |

##### Padding options

The set of spacing available for this component is limited, as the sub-component table above records. You can combine a set of 12, 16 and 20px spacing units. Just make sure the spacing is balanced and consistent throughout the table.

###### Example


12px gap between cells in the Header


12px gap between fixed cells and the rest


12px gap between cells and 16px padding top and bottom of the row


Other padding can be used within the cell content. E.g.: 8px

##### Sorting

Sorting helps users order the data on the Table based on that column's values, from highest to lowest or from lowest to highest. Clicking the sorting button first sorts highest to lowest, clicking again sorts lowest to highest, and clicking a third time returns to the default sorting. This functionality and the icon that enables it can be disabled and hidden.


Sorting and info features enabled


Sorting icon changes depending on the sorting direction

##### Info

The info icon gives contextual information about the data visible in that column. Just like any other info icon across the product, on hover or tap (mobile) it displays a tooltip with additional information. This functionality and the icon that enables it can be disabled and hidden.


Activating the info icon displays a tooltip


Both features can be disabled

##### Header placement

| DO | DON'T |
| --- | --- |
|  **DO:** Keep the Header at the top of the Table. |  **DON'T:** Don't place the Header in between rows. |

| CAUTION |
| --- |
|  **CAUTION:** Alternatively you can have a Table without a Header. Use it carefully — Tables without a header are reserved for simple tables where each column's data point can be understood by the user without context. |

---

## tabs

_From `components/tabs/tabs.md`._

#### Number of items

Tabs are available with 2 to 5 elements. We don't recommend using more than this to avoid overwhelming the user.

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- |
|  |  |  |  |

#### Modifiers

##### Icons

Icons can be positioned on the left or on top of the tab.

| DO |
| --- |
|  **DO:** On smaller screens with limited space, place the icons at the top to avoid scrolling. |
|  **DO:** On wider screens, position the icons on the left. |

| Without icons | With icons left | With icons on top |
| --- | --- | --- |
|  |  |  |

##### Badge

A badge can be placed next to the tab label.

| DO |
| --- |
|  **DO:** Use badges to indicate notifications or updates. For example, for messages or alerts. |

---



## tag

_From `components/tag/tag.md`._

#### Context / Style

Tags are available in a variety of styles to suit different visual contexts and hierarchies. They are available in the following contexts: Dark, Subdued, Primary, Secondary, Light, Error, Success, Information, and Warning. The choices of style depends on the purpose and the importance of the tag.

| Dark | Subdued | Primary | Secondary | Light | Error | Success | Information | Warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

| DO |
| --- |
|  **DO:** Use tags with different emphasis to indicate the level of importance. |
|  **DO:** Use tags to communicate the status of items. |

#### Modifiers

##### Icons

Icons are optional and can be included to provide additional context or visual cues that make the purpose of the tag more intuitive and easier to understand.

| With icon | Without icon |
| --- | --- |
|  |  |

##### Label

We recommend to use the tag with a label for most use cases. Only use it without a label when the icon is universally recognized.

| With label | Without label |
| --- | --- |
|  |  |

---

## text-area

_From `components/text-area/text-area.md`._

#### Modifiers

##### Header

Like all form components, text areas contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.



Text areas should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

##### State message

State messages can be used to provide additional information or feedback on the usage of the text area.

On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

More information:
* Guidelines on form validation and displaying errors
* Content guidelines for state messages

##### Icons and suffix

Unlike the text field, the text area does not contain any icons or suffixes.

##### Character counter

A character counter can be added to display the number of characters entered and the total number of characters allowed.



Depending on the platform, there is different behavior when the character count is exceeded.

| Web | Android | iOS |
| --- | --- | --- |
|  The counter goes into an error state. |  The entire field goes into an error state and an error message is displayed. |  It is not possible to type in more characters than are allowed by the character limit. |

##### Resize handle

Only on Web the text area contains a resize handle. It allows the user to change the height of the field. It is not possible to change the width of the field with the handle. It's also not possible to make the field smaller than the min-height (96px).

On Android, the field automatically grows if the content is longer than the field.

On iOS, the field has a fixed height. The user cannot resize the field.

| Web | iOS | Android |
| --- | --- | --- |
|  |  |  |

---

## text-button

_From `components/text-button/text-button.md`._

#### Colour variant

##### Default, danger and inverted

Three variants, `default` by default. Each sets four label colours — resting,
hover, pressed and disabled.

| Variant | When to use it |
| --- | --- |
| **Default** | Every case the other two do not cover |
| **Danger** | The action erases or deletes |
| **Inverted** | On a dark surface. **A visual choice only** — it carries no meaning about the action |

#### Size

##### 14 and 16

Two sizes, `14` and `16`, being the label's type size in pixels. Default `16`.
**The overall height does not change with size** — it is fixed at 40px in both.
No rule for choosing is documented.

#### Modifiers

##### Icon

An icon may sit before the label, after the label, or replace it entirely. The
icon is 24px in every case, with a gap between it and the label.

**Icon-only has two constraints the other placements do not have:** it is
available at size 16 only, and the label must still be written, because it
becomes the control's spoken name.

##### Going to an address

A text button can behave as a button, or as a link to an address that may open
in a new tab.

**The capability exists; the selection rule does not send you to it.** A control
that leaves the page is `Link`'s job, because a link is underlined and the
underline is what tells the user it takes them somewhere.

**Where a text button is used as an external link even so, the external-link
icon is mandatory** — the same rule `Link` follows. **The component does not
supply it**: setting the address as external adds a spoken "opens in a new tab"
and nothing visible, so the icon is placed through the icon slot at the end.

##### Acting on a form

A text button can be set to submit or reset a form it belongs to.

**It should not be the control that does either.** Submitting is the form's main
action, so it takes `Button` at **primary** emphasis. A reset or a cancel beside
it takes a lower emphasis — see `Button`'s own emphasis table, which holds
primary to one per section.

## text-field

_From `components/text-field/text-field.md`._

#### Modifiers

##### Header

Like all form components, text fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. See the form guidelines for more information.



Text fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

##### State message

State messages can be used to provide additional information or feedback on the usage of the text field. On the web, the state message is only used to indicate errors. On iOS/Android, all types of state messages (information, success, warning, error) are available.

| Error (Web, iOS, Android) | Information (iOS/Android) | Success (iOS/Android) | Warning (iOS/Android) |
| --- | --- | --- | --- |
|  |  |  |  |

More information: Guidelines on form validation and displaying errors · Content guidelines for state messages

##### Icons

Icons can be added as visual cues to provide clarity to the user. Icons on the left are non-clickable. Icons on the right can be clickable (icon button) or non-clickable.

| Left | Right | Left and right |
| --- | --- | --- |
|  |  |  |

| DO |
| --- |
|  **DO:** Use non-clickable icons to provide visual cues to the user. |
|  **DO:** Use clickable icon buttons for actions related to the text field, such as deleting the contents of the box. |

##### Suffix

The suffix can be added to provide additional context or constraints for the user input.

| DO |
| --- |
| <br>**DO:** Use the suffix for measurements, currency, or contextual information. |



| DO |
| --- |
|  **DO:** Use the suffix for measurements, currency, or contextual information. |

---

## toggle

_From `components/toggle/toggle.md`._

#### Toggle position

Toggle can be positioned on the left or on the right depending on the use case.

| Left | Right |
| --- | --- |
|  |  |

#### Modifiers

Toggles have the same elements as all form components:
* Required asterisk to the right of the label (visible by default)
* Optional mention to the right of the label
* Tooltip to the right of the toggle label

See the form guidelines for more information.

| Optional | Required | Tooltip |
| --- | --- | --- |
|  |  |  |

---

## toggle-group

_From `components/toggle-group/toggle-group.md`._

#### Modifiers

##### Toggle position

Like standalone toggles, toggle groups can also switch from a toggle left position to a toggle right position, depending on use case and layout.

| DO | DON'T |
| --- | --- |
|  **DO:** All toggles in a toggle group should have the same position. |  **DON'T:** Don't mix positions in the same toggle group. |

| Left | Right |
| --- | --- |
|  |  |

##### Header

Like all form components, toggle groups contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text. Go to the form guidelines for more information.

---



## tooltip

_From `components/tooltip/tooltip.md`._

#### Placement

##### Bottom, top, left and right

Four sides, `bottom` by default. The arrow follows the side, sitting against the
edge nearest the trigger.

**The requested side is not always the side used.** The component asks for a
position, then reads back where the panel was actually placed, and points the
arrow at wherever that turned out to be.

#### Alignment

##### Start, middle and end

Three positions along the chosen side, `middle` by default. On the left and
right sides, `start` and `end` mean top and bottom.

#### Modifiers

##### Offset

The gap between trigger and panel can be adjusted, and **may be negative**,
which is how an enlarged touch zone around a trigger is compensated for. No rule
for when to adjust it is documented.

## top-bar

_From `components/top-bar/top-bar.md`._

#### Size

Top bars are available in small and medium sizes. The small variant is best for compact layouts or secondary pages where vertical space is limited. The medium variant is ideal for primary pages or sections where emphasizing the title is important for clarity and hierarchy.

| Small | Medium |
| --- | --- |
|  |  |

#### Style

Top bars come in two styles: default and on picture. The default style works well on plain backgrounds, providing a clean and simple appearance. The on picture style is designed for use over images or visual elements, maintaining readability while blending seamlessly with the background.

| Default | On picture |
| --- | --- |
|  |  |

| DO |
| --- |
|  **DO:** Use the default variant on pages with a plain background. |
|  **DO:** Use the on picture variant on top of images. |

#### Modifiers

##### Icons and actions

The top bar contains optional icons and an optional button.

| With icons | With icons | With icon and button | Without icon or button |
| --- | --- | --- | --- |
|  |  |  |  |

##### Title

The small title in the medium top bar is optional. We don't recommend hiding the title in the small top bar, except for the on-picture variant, to help users understand their current location.

| With small title | Without small title |
| --- | --- |
|  |  |

##### Badge

A badge can be placed next to the title. They can be used to indicate notifications or updates. For example, for messages or alerts.




#### Scroll behaviour

On the web, consumers can choose whether the top bar stays fixed at the top or scrolls with the content. On iOS and Android, the top bar always stays on top.

| Fixed on top | Scrolls with content |
| --- | --- |
|  Web and app |  Web only |

---

## wizard

_From `components/wizard/wizard.md`._

#### List type

The wizard list is available as an unordered or numbered list.

| Unordered list | Numbered list |
| --- | --- |
|  |  |

**Unordered list:** Used when the user needs the flexibility to jump between steps without following a strict sequence. This variant is suitable for tasks where the order of completion is not critical.

**Numbered list:** Used when processes must be completed in a specific order, where each step depends on the completion of the previous one. This variant is suitable for tasks where linear progress is crucial.

#### Modifiers

##### Description

The description is optional.

| With description | Without description |
| --- | --- |
|  |  |

---
