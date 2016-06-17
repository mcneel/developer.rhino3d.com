---
title: Find Curve Parameter At Point
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/curveclosestpoint
order: 1
keywords: ['find', 'curve', 'parameter', 'point']
layout: code-sample-rhinocommon
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
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import rhinoscriptsyntax as rs

def RunCommand():
  rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)
  if(rc!= Rhino.Commands.Result.Success):
    return rc
  crv = objref.Curve()
  if( crv == None ):
    return Rhino.Commands.Result.Failure

  gp = Rhino.Input.Custom.GetPoint()
  gp.SetCommandPrompt("Pick a location on the curve")
  gp.Constrain(crv, False)
  gp.Get()
  if (gp.CommandResult() != Rhino.Commands.Result.Success):
    return gp.CommandResult();

  p = gp.Point()
  b, cp = crv.ClosestPoint(p)
  if (b):
    print "point: ({0},{1},{2}), parameter: {3}".format(p.X, p.Y, p.Z, cp)
    scriptcontext.doc.Objects.AddPoint(p)
    scriptcontext.doc.Views.Redraw()

  return Rhino.Commands.Result.Success

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
