+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
description = "An overview of the universal properties of Eto Controls"
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Control Properties"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

## Enabled
Controls are by default enabled, but can be disabled with `Enabled = false`. When a control is disabled it will not respond to any of its events, such as mouse interaction or keys,.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content" id="cs">

  ```cs
using Eto.Forms;

using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog()
{
    Padding = 8,
    Content = new Button() { Text = "Disabled", Enabled = false }
};

dialog.ShowModal(parent);
  ```

  </div>

  <div class="codetab-content" id="py">

  ```py
import scriptcontext as sc

from Eto.Drawing import *
from Eto.Forms import *

from Rhino.UI import *

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = Button()
button.Text = "Disabled"
button.Enabled = False

dialog = Dialog()
dialog.Padding = Padding(8)
dialog.Content = button
dialog.ShowModal(parent)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Disabled Button](/images/eto/properties/disabled-button.png)

{{< /column >}}
{{< /row >}}

## Visible

Controls are by default visible, but can be made invisible with `Visible = false`. When a control is invisible it still exists. It will not recieve any events such as mouse of keyboard, and may not be considered when the control layout is calculated. Note that the dialog defaults to different size than when the button is visible.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

  ```cs
using Eto.Forms;

using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var dialog = new Dialog()
{
    Padding = 8,
    Content = new Button() { Text = "Invisible", Visible = false }
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
import scriptcontext as sc

from Eto.Drawing import *
from Eto.Forms import *

from Rhino.UI import *

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = Button()
button.Text = "Invisible"
button.Visible = False

dialog = Dialog()
dialog.Padding = Padding(8)
dialog.Content = button
dialog.ShowModal(parent)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Invisible Button](/images/eto/properties/invisible-button.png)

{{< /column >}}
{{< /row >}}

## Tag
Tag allows for attaching an arbitratry piece of data to a Control, it is best to keep this piece of data simple. A number, string, enum or struct. Avoid larger items such as images, and especially other controls. 

This can be very useful when

## Parent(s) & ParentWindow
All Controls shown in the UI will have a Parent and ParentWindow.
ParentWindow retrieves the Dialog or Form this control is hosted in. This can be very useful when wanting to set focus to the parent or show another window on top of the current window.

## Cursor
The mouse cursor can easily be changed per control. This is a very powerful and intuitive way to indicate to the user how the control should be used. For Example indicating Drag functionaliy by using the grabbing hand cursor.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

  ```cs
using Eto.Forms;

using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var button = new Button() { Text = "Move", Cursor = Cursors.Move };

var dialog = new Dialog()
{
    Padding = 28,
    Content = button,
    Cursor = Cursors.Crosshair;
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content2" id="py2">

  ```py
import scriptcontext as sc

from Eto.Drawing import *
from Eto.Forms import *

from Rhino.UI import *

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = Button()
button.Text = "Move"
button.Cursor = Cursors.Move

dialog = Dialog()
dialog.Padding = Padding(28)
dialog.Content = button
dialog.Cursor = Cursors.Crosshair

dialog.ShowModal(parent)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Invisible Button](/images/eto/properties/cursor.png)

{{< /column >}}
{{< /row >}}
