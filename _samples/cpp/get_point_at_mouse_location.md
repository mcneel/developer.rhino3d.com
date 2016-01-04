---
title: Get Point at Mouse Location
description: Discusses how to convert a 2D screen point into a 3D world point.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/pointatcursor
order: 1
keywords: ['rhino']
layout: code-sample-cpp
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
