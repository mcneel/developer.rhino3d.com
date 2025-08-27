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

### Starting a file

It is critical that the top xmlns is the eto spec. If this is not the case, the controls will not create eto controls.
``` xml
<Panel
xmlns="http://schema.picoe.ca/eto.forms" 
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
/>
```

### Key-Words

#### x:Name
Eto has the Id property, but this unique id property also sets a property on the host control.
Of note `x:` is the Xaml namespace.

``` xml
<!-- MyForm.xeto -->
<CheckBox x:Name="MyCheckBox"/>
```

``` cs
// MyForm.cs
protected CheckBox MyCheckBox { get; set; }
```

### Properties

Properties can be set in a few ways.

``` xml
<TabPage Text="Table Layout">
<TableLayout Padding="10" Spacing="5,5">
<Label>Text Area</Label>

<Button FontWeight="Bold" Content="A button" />
<Button>
    <Button.FontWeight>Bold</Button.FontWeight>
    <Button.Content>A button</Button.Content>
</Button>
```

### Bindings

#### Properties

This example binds to the property someText to the ViewModel but then uses a resource to convert the Binding
``` xml
<!-- MyForm.xeto -->
<TextBox Text="{Binding SomeText, Converter={StaticResource myConverter}}" />
```

``` cs
// MyModel.cs
public string SomeText { get; set; }
```

``` cs
public class MyConverter : IValueConverter
{
  public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
  {
    return System.Convert.ToString(value) + " (converted)";
  }
  public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
  {
    return System.Convert.ToString(value) + " (converted back)";
  }
}
```

#### Events

Events are much simpler. Text="text".
``` xml
<TextBox TextChanged="HandleTextChanged" />
```
``` cs

```

#### Static Resource

Xaml allows for static resources inside of the Xaml and this is inherited of course into xeto.
``` xml
<Window.Resources>
  <sys:String x:Key="strHelloWorld">Hello, world!</sys:String>
</Window.Resources>
<TextBlock Text="{StaticResource strHelloWorld}" FontSize="56" />
```

Of note `x:` is the Xaml namespace, `sys:` is System.
``` xml
<Window.Resources>
  <sys:String x:Key="ComboBoxTitle">Items:</sys:String>

  <x:Array x:Key="ComboBoxItems" Type="sys:String">
    <sys:String>Item #1</sys:String>
    <sys:String>Item #2</sys:String>
    <sys:String>Item #3</sys:String>
  </x:Array>
</Window.Resources>
    
<Label Content="{StaticResource ComboBoxTitle}" />
<ComboBox ItemsSource="{StaticResource ComboBoxItems}" />
```

The below syntax lets you bind to Images in Embedded Resources
``` xml
<ImageView Image="{Resource Eto.Test.Images.TestImage.png}" />
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

``` cs
public Command ClickMe => new Command((sender, e) => MessageBox.Show("Clicked!"));
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

#### Stack Layout

Stack Layouts parent exactly as you'd expect, 
``` xml
<StackLayout>
  <Label>Button that executes command from model:</Label>
  <Button Command="{Binding ClickMe}">Click Me!</Button>
  <StackLayoutItem Expand="true" HorizontalAlignment="Stretch">
    <TextArea />
  </StackLayoutItem>
  <StackLayoutItem HorizontalAlignment="Right">
    <StackLayout Orientation="Horizontal">
      <Button Text="OK" />
      <Button Text="Cancel" />
    </StackLayout>
  </StackLayoutItem>
</StackLayout>
```

### Importing new controls

``` xml
xmlns:e="clr-namespace:Eto.Test.Sections.Controls;assembly=Eto.Test" 
```

### Extensions
[Syntax Examples](https://github.com/picoe/Eto/tree/3a4eba9cee170ed5ecafb421ece07314e5fb7460/src/Eto.Serialization.Xaml/Extensions)

XAML/xeto is Extensible and allows for certain parts of the syntax to be extended with new properties and tags.

### Access Keys
[More info](https://wpf-tutorial.com/control-concepts/access-keys/)

### Tab Inding
[More info](https://wpf-tutorial.com/control-concepts/tab-order/)

Defines the order which tab moves through controls.

``` xml
<TextBox TabIndex="4" />
```

The following syntax will cause a control to be part of the order, but it will be skipped.
``` xml
<TextBox TabIndex="5" IsReadOnly="True" IsTabStop="False" />
```
