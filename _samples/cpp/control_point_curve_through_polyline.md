---
layout: code-sample-cpp
title: Control Point Curve Through Polyline
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/crvthroughpline
description: Demonstrates how to create a control points curve through a polyline.
order: 1
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
