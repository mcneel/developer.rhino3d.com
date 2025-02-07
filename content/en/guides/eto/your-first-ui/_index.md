+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Your first Eto UI"
description = "As you may be new to Rhino, Eto and/or programming, this guide will focus entirely on a small fun eto app to get you started."

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++


![Your First UI](/images/eto/tutorials/your-first-ui.png)

## A simple To Do list
<!-- One of my favourite tutorials is the React beginner [tutorial](https://react.dev/learn/tutorial-tic-tac-toe). -->

You have so many exciting things to learn in Eto, it might be good to make a small To Do list.

Let's start simple and show a window.

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

var dialog = new Dialog()
{
  Width = 200,
  Height = 200
};

dialog.ShowModal();
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
from Eto.Forms import *
 
dialog = Dialog()
dialog.Width = 200
dialog.Height = 200

dialog.ShowModal()
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Your First Dialog](/images/eto/tutorials/your-first-dialog.png)

{{< /column >}}
{{< /row >}}

Creating a window in Eto isn't too complex in C# or python. Only 6 or 7 lines of code and a we're already making progress. The window is a bit empty though, lets add some content.

</br>

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

``` cs
using Eto.Forms;

var gridView = new GridView()
{
  Columns = {
    new GridColumn()
    {
      HeaderText = "+"
    },
    new GridColumn()
    {
      HeaderText = "Item"
    },
  },
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
from Eto.Forms import *

plusColumn = GridColumn()
plusColumn.HeaderText = "+"

itemColumn = GridColumn()
itemColumn.HeaderText = "Item"

gridView = GridView()
gridView.Columns.Add(plusColumn)
gridView.Columns.Add(itemColumn)

dialog = Dialog()
dialog.Width = 100
dialog.Height = 100
dialog.Content = gridView

dialog.ShowModal()
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Your First Content](/images/eto/tutorials/your-first-content.png)

{{< /column >}}
{{< /row >}}

</br>

We've added a GridView, our first Eto control along with some columns.
The UI looks a little sparse still. It would be nice to have some items in the UI.

</br>

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'py3')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content3" id="cs3">

``` cs
using System.Collections.Generic;

using Eto.Forms;

internal class ToDoItem
{
    public string Text { get; set; }

    public ToDoItem(string text)
    {
      Text = text;
    }
}

var items = new List<ToDoItem>()
{
  new ToDoItem("Groceries"),
  new ToDoItem("Feed Cat"),
  new ToDoItem("Drink Water"),
};

var gridView = new GridView()
{
  Columns = {
    new GridColumn()
    {
      HeaderText = "+"
    },
    new GridColumn()
    {
      HeaderText = "Items",
      Editable = true,
      DataCell = new TextBoxCell("Text")
    },
  },
  DataStore = items,
};

var dialog = new Dialog()
{
  Width = 200,
  Height = 200,
  Content = gridView,
};

dialog.ShowModal();
```

  </div>
  <div class="codetab-content3" id="py3">

  ```py
# TODO : Items do not appear in python
from Eto.Forms import *

class ToDoItem():
  def __init__(self, text: str):
    self.Text = text

items = (
  ToDoItem("Groceries"),
  ToDoItem("Feed Cat"),
  ToDoItem("Drink Water"),
  )

plusColumn = GridColumn()
plusColumn.HeaderText = "+"

itemColumn = GridColumn()
itemColumn.HeaderText = "Item"
itemColumn.Editable = True
itemColumn.DataCell = TextBoxCell("Text")

gridView = GridView()
gridView.Columns.Add(plusColumn)
gridView.Columns.Add(itemColumn)
gridView.DataStore = items,

dialog = Dialog()
dialog.Width = 200
dialog.Height = 200
dialog.Content = gridView

dialog.ShowModal()
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Your First Data](/images/eto/tutorials/your-first-data.png)

{{< /column >}}
{{< /row >}}

</br>

The UI is looking great! It's starting to look like a list UI now, we have items in our list. It's just not very functional. Let's add some functionality.

The code is getting big now, we're going to focus in on sections now that the skeleton is there.

</br>

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'py4')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content4" id="cs4">

``` cs
var buttonCell = new CustomCell()
{
    CreateCell = (cc) => 
    {
      var button = new Button() { Text = "x" };
      return button;
    }
};

var gridView = new GridView()
{
    Columns = {
        new GridColumn()
        {
          HeaderText = "+",
          Width = 24,
          DataCell = buttonCell,
```

  </div>
  <div class="codetab-content4" id="py4">

``` py
```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Your First Data](/images/eto/tutorials/your-first-button.png)

{{< /column >}}
{{< /row >}}

</br>

The UI still doesn't do anything, but it's starting to look like it does. Let's fix that and make it functional.

</br>

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'py5')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content5" id="cs5">

``` cs
var buttonCell = new CustomCell()
{
    CreateCell = (cc) => {
        var button = new Button();
        button.Text = "x";
        button.Click += (s, e) => {
            try
            {
              // Row/index can change, so we don't use that here
                items.Remove((ToDoItem)cc.Item);
            } catch {}
        };

        return new Panel() { Content = button, Padding = 2 };
    },
};
```

  </div>
  <div class="codetab-content5" id="py5">

