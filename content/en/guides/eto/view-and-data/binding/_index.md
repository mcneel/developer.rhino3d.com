+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto"]
description = "An introduction to Bindings in Eto"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model", "Binding" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "Binding"
type = "guides"

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
  This section is not for Python, python cannot use View Models and bindings in the same way as C#.
{{< /call-out >}}

# Introduction
Bindings pair properties in view models with UI Elements in the Eto Layout.
Let's look at a very simple example.

``` cs
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

public class ViewModel
{
  public string Name { get; set; }
}

var nameInput = new TextBox() { Width = 300 };
nameInput.BindDataContext(t => t.Text, (ViewModel vm) => vm.Name);

var viewModel = new ViewModel();
var myDialog = new Dialog()
{
  Padding = 12,
  Title = "What is your Name?",
  DataContext = viewModel,
  Content = nameInput
};

myDialog.ShowModal(parent);
RhinoApp.WriteLine(viewModel.Name);
```

If we use the Script Editor to run this script, a dialog appears with a text box. We can then enter text and hit close. You should see your inputted text printed to the command line.

Let's examine what happened.
1. A ViewModel with a `Name` property was stored as the data context of a Dialog
1. A TextBox's `Text` property was "bound" to the ViewModel's `Name` property in a binding that is stored in the Dialog
1. When changing the `Text` property of the TextBox, the `Name` property in the ViewModel is updated with the value

# More Binding
Binding goes beyond BindDataContext, even if that might be enough for a simpler UI.

Any binding in Eto can be created with [`control.Bind<T>`](http://pages.picoe.ca/docs/api/html/Methods_T_Eto_Forms_IBindable.htm), many controls will have binding methods or properties to simplify this.
e.g

- [`CheckBox.CheckedBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_CheckBox_CheckedBinding.htm)
- [`TextControl.TextBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_TextControl_TextBinding.htm)
- [`DropDown.ItemImageBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_DropDown_ItemImageBinding.htm)

These create half the binding for you but aren't strictly necessary.

These 3 snippets are functionally identical but achieve it through helper methods and properties
``` cs
cb.Bind<bool>(nameof(CheckBox.Checked), DataContext, nameof(ViewModel.Checked));
cb.BindDataContext(c => c.Checked, (ViewModel vm) => vm.Checked);
cb.CheckedBinding.BindDataContext(nameof(ViewModel.Checked));
```

Lastly there are the [BindableExtensions](http://pages.picoe.ca/docs/api/html/Methods_T_Eto_Forms_BindableExtensions.htm).

All bindings when created on an object are added to the [`IBindable.Bindings`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_IBindable_Bindings.htm) property that all Controls have.


# Examples
Why are some of the View Models below more complex than above? This page conveniently side steps that for now, check out [this page](../bindings-explained/) to learn why.


### Check Box

``` cs
using Eto.Forms;
using Eto.Drawing;

using Rhino.UI;
 
public class MyViewModel : ViewModel
{
  private bool _checked { get; set; }
  public bool Checked
  {
    get => _checked;
    set
    {
      _checked = value;
      RaisePropertyChanged(nameof(Checked));
    }
  }
}

var checkBox = new CheckBox()
{
    Text = "Check Please",
    Checked = true,
};
checkBox.BindDataContext(c => c.Checked, Binding.Property((MyViewModel vm) => vm.Checked).ToBool(true, false));
// Also works
// checkBox.CheckedBinding.BindDataContext(Binding.Property((MyViewModel vm) => vm.Checked).ToBool(true, false));
 
var dialog = new Dialog()
{
    Padding = 8,
    Content = checkBox,
    DataContext = new MyViewModel()
};
 
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

### Text Box

``` cs
using Eto.Forms;
using Eto.Drawing;
using Rhino.UI;
 
public class MyViewModel : ViewModel
{
  private string _text { get; set; }
  public string Text
  {
    get => _text;
    set
    {
      _text = value;
      RaisePropertyChanged(nameof(Text));
    }
  }
}
 
var textBox = new TextBox()
{
    TextAlignment = TextAlignment.Center,
    Width = 200,
    PlaceholderText = "example@email.com"
};
textBox.BindDataContext(tb => tb.Text, (MyViewModel vm) => vm.Text);
 
var dialog = new Dialog()
{
    Padding = 8,
    Content = textBox
};
 
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

### Drop Down

``` cs
using System;
using System.Collections.ObjectModel;

using Eto.Forms;
using Eto.Drawing;

using Rhino.UI; 

public class MyViewModel : ViewModel
{
  private int _selectedIndex { get; set; }
  public int SelectedIndex { get; set; }
  {
    get => _selectedIndex;
    set
    {
      _selectedIndex = value;
      RaisePropertyChanged(nameof(SelectedIndex));
    }
  }

  public ObservableCollection<string> Choices { get; set; } = new () {
    "Point", "Curve", "Brep",
  };
}
 
var dropDown = new DropDown();
dropDown.BindDataContext(dd => dd.DataStore, (MyViewModel vm) => vm.Choices);
dropDown.BindDataContext(dd => dd.SelectedIndex, (MyViewModel vm) => vm.SelectedIndex);
 
var dialog = new Dialog()
{
    Padding = 8,
    Content = dropDown,
    DataContext = new MyViewModel(),
};
 
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

## More Reading
- [Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)
- [Complex Bindings](../complex-bindings)
- [Bindings Deep Dive ](../bindings-explained)