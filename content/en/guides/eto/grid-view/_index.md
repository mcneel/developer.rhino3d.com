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

{{< call-out note "Cells" >}}
  It's advisable to read about [Cells](../cells) before Grid Views
{{< /call-out >}}

{{< row >}}
{{< column >}}

An introduction to Grid Views.

{{< /column >}}
{{< column >}}

[Eto.Forms.GridView API Reference](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_GridView.htm)

{{< /column >}}
{{< /row >}}

Grid Views let you display a collection of items as a table of rows and columns. Each column controls how its cells are rendered and edited; the rows are driven by a single data store that you bind to the view. This guide covers how to declare a Grid View, how to populate it, and the binding model that ties cells to your data.

![Grid View](/images/eto/controls/grid-view.png)

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

using Rhino.UI;

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

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content2" id="py2">

```py
import Eto.Forms as ef
from Rhino.UI import RhinoEtoApp

keyColumn = ef.GridColumn()
keyColumn.HeaderText = "Key"

valueColumn = ef.GridColumn()
valueColumn.HeaderText = "Value"

gridView = ef.GridView()
# gridView.DataStore = ...
gridView.Columns.Add(keyColumn)
gridView.Columns.Add(valueColumn)

dialog = ef.Dialog()
dialog.Width = 200
dialog.Height = 200
dialog.Content = gridView

parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__)
dialog.ShowModal(parent)
```

  </div>
</div>

</br>

## DataStore and Bindings

Cells in Grids make use of "Indirect Bindings". Bindings which are handled entirely internally by Eto and do not require `control.BindDataContext` to be used.

When we define our column, we can represent the row as data in one of two ways.

#### 1. As a data Object
Defining a row as a data object is a very strong way to define a GridView. The constructor of most data cells allows a string which is the name of a property on the Data Object.

#### 2. As an Array
A row can also be defined as an Array or List of data. Using a number as an index in the constructor will bind the cell to the Nth object in a list.

An index refers to a position in the row, not to the column the user sees on screen. Set `AllowColumnReordering = false` on the Grid so the two cannot drift apart.

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
      // 1. This is an Indirect Binding
      // Python cannot use this style, c# can
      DataCell = new TextBoxCell(nameof(MyDataObject.Property)),
    },
    new GridColumn()
    {
      // 2. This is an Indirect Binding
      // Python AND C# can both use this style
      DataCell = new TextBoxCell(1),
    },
  }
};
```

  </div>
  <div class="codetab-content3" id="py3">

``` py no-compile
# 1. This is an Indirect Binding
# Python cannot use this style (even though the syntax is valid), c# can
column_1 = ef.GridColumn()
column_1.DataCell = ef.TextBoxCell("Property")

# 2. This is an Indirect Binding
# Python AND C# can both use this style
column_2 = ef.GridColumn()
column_2.DataCell = ef.TextBoxCell(1)

grid_view = ef.GridView()
grid_view.Columns.Add(column_1)
grid_view.Columns.Add(column_2)
 ```

  </div>
</div>

</br>

## Data object examples

Below are some examples of valid data store inputs.

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content4" id="cs4">

``` cs no-compile
// Lists of Lists
var _2dList = new List<object> {
  new List<int> { 1, 2, 3 },
  new List<string> { "one", "two", "three" }
};

// Data Objects
var _1dList = new List<MyObject>
{
    new MyObject(1, "one"),
    new MyObject(2, "two"),
    new MyObject(3, "three"),
};
```

  </div>
  <div class="codetab-content4" id="py4">

  ```py no-compile
from System.Collections.Generic import List

# Each row has to support IList indexing for TextBoxCell(int) to read it.
# A GridItem does, so a plain Python list of GridItems is fine.
items = [ef.GridItem([False, "Cheese"]), ef.GridItem([True, "Crackers"])]

