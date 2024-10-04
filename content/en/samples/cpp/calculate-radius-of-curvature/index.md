+++
aliases = ["/en/5/samples/cpp/calculate-radius-of-curvature/", "/en/6/samples/cpp/calculate-radius-of-curvature/", "/en/7/samples/cpp/calculate-radius-of-curvature/", "/wip/samples/cpp/calculate-radius-of-curvature/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to compute the radius of curvature of a curve object at a selected location."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calculate Radius of Curvature"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/radiusofcurvature"
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
  go.SetCommandPrompt( L"Select curve for curvature measurement" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const ON_Curve* crv = go.Object(0).Curve();
  if( 0 == crv )
    return failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Select point on curve for curvature measurement" );
  gp.Constrain( *crv );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();

  double t = 0.0;
  if( !crv->GetClosestPoint(pt, &t) )
  {
    RhinoApp().Print( L"Failed to compute radius of curvature.\n" );
    return failure;
  }

  ON_3dVector tangent = crv->TangentAt( t );
  if( tangent.IsTiny() )
  {
    RhinoApp().Print( L"Failed to compute radius of curvature. Curve may have stacked control points.\n" );
    return failure;
  }

  ON_3dVector curvature = crv->CurvatureAt( t );
  const double k = curvature.Length();
  if( k < ON_SQRT_EPSILON )
  {
    RhinoApp().Print( L"Radius of curvature: infinite.\n" );
    return failure;
  }

  ON_3dVector radius_vector = curvature / (k * k);
  ON_Circle circle;
  if ( !circle.Create(pt, tangent, pt + 2.0 * radius_vector) )
  {
    RhinoApp().Print( L"Failed to compute radius of curvature.\n" );
    return failure;
  }

  context.m_doc.AddCurveObject( circle );
  context.m_doc.AddPointObject( pt );
  context.m_doc.Redraw();

  ON_wString wRadius;
  RhinoFormatNumber( circle.Radius(), wRadius );
  RhinoApp().Print( L"Radius of curvature: %s.\n", wRadius );

  return success;
}
```
