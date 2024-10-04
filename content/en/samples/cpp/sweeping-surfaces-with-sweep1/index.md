+++
aliases = ["/en/5/samples/cpp/sweeping-surfaces-with-sweep1/", "/en/6/samples/cpp/sweeping-surfaces-with-sweep1/", "/en/7/samples/cpp/sweeping-surfaces-with-sweep1/", "/wip/samples/cpp/sweeping-surfaces-with-sweep1/"]
authors = [ "dale" ]
categories = [ "Surfaces" ]
description = "Demonstrates how to use the CArgsRhinoSweep1 class and the RhinoSweep1 function. The definitions of these can be found in rhinoSdkSweep.h."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Sweeping Surfaces with Sweep1"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/sweep1"
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
  go.SetCommandPrompt( L"Select rail curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects(1,1);
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& rail_ref = go.Object(0);
  const CRhinoObject* rail_obj = rail_ref.Object();
  if( !rail_obj )
    return failure;
  const ON_Curve* rail_crv = rail_ref.Curve();
  if( !rail_crv )
    return failure;

  CRhinoGetObject gx;
  gx.SetCommandPrompt( L"Select cross section curves" );
  gx.SetGeometryFilter( CRhinoGetObject::curve_object );
  gx.EnablePreSelect( false );
  gx.EnableDeselectAllBeforePostSelect( false );
  gx.GetObjects(1,0);
  if( gx.CommandResult() != success )
    return gx.CommandResult();

  CRhinoPolyEdge edge;
  edge.Create( rail_crv, rail_obj );

  CArgsRhinoSweep1 args;
  args.m_rail_curve = edge.Duplicate();
  args.m_bHaveRailPickPoint = false;
  args.m_bClosed = rail_crv->IsClosed();
  args.m_bUsePivotPoint = false;

  int i;
  for( i = 0; i < gx.ObjectCount(); i++ )
  {
    const CRhinoObjRef& obj_ref = gx.Object(i);
    const ON_Curve* crv = obj_ref.Curve();
    if( crv )
    {
      ON_Curve* dup_crv = crv->DuplicateCurve();

      double t = 0;
      edge.GetClosestPoint( dup_crv->PointAtStart(), &t );

      args.m_shape_curves.Append( dup_crv );
      args.m_rail_params.Append( t );
      args.m_shape_objrefs.Append( obj_ref );
    }
  }

  // Start and end points
  args.m_bUsePoints[0] = 0;
  args.m_bUsePoints[1] = 0;

  // Point objects picked for endpoints
  args.m_bClosed = false;
  args.m_style = 0;
  args.m_planar_up = ON_zaxis; // Don't need this, but set it anyway..
  args.m_simplify = 0; // Simplify method for shape curves
  args.m_rebuild_count = -1; // Sample point count for rebuilding shapes
  args.m_refit_tolerance = context.m_doc.AbsoluteTolerance();
  args.m_sweep_tolerance = context.m_doc.AbsoluteTolerance();
  args.m_angle_tolerance = context.m_doc.AngleToleranceRadians();
  args.m_miter_type = 0; // 0: don't miter

  ON_SimpleArray<ON_Brep*> breps;
  if( RhinoSweep1(args, breps) )
  {
    for( i = 0; i < breps.Count(); i++ )
    {
      context.m_doc.AddBrepObject( *breps[i] );
      delete breps[i];
    }
  }

  // Clean up
  delete args.m_rail_curve;

  for( i = 0; i < args.m_shape_curves.Count(); i++ )
    delete args.m_shape_curves[i];

  context.m_doc.Redraw();

  return success;
}
```
