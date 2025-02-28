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

The clipboard can of course also include other items like bitmaps, which is done in a very similar way

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

```cs
using Eto.Forms;
Clipboard.Instance.Bitmap = bitmap
```

  </div>
  <div class="codetab-content2" id="py2">

```py
from Eto.Forms import Clipboard;
Clipboard.Instance.Bitmap = bitmap
```

  </div>
</div>

