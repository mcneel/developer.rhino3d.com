---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Brep from Curve Bounding Box
keywords: ['brep', 'curve', 'bounding']
categories: ['Curves']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result BrepFromCurveBBox(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = RhinoGet.GetOneObject("Select Curve", false, ObjectType.Curve, out objref);
    if( rc != Result.Success )
      return rc;
    var curve = objref.Curve();

    var view = doc.Views.ActiveView;
    var plane = view.ActiveViewport.ConstructionPlane();
    // Create a construction plane aligned bounding box
    var bbox = curve.GetBoundingBox(plane);

    if (bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0) {
      RhinoApp.WriteLine("the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created.");
      return Result.Failure;
    }
    var brep = Brep.CreateFromBox(bbox);
    doc.Objects.AddBrep(brep);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function BrepFromCurveBBox(ByVal doc As RhinoDoc) As Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve, objref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim curve = objref.Curve()

	Dim view = doc.Views.ActiveView
	Dim plane = view.ActiveViewport.ConstructionPlane()
	' Create a construction plane aligned bounding box
	Dim bbox = curve.GetBoundingBox(plane)

	If bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0 Then
	  RhinoApp.WriteLine("the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created.")
	  Return Result.Failure
	End If
	Dim brep = Brep.CreateFromBox(bbox)
	doc.Objects.AddBrep(brep)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
from Rhino.Geometry import *
from Rhino.Commands import Result
from Rhino.Input import RhinoGet
from Rhino.DocObjects import ObjectType
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
  rc, objRef = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)
  if rc <> Result.Success:
    return rc
  curve = objRef.Curve()
  if None == curve:
    return Result.Failure

  view = doc.Views.ActiveView
  plane = view.ActiveViewport.ConstructionPlane()
  # Create a construction plane aligned bounding box
  bbox = curve.GetBoundingBox(plane)

  if bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0:
    print "the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created."
    return Result.Failure

  brep = Brep.CreateFromBox(bbox)
  doc.Objects.AddBrep(brep)
  doc.Views.Redraw()

  return Result.Success

if __name__ == "__main__":
  print RunCommand()
```
{: #py .tab-pane .fade .in}

