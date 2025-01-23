+++
aliases = []
authors = [ "curtis", "callum" ]
categories = [ "Eto" ]
description = "An introduction to View Models"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model" ]
languages = [ "C#", "py" ]
sdk = [ "Eto" ]
title = "View Models"
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

<!-- cs -- WIP -->

## What is a View Model?
View Models contain the data and logic that accompnies our UI, separating view logic and model logic keeps our UIs more organised and promotes better coding.

## Why are View Models needed?
The simplest reason is to keep different things in different places.

#### Examples of View Model data and logic
Notice how none of the properties or methods relate to the UI and focus entirely on Data and back end.

``` cs
// Data
internal ObservableCollection<User> Users { get; }

// Methods
internal void LoadSettings();
internal void ResetSettings();
internal void AddUser(User user);
```

#### Examples of view data and logic
Notice that the properties and methods are very much view specific only relating to the UI.

``` cs
// Data
private bool IsButtonVisible { get; }
private static float BorderThickness { get; }
public Color BackgroundColour { get; }

// Methods
internal void RedrawView();
internal void CloseView();
```

<!--
# View Model structure

## A very basic View Mdoel
A very basic View Model with a single property.

``` cs
internal class MyViewModel
{
  public int Count { get; set; } = 0;
}
```

## A better basic View Model


``` cs
public class MyViewModel : INotifyPropertyChanged
{

  private int _count { get; set; }
  public int Count
  {
    get => _count;
    set
    {
      _count = value;
      RaisePropertyChanged(nameof(Count));
    }
  }

  public event PropertyChangedEventHandler PropertyChanged;

  protected virtual void RaisePropertyChanged(string propertyName)
  {
    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
  }
}
```

## A much better and simpler View Model
Rhino.UI has a ViewModel that can be used to save repeating yourself

``` cs
public class MyViewModel : Rhino.UI.ViewModel
{

  private int _count { get; set; }
  public int Count
  {
    get => _count;
    set
    {
      _count = value;
      RaisePropertyChanged(nameof(Count));
    }
  }
}
```
-->

## More Reading
- [Binding Data](../binding)
- [Complex Bindings](../complex-bindings)
- [Bindings Deep Dive ](../bindings-explained)