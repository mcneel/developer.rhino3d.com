+++
aliases = ["/en/5/samples/cpp/duplicate-borders-of-surfaces/", "/en/6/samples/cpp/duplicate-borders-of-surfaces/", "/en/7/samples/cpp/duplicate-borders-of-surfaces/", "/wip/samples/cpp/duplicate-borders-of-surfaces/"]
authors = [ "dale" ]
categories = [ "Surfaces" ]
description = "Demonstrates how to duplicate the borders of surfaces and polysurfaces."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Duplicate the Borders of Surfaces"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/dupborder"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surface or polysurface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object |
                        CRhinoGetObject::polysrf_object );
  go.AcceptNothing();
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& object_ref = go.Object(0);
  const CRhinoObject* object = object_ref.Object();
  const ON_Brep* brep = object_ref.Brep();
  if( !object | !brep )
    return failure;

  object->Select( false );

  ON_SimpleArray<const ON_Curve*> curve_array( brep->m_E.Count() );

  for( int i = 0; i < brep->m_E.Count(); i++ )
  {
    const ON_BrepEdge& edge = brep->m_E[i];

    // Find only the naked edges
    if( edge.m_ti.Count() == 1 && edge.m_c3i >= 0 )
    {
      ON_Curve* curve = edge.DuplicateCurve();

      // Make the curve direction go in the natural
      // boundary loop direction so that the curve
      // directions come out consistantly
      if( brep->m_T[edge.m_ti[0]].m_bRev3d )
        curve->Reverse();
      if( brep->m_T[edge.m_ti[0]].Face()->m_bRev)
        curve->Reverse();

      curve_array.Append( curve );
    }
  }

  double tol = 2.1 * RhinoApp().ActiveDoc()->AbsoluteTolerance();
  ON_SimpleArray<ON_Curve*> output_array;

  // Join the curves
  if( RhinoMergeCurves(curve_array, output_array, tol) )
  {
    for( int i = 0; i < output_array.Count(); i++ )
    {
      CRhinoCurveObject* curve_object = new CRhinoCurveObject;
      curve_object->SetCurve( output_array[i]);
      if( context.m_doc.AddObject(curve_object) )
        curve_object->Select();
      else
        delete curve_object;
    }
  }

  // Don't leak memory
  for( int i = 0; i < curve_array.Count(); i++ )
    delete curve_array[i];

  context.m_doc.Redraw();
  return success;
}
```
