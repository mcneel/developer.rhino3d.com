---
title: Simple Geometry Component
description: This guide demonstrates how to use some of the simpler geometry types and classes in RhinoCommon & Grasshopper.
authors: ['David Rutten']
author_contacts: ['DavidRutten']
sdk: ['Grasshopper']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm
order: 3
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

 
We'll discuss how to deal with different access levels of input data and invalid Structs vs. invalid and null Classes.

## Overview

This component will perform a simple Circle-Line Split operation.  We'll retrieve a single Circle and a single Line input, make sure the data is valid, project the line onto the circle plane, determine whether or not the Split operation is valid and then output the two arcs on either side of the slicing line.

## Prerequisites

We will not be dealing with any of the basics of component development.  Please make sure you have read the [Your First Component]({{ site.baseurl }}/guides/grasshopper/your-first-component-windows), [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple-component), and [Simple Mathematics Component]({{ site.baseurl }}/guides/grasshopper/simple-mathematics-component) guides before starting this one.

Before you start, create a new class that derives from `Grasshopper.Kernel.GH_Component`, as outlined in the [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple-component) guide.

## Input Parameters

This part of the component is very similar to the [Simple Mathematics Component]({{ site.baseurl }}/guides/grasshopper/simple-mathematics-component), except this time there will be no default values.

