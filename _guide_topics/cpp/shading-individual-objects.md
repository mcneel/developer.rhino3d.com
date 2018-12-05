---
title: Shading Individual Objects
description: This guide demonstrates how to shade individual objects using C/C++.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/shadeobjects
order: 1
keywords: ['rhino', 'shading']
layout: toc-guide-page
---

 
## Overview

The drawing display pipeline technology provides both users and developers great flexibility and control over how objects are drawn on the screen.  One of the features available is the ability to have objects draw using different display modes in the same viewport.  For example, it is possible for a viewport to display both wireframe and shaded objects at the same time.

To allow an object to draw in a display mode other than what the viewport is currently set to, all you need to do is to add an `ON_DisplayMaterialRef` object to an object's attributes.  A `ON_DisplayMaterialRef` defines what viewport an object will draw using a different display attributes and what display attributes it will use.

## Sample

The following sample code demonstrates how to shade individual objects using the Rhino C/C++ SDK.  This shading is independent of the viewport's current display mode, or display attribute.  Is is accomplished by adding a `ON_DisplayMaterialRef` object to an object's attributes.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Get a list of available display attributes
  DisplayAttrsMgrList attrs_list;
  const int attrs_count = CRhinoDisplayAttrsMgr::GetDisplayAttrsList( attrs_list );
  if( attrs_count <= 0 )
    return CRhinoCommand::nothing;

  ON_wString display_name( L"Shaded" );
  ON_UUID display_material_id = ON_nil_uuid;

  // Find the "Shaded" display attribute
  int i;
  for( i = 0; i < attrs_count; i++ )
  {
    CDisplayPipelineAttributes* pAttrs = attrs_list[i].m_pAttrs;
    if( !pAttrs )
      continue;

    ON_wString english_name = pAttrs->EnglishName();
    english_name.Remove( '_' );
    english_name.Remove( ' ' );
    english_name.Remove( '-' );
    english_name.Remove( ',' );
    english_name.Remove( '.' );

    if( english_name.CompareNoCase(display_name) == 0 )
    {
      display_material_id = pAttrs->Id();
      break;
    }
  }

  // Bail if not found
  if( display_material_id == ON_nil_uuid )
  {
    RhinoApp().Print( L" \"%s\" display mode not found.\n", display_name );
    return CRhinoCommand::nothing;
  }

  // Select the objects to shade
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surfaces, polysurfaces, and meshes to shade" );
  go.SetGeometryFilter( ON::surface_object | ON::brep_object | ON::mesh_object );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Get the viewport to shade the objects in
  CRhinoView* view = RhinoApp().ActiveView();
  if( !view )
    return failure;

  // Create a display material reference and assign
  // the display attributes id and the viewport id
  // to it.
  ON_DisplayMaterialRef dmr;
  dmr.m_display_material_id = display_material_id;
  dmr.m_viewport_id = view->Viewport().VP().ViewportId();

  // Process each selected object
  const int object_count = go.ObjectCount();
  for( i = 0; i < object_count; i++ )
  {
    const CRhinoObjRef& ref = go.Object(i);
    const CRhinoObject* obj = ref.Object();
    if( !obj )
      continue;

    // Make a copy of the object's attributes
    ON_3dmObjectAttributes attributes = obj->Attributes();
    // Add a display material reference
    attributes.AddDisplayMaterialRef( dmr );
    // Modify the object's attributes
    context.m_doc.ModifyObjectAttributes( ref, attributes );
  }

  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
