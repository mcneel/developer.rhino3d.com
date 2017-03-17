---
title: Zoom Extents of Points
description: Demonstrates how to zoom to the extends of an array of 3D points.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/zoompoints
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
static void ZoomExtents( CRhinoView* view, const ON_3dPointArray& point_array )
{
  if( 0 == view )
    return;

  const ON_Viewport& current_vp = view->ActiveViewport().VP();
  ON_Viewport zoomed_vp;

  ON_Xform w2c;
  current_vp.GetXform( ON::world_cs, ON::camera_cs, w2c );

  ON_BoundingBox bbox = point_array.BoundingBox();
  if( bbox.IsValid() )
  {
    double border = 1.1;

    double dx = bbox.m_max.x - bbox.m_min.x;
    dx *= 0.5 * (border - 1.0);
    bbox.m_max.x += dx;
    bbox.m_min.x -= dx;

    double dy = bbox.m_max.y - bbox.m_min.y;
    dy *= 0.5 * (border - 1.0);
    bbox.m_max.y += dy;
    bbox.m_min.y -= dy;

    if( RhinoDollyExtents(current_vp, bbox, zoomed_vp) )
    {
      view->ActiveViewport().SetVP( zoomed_vp, true );
      view->Redraw();
    }
  }
}
```
