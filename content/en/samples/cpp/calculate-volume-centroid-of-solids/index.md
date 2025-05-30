+++
aliases = ["/en/5/samples/cpp/calculate-volume-centroid-of-solids/", "/en/6/samples/cpp/calculate-volume-centroid-of-solids/", "/en/7/samples/cpp/calculate-volume-centroid-of-solids/", "/en/wip/samples/cpp/calculate-volume-centroid-of-solids/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "http://wiki.mcneel.com/developer/sdksamples/volumecentroid"
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calculate Volume Centroid of Solids"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/volumecentroid"
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
  go.SetCommandPrompt( L"Select solids for volume centroid calculation" );
  go.SetGeometryFilter(
        CRhinoGetObject::surface_object |
        CRhinoGetObject::polysrf_object
        );
  go.SetGeometryAttributeFilter(
        CRhinoGetObject::closed_surface |
        CRhinoGetObject::closed_polysrf
        );
  go.EnableSubObjectSelect( false );
  go.EnableGroupSelect( true );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  ON_SimpleArray<const ON_Geometry*> geom( go.ObjectCount() );
  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const ON_Geometry* geo = go.Object(i).Geometry();
    if( 0 == geo )
      return failure;
    geom.Append( geo );
  }

  // Get bounding box of all objects
  ON_BoundingBox bbox;
  for( i = 0; i < geom.Count(); i++ )
    geom[i]->GetBoundingBox( bbox, bbox.IsValid() );

  ON_3dPoint base_point = bbox.Center();
  ON_SimpleArray<ON_MassProperties> MassProp;
  MassProp.Reserve( geom.Count() );

  for( i = 0; i < geom.Count(); i++ )
  {
    ON_MassProperties* mp = &MassProp.AppendNew();

    if( const ON_Surface* srf = ON_Surface::Cast(geom[i]) )
      srf->VolumeMassProperties( *mp, true, true, false, false, base_point );       

    else if( const ON_Brep* brep = ON_Brep::Cast(geom[i]) )
      brep->VolumeMassProperties( *mp, true, true, false, false, base_point );
  }

  ON_MassProperties results;
  results.Sum( MassProp.Count(), MassProp.Array() );

  ON_3dPoint pt( results.m_x0, results.m_y0, results.m_z0 );
  context.m_doc.AddPointObject( pt );
  context.m_doc.Redraw();

  RhinoApp().Print( L"Volume centroid = %g,%g,%g\n", pt.x, pt.y, pt.z );

  return success;
}
```
