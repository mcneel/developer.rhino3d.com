---
title: Transform Screen to World Coordinates
description: Demonstrates how to transform screen coordinates to world coordinates.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/screentoworld
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoCommand::result rc = failure;

  // Get the active view
  CRhinoView* view = RhinoApp().ActiveView();
  if( view )
  {
    // Get the current cursor position
    POINT point;
    if( GetCursorPos(&point ) )
    {
      // Convert the screen coordinates to client coordinates
      view->ScreenToClient( &point );

      // Obtain the view's screen-to-world transformation
      ON_Xform screen_to_world;
      view->ActiveViewport().VP().GetXform( ON::screen_cs, ON::world_cs, screen_to_world );

      // Create a 3-D point
      ON_3dPoint pt( point.x, point.y, 0 );
      // Transform it
      pt.Transform( screen_to_world );

      // Add it to the document
      context.m_doc.AddPointObject( pt );
      context.m_doc.Redraw();

      rc = success;
    }
  }

  return rc;
}
```
