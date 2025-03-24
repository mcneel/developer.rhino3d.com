+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Fundamentals" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux", "Fundamentals" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Tree Grid Views"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

{{< call-out note "Cells" >}}
  It's advisable to read about [Cells](../cells) before Tree Grid Views. It's also advisable to read about [Grid Views](../grid-view) before Tree Grid Views as an introductory step
{{< /call-out >}}

{{< row >}}
{{< column >}}

An introduction to Tree Grid Views.

{{< /column >}}
{{< column >}}

[Eto.Forms.TreeGridView API Reference](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_TreeGridView.htm)

{{< /column >}}
{{< /row >}}

![Tree Grid View](/images/eto/tutorials/tree-grid-view.png)

Tree Grid Views allow us to create rows which are bound to a data structure.
This guide will cover all the eccentricities of Tree Grid Views which can be confusing.

## Trees
Trees are a common data structure in programming. Trees are composed of nodes and branches with a common singular root.

![Tree Data Structure](/images/eto/data/tree-diagram.png)


## Declaration

TreeGridViews are defined by Columns which are bound to a tree defining the rows.
Without data, they're not particularly interesting.

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

var treeGridView = new TreeGridView()
{
  Columns = {
    new GridColumn()
    {
        HeaderText = "Name",
        DataCell = new TextBoxCell(),
    },
  },
  // DataStore = ...
};

