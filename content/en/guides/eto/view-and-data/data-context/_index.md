+++
aliases = ["/wip/guides/eto/view-and-data/data-context/"]
authors = [ "curtis", "callum" ]
categories = [ "Getting Started" ] # What is this?
description = "An introduction to the Eto Data Context"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model" ]
languages = [ "C#" ]
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

## An Overview
All `Eto.Forms.Control` objects have the `DataContext` property.
DataContext lets us choose a data object for our object to bind to, this will likely be a ViewModel, or a data object class. But it could even be as simple as an integer.
If an object does not have bindngs, it will not need a DataContext object.

## The relationship between DataContext and DataStore
Some Controls have a `DataStore` property, a good example is the [GridView](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_GridView.htm).
The DataStore is _similar_ to the DataContext, but should be used differently.
The DataStore *should always* be an enumerable, such as a list, array, or better yet, an `ObservableCollection<T>`.

## Trickle Down
A very useful feature to be aware of is the trickle-down effect of DataContext.
Any Control, (including Forms and Dialogs) that has a DataContext will bequeath the DataContext to every child control meaning that this can be accessed anywhere in your UI Tree.
If a child control overrides its DataContext with a new DataContext then a new lineage of this DataContext is created.

``` cs
var dialog = new Dialog()
{
  DataContext = new MyMainViewModel(), // <-- Start of Main View Model
  Content = new TableLayout()
  {
    Rows = {
      new TableRow(
        new PixelLayout()
        {
          DataContext = new MyNewViewModel(), // <-- Start of New View Model
          Items = {
            new Drawable(),
            new Button() // <-- Button has a DataContext of MyNewViewModel
          }
        }
      ),
      new TableRow(
        new Button(),
        new Button(), // <-- Buttons all have a DataContext of MyMainViewModel
        new Button(), 
      ),
    }
  }
};
```

{{< call-out warning "Common DataContext Mistake" >}}
DataContext is often not an available property until the Form has been constructed.
Trying to access the DataContext from the constructor of a control or form will likley fail.
{{< /call-out >}}


## Related topics

- [Binding Data with a ViewModel](../binding/)
