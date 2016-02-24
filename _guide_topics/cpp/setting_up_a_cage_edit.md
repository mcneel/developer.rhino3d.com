---
title: Setting Up a Cage Edit
description: This guide demonstrates how to setup a cage editing scenario using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/cageedit
order: 1
keywords: ['rhino', 'cage', 'edit']
layout: toc-guide-page
---

# Setting Up a Cage Edit

{{ page.description }}

## Problem

Imagine you have two objects: a surface and a line curve and you would like to setup cage editing, with the surface as the captive object and the line curve as the control object.

## Solution

To allow the line curve to control the surface, you will need to create a `CRhinoMorphControl` object.  A `CRhinoMorphControl` object has a `ON_MorphControl` object, as its data member, which contains the definition of the controlling object (in this case, line).

Once you have properly defined the `ON_MorphControl` object and created the runtime `CRhinoMorphControl` object, you can use the RhinoCaptureObject API function to setup the "capture."

The following example code demonstrates how you might write a command that allows a surface to be controlled by a line...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  ON_Workspace ws;
  CRhinoCommand::result rc = CRhinoCommand::success;

  // Get the captive object
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select captive surface or polysurface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
  go.GetObjects( 1, 1 );
  rc = go.CommandResult();
  if( CRhinoCommand::success != rc )
    return rc;

  const CRhinoObject* captive = go.Object(0).Object();
  if( 0 == captive )
    return CRhinoCommand::failure;

  // Define the control line
  ON_Line line;
  rc = RhinoGetLine( CArgsRhinoGetLine(), line );
  if( CRhinoCommand::success != rc )
    return rc;

  // Get the curve parameters
  int degree = 3;
  int cv_count = 4;
  for(;;)
  {
    CRhinoGetOption gl;
    gl.SetCommandPrompt( L"NURBS Parameters" );
    gl.AcceptNothing();
    int d_opt = gl.AddCommandOptionInteger( RHCMDOPTNAME(L"Degree"), &degree, L"Curve degree", 1.0, 100.0 );
    int p_opt = gl.AddCommandOptionInteger( RHCMDOPTNAME(L"PointCount"), &cv_count, L"Number of control points", 2.0, 100.0 );
    gl.GetOption();
    rc = gl.CommandResult();
    if( CRhinoCommand::success != rc )
      return rc;

    if( CRhinoGet::nothing == gl.Result() )
      break;

    if( cv_count <= degree )
    {
      if( CRhinoGet::option != gl.Result() )
        continue;
      const CRhinoCommandOption* opt = go.Option();
      if( 0 == opt )
        continue;
      if( d_opt == opt->m_option_index )
        cv_count = degree + 1;
      else
        degree = cv_count - 1;
    }
  }

  // Set up morph control
  ON_MorphControl* control = new ON_MorphControl();
  control->m_varient = 1; // 1= curve

  // Specify the source line curve
  control->m_nurbs_curve0.Create( 3, false, 2, 2 );
  control->m_nurbs_curve0.MakeClampedUniformKnotVector();
  control->m_nurbs_curve0.SetCV( 0, line.from );
  control->m_nurbs_curve0.SetCV( 1, line.to );

  // Specify the destination NURBS curve
  control->m_nurbs_curve.Create( 3, false, degree + 1, cv_count );
  control->m_nurbs_curve.MakeClampedUniformKnotVector();
  double* g = ws.GetDoubleMemory( control->m_nurbs_curve.m_cv_count );
  control->m_nurbs_curve.GetGrevilleAbcissae( g );
  ON_Interval d = control->m_nurbs_curve.Domain();
  double s = 0.0;
  int i;
  for( i = 0; i < control->m_nurbs_curve.m_cv_count; i++ )
  {
    s = d.NormalizedParameterAt( g[i] );
    control->m_nurbs_curve.SetCV( i, line.PointAt(s) );
  }

  // Make sure domains match
  s = line.Length();
  if( s > ON_SQRT_EPSILON )
    control->m_nurbs_curve0.SetDomain( 0.0, s );
  d = control->m_nurbs_curve0.Domain();
  control->m_nurbs_curve.SetDomain( d[0], d[1] );

  // Create the morph control object
  CRhinoMorphControl* control_object = new CRhinoMorphControl();
  control_object->SetControl( control );
  context.m_doc.AddObject( control_object );

  // Set up the capture
  RhinoCaptureObject( control_object, const_cast<CRhinoObject*>(captive) );

  // Clean up display
  context.m_doc.UnselectAll();

  // Turn on the control grips
  control_object->EnableGrips( true );
  context.m_doc.Redraw( CRhinoView::mark_display_hint );

  return rc;
}
```
