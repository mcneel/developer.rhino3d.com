+++
aliases = [ ]
authors = [ "callum", "curtis" ]
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

+++
Drawable provides infinite flexibility in Eto, you can draw anything in a resuable UI control.

## Your first Drawable

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
    Width = 52,
    Height = 52
};

bool over = false;

drawable.Paint += (s, e) => {
    var rect = new RectangleF(1, 1, 50, 50);
    e.Graphics.FillEllipse(Color.FromArgb(255, 90, 89), rect);

    if (over)
    {
        var pen = new Pen(Color.FromArgb(153, 0, 5), 5f);
        e.Graphics.DrawLine(pen, 16, 16, 34, 34);
        e.Graphics.DrawLine(pen, 16, 34, 34, 16);
    }
};

drawable.MouseEnter += (s, e) => {
    over = true;
    drawable.Invalidate(true);
};

drawable.MouseLeave += (s, e) => {
    over = false;
    drawable.Invalidate(true);
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

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
from Eto.Forms import *
from Eto.Drawing import *

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

drawable = Drawable()
drawable.Width = 52
drawable.Height = 52
drawable.over = False

def mouse_enter(sender, e):
    drawable.over = True
    drawable.Invalidate(True)

def mouse_leave(sender, e):
    drawable.over = False
    drawable.Invalidate(True)
    
def draw(sender, e):
    rect = RectangleF(1, 1, 50, 50)
    e.Graphics.FillEllipse(Color.FromArgb(255, 90, 89), rect)

    if drawable.over:
        pen = Pen(Color.FromArgb(153, 0, 5), 5)
        e.Graphics.DrawLine(pen, 16, 16, 34, 34)
        e.Graphics.DrawLine(pen, 16, 34, 34, 16)

drawable.Paint += draw
drawable.MouseEnter += mouse_enter
drawable.MouseLeave += mouse_leave


dialog = Dialog()
dialog.Content = drawable
dialog.Padding = Padding(24)
dialog.ShowModal(parent)
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Eto Button](/images/eto/controls/drawable-1.png)

{{< /column >}}
{{< /row >}}
