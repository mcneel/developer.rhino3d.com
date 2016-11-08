---
title: Sweeping Surfaces with Sweep2
description: Demonstrates how to use the CArgsRhinoSweep2 class and the RhinoSweep2 function. The definitions of these can be found in rhinoSdkSweep.h.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Surfaces']
origin: http://wiki.mcneel.com/developer/sdksamples/sweep2
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
// Helper function to calculate rail parameters
bool GetShapeParameterOnRail(
  const ON_Curve& shape,
  const ON_Curve& rail,
  double tol,
  double& t
  )
{
  ON_Interval rail_domain = rail.Domain();

  // Test start point
  bool rc = rail.GetClosestPoint( shape.PointAtStart(), &t, tol );
  if( rc )
  {
    if( rail.IsClosed() )
    {
      if( fabs(t - rail_domain.Max()) < ON_SQRT_EPSILON )
        t = rail_domain.Min();
      if( fabs(t - rail_domain.Min()) < ON_SQRT_EPSILON )
        t = rail_domain.Min();
    }
    return true;
  }

  // Test end point
  rc = rail.GetClosestPoint( shape.PointAtEnd(), &t, tol );
  if( rc )
  {
    if( rail.IsClosed() )
    {
      if( fabs(t - rail_domain.Max()) < ON_SQRT_EPSILON )
        t = rail_domain.Min();
      if( fabs(t - rail_domain.Min()) < ON_SQRT_EPSILON )
        t = rail_domain.Min();
    }
    return true;
  }

  // Try intersecting...
  ON_SimpleArray<ON_X_EVENT> x;
  if( 1 == rail.IntersectCurve(&shape, x, tol, 0.0) && x[0].IsPointEvent() )
  {
    t = x[0].m_a[0];
    if( rail.IsClosed() )
    {
      if( fabs(t - rail_domain.Max()) < ON_SQRT_EPSILON )
        t = rail_domain.Min();
    }
    return true;
  }

  return false;
}

// RhinoSweep2 wrapper function
bool MySweep2(
  const ON_Curve* Rail1,
  const CRhinoObject* Rail1_obj,
  const ON_Curve* Rail2,
  const CRhinoObject* Rail2_obj,
  ON_SimpleArray<const ON_Curve*> sCurves,
  ON_SimpleArray<ON_Brep*>& Sweep2_Breps
  )
{
  if( 0 == Rail1 | 0 == Rail1_obj )
    return false;

  if( 0 == Rail2 | 0 == Rail2_obj )
    return false;

  CRhinoDoc* doc = RhinoApp().ActiveDoc();
  if( 0 == doc )
    return false;

  // Define a new class that contains sweep2 arguments
  CArgsRhinoSweep2 args;

  // Set the 2 rails
  CRhinoPolyEdge Edge1, Edge2;
  Edge1.Create( Rail1, Rail1_obj );
  Edge2.Create( Rail2, Rail2_obj );

  // Ok, we can at least do some rail direction matching
  if( !RhinoDoCurveDirectionsMatch(&Edge1, &Edge2) )
    Edge2.Reverse();

  // Add rails to sweep arguments
  args.m_rail_curves[0] = &Edge1;
  args.m_rail_curves[1] = &Edge2;

  args.m_rail_pick_points[0] = ON_UNSET_POINT;
  args.m_rail_pick_points[1] = ON_UNSET_POINT;

  // To create a closed sweep, you need to have:
  //  1. Two closed rail curves and and a single shape curve, or
  //  2. Set CArgsRhinoSweep2::m_bClosed = true
  args.m_bClosed = false;

  double tol = doc->AbsoluteTolerance();

  // Loop through sections to set parameters
  for( int i = 0; i < sCurves.Count(); i++ )
  {
    const ON_Curve* sCurve = sCurves[i];
    if( 0 == sCurve )
      continue;

    // Add to shapes
    args.m_shape_curves.Append( sCurve );

    // Cook up some rail parameters
    double t0 = 0.0;
    if( !GetShapeParameterOnRail(*sCurve, Edge1, tol, t0) )
      return false;
    args.m_rail_params[0].Append( t0 );

    double t1 = 0.0;
    if( !GetShapeParameterOnRail(*sCurve, Edge2, tol, t1) )
      return false;
    args.m_rail_params[1].Append( t1 );
  }

  // Set the rest of parameters
  args.m_simplify = 0;
  args.m_bSimpleSweep = false;
  args.m_bSameHeight = false;
  args.m_rebuild_count = -1; //Sample point count for rebuilding shapes
  args.m_refit_tolerance = tol;
  args.m_sweep_tolerance = tol;
  args.m_angle_tolerance = doc->AngleToleranceRadians();

  // Sweep2
  return RhinoSweep2(args, Sweep2_Breps) ? true : false;
}

// Test command that uses the above functions.
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select first rail curve
  CRhinoGetObject go1;
  go1.SetCommandPrompt( L"Select first rail curve" );
  go1.SetGeometryFilter( CRhinoGetObject::curve_object );
  go1.EnablePreSelect( false );
  go1.GetObjects( 1, 1 );
  if( go1.CommandResult() != success )
    return go1.CommandResult();

  const CRhinoObject* Rail1_obj = go1.Object(0).Object();
  const ON_Curve* Rail1 = go1.Object(0).Curve();
  if( 0 == Rail1_obj | 0 == Rail1 )
    return failure;

  // Select second rail curve
  CRhinoGetObject go2;
  go2.SetCommandPrompt( L"Select second rail curve" );
  go2.SetGeometryFilter( CRhinoGetObject::curve_object );
  go2.EnablePreSelect( false );
  go2.EnableDeselectAllBeforePostSelect( false );
  go2.GetObjects( 1, 1 );
  if( go2.CommandResult() != success )
    return go2.CommandResult();

  const CRhinoObject* Rail2_obj = go2.Object(0).Object();
  const ON_Curve* Rail2 = go2.Object(0).Curve();
  if( 0 == Rail2_obj | 0 == Rail2 )
    return failure;

  // Select cross section curves
  CRhinoGetObject gx;
  gx.SetCommandPrompt( L"Select cross section curves" );
  gx.SetGeometryFilter( CRhinoGetObject::curve_object );
  gx.EnablePreSelect( false );
  gx.EnableDeselectAllBeforePostSelect( false );
  gx.GetObjects( 1, 0 );
  if( gx.CommandResult() != success )
    return gx.CommandResult();

  ON_SimpleArray<const ON_Curve*> sCurves;
  int i;
  for( i = 0; i < gx.ObjectCount(); i++ )
  {
    const ON_Curve* sCurve = gx.Object(i).Curve();
    if( sCurve )
      sCurves.Append( sCurve );
  }

  // Call MySweep2 function
  ON_SimpleArray<ON_Brep*> Sweep2_Breps;
  if( MySweep2(Rail1, Rail1_obj, Rail2, Rail2_obj, sCurves, Sweep2_Breps) )
  {
    // Add to context then delete
    for( i = 0; i < Sweep2_Breps.Count(); i++ )
    {
      ON_Brep* brep = Sweep2_Breps[i];
      if( brep )
      {
        context.m_doc.AddBrepObject( *brep );
        delete Sweep2_Breps[i]; // Don't leak...
        Sweep2_Breps[i] = 0;
      }
    }

    context.m_doc.Redraw();
  }

  return success;
}
```
