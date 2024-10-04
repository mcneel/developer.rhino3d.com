+++
aliases = ["/en/5/samples/cpp/rotate-objects-around-center/", "/en/6/samples/cpp/rotate-objects-around-center/", "/en/7/samples/cpp/rotate-objects-around-center/", "/wip/samples/cpp/rotate-objects-around-center/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how rotate objects around the center point of their bounding box."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Rotate Objects Around Center"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/rotatecenter"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select objects to rotate
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects to rotate" );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Rotation angle (in degrees)
  CRhinoGetNumber gn;
  gn.SetCommandPrompt( L"Rotation angle" );
  gn.SetDefaultNumber( m_angle );
  gn.GetNumber();
  if( gn.CommandResult() != success )
    return gn.CommandResult();

  // Validate input
  double angle = gn.Number();
  if( angle == 0 )
    return nothing;

  m_angle = angle;

  // Get the active view's construction plane
  ON_Plane plane = RhinoActiveCPlane();

  // Do not split objects that get kinky
  // when they are transformed.
  CRhinoKeepKinkySurfaces keep_kinky_srfs;

  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    // Get an object reference
    const CRhinoObjRef& ref = go.Object(i);

    // Get the real object
    const CRhinoObject* obj = ref.Object();
    if( !obj )
      continue;

    // Get the object's tight bounding box
    ON_BoundingBox bbox;
    if( !obj->GetTightBoundingBox(bbox, false, 0) )
      continue;

    // Create transformation matrix
    ON_Xform xform;
    xform.Rotation( m_angle * ON_PI / 180.0, plane.zaxis, bbox.Center() );

    // Transform the object
    context.m_doc.TransformObject( obj, xform, true, true, true );
  }

  context.m_doc.Redraw();

  return success;
}
```
