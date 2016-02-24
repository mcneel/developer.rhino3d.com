---
title: Finding Points on Curves at Arc Length Distances
description: This guide demonstrates how to find points that are a specified distance from the start of curves using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/sdksamples/arclengthpoint
order: 1
keywords: ['rhino']
layout: toc-guide-page
---

# Finding Points on Curves at Arc Length Distances

{{ page.description }}

## Problem

For a given length from the beginning of a curve, you would like to get the curve's parameter at this  point.

## Solution

The two functions on `ON_Curve` that are useful for determining the parameter of the point on a curve that is a prescribed arc length distance from the start of a curve are:

- `ON_Curve::GetNormalizedArcLengthPoint`
- `ON_Curve::GetNormalizedArcLengthPoints`

To use these functions, calculate a normalized arc length parameter.  That is, a parameter on the curve where 0.0 = the start of the curve, 0.5 = the midpoint of the curve, and 1.0 = the end of the curve.

**NOTE**: To determine the parameter of the point on a curve that is a prescribed arc length distance from the end of a curve, just reverse the curve before calling one of the above curve members.

## Sample

The following code sample demonstrates how to use these functions:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& obj_ref = go.Object(0);
  const ON_Curve* crv = obj_ref.Curve();
  if( 0 == crv )
    return failure;

  double crv_length = 0.0;
  if( !crv->GetLength(&crv_length) )
    return failure;

  CRhinoGetNumber gn;
  gn.SetCommandPrompt( L"Length from start" );
  gn.SetLowerLimit( 0.0, TRUE );
  gn.SetUpperLimit( crv_length, TRUE );
  gn.GetNumber();
  if( gn.CommandResult() != success )
    return gn.CommandResult();

  // Cook up a normalized arc length parameter,
  // where 0.0 <= s <= 1.0.
  double length = fabs( gn.Number() );
  double s = 0.0;
  if( length == 0.0 )
    s = 0.0;
  else if( length == crv_length )
    s = 1.0;
  else
    s = length / crv_length;

  // Get the parameter of the point on the curve that is a
  // prescribed arc length from the start of the curve.
  double t = 0.0;
  if( crv->GetNormalizedArcLengthPoint(s, &t) )
  {
    ON_3dPoint pt = crv->PointAt( t );
    context.m_doc.AddPointObject( pt );
    context.m_doc.Redraw();
  }

  return success;
}
```
