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

## Tic Tac EToe
<!-- One of my favourite tutorials is the React beginner [tutorial](https://react.dev/learn/tutorial-tic-tac-toe). -->

Tic Tac Toe is a very good and simple example to get started, it requires some view and model logic, and a message box.
In other pages code samples are complete, as this page builds an entire app, samples will be shortened for brevity where appropriate.

## Starting out
The below code gives us a Dialog. If this is your first desktop UI, congratulations!

``` cs
using Eto.Forms;

using Rhino.UI;

var dialog = new Dialog()
{
  Width = 300,
  Height = 300,
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

## Layout
The dialog is looking pretty boring at the moment, but we can fix that by adding some buttons.

``` cs
using Eto.Forms;
using Eto.Drawing;

using Rhino.UI;

var layout = new TableLayout()
{
  Spacing = new (4,4),
  Rows = {
    new TableRow(new Button(), new Button(), new Button()),
    new TableRow(new Button(), new Button(), new Button()),
    new TableRow(new Button(), new Button(), new Button())
  }
};

var dialog = new Dialog()
{
  Padding = 8,
  Content = layout
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

## Buttons

The dialog is now populated with 9 buttons, a perfect 3x3 grid.
But the buttons look a bit flat and don't do anything currently which isn't much fun.

``` cs
var layout = new TableLayout()
{
  Spacing = new (4,4),
};

for (int x = 0; x < 3; x++)
{
  var row = new TableRow();
  for (int y = 0; y < 3; y++)
  {
    var button = new Button() { Width = 80, Height = 80 };
    row.Cells.Add(button);
  }
  layout.Rows.Add(row);
}
```

Now let's put the fun in functionality and give the buttons a click action.

``` cs
var button = new Button() { Width = 80, Height = 80 };
button.Click += (s, e) => {
  button.Text = "X";
};
```

## X Wins!
Now when the buttons are clicked, we can see the button reads "X", which is great news for X and bad news for O.
Let's make the buttons alternate.

``` cs
bool xTurn = true;
for (int x = 0; x < 3; x++)
{
  var row = new TableRow();
  for (int y = 0; y < 3; y++)
  {
    var button = new Button() { Width = 80, Height = 80 };
    button.Click += (s, e) => {
        button.Text = xTurn ? "X" : "O";
        xTurn = !xTurn;
    };
    row.Cells.Add(button);
  }
  layout.Rows.Add(row);
}
```

## Tic Tac Toe
With the above code, you have a simple Tic Tac Toe game running in Eto.
But you might notice that clicking an already clicked button flips the text! Which shouldnt be possible. So let's disable this possibility.

``` cs
button.Click += (s, e) => {
    button.Text = xTurn ? "X" : "O";
    xTurn = !xTurn;
    button.Enabled = false;
};
```

## Advancing

Currently we can play Tic Tac Toe, but the game doesn't detect a winner, or declare it. To do this we're going to need to some more power in our View. We'll create a View Model and add data context to the dialog

``` cs
internal class ViewModel
{

}

// ...

var dialog = new Dialog()
{
  DataContext = new ViewModel(),
  Content = layout,
  Width = 300,
  Height = 300,
};
```


## Wrapping it all up
Ok done, wow.

``` cs
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

using System;
using System.Linq;
using System.Collections.Generic;


internal enum Status
{
    Continue,
    Draw,
    XWin,
    OWin
}

internal class ViewModel
{

  private bool IsCross { get; set; } = false;

  public string NextStep()
  {
    IsCross = !IsCross;
    return IsCross ? "X" : "O";
  }

  public Status CheckWinner(TableLayout layout)
  {
    var buttons = layout.Children.OfType<Button>();

    var status = Status.Continue;

    for(int x = 0; x < 3; x++)
    {
      var vertColValues = GetRowData(buttons, p => p.X == x);
      if (TryGetStatus(vertColValues, out status))
        return status;
    }
    
    for(int y = 0; y < 3; y++)
    {
      var hozColValues = GetRowData(buttons, p => p.Y == y);
      if (TryGetStatus(hozColValues, out status))
        return status;
    }

    var lineValues1 = GetRowData(buttons, p => p.Y == p.X);
    if (TryGetStatus(lineValues1, out status))
      return status;

    var lineValues2 = GetRowData(buttons, p => {
        var result = (p.X == 0f && p.Y == 2f) ||
              (p.X == 1f && p.Y == 1f) ||
              (p.X == 2f && p.Y == 0f);
        return result;
    });
    if (TryGetStatus(lineValues2, out status))
      return status;

    if (buttons.All(b => !string.IsNullOrEmpty(b.Text)))
      return Status.Draw;

    return Status.Continue;
  }

  private bool TryGetStatus(IEnumerable<string> values, out Status status)
  {
    status = Status.Continue;
    if (values.Count() != 3) return false;
    if (values.Any(v => String.IsNullOrEmpty(v))) return false;
    if (values.ToHashSet().Count != 1) return false;
    
    status = values.All(v => v.Equals("X")) ? Status.XWin : Status.OWin;
    return true;
  }

  private IEnumerable<string> GetRowData(IEnumerable<Button> buttons, Func<PointF, bool> predicate)
  {
    buttons = buttons.Where(b => predicate((PointF)b.Tag));
    return buttons.Select(b => b.Text);
  }

}

var layout = new TableLayout()
{
  Spacing = new (4,4)
};
for (int x = 0; x < 3; x++)
{
  var row = new TableRow();
  for (int y = 0; y < 3; y++)
  {
    var button = new Button() { Tag = new PointF(x,y), Width = 80, Height = 80 };
    button.Click += (s, e) => {
      var data = (layout.DataContext as ViewModel);
      var text = data.NextStep();
      button.Text = text;
      button.Enabled = false;

      var status = data.CheckWinner(layout);
      if (status != Status.Continue)
      {
        var message = status switch
        {
            Status.XWin => "X Wins!",
            Status.OWin => "O Wins!",
            _ => "It's a Draw!"
        };

        MessageBox.Show(message);
        layout.ParentWindow.Close();
      }
    };
    row.Cells.Add(button);
  }
  layout.Rows.Add(row);
}

var dialog = new Dialog()
{
  DataContext = new ViewModel(),
  Content = layout
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```