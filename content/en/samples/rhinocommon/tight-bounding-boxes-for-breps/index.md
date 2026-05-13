+++
aliases = ["/en/5/samples/rhinocommon/tight-bounding-boxes-for-breps/", "/en/6/samples/rhinocommon/tight-bounding-boxes-for-breps/", "/en/7/samples/rhinocommon/tight-bounding-boxes-for-breps/", "/en/wip/samples/rhinocommon/tight-bounding-boxes-for-breps/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to generate tight bounding boxes for Brep objects."
keywords = [ "tight", "bounding", "boxes", "breps" ]
languages = [ "C#", "Python" ]
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

<div class="codetab-content" id="py">

```python
from scriptcontext import doc
import rhinoscriptsyntax as rs
from Rhino import RhinoApp
from Rhino.Geometry import Curve, Mesh, Box
from Rhino.Input import RhinoGet
from Rhino.DocObjects import ObjectType
from Rhino.Commands import Result
from System.Collections.Generic import List

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
    split_brep = brep_face.Split(curves, doc.ModelAbsoluteTolerance)

    if split_brep == None:
        RhinoApp.WriteLine("Unable to split surface.")
        return Result.Nothing

    meshes = Mesh.CreateFromBrep(split_brep)
    print(type(meshes))
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
