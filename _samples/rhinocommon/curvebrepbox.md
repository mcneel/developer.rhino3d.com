---
layout: code-sample
title: Create a Box From a Curve's Bounding Box
author: 
categories: ['Curves'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['create', 'curves', 'bounding']
order: 48
description:  
---



```cs
public class BrepFromCurveBBoxCommand : Command
{
  public override string EnglishName { get { return "csBrepFromCurveBBox"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class BrepFromCurveBBoxCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbBrepFromCurveBBox"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim objref As DocObjects.ObjRef = Nothing
    Dim rc = RhinoGet.GetOneObject("Select Curve", False, DocObjects.ObjectType.Curve, objref)
    If rc <> Result.Success Then
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
    Dim brepbox = Brep.CreateFromBox(bbox)
    doc.Objects.AddBrep(brepbox)
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