# Rows of raw values need a .NET list. A Python list does not satisfy IList,
# so TextBoxCell(0) would render nothing.
items = List[List[object]]()
items.Add(List[object]([1, "one"]))
items.Add(List[object]([2, "two"]))
items.Add(List[object]([3, "three"]))
  ```

  </div>
</div>

</br>

### ReloadData

Generally `ObservableCollection<T>` informs the UI of changes when the collection is updated. In GridViews this is not the case and a more specific reload is required `GridView.ReloadData()`.

<!-- TODO : Are you sure about this? Why do we EVER use this for samples then? -->

Reloading an ENTIRE GridView due to 1 cell changing would be very inefficient, and hence ReloadData lets us specify a Row to reload which is much more efficient.

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'py5')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content5" id="cs5">

```cs no-compile
// Reload a single row by index
gridView.ReloadData(new[] { 0 });

// Reload several rows at once
gridView.ReloadData(Enumerable.Range(0, gridView.DataStore.Count()));
```

  </div>
  <div class="codetab-content5" id="py5">

```py no-compile
from System.Collections.Generic import List

# Reload a single row by index
gridView.ReloadData(List[int]([0]))

# Reload several rows at once
gridView.ReloadData(List[int](list(range(len(gridView.DataStore)))))
```

  </div>
</div>

## Example Code

### Our first Grid View

For this example we'll build a very simple spreadsheet application.
Starting off with the Basic layout and some dummy data (otherwise the UI looks quite disappointing).

![Empty Grid View](/images/eto/tutorials/grid-view-01.png)

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

```cs
using System.Collections.Generic;

using Eto.Forms;
using Eto.Drawing;

using Rhino.UI;

var gridView = new GridView()
{
    // Styling
    Border = BorderType.Line,
    GridLines = GridLines.Both,
    
    // Dummy Data
    DataStore = new List<List<string>>
    {
        new List<string>() { "None" }
    }
};

// Use a series of letters to create all the Columns

