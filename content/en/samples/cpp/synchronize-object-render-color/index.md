+++
aliases = ["/5/samples/cpp/synchronize-object-render-color/", "/6/samples/cpp/synchronize-object-render-color/", "/7/samples/cpp/synchronize-object-render-color/", "/wip/samples/cpp/synchronize-object-render-color/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to synchronize the basic material color of an object with the object's display color."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Synchronize Object Render Color"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/syncobjectmaterialcolor"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  int num_modified = 0;
  CRhinoObjectIterator it( CRhinoObjectIterator::normal_objects,
                           CRhinoObjectIterator::active_objects );
  it.IncludeLights( FALSE );

  CRhinoObject* obj = 0;
  for( obj = it.First(); obj; obj = it.Next() )
  {
    // If the object gets its color from its layer, then we will
    // let the layer handle its material color as well.
    ON::object-color_source color_source = obj->Attributes().ColorSource();
    if( color_source != ON::color_from_object )
      continue;

    int material_index = obj->Attributes().m_material_index;
    if( material_index < 0 )
    {
      // If material_index < 0, then the object does not have a
      // material assigned to it. So, we will create a new material
      // that is based on Rhino's default material, and add it
      // to the material table.
      ON_Material material( RhinoApp().AppSettings().DefaultMaterial() );
      material_index = context.m_doc.m_material_table.AddMaterial( material );
      if( material_index >= 0 )
      {
        // Now that we have added the new material,
        // assign it to the object.
        CRhinoObjectAttributes new_attributes( obj->Attributes() );
        new_attributes.m_material_index = material_index;
        // Make sure to set the material source to "from object"
        new_attributes.SetMaterialSource( ON::material_from_object );
        obj->ModifyAttributes( new_attributes );
      }
    }
    if( material_index < 0 )
      continue;

    const CRhinoMaterial& material = context.m_doc.m_material_table[material_index];
    if( obj->Attributes().DrawColor() == material.Diffuse() )
      continue;

    // Modify the material's basic,or diffuse, color
    ON_Material new_material( material );
    new_material.SetDiffuse( obj->Attributes().DrawColor() );
    context.m_doc.m_material_table.ModifyMaterial( new_material,
                                                   material.MaterialIndex(),
                                                   FALSE );
    num_modified++;
  }

  if( num_modified > 0 )
    context.m_doc.Regen();

  return CRhinoCommand::success;
}
```
