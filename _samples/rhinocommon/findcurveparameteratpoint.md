---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Find Curve Parameter At Point
keywords: ['find', 'curve', 'parameter', 'point']
categories: ['Curves']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result FindCurveParameterAtPoint(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = RhinoGet.GetOneObject("Select curve", true, ObjectType.Curve,out objref);
    if(rc!= Result.Success)
      return rc;
    var curve = objref.Curve();
    if( curve==null )
      return Result.Failure;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Pick a location on the curve");
    gp.Constrain(curve, false);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();

    var point = gp.Point();
    double closest_point_param;
    if (curve.ClosestPoint(point, out closest_point_param))
    {
      RhinoApp.WriteLine("point: ({0}), parameter: {1}", point, closest_point_param);
      doc.Objects.AddPoint(point);
      doc.Views.Redraw();
    }
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function FindCurveParameterAtPoint(ByVal doc As RhinoDoc) As Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select curve", True, ObjectType.Curve,objref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim curve = objref.Curve()
	If curve Is Nothing Then
	  Return Result.Failure
	End If

	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Pick a location on the curve")
	gp.Constrain(curve, False)
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If

	Dim point = gp.Point()
	Dim closest_point_param As Double = Nothing
	If curve.ClosestPoint(point, closest_point_param) Then
	  RhinoApp.WriteLine("point: ({0}), parameter: {1}", point, closest_point_param)
	  doc.Objects.AddPoint(point)
	  doc.Views.Redraw()
	End If
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}

