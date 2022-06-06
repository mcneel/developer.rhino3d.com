+++
aliases = ["/5/samples/cpp/convert-arc-to-nurbs-curve/", "/6/samples/cpp/convert-arc-to-nurbs-curve/", "/7/samples/cpp/convert-arc-to-nurbs-curve/", "/wip/samples/cpp/convert-arc-to-nurbs-curve/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to convert an ON_ArcCurve object to an ON_NurbsCurve object."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Convert an Arc to a NURBS Curve"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/convertarctonurbs"
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
  go.SetCommandPrompt( L"Select arc to convert" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.SetGeometryAttributeFilter( CRhinoGetObject::open_curve );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& obj_ref = go.Object(0);
  const CRhinoObject* obj = obj_ref.Object();
  if( !obj )
    return failure;

  const ON_ArcCurve* arc_crv = ON_ArcCurve::Cast( obj_ref.Geometry() );
  if( !arc_crv )
  {
    RhinoApp().Print( L"Curve is not an arc.\n" );
    return nothing;
  }

  ON_NurbsCurve nurbs_crv;
  if( arc_crv->GetNurbForm(nurbs_crv) && nurbs_crv.IsValid() )
  {
    ON_3dmObjectAttributes attribs = obj->Attributes();
    context.m_doc.AddCurveObject( nurbs_crv, &attribs );
    context.m_doc.DeleteObject( obj_ref );
    context.m_doc.Redraw();
    return success;
  }

  return failure;
}
```
