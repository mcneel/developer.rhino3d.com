+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Eto Tab Layout"
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
 <!-- TODO : Include these samples https://developer.rhino3d.com/guides/rhinopython/eto-controls-python/ -->


{{< row >}}
{{< column >}}

An introduction to Tab Control in Eto.

{{< /column >}}
{{< column >}}

[Eto.Forms.TabControl API Reference](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_TabControl.htm)

{{< /column >}}
{{< /row >}}

</br>

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

var button = new Button() { Text = "I am a button" };
button.Click += (s, e) => { MessageBox.Show("You clicked me"); };

var dialog = new Dialog()
{
    Padding = 8,
    Content = button
};

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

```py
import scriptcontext as sc

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions

import Eto.Drawing as ed
import Eto.Forms as ef


def show_message(sender, e):
  ef.MessageBox.Show("You clicked me")

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

dialog = ef.Dialog()
dialog.Padding = ed.Padding(8)

button = ef.Button()
button.Click += show_message
button.Text = "I am a button"

dialog.Content = button
dialog.ShowModal(parent)
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Eto Button](/images/eto/controls/button.png)

{{< /column >}}
{{< /row >}}
