<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832465961/Avatar | Last modified: Aug 13, 2026 -->

# Avatar

Avatars represent user profiles of agencies, agents, private sellers and seekers.

![](images/tzzux_iIi19kcr1hdcYcRg.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| Ready ✅ | Ready ✅ | Ready ✅ | Partially available 🚧 |

* [Avatar on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=3-7303)
* [Avatar on Storybook](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/ui-content-avatar--docs)

---

## Usage

Avatars help users identify agencies, agents, private sellers or seeker. They can include logos, images, icons, or initials. They come in two shapes (square and circle) and several sizes.

### When to use

**Avatar** — representing a user, agent, agency, or seeker. Circle for individuals, square for agencies.

### When NOT to use

**No alternative.** Nothing else in the system covers this — see [components-rules-ai.md](../components-rules-ai.md).

### Variant Selection Flow

```
Shape
├─ An individual — agent, seeker, private owner → Circle
├─ An agency or company → Square
└─ An AVIV intermediary agent's logo of unpredictable ratio → Rectangular, adaptive

Size
└─ Any existing size from 24 to 128px
   └─ Never scale or reshape an avatar to a size that is not offered

Padding and border
├─ Sits directly on a busy or image background → With padding and/or border
└─ Sits on a plain surface → Without

Fallback when no image is available
├─ Circle or square → Icon or initials (building icon for agencies)
└─ Rectangular adaptive → No fallback exists; an image must be supplied
```

### Usage Guidance

Not documented

### Related Components

**No overlapping component.** Nothing else in the system covers representing a user, agent, agency or seeker. Avatar is chosen directly — see [components-rules-ai.md](../components-rules-ai.md) Rule 1, *Identity and media*.

---

## Variants & Modifiers

### Shapes and sizes

The avatar is available as a circle or square in sizes between 24 and 128px.

#### Circle

| 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 104 | 128 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](images/e6ada9dab0a9bc2b37537a.png) | ![](images/3166f43105b6b69345cd35.png) | ![](images/f3b7284ae6d9585d4a7b2d.png) | ![](images/593c59942f1e0ab6e81b62.png) | ![](images/eaffe81064827a831cc676.png) | ![](images/74106b5496aa7c4c8ca782.png) | ![](images/3ea1401d5d01a3bf9f85ff.png) | ![](images/b46a0eea2b3f783dbdee17.png) | ![](images/290810fd73a7fbc1ae8f52.png) | ![](images/23fa6bcb4e140f7dcd75f1.png) |

#### Square

| 24 | 32 | 40 | 48 | 56 | 64 |
| --- | --- | --- | --- | --- | --- |
| ![](images/4909109b9b66e765e86bb5.png) | ![](images/bee01687d68b42c68bc797.png) | ![](images/c6a6f404d191b0bae7e4d0.png) | ![](images/edfb0fd980fdbcc7d7fe35.png) | ![](images/84f7ce7997e26c1fc3ef51.png) | ![](images/5e80fe9bf9aafd588c9460.png) |

| 72 | 80 | 104 | 128 |
| --- | --- | --- | --- |
| ![](images/c83c66f7a997cd8056eba5.png) | ![](images/eb7f3b60ad799249754ae1.png) | ![](images/9bab0c14884b4e588d0369.png) | ![](images/4335d78a3a4a6f918ac12d.png) |

#### Rectangular, flexible

| Rectangular without stroke | Rectangular with padding and stroke | Rectangular with stroke |
| --- | --- | --- |
| ![](images/e393be16d3138b886874fb.png) | ![](images/9003668cf074a284c70081.png) | ![](images/bde75fe4880fa27fdb5c76.png) |

| DO | DON'T |
| --- | --- |
| ![](images/2823406288571eb74cd2b5.png) **DO:** Use the avatar in one of the available sizes and shapes. | ![](images/780aa2fb05d8390252a9ba.png) **DON'T:** Don't scale or change the shape of the avatar. |

| DO |
| --- |
| ![](images/d897cb50a74f080115994c.png) **DO:** Use the circle for individuals such as agents, seekers, and private owners. Use the square for agencies. |

### No padding

All avatar sizes are available with and without padding.

### No border

All avatar sizes are available with and without border.

### Icons and initials

Icons or initials can be used as a fallback if no image or logo is available.

| DO | DON'T |
| --- | --- |
| ![](images/b4f2e3d1a4d1b21f879683.png) **DO:** If an image is not available, use icons or initials. We recommend using the building icons for agencies and the user icon or initials for individuals such as agents, private sellers, or seekers. | ![](images/265473aaebaabe296fe8bd.png) **DON'T:** Don't use any other illustrations or emojis. |

### Rectangular, adaptive avatar

This Avatar variant's goal is to, within certain limits, adapt to the logo ratio of AVIV Intermediary agents. That way the agent's logo can be better represented within the AVIV platform without size or ratio constraint limitations.

#### Specs

The avatar size and ratio adapts to the user's choice of image (in this case, logo). However, to ensure a stable experience, we've introduced a set of maximum and minimum width and height — depending on the logo ratio, if either the width or the height hits the maximum or minimum, it will stay at that size.

![](images/U-_u0IvIImRicE9FaEB59w.svg)

Max. and min. sizes

![](images/l6RR95-gzQBODVsi31ziyg.png)

Examples with real logos

![](images/RddWg7QtkCHLhrT5RzywsQ.png)

**DON'T:** Rectangular avatars don't have icons or initials fallback.

---

## Behavior & Responsiveness

### Interactive States & Loading

Not documented

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
