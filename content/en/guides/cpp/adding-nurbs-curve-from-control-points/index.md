+++
aliases = ["/en/5/guides/cpp/adding-nurbs-curve-from-control-points/", "/en/6/guides/cpp/adding-nurbs-curve-from-control-points/", "/en/7/guides/cpp/adding-nurbs-curve-from-control-points/", "/en/wip/guides/cpp/adding-nurbs-curve-from-control-points/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates two ways to create a clamped NURBS curve from a set of control points using C/C++."
keywords = [ "rhino", "nurbs", "curve", "control", "points" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Adding a NURBS Curve from Control Points"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs more explanation in order to be a guide"
origin = "http://wiki.mcneel.com/developer/sdksamples/addnurbscurve"
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


## Overview

Imagine you would like to create a NURBS curve from a set of control points, such that it looks like this:

![NURBS Curve Control Points](/images/adding-a-nurbs-curve-from-control-points-01.png)

There are two methods to achieve this...

## Method 1

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
{
  ON_3dPointArray points;
  points.Append( ON_3dPoint(0, 0, 0) );
  points.Append( ON_3dPoint(0, 2, 0) );
  points.Append( ON_3dPoint(2, 4, 0) );
  points.Append( ON_3dPoint(4, 2, 0) );
  points.Append( ON_3dPoint(4, 0, 0) );

  ON_NurbsCurve* nc = ON_NurbsCurve::New();
  nc->CreateClampedUniformNurbs( 3, 4, points.Count(), points );

  if( nc->IsValid() )
  {
    context.m_doc.AddCurveObject( *nc );
    context.m_doc.Redraw();
  }

  RhinoApp().ActiveDoc()->Redraw();
  return CRhinoCommand::success;
}
```

## Method 2

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
{
  ON_3dPointArray points;
  points.Append( ON_3dPoint(0, 0, 0) );
  points.Append( ON_3dPoint(0, 2, 0) );
  points.Append( ON_3dPoint(2, 4, 0) );
  points.Append( ON_3dPoint(4, 2, 0) );
  points.Append( ON_3dPoint(4, 0, 0) );

  int dimension = 3;
  bool bIsRat = false;
  int order = 4;
  int cv_count = points.Count();

  ON_NurbsCurve* nc = ON_NurbsCurve::New(dimension, bIsRat, order, cv_count);
  if( !nc )
        return CRhinoCommand::failure;

  //Set CV points
  nc->ReserveCVCapacity( cv_count );
  for( int i = 0; i < points.Count(); i++ )
  {
        nc->SetCV(i, points[i] );
  }

  //Set Knots
  nc->ReserveKnotCapacity( order+cv_count-2 );
  ON_MakeClampedUniformKnotVector( order, cv_count, nc->m_knot );

  if( nc->IsValid() )
  {
    context.m_doc.AddCurveObject( *nc );
    context.m_doc.Redraw();
  }

  RhinoApp().ActiveDoc()->Redraw();
  return CRhinoCommand::success;
}
```
