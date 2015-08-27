---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Create Spiral
keywords: ['create', 'spiral']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result CreateSpiral(Rhino.RhinoDoc doc)
  {
    var axisStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var axisDir = new Rhino.Geometry.Vector3d(1, 0, 0);
    var radiusPoint = new Rhino.Geometry.Point3d(0, 1, 0);

    Rhino.Geometry.NurbsCurve curve0 = GetSpirial0();
    if (null != curve0)
      doc.Objects.AddCurve(curve0);

    Rhino.Geometry.NurbsCurve curve1 = GetSpirial1();
    if (null != curve1)
      doc.Objects.AddCurve(curve1);

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }

  private static Rhino.Geometry.NurbsCurve GetSpirial0()
  {
    var axisStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var axisDir = new Rhino.Geometry.Vector3d(1, 0, 0);
    var radiusPoint = new Rhino.Geometry.Point3d(0, 1, 0);

    return Rhino.Geometry.NurbsCurve.CreateSpiral(axisStart, axisDir, radiusPoint, 1, 10, 1.0, 1.0);
  }

  private static Rhino.Geometry.NurbsCurve GetSpirial1()
  {
    var railStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var railEnd = new Rhino.Geometry.Point3d(0, 0, 10);
    var railCurve = new Rhino.Geometry.LineCurve(railStart, railEnd);

    double t0 = railCurve.Domain.Min;
    double t1 = railCurve.Domain.Max;

    var radiusPoint = new Rhino.Geometry.Point3d(1, 0, 0);

    return Rhino.Geometry.NurbsCurve.CreateSpiral(railCurve, t0, t1, radiusPoint, 1, 10, 1.0, 1.0, 12);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function CreateSpiral(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim axisStart = New Rhino.Geometry.Point3d(0, 0, 0)
	Dim axisDir = New Rhino.Geometry.Vector3d(1, 0, 0)
	Dim radiusPoint = New Rhino.Geometry.Point3d(0, 1, 0)

	Dim curve0 As Rhino.Geometry.NurbsCurve = GetSpirial0()
	If Nothing IsNot curve0 Then
	  doc.Objects.AddCurve(curve0)
	End If

	Dim curve1 As Rhino.Geometry.NurbsCurve = GetSpirial1()
	If Nothing IsNot curve1 Then
	  doc.Objects.AddCurve(curve1)
	End If

	doc.Views.Redraw()

	Return Rhino.Commands.Result.Success
  End Function

  Private Shared Function GetSpirial0() As Rhino.Geometry.NurbsCurve
	Dim axisStart = New Rhino.Geometry.Point3d(0, 0, 0)
	Dim axisDir = New Rhino.Geometry.Vector3d(1, 0, 0)
	Dim radiusPoint = New Rhino.Geometry.Point3d(0, 1, 0)

	Return Rhino.Geometry.NurbsCurve.CreateSpiral(axisStart, axisDir, radiusPoint, 1, 10, 1.0, 1.0)
  End Function

  Private Shared Function GetSpirial1() As Rhino.Geometry.NurbsCurve
	Dim railStart = New Rhino.Geometry.Point3d(0, 0, 0)
	Dim railEnd = New Rhino.Geometry.Point3d(0, 0, 10)
	Dim railCurve = New Rhino.Geometry.LineCurve(railStart, railEnd)

	Dim t0 As Double = railCurve.Domain.Min
	Dim t1 As Double = railCurve.Domain.Max

	Dim radiusPoint = New Rhino.Geometry.Point3d(1, 0, 0)

	Return Rhino.Geometry.NurbsCurve.CreateSpiral(railCurve, t0, t1, radiusPoint, 1, 10, 1.0, 1.0, 12)
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

