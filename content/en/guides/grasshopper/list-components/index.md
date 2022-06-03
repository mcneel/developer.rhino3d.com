+++
authors = [ "david" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to operate on more than one item at a time."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "List Components"
type = "guides"
weight = 1
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

 
## Overview

So far the example components have all operated on individual data items.  This is known as One-In-One-Out.  But what if you want to operate on more than one item at a time; One-In-Many-Out, Many-In-One-Out or Many-In-Many-Out?  This requires that input or output parameters have a non-standard [Grasshopper.Kernel.GH_ParamAccess](/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm) flag.

## List Parameters

Input and Output parameters that are part of Grasshopper components have an access flag that affects how the component treats data stored in these parameters.  Take for example the Polyline component.  It creates a single polyline object from a *collection* of corner-points.  This is a Many-In-One-Out kind of logic.  The Divide component creates a whole bunch of division points from a single curve. This is an example of One-In-Many-Out.  The Cull components remove certain items from lists, this is an example of Many-In-Many-Out.

Most components treat their inputs and outputs as parameters that provide individual instances of data, rather than related collections of data.  This is indicated by all parameters having an [GH_ParamAccess.item](/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm) access flag.  You can however assign different access flags to parameters.  Preferably this flag should be assigned only once, namely in the [RegisterInputParams](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm) or [RegisterOutputParams](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm) method overrides.  It is legal to modify an access flag as long as a solution is not currently in progress, but it is not recommended.

In this guide, we'll be writing a component that removes (culls) the bottom-most N objects in a collection of geometric shapes.  As inputs we'll need a collection of geometry and an integer indicating how many objects the user wants to remove, and as output we'll provide the same collection of geometry, but with the bottom-most objects missing.  This is therefore a Many-In-Many-Out case.

The Component code (without the `RegisterInputParams`, `RegisterOutputParams` and `SolveInstance` methods) may look like this:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
public class Component_CullByElevation : GH_Component
{
  public Component_CullByElevation()
    : base("Cull Elevation", "CullZ", "Cull objects by relative elevation", "Sets", "Sequence")
  { }

  public override Kernel.GH_Exposure Exposure
  {
    get { return GH_Exposure.primary | GH_Exposure.obscure; }
  }
  public override System.Guid ComponentGuid
  {
    get { return new Guid("{A8FF9CBA-0837-4cd6-9198-0D17325D3F8F}"); }
  }

  //...additional component code will go here..
}

```

</div>

<div class="codetab-content" id="vb">

```vbnet
Public Class Component_CullByElevation
  Inherits GH_Component

  Public Sub New()
    MyBase.New("Cull Elevation", "CullZ", "Cull objects by relative elevation", "Sets", "Sequence")
  End Sub

  Protected Overrides ReadOnly Property Icon() As System.Drawing.Bitmap
    Get
      Return My.Resources.TheIconNameForThisComponent
    End Get
  End Property
  Public Overrides ReadOnly Property Exposure() As Kernel.GH_Exposure
    Get
      Return GH_Exposure.primary Or GH_Exposure.obscure
    End Get
  End Property
  Public Overrides ReadOnly Property ComponentGuid() As System.Guid
    Get
      Return New Guid("{A8FF9CBA-0837-4cd6-9198-0D17325D3F8F}")
    End Get
  End Property

  '...further example code will come here...

End Class
```

</div>
</div>

We'll need to register the parameters as well, and we'll use the overloaded methods to immediately assign the correct parameter access flags...

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
protected override void RegisterInputParams(Kernel.GH_Component.GH_InputParamManager pManager)
{
  pManager.AddGeometryParameter("Geometry", "G", "Geometry to cull", GH_ParamAccess.list);
  pManager.AddIntegerParameter("Count", "C", "Number of objects to cull", GH_ParamAccess.item, 1);
}
protected override void RegisterOutputParams(Kernel.GH_Component.GH_OutputParamManager pManager)
{
  pManager.AddGeometryParameter("Geometry", "G", "Culled geometry", GH_ParamAccess.list);
}

```

</div>

<div class="codetab-content1" id="vb1">

```vbnet
Protected Overrides Sub RegisterInputParams(ByVal pManager As Kernel.GH_Component.GH_InputParamManager)
  'list access is non-standard, so we need to specifically assign it.
  pManager.AddGeometryParameter("Geometry", "G", "Geometry to cull", GH_ParamAccess.list)
  pManager.AddIntegerParameter("Count", "C", "Number of objects to cull", GH_ParamAccess.item, 1)
End Sub
Protected Overrides Sub RegisterOutputParams(ByVal pManager As Kernel.GH_Component.GH_OutputParamManager)
  'Again, we need to specify list access as that is not default.
  pManager.AddGeometryParameter("Geometry", "G", "Culled geometry", GH_ParamAccess.list)
End Sub
```

</div>
</div>

Input parameters rigorously enforce their access.  You are only allowed to retrieve individual items from inputs that have the [GH_ParamAccess.item](/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm) flag set.  Lists can only be retrieved when the access is set to `GH_ParamAccess.list` and data trees can only be gotten from a `GH_ParamAccess.tree` parameter.  Failure to do so will result in an error message at runtime.  Output parameter are more flexible, but this is only because output access was added only in Grasshopper 0.9.0001 and strict enforcement would result in SDK breakage with previous versions.

## Solving Routine

The `SolveInstance` implementation is basically identical to previous examples, the only difference is the way the component interacts with the parameters...

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
protected override void SolveInstance(Kernel.IGH_DataAccess DA)
{
  //Declare a new List(Of T) to hold your data.
  //This list must exist and should probably be empty.
  List<IGH_GeometricGoo> geometry = new List<IGH_GeometricGoo>();
  Int32 count = 0;

  //Retrieve the whole list using Da.GetDataList().
  if ((!DA.GetDataList(0, geometry)))
    return;
  if ((!DA.GetData(1, count)))
    return;

  //Validate inputs.
  if ((count < 0))
  {
    AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Count must be a positive integer");
    return;
  }

  //The number of objects to cull is larger than or
  //equal to the total number of objects. I.e. cull them all.
  if ((geometry.Count <= count))
    return;

  //Iteratively remove the lowest object from the list.
  for (Int32 N = 1; N <= count; N++)
  {
    double lowestElevation = double.MaxValue;
    Int32 lowestIndex = -1;

    //Iterate over all remaining geometry and find the lowest one.
    for (Int32 i = 0; i <= geometry.Count - 1; i++)
    {
      if ((geometry[i] == null))
        continue;
      BoundingBox bbox = geometry[i].Boundingbox;
      if ((!bbox.IsValid))
        continue;

      double localElevation = bbox.Min.Z;
      if ((localElevation < lowestElevation))
      {
        lowestElevation = localElevation;
        lowestIndex = i;
      }
    }

    //Delete the lowest object.
    geometry.RemoveAt(lowestIndex);
  }

  //Assign the remaining geometry
  //(even if it is only a single item!)
  //using the DA.SetDataList() method.
  DA.SetDataList(0, geometry);
}

```

</div>

<div class="codetab-content2" id="vb2">

```vbnet
Protected Overrides Sub SolveInstance(ByVal DA As Kernel.IGH_DataAccess)
  'Declare a new List(Of T) to hold your data.
  'This list cannot be a null reference.
  Dim geometry As New List(Of IGH_GeometricGoo)
  Dim count As Int32 = 0

  'Retrieve the whole list using DA.GetDataList().
  If (Not DA.GetDataList(0, geometry)) Then Return
  If (Not DA.GetData(1, count)) Then Return

  'Validate inputs.
  If (count < 0) Then
    AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Count must be a positive integer")
    Return
  End If

  'The number of objects to cull is larger than or
  'equal to the total number of objects. I.e. cull them all.
  If (geometry.Count <= count) Then Return

  'Iteratively remove the lowest object from the list.
  For N As Int32 = 1 To count
    Dim lowestElevation As Double = Double.MaxValue
    Dim lowestIndex As Int32 = -1

    'Iterate over all remaining geometry and find the lowest one.
    For i As Int32 = 0 To geometry.Count - 1
      If (geometry(i) Is Nothing) Then Continue For
      Dim bbox As BoundingBox = geometry(i).Boundingbox
      If (Not bbox.IsValid) Then Continue For

      Dim localElevation As Double = bbox.Min.Z
      If (localElevation < lowestElevation) Then
        lowestElevation = localElevation
        lowestIndex = i
      End If
    Next

    'Delete the lowest object.
    If (lowestIndex >= 0) Then geometry.RemoveAt(lowestIndex)
  Next

  'Assign the remaining geometry using the DA.SetDataList() method.
  DA.SetDataList(0, geometry)
End Sub
```

</div>
</div>

## Related Topics

- [What is a Grasshopper Component?](/guides/grasshopper/what-is-a-grasshopper-component)
- [Your First Component](/guides/grasshopper/your-first-component-windows)
- [Simple Component](/guides/grasshopper/simple-component)
- [Simple Mathematics Component](/guides/grasshopper/simple-mathematics-component)
- [Simple Geometry Component](/guides/grasshopper/simple-geometry-component)
