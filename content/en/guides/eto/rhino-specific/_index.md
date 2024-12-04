+++
aliases = []
authors = [ "curtis", "callum" ]
categories = [ "Eto" ]
description = "Rhino Specific Eto"
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

# Forms, Dialogs and Rhino Documents
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
  using Rhino;
  using Rhino.UI;
  using Eto.Forms;

  // ... 

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var myForm = new Form();
    myForm.Show(doc);
  }
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

  // ... 

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var myDialog = new Dialog();
    var parent = RhinoEtoApp.MainWindowForDocument(doc);
    
    dialog.ShowModal(parent)
    // or

    // DefaultButton and AbortButton is required for SemiModal
    dialog.DefaultButton = new Button()
    dialog.AbortButton = new Button()

    dialog.ShowSemiModal(doc, parent);
  }
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


## \#RhinoStyle
To ensure your form follows the same style as Rhino, and responds correctly to Dark/Light mode changes from within Rhino or the OS, there is a very handy extension method that can help you. It only needs to be called once at the top level of your Dialog or Form. It can safely be called inside or outside the constructor.


<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>


<div class="tab-content">
  <div class="codetab-content2" id="cs2">

  ```cs
  using Rhino.UI;

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

# PushPickButton


# WindowsFromDocument & GetRhinoDoc

# GetRhinoDoc

# ToEto

``` cs
public static Font ToEto(...);
public static Bitmap ToEto(...);
public static Icon ToEto(...);
public static Color ToEto(...);
public static Image ToEto(...);
```