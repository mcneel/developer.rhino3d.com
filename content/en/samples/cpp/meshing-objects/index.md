+++
aliases = ["/5/samples/cpp/meshing-objects/", "/6/samples/cpp/meshing-objects/", "/7/samples/cpp/meshing-objects/", "/wip/samples/cpp/meshing-objects/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to mesh surface and polysurface objects using the RhinoMeshObjects function."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Meshing Objects"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/meshobjects"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select some geometry to mesh
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surface or polysurface to mesh" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  ON_SimpleArray<const CRhinoObject*> objects;
  objects.Append( go.Object(0).Object() );

  // RhinoMeshObjects need to know how to mesh the objects. This information is provided
  // by passing the function a ON_MeshParameters object. For details on this class, see
  // opennurbs_mesh.h.

  // In this example, instead of making up our own default mesh parameters, we will just
  // get some existing ones that we know work well.
  const CRhinoAppRenderMeshSettings& rms = RhinoApp().AppSettings().RenderMeshSettings();
  //ON_MeshParameters mp = rms.QualityMeshParameters();
  ON_MeshParameters mp = rms.FastMeshParameters();

  // Set the user interface style.
  int ui_style = 0; // simple ui

  ON_ClassArray<CRhinoObjectMesh> meshes;

  // Mesh the selected objects.
  CRhinoCommand::result rc = RhinoMeshObjects( objects, mp, ui_style, meshes );
  if( rc == success )
  {
    int i;
    for( i = 0; i < meshes.Count(); i++ )
    {
      CRhinoObjectMesh& mesh = meshes[i];
      CRhinoMeshObject* mesh_object = new CRhinoMeshObject( mesh.m_mesh_attributes );
      mesh_object->SetMesh( mesh.m_mesh );
      mesh.m_mesh = 0;
      context.m_doc.AddObject( mesh_object );
    }

    context.m_doc.Redraw();
  }

  return rc;
}
```
