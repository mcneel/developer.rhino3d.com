---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Create a specialized GetObject with a Custom Geometry Filter
keywords: ['create', 'specialized', 'getobject', 'with', 'custom', 'geometry', 'filter']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  private static double m_tolerance;
  public static Result CustomGeometryFilter(RhinoDoc doc)
  {
    m_tolerance = doc.ModelAbsoluteTolerance;
    
    // only use a custom geometry filter if no simpler filter does the job

    // only curves
    var gc = new GetObject();
    gc.SetCommandPrompt("select curve");
    gc.GeometryFilter = ObjectType.Curve;
    gc.DisablePreSelect();
    gc.SubObjectSelect = false;
    gc.Get();
    if (gc.CommandResult() != Result.Success)
      return gc.CommandResult();
    if (null == gc.Object(0).Curve())
      return Result.Failure;
    Rhino.RhinoApp.WriteLine("curve was selected");

    // only closed curves
    var gcc = new GetObject();
    gcc.SetCommandPrompt("select closed curve");
    gcc.GeometryFilter = ObjectType.Curve;
    gcc.GeometryAttributeFilter = GeometryAttributeFilter.ClosedCurve;
    gcc.DisablePreSelect();
    gcc.SubObjectSelect = false;
    gcc.Get();
    if (gcc.CommandResult() != Result.Success)
      return gcc.CommandResult();
    if (null == gcc.Object(0).Curve())
      return Result.Failure;
    Rhino.RhinoApp.WriteLine("closed curve was selected");

    // only circles with a radius of 10
    var gcc10 = new GetObject();
    gcc10.SetCommandPrompt("select circle with radius of 10");
    gc.GeometryFilter = ObjectType.Curve;
    gcc10.SetCustomGeometryFilter(CircleWithRadiusOf10GeometryFilter); // custom geometry filter
    gcc10.DisablePreSelect();
    gcc10.SubObjectSelect = false;
    gcc10.Get();
    if (gcc10.CommandResult() != Result.Success)
      return gcc10.CommandResult();
    if (null == gcc10.Object(0).Curve())
      return Result.Failure;
    RhinoApp.WriteLine("circle with radius of 10 was selected");

    return Result.Success;
  }

  private static bool CircleWithRadiusOf10GeometryFilter (Rhino.DocObjects.RhinoObject rhObject, GeometryBase geometry,
    ComponentIndex componentIndex)
  {
    bool is_circle_with_radius_of10 = false;
    Circle circle;
    if (geometry is Curve && (geometry as Curve).TryGetCircle(out circle))
      is_circle_with_radius_of10 = circle.Radius <= 10.0 + m_tolerance && circle.Radius >= 10.0 - m_tolerance;
    return is_circle_with_radius_of10;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared m_tolerance As Double
  Public Shared Function CustomGeometryFilter(ByVal doc As RhinoDoc) As Result
	m_tolerance = doc.ModelAbsoluteTolerance

	' only use a custom geometry filter if no simpler filter does the job

	' only curves
	Dim gc = New GetObject()
	gc.SetCommandPrompt("select curve")
	gc.GeometryFilter = ObjectType.Curve
	gc.DisablePreSelect()
	gc.SubObjectSelect = False
	gc.Get()
	If gc.CommandResult() <> Result.Success Then
	  Return gc.CommandResult()
	End If
	If Nothing Is gc.Object(0).Curve() Then
	  Return Result.Failure
	End If
	Rhino.RhinoApp.WriteLine("curve was selected")

	' only closed curves
	Dim gcc = New GetObject()
	gcc.SetCommandPrompt("select closed curve")
	gcc.GeometryFilter = ObjectType.Curve
	gcc.GeometryAttributeFilter = GeometryAttributeFilter.ClosedCurve
	gcc.DisablePreSelect()
	gcc.SubObjectSelect = False
	gcc.Get()
	If gcc.CommandResult() <> Result.Success Then
	  Return gcc.CommandResult()
	End If
	If Nothing Is gcc.Object(0).Curve() Then
	  Return Result.Failure
	End If
	Rhino.RhinoApp.WriteLine("closed curve was selected")

	' only circles with a radius of 10
	Dim gcc10 = New GetObject()
	gcc10.SetCommandPrompt("select circle with radius of 10")
	gc.GeometryFilter = ObjectType.Curve
	gcc10.SetCustomGeometryFilter(AddressOf CircleWithRadiusOf10GeometryFilter) ' custom geometry filter
	gcc10.DisablePreSelect()
	gcc10.SubObjectSelect = False
	gcc10.Get()
	If gcc10.CommandResult() <> Result.Success Then
	  Return gcc10.CommandResult()
	End If
	If Nothing Is gcc10.Object(0).Curve() Then
	  Return Result.Failure
	End If
	RhinoApp.WriteLine("circle with radius of 10 was selected")

	Return Result.Success
  End Function

  Private Shared Function CircleWithRadiusOf10GeometryFilter(ByVal rhObject As Rhino.DocObjects.RhinoObject, ByVal geometry As GeometryBase, ByVal componentIndex As ComponentIndex) As Boolean
	Dim is_circle_with_radius_of10 As Boolean = False
	Dim circle As Circle = Nothing
	If TypeOf geometry Is Curve AndAlso (TryCast(geometry, Curve)).TryGetCircle(circle) Then
	  is_circle_with_radius_of10 = circle.Radius <= 10.0 + m_tolerance AndAlso circle.Radius >= 10.0 - m_tolerance
	End If
	Return is_circle_with_radius_of10
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
import rhinoscriptsyntax as rs
from scriptcontext import *
import Rhino

def circleWithRadiusOf10GeometryFilter (rhObject, geometry, componentIndex):
  isCircleWithRadiusOf10 = False
  c = rs.coercecurve(geometry)
  if c:
    b, circle = c.TryGetCircle()
  if b:
    isCircleWithRadiusOf10 = circle.Radius <= 10.0 + Rhino.RhinoMath.ZeroTolerance and circle.Radius >= 10.0 - Rhino.RhinoMath.ZeroTolerance
  return isCircleWithRadiusOf10

def RunCommand():
  # only use a custom geometry filter if no simpler filter does the job

  # for curves - only a simple filter is needed
  if rs.GetObject("select curve", rs.filter.curve): #Rhino.DocObjects.ObjectType.Curve):
    print "curve vas selected"

  # for circles with a radius of 10 - a custom geometry filter is needed
  if rs.GetObject("select circle with radius of 10", rs.filter.curve, False, False, circleWithRadiusOf10GeometryFilter):
      print "circle with radius of 10 was selected"

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in .active}

