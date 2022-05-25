+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to split a brep with another brep using the RhinoSplitBrep function."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Split Brep"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/splitbrep"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Pick the brep to split
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surface or polysuface to split" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& split_ref = go.Object(0);

  const CRhinoObject* split_object = split_ref.Object();
  if( !split_object )
    return failure;

  const ON_Brep* split = split_ref.Brep();
  if( !split )
    return failure;

  // Pick the cutting brep
  go.SetCommandPrompt( L"Select cutting surface or polysuface" );
  go.EnablePreSelect( FALSE );
  go.EnableDeselectAllBeforePostSelect( FALSE );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const ON_Brep* cutter = go.Object(0).Brep();
  if( !cutter )
    return failure;

  ON_SimpleArray<ON_Brep*> pieces;
  double tol = context.m_doc.AbsoluteTolerance();

  // Try splitting the brep
  if( !RhinoBrepSplit(*split, *cutter, tol, pieces) )
    RhinoApp().Print( L"Unable to split brep.\n" );

  int i, count = pieces.Count();
  if( count == 0 | count == 1 )
  {
    if( count == 1 )
      delete pieces[0];
    return nothing;
  }

  CRhinoObjectAttributes attrib = split_object->Attributes();
  attrib.m_uuid = ON_nil_uuid;

  const CRhinoObjectVisualAnalysisMode* vam_list = split_object->m_analysis_mode_list;

  for( i = 0; i < count; i++ )
  {
    CRhinoBrepObject* brep_object = new CRhinoBrepObject( attrib );
    if( brep_object )
    {
      brep_object->SetBrep( pieces[i] );
      if( context.m_doc.AddObject(brep_object) )
        RhinoCopyAnalysisModes( vam_list, brep_object );
      else
        delete brep_object;
    }
  }

  context.m_doc.DeleteObject( split_ref );
  context.m_doc.Redraw();

  return success;
}
```