var dialog = new Dialog()
{
  Width = 400,
  Height = 200,
  Content = treeGridView,
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content2" id="py2">

```py
import scriptcontext as sc
import Eto.Forms as ef
from Rhino.UI import RhinoEtoApp

plusColumn = ef.GridColumn()
plusColumn.HeaderText = "Key"

itemColumn = ef.GridColumn()
itemColumn.HeaderText = "Value"

gridView = ef.GridView()
# gridView.DataStore = ...
gridView.Columns.Add(plusColumn)
gridView.Columns.Add(itemColumn)

dialog = ef.Dialog()
dialog.Width = 100
dialog.Height = 100
dialog.Content = gridView

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)
dialog.ShowModal(parent)
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Empty Tree Grid View](/images/eto/tutorials/empty-tree-grid-view.png)

{{< /column >}}
{{< /row >}}

## DataStore and Bindings

Tree Grid View data stores differ to the GridView as they require a more rigid (tree) structure.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content4" id="cs4">

``` cs
using Eto.Forms;

using Rhino.UI;

var treeData = new TreeGridItemCollection()
{
    new TreeGridItem(new TreeGridItem[]
    {
        new TreeGridItem("Antarctica"),
        new TreeGridItem("Africa"),
        new TreeGridItem("Asia"),
        new TreeGridItem("Australia"),
        new TreeGridItem("Europe"),
        new TreeGridItem("North America"),
        new TreeGridItem("South America"),
    }, 
    "Earth")
};
 

var treeGridView = new TreeGridView()
{
  Columns = {
    new GridColumn()
    {
        HeaderText = "Name",
        // 0 Binds to the first item in the list, if there is no list, then the only item available
        DataCell = new TextBoxCell(0),
    },
  },
  DataStore = treeData
};

var dialog = new Dialog()
{
  Width = 400,
  Height = 200,
  Content = treeGridView,
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content4" id="py4">

  ```py

  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Simple Tree Grid View](/images/eto/tutorials/simple-tree-grid-view.png)

{{< /column >}}
{{< /row >}}

</br>

### Reloading Data

Generally `ObservableCollection<T>` is used to inform the UI of changes when the collection is changed. It is not possible to use an `ObservableCollection<t>` for a TreeGridView as a Tree structure is required, hence `TreeGridStore` is used.

TreeGridView offers two reload options `ReloadItem()` which reloads 1 item (optionally including children)  and `ReloadData()` which reloads _everything_.

Reloading an ENTIRE GridView due to 1 cell changing would be very inefficient, using ReloadItem is much more efficient.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

```cs
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content3" id="py3">

```py

```

  </div>
</div>


## Code

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

```cs
using System.Collections.ObjectModel;
using System.Collections;
using System.Linq;
using System;

using Eto.Drawing;
using Eto.Forms;

using Rhino.UI;

class Flaggable
{
    public string Name { get; set; }

    public string Flag { get; set; }

    public Flaggable(string name, string flag)
    {
        Name = name; Flag = flag;
    }
}

var treeData = new TreeGridItemCollection()
{
    new TreeGridItem(new TreeGridItem[]
    {
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("The South Pole", "💈"))
            }, new Flaggable("Antarctica", "🇦🇶")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("South Africa", "🇿🇦")),
                new TreeGridItem(new Flaggable("Kenya", "🇰🇪")),
            }, new Flaggable("Africa", "🌍")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("China", "🇨🇳")),
                new TreeGridItem(new Flaggable("Japan", "🇯🇵"))
            }, new Flaggable("Asia", "🌏")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("Sydney", "🏖️")),
                new TreeGridItem(new Flaggable("Canberra", "🐨")),
            }, new Flaggable("Australia", "🇦🇺")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("Belgium", "🇧🇪")),
                new TreeGridItem(new Flaggable("Monaco", "🇲🇨")),
            }, new Flaggable("Europe", "🌍")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("Canada", "🇨🇦")),
                new TreeGridItem(new Flaggable("Mexico", "🇲🇽")),
            }, new Flaggable("North America", "🌎")),
        new TreeGridItem(new []{
                new TreeGridItem(new Flaggable("Brazil", "🇧🇷")),
                new TreeGridItem(new Flaggable("Colombia", "🇨🇴")),
            }, new Flaggable("South America", "🌎")),
    }, 
    new Flaggable("Earth", "🗺️"))
};



class CustCell : CustomCell
{
    protected override Control OnCreateCell(CellEventArgs args)
    {
        var textBox = new Label() { TextAlignment = TextAlignment.Left };
        return textBox;
    }

    protected override void OnConfigureCell(CellEventArgs args, Control control)
    {
        if (control is not Label text) return;
        if (args.Item is not TreeGridItem item) return;
        if (item.Values?.FirstOrDefault() is not Flaggable flag) return;

        text.Text = flag.Name;
    }
}

var treeGridView = new TreeGridView()
{
  AllowMultipleSelection = false,
  Columns = {
    new GridColumn()
    {
      HeaderText = "Place",
      DataCell = new CustCell(), //(nameof(Flaggable.Name)),
    },
  },
  DataStore = treeData,
};

var bigFont = new Font(FontFamilies.Sans, 150, FontStyle.None, FontDecoration.None);
var label = new Label()
{
    Width = 200,
    Font = bigFont,
    Text = "🏁",
    TextAlignment = TextAlignment.Center
};

treeGridView.SelectedItemChanged += (s, e) => {
    if (treeGridView.SelectedItem is not TreeGridItem item) return;
    if (item.Values?.FirstOrDefault() is not Flaggable flag) return;
    label.Text = flag.Flag;
};

var layout = new DynamicLayout();
layout.BeginHorizontal();
layout.Add(treeGridView, true, true);
layout.Add(label, false, true);
layout.EndHorizontal();
 
var dialog = new Dialog()
{
  Width = 400,
  Height = 400,
  Content = layout,
  Resizable = true,
};

dialog.ShowModal(null);
```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
import scriptcontext as sc

import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions

import Eto.Forms as ef
import Eto.Drawing as ed

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

dialog = ef.Dialog()
dialog.Padding = ed.Padding(8)
dialog.BackgroundColor = ed.Colors.DimGray

button = ef.Button()
button.Text = "Click me!"

panel = ef.Panel()
panel.Padding = ed.Padding(8)
panel.BackgroundColor = ed.Colors.DarkGray
panel.Content = button

dialog.Content = panel
dialog.ShowModal(parent)
  ```

  </div>
</div>
