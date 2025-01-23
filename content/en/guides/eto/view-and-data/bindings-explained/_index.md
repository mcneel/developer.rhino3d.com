+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto"]
description = "A deep dive into Eto Bindings"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model", "Binding" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "How do Bindings Work?"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ ]

[page_options]
byline = true
toc = true
toc_type = "single"
+++

{{< call-out note "View Models" >}}
  This section is not for Python, python cannot use View Models in the same way as C#.
{{< /call-out >}}

## Directionality

Below is a simple Eto Binding that binds both the DataContext and the Checked state of a CheckBox to a View Model.

``` cs
using Eto.Forms;
using Eto.Drawing;

public class MainForm : Form
{
  public MainForm()
  {
    Size = new Size(200, 200);
    DataContext = new ViewModel();

    var cb = new CheckBox() { Text = "Click Me" };
    cb.BindDataContext(b => b.Checked, (ViewModel vm) => vm.Checked);
    Content = cb;

    this.KeyDown += (s, e) => {
      if (this.DataContext is ViewModel vm)
      {
        vm.Checked = !vm.Checked;
        Invalidate(true);
      }
    }
  }
}

public class ViewModel
{
  public bool Checked { get; set; }
}
```

With this small View Model and UI we can notice the following behaviours

- Checking the check box will update the View Model

- Pressing a Key will update the View Model, but not the UI.

The current View Model and UI has a singular direction, data must be set by the UI or the two get out of sync.
Obviously this is non-optimal, it would be better if changing the View Model updated the UI as well, and then both were permanently in sync.


The View Model needs to notify the UI when it is changed.
We do this by implimenting `INotifyPropertyChanged` on the View Model, and expanding the properties.

``` cs
public class ViewModel : INotifyPropertyChanged
{

  private bool _checked { get; set; }
  public bool Checked
  {
    get => _checked;
    set
    {
      _checked = value;
      OnPropertyChanged(nameof(Checked));
    }
  }

  public event PropertyChangedEventHandler PropertyChanged;

  protected void OnPropertyChanged(string propertyName)
  {
    if (PropertyChanged != null)
      PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
  }

}
```
Looking at the View Model now, it seems a lot more complicated, let's walk through the changes and what they do.

1. INotifyPropertyChanged has been implimented
1. Checked has been expanded to also raise OnPropertyChanged when set
1. The PropertyChanged event has been added
1. A simple method to make calling the event easier has been added.

``` cs
public class ViewModel : INotifyPropertyChanged // 1.
{

  private bool _checked { get; set; }
  public bool Checked
  {
    // expanded getter returning _checked, no difference between this and get;
    get => _checked;
    set
    {
      // 2. The only difference between this and set is including OnPropertyChanged
        _checked = value;
        OnPropertyChanged(nameof(Checked));
    }
  }

  // 3. New event to invoke when a property changes
  //    When creating bindings, this event is subscribed to
  public event PropertyChangedEventHandler PropertyChanged;

  // 4. Helper method to make invoking the event simpler
  protected void OnPropertyChanged(string propertyName)
  {
    if (PropertyChanged != null)
      PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
  }

}
```

# How does this all work? Though? What? Why?

1. A view Constructor Starts
1. The DataContext is created and set
1. Am abstract Binding with the Data Context is created (View Model does not need to exist yet)

## Alternatives to IPropertyNotified
IPropertyNotified isn't strictly necessary to ensure ViewModel -> UI changes are propagated.
The following sample showcases the use of UpdateBindings, which will notify the UI as if `OnPropertyChange` was called for all bound properties.

``` cs
using System;

using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var cb = new CheckBox() { Text = "Click Me" };
var b = Binding.Property((MyViewModel vm) => vm.Checked);
cb.BindDataContext(c => c.Checked, b.ToBool(true, false));

var vm = new MyViewModel();
var dialog = new Dialog()
{
	MinimumSize = new Size(200, 200),
	DataContext = vm,
	Content = cb,
};

dialog.KeyDown += (s, e) => {
    vm.Checked = !vm.Checked;
    dialog.UpdateBindings(BindingUpdateMode.Destination);
};

public class MyViewModel
{
	public bool Checked { get; set; }
}

dialog.ShowModal();
```

# Callum, what about the other binding styles? Property names etc?

## Notes
- Bindings, when created, are added to the bindings in the Control (IBindable)
- INotifyProperty is necessary for VM -> UI

These 3 bindings are functionality identical

``` cs
cb.BindDataContext(c => c.Checked, (ViewModel vm) => vm.Checked);
cb.Bind<bool>(nameof(CheckBox.Checked), DataContext, nameof(ViewModel.Checked));
cb.CheckedBinding.BindDataContext(nameof(ViewModel.Checked));
```

## TroubleShooting

### Cannot convert lambda expression to type 'IndirectBinding<bool?>' because it is not a delegate type
Likely the types you're attempting to use are not able to be cast correctly. e.g bool and bool? are not friends.

Declaring Binding.Property instead of a lambda and using ToBool() will help.

``` cs
cb.BindDataContext(c => c.Checked, (ViewModel vm) => vm.Checked);
cb.BindDataContext(c => c.Checked, Binding.Property((ViewModel vm) => vm.Checked).ToBool(true, false));
```

## More Reading
[Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)