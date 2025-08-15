+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Eto Clipboard"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

{{< row >}}
{{< column >}}

An introduction to the System Clipboard

{{< /column >}}
{{< column >}}

[Eto.Forms.Clipboard API Reference](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_Clipboard.htm)

{{< /column >}}
{{< /row >}}

</br>

The clipboard is where data is stored when copy (`ctrl + c` or `⌘ + c`) is run on a computer.
`Clipboard.Instance` contains all of the potential copied items such as text, images, urls or html.

This code will put "I was copied" into your clipboard, and using (`ctrl + v` or `⌘ + v`) will paste the text.
<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

```cs
using Eto.Forms;
Clipboard.Instance.Text = "I was copied";
```

  </div>
  <div class="codetab-content1" id="py1">

```py
from Eto.Forms import Clipboard;
Clipboard.Instance.Text = "I was copied"
```

  </div>
</div>

</br>

The clipboard can of course also include other items like bitmaps, which is done in a very similar way. Note that changing `Clipboard.Instance.<item>` is universal and will work across other applications.

</br>

## Application Specific

Text and Bitmaps are simple and universal, but what about a custom data type? Some data types are application specific, if I copy a 3d Sphere in Rhino we would only expect this to paste in Rhino, if we're lucky, maybe into other 3d applications. As there are no specific clipboard items for your custom data, we need to create our own.

![Clipboard Example](/images/eto/clipboard.png)

This sample will add data to the clipboard with the key "PointF" and retrieve the data with the same key. Using keys for this is excellent as data from different sources can exist simultaneously.

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

```cs
using System.Text.Json;
using System;

using Eto.Drawing;
using Eto.Forms;

using Rhino.UI;

var copyButton = new Button() { Text = "Copy" };
var pasteButton = new Button() { Text = "Paste" };

copyButton.Click += (s,e) => {
    JsonSerializerOptions options = new JsonSerializerOptions()
    {
        IgnoreReadOnlyFields = true,
        IgnoreReadOnlyProperties = true,
    };
    
    try
    {
        string data = JsonSerializer.Serialize(new PointF(4, 8), options);
        Clipboard.Instance.SetString(data, nameof(PointF));
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
};

pasteButton.Click += (s,e) => {
    try
    {
        string data = Clipboard.Instance.GetString(nameof(PointF));
        PointF point = JsonSerializer.Deserialize<PointF>(data);
        Console.WriteLine(point.ToString());
    } catch {}
};

var layout = new DynamicLayout() { Spacing = new Size(4, 8), Padding = 8 };
layout.BeginHorizontal();
layout.Add(copyButton);
layout.Add(pasteButton);
layout.EndHorizontal();

var dialog = new Dialog()
{
  Content = layout,
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content2" id="py2">

```py
import System.Text.Json as js

import Eto.Drawing as ed
import Eto.Forms as ef

from Rhino.UI import RhinoEtoApp

def copy_data(sender, args):
    options = js.JsonSerializerOptions()
    options.IncludeFields = False
    options.IgnoreReadOnlyProperties = True

    data = js.JsonSerializer.Serialize(ed.PointF(4, 8), options);
    ef.Clipboard.Instance.SetString(data, "PointF")

def paste_data(sender, args):
    data = ef.Clipboard.Instance.GetString("PointF")
    point = js.JsonSerializer.Deserialize[ed.PointF](data)
    print (point)

copy_button = ef.Button()
copy_button.Text = "Copy"
copy_button.Click += copy_data

paste_button = ef.Button()
paste_button.Text = "Paste"
paste_button.Click += paste_data

layout = ef.DynamicLayout()
layout.Spacing = ed.Size(4, 8)
layout.Padding = ed.Padding(8)

layout.BeginHorizontal()
layout.Add(copy_button)
layout.Add(paste_button)
layout.EndHorizontal()

dialog = ef.Dialog()
dialog.Content = layout

parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__)
dialog.ShowModal(parent)
```

  </div>
</div>

