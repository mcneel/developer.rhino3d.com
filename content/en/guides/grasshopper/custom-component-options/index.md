+++
aliases = ["/en/5/guides/grasshopper/custom-component-options/", "/en/6/guides/grasshopper/custom-component-options/", "/en/7/guides/grasshopper/custom-component-options/", "/wip/guides/grasshopper/custom-component-options/"]
authors = [ "david" ]
categories = [ "Advanced" ]
description = "This guide discusses how to add custom options to a component and have them included in *.gh/.ghx* (de)serialization."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Custom Component Options"
type = "guides"
weight = 4
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
It skips over some portions of Component design which have already been handled in previous guides, so do not read this guide before familiarizing yourself with the [Simple Component](/guides/grasshopper/simple-component) guide.

## Overview

The component we'll create in this article will sort a list of numbers and have the custom option to convert those numbers to absolute values prior to sorting.  However, rather than providing this option as a boolean input parameter, we'll allow people to set it via the Component context menu. We'll need to do four special things to achieve this, to wit:

- Declare a class level variable/property.
- Provide access to the variable from within the Component menu.
- Include the variable in (de)serialization.
- Record undo events when changing the value.

## Example Component

Before you start with this guide, create a new class that derives from [GH_Component](/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm), as outlined in the [Simple Component](/guides/grasshopper/simple-component) guide.

This component will require one input parameter and one output parameter, both of type Number with list access:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

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

</div>

<div class="codetab-content" id="vb">

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

</div>
</div>

Assuming for now we'll have a local property called `Absolute()` which gets a single boolean, we can also already write the `SolveInstance()` method:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

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

</div>

<div class="codetab-content1" id="vb1">

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

</div>
</div>

## Class Level Variables

The "Absolute" option for this component applies to the entire object, but not to other instances of this component.  Since it needs to survive (i.e. retain its value) for as long as the component lives, it has to be declared as a class level variable:

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

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

</div>

<div class="codetab-content2" id="vb2">

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

</div>
</div>

The `m_absolute` field is a private field (only accessible from within this component) and it is exposed publicly via the `Absolute()` method, which allows both getting and setting.  Furthermore, whenever the `m_absolute` field is set, the `Absolute()` method ensures that the correct message is assigned.  The [Message](/api/grasshopper/html/P_Grasshopper_Kernel_GH_Component_Message.htm) field on `GH_Component` allows you to set a string which will be displayed underneath the component on the canvas.  This is to signal to users that there's an option they can change which is not directly accessible via the input parameters.  Note that the message is not set *until* the `Absolute()` property is accessed, so you should specifically place a call to `Absolute = False` (or `True`) in the constructor.

It is of course possible to add any number of custom fields to a component, but you can only attach a single message, if you have more than one field you want to make the user aware of, you'll need to get creative.

## (De)serialization of Custom Data

When you add options or states to your component which need to be "sticky," you'll also need to (de)serialize them correctly.  (De)serialization is used when saving and opening files, when copying and pasting objects and during undo/redo actions.  In this particular case, we only need to add a single boolean to the standard file archive.  Serialization in Grasshopper happens using the *GH_IO.dll* methods and types, not via standard framework mechanisms such as the `SerializableAttribute`.

Override the [Write](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Write.htm) and [Read](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Read.htm) methods on `GH_Component` and be sure to always call the base implementation.

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

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

</div>

<div class="codetab-content3" id="vb3">

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

</div>
</div>

## Context Menu Changes

We'll also need to add an additional menu item to the component context menu, then handle the click event for that item.  Adding items to a context menu is best done via the [AppendAdditionalComponentMenuItems](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm) method.  It allows you to insert any number of item in between the Bake and the Help items.  The easiest way to add menu items is to use the Shared methods on [GH_DocumentObject](/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentObject.htm) such as [Menu_AppendItem](/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm) or one of the overloads.  In this case we also want to assign a tooltip text to the item which cannot be done from inside `Menu_AppendItem()`.

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'vb4')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

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

</div>

<div class="codetab-content4" id="vb4">

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

</div>
</div>

When this menu item is clicked, the delegate assigned inside the `Menu_AppendItem()` method will be invoked.  It is here that we must handle a click event.  There are usually three steps involved in handling clicks; Record the current state as an undo event, change the state, trigger a new solution:

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'vb5')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

```cs
private void Menu_AbsoluteClicked(object sender, EventArgs e)
{
  RecordUndoEvent("Absolute");
  Absolute = !Absolute;
  ExpireSolution(true);
}
...

```

</div>

<div class="codetab-content5" id="vb5">

```vbnet
...
Private Sub Menu_AbsoluteClicked(ByVal sender As Object, ByVal e As EventArgs)
  RecordUndoEvent("Absolute")
  Absolute = Not Absolute
  ExpireSolution(True)
End Sub
...
```

</div>
</div>

Since our `Write()` and `Read()` methods handle the (de)serialization of the `Absolute` field, we can use the default [RecordUndoEvent](/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) method. It is possible to define your own undo records, but that is a topic for another guide.

## Related Topics

- [Simple Component](/guides/grasshopper/simple-component)
