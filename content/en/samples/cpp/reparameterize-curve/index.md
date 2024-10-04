+++
aliases = ["/en/5/samples/cpp/reparameterize-curve/", "/en/6/samples/cpp/reparameterize-curve/", "/en/7/samples/cpp/reparameterize-curve/", "/wip/samples/cpp/reparameterize-curve/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to Reparameterize a curve object."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Reparameterize Curve"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/reparameterizecrv"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoCommand::result rc = CRhinoCommand::success;

  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve to reparameterize" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  rc = go.CommandResult();
  if( rc != CRhinoCommand::success )
    return rc;

  CRhinoObjRef& objref = go.Object(0);
  const ON_Curve* pC = objref.Curve();
  if( !pC )
    return CRhinoCommand::failure;

  double s0, s1;
  pC->GetDomain( &s0, &s1 );

  CRhinoGetNumber gn;
  gn.SetCommandPrompt( L"Domain start" );
  gn.SetDefaultNumber( s0 ) ;
  gn.AcceptNothing();
  gn.GetNumber();
  rc = gn.CommandResult();
  if( rc != CRhinoCommand::success )
    return rc;

  double t0 = gn.Number();

  gn.SetCommandPrompt( L"Domain end" );
  gn.SetDefaultNumber( s1 );
  gn.SetLowerLimit( t0, TRUE );
  gn.AcceptNothing();
  gn.GetNumber();
  rc = gn.CommandResult();
  if( rc != CRhinoCommand::success )
    return rc;

  double t1 = gn.Number();

  if( s0 == t0 && s1 == t1 )
    return CRhinoCommand::nothing;

  ON_Curve *pNC = pC->DuplicateCurve();
  if( pNC )
  {
    pNC->SetDomain( t0, t1 );
    CRhinoCurveObject* obj = new CRhinoCurveObject();
    if( obj )
    {
      obj->SetCurve( pNC );
      context.m_doc.ReplaceObject( objref, obj );
      context.m_doc.Redraw();
   }
   else
     rc = CRhinoCommand::failure;
  }
  else
    rc = CRhinoCommand::failure;

  return rc;
}
```
