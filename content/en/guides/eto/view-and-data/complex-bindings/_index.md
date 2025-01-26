+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto"]
description = "Complex Bindings in Eto"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model", "Binding" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "Complex Bindings"
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

## Introduction
If you haven't read [the introductory page](../binding) on bindings, start there.

Bindings in Eto are very powerful, very easy to chain together and as such can get complex. This page attempts to break all the exciting things that can be done with bindings and then use those knowledge chunks to build some of those complex bindings.

# Knowledge Chunks

## Conversions
### Convert\<T>
Convert\<t> makes converting a ViewModel property into a more View appropriate value very simple with the added bonus of keeping the data in the View Model and View simple. In the example below Enums are used for all the value operations whilst the binding takes care of the messy text.

``` cs
using Eto;
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var lb = new Label() { Text = "Go Me" };

var prop = Binding.Property((ViewModel vm) => vm.Value)
            .Convert((v) => {
    var str = v switch
    {
        MyEnum.Brie => "Brie.. Mmmm..",
        MyEnum.Cheddar => "Cheddar, my favourite!",
        MyEnum.Edam => "Edam? No Thanks,",
        MyEnum.Peccorino => "MMMMMMM",
        _ => "err!"
    };
    return str;
});
lb.BindDataContext(l => l.Text, prop);

var viewModel = new ViewModel();
var dialog = new Dialog()
{
  Padding = 8,
  MinimumSize = new Size(200, 200),
  Content = lb,
  DataContext = viewModel,
};

dialog.KeyDown += (s, e) => {
    if (e.Key == Keys.Up)
    {
        viewModel.MoveUp();
        e.Handled = true;
    }

    if (e.Key == Keys.Down)
    {
        viewModel.MoveDown();
        e.Handled = true;
    }
};

public enum MyEnum { Brie = 0, Cheddar, Edam, Peccorino }

public class ViewModel : Rhino.UI.ViewModel
{
  public MyEnum Value { get; set; }

  public void MoveUp()
  {
    Value = ++Value;
    if (Value > MyEnum.Peccorino)
    Value = MyEnum.Peccorino;
    RaisePropertyChanged(nameof(Value));
  }

  public void MoveDown()
  {
    Value = --Value;
    if (Value < 0)
        Value = 0;
    RaisePropertyChanged(nameof(Value));
  }

}

dialog.ShowModal();
```


### OfType\<T>
OfType conveniently allows for objects to be cast into other compatible types.
The below example uses a list of enums which can be exchanged for ints, very convenient for SelectedIndex.

``` cs
using System;
using System.Linq;
using System.Collections.ObjectModel;

using Eto;
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var dd = new DropDown()
{
    DataStore = new ObservableCollection<object>(Enum.GetValues<Days>().Cast<object>()),
};

var prop = Binding.Property((ViewModel vm) => vm.SelectedDay).OfType<int>();
dd.BindDataContext(l => l.SelectedIndex, prop);

var dialog = new Dialog()
{
  Padding = 8,
  MinimumSize = new Size(200, 200),
  Content = dd,
  DataContext = new ViewModel()
};

public enum Days { Monday = 0, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday }

public class ViewModel : Rhino.UI.ViewModel
{
    private Days _selectedDay { get; set; }

    public Days SelectedDay
    {
      get => _selectedDay;
      set
      {
        _selectedDay = value;
      }
    }
}

dialog.ShowModal();
```


### ToBool
ToBool offers an easy way to convert `bool?` and `bool` bindings. It seems silly and small, but as many View Models will want to use `bool` and many toggleable controls use `bool?`, it's super handy.

``` cs
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var cb = new CheckBox() { Text = "Click Me" };

// NOTE : Removing ToBool(...) will result in compilation errors
cb.BindDataContext(c => c.Checked, Binding.Property((MyViewModel vm) => vm.Checked).ToBool(true, false));

var dialog = new Dialog()
{
	MinimumSize = new Size(200, 200),
	DataContext = new MyViewModel(),
	Content = cb,
};

public class MyViewModel : ViewModel
{
  public bool Checked { get; set; }
}

dialog.ShowModal();
```

### Child
Child lets you access nested properties of a View Model, possibly even from a ViewModel inside the main Model.

``` cs
using Eto;
using Eto.Forms;
using Eto.Drawing;

using Rhino;
using Rhino.UI;

var cb = new CheckBox() { Text = "Click Me" };
cb.BindDataContext(cb => cb.Checked, Binding.Property((ViewModel vm) => vm.Model).Child(vc => vc.Checked).ToBool(true, false));

var dialog = new Dialog()
{
  Padding = 8,
  MinimumSize = new Size(200, 200),
  Content = cb,
  DataContext = new ViewModel(),
};

public class ViewModel : Rhino.UI.ViewModel
{
  public InnerViewModel Model { get; set; }	 = new();
}

public class InnerViewModel : Rhino.UI.ViewModel
{
  private bool _checked { get; set; } = false;
  public bool Checked
  {
    get => _checked;
    set
    {
      _checked = value;
      RaiseInvalidPropertyValue(nameof(Checked));
      RhinoApp.WriteLine("Checked!");
    }
  }
}

dialog.ShowModal();
```

