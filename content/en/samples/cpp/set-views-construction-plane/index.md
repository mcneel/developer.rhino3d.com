+++
aliases = ["/5/samples/cpp/set-views-construction-plane/", "/6/samples/cpp/set-views-construction-plane/", "/7/samples/cpp/set-views-construction-plane/", "/wip/samples/cpp/set-views-construction-plane/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to set a view's construction plane."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Set a View's Construction Plane"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/setconstructionplane"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
          const CRhinoCommandContext& context )
{
  CRhinoView* view = ::RhinoApp().ActiveView();
  if( !view )
    return CRhinoCommand::failure;

  CRhinoGetOption go;
  go.SetCommandPrompt( L"Select a construction plane" );
  int back_option   = go.AddCommandOption( RHCMDOPTNAME(L"Back") );
  int bottom_option = go.AddCommandOption( RHCMDOPTNAME(L"Bottom") );
  int front_option  = go.AddCommandOption( RHCMDOPTNAME(L"Front") );
  int left_option   = go.AddCommandOption( RHCMDOPTNAME(L"Left") );
  int right_option  = go.AddCommandOption( RHCMDOPTNAME(L"Right") );
  int top_option    = go.AddCommandOption( RHCMDOPTNAME(L"Top") );

  go.GetOption();
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoCommandOption* opt = go.Option();
  if( !opt )
    return CRhinoCommand::failure;

  int option_index = opt->m_option_index;
  ON_3dmConstructionPlane cplane = view->Viewport().ConstructionPlane();
  if( option_index == back_option )
    cplane.m_plane.CreateFromPoints( ON_origin, -ON_xaxis ,ON_zaxis );
  else if( option_index == bottom_option )
    cplane.m_plane.CreateFromPoints( ON_origin, -ON_xaxis, ON_yaxis );
  else if( option_index == front_option )
    cplane.m_plane.CreateFromPoints( ON_origin, ON_xaxis, ON_zaxis );
  else if( option_index == left_option )
    cplane.m_plane.CreateFromPoints( ON_origin, -ON_yaxis, ON_zaxis );
  else if( option_index == right_option )
    cplane.m_plane.CreateFromPoints( ON_origin, ON_yaxis, ON_zaxis );
  else if( option_index == top_option )
    cplane.m_plane.CreateFromPoints( ON_origin, ON_xaxis, ON_yaxis );
  else
    return CRhinoCommand::failure;

  view->Viewport().PushConstructionPlane( cplane );
  view->Redraw();
  return CRhinoCommand::success;
}
```
