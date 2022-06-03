+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to use the ON_EvPrincipalCurvatures function in C/C++."
keywords = [ "rhino", "curves" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Create Principal Curvature Curves"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/principalcurvaturelines"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

You are looking for a way to create Principal Curvature lines starting with points on a surface.  There is an ON
an `ON_EvPrincipalCurvatures` function, it's not clear how it should be used.

## Solution

The Rhino C/C++ SDK does not have a function to create these Principal Curvature curves.  But, using `ON_EvPrincipalCurvatures`, you *can* calculate them.

Before using `ON_EvPrincipalCurvatures`, you will need to calculate the second derivative of the surface that the test location.  Then, it is just a matter or cooking up some curves based on the results.

## Sample

The following is an example of how you might write such a command...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObject* obj = go.Object(0).Object();
  const ON_BrepFace* face = go.Object(0).Face();
  if( 0 == obj | 0 == face )
    return CRhinoCommand::failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Select point on surface" );
  gp.Constrain( *face, obj->Attributes().m_wire_density );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  double s, t;
  const ON_Surface* srf = gp.PointOnSurface( &s, &t );
  if( 0 == srf )
    return CRhinoCommand::failure;

  ON_3dPoint P;
  ON_3dVector Ds, Dt, Dss, Dst, Dtt;
  if( !srf->Ev2Der(s, t, P, Ds, Dt, Dss, Dst, Dtt) )
    return CRhinoCommand::failure; // failed to evaluate derivatives

  ON_3dVector N;
  if( !srf->EvNormal(s, t, N) )
    return CRhinoCommand::failure; // failed to evaluate normal

  double gauss, mean, k[2];
  ON_3dVector K[2];
  if( !ON_EvPrincipalCurvatures(Ds, Dt, Dss, Dst, Dtt, N, &gauss, &mean, &k[0], &k[1], K[0], K[1]) )
    return CRhinoCommand::failure; // failed to evaluate principal curvatures

  int i;
  for( i = 0; i < 2; i++ )
  {
    if( fabs(k[i]) <= 1.0e-4 | fabs(k[i]) >= 1.0e4 )
    {
      // just draw a line as curvature is huge/tiny
      ON_Line line( P - K[i] * 5.0, P + K[i] * 5.0 );
      context.m_doc.AddCurveObject( line );
    }
    else
    {
      double r = 1.0 / k[i];
      ON_3dPoint center = P + r * N;
      ON_3dPoint start = center - r * K[i];
      ON_3dPoint end = center + r * K[i];
      ON_Arc arc( start, P, end );
      context.m_doc.AddCurveObject( arc );
    }
  }
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
