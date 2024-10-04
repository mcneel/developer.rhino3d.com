+++
aliases = ["/en/5/guides/cpp/window-selecting/", "/en/6/guides/cpp/window-selecting/", "/en/7/guides/cpp/window-selecting/", "/wip/guides/cpp/window-selecting/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to drag a window to select objects."
keywords = [ "rhino", "window", "selecting" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Window Selecting"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/windowselect"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

The `CRhinoGetObject` class is used for selecting Rhino objects.  When active, `CRhinoGetObject` object will allow the user to select objects either by picking them or by dragging a crossing window.  But, using C/C++, it is possible to write your own object picking class or function.  The heart of such a tool is the `CRhinoPickContext` which defines the rules for the picking.  Once the rules have been defined, you can use `CRhinoDoc::PickObjects` to do the work.

## Sample

The following sample code demonstrates how to drag a window to select objects.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Drag a window to select objects" );
  gp.SetGetPointCursor( RhinoApp().m_default_cursor );
  gp.ConstrainToTargetPlane();
  CRhinoGet::result res = gp.Get2dRectangle( 0, 0, FALSE, PS_DOT );
  if( res != CRhinoGet::rect2d )
    return failure;

  CRect pick_rect = gp.Rectangle2d();
  CRhinoView* view = gp.View();

  CRhinoPickContext pick_context;
  pick_context.m_go = 0;
  pick_context.m_view = view;
  pick_context.m_pick_style = CRhinoPickContext::window_pick;
  pick_context.m_bPickGroups = true;
  switch( view->Viewport().DisplayMode() )
  {
    case ON::shaded_display:
    case ON::renderpreview_display:
      pick_context.m_pick_mode = CRhinoPickContext::shaded_pick;
      break;
  }

  CRhinoObjRefArray pick_list;
  int pick_count = 0;
  if( view->Viewport().GetPickXform(pick_rect, pick_context.m_pick_region.m_xform) )
  {
    pick_context.UpdateClippingPlanes();
    POINT screen_point = pick_rect.BottomRight();
    view->ActiveViewport().VP().GetFrustumLine( screen_point.x, screen_point.y, pick_context.m_pick_line );
    int i, pick_count = context.m_doc.PickObjects( pick_context, pick_list );
    for( i = 0; i < pick_count; i++ )
    {
      const CRhinoObject* obj = pick_list[i].Object();
      if( obj && obj->IsSelectable() )
        obj->Select( true );
    }
    if( pick_count )
      context.m_doc.Redraw();
  }

  return success;
}
```