var cols = new string[] { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
foreach(var c in cols)
{
    var col = new GridColumn()
    {
        HeaderText = c,
        
        // The Data Cell is created for each Cell
        DataCell = new TextBoxCell(0),
    };

    gridView.Columns.Add(col);
};

var clearButton = new Button() { Text = "Clear All" };
var closeButton = new Button() { Text = "Close" };

// Organise our layout nicely
var buttonRow = new DynamicLayout() { Spacing = new Size(4, 0) };
buttonRow.BeginHorizontal();
buttonRow.AddSpace(true, true);
buttonRow.Add(clearButton, false, false);
buttonRow.Add(closeButton, false, false);
buttonRow.EndHorizontal();

// Create the Dialog that hosts our UI elements
var dialog = new Dialog()
{
  Padding = 4,
  Content = new StackLayout()
  {
      Spacing = 4,
      Items = {
          gridView,
          buttonRow
      }
  }
};

closeButton.Click += (s, e) => dialog.Close();

// Make sure we parent the dialog correctly
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

  </div>
  <div class="codetab-content1" id="py1">

```py
import Eto.Forms as ef
import Eto.Drawing as ed
from Rhino.UI import RhinoEtoApp

from System.Collections.Generic import List

gridView = ef.GridView()
gridView.Border = ef.BorderType.Line
gridView.GridLines = ef.GridLines.Both

# Dummy data so the grid renders with something in it
row = List[object]()
row.Add("None")

data = List[List[object]]()
data.Add(row)

gridView.DataStore = data

# Use a series of letters to create all the Columns
cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for c in cols:
    col = ef.GridColumn()
    col.HeaderText = c

    # The Data Cell is created for each Cell
    col.DataCell = ef.TextBoxCell(0)

    gridView.Columns.Add(col)

clearButton = ef.Button()
clearButton.Text = "Clear All"

closeButton = ef.Button()
closeButton.Text = "Close"

# Organise our layout nicely
buttonRow = ef.DynamicLayout()
buttonRow.Spacing = ed.Size(4, 0)
buttonRow.BeginHorizontal()
buttonRow.AddSpace(True, True)
buttonRow.Add(clearButton, False, False)
buttonRow.Add(closeButton, False, False)
buttonRow.EndHorizontal()

stackLayout = ef.StackLayout()
stackLayout.Spacing = 4
stackLayout.Items.Add(ef.StackLayoutItem(gridView))
stackLayout.Items.Add(ef.StackLayoutItem(buttonRow))

# Create the Dialog that hosts our UI elements
dialog = ef.Dialog()
dialog.Padding = ed.Padding(4)
dialog.Content = stackLayout

closeButton.Click += lambda s, e: dialog.Close()

# Make sure we parent the dialog correctly
parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__)
dialog.ShowModal(parent)
```

  </div>
</div>

</br>

### Building a Mini Spreadsheet

Building on the previous example, this version backs the grid with a view model, lets cells reference each other with a `=A1` style formula, and adds a Clear button that resets the sheet.

<div class="codetab">
  <button class="tablinks10" onclick="openCodeTab(event, 'cs10')" id="defaultOpen10">C#</button>
  <button class="tablinks10" onclick="openCodeTab(event, 'py10')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content10" id="cs10">

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
    // What the grid shows. The GridView edits this directly.
    public ObservableCollection<ObservableCollection<string>> Cells { get; } = new();

    // What the user typed. Kept apart so a formula survives being displayed as its result.
    public List<List<string>> Formulas { get; } = new List<List<string>>();

    public List<char> ColumnLabels { get; } = new List<char>() {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'};

    public SheetModel(int rows)
    {
        for(int i = 0; i < rows; i++)
        {
            var values = Enumerable.Range(0, ColumnLabels.Count).Select(j => (j * i).ToString()).ToList();
            Cells.Add(new ObservableCollection<string>(values));
            Formulas.Add(new List<string>(values));
        }
    }

    public void SetFormula(int row, int col, string text)
    {
        if (row < 0 || row >= Formulas.Count) return;
        if (col < 0 || col >= Formulas[row].Count) return;

        Formulas[row][col] = text ?? string.Empty;
    }

    public void Calculate()
    {
        for(int x = 0; x < Formulas.Count; x++)
            for(int y = 0; y < Formulas[x].Count; y++)
                Cells[x][y] = Resolve(x, y);
    }

    string Resolve(int x, int y)
    {
        var formula = Formulas[x][y] ?? string.Empty;
        var match = Regex.Match(formula, @"^=([a-zA-Z])(\d+)$");
        if (!match.Success) return formula;

        if (!int.TryParse(match.Groups[2].Value, out int row)) return formula;
        if (row < 1 || row > Formulas.Count) return formula;

        char c = match.Groups[1].Value.ToUpper().FirstOrDefault();
        int col = ColumnLabels.IndexOf(c);
        if (col < 0 || col >= Formulas[row - 1].Count) return formula;

        // A cell pointing at itself would never settle on a value.
        if (row - 1 == x && col == y) return formula;

        return Cells[row - 1][col] ?? string.Empty;
    }

    public void Clear()
    {
        for(int x = 0; x < Cells.Count; x++)
        {
            for(int y = 0; y < Cells[x].Count; y++)
            {
                Cells[x][y] = "0";
                Formulas[x][y] = "0";
            }
        }
    }
}

var model = new SheetModel(10);

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
    AllowColumnReordering = false,
    AllowMultipleSelection = false,
    AllowEmptySelection = true,
    Cursor = Eto.Forms.Cursors.IBeam,
    GridLines = GridLines.Both,
};
gridView.CellEdited += (s, e) => {
    // The grid has already written the typed text into Cells, so capture it as the formula first.
    model.SetFormula(e.Row, e.Column, model.Cells[e.Row][e.Column]);
    model.Calculate();
    gridView.ReloadData(Enumerable.Range(0, model.Cells.Count));
};

int i = 0;
foreach(char c in model.ColumnLabels)
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
    gridView.ReloadData(Enumerable.Range(0, model.Cells.Count));
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

dialog.ShowModal(parent);
  ```

  </div>
  <div class="codetab-content10" id="py10">

```py
import re

