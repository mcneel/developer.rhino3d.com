---
layout: code-sample-cpp
title: Get Point at Mouse Location
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/pointatcursor
description: Discusses how to convert a 2D screen point into a 3D world point.
order: 1
---

```cpp
static bool GetPointAtCursorPos( ON_3dPoint& point )
{
  bool rc = false;
  CRhinoView* view = RhinoApp().ActiveView();
  if (view)
  {
    POINT pt;
    if (::GetCursorPos(&pt) )
    {
      view->ScreenToClient( &pt );
      ON_Xform xform;
      if( view->ActiveViewport().VP().GetXform(ON::screen_cs, ON::world_cs, xform) )
      {
        point = ON_3dPoint( pt.x, pt.y, 0.0 );
        point.Transform( xform );
        rc = true;
      }
    }
  }
  return rc;
}
```
