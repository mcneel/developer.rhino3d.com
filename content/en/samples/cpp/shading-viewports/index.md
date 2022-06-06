+++
aliases = ["/5/samples/cpp/shading-viewports/", "/6/samples/cpp/shading-viewports/", "/7/samples/cpp/shading-viewports/", "/wip/samples/cpp/shading-viewports/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to set a viewport to shaded display."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Shading Viewports"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/shadedisplay"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoView* view = RhinoApp().ActiveView();
  if( 0 == view )
    return CRhinoCommand::failure;

  ON::display_mode dm = view->ActiveViewport().DisplayMode();
  if( dm != ON::shaded_display )
  {
    view->ActiveViewport().SetDisplayMode( ON::shaded_display );
    context.m_doc.ViewModified( view );
    view->Redraw();
  }

  return CRhinoCommand::success;
}
```
