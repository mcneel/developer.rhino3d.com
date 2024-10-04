+++
aliases = ["/en/5/samples/cpp/transform-world-to-screen-coordinates/", "/en/6/samples/cpp/transform-world-to-screen-coordinates/", "/en/7/samples/cpp/transform-world-to-screen-coordinates/", "/wip/samples/cpp/transform-world-to-screen-coordinates/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to transform world coordinates to screen coordinates."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Transform World to Screen Coordinates"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/worldtoscreen"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Pick a point
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Pick point" );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  // Get the view the point was picked in
  CRhinoView* view = gp.View();
  if( 0 == view )
    return CRhinoCommand::failure;

  // Obtain the view's world-to-screen transformation
  ON_Xform world_to_screen;
  view->ActiveViewport().VP().GetXform( ON::world_cs, ON::screen_cs, world_to_screen );

  // Get the picked point
  ON_3dPoint picked_pt = gp.Point();

  // Create a 3-D point
  ON_3dPoint screen_pt = picked_pt;
  // Transform it
  screen_pt.Transform( world_to_screen );

  // Create a Windows 2-D point from the transformed point
  POINT pt2d;
  pt2d.x = (int)screen_pt.x;
  pt2d.y = (int)screen_pt.y;

  // TODO...

  RhinoApp().Print( L"Screen point = %d, %d\n", pt2d.x, pt2d.y );

  return CRhinoCommand::success;
}
```