<ul class="nav nav-pills">
  <li class="active"><a href="#cs" data-toggle="pill">C#</a></li>
  <li><a href="#vb" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
{
  pManager.AddCircleParameter("Circle", "C", "The circle to slice", GH_ParamAccess.item);
  pManager.AddLineParameter("Line", "L", "Slicing line", GH_ParamAccess.item);
}
...
```
{: #cs .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)
  pManager.AddCircleParameter("Circle", "C", "The circle to slice", GH_ParamAccess.item)
  pManager.AddLineParameter("Line", "L", "Slicing line", GH_ParamAccess.item)
End Sub
...
```
{: #vb .tab-pane .fade .in}

</div>

The first parameter is of type `Param_Circle` and the data it contains will consist solely of `GH_Circle`.  `GH_Circle` is a class that wraps the `Rhino.Geometry.Circle` structure.  It provides methods that allow Grasshopper to incorporate RhinoCommon circles into the default GUI.  These methods include Archiving, Previewing, Baking and Casting (Converting) functions.  However, when accessing data inside a `Param_Circle` parameter, you are not limited to the `GH_Circle` type, as we shall see.

The second parameter is of type `Param_Line` and it works very similar to the `Param_Circle` type discussed above.

## Output Parameters

Our component will output two arcs on success, or nulls on failure.

<ul class="nav nav-pills">
  <li class="active"><a href="#cs1" data-toggle="pill">C#</a></li>
  <li><a href="#vb1" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
{
  pManager.AddArcParameter("Arc A", "A", "First Split result.", GH_ParamAccess.item);
  pManager.AddArcParameter("Arc B", "B", "Second Split result.", GH_ParamAccess.item);
}
...
```
{: #cs1 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub RegisterOutputParams(ByVal pManager As GH_Component.GH_OutputParamManager)
  pManager.AddArcParameter("Arc A", "A", "First Split result.", GH_ParamAccess.item)
  pManager.AddArcParameter("Arc B", "B", "Second Split result.", GH_ParamAccess.item)
End Sub
...
```
{: #vb1 .tab-pane .fade .in}

</div>

## Solve Instance

The `SolveInstance()` implementation for this component is responsible for the following steps:

1. Declare placeholder variables for the input data.
1. Retrieve input data.
1. Test input data for validity.
1. Project line segment onto circle plane.
1. Test projected segment for validity.
1. Solve intersections for circle and projected segment.
1. Abort on insufficient intersections.
1. Create the slice arcs.
1. Assign arcs to the output parameters.

Steps 2 and 9 however can be approached from different directions.  First I'll show you the recommended approach and then we'll have a look at the alternatives:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs2" data-toggle="pill">C#</a></li>
  <li><a href="#vb2" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
protected override void SolveInstance(IGH_DataAccess DA)
{
  // 1. Declare placeholder variables and assign initial invalid data.
  //    This way, if the input parameters fail to supply valid data, we know when to abort.
  Rhino.Geometry.Circle circle = Rhino.Geometry.Circle.Unset;
  Rhino.Geometry.Line line = Rhino.Geometry.Line.Unset;

  // 2. Retrieve input data.
  if (!DA.GetData(0, ref circle)) { return; }
  if (!DA.GetData(1, ref line)) { return; }

  // 3. Abort on invalid inputs.
  if (!circle.IsValid) { return; }
  if (!line.IsValid) { return; }

  // 4. Project line segment onto circle plane.
  line.Transform(Rhino.Geometry.Transform.PlanarProjection(circle.Plane));

  // 5. Test projected segment for validity.
  if (line.Length < Rhino.RhinoMath.ZeroTolerance)
  {
    AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Line could not be projected onto the Circle plane");
    return;
  }

  // 6. Solve intersections and 7. Abort if there are less than two intersections.
  double t1;
  double t2;
  Rhino.Geometry.Point3d p1;
  Rhino.Geometry.Point3d p2;

  switch (Rhino.Geometry.Intersect.Intersection.LineCircle(line, circle, out t1, out p1, out t2, out p2))
  {
    case Rhino.Geometry.Intersect.LineCircleIntersection.None:
      AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "No intersections were found");
      return;

    case Rhino.Geometry.Intersect.LineCircleIntersection.Single:
      AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Only a single intersection was found");
      return;
  }

  // 8. Create slicing arcs.
  double ct;
  circle.ClosestParameter(p1, out ct);

  Rhino.Geometry.Vector3d tan = circle.TangentAt(ct);

  // 9. Assign output arcs.
  DA.SetData(0, new Rhino.Geometry.Arc(p1, tan, p2));
  DA.SetData(1, new Rhino.Geometry.Arc(p1, -tan, p2));
}
...
```
{: #cs2 .tab-pane .fade .in .active}

```vbnet
...
Protected Overrides Sub SolveInstance(ByVal DA As Grasshopper.Kernel.IGH_DataAccess)
  '1. Declare placeholder variables and assign initial invalid data.
  '   This way, if the input parameters fail to supply valid data, we know when to abort.
  Dim circle As Rhino.Geometry.Circle = Rhino.Geometry.Circle.Unset
  Dim line As Rhino.Geometry.Line = Rhino.Geometry.Line.Unset

  '2. Retrieve input data.
  If (Not DA.GetData(0, circle)) Then Return
  If (Not DA.GetData(1, line)) Then Return

  '3. Abort on invalid inputs.
  If (Not circle.IsValid) Then Return
  If (Not line.IsValid) Then Return

  '4. Project line segment onto circle plane.
  line.Transform(Rhino.Geometry.Transform.PlanarProjection(circle.Plane))

  '5. Test projected segment for validity.
  If (line.Length < Rhino.RhinoMath.ZeroTolerance) Then
    AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Line could not be projected onto the Circle plane")
    Return
  End If

  '6. Solve intersections and 7. Abort if there are less than two intersections.
  Dim t1 As Double
  Dim p1 As Rhino.Geometry.Point3d
  Dim t2 As Double
  Dim p2 As Rhino.Geometry.Point3d

  Select Case Rhino.Geometry.Intersect.Intersection.LineCircle(line, circle, t1, p1, t2, p2)
    Case Rhino.Geometry.Intersect.LineCircleIntersection.None
      AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "No intersections were found")
      Return
    Case Rhino.Geometry.Intersect.LineCircleIntersection.Single
      AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Only a single intersection was found")
      Return
  End Select

  '8. Create slicing arcs.
  Dim ct As Double
  circle.ClosestParameter(p1, ct)

  Dim tan As Rhino.Geometry.Vector3d = circle.TangentAt(ct)

  '9. Assign output arcs.
  DA.SetData(0, New Rhino.Geometry.Arc(p1, tan, p2))
  DA.SetData(1, New Rhino.Geometry.Arc(p1, -tan, p2))
