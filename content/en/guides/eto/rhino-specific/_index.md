+++
aliases = []
authors = [ "curtis", "callum" ]
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
It is worth noting that at the time of writing when using the script editor, a form will show *behind* the editor in C# and python.
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
#! python3
import scriptcontext as sc

from Rhino.UI import EtoExtensions
from Eto.Forms import Form

form = Form()

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
  
    var myDialog = new Dialog();
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    
    dialog.ShowModal(parent)
    // or

    // DefaultButton and AbortButton is required for SemiModal
    dialog.DefaultButton = new Button()
    dialog.AbortButton = new Button()

    dialog.ShowSemiModal(__rhino_doc__, parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
  #! python3
  import scriptcontext as sc

  from Rhino.UI import RhinoEtoApp, EtoExtensions
  from Eto.Forms import Dialog, Button

  parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

  dialog = Dialog()

  dialog.ShowModal(parent)
  # or

  # DefaultButton and AbortButton is required for SemiModal
  dialog.DefaultButton = Button()
  dialog.AbortButton = Button()

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

  var myForm = new Form();
  myForm.UseRhinoStyle();
  ```

  </div>

  <div class="codetab-content2" id="py2">

```py
#! python3
from Rhino.UI import EtoExtensions
from Eto.Forms import form

form = Form()
EtoExtensions.UseRhinoStyle(form)
```

  </div>
</div>

// TODO : Organise this better

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
using Rhino.Inputs;

var form = new Form();
form.Show(__rhino_doc__);

form.PushPickButton(() => {

});
```

  </div>
  <div class="codetab-content5" id="py5">

```py
import scriptcontext as sc

from Rhino.UI import EtoExtensions
from Eto.Forms import Form

form = Form()
EtoExtensions.Show(form, sc.doc)
doc = EtoExtensions.GetRhinoDoc(form)
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
from Eto.Forms import Form

form = Form()
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

var form = new Form();
form.Content = new Label() { Text = "0" };

form.Shown += (s, e) => RhinoDoc.AddRhinoObject += Incriment;
form.Closing += (s, e) => RhinoDoc.AddRhinoObject -= Incriment;

form.Shown += (a, b) => RhinoDoc.AddRhinoObject += (s, e) =>
{
  var doc = e.TheObject.Document;
  var form2 = EtoExtensions.WindowsFromDocument<Form>(doc).FirstOrDefault();
  var label = form2.FindChild<Label>();
  if (int.TryParse(label.Text, out var count))
    label.Text = $"{++count}";
};

form.Show(__rhino_doc__);
```
  </div>
</div>

## LocalizeAndRestore

After constructing a window calling this will store the location of the window so when it is closed it reopens in the same place. This information is stored permanently, so the window will keep its permission between Rhino sessions.

NOTE : This does not work in the script editor.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

  ```cs
  using Rhino.UI;
  using Eto.Forms;

  class MyForm : Form {}

  var myForm = new MyForm();
  myForm.SavePosition();
  myForm.Show();
  ```

  </div>

  <div class="codetab-content3" id="py3">

```py
from Rhino.UI import EtoExtensions
from Eto.Forms import form

class MyForm(Form):
  pass

form = MyForm()
EtoExtensions.SavePosition(form)
form.Show()
```

  </div>
</div>


## To and from Eto 

Moving between `System.Drawing` and Eto is often required when using Rhino SDKs or working with Non-Eto UIs on Windows. Eto provides lots of handy dandy `ToEto(...)` methods that can be called on most Eto types. See below for just a few. Note that some are available in Eto, but many additions are included within Rhino.

``` cs
public static Font ToEto(...);
public static Bitmap ToEto(...);
public static Icon ToEto(...);
public static Color ToEto(...);
public static Image ToEto(...);
```

Eto also includes many corresponding ToSD or ToSystemDrawing methods as well should you need to move from Eto to `System.Drawing` types.

``` cs
public static SizeF ToSD(...);
public static RectangleF ToSD(...);
public static Point ToSD(...);
public static PointF ToSD(...);
public static Color ToSystemDrawing(...);
```

## Relative Positioning


``` cs
public static PointF ToEtoScreen(...);
public static RectangleF ToEtoScreen(...);

public static Rectangle ToSystemDrawingScreen(...);
```