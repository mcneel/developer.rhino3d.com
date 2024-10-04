+++
aliases = ["/en/5/samples/rhinocommon/pick-point/", "/en/6/samples/rhinocommon/pick-point/", "/en/7/samples/rhinocommon/pick-point/", "/wip/samples/rhinocommon/pick-point/"]
authors = [ "steve" ]
categories = [ "Picking and Selection", "Adding Objects" ]
description = "Demonstrates how to pick and select a point object."
keywords = [ "pick", "select", "point", "objects" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Pick Point"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/pickpoint"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  public static Result PickPoint(RhinoDoc doc)
  {
    // this creates a point where the mouse is clicked.
    var gp = new GetPoint();
    gp.SetCommandPrompt("Click for new point");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var point3d = gp.Point();
    doc.Objects.AddPoint(point3d);
    doc.Views.Redraw();

    // selects a point that already exists
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select point", false, ObjectType.Point, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var point = obj_ref.Point();
    RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
      point.Location.X,
      point.Location.Y,
      point.Location.Z);
    doc.Objects.UnselectAll();

    // selects multiple points that already exist
    ObjRef[] obj_refs;
    rc = RhinoGet.GetMultipleObjects("Select point", false, ObjectType.Point, out obj_refs);
    if (rc != Result.Success)
      return rc;
    foreach (var o_ref in obj_refs)
    {
      point = o_ref.Point();
      RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
        point.Location.X,
        point.Location.Y,
        point.Location.Z);
    }
    doc.Objects.UnselectAll();

    // also selects a point that already exists.
    // Used when RhinoGet doesn't provide enough control
    var go = new GetObject();
    go.SetCommandPrompt("Select point");
    go.GeometryFilter = ObjectType.Point;
    go.GetMultiple(1, 0);
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();
    foreach (var o_ref in  go.Objects())
    {
      point = o_ref.Point();
      if (point != null)
        RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
          point.Location.X,
          point.Location.Y,
          point.Location.Z);
    }

    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function PickPoint(ByVal doc As RhinoDoc) As Result
	' this creates a point where the mouse is clicked.
	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Click for new point")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim point3d = gp.Point()
	doc.Objects.AddPoint(point3d)
	doc.Views.Redraw()

	' selects a point that already exists
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select point", False, ObjectType.Point, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim point = obj_ref.Point()
	RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
	doc.Objects.UnselectAll()

	' selects multiple points that already exist
	Dim obj_refs() As ObjRef = Nothing
	rc = RhinoGet.GetMultipleObjects("Select point", False, ObjectType.Point, obj_refs)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	For Each o_ref In obj_refs
	  point = o_ref.Point()
	  RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
	Next o_ref
	doc.Objects.UnselectAll()

	' also selects a point that already exists.
	' Used when RhinoGet doesn't provide enough control
	Dim go = New GetObject()
	go.SetCommandPrompt("Select point")
	go.GeometryFilter = ObjectType.Point
	go.GetMultiple(1, 0)
	If go.CommandResult() <> Result.Success Then
	  Return go.CommandResult()
	End If
	For Each o_ref In go.Objects()
	  point = o_ref.Point()
	  If point IsNot Nothing Then
		RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
	  End If
	Next o_ref

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *
from scriptcontext import doc
import rhinoscriptsyntax as rs

def RunCommand():
    # creates a point where the mouse is clicked
    # using RhinoCommon
    gp = GetPoint()
    gp.SetCommandPrompt("Click for point")
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    point3d = gp.Point()
    doc.Objects.AddPoint(point3d)
    doc.Views.Redraw()

    # creates a point where the mouse is clicked
    # using the RhinoScript syntax
    point3d = rs.GetPoint("Click for point")
    if point3d == None: return Result.Nothing
    rs.AddPoint(point3d)
    doc.Objects.AddPoint(point3d)


    # selects a point that already exists
    # using RhinoCommon
    rc, obj_ref = RhinoGet.GetOneObject("Select point", False, ObjectType.Point)
    if rc != Result.Success:
        return rc
    point = obj_ref.Point()
    RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    doc.Objects.UnselectAll()

    # also selects a point that already exists
    # using RhinoCommon
    # Used when RhinoGet doesn't provide enough control
    go = GetObject()
    go.SetCommandPrompt("Select point")
    go.GeometryFilter = ObjectType.Point
    go.GetMultiple(1, 0)
    if go.CommandResult() != Result.Success:
        return go.CommandResult()
    for o_ref in  go.Objects():
        point = o_ref.Point()
        if point != None:
            RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    doc.Objects.UnselectAll()

    # selects a point that already exists
    # using RhinoScript syntax
    point_id = rs.GetObject("Select point", rs.filter.point)
    if point_id == None: return Result.Nothing
    print "point id: {0}".format(point_id)
    rs.UnselectAllObjects()

    # selects multiple points that already exist
    rc, obj_refs = RhinoGet.GetMultipleObjects("Select point", False, ObjectType.Point)
    if rc != Result.Success:
        return rc
    for o_ref in obj_refs:
        point = o_ref.Point()
        RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    doc.Objects.UnselectAll()

    # selects multiple poins that already exists
    # using the RhinoScript syntax
    point_ids = rs.GetObjects("Select point", rs.filter.point)
    for p_id in point_ids:
        print "point id: {0}".format(p_id)

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
