+++
aliases = [ ]
authors = [ "callum"]
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


<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

  ```cs
using Eto.Forms;
using Eto.Drawing;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog()
{
    Padding = 8 // Comment out to remove Padding
};

var stackLayout = new StackLayout()
{
    Spacing = 8 // Comment out to remove Spacing
};

stackLayout.Orientation = Orientation.Vertical;
stackLayout.Items.Add(new Button() { Text = "One" });
stackLayout.Items.Add(new Button() { Text = "Two" });
stackLayout.Items.Add(new Button() { Text = "Three" });

dialog.Content = stackLayout;
dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content2" id="py2">

  ```py
import scriptcontext as sc

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

dialog = ef.Dialog()
dialog.Padding = ed.Padding(8) # Comment out to remove Padding

stack_layout = ef.StackLayout()
stack_layout.Spacing = 8 # Comment out to remove Spacing

stack_layout.Orientation = Orientation.Vertical

button_one = ef.Button()
button_one.Text = "One"
button_two = ef.Button()
button_two.Text = "Two"
button_three = ef.Button()
button_three.Text = "Three"

stack_layout.Items.Add(ef.StackLayoutItem(button_one))
stack_layout.Items.Add(ef.StackLayoutItem(button_two))
stack_layout.Items.Add(ef.StackLayoutItem(button_three))

dialog.Content = stack_layout
dialog.ShowModal(parent)
  ```

  </div>
</div>


## Extra adjustments in Spacing
When working with multi-control Containers in eto, adding in extra spacing can be achieved through the use of `Null` or `None`. This can add nudges, force alignments and even be the area of the layout that expands in case you don't want anything else to.

<!-- Table Layout -->
<!-- Stack Layout -->
<!-- Dynamic Layout -->

<!-- Dynamic Layout null spaces-->

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

  ```cs
using Eto.Forms;
using Eto.Drawing;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog()
{
    Padding = 13,
    Width = 400,
    Height = 130
};

var dynamicLayout = new DynamicLayout()
{
    Spacing = new Size(8, 8)
};

dynamicLayout.Add(new TextBox(), true, true);
dynamicLayout.Add(null, true, false); // Adds a little space

dynamicLayout.AddSeparateRow(null, new Size(8,8), true, false,
    new [] {
        null, // Causes Align Right
        new Button() { Text = "Apply"},
        new Button() { Text = "Ok"},
        new Button() { Text = "Cancel"},
    });

dialog.Content = dynamicLayout;
dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content3" id="py3">

  ```py
import scriptcontext as sc

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

dialog = ef.Dialog()
dialog.Padding = ed.Padding(12)
dialog.Width = 400
dialog.Height = 120

dynamic_layout = ef.DynamicLayout()
dynamic_layout.Spacing = ed.Size(8, 8)

dynamic_layout.Add(ef.TextBox(), True, True)
dynamic_layout.Add(None, True, False) # Adds a little space

apply_button = ef.Button()
apply_button.Text = "Apply"
ok_button = ef.Button()
ok_button.Text = "Ok"
cancel_button = ef.Button()
cancel_button.Text = "Cancel"

rows = [
    None, # Causes Align Right
    apply_button,
    ok_button,
    cancel_button,
]

dynamic_layout.AddSeparateRow(None, Size(8,8), True, False, rows)

dialog.Content = dynamic_layout
dialog.ShowModal(parent)
  ```

  </div>
</div>


{{< /column >}}
{{< column >}}

![Dynamic Layout](/images/eto/controls/null-spaced-layout-1.png)

{{< /column>}}
{{< /row >}}