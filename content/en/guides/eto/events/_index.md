+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
description = "An overview of events in Eto."
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Eto Events"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

Events in Eto are very similar to events everywhere else in C# and C# libraries with 2 noteworthy exceptions.

## Handled
Mouse and Key events follow a trickle-down system.

If a key, or key combination is not swallowed by the Operating System or MenuBar Commands, then the key press will first hit the ParentWindow and slowly move deeper into the UI tree until an event captures the key and considers it "Handled". If a TextArea is focused, this will, of course, receive the input keys first.

Mouse events are a little different, the trickle down system only interacts with elements whose bounding box contains the point of the mouse movement, the mouse does however start at the highest element(s) in the tree and work inwards, similar to key presses.

This trickle down will be immediately stopped whenever Handled is set to true. Some key or mouse events also require Handled to be set to true before they will fire. For example KeyUp will only fire if KeyDown is Handled. Also of note, Mac has a distinctive bonk which will sound if a key goes unhandled.

### Click Handlers
In this code sample you can see clicking the center also clicks every other panel, clicking the outer panels only affects the outer panels.

Uncommenting true in the constructors allows you to stop the trickle-down of the click handling.

``` cs
using System;

using Eto.Forms;
using Eto.Drawing;

public class ClickPanel : Panel
{
    private Random rand { get; } = new();
    private bool Handled { get; }

    public ClickPanel(bool handled = false)
    {
        Padding = 18;
        UpdateBackground();
        Handled = handled;
    }

    protected override void OnMouseDown(MouseEventArgs e)
    {
        UpdateBackground();
        e.Handled = Handled;
        base.OnMouseDown(e);
    }

    private void UpdateBackground()
    {
        byte[] buffer = new byte[3];
        System.Random.Shared.NextBytes(buffer);
        this.BackgroundColor = Color.FromArgb(buffer[0], buffer[1], buffer[2]);
        this.Invalidate();
    }

}

var dialog = new Dialog()
{
    Width = 200,
    Height = 200,
    Content = new ClickPanel(/*true*/)
    {
        Content = new ClickPanel(/*true*/)
        {
            Content = new ClickPanel(/*true*/)
            {
                Content = new ClickPanel(/*true*/)
                {
                    Content = new ClickPanel(/*true*/)
                }
            }
        }
    }
};

dialog.ShowModal();
```

## Overriding events
Overriding events in Eto is quite common, it's extremely important to call `base.<event>` inside this overridden event or else subscribing to this event will not work.

``` cs
using System;

using Eto.Forms;

public class MyButton : Button
{
    protected override void OnClick(EventArgs e)
    {
      // base.OnClick(e); // Uncomment to re-enable event subscription
    }
}

var button = new MyButton() { Text = "Click me"};

var dialog = new Dialog()
{
    Width = 200,
    Height = 200,
    Content = button,
};

button.Click += (s, e) => {
    button.Visible = false;
    dialog.Invalidate(true);
};

dialog.ShowModal();
```