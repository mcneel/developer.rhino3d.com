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

## A simple To Do list
<!-- One of my favourite tutorials is the React beginner [tutorial](https://react.dev/learn/tutorial-tic-tac-toe). -->

You have so many exciting things to learn in Eto, it might be good to make a small To Do list.

Let's start simple and show a window.

``` cs
using Eto.Forms;

var dialog = new Dialog() { Width = 200, Height = 200 };
dialog.ShowModal();
```

Hurray! That didn't take much code, and it's a great start.
Next lets add some content.

``` cs
using Eto.Forms;

var gridView = new GridView()
{
    Columns = {
        new GridColumn() { HeaderText = "+" },
        new GridColumn() { HeaderText = "Item" },
    },
};

var dialog = new Dialog()
{
  Width = 200,
  Height = 200,
  Content = gridView,
};
```

We've added a GridView, our first Eto control with some columns.
The UI looks a little sparse still. It would be nice to have some items in the UI.

``` cs
using System.Collections.Generic;

using Eto.Forms;

internal class ToDoItem
{
    public bool AddItem { get; set; } = false;
    public string Text { get; set; }
}

var items = new List<ToDoItem>()
{
  new ToDoItem() { Text = "Groceries" },
  new ToDoItem() { Text = "Feed Cat" },
  new ToDoItem() { Text = "Drink Water" },
};

var gridView = new GridView()
{
    Columns = {
        new GridColumn() { HeaderText = "+" },
        new GridColumn()
        {
            HeaderText = "Items",
            Editable = true,
            Expand = true,
            HeaderToolTip = "To Do Item",
            DataCell = new TextBoxCell(nameof(ToDoItem.Text))
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

The UI is looking great! It's starting to look like a list UI now, we have items in our list. It's just... lacking functionality. Let's add some functionality, and for this, we'll need, a _View Model_.


``` cs
using System.Collections.Generic;
using System.Collections.ObjectModel;

using Eto.Forms;

using Rhino.UI;

internal class ToDoItem
{
    public string Text { get; set; }
}

internal class ToDoModel : ViewModel
{
    public ObservableCollection<ToDoItem> Items { get; } = new();
}

var viewModel = new ToDoModel();
viewModel.Items.Add(new ToDoItem() { Text = "Groceries" });
viewModel.Items.Add(new ToDoItem() { Text = "Feed Cat" });
viewModel.Items.Add(new ToDoItem() { Text = "Drink Water" });

var buttonCell = new CustomCell()
{
    CreateCell = (cc) => 
    {
      var button = new Button() { Text = "+" };
      return button;
    }
};

var gridView = new GridView()
{
    Columns = {
        new GridColumn()
        {
          HeaderText = "+",
          DataCell = buttonCell,
          Width = 24,
        },
        new GridColumn()
        {
            HeaderText = "Items",
            Editable = true,
            Expand = true,
            HeaderToolTip = "To Do Item",
            DataCell = new TextBoxCell(nameof(ToDoItem.Text))
        },
    },
    DataStore = viewModel.Items,
};

var dialog = new Dialog()
{
  Width = 200,
  Height = 200,
  Content = gridView,
  DataContext = viewModel,
};

dialog.ShowModal();
```

The UI is starting to get chonky now! It still doesn't do anything, but at least it looks like it does!

Ok, the code is getting big now, we're going to focus in on sections now that the skeleton is there.

``` cs
var buttonCell = new CustomCell()
{
    CreateCell = (cc) => {
        int row = cc.Row;

        var button = new Button();
        button.Text = "+";
        button.Click += (s, e) => {
            try
            {
                Model.Items.RemoveAt(row);
            } catch {}
        };

        return new Panel() { Content = button, Padding = 2 };
    },
};
```

Awesome! Now we can remove items from the list, but we still can't add...

``` cs
internal class ToDoItem
{
    public bool AddItem { get; set; } = false; // <-- Add this
    public string Text { get; set; }
}
```

``` cs
var buttonCell = new CustomCell()
{
    CreateCell = (cc) => {
        int row = cc.Row;
        var element = Model.Items.ElementAtOrDefault(row);
        if (element is null) return new Panel();

        var button = new Button();
        if (element.AddItem)
        {
            button.Text = "+";
            button.Click += (s, e) => {
                try
                {
                    Model.Items.Insert(Model.Items.Count - 1, new ToDoItem() { Text = "..." });
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
```

# Putting it all together

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
        Model.Items.Add(new ToDoItem() { Text = "Buy Grocieries..."});
        Model.Items.Add(new ToDoItem() { Text = "", AddItem = true });
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
                    button.Text = "+";
                    button.Click += (s, e) => {
                        try
                        {
                            Model.Items.Insert(Model.Items.Count - 1, new ToDoItem() { Text = "..." });
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