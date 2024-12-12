+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Sizing"
description = "An overview of Sizing in Eto"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++
<!-- Sizing, automatic, manual etc. -->

## Explicit Sizing
Sizes can be declared explicitly in eto.

{{< row >}}
{{< column >}}

``` cs
using Eto.Forms;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog()
{
  Width = 100,
  Height = 100
};

dialog.Content = new Button() { Text = "Button" };
dialog.ShowModal(parent);
```

Declaring sizes forces Eto to use the sizes you give.

<!-- TODO : Add Python sample -->

{{< /column >}}
{{< column >}}

  ![Explicitly Sized Button](/images/eto/controls/explicit-button.png)

{{< /column >}}
{{< /row >}}


## Implicit Sizing
If no sizes are declared, or if the sizes declared are `-1`, Eto will auto-size controls, containers and windows.

{{< row >}}
{{< column >}}
``` cs
using Eto.Forms;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog();

dialog.Content = new Button() { Text = "I am a particularly wordy button, and I have a lot of information." };
dialog.ShowModal(parent); 
```

{{< /column >}}
{{< column >}}

![Implicitly Sized Button](/images/eto/controls/implicit-button.png)

{{< /column >}}
{{< /row >}}

## Best Practices
 // Minimum Sizes 
 // Maximum Sizes?
 // Explicitly setting a size?