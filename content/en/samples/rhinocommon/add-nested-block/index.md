+++
aliases = ["/5/samples/rhinocommon/add-nested-block/", "/6/samples/rhinocommon/add-nested-block/", "/7/samples/rhinocommon/add-nested-block/", "/wip/samples/rhinocommon/add-nested-block/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Blocks" ]
description = "Demonstrates how to add a nested block to an instance definition."
keywords = [ "add", "nested", "block" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Nested Block"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

