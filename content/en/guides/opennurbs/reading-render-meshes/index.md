+++
authors = [ "dalelear" ]
categories = [ "Fundamentals" ]
description = "This brief guide describes how to read render meshes using the openNURBS toolkit."
keywords = [ "openNURBS", "reading", "render", "mesh" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Reading Render Meshes"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onrendermesh"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
If you are developing software to read .3dm files, you might find that the software only *seems* to read NURBS data; but render meshes are ignored.  We do provide methods for third-party developers to read render meshes from .3dm files.

An object's render meshes are stored on that object. For example, the render meshes for `ON_Brep` and `ON_Extrusion` objects are stored on that object. The developer can obtain an object's render meshes from a Brep by calling `ON_Brep::GetMesh` and from an Extrusion by calling `ON_MeshCache::Mesh`.

If you are referencing the `Example_read` sample included with the openNURBS toolkit, then after the 3DM file has been read, you can obtain the render meshes from the `ONX_Model` object as follows:

```cpp
ONX_Model model = ...

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    // Test for mesh object
    const ON_Mesh* mesh = ON_Mesh::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != mesh)
    {
      // TODO: do something with ON_Mesh object...
      continue;
    }

    // Test for Brep object
    const ON_Brep* brep = ON_Brep::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != brep)
    {
      ON_SimpleArray<const ON_Mesh*> meshes(brep->m_F.Count());
      const int mesh_count = brep->GetMesh(ON::render_mesh, meshes);
      if (mesh_count > 0)
      {
        // TODO: do something with array of ON_Mesh objects...
      }
      continue;
    }

    // Test for extrusion object
    const ON_Extrusion* extrusion = ON_Extrusion::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != extrusion)
    {
      const ON_Mesh* mesh = extrusion->m_mesh_cache.Mesh(ON::render_mesh);
      if (nullptr != mesh)
      {
        // TODO: do something with ON_Mesh object...
      }
      continue;
    }
  }
}
```
