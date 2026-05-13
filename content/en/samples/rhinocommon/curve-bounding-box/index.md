+++
aliases = ["/en/5/samples/rhinocommon/curve-bounding-box/", "/en/6/samples/rhinocommon/curve-bounding-box/", "/en/7/samples/rhinocommon/curve-bounding-box/", "/en/wip/samples/rhinocommon/curve-bounding-box/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to create a curve bounding box (world and plane oriented)."
keywords = [ "curve", "bounding", "world", "plane", "oriented" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Curve Bounding Box"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/curveboundingbox"
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
  public static Rhino.Commands.Result CurveBoundingBox(Rhino.RhinoDoc doc)
  {
    // Select a curve object
    Rhino.DocObjects.ObjRef rhObject;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", false, Rhino.DocObjects.ObjectType.Curve, out rhObject);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    // Validate selection
    var curve = rhObject.Curve();
    if (curve == null)
      return Rhino.Commands.Result.Failure;

    // Get the active view's construction plane
    var view = doc.Views.ActiveView;
    if (view == null)
      return Rhino.Commands.Result.Failure;
    var plane = view.ActiveViewport.ConstructionPlane();

    // Compute the tight bounding box of the curve in world coordinates
    var bbox = curve.GetBoundingBox(true);
    if (!bbox.IsValid)
      return Rhino.Commands.Result.Failure;

    // Print the min and max box coordinates in world coordinates
    Rhino.RhinoApp.WriteLine("World min: {0}", bbox.Min);
    Rhino.RhinoApp.WriteLine("World max: {0}", bbox.Max);

    // Compute the tight bounding box of the curve based on the
    // active view's construction plane
    bbox = curve.GetBoundingBox(plane);

    // Print the min and max box coordinates in cplane coordinates
    Rhino.RhinoApp.WriteLine("CPlane min: {0}", bbox.Min);
    Rhino.RhinoApp.WriteLine("CPlane max: {0}", bbox.Max);
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def CurveBoundingBox():
    # Select a curve object
    rc, rhobject = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve)
    if rc!=Rhino.Commands.Result.Success: return

    # Validate selection
    curve = rhobject.Curve()
    if not curve: return

    ## Get the active view's construction plane
    view = scriptcontext.doc.Views.ActiveView
    if not view: return
    plane = view.ActiveViewport.ConstructionPlane()

    # Compute the tight bounding box of the curve in world coordinates
    bbox = curve.GetBoundingBox(True)
    if not bbox.IsValid: return

    # Print the min and max box coordinates in world coordinates
    print "World min:", bbox.Min
    print "World max:", bbox.Max

    # Compute the tight bounding box of the curve based on the
    # active view's construction plane
    bbox = curve.GetBoundingBox(plane)

    # Print the min and max box coordinates in cplane coordinates
    print "CPlane min:", bbox.Min
    print "CPlane max:", bbox.Max

if __name__=="__main__":
    CurveBoundingBox()
```

</div>
