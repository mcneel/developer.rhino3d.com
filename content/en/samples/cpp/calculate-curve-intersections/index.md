+++
aliases = ["/en/5/samples/cpp/calculate-curve-intersections/", "/en/6/samples/cpp/calculate-curve-intersections/", "/en/7/samples/cpp/calculate-curve-intersections/", "/wip/samples/cpp/calculate-curve-intersections/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to calculate the intersection of two curves and obtain their intersection points."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calculate Curve Intersections"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/intersectcurves"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
      const CRhinoCommandContext& context
      )
{
  // Select two curves to intersect
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select two curves" );
  go.SetGeometryFilter( ON::curve_object );
  go.GetObjects( 2, 2 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Validate input
  const ON_Curve* curveA = go.Object(0).Curve();
  const ON_Curve* curveB = go.Object(1).Curve();
  if( 0 == curveA | 0 == curveB )
    return CRhinoCommand::failure;

  // Calculate the intersection
  double intersection_tolerance = 0.001;
  double overlap_tolerance = 0.0;
  ON_SimpleArray<ON_X_EVENT> events;
  int count = curveA->IntersectCurve(
        curveB,
        events,
        intersection_tolerance,
        overlap_tolerance
        );

  // Process the results
  if( count > 0 )
  {
    int i;
    for( i = 0; i < events.Count(); i++ )
    {
      const ON_X_EVENT& e = events[i];
      context.m_doc.AddPointObject( e.m_A[0] );
      if( e.m_A[0].DistanceTo(e.m_B[0]) > ON_EPSILON )
      {
        context.m_doc.AddPointObject( e.m_B[0] );
        context.m_doc.AddCurveObject( ON_Line(e.m_A[0], e.m_B[0]) );
      }
    }
    context.m_doc.Redraw();
  }

  return CRhinoCommand::success;
}
```
