---
title: Adding a NURBS Curve from Control Points
description: This guide demonstrates two ways to create a clamped NURBS curve from a set of control points using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/addnurbscurve
order: 1
keywords: ['rhino', 'nurbs', 'curve', 'control', 'points']
layout: toc-guide-page
TODO: 'needs more explanation in order to be a guide'
---

# {{ page.title }}

{{ page.description }}

## Overview

Imagine you would like to create a NURBS curve from a set of control points, such that it looks like this:

![NURBS Curve Control Points]({{ site.baseurl }}/images/adding_a_nurbs_curve_from_control_points_01.png)

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
