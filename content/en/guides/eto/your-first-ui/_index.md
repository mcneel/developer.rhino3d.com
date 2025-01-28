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