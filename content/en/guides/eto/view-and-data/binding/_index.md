+++
aliases = []
authors = [ "curtis", "callum" ]
categories = [ "Eto"]
description = "An introduction to Bindings in Eto"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model", "Binding" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "Binding"
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
  This section is not for Python, python cannot use View Models and bindings in the same way as C#.
{{< /call-out >}}

## Introduction
Bindings pair properties in view models with UI Elements in the Eto Layout.
Let's look at a very simple example.

{{< row >}}
{{< column >}}

// TODO : Add Python
``` cs
public class ViewModel()
{
  public string Name { get; set; }
}

var nameInput = new TextBox();
nameInput.BindDataContext(t => t.Text, (ViewModel vm) => vm.Name);

var viewModel = new ViewModel();
var myDialog = new Dialog<string>()
{
  Title = "What is your Name?",
  DataContext = viewModel,
  Content = nameInput
};

myDialog.Show();
RhinoApp.WriteLine(viewModel.Name);
```

{{< /column >}}

{{< column >}}

If we use the Script Editor to run this script, a dialog appears with a text box. We can then enter text and hit close. You should see your inputted text printed to the command line.

Let's examine what happened.
1. A ViewModel with a `Name` property was set as the data context of a Dialog
2. A TextBox's `Text` property was "bound" to the ViewModel's `Name` property.
3. When changing the `Text` property, the `Name` property is updated


{{< /column >}}
{{< /row >}}

## More Reading
[Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)