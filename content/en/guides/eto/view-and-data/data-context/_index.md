+++
aliases = ["/wip/guides/eto/view-and-data/data-context/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "An introduction to the Eto Data Context"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model" ]
languages = [ "C#", "py" ]
sdk = [ "Eto" ]
title = "Data Context"
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

<!-- cs -- Tested on Win/Mac -->
<!-- cs -- TODO : DataStore examples and best practices -->

## An Overview
All `Eto.Forms.Control` objects have the [`DataContext`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_BindableWidget_DataContext.htm) property.
DataContext lets us choose a data object for our View to bind to, this will likely be a ViewModel, or a data object class. But it could even be as simple as an integer (although this would be unusual).
If a View does not have or need bindings, it will likely not need a DataContext object.
The DataContext should not be used for arbitrary data storage, use [Tag](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_Control_Tag.htm) for this.

## The relationship between DataContext and DataStore
Some Controls have a `DataStore` property, a good example is the [GridView](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_GridView.htm).
The DataStore is _similar_ to the DataContext, but should be used differently.
The DataStore will always be an enumerable, such as a list, array, or better yet, an [`ObservableCollection<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=net-7.0).

## Trickle Down
A very useful feature to be aware of is the trickle-down effect of DataContext.
Any Control, (including Forms and Dialogs) that has a DataContext will set the DataContext of every child control meaning that this can be accessed anywhere in your UI Tree.
If a child control overrides its DataContext with a new DataContext then a new lineage of this DataContext is created.


<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

```cs
using Eto.Forms;

using Rhino.UI;

class MyMainViewModel {}
class MyNewViewModel {}

var dialog = new Dialog()
{
  DataContext = new MyMainViewModel(), // <-- Start of Main View Model
  Content = new TableLayout()
  {
    Rows = {
      new TableRow( // <-- TableRow has a DataContext of MyMainViewModel
        new StackLayout() // <-- StackLayout has a DataContext of MyNewViewModel
        {
          DataContext = new MyNewViewModel(), // <-- Start of New View Model
          Items = {
            new Drawable(), // <-- Drawable has a DataContext of MyNewViewModel
            new Button()    // <-- Button has a DataContext of MyNewViewModel
          }
        }
      ),
      new TableRow(    // <-- TableRow has a DataContext of MyMainViewModel
        new Button(), 
        new Button(), // <-- Buttons all have a DataContext of MyMainViewModel
        new Button()
      ),
    }
  }
};

var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
dialog.ShowModal(parent);
```

</div>
<div class="codetab-content1" id="py1">

```py
import scriptcontext as sc
 
import Rhino
from Rhino.UI import RhinoEtoApp, EtoExtensions
import Eto.Forms as ef
import Eto.Drawing as ed
 
parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

class MyMainViewModel():
  pass

class MyNewViewModel():
  pass

stack_layout = ef.StackLayout()
stack_layout.DataContext = ef.MyNewViewModel()

# Drawable has a DataContext of MyNewViewModel
stack_layout.Items.Add(ef.StackLayoutItem(ef.Drawable()))

# Button has a DataContext of MyNewViewModel
stack_layout.Items.Add(ef.StackLayoutItem(ef.Button()))

table_layout = ef.TableLayout()
table_layout.Rows.Add(ef.TableRow(ef.TableCell(stack_layout)))

# Buttons and TableRow all have a DataContext of MyMainViewModel
table_layout.Rows.Add(ef.TableRow(ef.TableCell(ef.Button()), ef.TableCell(ef.Button()), ef.TableCell(ef.Button())))

dialog = ef.Dialog()
dialog.DataContext = ef.MyMainViewModel()
dialog.Content = table_layout

dialog.ShowModal(parent)
```
  </div>
</div>

## Related topics

- [Binding Data with a ViewModel](../binding/)
