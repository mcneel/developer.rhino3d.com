---
title: Reading Per-Face Render Materials
description: This brief guide describes how to read render materials from Brep faces using the openNURBS toolkit.
authors: ['dale_fugier']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['openNURBS', 'reading', 'render', 'material']
layout: toc-guide-page
---


New in Rhino 6 is per-Brep face render material assignment. This eliminates the step of extracting faces just to change the material required in prior versions.

The `ON_BrepFace:m_face_material_channel` property provides a way to have individual Brep faces use a rendering material that is different from the rendering material used by the parent Brep. 

If `ON_BrepFace:m_face_material_channel` is zero, which is the default value, then the face will use the parent Brep's rendering material.

if `ON_BrepFace:m_face_material_channel` is greater than zero, then his value can use used to obtain the face's rendering material id from the parent Brep's rendering material's channel index array. 

If you are referencing the `Example_read` sample included with the openNURBS toolkit, then after the 3DM file has been read, you can query an object's render material as follows:

```cpp
ONX_Model model = .....

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr == model_geometry)
    continue;

  const ON_Brep* brep = ON_Brep::Cast(model_geometry->Geometry(nullptr));
  const ON_3dmObjectAttributes* attributes = model_geometry->Attributes(nullptr);
  if (nullptr == brep || nullptr == attributes)
    continue;

  const ON_Material* material = ModelGeometryRenderMaterial(model, *attributes);
  if (nullptr != material)
  {
    for (int fi = 0; fi < brep->m_F.Count(); fi++)
    {
      const ON_Material* face_material = nullptr;
      const ON_BrepFace& face = brep->m_F[fi];
      const int channel = face.m_face_material_channel;
      if (channel > 0 && channel < material->m_material_channel.Count())
      {
        const ON_UuidIndex& idx = material->m_material_channel[channel - 1];
        face_material = ModelGeometryRenderMaterial(model, idx.m_id);
      }

      if (nullptr == face_material)
        face_material = material;

      if (nullptr != face_material)
      {
        // Dump the diffuse color, for example.
        ON_Color color = face_material->Diffuse();
        // TODO...
      }
    }
  }
}

/*
Helper function to return an ON_Material, given an ON_ObjectAttributes.
*/
static const ON_Material* ModelGeometryRenderMaterial(
  const ONX_Model& model, 
  const ON_3dmObjectAttributes& attributes
)
{
  ON_ModelComponentReference rc = model.RenderMaterialFromAttributes(attributes);
  if (!rc.IsEmpty())
    return ON_Material::Cast(rc.ModelComponent());
  return nullptr;
}

/*
Helper function to return an ON_Material, given a material id.
*/
static const ON_Material* ModelGeometryRenderMaterial(
  const ONX_Model& model, 
  const ON_UUID& material_id
)
{
  ON_ModelComponentReference rc = model.RenderMaterialFromId(material_id);
  if (!rc.IsEmpty())
    return ON_Material::Cast(rc.ModelComponent());
  return nullptr;
}
```
