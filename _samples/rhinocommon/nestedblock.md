---
layout: code-sample
title: Nested Block
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['nested', 'block']
order: 117
description:  
---



```cs
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
```
{: #cs .tab-pane .fade .in .active}


```vbnet
no vb code sample available
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}