import Eto.Forms as ef
import Eto.Drawing as ed
from Rhino.UI import RhinoEtoApp

from System.Collections.ObjectModel import ObservableCollection
from System.Collections.Generic import List

parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__)


class SheetModel:
    def __init__(self, rows):
        self.ColumnLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        # What the grid shows. The GridView edits this directly.
        self.Cells = ObservableCollection[ObservableCollection[str]]()

        # What the user typed. Kept apart so a formula survives being displayed as its result.
        self.Formulas = []

        for i in range(rows):
            values = [str(i * j) for j in range(len(self.ColumnLabels))]

            row = ObservableCollection[str]()
            for value in values:
                row.Add(value)

            self.Cells.Add(row)
            self.Formulas.append(list(values))

    def SetFormula(self, row, col, text):
        if row < 0 or row >= len(self.Formulas):
            return
        if col < 0 or col >= len(self.Formulas[row]):
            return

        self.Formulas[row][col] = text or ""

    def Calculate(self):
        for x in range(len(self.Formulas)):
            for y in range(len(self.Formulas[x])):
                self.Cells[x][y] = self.Resolve(x, y)

    def Resolve(self, x, y):
        formula = self.Formulas[x][y] or ""
        match = re.match(r"^=([a-zA-Z])(\d+)$", formula)
        if match is None:
            return formula

        row = int(match.group(2))
        if row < 1 or row > len(self.Formulas):
            return formula

        letter = match.group(1).upper()
        if letter not in self.ColumnLabels:
            return formula

        col = self.ColumnLabels.index(letter)
        if col >= len(self.Formulas[row - 1]):
            return formula

        # A cell pointing at itself would never settle on a value.
        if row - 1 == x and col == y:
            return formula

        return self.Cells[row - 1][col] or ""

    def Clear(self):
        for x in range(self.Cells.Count):
            for y in range(self.Cells[x].Count):
                self.Cells[x][y] = "0"
                self.Formulas[x][y] = "0"


model = SheetModel(10)

dialog = ef.Dialog()
dialog.Padding = ed.Padding(4)
dialog.DataContext = model

gridView = ef.GridView()
gridView.DataStore = model.Cells
gridView.Border = ef.BorderType.Line
gridView.AllowColumnReordering = False
gridView.AllowMultipleSelection = False
gridView.AllowEmptySelection = True
gridView.Cursor = ef.Cursors.IBeam
gridView.GridLines = ef.GridLines.Both


def on_cell_edited(s, e):
    # The grid has already written the typed text into Cells, so capture it as the formula first.
    model.SetFormula(e.Row, e.Column, model.Cells[e.Row][e.Column])
    model.Calculate()
    gridView.ReloadData(List[int](list(range(model.Cells.Count))))


gridView.CellEdited += on_cell_edited

for i, c in enumerate(model.ColumnLabels):
    col = ef.GridColumn()
    col.HeaderText = c
    col.AutoSize = False
    col.Width = 80
    col.DataCell = ef.TextBoxCell(i)
    col.Editable = True
    gridView.Columns.Add(col)

clearButton = ef.Button()
clearButton.Text = "Clear All"


def on_clear(s, e):
    model.Clear()
    gridView.ReloadData(List[int](list(range(model.Cells.Count))))


clearButton.Click += on_clear

closeButton = ef.Button()
closeButton.Text = "Close"
closeButton.Click += lambda s, e: dialog.Close()

buttonRow = ef.DynamicLayout()
buttonRow.Spacing = ed.Size(4, 0)
buttonRow.BeginHorizontal()
buttonRow.AddSpace(True, True)
buttonRow.Add(clearButton, False, False)
buttonRow.Add(closeButton, False, False)
buttonRow.EndHorizontal()

stackLayout = ef.StackLayout()
stackLayout.Spacing = 4
stackLayout.Items.Add(ef.StackLayoutItem(gridView))
stackLayout.Items.Add(ef.StackLayoutItem(buttonRow))

dialog.Content = stackLayout

dialog.ShowModal(parent)
```

  </div>
</div>
