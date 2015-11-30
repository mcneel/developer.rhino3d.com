---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Project Points to Mesh
keywords: ['project', 'points', 'mesh']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result ProjectPointsToMeshesEx(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("mesh", false, ObjectType.Mesh, out obj_ref);
    if (rc != Result.Success) return rc;
    var mesh = obj_ref.Mesh();

    ObjRef[] obj_ref_pts;
    rc = RhinoGet.GetMultipleObjects("points", false, ObjectType.Point, out obj_ref_pts);
    if (rc != Result.Success) return rc;
    var points = new List<Point3d>();
    foreach (var obj_ref_pt in obj_ref_pts)
    {
      var pt = obj_ref_pt.Point().Location;
      points.Add(pt);
    }

    int[] indices;
    var prj_points = Intersection.ProjectPointsToMeshesEx(new[] {mesh}, points, new Vector3d(0, 1, 0), 0, out indices);
    foreach (var prj_pt in prj_points) doc.Objects.AddPoint(prj_pt);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ProjectPointsToMeshesEx(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh, obj_ref)
	If rc IsNot Result.Success Then
		Return rc
	End If
	Dim mesh = obj_ref.Mesh()

	Dim obj_ref_pts() As ObjRef = Nothing
	rc = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point, obj_ref_pts)
	If rc IsNot Result.Success Then
		Return rc
	End If
	Dim points = New List(Of Point3d)()
	For Each obj_ref_pt In obj_ref_pts
	  Dim pt = obj_ref_pt.Point().Location
	  points.Add(pt)
	Next obj_ref_pt

	Dim indices() As Integer = Nothing
	Dim prj_points = Intersection.ProjectPointsToMeshesEx( {mesh}, points, New Vector3d(0, 1, 0), 0, indices)
	For Each prj_pt In prj_points
		doc.Objects.AddPoint(prj_pt)
	Next prj_pt
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from System.Collections.Generic import *
from Rhino import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Geometry.Intersect import *
from Rhino.Input import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh)
  if rc != Result.Success: return rc
  mesh = obj_ref.Mesh()

  rc, obj_ref_pts = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point)
  if rc != Result.Success: return rc
  points = []
  for obj_ref_pt in obj_ref_pts:
    pt = obj_ref_pt.Point().Location
    points.append(pt)

  prj_points, indices = Intersection.ProjectPointsToMeshesEx({mesh}, points, Vector3d(0, 1, 0), 0)
  for prj_pt in prj_points:
    doc.Objects.AddPoint(prj_pt)
  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

