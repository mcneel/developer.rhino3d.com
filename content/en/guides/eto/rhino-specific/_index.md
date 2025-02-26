+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto" ]
description = "Rhino Specific Eto extensions that make your life easier."
keywords = [ "Eto", "UI", "Plugin" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "Rhino specific Eto"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ ]

[page_options]
byline = true
toc = true
toc_type = "single"
+++

## Forms, Dialogs and Rhino Documents
Ensuring a Form or Dialog has an appropriate parent host, and is correctly tied to the calling Rhino Document is very important to avoid dialogs hidden behind Rhino, and issues with multiple open documents.

## Showing a Form
It is worth noting that at the time of writing when using the script editor, a form may show *behind* the editor in C# and python.
A dialog will temporarily hide the editor until it is closed.

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content" id="cs">

  ```cs
using Rhino.UI;
using Eto.Forms;

var myForm = new Form();
myForm.Show(__rhino_doc__);
  ```

  </div>

  <div class="codetab-content" id="py">

```py
import scriptcontext as sc

from Rhino.UI import EtoExtensions
import Eto.Forms as ef

form = ef.Form()

EtoExtensions.Show(form, sc.doc)
```

  </div>
</div>

## Showing a Dialog

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>


<div class="tab-content">
  <div class="codetab-content1" id="cs1">

  ```cs
using Rhino.UI;

using Eto.Forms;
 
var dialog = new Dialog()
{
    Width = 200,
    Height = 200
};
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
 
dialog.ShowModal(parent);
// or
 
// DefaultButton and AbortButton is required for SemiModal
dialog.DefaultButton = new Button();
dialog.AbortButton = new Button();
 
dialog.ShowSemiModal(__rhino_doc__, parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
import scriptcontext as sc

from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

dialog = ef.Dialog()
dialog.Width = 200
dialog.Height = 200

dialog.ShowModal(parent)
# or

# DefaultButton and AbortButton is required for SemiModal
dialog.DefaultButton = ef.Button()
dialog.AbortButton = ef.Button()

EtoExtensions.ShowSemiModal(dialog, sc.doc, parent)
  ```

  </div>
</div>

{{< call-out warning "Common DataContext Mistake" >}}
Avoid using RhinoEtoApp.MainWindow, it will not work correctly on Mac.
Prefer `RhinoEtoApp.MainWindowForDocument(doc)`.

It is also advisable to avoid using `RhinoEtoApp.MainWindowForDocument(RhinoDoc.ActiveDoc)`, as this may cause unexpected issues.
{{< /call-out >}}

<!-- TODO : I've seen this question before, so it'd be good to answer it
## Creating a non-document specific form (Like Grasshopper)

Creating a form that works regardless of the document can be trickier, but 
-->

## RhinoStyle
To ensure your form follows the same style as Rhino, and responds correctly to Dark/Light mode changes from within Rhino or the OS, there is a very handy extension method that can help you. It only needs to be called once at the top level of your Dialog or Form. It can safely be called inside or outside the constructor.


<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>


<div class="tab-content">
  <div class="codetab-content2" id="cs2">

  ```cs
using Rhino.UI;
using Eto.Forms;

var form = new Form();
form.UseRhinoStyle();
form.Show();
  ```

  </div>

  <div class="codetab-content2" id="py2">

```py
from Rhino.UI import EtoExtensions
import Eto.Forms as ef

form = ef.Form()
EtoExtensions.UseRhinoStyle(form)
form.Show()
```

  </div>
</div>

<!-- cs -- Everything above this line has been Tested on Win/Mac -->

## PushPickButton
Push Pick Button can be very helpful for hiding and showing your form whilst the user is performing an action, giving them the full use of their screen real estate.

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'py5')">Python</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

```cs
using Rhino.UI;
using Eto.Forms;

using Rhino;
using Rhino.Input;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var label = new Label() { Text = "None" };
var button = new Button() { Text = "Click me!" }; 

var dialog = new Dialog()
{
    Width = 120,
    Height = 120,
    Content = new TableLayout()
    {
        Rows = {
            new TableRow(label),
            new TableRow(button),
        }
    },
    DefaultButton = new Button(),
    AbortButton = new Button()
};

button.Click += (s, e) => {
    dialog.PushPickButton((s, e) => {
        RhinoGet.GetCircle(out var circle);
        label.Text = ((int)circle.Radius).ToString();
    });
};

EtoExtensions.ShowSemiModal(dialog, __rhino_doc__, parent);
```

  </div>
  <div class="codetab-content5" id="py5">

