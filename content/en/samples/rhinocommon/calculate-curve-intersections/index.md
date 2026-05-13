+++
aliases = ["/en/5/samples/rhinocommon/calculate-curve-intersections/", "/en/6/samples/rhinocommon/calculate-curve-intersections/", "/en/7/samples/rhinocommon/calculate-curve-intersections/", "/en/wip/samples/rhinocommon/calculate-curve-intersections/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to calculate the intersection points between two user-specified curves."
keywords = [ "calculate", "curve", "intersections" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Calculate Curve Intersections"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/intersectcurves"
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
  public static Rhino.Commands.Result IntersectCurves(Rhino.RhinoDoc doc)
  {
    // Select two curves to intersect
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select two curves");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GetMultiple(2, 2);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    // Validate input
    var curveA = go.Object(0).Curve();
    var curveB = go.Object(1).Curve();
    if (curveA == null || curveB == null)
      return Rhino.Commands.Result.Failure;

    // Calculate the intersection
    const double intersection_tolerance = 0.001;
    const double overlap_tolerance = 0.0;
    var events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance);

    // Process the results
    if (events != null)
    {
      for (int i = 0; i < events.Count; i++)
      {
        var ccx_event = events[i];
        doc.Objects.AddPoint(ccx_event.PointA);
        if (ccx_event.PointA.DistanceTo(ccx_event.PointB) > double.Epsilon)
        {
          doc.Objects.AddPoint(ccx_event.PointB);
          doc.Objects.AddLine(ccx_event.PointA, ccx_event.PointB);
        }
      }
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

def IntersectCurves():
    # Select two curves to intersect
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select two curves")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    go.GetMultiple(2, 2)
    if go.CommandResult()!=Rhino.Commands.Result.Success: return

    # Validate input
    curveA = go.Object(0).Curve()
    curveB = go.Object(1).Curve()
    if not curveA or not curveB: return

    # Calculate the intersection
    intersection_tolerance = 0.001
    overlap_tolerance = 0.0
    events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance)

    # Process the results
    if not events: return
    for ccx_event in events:
        scriptcontext.doc.Objects.AddPoint(ccx_event.PointA)
        if ccx_event.PointA.DistanceTo(ccx_event.PointB) > float.Epsilon:
            scriptcontext.doc.Objects.AddPoint(ccx_event.PointB)
            scriptcontext.doc.Objects.AddLine(ccx_event.PointA, ccx_event.PointB)
    scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    IntersectCurves()
```

</div>