``` py
```

  </div>
</div>

That's odd. Why doesn't the x button do anything?
That's because the data behind our UI isn't informing our GridView of the updates.
Luckily the solution is pretty simple.

``` cs
var items = new List<ToDoItem>() // Old
var items = new ObservableCollection<ToDoItem>() // New
```

[ObservableCollections](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=net-9.0) notify the UI of changes in the collection. It is advisable to NEVER replace the collection with a new collection, but instead clear and refill.

We'll create one last change, then a small refactor is in order.

``` cs
internal class ToDoItem
{
    public string Text { get; set; }
    public bool AddItem { get; set; } = false; // <-- Add a new property
 
    public ToDoItem(string text)
    {
      Text = text;
    }
}

var items = new ObservableCollection<ToDoItem>()
{
  new ToDoItem("Groceries"),
  new ToDoItem("Feed Cat"),
  new ToDoItem("Drink Water"),
  new ToDoItem("..") { AddItem = true }, // <-- Add a new item
};

var buttonCell = new CustomCell()
{
    CreateCell = (cc) => {
        if (cc.Item is not ToDoItem element) return new Panel();

        var button = new Button();
        if (element.AddItem) // <-- AddItems only add
        {
            button.Text = "+";
            button.Click += (s, e) => {
                try
                {
                    items.Insert(items.Count - 1, new ToDoItem("..."));
                } catch {}
            };
        }
        else // <-- Otherwise they remove
        {
            button.Text = "✗";
            button.Click += (s, e) => {
                try
                {
                    items.Remove(element);
                } catch {}
            };
        }

        return new Panel() { Content = button, Padding = 2 };
    },
};
```

Now we're cooking 

Awesome! The UI can add or remove items from the list!

</br>

# Putting it all together
Below I've compiled all the code, and even added a few extra little bits to make the UI a bit nicer, they're not strictly necessary, but they should make it a touch nicer.

</br>


<div class="codetab">
  <button class="tablinks10" onclick="openCodeTab(event, 'cs10')" id="defaultOpen10">C#</button>
  <button class="tablinks10" onclick="openCodeTab(event, 'py10')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content10" id="cs10">

``` cs
using System;
using System.Linq;
using System.Collections.ObjectModel;

using Eto;
using Eto.Forms;

using Rhino.UI;

internal class ToDoItem
{
    public bool AddItem { get; set; } = false;
    public string Text { get; set; }

    public ToDoItem(string text)
    {
      Text = text;
    }
}

internal class ToDoModel : ViewModel
{
    public ObservableCollection<ToDoItem> Items { get; } = new();
}

internal class ToDoList : Dialog
{

    private ToDoModel Model => DataContext as ToDoModel;

    public ToDoList()
    {
        Width = 300;
        Height = 200;
        DataContext = new ToDoModel();
        Model.Items.Add(new ToDoItem("Buy Groceries..."));
        Model.Items.Add(new ToDoItem("") { AddItem = true });
        InitLayout();
    }

    private void InitLayout()
    {
        var buttonCell = new CustomCell()
        {
            CreateCell = (cc) => {
                int row = cc.Row;
                var element = Model.Items.ElementAtOrDefault(row);
                if (element is null) return new Panel();

                var button = new Button();
                if (element.AddItem)
                {
                    button.Text = "x";
                    button.Click += (s, e) => {
                        try
                        {
                            Model.Items.Insert(Model.Items.Count - 1, new ToDoItem("..."));
                        } catch {}
                    };
                }
                else
                {
                    button.Text = "✗";
                    button.Click += (s, e) => {
                        try
                        {
                            if (Model.Items[row].AddItem) return;
                            Model.Items.RemoveAt(row);
                        } catch {}
                    };
                }

                return new Panel() { Content = button, Padding = 2 };
            },
        };

        var gv = new GridView()
        {
            Border = BorderType.None,
            CanDeleteItem = (e) => true,
            GridLines = GridLines.None,
            RowHeight = 24,
            Columns = {
                new GridColumn()
                {
                    HeaderText = "+",
                    HeaderToolTip = "Click + to add, ✗ to remove",
                    DataCell = buttonCell,
                    Width = 24,
                    Expand = false,
                },
                new GridColumn()
                {
                    HeaderText = "Item",
                    Editable = true,
                    Expand = true,
                    HeaderToolTip = "To Do Item",
                    DataCell = new TextBoxCell(nameof(ToDoItem.Text))
                    {
                        AutoSelectMode = AutoSelectMode.OnFocus,
                        TextAlignment = TextAlignment.Left,
                    },
                },
            },
            DataStore = Model.Items,
        };

        Content = gv;
    }

}

var list = new ToDoList();
list.ShowModal(RhinoEtoApp.MainWindowForDocument(__rhino_doc__));
```

  </div>
</div>