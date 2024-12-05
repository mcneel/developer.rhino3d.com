+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Layouts"
description = "An overview of layouts in Eto"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

<!-- Spacing, Padding (using nulls to space things out!) all the good stuff  -->

### Spacing
Multi-control containers in Eto will have a `Spacing` property, which add space vertically and horizontally _between_ controls.

### Padding
Single and multi-control containers in Eto will have a `Padding` property, which add space _around_ controls.

{{< row >}}
{{< column >}}
  #### Spacing
  ![Spacing](/images/eto/spacing.png)
{{< /column >}}
{{< column >}}
  #### Padding
  ![Padding](/images/eto/padding.png)
{{< /column >}}
{{< column >}}
  #### Spacing & Padding
  ![Spacing & Padding](/images/eto/stack-layout.png)
{{< /column >}}
{{< /row >}}


## Spaces
When working with multi-control Containers in eto, adding in extra spacing, i.e "a nudge", adding empty spaces can be achieved through the use of `Null`.

<!-- Table Layout -->
<!-- Stack Layout -->
<!-- Dynamic Layout -->

<!-- Dynamic Layout null spaces-->