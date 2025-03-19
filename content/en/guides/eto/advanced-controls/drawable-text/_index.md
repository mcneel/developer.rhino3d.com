+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
description = "An overview of the Eto Drawable Control"
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Eto Drawable"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

[page_options]
  block_webcrawlers = true

+++
Drawable provides infinite flexibility in Eto, you can draw anything in a reusable UI control.

## NAME ME
Drawables let you draw anything in a 2d space.
Use this as a scratch pad and try out the various drawing methods.

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
using Eto.Drawing;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var drawable = new Drawable() {
    Width = 200,
    Height = 200
};

drawable.Paint += (s, e) => {

    // Circle
    var rect = new RectangleF(0, 0, 50, 50);
    e.Graphics.FillEllipse(Colors.Red, rect);

    // Line
    var linePen = new Pen(Colors.Blue, 4f);
    e.Graphics.DrawLine(linePen, 60, 60, 120, 60);

    // Rectangle
    var rectPen = new Pen(Colors.Green, 6f);
    e.Graphics.DrawRectangle(rectPen, 10, 80, 140, 80);
};

var dialog = new Dialog()
{
    Padding = 24,
    Content = drawable
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

```py
import scriptcontext as sc

from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

drawable = ef.Drawable()
drawable.Width = 200
drawable.Height = 200

def draw(sender, e):

    # Circle
    rect = ed.RectangleF(0, 0, 50, 50)
    e.Graphics.FillEllipse(ed.Colors.Red, rect)

    # Line
    linePen = ed.Pen(ed.Colors.Blue, 4)
    e.Graphics.DrawLine(linePen, 60, 60, 120, 60)

    # Rectangle
    rectPen = ed.Pen(ed.Colors.Green, 6)
    e.Graphics.DrawRectangle(rectPen, 10, 80, 140, 80)

drawable.Paint += draw

dialog = ef.Dialog()
dialog.Padding = ed.Padding(24)
dialog.Content = drawable

dialog.ShowModal(parent)
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Eto Button](/images/eto/controls/drawable-1.png)

{{< /column >}}
{{< /row >}}
