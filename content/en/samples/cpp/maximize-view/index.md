+++
aliases = ["/en/5/samples/cpp/maximize-view/", "/en/6/samples/cpp/maximize-view/", "/en/7/samples/cpp/maximize-view/", "/en/wip/samples/cpp/maximize-view/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to maximize a view."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Maximize View"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/maximizeview"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Name of viewport to maximize" );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  ON_wString view_name( gs.String() );
  view_name.TrimLeftAndRight();
  if( view_name.IsEmpty() )
    return CRhinoCommand::cancel;

  ON_SimpleArray<CRhinoView*> view_list;
  int view_count = context.m_doc.GetViewList( view_list );

  CRhinoView* active_view = NULL;
  int i;

  for( i = 0; i < view_count; i++ )
  {
    CRhinoView* view = view_list[i];
    if( view && view_name.CompareNoCase(view->Viewport().Name()) == 0 )
    {
      active_view = view;
      break;
    }
  }

  if( !active_view )
  {
    RhinoApp().Print( L"Unable to find viewport named %s\n", view_name );
    return CRhinoCommand::nothing;
  }

  ::RhinoApp().SetActiveView( active_view );
  CWnd* frame_wnd = active_view->GetParent();
  if( frame_wnd )
  {
    frame_wnd->ShowWindow( SW_SHOWMAXIMIZED );
    frame_wnd->BringWindowToTop();
  }
  return CRhinoCommand::success;
}
```
