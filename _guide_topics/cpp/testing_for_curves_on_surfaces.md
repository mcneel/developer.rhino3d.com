---
title: Testing for Curves on Surfaces
description: This guide discusses how to test to see if a curve lies on a surface using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/iscurveonsurface
order: 1
keywords: ['rhino', 'curves', 'surfaces']
layout: toc-guide-page
---

# Testing for Curves on Surfaces

{{ page.description }}

## Problem

In your plugin, you are using a surface and an interpolated curve on that surface.  You know the curve is interpolated on the surface because that is how you created it (using the *InterpCrfOnSrf* command).  Now, what if you import some other 3dm file with curve and surface already in it?  How can one check that curve lies completely on surface using C/C++?

## Solution

The Rhino C/C++ SDK does not have a function that tests whether or not a curve lies on a surface.  But, you can write your own test that should give you the correct answer for most cases.

The best approach for writing a function to do this would be to sample many curve points and perform closest point tests against the surface with each curve point.  If the distance between the curve points and the surface points are within some tolerance, then chances are the curve is on the surface - at least the sampled points are on the surface.

## Sample

The following sample function does just this:

```cpp
// Description:
//   Test to see if a curve lies on a surface.
// Parameters:
//   srf - [in] The surface
//   crv - [in] The curve
//   tol - [in] The tolerance
// Returns:
//   True if the curve (probably) lies on the surface.
//   False otherwise.

static bool RhinoIsCurveOnSurface(
        const ON_Surface& srf,
        const ON_Curve& crv,
        double tol
        )
{
  if( !srf.IsValid() | !crv.IsValid() )
    return false;

  ON_NurbsCurve nc;
  if( !crv.GetNurbForm(nc) )
    return false;

  const int span_count = nc.SpanCount();
  ON_SimpleArray<double> span_vector( span_count + 1 );
  span_vector.SetCount( span_count + 1 );
  nc.GetSpanVector( span_vector.Array() );

  bool rc = true;
  double num_samples = nc.Degree() * 2;
  int i, j;
  for( i = 0; i < span_count && rc; i++ )
  {
    ON_Interval span( span_vector[i], span_vector[i+1] );
    rc = span.IsIncreasing();
    if( rc )
    {
      for( j = 0; j <= num_samples && rc; j++ )
      {
        double crv_t = span.ParameterAt( j / num_samples );
        ON_3dPoint crv_pt = nc.PointAt( crv_t );
        double s = 0.0, t = 0.0;
        rc = srf.GetClosestPoint( crv_pt, &s, &t );
        if( rc )
        {
          ON_3dPoint srf_pt = srf.PointAt( s, t );
          rc = ( fabs(crv_pt.DistanceTo(srf_pt)) <= tol );
        }
      }
    }
  }

  return rc;
}
```