```py
import scriptcontext as sc
import rhinoscriptsyntax as rs

import Eto.Forms as ef
from Rhino import Input, UI, RhinoApp
from Rhino.UI import RhinoEtoApp, EtoExtensions
from Rhino.Geometry import Rectangle3d, Plane

label = ef.Label()
label.Text = "None"

button = ef.Button()
button.Text = "Click me!"

table_layout = ef.TableLayout()
table_layout.Rows.Add(ef.TableRow(ef.TableCell(label)))
table_layout.Rows.Add(ef.TableRow(ef.TableCell(button)))

dialog = ef.Dialog()
dialog.Width = 120
dialog.Height = 120
dialog.Content = table_layout
dialog.DefaultButton = ef.Button()
dialog.AbortButton = ef.Button()

def on_push_pick(s, e):
  points = rs.GetRectangle(1)
  rect = Rectangle3d(Plane.WorldXY, points[0], points[2])
  label.Text = str(rect.Width)

def on_click(s, e):
    EtoExtensions.PushPickButton(dialog, on_push_pick)

button.Click += on_click

parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__)
EtoExtensions.ShowSemiModal(dialog, __rhino_doc__, parent)
```

  </div>
</div>

## GetRhinoDoc

It's important to avoid using `RhinoDoc.ActiveDoc` especially when programming for mac, or else multiple documents will likely crash your code. This can get tricky when using events such as `RhinoApp.Idle` which don't/can't provide a Rhino Doc instance.

As long as you use `form.Show(doc);` to create your form, `form.GetRhinoDoc();` can be called anytime to retrieve the document. Of course, in the script editor, the document can be retried via the script context, but this is not the case elsewhere.

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

```cs
using Rhino.UI;
using Eto.Forms;

var myForm = new Form();
myForm.Show(__rhino_doc__);

var doc = myForm.GetRhinoDoc();
```

  </div>
  <div class="codetab-content4" id="py4">

```py
import scriptcontext as sc

from Rhino.UI import EtoExtensions
import Eto.Forms as ef

form = ef.Form()
EtoExtensions.Show(form, sc.doc)
doc = EtoExtensions.GetRhinoDoc(form)
```

  </div>
</div>

## WindowsFromDocument

Returns all the associated windows with the current Document, this can be useful in the inverse scenario where you have access to the RhinoDoc, but not the instance of the form.

<div class="codetab">
  <button class="tablinks6" onclick="openCodeTab(event, 'cs6')" id="defaultOpen6">C#</button>
  <button class="tablinks6" onclick="openCodeTab(event, 'py6')">Python</button>
</div>

<div class="tab-content">
<div class="codetab-content6" id="cs6">

```cs
using Rhino;
using Rhino.UI;
using Rhino.DocObjects;

using System.Linq;

using Eto.Forms;

class MyForm : Form {}
var myForm = new MyForm() { Width = 100, Height = 100 };
myForm.Content = new Label() { Text = "0" };

void IncrementLabel(object sender, RhinoObjectEventArgs e)
{
  var doc = e.TheObject.Document;
  var form2 = EtoExtensions.WindowsFromDocument<MyForm>(doc).FirstOrDefault();
  var label = form2.FindChild<Label>();
  if (int.TryParse(label.Text, out var count))
    label.Text = $"{++count}";
}

myForm.Shown += (a, b) => 
{
    RhinoDoc.AddRhinoObject -= IncrementLabel;
    RhinoDoc.AddRhinoObject += IncrementLabel;
};

myForm.Closed += (s, e) => {
    RhinoDoc.AddRhinoObject -= IncrementLabel;
};

myForm.Show(__rhino_doc__);
```
  </div>
</div>


<div class="tab-content">
<div class="codetab-content6" id="py6">

```py
import scriptcontext as sc
 
import Eto.Forms as ef
from Rhino import RhinoDoc
from Rhino.UI import RhinoEtoApp, EtoExtensions
 
class MyForm(ef.Form):
    pass

label = ef.Label()
label.Text = "0"

myForm = MyForm()
myForm.Width = 100
myForm.Height = 100
myForm.Content = label
myForm.count = 0

def IncrementLabel(s, args):
    doc = args.TheObject.Document
    form = EtoExtensions.WindowsFromDocument[MyForm](doc)[0]
    label = form.FindChild[ef.Label]()
    form.count += form.count
    label.Text = form.count

def subscribe(s, e):
    RhinoDoc.AddRhinoObject += IncrementLabel

myForm.Shown += subscribe

EtoExtensions.Show(myForm, sc.doc)
```
  </div>
</div>

## LocalizeAndRestore

{{< call-out note "Script Editor" >}}
  This script will not work in the Script Editor due to how LocalizeAndRestore works.
  It will work with a plugin, and the code sample is included as it is very convenient.
{{< /call-out >}}

After constructing a window calling this will store the location of the window so when it is closed it reopens in the same place. This information is stored permanently, so the window will keep its position between Rhino sessions.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

  ```cs
using Rhino.UI;
using Eto.Forms;

class MyDialog : Dialog {}

var myDialog = new MyDialog();
myDialog.LoadComplete += (s, e) => myDialog.LocalizeAndRestore();
myDialog.ShowModal();
  ```

  </div>

  <div class="codetab-content3" id="py3">

