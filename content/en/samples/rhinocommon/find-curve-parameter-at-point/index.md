+++
aliases = ["/en/5/samples/rhinocommon/find-curve-parameter-at-point/", "/en/6/samples/rhinocommon/find-curve-parameter-at-point/", "/en/7/samples/rhinocommon/find-curve-parameter-at-point/", "/en/wip/samples/rhinocommon/find-curve-parameter-at-point/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to find the curve parameter given a specific point on the curve."
keywords = [ "find", "curve", "parameter", "point" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Find Curve Parameter At Point"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/curveclosestpoint"
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
  public static Result FindCurveParameterAtPoint(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = RhinoGet.GetOneObject("Select curve", true, ObjectType.Curve,out objref);
    if(rc!= Result.Success)
      return rc;
    var curve = objref.Curve();
    if( curve==null )
      return Result.Failure;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Pick a location on the curve");
    gp.Constrain(curve, false);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();

    var point = gp.Point();
    double closest_point_param;
    if (curve.ClosestPoint(point, out closest_point_param))
    {
      RhinoApp.WriteLine("point: ({0}), parameter: {1}", point, closest_point_param);
      doc.Objects.AddPoint(point);
      doc.Views.Redraw();
    }
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import rhinoscriptsyntax as rs

def RunCommand():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)
    if(rc!= Rhino.Commands.Result.Success):
        return rc
    crv = objref.Curve()
    if( crv == None ):
        return Rhino.Commands.Result.Failure

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Pick a location on the curve")
    gp.Constrain(crv, False)
    gp.Get()
    if (gp.CommandResult() != Rhino.Commands.Result.Success):
        return gp.CommandResult();

    p = gp.Point()
    b, cp = crv.ClosestPoint(p)
    if (b):
        print "point: ({0},{1},{2}), parameter: {3}".format(p.X, p.Y, p.Z, cp)
        scriptcontext.doc.Objects.AddPoint(p)
        scriptcontext.doc.Views.Redraw()

    return Rhino.Commands.Result.Success

if __name__=="__main__":
    RunCommand()
```

</div>
