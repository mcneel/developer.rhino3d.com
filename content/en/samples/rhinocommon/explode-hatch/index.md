+++
aliases = ["/en/5/samples/rhinocommon/explode-hatch/", "/en/6/samples/rhinocommon/explode-hatch/", "/en/7/samples/rhinocommon/explode-hatch/", "/en/wip/samples/rhinocommon/explode-hatch/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to explode a user-specified hatch object into its constituent parts (curves, points, etc.)"
keywords = [ "explode", "hatch" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Explode Hatch"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/explodehatch"
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
  public static Rhino.Commands.Result ExplodeHatch(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Hatch;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.Geometry.Hatch hatch = objref.Geometry() as Rhino.Geometry.Hatch;
    if (null == hatch)
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.GeometryBase[] hatch_geom = hatch.Explode();
    if (null != hatch_geom)
    {
      for (int i = 0; i < hatch_geom.Length; i++)
      {
        Rhino.Geometry.GeometryBase geom = hatch_geom[i];
        if (null != geom)
        {
          switch (geom.ObjectType)
          {
            case Rhino.DocObjects.ObjectType.Point:
              {
                Rhino.Geometry.Point point = geom as Rhino.Geometry.Point;
                if (null != point)
                  doc.Objects.AddPoint(point.Location);
              }
              break;
            case Rhino.DocObjects.ObjectType.Curve:
              {
                Rhino.Geometry.Curve curve = geom as Rhino.Geometry.Curve;
                if (null != curve)
                  doc.Objects.AddCurve(curve);
              }
              break;
            case Rhino.DocObjects.ObjectType.Brep:
              {
                Rhino.Geometry.Brep brep = geom as Rhino.Geometry.Brep;
                if (null != brep)
                  doc.Objects.AddBrep(brep);
              }
              break;
          }
        }
      }
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

def ExplodeHatch():
    filter = Rhino.DocObjects.ObjectType.Hatch
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", False, filter)
    if rc != Rhino.Commands.Result.Success: return

    hatch = objref.Geometry()
    if not hatch: return

    hatch_geom = hatch.Explode()
    if hatch_geom:
        for geom in hatch_geom:
            if geom.ObjectType == Rhino.DocObjects.ObjectType.Point:
                scriptcontext.doc.Objects.AddPoint(geom)
            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Curve:
                scriptcontext.doc.Objects.AddCurve(geom)
            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Brep:
                scriptcontext.doc.Objects.AddBrep(geom)
        scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    ExplodeHatch()
```

</div>
