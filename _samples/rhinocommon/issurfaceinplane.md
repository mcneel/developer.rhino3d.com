---
layout: code-sample
title: Is Surface In Plane
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['surface', 'plane']
order: 103
description:  
---



```cs
public class IsPlanarSurfaceInPlaneCommand : Command
{
  public override string EnglishName { get { return "csIsPlanarSurfaceInPlane"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("select surface", true, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var surface = obj_ref.Surface();

    Point3d[] corners;
    rc = RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var is_or_isnt = "";
    if (IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance))
      is_or_isnt = " not ";

    RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt);
    return Result.Success;
  }

  private bool IsSurfaceInPlane(Surface surface, Plane plane, double tolerance)
  {
    if (!surface.IsPlanar(tolerance))
      return false;
   
    var bbox = surface.GetBoundingBox(true);
    return bbox.GetCorners().All(
      corner => System.Math.Abs(plane.DistanceTo(corner)) <= tolerance);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class IsPlanarSurfaceInPlaneCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbIsPlanarSurfaceInPlane"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim obj_ref As ObjRef = Nothing
    Dim rc = RhinoGet.GetOneObject("select surface", True, ObjectType.Surface, obj_ref)
    If rc <> Result.Success Then
      Return rc
    End If
    Dim surface = obj_ref.Surface()

    Dim corners As Point3d() = Nothing
    rc = RhinoGet.GetRectangle(corners)
    If rc <> Result.Success Then
      Return rc
    End If

    Dim plane = New Plane(corners(0), corners(1), corners(2))

    Dim is_or_isnt = If(IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance), "", " not ")
    RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt)
    Return Result.Success
  End Function

  Private Function IsSurfaceInPlane(surface As Surface, plane As Plane, tolerance As Double) As Boolean
    If Not surface.IsPlanar(tolerance) Then
      Return False
    End If

    Dim bbox = surface.GetBoundingBox(True)
    Return bbox.GetCorners().All(Function(corner) Math.Abs(plane.DistanceTo(corner)) <= tolerance)
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
from Rhino.Geometry import *
import rhinoscriptsyntax as rs
from scriptcontext import doc
import math

def RunCommand():
  surface_id = rs.GetSurfaceObject()[0]
  if surface_id == None:
    return
  surface = rs.coercesurface(surface_id)

  corners = rs.GetRectangle()
  if corners == None:
    return
    
  plane = Plane(corners[0], corners[1], corners[2])

  is_or_isnt = "" if IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance) else " not "
  print "Surface is{0} in plane.".format(is_or_isnt)

def IsSurfaceInPlane(surface, plane, tolerance):
  if not surface.IsPlanar(tolerance):
    return False
 
  bbox = surface.GetBoundingBox(True)
  rc = True
  for corner in bbox.GetCorners():
      if math.fabs(plane.DistanceTo(corner)) > tolerance:
          rc = False
          break
          
  return rc

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}


