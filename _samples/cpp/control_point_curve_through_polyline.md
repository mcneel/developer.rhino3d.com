---
title: Control Point Curve Through Polyline
description: Demonstrates how to create a control points curve through a polyline.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/sdksamples/crvthroughpline
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
ON_NurbsCurve* RhControlPointsCurveThroughPolyline(
    const ON_Polyline& polyline,
    int degree
    )
{
  const int count = polyline.Count();
  if( count < 2 )
    return 0;

  degree = ( count <= degree) ? count - 1 : degree;

  ON_NurbsCurve* curve = ON_NurbsCurve::New();
  if( curve )
  {
    bool rc = false;
    if( polyline.IsClosed() )
      rc = curve->CreatePeriodicUniformNurbs( 3, degree + 1, count - 1, polyline );
    else
      rc = curve->CreateClampedUniformNurbs( 3, degree + 1, count, polyline );

    if( !rc )
    {
      delete curve;
      curve = 0;
    }
  }

  return curve;
}
```
