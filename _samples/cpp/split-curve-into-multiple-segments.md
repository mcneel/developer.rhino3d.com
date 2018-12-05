---
title: Split Curve Into Multiple Segments
description: Demonstrates how to split a curve into multiple curve segments.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/sdksamples/curvesplitter
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select curve to split
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve to split" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Validate selection
  const CRhinoObjRef& crv_obj_ref = go.Object(0);
  const CRhinoObject* crv_obj = crv_obj_ref.Object();
  const ON_Curve* crv = crv_obj_ref.Curve();
  if( 0 == crv_obj | 0 == crv )
    return failure;

  // Number of segments to create
  CRhinoGetInteger gi;
  gi.SetCommandPrompt( L"Number of segments to create" );
  gi.SetLowerLimit( 2 );
  gi.SetUpperLimit( 100 );
  gi.GetInteger();
  if( gi.CommandResult() != success )
    return gi.CommandResult();

  int num_segments = gi.Number();

  // Generate an array of curve parameters where
  // the splitting will occur.
  ON_SimpleArray<double> curve_t( num_segments );
  bool rc = RhinoDivideCurve( *crv, num_segments, 0, false, true, 0, &curve_t );
  if( !rc )
  {
    RhinoApp().Print( L"Error dividing curve into segments.\n" );
    return failure;
  }

  // If the curve is closed, append the ending domain parameter
  ON_Interval dom = crv->Domain();
  if( crv->IsClosed() )
    curve_t.Append( dom.m_t[1] );

  ON_3dmObjectAttributes atts( crv_obj->Attributes() );

  // Do the splitting (or should I say trimming...)
  int i;
  for( i = 0; i < curve_t.Count() - 1; i++ )
  {
    // Build an interval to trim
    ON_Interval interval( curve_t[i], curve_t[i+1] );
    if( dom.Includes(interval) )
    {
      // Do the trim
      ON_Curve* new_crv = ON_TrimCurve( *crv, interval );
      if( new_crv )
      {
        // Add the "trimmed" curve
        CRhinoCurveObject* new_crv_obj = new CRhinoCurveObject( atts );
        new_crv_obj->SetCurve( new_crv );
        context.m_doc.AddObject( new_crv_obj );
      }
    }
  }

  // Delete the original object
  context.m_doc.DeleteObject( crv_obj_ref );
  context.m_doc.Redraw();

  return success;
}
```
