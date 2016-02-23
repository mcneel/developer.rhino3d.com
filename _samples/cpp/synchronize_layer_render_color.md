---
title: Synchronize Layer Render Color
description: Demonstrates how to synchronize the basic material color of a layer with the layer's color.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Layers']
origin: http://wiki.mcneel.com/developer/sdksamples/synclayermaterialcolor
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
  CRhinoMaterialTable& material_table = context.m_doc.m_material_table;
  int num_modified = 0;

  int i, layer_count = layer_table.LayerCount();
  for( i = 0; i < layer_count; i++ )
  {
    const CRhinoLayer& layer = layer_table[i];
    if( layer.IsDeleted() | layer.IsReference() )
      continue;

    int material_index = layer.RenderMaterialIndex();
    if( material_index < 0 )
    {
      // If material_index < 0, then the layer does not have a
      // material assigned to it. So, we will create a new material
      // that is based on Rhino's default material, and add it
      // to the material table.

      ON_Material material( RhinoApp().AppSettings().DefaultMaterial() );
      material_index = material_table.AddMaterial( material );
      if( material_index >= 0 )
      {
        // Now that we have added the new material,
        // assign it to the layer.
        ON_Layer new_layer( layer );
        new_layer.SetRenderMaterialIndex( material_index );
        layer_table.ModifyLayer( new_layer, layer.LayerIndex() );
      }
    }

    if( material_index < 0 )
      continue;

    const CRhinoMaterial& material = material_table[material_index];
    if( layer.Color() == material.Diffuse() )
      continue;

    // Modify the material's basic, or diffuse, color
    ON_Material new_material( material );
    new_material.SetDiffuse( layer.Color() );
    material_table.ModifyMaterial( new_material, material.MaterialIndex(), FALSE );

    num_modified++;
  }

  if( num_modified > 0 )
    context.m_doc.Regen();
  return CRhinoCommand::success;
}
```
