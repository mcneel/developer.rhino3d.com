+++
aliases = ["/en/5/samples/cpp/create-new-view/", "/en/6/samples/cpp/create-new-view/", "/en/7/samples/cpp/create-new-view/", "/en/wip/samples/cpp/create-new-view/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Viewports and Views" ]
description = "Demonstrates how to create a new view that has the properties of an existing view."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Create New View"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/newview"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  AFX_MANAGE_STATE( ::RhinoApp().RhinoModuleState() );

  ON_SimpleArray<ON_UUID> viewport_ids;
  ON_SimpleArray<CRhinoView*> view_list;
  CRhinoView* view = 0;
  int i = 0;

  // Build a list of (current) viewport ids
  context.m_doc.GetViewList( view_list, true, false );
  for( i = 0; i < view_list.Count(); i++ )
  {
    CRhinoView* view = view_list[i];
    if( view )
      viewport_ids.Append( view->ActiveViewportID() );
  }
  view_list.Empty();

  // Create a new view
  context.m_doc.NewView( ON_3dmView() );

  // Find the viewport (id) that was just created
  context.m_doc.GetViewList( view_list, true, false );
  for( i = 0; i < view_list.Count(); i++ )
  {
    view = view_list[i];
    if( view )
    {
      int rc = viewport_ids.Search( view->ActiveViewportID() );
      if( rc < 0 )
        break;
      else
        view = 0;
    }
  }

  // Make the necessary updates.
  if( view )
  {
    ON_3dmView v = view->ActiveViewport().View();
    v.m_name = L"New View";
    view->ActiveViewport().SetView( v );
    view->Redraw();
  }

  return CRhinoCommand::success;
}
```
