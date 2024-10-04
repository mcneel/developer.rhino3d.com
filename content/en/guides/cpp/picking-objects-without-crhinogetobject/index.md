+++
aliases = ["/en/5/guides/cpp/picking-objects-without-crhinogetobject/", "/en/6/guides/cpp/picking-objects-without-crhinogetobject/", "/en/7/guides/cpp/picking-objects-without-crhinogetobject/", "/wip/guides/cpp/picking-objects-without-crhinogetobject/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates an alternate technique to picking objects without using CRhinoGetObject."
keywords = [ "rhino", "picking" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Picking Objects without CRhinoGetObject"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pickobjects"
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

 
## Problem

Imagine you  have a 3D point, now you want to pick all the objects that are underneath it.

## Solution

You can use `CRhinoPickContext` to build your own object picker.  For more details on `CRhinoPickContext`, see *rhinoSdkPick.h*. With the `CRhinoPickContext` class, you can define the rules for picking.  For example, you can specify a picking style (point, window, crossing).  You can also specify a filter so you only pick the types of objects you want. The most important part is to define a pick chord, which starts on near clipping plane and ends on far clipping plane.

After you have created the `CRhinoPickContext` object and filled out its parameters, call `CRhinoDoc::PickObjects`.  This function goes through the list of eligible objects and intersects them with the pick frustum.  If they hit the frustum in an acceptable manner, the object is added to a pick list passed in by the caller.

Here is a simple example of a function that might work for you:

```cpp
static int MyObjectPicker( CRhinoDoc& doc, CRhinoView* view, POINT point, CRhinoObjRefArray& pick_list )
{
  if( 0 == view )
    return 0;

  CRhinoPickContext pick_context;
  pick_context.m_view = view;
  pick_context.m_pick_style = CRhinoPickContext::point_pick;

  CRhinoViewport& active_vp = view->ActiveViewport();
  switch( active_vp.DisplayMode() )
  {
    case ON::shaded_display:
    case ON::renderpreview_display:
      pick_context.m_pick_mode = CRhinoPickContext::shaded_pick;
      break;
  }

  int pick_count = 0;
  if( active_vp.GetPickXform(point.x, point.y, pick_context.m_pick_region.m_xform) )
  {
    // adds objects to pick_list - does not change any status
    active_vp.VP().GetFrustumLine( point.x, point.y, pick_context.m_pick_line );
    pick_context.UpdateClippingPlanes();
    pick_count = doc.PickObjects( pick_context, pick_list );
  }

  return pick_count;
}
```

And, here is a sample of its use:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetPoint gp;
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  CRhinoView* view = gp.View();
  if( 0 == view )
    return failure;

  ON_Xform w2s;
  view->ActiveViewport().VP().GetXform( ON::world_cs, ON::screen_cs, w2s );

  ON_3dPoint pt3d = gp.Point();
  pt3d.Transform( w2s );

  POINT pt2d;
  pt2d.x = (int)pt3d.x;
  pt2d.y = (int)pt3d.y;

  CRhinoObjRefArray pick_list;
  int pick_count = MyObjectPicker( context.m_doc, view, pt2d, pick_list );
  for( int i = 0; i < pick_count; i++ )
  {
    const CRhinoObject* obj = pick_list[i].Object();
    if( obj )
      obj->Select( true, true, true );
  }
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
