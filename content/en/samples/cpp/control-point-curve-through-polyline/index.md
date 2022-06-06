+++
aliases = ["/5/samples/cpp/control-point-curve-through-polyline/", "/6/samples/cpp/control-point-curve-through-polyline/", "/7/samples/cpp/control-point-curve-through-polyline/", "/wip/samples/cpp/control-point-curve-through-polyline/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to create a control points curve through a polyline."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Control Point Curve Through Polyline"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/crvthroughpline"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
