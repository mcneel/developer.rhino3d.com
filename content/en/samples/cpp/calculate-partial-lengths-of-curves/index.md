+++
aliases = ["/en/5/samples/cpp/calculate-partial-lengths-of-curves/", "/en/6/samples/cpp/calculate-partial-lengths-of-curves/", "/en/7/samples/cpp/calculate-partial-lengths-of-curves/", "/en/wip/samples/cpp/calculate-partial-lengths-of-curves/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to calculate the length of a curve from the start point to some point on the curve."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calculating Partial Lengths of Curves"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/curvelength"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const ON_Curve* crv = go.Object(0).Curve();
  if( 0 == crv )
    return CRhinoCommand::failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Point on surface" );
  gp.Constrain( *crv );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();

  double t = 0.0;
  if( crv->GetClosestPoint(pt, &t) )
  {
    ON_Interval domain = crv->Domain();
    ON_Interval sub_domain( domain.Min(), t );
    double length = 0.0;
    if( crv->GetLength(&length, 0.0, &sub_domain) )
      RhinoApp().Print( L"Distance from start of curve = %f.\n", length );
  }

  return CRhinoCommand::success;
}
```
