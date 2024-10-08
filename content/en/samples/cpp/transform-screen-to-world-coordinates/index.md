+++
aliases = ["/en/5/samples/cpp/transform-screen-to-world-coordinates/", "/en/6/samples/cpp/transform-screen-to-world-coordinates/", "/en/7/samples/cpp/transform-screen-to-world-coordinates/", "/en/wip/samples/cpp/transform-screen-to-world-coordinates/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to transform screen coordinates to world coordinates."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Transform Screen to World Coordinates"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/screentoworld"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
