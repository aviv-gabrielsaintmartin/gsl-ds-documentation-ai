<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3433955377/Energy+Tag | Last modified: Aug 21, 2026 -->

# Energy Tag

Energy tags are used to indicate the energy efficiency of properties.

![](images/ce59970630d0d71fe178ce.png)

| Figma | Web | iOS | Android |
| --- | --- | --- | --- |
| [Energy tag on Figma](https://www.figma.com/design/xxqSJcKOphrgimxRQbvtfe/2.-Gemini-Components-Library?node-id=4612-2541) | To Do 🚧 | To Do 🚧 | Ready ✅ |

---

## Usage

Energy tags serve as a visual indicator to quickly communicate the energy efficiency of a property. Each tag consists of a letter and a color code, providing a standardized, at-a-glance indicator of a building's energy performance.

![](images/b1ba138b531dc540f4b14f.png)

### When to use

**Energy tag** — property energy efficiency ratings **only**. Use the correct country/region variant.

### When NOT to use

| Instead, when… | Use |
| --- | --- |
| A general status label, not a property energy rating | **Tag** |
| Seller lead scoring | **Score tag** |
| The element is interactive | **Chip** |

### Variant Selection Flow

```
Country or region — dictated by where the property is, never a design choice
├─ France → French variant
├─ Germany → German variant
├─ Austria → Austrian variant
├─ Belgium, Brussels → Brussels variant
├─ Belgium, Flanders → Flanders variant
└─ Belgium, Wallonia → Wallonia variant

Unsupported markets
└─ Switzerland and others have no energy tag — never substitute another country's
```

### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/6c8baef751aea1a1abd32c.png) **DO:** Use energy tags in property-related interfaces to allow potential buyers or renters to consider energy performance in their decision making. | **DON'T:** Don't use energy tags to represent non-energy ratings, such as reviews, quality scores or customer satisfaction levels. |

### Related Components

| Component | Priority | Usage | Example Scenario |
| --- | --- | --- | --- |
| **Energy tag** | — | Energy tags display property energy efficiency ratings. Use the correct country/region variant. | — |
| [**Tag**](../tag/tag.md) | High | Non-interactive component for fixed information such as labels, categories, or statuses. | A general status label, not a property energy rating |
| **Score tag** | Medium | A Tag specialised for seller lead scoring. | Seller lead scoring, not energy efficiency |

---

## Variants & Modifiers

### Country

Energy tags vary by country and region, reflecting local standards for energy efficiency. Please note that in Belgium there are three different systems for Brussels, Wallonia and Flanders.

#### France

![](images/92890980f2bafec86711e7.png) ![](images/8d33a796182efc5b8bedbd.png) ![](images/312e30808e5223fd439d2f.png) ![](images/82fd449a59b50df8032a75.png) ![](images/9d0d2eefceace54fe3b534.png) ![](images/df521581442dc939a56ef7.png)

#### Germany

![](images/2647e9b08a0435ebabb421.png) ![](images/7de8608d96b76e0fe2b906.png) ![](images/9061c23eac617da2c4d7cc.png) ![](images/4a48bbff55fc4fbf2613d5.png) ![](images/e7d5799b573f34104be43a.png) ![](images/0887a41106567b97296a30.png) ![](images/b9ddda227fd2b5f1e2d49f.png) ![](images/bbbb7c4809d1e9e6e30f53.png)

#### Austria

![](images/0d08e2f1ac5506253b6da3.png) ![](images/c848bd852fe9e13c239d58.png) ![](images/ab3b88cd66ce50f9aadefe.png) ![](images/7966178a9d197eafc2c561.png) ![](images/645f89f7459a672731483c.png) ![](images/f49b39014d8258484c81e7.png) ![](images/1d135fd212dd0baf982028.png) ![](images/8c4955b7651e28cb6db4c1.png)

#### Brussels (Belgium)

![](images/82ad8b9488368b26d7039b.png) ![](images/90ae19c58f9a4839e3744e.png) ![](images/0fa72ec597ca7417ca1b3a.png) ![](images/18dfeb027336f33eaff91b.png) ![](images/3481c7306c694ccdb40bd7.png) ![](images/443acc9b67cedfcb4c44f6.png) ![](images/85fed5b3c6fc885a979e07.png)

#### Flanders (Belgium)

![](images/34d710d72c20cadd7f49d6.png) ![](images/6369eee5ea2a3337b1528c.png) ![](images/c2ab91b77d596189b677aa.png) ![](images/934c8a677e39edbf468c1d.png) ![](images/e1a40056ae8ebac02fe9b0.png) ![](images/2e265877f2e97c2fe7b093.png) ![](images/c0b4c46eb61cf5210a6b8d.png)

#### Wallonia (Belgium)

![](images/bb020fc0280fa5407d8aed.png) ![](images/f8ccbf5916640b6404dab6.png) ![](images/2cd21dd609c7b725f160cf.png) ![](images/aa653f9ea28db3b4892aed.png) ![](images/6f8d343b8e512ee12667f8.png) ![](images/b749c28d7c8df01c219a75.png) ![](images/0107ac25bdd5b32ff51490.png) ![](images/b53268f4661c4786f0610e.png) ![](images/9c70404ab0df831f6c26d2.png)

We don't currently support energy tags for other countries, such as Switzerland.

### Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

This component has no interactive states. It is a static, display-only element with no hover, focus, pressed, loading, or disabled behavior.

### Touch Target & Layout

Not applicable. This component does not respond to touch or pointer interaction and has no minimum touch target requirement.

### Breakpoints & Platform Adaptations

Not applicable. This component does not adapt its layout or behavior across breakpoints or platforms.

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
