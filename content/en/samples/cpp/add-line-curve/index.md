+++
aliases = ["/en/5/samples/cpp/add-line-curve/", "/en/6/samples/cpp/add-line-curve/", "/en/7/samples/cpp/add-line-curve/", "/wip/samples/cpp/add-line-curve/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Curves" ]
description = "Demonstrates how to add a line curve."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add a Line Curve Object"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addline"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Start of line" );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt_start = gp.Point();

  gp.SetCommandPrompt( L"End of line" );
  gp.SetBasePoint( pt_start );
  gp.DrawLineFromPoint( pt_start, TRUE );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt_end = gp.Point();
  ON_3dVector v = pt_end - pt_start;
  if( v.IsTiny() )
    return CRhinoCommand::nothing;

  ON_Line line( pt_start, pt_end );

  context.m_doc.AddCurveObject( line );
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
