+++
aliases = ["/en/5/samples/rhinocommon/isbrepbox-test/", "/en/6/samples/rhinocommon/isbrepbox-test/", "/en/7/samples/rhinocommon/isbrepbox-test/", "/en/wip/samples/rhinocommon/isbrepbox-test/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to determine whether a given Brep is a box."
keywords = [ "isbrepbox", "test" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "IsBrepBox Test"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/isbrepbox"
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
  private static bool IsBrepBox(Rhino.Geometry.Brep brep)
  {
    const double zero_tolerance = 1.0e-6; // or whatever
    bool rc = brep.IsSolid;
    if( rc )
      rc = brep.Faces.Count == 6;

    var N = new Rhino.Geometry.Vector3d[6];
    for (int i = 0; rc && i < 6; i++)
    {
      Rhino.Geometry.Plane plane;
      rc = brep.Faces[i].TryGetPlane(out plane, zero_tolerance);
      if( rc )
      {
        N[i] = plane.ZAxis;
        N[i].Unitize();
      }
    }

    for (int i = 0; rc && i < 6; i++)
    {
      int count = 0;
      for (int j = 0; rc && j < 6; j++)
      {
        double dot = Math.Abs(N[i] * N[j]);
        if (dot <= zero_tolerance)
          continue;
        if (Math.Abs(dot - 1.0) <= zero_tolerance)
          count++;
        else
          rc = false;
      }

      if (rc)
      {
        if (2 != count)
          rc = false;
      }
    }
    return rc;
  }

  public static Rhino.Commands.Result IsBrepBox(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef obj_ref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select Brep", true, Rhino.DocObjects.ObjectType.Brep, out obj_ref);
    if (rc == Rhino.Commands.Result.Success)
    {
      var brep = obj_ref.Brep();
      if (brep != null)
      {
        Rhino.RhinoApp.WriteLine(IsBrepBox(brep) ? "Yes it is a box" : "No it is not a box");
      }
    }
    return rc;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino

def IsBrepBox(brep):
    zero_tolerance = 1.0e-6 #or whatever
    rc = brep.IsSolid
    if rc: rc = brep.Faces.Count == 6

    N = []
    for i in range(6):
        if not rc: break
        rc, plane = brep.Faces[i].TryGetPlane(zero_tolerance)
        if rc:
            v = plane.ZAxis
            v.Unitize()
            N.append(v)

    for i in range(6):
        count = 0
        for j in range(6):
            if not rc: break
            dot = abs(N[i] * N[j])
            if dot<=zero_tolerance: continue
            if abs(dot-1.0)<=zero_tolerance:
                count += 1
            else:
                rc = False

    if rc:
        if 2!=count: rc = False
    return rc

if __name__=="__main__":
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select Brep", True, Rhino.DocObjects.ObjectType.Brep)
    if rc==Rhino.Commands.Result.Success:
        brep = objref.Brep()
        if brep:
            if IsBrepBox(brep): print("Yes it is a box")
            else: print("No it is not a box")
```

</div>
