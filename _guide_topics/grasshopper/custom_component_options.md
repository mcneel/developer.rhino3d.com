---
title: Custom Component Options
description: This guide discusses how to add custom options to a component and have them included in *.gh/.ghx* (de)serialization.
author: david@mcneel.com
apis: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm
order: 4
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

It skips over some portions of Component design which have already been handled in previous guides, so do not read this guide before familiarizing yourself with the [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple_component) guide.

## Overview

The component we'll create in this article will sort a list of numbers and have the custom option to convert those numbers to absolute values prior to sorting.  However, rather than providing this option as a boolean input parameter, we'll allow people to set it via the Component context menu. We'll need to do four special things to achieve this, to wit:

- Declare a class level variable/property.
- Provide access to the variable from within the Component menu.
- Include the variable in (de)serialization.
- Record undo events when changing the value.

## Example Component

Before you start with this guide, create a new class that derives from [GH_Component]({{ site.baseurl }}/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm), as outlined in the [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple_component) guide.

This component will require one input parameter and one output parameter, both of type Number with list access:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
  protected override void RegisterInputParams(Kernel.GH_Component.GH_InputParamManager pManager)
  {
    pManager.AddNumberParameter("Values", "V", "Values to sort", GH_ParamAccess.list);
  }
  protected override void RegisterOutputParams(Kernel.GH_Component.GH_OutputParamManager pManager)
  {
    pManager.AddNumberParameter("Values", "V", "Sorted values", GH_ParamAccess.list);
  }
