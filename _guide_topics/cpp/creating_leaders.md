---
title: Creating Leaders
description: This brief guide demonstrates how to an annotation leader using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/leader
order: 1
keywords: ['rhino', 'leaders']
layout: toc-guide-page
---

# Creating Leaders

{{ page.description }}

## How To

Leaders in Rhino are defined by the `ON_Leader2` class.  To construct a leader, you must provide:

1. A plane, or an `ON_Plane` object, which defines the plane in which the leader will be located.
2. Two or more 2D points that line in the plane that you specified above.

In the following sample code, we will construct a simple leader object.  The leader will reside in the world x-y plane and will have four points...

```cpp
CRhinoCommand::result CCommandLeader::RunCommand( const CRhinoCommandContext& context )
{
  // Some set of points that define the leader
  ON_3dPointArray points;
  points.Append( ON_3dPoint(1.0, 1.0, 0.0) );
  points.Append( ON_3dPoint(5.0, 1.0, 0.0) );
  points.Append( ON_3dPoint(5.0, 5.0, 0.0) );
  points.Append( ON_3dPoint(9.0, 5.0, 0.0) );

  // The plane in which the leader resides
  ON_Plane plane = ON_xy_plane;

  // Create the leader
  ON_Leader2 leader;
  leader.SetPlane( plane );

  // Add the points to the leader
  int i;
  for( i = 0; i < points.Count(); i++ )
  {
    // Make sure the points are on the plane
    ON_2dPoint p2;
    if( leader.m_plane.ClosestPointTo(points[i], &p2.x, &p2.y) )
    {
      if( leader.m_points.Count() < 1 | p2.DistanceTo(*leader.m_points.Last()) > ON_SQRT_EPSILON )
        leader.m_points.Append( p2 );
    }
  }

  // Create the leader object
  CRhinoAnnotationLeader* leader_object = new CRhinoAnnotationLeader();
  // Add our leader to the object
  leader_object->SetAnnotation( leader );

  if( context.m_doc.AddObject(leader_object) )
    context.m_doc.Redraw();
  else
    delete leader_object; // error

  return success;
}
```
