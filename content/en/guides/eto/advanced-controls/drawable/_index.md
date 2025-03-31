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

## Your first Drawable
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
    Padding = 5,
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
    e.Graphics.DrawRectangle(rectPen, 10, 80, 140, 40);

    // Rounded Rectangle
    var roundRect = new RectangleF(10, 140, 140, 40);
    var roundedRectPen = new Pen(Colors.BlueViolet, 6);
    var roundedRectPath = GraphicsPath.GetRoundRect(roundRect, 10);
    e.Graphics.DrawPath(roundedRectPen, roundedRectPath);
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
drawable.Padding = ed.Padding(5)
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
    e.Graphics.DrawRectangle(rectPen, 10, 80, 140, 40)

    # Rounded Rectangle
    roundedRectPen = ed.Pen(ed.Colors.BlueViolet, 6)
    roundRect = ed.RectangleF(10, 140, 140, 40)
    roundedRectPath = ed.GraphicsPath.GetRoundRect(roundRect, 10)
    e.Graphics.DrawPath(roundedRectPen, roundedRectPath)

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

## Basic Drawable Mouse Events

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

var drawable = new Drawable() {
    Width = 52,
    Height = 52
};

bool over;

drawable.Paint += (s, e) => {
    var rect = new RectangleF(1, 1, 50, 50);
    e.Graphics.FillEllipse(Color.FromArgb(255, 90, 89), rect);

    if (over)
    {
        var pen = new Pen(Color.FromArgb(170, 22, 1), 5f);
        e.Graphics.DrawLine(pen, 16, 16, 34, 34);
        e.Graphics.DrawLine(pen, 34, 16, 16, 34);
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
  <div class="codetab-content3" id="py3">

```py
import scriptcontext as sc

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

drawable = ef.Drawable()
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
    rect = ed.RectangleF(1, 1, 50, 50)
    e.Graphics.FillEllipse(ed.Color.FromArgb(255, 90, 89), rect)

    if drawable.over:
        pen = ed.Pen(ed.Color.FromArgb(170, 22, 1), 5)
        e.Graphics.DrawLine(pen, 16, 16, 34, 34)
        e.Graphics.DrawLine(pen, 34, 16, 16, 34)

drawable.Paint += draw
drawable.MouseEnter += mouse_enter
drawable.MouseLeave += mouse_leave


dialog = ef.Dialog()
dialog.Content = drawable
dialog.Padding = ed.Padding(24)
dialog.ShowModal(parent)
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Eto Button](/images/eto/controls/drawable-2.png)

{{< /column >}}
{{< /row >}}

## Dragging in Drawables

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
using Eto.Drawing;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

bool mouseDown = false;
PointF location = new (100, 100);

RectangleF GetRect()
{
    return RectangleF.FromCenter(new PointF(location.X, location.Y), new SizeF(30, 30));
}

var drawable = new Drawable() {
    Width = 200,
    Height = 200
};

bool over;

drawable.Paint += (s, e) => {
    var rect = GetRect();
    e.Graphics.FillEllipse(Colors.OrangeRed, rect);
    
    if (!mouseDown) return;
    e.Graphics.DrawEllipse(Colors.Goldenrod, rect);
};

drawable.MouseMove += (s, e) => {
    if (!mouseDown) return;
    location = e.Location;
    drawable.Invalidate(true);
};

drawable.MouseUp += (s, e) => {
    mouseDown = false;
    drawable.Invalidate(true);
};

drawable.MouseDown += (s, e) => {
    if (!GetRect().Contains(e.Location)) return;
    mouseDown = true;
    location = e.Location;
    drawable.Invalidate(true);
};

var dialog = new Dialog()
{
    Padding = 24,
    Content = drawable
};

dialog.ShowInTaskbar = true;
dialog.ShowModal();
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

drawable = ef.Drawable()
drawable.Width = 200
drawable.Height = 200
drawable.down = False
drawable.mouse_location = ed.PointF(100, 100)

def get_rect():
    point = ed.PointF(drawable.mouse_location.X, drawable.mouse_location.Y)
    size = ed.SizeF(30, 30)
    rect = ed.RectangleF.FromCenter(point, size)
    return rect

def mouse_move(sender, e):
    if not drawable.down:
        return
        
    drawable.mouse_location = e.Location
    drawable.Invalidate(True)
    
def mouse_up(sender, e):
    drawable.down = False
    drawable.Invalidate(True)

def mouse_down(sender, e):
    if not get_rect().Contains(e.Location):
        return

    drawable.down = True
    drawable.mouse_location = e.Location
    drawable.Invalidate(True)
    
def draw(sender, e):
    rect = get_rect()
    e.Graphics.FillEllipse(ed.Colors.OrangeRed, rect)
    
    if not drawable.down:
        return

    e.Graphics.DrawEllipse(ed.Colors.Goldenrod, rect)

drawable.Paint += draw
drawable.MouseMove += mouse_move
drawable.MouseUp += mouse_up
drawable.MouseDown += mouse_down


dialog = ef.Dialog()
dialog.Padding = ed.Padding(24)
dialog.Content = drawable

dialog.ShowModal(parent)

```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Eto Button](/images/eto/controls/drawable-3.png)

{{< /column >}}
{{< /row >}}
