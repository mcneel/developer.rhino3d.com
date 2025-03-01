+++
aliases = [ ]
authors = [ "callum"]
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

<!-- cs -- Tested on Win/Mac -->

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

import Eto.Drawing as ed
import Eto.Forms as ef

from Rhino.UI import RhinoEtoApp

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = ef.Button()
button.Text = "Disabled"
button.Enabled = False

dialog = ef.Dialog()
dialog.Padding = ed.Padding(8)
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

Controls are by default visible, but can be made invisible with `Visible = false`. When a control is invisible it still exists. It will not receive any events such as mouse of keyboard, and may not be considered when the control layout is calculated. Note that the dialog defaults to different size than when the button is visible.

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
    Width = 200,
    Height = 200,
    Padding = 8,
    Content = new Button() { Text = "Invisible", Visible = false }
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
import scriptcontext as sc

import Eto.Drawing as ed
import Eto.Forms as ef

from Rhino.UI import RhinoEtoApp

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = ef.Button()
button.Text = "Invisible"
button.Visible = False

dialog = ef.Dialog()
dialog.Width = 200
dialog.Height = 200
dialog.Padding = ed.Padding(8)
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
Tag allows for attaching an arbitrary piece of data to a Control, it is best to keep this piece of data simple. A number, string, enum or struct. Avoid larger items such as images, and especially other controls. 

This can be very useful when controls are not hard coded, and instead created in loops.

## Parent(s) & ParentWindow
{{< call-out note "Parental Guidance" >}}
  Parent and ParentWindow will not be set until the Control has been added to a Parent/Container, and the Parents to the Window.
{{< /call-out >}}

All Controls shown in the UI will have a Parent and ParentWindow.
ParentWindow retrieves the Dialog or Form this control is hosted in. This can be very useful when wanting to set focus to the parent or show another window on top of the current window.

## Cursor
The mouse cursor can easily be changed per control. This is a very powerful and intuitive way to indicate to the user how the control should be used. For Example indicating Drag functionally by using the grabbing hand cursor.

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
    Cursor = Cursors.Crosshair
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content2" id="py2">

  ```py
import scriptcontext as sc

import Eto.Drawing as ed
import Eto.Forms as ef

from Rhino.UI import RhinoEtoApp

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

button = ef.Button()
button.Text = "Move"
button.Cursor = ef.Cursors.Move

dialog = ef.Dialog()
dialog.Padding = ed.Padding(28)
dialog.Content = button
dialog.Cursor = ef.Cursors.Crosshair

dialog.ShowModal(parent)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Invisible Button](/images/eto/properties/cursor.png)

{{< /column >}}
{{< /row >}}
