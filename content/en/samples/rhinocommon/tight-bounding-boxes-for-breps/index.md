+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to generate tight bounding boxes for Brep objects."
keywords = [ "tight", "bounding", "boxes", "breps" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Tight Bounding Boxes for Breps"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/tightboundingbox"
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
  public static Result TightBoundingBox(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject(
      "Select surface to split", true, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var surface = obj_ref.Surface();
    if (surface == null)
      return Result.Failure;

    obj_ref = null;
    rc = RhinoGet.GetOneObject(
      "Select cutting curve", true, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Failure;

    var brep_face = surface as BrepFace;
    if (brep_face == null)
      return Result.Failure;

    var split-brep = brep_face.Split(
      new List<Curve> {curve}, doc.ModelAbsoluteTolerance);
    if (split-brep == null)
    {
      RhinoApp.WriteLine("Unable to split surface.");
      return Result.Nothing;
    }

    var meshes = Mesh.CreateFromBrep(split-brep);

    foreach (var mesh in meshes)
    {
      var bbox = mesh.GetBoundingBox(true);
      switch (bbox.IsDegenerate(doc.ModelAbsoluteTolerance))
      {
        case 3:
        case 2:
          return Result.Failure;
        case 1:
          // rectangle
          // box with 8 corners flattened to rectangle with 4 corners
          var rectangle_corners = bbox.GetCorners().Distinct().ToList();
          // add 1st point as last to close the loop
          rectangle_corners.Add(rectangle_corners[0]);
          doc.Objects.AddPolyline(rectangle_corners);
          doc.Views.Redraw();
          break;
        case 0:
          // box
          var brep_box = new Box(bbox).ToBrep();
          doc.Objects.AddBrep(brep_box);
          doc.Views.Redraw();
          break;
      }
    }

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function TightBoundingBox(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select surface to split", True, ObjectType.Surface, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim surface = obj_ref.Surface()
	If surface Is Nothing Then
	  Return Result.Failure
	End If

	obj_ref = Nothing
	rc = RhinoGet.GetOneObject("Select cutting curve", True, ObjectType.Curve, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim curve = obj_ref.Curve()
	If curve Is Nothing Then
	  Return Result.Failure
	End If

	Dim brep_face = TryCast(surface, BrepFace)
	If brep_face Is Nothing Then
	  Return Result.Failure
	End If

	Dim split-brep = brep_face.Split(New List(Of Curve) From {curve}, doc.ModelAbsoluteTolerance)
	If split-brep Is Nothing Then
	  RhinoApp.WriteLine("Unable to split surface.")
	  Return Result.Nothing
	End If

	Dim meshes = Mesh.CreateFromBrep(split-brep)

	For Each mesh In meshes
	  Dim bbox = mesh.GetBoundingBox(True)
	  Select Case bbox.IsDegenerate(doc.ModelAbsoluteTolerance)
		Case 3, 2
		  Return Result.Failure
		Case 1
		  ' rectangle
		  ' box with 8 corners flattened to rectangle with 4 corners
		  Dim rectangle_corners = bbox.GetCorners().Distinct().ToList()
		  ' add 1st point as last to close the loop
		  rectangle_corners.Add(rectangle_corners(0))
		  doc.Objects.AddPolyline(rectangle_corners)
		  doc.Views.Redraw()
		Case 0
		  ' box
		  Dim brep_box = (New Box(bbox)).ToBrep()
		  doc.Objects.AddBrep(brep_box)
		  doc.Views.Redraw()
	  End Select
	Next mesh

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from scriptcontext import doc
import rhinoscriptsyntax as rs
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from System.Collections.Generic import *

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select surface to split", True, ObjectType.Surface)
    if rc != Result.Success:
        return rc
    brep_face = obj_ref.Surface()
    if brep_face == None:
        return Result.Failure

    rc, obj_ref = RhinoGet.GetOneObject("Select cutting curve", True, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve = obj_ref.Curve()
    if curve == None:
        return Result.Failure

    curves = List[Curve]([curve])
    split-brep = brep_face.Split(curves, doc.ModelAbsoluteTolerance)

    if split-brep == None:
        RhinoApp.WriteLine("Unable to split surface.")
        return Result.Nothing

    meshes = Mesh.CreateFromBrep(split-brep)
    print type(meshes)
    for mesh in meshes:
        bbox = mesh.GetBoundingBox(True)
        bbox_type = bbox.IsDegenerate(doc.ModelAbsoluteTolerance)
        if bbox_type == 1: # rectangle
            # box with 8 corners flattened to rectangle with 4 corners
            box_corners = bbox.GetCorners()
            rectangle_corners = []
            for corner_point in box_corners:
                if corner_point not in rectangle_corners:
                    rectangle_corners.append(corner_point)
            # add 1st point as last to close the loop
            rectangle_corners.append(rectangle_corners[0])
            doc.Objects.AddPolyline(rectangle_corners)
            doc.Views.Redraw()
        elif bbox_type == 0: # box
            brep_box = Box(bbox).ToBrep()
            doc.Objects.AddBrep(brep_box)
            doc.Views.Redraw()
        else: # bbox invalid, point, or line
            return Result.Failure

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
