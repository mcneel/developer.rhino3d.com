+++
aliases = ["/en/5/samples/cpp/intersect-line-curves/", "/en/6/samples/cpp/intersect-line-curves/", "/en/7/samples/cpp/intersect-line-curves/", "/wip/samples/cpp/intersect-line-curves/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to intersect line curves."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Intersect Line Curves"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/intersectlines"
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
  go.SetCommandPrompt( L"Select lines" );
  go.SetGeometryFilter( ON::curve_object );
  go.GetObjects( 2, 2 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  if( go.ObjectCount() != 2 )
    return failure;

  const ON_LineCurve* crv0 = ON_LineCurve::Cast( go.Object(0).Geometry() );
  const ON_LineCurve* crv1 = ON_LineCurve::Cast( go.Object(1).Geometry() );
  if( 0 == crv0 | 0 == crv1 )
    return failure;  

  ON_Line line0 = crv0->m_line;
  ON_Line line1 = crv1->m_line;

  ON_3dVector v0 = line0.to - line0.from;
  v0.Unitize();

  ON_3dVector v1 = line1.to - line1.from;
  v1.Unitize();

  if( v0.IsParallelTo(v1) != 0 )
  {
    RhinoApp().Print( L"Selected lines are parallel.\n" );
    return nothing;
  }

  ON_Line ray0( line0.from, line0.from + v0 );
  ON_Line ray1( line1.from, line1.from + v1 );

  double s = 0, t = 0;
  if( !ON_Intersect(ray0, ray1, &s, &t) )
  {
    RhinoApp().Print( L"No intersection found.\n" );
    return nothing;
  }

  ON_3dPoint pt0 = line0.from + s * v0;
  ON_3dPoint pt1 = line1.from + t * v1;

  // pt0 and pt1 should be equal, so we will
  // only add pt0 to the document
  context.m_doc.AddPointObject( pt0 );
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
