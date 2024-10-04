+++
aliases = ["/en/5/guides/cpp/textures-and-mappings/", "/en/6/guides/cpp/textures-and-mappings/", "/en/7/guides/cpp/textures-and-mappings/", "/wip/guides/cpp/textures-and-mappings/"]
authors = [ "dale", "jussi" ]
categories = [ "RDK" ]
description = "This guide discusses materials, textures, and texture mapping using C/C++."
keywords = [ "rhino", "textures", "materials", "mapping" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Textures and Mappings"
type = "guides"
weight = 3

[admin]
TODO = "Overview's Texture Coordinates section does not use names used in sample"
origin = "http://wiki.mcneel.com/developer/sdksamples/texturesandmappings"
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

 
## Overview

Broadly speaking, there are six concepts that are important to understand when dealing with materials, textures, and mappings:

- **Texture Bitmap**: A bitmap image, usually saved in a file.
- **Texture Coordinates**: In Rhino these are 2d and 3d points that are saved in an `ON_Mesh` in the `m_T[]` or `m_TC[]` arrays. They should always be set by a texture mapping and never modified directly.
- **Texture Mapping**: A function that sets texture coordinates.  Persistent texture mappings are stored in `CRhinoDoc::m_texture_mapping_table[]`.
- **Surface parameters**: A set of 2d points stored in an `ON_Mesh` in the `m_S[]` array. They are used by the surface parameter mapping.
- **Render Material**: A collection of rendering color and shading information, including the names of texture bitmaps.  Rendering materials are stored in `CRhinoDoc::m_material_table[]`.
- **Object Attributes**: Attributes of a Rhino object, including the rendering materials and texture mappings the object uses, are stored in the `CRhinoObjectAttributes` class returned by `CRhinoObject::Attributes()`.

## Sample

The following sample creates a material with a bitmap texture, then modifies a mesh object's attributes, sets up surface parameters and applies a surface parameter mapping so the bitmap is projected onto the mesh along the world Z axis...

```cpp
  CRhinoDoc* pDoc = context.Document();
  if (nullptr == pDoc)
    return CRhinoCommand::failure;
  CRhinoDoc& doc = *pDoc;

  // Id of the currently active render plug-in
  const UUID renderPlugInId = RhinoApp().CurrentRenderPlugIn()->PlugInID();

  // Create a material with a texture bitmap
  ON_Texture tex;
  tex.m_image_file_reference.SetFullPath(L"C:/my-texture-folder/sample-texture.bmp", true);
  tex.m_bOn = true;
  tex.m_type = ON_Texture::TYPE::bitmap_texture;
  tex.m_mode = ON_Texture::MODE::modulate_texture;
  tex.m_mapping_channel_id = 1;

  ON_Material mat;
  mat.m_diffuse.SetRGB(150, 0, 0);
  mat.m_specular.SetRGB(200, 200, 200);
  mat.m_shine = 0.5 * ON_Material::MaxShine;
  mat.AddTexture(tex);

  int mat_index = doc.m_material_table.AddMaterial(mat);
  if (mat_index < 0)
    return CRhinoCommand::failure;

  // Select a mesh to modify
  CRhinoGetObject go;
  go.SetGeometryFilter(ON::mesh_object);
  go.SetCommandPrompt(L"Select a mesh");
  go.GetObjects(1, 1);
  if (CRhinoCommand::success != go.CommandResult())
    return go.CommandResult();
  const CRhinoMeshObject* mesh0_object =
    CRhinoMeshObject::Cast(go.Object(0).Object());
  if (0 == mesh0_object)
    return CRhinoCommand::failure;
  const ON_Mesh* mesh0 = mesh0_object->Mesh();
  if (0 == mesh0)
    return CRhinoCommand::failure;

  // Copy the mesh
  ON_Mesh* mesh1 = new ON_Mesh(*mesh0);
  ON_BoundingBox bbox = mesh1->BoundingBox();
  ON_Interval x_extents(bbox.m_min.x, bbox.m_max.x);
  ON_Interval y_extents(bbox.m_min.y, bbox.m_max.y);

  // Set up surface parameters.
  // They will be used by a surface parameter mapping.
  const int vertex_count = mesh1->m_V.Count();
  mesh1->m_S.Reserve(vertex_count);
  mesh1->m_S.SetCount(0);
  for (int vi = 0; vi < vertex_count; vi++)
  {
    const ON_3dPoint& V = mesh0->m_V[vi];
    ON_2dPoint& tc = mesh1->m_S.AppendNew();
    tc.x = (float)x_extents.NormalizedParameterAt(V.x);
    tc.y = (float)y_extents.NormalizedParameterAt(V.y);
  }

  // Adjust surface packing settings so that surface parameter
  // mapping will create vertex coordinates 1-to-1 with the
  // surface parameters.
  mesh1->m_srf_domain[0].Set(0.0, 1.0);
  mesh1->m_srf_domain[1].Set(0.0, 1.0);
  mesh1->m_srf_scale[0] = 0.0;
  mesh1->m_srf_scale[1] = 0.0;
  mesh1->m_packed_tex_domain[0].Set(0.0, 1.0);
  mesh1->m_packed_tex_domain[1].Set(0.0, 1.0);
  mesh1->m_packed_tex_rotate = false;

  // Update the mesh
  CRhinoMeshObject* mesh1_object = new CRhinoMeshObject();
  mesh1_object->SetMesh(mesh1);
  doc.ReplaceObject(CRhinoObjRef(mesh0_object), mesh1_object);

  // Make a copy of the object attributes in order to apply some changes
  ON_3dmObjectAttributes att = mesh1_object->Attributes();

  // Update the object to use the new material
  att.m_material_index = mat_index;
  att.SetMaterialSource(ON::material_from_object);

  // Add new texture mapping to the document texture mapping table
  const int textureMappingIndex = doc.m_texture_mapping_table.AddTextureMapping(ON_TextureMapping::SurfaceParameterTextureMapping);
  // Look up the mapping id of the newly added texture mapping
  const UUID textureMappingId = doc.m_texture_mapping_table[textureMappingIndex].Id();
  // Remove all texture mappings from the object attributes
  att.m_rendering_attributes.m_mappings.Destroy();
  // Add the newly added texture mapping on the mapping channel that the texture uses
  att.m_rendering_attributes.AddMappingChannel(renderPlugInId, tex.m_mapping_channel_id, textureMappingId);

  // Apply the modified attributes to the mesh object
  doc.ModifyObjectAttributes(CRhinoObjRef(mesh1_object), att);

  doc.Redraw();
```
