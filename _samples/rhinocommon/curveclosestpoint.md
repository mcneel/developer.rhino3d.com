---
layout: code-sample
title: Find the Parameter of a Curve at a Point
author: 
categories: ['Curves'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['find', 'parameter', 'curve', 'point']
order: 49
description:  
---



```cs
public class CurveClosestPointCommand : Command
{
  public override string EnglishName { get { return "csFindCurveParameterAtPoint"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class CurveClosestPointCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbFindCurveParameterAtPoint"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim objref As Rhino.DocObjects.ObjRef = Nothing
    Dim rc = RhinoGet.GetOneObject("Select curve", True, ObjectType.Curve, objref)
    If rc <> Result.Success Then
      Return rc
    End If
    Dim curve = objref.Curve()
    If curve Is Nothing Then
      Return Result.Failure
    End If

    Dim gp = New GetPoint()
    gp.SetCommandPrompt("Pick a location on the curve")
    gp.Constrain(curve, False)
    gp.[Get]()
    If gp.CommandResult() <> Result.Success Then
      Return gp.CommandResult()
    End If

    Dim point = gp.Point()
    Dim closestPointParam As Double
    If curve.ClosestPoint(point, closestPointParam) Then
      RhinoApp.WriteLine("point: {0}, parameter: {1}", point, closestPointParam)
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


