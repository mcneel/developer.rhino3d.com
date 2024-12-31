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

## What is a View Model?
View Models contain the data and logic that accompnies our UI, separating view logic and model logic keeps our UIs more organised and promotes better coding.

## Why are View Models needed?
The simplest reason is to keep different things in different places.

#### Examples of View Model data and logic
``` cs
// Data
internal ObservableCollection<T> Users { get; }

// Methods
internal void LoadSettings();
internal void ResetSettings();
internal void ClearUsers();
```

#### Examples of View data and logic
``` cs
// Data
private bool IsButtonVisible { get; }
private static float BorderThickness { get; }
public Color BackgroundColour { get; }

// Methods
internal void RedrawView();
internal void CloseView();
```

## A Very Basic View Model
View Models do not need to be complex, they do not need to ...

``` cs
internal class ViewModel
{
  public int Count { get; set; } = 0;
}
```

## A Better View Model


``` cs
public class ViewModel : INotifyPropertyChanged
{
  public event PropertyChangedEventHandler PropertyChanged;

  protected virtual void RaisePropertyChanged(string propertyName)
  {
    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
  }
}
```

## Related topics

 - Notify Properties
 - 