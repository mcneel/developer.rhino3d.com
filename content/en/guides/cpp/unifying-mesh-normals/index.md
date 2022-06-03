+++
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to unify the normal direction of mesh faces using C/C++."
keywords = [ "rhino", "mesh", "normals" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Unifying Mesh Normals"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/unifymeshnormals"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

You have found that `RhinoUnifyMeshNormals` C/C++ functions seems to behave differently than the *UnifyMeshNormals* command.  How can one achieve the same functionality in a plugin?

## Solution

In addition to calling the `RhinoUnifyMeshNormals` function, the *UnifyMeshNormals* command also recomputes the mesh's vertex normals, based on the new face normals, using `ON_Mesh::ComputeVertexNormals`.

## Sample

The following sample demonstrates this.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select mesh to unify normals" );
  go.SetGeometryFilter( CRhinoGetObject::mesh_object );
  go.GetObjects( 1, 1 );
  CRhinoCommand::result rc = go.CommandResult();
  if( rc != CRhinoCommand::success )
    return rc;

  const CRhinoObjRef ref = go.Object(0);
  const ON_Mesh* mesh = ref.Mesh();
  if( 0 == mesh )
    return CRhinoCommand::failure;

  int count = 0;
  ON_Mesh* new_mesh = RhinoUnifyMeshNormals( *mesh, 0, false, &count );
  if( new_mesh && new_mesh->IsValid() )
  {
    new_mesh->ComputeVertexNormals();

    CRhinoMeshObject* new_obj = new CRhinoMeshObject();
    new_obj->SetMesh( new_mesh );

    context.m_doc.ReplaceObject( ref, new_obj );
    context.m_doc.Redraw();

    RhinoApp().Print( L"Reversed the orientation of %d faces.\n", count );
    rc = CRhinoCommand::success;
  }
  else
  {
    if( 0 != count )
    {
      RhinoApp().Print( L"Unable to unify mesh normals.\n" );
      rc = CRhinoCommand::failure;
    }
    else
    {
      RhinoApp().Print( L"All face normals are already oriented in the same direction.\n" );
      rc = CRhinoCommand::nothing;
    }
  }

  return rc;
}
```
