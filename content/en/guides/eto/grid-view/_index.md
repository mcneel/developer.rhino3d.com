+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Fundamentals" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux", "Fundamentals" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Grid Views"

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

An introduction to Grid Views.

{{< /column >}}
{{< column >}}

[Eto.Forms.GridView API Reference](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_GridView.htm)

{{< /column >}}
{{< /row >}}

</br>

Grid Views allow us to create columns and rows which are bound to a View Model.
This guide will cover all the eccentricities of Grid Views which can be confusing.

![Pixel Layout](/images/eto/controls/grid-view.png)

## Declaration

GridViews are defined by Columns which are bound to a list defining the rows.

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

```cs
using Eto.Forms;

var gridView = new GridView()
{
  Columns = {
    new GridColumn()
    {
      HeaderText = "Key"
    },
    new GridColumn()
    {
      HeaderText = "Value"
    },
  },
  // DataStore = ...
};

var dialog = new Dialog()
{
  Width = 200,
  Height = 200,
  Content = gridView,
};
```

  </div>
  <div class="codetab-content2" id="py2">

```py
import Eto.Forms as ef

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

dialog.ShowModal()
```

  </div>
</div>

## DataStore and Bindings

It is worth noting that Cells in Grids make use of "Indirect Bindings". Bindings which are handed entirely internally by Eto and do not require `control.BindDataContext` to be created.

When we define our column, we can represent the row as data in one of two days.

#### 1. As a data Object
Using a string allows us to specify a property name of the Data Object

#### 2. As an Array
Using a number as an index in the constructor will bind the cell to the Nth object in a list.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

```cs no-compile
var gridView = new GridView()
{
  Columns = {
    new GridColumn()
    {
      // Python cannot use this style, c# can
      DataCell = new TextBoxCell(nameof(MyDataObject.Property)), // <-- 1. This is an Indirect Binding
    },
    new GridColumn()
    {
      // Python AND C# can both use this style
      DataCell = new TextBoxCell(1), // <-- 2. This is an Indirect Binding
    },
  },
  DataStore = items
};
```

  </div>
  <div class="codetab-content3" id="py3">

``` py
# 2D List
list = [[1, 2], [3, 4]]
 ```

  </div>
</div>

{{< call-out note "Python Note" >}}
Note that Python MUST be a 2D list as bindings do not work the same way.
{{< /call-out >}}


<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content4" id="cs4">


``` cs
// 2D List
List<List<string>> _2dList { get; }
// 2D Array
string[,] _2dArray_ { get; }

// 1D List
List<MyObject> _1dList { get; }
// 1D Array
MyObject[] _1dArray { get; }
```

  </div>
  <div class="codetab-content4" id="py4">

  ```py
# 2D List
list = [[1, 2], [3, 4]]
  ```

  </div>
</div>

### Also mention ReloadData

Generally `ObservableCollection<T>` informs the UI of changes when the collection is updated. In GridViews this is not the case and a more specific reload is required `GridView.ReloadData()`. \

Reloading an ENTIRE GridView due to 1 cell changing would be very inefficient, and hence ReloadData lets us specify a Row to reload which is much more efficient.

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'py5')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content5" id="cs5">

```cs

```

  </div>
  <div class="codetab-content5" id="py5">

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
using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Collections.ObjectModel;

using Eto.Forms;
using Eto.Drawing;

using Rhino.UI;
 
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

class SheetModel : ViewModel
{
    public ObservableCollection<ObservableCollection<string>> Cells { get; } = new();

    public List<char> ColumnLabels { get; } = new List<char>() {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};

    public SheetModel(int rows, int cols)
    {
        for(int i = 0; i < rows; i++)
        {
            // var row = new ObservableCollection<string>(Enumerable.Repeat(string.Empty, cols));
            var row = new ObservableCollection<string>(Enumerable.Range(0, cols).Select(j => (j * i).ToString()));
            Cells.Add(row);
        }
    }

    public void Calculate()
    {
        for(int x = 0; x < Cells.Count; x++)
        {
            var currentRow = Cells[x];
            for(int y = 0; y < currentRow.Count; y++)
            {
                var cell = currentRow[y] ?? string.Empty;
                var match = Regex.Match(cell, @"=([a-zA-Z])([\d]+)");
                if (match.Groups.Count < 3) continue;
                
                string letter = match.Groups[1].Value.ToUpper();
                string number = match.Groups[2].Value;

                if (!int.TryParse(number, out int row)) continue;
                if (row < 0 || row > 10) continue;

                char c = letter.FirstOrDefault();

                int col = ColumnLabels .IndexOf(c);

                currentRow[y] = Cells[row-1][col];
                
                // Cells[x][y]
            }
        }
    }

    public void Clear()
    {
        foreach(var cell in Cells)
        {
            cell.Clear();
            for(int i = 0; i < 10; i++)
                cell.Add("0");
        }
    }
}

var cols = new char[] {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};

var model = new SheetModel(10, cols.Length);

var dialog = new Dialog()
{
  Padding = 4,
  DataContext = model
};

var gridView = new GridView()
{
    DataStore = model.Cells,
    Border = BorderType.Line,
    CanDeleteItem = (s) => false,
    AllowMultipleSelection = false,
    AllowEmptySelection = true,
    Cursor = Eto.Forms.Cursors.IBeam,
    GridLines = GridLines.Both,
};
gridView.CellEdited += (s, e) => {
    model.Calculate();
};

int i = 0;
foreach(char c in cols)
{
    var col = new GridColumn()
    {
        HeaderText = $"{c}",
        AutoSize = false,
        Width = 80,
        DataCell = new TextBoxCell(i++),
        Editable = true
    };

    gridView.Columns.Add(col);
};

var clearButton = new Button() { Text = "Clear All" };
clearButton.Click += (s,e) => {
    model.Clear();
    gridView.ReloadData(Enumerable.Range(0, cols.Length));
};

var closeButton = new Button() { Text = "Close" };
closeButton.Click += (s, e) => dialog.Close();

var buttonRow = new DynamicLayout() { Spacing = new Size(4, 0) };
buttonRow.BeginHorizontal();
buttonRow.AddSpace(true, true);
buttonRow.Add(clearButton, false, false);
buttonRow.Add(closeButton, false, false);
buttonRow.EndHorizontal();
 
dialog.Content = new StackLayout()
{
    Spacing = 4,
    Items = {
        gridView,
        buttonRow
    }
};
dialog.UseRhinoStyle();
dialog.ShowModal(parent);
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