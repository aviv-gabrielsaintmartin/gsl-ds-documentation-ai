Four types of color palettes are available for data visualization: qualitative, sequential, diverging, and semantic.

---

## Accessibility (a11y)

> ℹ️ Our color palettes are fully accessible to color-blind people.

To achieve this, we based our design on several resources like the work of [Paul Tol](https://personal.sron.nl/~pault/) who created several color-blind palettes, or [ColorBrewer](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) who proposes palettes dedicated to maps.

Our palettes are tested using tools like [Viz Palette](https://www.susielu.com/data-viz/viz-palette).

---

## Variants & Modifiers

### Categorical

A categorical color palette consists of visually distinct colors representing discrete categories or groups.

Each color in the palette is selected to be easily distinguishable from the others, ensuring that categories are identifiable.

![](images/83d3a206a5020bfd0fc609.png)

![](images/1b16e49bafc3f3cccd5e3d.png)

#### Color order

> ⚠️ Don't change the color order as it's made to ensure a good differentiation between color.

| 01 bar | 02 bars | 03 bars | 04 bars | 05 bars |
| --- | --- | --- | --- | --- |
| ![](images/5c9aa6a664f7b090df2980.png) | Image unavailable | ![](images/f490d99412fbc433245a17.png) | ![](images/d9138e0681063e55805dd7.png) | ![](images/ad40f1ae8c1f4d132808bf.png) |

| 01 line | 02 lines | 03 lines | 04 lines | 05 lines |
| --- | --- | --- | --- | --- |
| ![](images/3dac8f58e6288a20b6b53c.png) | ![](images/78dd27e9db32381a7bc2e8.png) | ![](images/3008ad63ffcabdfa998601.png) | *Image unavailable* | ![](images/98e5d4c82657a586383ce5.png) |

| 02 slices | 03 slices | 04 slices | 05 slices |
| --- | --- | --- | --- |
| ![](images/bc1016794783007f26958b.png) | ![](images/f324331331f185aefa41a6.png) | ![](images/84b7ff7e37b1b318d761d6.png) | *Image unavailable* |

#### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** If colors don't aid in understanding the graph or compete with the same value, stick with the default color for each bar. | **DON'T:** Use different bar colors when competing against the same measure (e.g. K/€). Exceptions are only allowed when colors have a specific meaning (e.g. red for Se Loger, blue for Immonet, yellow for Immowelt...). |

| DO |
| --- |
| **DO:** Highlight the best-performing data point — use the disabled color to reduce emphasis on less important parts, while sticking to the default color to emphasize critical information. |

### Sequential

A sequential color palette is a set of colors arranged in a progressive order, typically based on a single hue or a related range of hues.

This is used to visualize data that follows a natural progression or order, like time series data, temperature gradients, or any dataset where values exhibit a clear increase or decrease.

Use a sequential color scale for a more intuitive reading than a diverging palette.

> ℹ️ Please note that sequential palettes in dark mode work the other way, dark to light.

![](images/6c1399267109e3f91da596.png)

![](images/729a712b25a3e3a1b8e9e4.png)

![](images/4bd2b5652c7ed8c6d71a16.png)

![](images/004f99c43cb7a9031e765d.png)

### Diverging

A diverging palette is the optimal choice for a numerical variable with a central value, such as zero.

It combines two sequential palettes that share the same endpoint at the central value. Larger values are represented by colors on one side, while smaller values are depicted by colors on the other side.

Use a diverging palette:
* If there's a meaningful middle point
* To emphasize the extremes
* To let readers see more differences in the data

Diverging color palettes offer precision but may not be as intuitive to comprehend as sequential palettes.

> ℹ️ Please note that diverging palettes do not differentiate between light and dark themes.

![](images/ba052c58bd58d594aee3e9.png)

![](images/daf342e057402de39bdfe4.png)

### Semantic

A semantic color palette is a collection of colors assigned with specific meanings or associations to represent distinct concepts, categories, or states clearly and intuitively.

![](images/5e9b7b7f3bbd15ca4af884.png)

![](images/9e6cb6c9a3a542e72b15b7.png)

#### Usage Guidance

| DO | DON'T |
| --- | --- |
| ![](images/09abf640ed06a36cec004e.png) **DO:** Use icons, tags or any other elements that don't need color to be understood. | ![](images/8f2de4eaf0df6bdf4e99ee.png) **DON'T:** Rely on color alone to give meaning — green and red can be the same color for some types of color-blind issues. |

---

## Resources

* [Which color scale to use when visualizing data](https://blog.datawrapper.de/which-color-scale-to-use-in-data-vis/#categorical-color-scales) by DataWrapper
* [How to choose colors for data visualizations](https://www.atlassian.com/data/charts/how-to-choose-colors-data-visualization) by Atlassian
* [Colors for data visualization](https://spectrum.adobe.com/page/color-for-data-visualization/) by Adobe
* [Carbon Design Color palettes](https://carbondesignsystem.com/data-visualization/color-palettes/#categorical-palettes) by IBM
* [The economist Dataviz guidelines (PDF)](https://design-system.economist.com/documents/CHARTstyleguide_20170505.pdf)
* [Friendly color blind palettes](https://personal.sron.nl/~pault/) by Paul Tol
* [Color brewer map color palettes](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)
