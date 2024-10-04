+++
aliases = ["/en/5/samples/cpp/ghost-viewport/", "/en/6/samples/cpp/ghost-viewport/", "/en/7/samples/cpp/ghost-viewport/", "/wip/samples/cpp/ghost-viewport/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to set a viewport to ghosted display."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Ghost Viewport"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/ghostedshade"
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

  CRhinoViewport& vp = view->ActiveViewport();

  const CDisplayPipelineAttributes* pStdAttrs = CRhinoDisplayAttrsMgr::StdGhostedAttrs();
  if( pStdAttrs )
  {
    vp.SetDisplayMode( pStdAttrs->Id() );
    view->Redraw();
  }

  return CRhinoCommand::success;
}
```
