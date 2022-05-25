+++
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Discusses how to convert a 2D screen point into a 3D world point."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Get Point at Mouse Location"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pointatcursor"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
