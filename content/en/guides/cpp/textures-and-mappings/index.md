+++
authors = [ "dale" ]
categories = [ "RDK" ]
description = "This guide discusses materials, textures, and texture mapping using C/C++."
keywords = [ "rhino", "textures", "materials", "mapping" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Textures and Mappings"
type = "guides"
weight = 3
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs review and more explanatory content."
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

Broadly speaking, there are five concepts that are important to understand when dealing with materials, textures, and mappings:

- **Texture Bitmap**: A bitmap image, usually saved in a file.
- **Texture Coordinates**: In Rhino these are 2d and 3d points that are saved in an `ON_Mesh` in the `m_T[]` or `m_TC[]` arrays.
- **Texture Mapping**: A function that sets texture coordinates.  Persistent texture mappings are stored in `CRhinoDoc::m_texture_mapping_table[]`.
- **Render Material**: A collection of rendering color and shading information, including the names of texture bitmaps.  Rendering materials are stored in `CRhinoDoc::m_material_table[]`.
- **Object Attributes**: Attributes of a Rhino object, including the rendering materials and texture mappings the object uses, are stored in the `CRhinoObjectAttributes` class returned by `CRhinoObject::Attributes()`.

## Sample

The following sample creates a material with a bitmap texture, then modifies a mesh object's attributes and texture coordinates so the bitmap is projected onto the mesh along the world Z axis...

```cpp
// Create a material with a texture bitmap
ON_Texture tex;
tex.m_filename = L"full path to your texture.jpg/bmp/...";
tex.m_bOn = true;
tex.m_type = ON_Texture::bitmap_texture;
tex.m_mode = ON_Texture::modulate_texture;

ON_Material mat;
mat.m_diffuse.SetRGB(150,0,0);
mat.m_specular.SetRGB(200,200,200);
mat.m_shine = 0.5*ON_Material::GetMaxShine()
mat.AddTexture(tex);

int mat_index = context.m_doc.m_material_table.AddMaterial(mat);
if ( mat_index < 0 )
  return CRhinoCommand::failure;  

// Select a mesh to modify
CRhinoGetObject go;
go.SetGeometryFilter(ON::mesh_object);
go.SetCommandPrompt(L"Select a mesh");
go.GetObjects(1,1);
if ( CRhinoCommand::success != go.CommandResult() )
  return go.CommandResult();
const CRhinoMeshObject* mesh0_object =
   CRhinoMeshObject::Cast(go.Object(0).Object());
if ( 0 == mesh0_object )
  return CRhinoCommand::failure;
const ON_Mesh* mesh0 = mesh0_object->Mesh();
if ( 0 == mesh0 )
  return CRhinoCommand::failure;

// Copy the mesh and set its texture coordinates
ON_Mesh* mesh1 = new OnMesh(mesh0);
ON_BoundingBox bbox = mesh1->BoundingBox();
ON_Interval x_extents(bbox.m_min.x,bbox.m_max.x);
ON_Interval y_extents(bbox.m_min.y,bbox.m_max.y);

const int vertex_count = mesh1->m_V.Count();
mesh1->m_T.Reserve(vertex_count);
mesh1->m_T.SetCount(0);
for ( int vi = 0; vi < vertex_count; vi++ )
{
  const ON_3dPoint& V = mesh->m_V[vi];
  ON_2fPoint& tc = mesh1->m_T.AppendNew();
  tc.x = (float)x_extents.NormalizedParameterAt(V.x);
  tc.y = (float)y_extents.NormalizedParameterAt(V.y);
}

// Update the mesh
CRhinoMeshObject* mesh1_object = new CRhinoMeshObject();
mesh1_object.SetMesh(mesh1);
context.m_doc.ReplaceObject(CRhinoObjRef(mesh0_object),mesh1_object);
ON_3dmObjectAttributes att = mesh1_object->Attributes();
att.m_material_index;
att.SetMaterialSource( ON::material_from_object );
context.m_doc.Redraw();
```
