---
title: Project Points to Breps
description: Demonstrates how to project points to Brep objects.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/projectpointstobreps
order: 1
keywords: ['projecting', 'points', 'breps']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result ProjectPointsToBreps(RhinoDoc doc)
  {
    var gs = new GetObject();
    gs.SetCommandPrompt("select surface");
    gs.GeometryFilter = ObjectType.Surface | ObjectType.PolysrfFilter;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();
    var brep = gs.Object(0).Brep();
    if (brep == null)
      return Result.Failure;

    var points = Intersection.ProjectPointsToBreps(
                 new List<Brep> {brep}, // brep on which to project
                 new List<Point3d> {new Point3d(0, 0, 0), new Point3d(3,0,3), new Point3d(-2,0,-2)}, // some random points to project
                 new Vector3d(0, 1, 0), // project on Y axis
                 doc.ModelAbsoluteTolerance);

    if (points != null && points.Length > 0)
    {
      foreach (var point in points)
      {
        doc.Objects.AddPoint(point);
      }
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ProjectPointsToBreps(ByVal doc As RhinoDoc) As Result
	Dim gs = New GetObject()
	gs.SetCommandPrompt("select surface")
	gs.GeometryFilter = ObjectType.Surface Or ObjectType.PolysrfFilter
	gs.DisablePreSelect()
	gs.SubObjectSelect = False
	gs.Get()
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If
	Dim brep = gs.Object(0).Brep()
	If brep Is Nothing Then
	  Return Result.Failure
	End If

	Dim points = Intersection.ProjectPointsToBreps(New List(Of Brep) _
	    From {brep}, New List(Of Point3d)
	    From {New Point3d(0, 0, 0), New Point3d(3,0,3), New Point3d(-2,0,-2)}, New Vector3d(0, 1, 0), doc.ModelAbsoluteTolerance) ' project on Y axis -  some random points to project -  brep on which to project

	If points IsNot Nothing AndAlso points.Length > 0 Then
	  For Each point In points
		doc.Objects.AddPoint(point)
	  Next point
	End If
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from scriptcontext import *
from Rhino.Geometry import *

def RunCommand():
  srfid = rs.GetObject("select surface", rs.filter.surface | rs.filter.polysurface)
  if not srfid: return
  brep = rs.coercebrep(srfid)
  if not brep: return

  pts = Intersect.Intersection.ProjectPointsToBreps(
      [brep], # brep on which to project
      [Point3d(0, 0, 0), Point3d(3,0,3), Point3d(-2,0,-2)], # points to project
      Vector3d(0, 1, 0), # project on Y axis
      doc.ModelAbsoluteTolerance)

  if pts != None and pts.Length > 0:
    for pt in pts:
      doc.Objects.AddPoint(pt)

  doc.Views.Redraw()

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}