```py
from Rhino.UI import EtoExtensions
import Eto.Forms as ef

class MyDialog(ef.Dialog):
  pass

def on_load(s, e):
  EtoExtensions.LocalizeAndRestore(dialog)

dialog = MyDialog()
dialog.LoadComplete += on_load

dialog.ShowModal()
```

  </div>
</div>


## To and from Eto 

{{< call-out note "System.Drawing.Common" >}}
  Outside of Rhino, ToSD and other System.Drawing.Common calls [will not work in dotnet 7.0 onwards.](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/system-drawing)
{{< /call-out >}}

Moving between `System.Drawing` and Eto is often required when using Rhino SDKs or working with Non-Eto UIs on Windows. Eto provides lots of handy dandy `ToEto(...)` methods that can be called on most Eto types. See below for just a few. Note that some are available in Eto, but many additions are included within Rhino.

``` cs no-compile
public static Font ToEto(...);
public static Bitmap ToEto(...);
public static Icon ToEto(...);
public static Color ToEto(...);
public static Image ToEto(...);
```

Eto also includes many corresponding ToSD or ToSystemDrawing methods as well should you need to move from `Eto.Forms` types to `System.Drawing` types.

``` cs no-compile
public static SizeF ToSD(...);
public static RectangleF ToSD(...);
public static Point ToSD(...);
public static PointF ToSD(...);
public static Color ToSystemDrawing(...);
```

## Relative Positioning

{{< call-out note "A note on Locations" >}}
  The Location of any `Eto.Forms.Control` is always positioned at the Top Left.
{{< /call-out >}}

Locations of Eto Controls are relative. If you call `myControl.Location` the position returned is not the absolute position on the screen.

Let's take the example of the [Table Layout](../containers/#tables) from the [Containers Page](../containers) and add a some code to get the positions of the buttons.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks7" onclick="openCodeTab(event, 'cs7')" id="defaultOpen7">C#</button>
  <button class="tablinks7" onclick="openCodeTab(event, 'py7')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content7" id="cs7">

  ```cs no-compile
dialog.LoadComplete += (s, e) => {
    foreach(var button in dialog.Children.OfType<Button>())
    {
        button.Text = button.Location.ToString();
    }
};

dialog.ShowModal(parent);
  ```

  </div>

  <div class="codetab-content7" id="py7">

```py no-compile
# TODO : Fill this out
...
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Relative Positions](/images/eto/relative-positions.png)

{{< /column >}}
{{< /row >}}

</br>

Obviously this is useful in the context of the Dynamic Layout, but outside of the context it's not useful. Enter `PointToScreen(...)` which returns the coordinates of a control relative to another control, such as the ParentWindow or even the Screen. Make sure to move the Dialog once its loaded.


{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks8" onclick="openCodeTab(event, 'cs8')" id="defaultOpen8">C#</button>
  <button class="tablinks8" onclick="openCodeTab(event, 'py8')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content8" id="cs8">

  ```cs no-compile
dialog.LocationChanged += (s, e) => {
    foreach(var button in dialog.Children.OfType<Button>())
    {
        var location = button.PointToScreen(button.Location);
        button.Text = location.ToString();
    }
};

dialog.ShowModal(parent);
  ```

  </div>

  <div class="codetab-content8" id="py8">

```py no-compile
# TODO : Fill this out
...
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Screen Positions](/images/eto/screen-positions.png)

{{< /column >}}
{{< /row >}}

</br>

<!-- TODO : This is kind of wonky and needs work.

Below is a small dialog with a label that can be dragged to see the Controls Location relative to its Container, Parent Window and the Screen.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks9" onclick="openCodeTab(event, 'cs9')" id="defaultOpen9">C#</button>
  <button class="tablinks9" onclick="openCodeTab(event, 'py9')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content9" id="cs9">

```cs no-compile
using System.Linq;

using Eto.Forms;
using Eto.Drawing;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var pixelLayout = new PixelLayout() {
    Width = 400,
    Height = 400
};

var dragLabel = new Label() { Text = "Drag Me!" };
bool drag = false;

dragLabel.MouseDown += (s, e) => {
    drag = true;
};

dragLabel.MouseUp += (s, e) => {
    drag = false;
};

dragLabel.MouseMove += (s, e) => {
    if (!drag) return;
    pixelLayout.Move(dragLabel, (int)e.Location.X, (int)e.Location.Y);
    dragLabel.Text = e.Location.ToString();
};

pixelLayout.Add(dragLabel, 10, 10);

var dialog = new Dialog()
{
    Content = new Panel() {
        Content = pixelLayout,
        Padding = 12
    }
};

dialog.ShowModal(parent);
```
  </div>

  <div class="codetab-content9" id="py9">

```py no-compile
# TODO : Fill this out
...
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Drag Positions](/images/eto/drag-positions.png)

{{< /column >}}
{{< /row >}}

// TODO : Doc this

``` cs no-compile
public static PointF PointToScreen(...);

public static PointF ToEtoScreen(...);
public static RectangleF ToEtoScreen(...);

public static Rectangle ToSystemDrawingScreen(...);
```
-->