<!-- TODO!
## Timings
### After Delay


``` cs

```


## Misc
### Catch Exception


``` cs

```


### GetValue & SetValue <-- No idea what these do


``` cs

```

-->

# Combining bindings together

Here is a more fully formed UI project with some of the bindings we used above all brought togehter.

Convert / Cast / Child / ToBool
// Enabled Binding would be good too

``` cs
using System;
using System.Linq;
using System.Collections.Generic;
using System.Collections.ObjectModel;

using Eto.Forms;
using Eto.Drawing;

using Rhino.UI;
using Rhino.UI.Controls;

public enum Geometry { None = 0, Point, Line, Curve, Brep, Mesh, Sphere, SubD }

public class MyViewModel : ViewModel
{
  public ChoicesModel Top { get; set; } = new ChoicesModel(Enum.GetValues<Geometry>().Except(new Geometry[] { Geometry.None }).Cast<object>());
  public ChoicesModel Bottom { get; set; } = new ChoicesModel( new object[] {});
}

public class ChoicesModel : ViewModel
{
  private int _selectedIndex { get; set; } = 0;

  public ObservableCollection<object> Choices { get; set; } = new();
  public int SelectedIndex {
    get => _selectedIndex;
    set
    {
        _selectedIndex = value;
        RaisePropertyChanged(nameof(SelectedIndex));
    }
  }

  public ChoicesModel(IEnumerable<object> data)
  {
    Choices = new(data);
  }
}

class DropDownDialog : Dialog
{
    private MyViewModel Model => DataContext as MyViewModel;

    private Button MoveUp { get; set; } = new Button() { Text = "↑" };
    private Button MoveDown { get; set; } = new Button() { Text = "↓" };

    private DropDown TopChoices { get; set; } = new DropDown() { Width = 200 };
    private DropDown BottomChoices { get; set; } = new DropDown() { Width = 200 };

    public DropDownDialog()
    {
        Width = 300;
        Padding = 8;
        DataContext = new MyViewModel();
        InitLayout();
        InitBindings();
    }

    private void InitLayout()
    {

        Content = new TableLayout() {
            Spacing = new Size(8, 8),
            Rows = {
                new TableRow(new Label() { Text = "Top" }),
                new TableRow(TopChoices, MoveDown),
                new TableRow(new Divider(), new Divider()),
                // new TableRow(null),
                new TableRow(new Label() { Text = "Bottom" }),
                new TableRow(BottomChoices, MoveUp)
            },
        };
    }

    private void InitBindings()
    {
        TopChoices.BindDataContext(tc => tc.DataStore, Binding.Property((MyViewModel vm) => vm.Top).Child(t => t.Choices).Cast<IEnumerable<object>>());
        TopChoices.SelectedIndexBinding.BindDataContext(Binding.Property((MyViewModel vm) => vm.Top).Child(t => t.SelectedIndex));
        
        BottomChoices.BindDataContext(tc => tc.DataStore, Binding.Property((MyViewModel vm) => vm.Bottom).Child(t => t.Choices).Cast<IEnumerable<object>>());
        BottomChoices.SelectedIndexBinding.BindDataContext(Binding.Property((MyViewModel vm) => vm.Bottom).Child(t => t.SelectedIndex));

        MoveDown.BindDataContext(md => md.Enabled, Binding.Property((MyViewModel vm) => vm.Top).Child(b => b.Choices).Convert(oc => oc.Count > 0));
        MoveUp.BindDataContext(md => md.Enabled, Binding.Property((MyViewModel vm) => vm.Bottom).Child(b => b.Choices).Convert(oc => oc.Count > 0));

        MoveDown.Click += (s,e) => {
            var toMove = (Geometry)Model.Top.Choices.ElementAtOrDefault(Model.Top.SelectedIndex);
            if (toMove == Geometry.None) return;
            Model.Top.Choices.Remove(toMove);
            Model.Bottom.Choices.Add(toMove);

            this.UpdateBindings(BindingUpdateMode.Destination);
            this.UpdateBindings(BindingUpdateMode.Source);
        };

        MoveUp.Click += (s,e) => {
            var toMove = (Geometry)Model.Bottom.Choices.ElementAtOrDefault(Model.Bottom.SelectedIndex);
            if (toMove == Geometry.None) return;
            Model.Bottom.Choices.Remove(toMove);
            Model.Top.Choices.Add(toMove);

            this.UpdateBindings(BindingUpdateMode.Destination);
            this.UpdateBindings(BindingUpdateMode.Source);
        };
    }
}

var dialog = new DropDownDialog();
var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

## More Reading
- [Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)