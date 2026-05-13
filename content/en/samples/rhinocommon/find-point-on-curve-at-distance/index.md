+++
aliases = ["/en/5/samples/rhinocommon/find-point-on-curve-at-distance/", "/en/6/samples/rhinocommon/find-point-on-curve-at-distance/", "/en/7/samples/rhinocommon/find-point-on-curve-at-distance/", "/en/wip/samples/rhinocommon/find-point-on-curve-at-distance/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how find a point on a curve given a specified length from the start of the curve."
keywords = [ "find", "point", "curve", "distance" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Find point on curve at distance"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/arclengthpoint"
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
  public static Rhino.Commands.Result ArcLengthPoint(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve",
      true, Rhino.DocObjects.ObjectType.Curve,out objref);
    if(rc!= Rhino.Commands.Result.Success)
      return rc;
    Rhino.Geometry.Curve crv = objref.Curve();
    if( crv==null )
      return Rhino.Commands.Result.Failure;

    double crv_length = crv.GetLength();
    double length = 0;
    rc = Rhino.Input.RhinoGet.GetNumber("Length from start", true, ref length, 0, crv_length);
    if(rc!= Rhino.Commands.Result.Success)
      return rc;

    Rhino.Geometry.Point3d pt = crv.PointAtLength(length);
    if (pt.IsValid)
    {
      doc.Objects.AddPoint(pt);
      doc.Views.Redraw();
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def ArcLengthPoint():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)
    if rc!=Rhino.Commands.Result.Success: return rc
    crv = objref.Curve()
    if not crv: return Rhino.Commands.Result.Failure
    crv_length = crv.GetLength()
    length = 0
    rc, length = Rhino.Input.RhinoGet.GetNumber("Length from start", True, length, 0, crv_length)
    if rc!=Rhino.Commands.Result.Success: return rc
    pt = crv.PointAtLength(length)
    if pt.IsValid:
        scriptcontext.doc.Objects.AddPoint(pt)
        scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    ArcLengthPoint()
```

</div>
