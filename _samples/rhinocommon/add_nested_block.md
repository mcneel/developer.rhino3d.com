---
title: Add Nested Block
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects', 'Blocks']
origin: unset
order: 1
keywords: ['add', 'nested', 'block']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddNestedBlock(RhinoDoc doc)
  {
    var circle = new Circle(Point3d.Origin, 5);
    Curve[] curveList = { new ArcCurve(circle) };
    var circleIndex = doc.InstanceDefinitions.Add("Circle", "Circle with radius of 5", Point3d.Origin, curveList);
    var transform = Transform.Identity;
    var irefId = doc.InstanceDefinitions[circleIndex].Id;
    var iref = new InstanceReferenceGeometry(irefId, transform);
    circle.Radius = circle.Radius * 2.0;
    GeometryBase[] blockList = { iref, new ArcCurve(circle) };
    var circle2Index = doc.InstanceDefinitions.Add("TwoCircles", "Nested block test", Point3d.Origin, blockList);
    doc.Objects.AddInstanceObject(circle2Index, transform);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddNestedBlock(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	Dim circle = New Circle(Point3d.Origin, 5)
	Dim curveList() As Curve = { New ArcCurve(circle) }
	Dim circleIndex = doc.InstanceDefinitions.Add("Circle", "Circle with radius of 5", Point3d.Origin, curveList)
	Dim transform = Transform.Identity
	Dim irefId = doc.InstanceDefinitions(circleIndex).Id
	Dim iref = New InstanceReferenceGeometry(irefId, transform)
	circle.Radius = circle.Radius * 2.0
	Dim blockList() As GeometryBase = { iref, New ArcCurve(circle) }
	Dim circle2Index = doc.InstanceDefinitions.Add("TwoCircles", "Nested block test", Point3d.Origin, blockList)
	doc.Objects.AddInstanceObject(circle2Index, transform)
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