...
```
{: #cs .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)
  pManager.AddNumberParameter("Values", "V", "Values to sort", GH_ParamAccess.list)
End Sub
Protected Overrides Sub RegisterOutputParams(ByVal pManager As Kernel.GH_Component.GH_OutputParamManager)
  pManager.AddNumberParameter("Values", "V", "Sorted values", GH_ParamAccess.list)
End Sub
...
```
{: #vb .tab-pane .fade .in}

</div>

Assuming for now we'll have a local property called `Absolute()` which gets a single boolean, we can also already write the `SolveInstance()` method:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs1" data-toggle="pill">C#</a></li>
  <li><a href="#vb1" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
  protected override void SolveInstance(Kernel.IGH_DataAccess DA)
  {
    List<double> values = new List<double>();
    if ((!DA.GetDataList(0, values)))
      return;
    if ((values.Count == 0))
      return;

    // Don't worry about where the Absolute property comes from, we'll get to it soon.
    if ((Absolute))
    {
      for (Int32 i = 0; i < values.Count; i++)
      {
        values(i) = Math.Abs(values(i));
      }
    }

    values.Sort();
    DA.SetDataList(0, values);
  }
...
```
{: #cs1 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub SolveInstance(ByVal DA As Kernel.IGH_DataAccess)
  Dim values As New List(Of Double)
  If (Not DA.GetDataList(0, values)) Then Return
  If (values.Count = 0) Then Return

  'Don't worry about where the Absolute property comes from, we'll get to it soon.
  If (Absolute) Then
    For i As Int32 = 0 To values.Count - 1
      values(i) = Math.Abs(values(i))
    Next
  End If

  values.Sort()
  DA.SetDataList(0, values)
End Sub
...
```
{: #vb1 .tab-pane .fade .in}

## Class Level Variables

The "Absolute" option for this component applies to the entire object, but not to other instances of this component.  Since it needs to survive (i.e. retain its value) for as long as the component lives, it has to be declared as a class level variable:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs2" data-toggle="pill">C#</a></li>
  <li><a href="#vb2" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
private bool m_absolute = false;
public bool Absolute
{
  get { return m_absolute; }
  set
  {
    m_absolute = value;
    if ((m_absolute))
    {
      Message = "Absolute";
    }
    else
    {
      Message = "Standard";
    }
  }
}
...
```
{: #cs2 .tab-pane .fade .in .active}

```vbnet
...
Private m_absolute As Boolean = False
Public Property Absolute() As Boolean
  Get
    Return m_absolute
  End Get
  Set(ByVal value As Boolean)
    m_absolute = value
    If (m_absolute) Then
      Message = "Absolute"
    Else
      Message = "Standard"
    End If
  End Set
End Property
...
```
{: #vb2 .tab-pane .fade .in}

The `m_absolute` field is a private field (only accessible from within this component) and it is exposed publicly via the `Absolute()` method, which allows both getting and setting.  Furthermore, whenever the `m_absolute` field is set, the `Absolute()` method ensures that the correct message is assigned.  The [Message]({{ site.baseurl }}/api/grasshopper/html/P_Grasshopper_Kernel_GH_Component_Message.htm) field on `GH_Component` allows you to set a string which will be displayed underneath the component on the canvas.  This is to signal to users that there's an option they can change which is not directly accessible via the input parameters.  Note that the message is not set *until* the `Absolute()` property is accessed, so you should specifically place a call to `Absolute = False` (or `True`) in the constructor.

It is of course possible to add any number of custom fields to a component, but you can only attach a single message, if you have more than one field you want to make the user aware of, you'll need to get creative.

## (De)serialization of Custom Data

When you add options or states to your component which need to be "sticky," you'll also need to (de)serialize them correctly.  (De)serialization is used when saving and opening files, when copying and pasting objects and during undo/redo actions.  In this particular case, we only need to add a single boolean to the standard file archive.  Serialization in Grasshopper happens using the *GH_IO.dll* methods and types, not via standard framework mechanisms such as the `SerializableAttribute`.

Override the [Write]({{ site.baseurl }}/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Write.htm) and [Read]({{ site.baseurl }}/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Read.htm) methods on `GH_Component` and be sure to always call the base implementation.

<ul class="nav nav-pills">
  <li class="active"><a href="#cs3" data-toggle="pill">C#</a></li>
  <li><a href="#vb3" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
public override bool Write(GH_IO.Serialization.GH_IWriter writer)
{
  // First add our own field.
  writer.SetBoolean("Absolute", Absolute);
  // Then call the base class implementation.
  return base.Write(writer);
}
public override bool Read(GH_IO.Serialization.GH_IReader reader)
{
  // First read our own field.
  Absolute = reader.GetBoolean("Absolute");
  // Then call the base class implementation.
  return base.Read(reader);
}
...
```
{: #cs3 .tab-pane .fade .in .active}

```vbnet
...
Public Overrides Function Write(ByVal writer As GH_IO.Serialization.GH_IWriter) As Boolean
  'First add our own field.
  writer.SetBoolean("Absolute", Absolute)
  'Then call the base class implementation.
  Return MyBase.Write(writer)
End Function
Public Overrides Function Read(ByVal reader As GH_IO.Serialization.GH_IReader) As Boolean
  'First read our own field.
  Absolute = reader.GetBoolean("Absolute")
  'Then call the base class implementation.
  Return MyBase.Read(reader)
End Function
...
```
{: #vb3 .tab-pane .fade .in}

## Context Menu Changes

We'll also need to add an additional menu item to the component context menu, then handle the click event for that item.  Adding items to a context menu is best done via the [AppendAdditionalComponentMenuItems]({{ site.baseurl }}/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm) method.  It allows you to insert any number of item in between the Bake and the Help items.  The easiest way to add menu items is to use the Shared methods on [GH_DocumentObject]({{ site.baseurl }}/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentObject.htm) such as [Menu_AppendItem]({{ site.baseurl }}/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm) or one of the overloads.  In this case we also want to assign a tooltip text to the item which cannot be done from inside `Menu_AppendItem()`.

<ul class="nav nav-pills">
  <li class="active"><a href="#cs4" data-toggle="pill">C#</a></li>
  <li><a href="#vb4" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void AppendAdditionalComponentMenuItems(System.Windows.Forms.ToolStripDropDown menu)
{
  // Append the item to the menu, making sure it's always enabled and checked if Absolute is True.
  ToolStripMenuItem item = Menu_AppendItem(menu, "Absolute", Menu_AbsoluteClicked, true, Absolute);
  // Specifically assign a tooltip text to the menu item.
  item.ToolTipText = "When checked, values are made absolute prior to sorting.";
}
...
```
{: #cs4 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub AppendAdditionalComponentMenuItems(ByVal menu As System.Windows.Forms.ToolStripDropDown)
  'Append the item to the menu, making sure it's always enabled and checked if Absolute is True.
  Dim item As ToolStripMenuItem = Menu_AppendItem(menu, "Absolute", AddressOf Menu_AbsoluteClicked, True, Absolute)
  'Specifically assign a tooltip text to the menu item.
  item.ToolTipText = "When checked, values are made absolute prior to sorting."
End Sub
...
```
{: #vb4 .tab-pane .fade .in}

When this menu item is clicked, the delegate assigned inside the `Menu_AppendItem()` method will be invoked.  It is here that we must handle a click event.  There are usually three steps involved in handling clicks; Record the current state as an undo event, change the state, trigger a new solution:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs5" data-toggle="pill">C#</a></li>
  <li><a href="#vb5" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
private void Menu_AbsoluteClicked(object sender, EventArgs e)
{
  RecordUndoEvent("Absolute");
  Absolute = !Absolute;
  ExpireSolution(true);
}
...
```
{: #cs5 .tab-pane .fade .in .active}

```vbnet
...
Private Sub Menu_AbsoluteClicked(ByVal sender As Object, ByVal e As EventArgs)
  RecordUndoEvent("Absolute")
  Absolute = Not Absolute
  ExpireSolution(True)
End Sub
...
```
{: #vb5 .tab-pane .fade .in}

Since our `Write()` and `Read()` methods handle the (de)serialization of the `Absolute` field, we can use the default [RecordUndoEvent]({{ site.baseurl }}/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) method. It is possible to define your own undo records, but that is a topic for another guide.

---

## Related Topics

- [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple_component)
