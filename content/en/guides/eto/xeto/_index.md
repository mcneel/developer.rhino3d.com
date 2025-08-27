+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto" ]
description = "An introduction to xeto, XAML in Eto"
keywords = [ "Eto", "UI", "xeto" ]
languages = [ "C#", "py" ]
sdk = [ "Eto" ]
title = "Xeto"
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

[XEto Examples](https://github.com/search?q=repo%3Apicoe%2FEto%20path%3A*.xeto&type=code)

## What is Xeto?

Xeto is a way to describe Eto UIs layout using the XAML language.

## Cheat-sheet

### Properties

``` xml
<TabPage Text="Table Layout">
<TableLayout Padding="10" Spacing="5,5">
<Label>Text Area</Label>
```

### Bindings

#### Properties

This example binds to the property someText to the ViewModel but then uses a resource to convert the Binding
``` xml
<TextBox Text="{Binding SomeText, Converter={StaticResource myConverter}}" />
```

#### Events

Events are much simpler. Text="text".
``` xml
<TextBox TextChanged="HandleTextChanged" />
```
``` cs

```

#### Converters

``` xml
<Panel.Properties>
  <l:MyConverter x:Key="myConverter"/>
</Panel.Properties>
```

#### Buttons

``` xml
<Button Command="{Binding ClickMe}">Click Me!</Button>
```


### Parenting

#### Dynamic Layout


#### Table Layout

``` xml
<TableLayout Padding="10" Spacing="5,5">
  <TableRow>
    <Label Text="Text Box with converter" />
  </TableRow>
</TableLayout>

```

### Importing new controls

``` xml
xmlns:e="clr-namespace:Eto.Test.Sections.Controls;assembly=Eto.Test" 
```