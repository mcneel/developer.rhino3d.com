---
title: Set a CPlane to a View
description: Demonstrates how to set the construction plane in the active viewport parallel to the view.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/cplaneview
order: 1
keywords: ['rhino']
layout: code-sample-cpp
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