End Sub
...
```
{: #vb2 .tab-pane .fade .in}

</div>

As I mentioned before, the first input parameter is of type `Param_Circle` and it contains data of type `GH_Circle`.  But when we're accessing the parameter via the `DA.GetData(0, circle)` method, we're using `Rhino.Geometry.Circle` instead of `GH_Circle`.  The `DA.GetData()` method is capable of converting data from the intrinsic parameter type into requested types, provided the conversion makes sense.  `GH_Circle` to `Rhino.Geometry.Circle` is a perfectly valid conversion, `GH_Circle` to `Rhino.Geometry.Transform` would not be.

The Grasshopper Component SDK has been designed on the premise that the bulk of all components that operate on data only care about the data itself, not how it is wrapped up inside the Grasshopper data structures.  The conversion routines that translate `GH_Circle` data into `Rhino.Geometry.Circle` data (and obviously also `GH_Number` into `System.Double`, and `GH_Colour` into `System.Drawing.Color` etc.), have been highly optimised and should be used in almost all circumstances.

If however you feel the need to get access to the `GH_Circle` data directly, you can retrieve that instance in the same fashion:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs3" data-toggle="pill">C#</a></li>
  <li><a href="#vb3" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
...
Grasshopper.Kernel.Data.GH_Circle circle = null;
if (!DA.GetData(0, circle)) { return; }
...
```
{: #cs3 .tab-pane .fade .in .active}

```vbnet
...
Dim circle As Grasshopper.Kernel.Data.GH_Circle = Nothing
If (Not DA.GetData(0, circle)) Then Return
...
```
{: #vb3 .tab-pane .fade .in}

</div>

Note that a single instance of `GH_Circle` may be shared among any number of parameters in Grasshopper, and thus changing one will change data everywhere.  If you request `Rhino.Geometry.Circle`, `System.Double` or `System.Drawing.Color` instead of `GH_Circle`, `GH_Number` or `GH_Colour` you won't have to worry about this pitfall since you will always be given an object that has been disassociated from the (potentially shared) wrapper type.

Similarly, you are allowed to store output data in different formats as well.  Instead of...

<ul class="nav nav-pills">
  <li class="active"><a href="#cs4" data-toggle="pill">C#</a></li>
  <li><a href="#vb4" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
DA.SetData(0, new Rhino.Geometry.Arc(p1, tan, p2));
```
{: #cs4 .tab-pane .fade .in .active}

```vbnet
DA.SetData(0, New Rhino.Geometry.Arc(p1, tan, p2))
```
{: #vb4 .tab-pane .fade .in}

</div>

...you could also provide an instance of `Grasshopper.Kernel.Types.GH_Arc`:

<ul class="nav nav-pills">
  <li class="active"><a href="#cs5" data-toggle="pill">C#</a></li>
  <li><a href="#vb5" data-toggle="pill">VB.NET</a></li>
</ul>

{::options parse_block_html="true" /}
<div class="tab-content">

```cs
Grasshopper.Kernel.Types.GH_Arc gh_arc = new Grasshopper.Kernel.Types.GH_Arc(new Rhino.Geometry.Arc(p1, tan, p2));
DA.SetData(0, gh_arc);
```
{: #cs5 .tab-pane .fade .in .active}

```vbnet
Dim gh_arc As New Grasshopper.Kernel.Types.GH_Arc(New Rhino.Geometry.Arc(p1, tan, p2))
DA.SetData(0, gh_arc)
```
{: #vb5 .tab-pane .fade .in}

</div>

---

## Related Topics

- [Your First Component]({{ site.baseurl }}/guides/grasshopper/your-first-component-windows)
- [Simple Component]({{ site.baseurl }}/guides/grasshopper/simple-component)
- [Simple Mathematics Component]({{ site.baseurl }}/guides/grasshopper/simple-mathematics-component)
