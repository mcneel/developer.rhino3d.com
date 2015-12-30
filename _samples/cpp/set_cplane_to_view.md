---
layout: code-sample-cpp
title: Set a CPlane to a View
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/cplaneview
description: Demonstrates how to set the construction plane in the active viewport parallel to the view.
order: 1
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
{
  CRhinoCommand::result rc = CRhinoCommand::cancel;

  // Get the active view object
  CRhinoView* view = ::RhinoApp().ActiveView();
  if( view )
  {
    // Get reference to the view's viewport object
    CRhinoViewport& vp = view->Viewport();
    // Create plane object based on viewport parameters
    ON_Plane plane( vp.Target(), vp.VP().CameraX(), vp.VP().CameraY() );
    // Copy viewport's cplane object
    ON_3dmConstructionPlane cplane = vp.ConstructionPlane();
    // Set the cplane's plane object
    cplane.m_plane = plane;
    // Push the new cplane onto the cplane stack
    view->Viewport().PushConstructionPlane( cplane );
    // Redraw the view
    view->Redraw();
    rc = CRhinoCommand::success;
  }
  return rc;
}
```
