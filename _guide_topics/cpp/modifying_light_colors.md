---
title: Modifying a Light's Color
description: This brief guide describes how to modify the diffuse color of an existing light using C/C++.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/modifylightcolor
order: 1
keywords: ['rhino', 'light', 'color']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The process for modifying a light object is slightly different than the process for modifying other geometric objects, such as points, curves, and surfaces.  This is because light objects are stored in a different location in the Rhino document.

## How To

Light objects are stored in a `CRhinoLightTable` object that is held by the active document object.  Thus, instead of using one of the `ModifyObject()` members found on `CRhinoDoc`, you need to use the `ModifyLight()` member found on `CRhinoLightTable` in order to modify an existing light object.

For more details on `CRhinoLight` and `CRhinoLightTable`, see *rhinoSdkLight.h* included with the C/C++ SDK.

## Sample

The following example demonstrates how to modify the diffuse color of a light object...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Pick an existing light object
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select light to change color" );
  go.SetGeometryFilter( CRhinoGetObject::light_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // The the light object
  CRhinoObjRef& ref = go.Object(0);
  const CRhinoLight* light_obj = CRhinoLight::Cast( ref.Object() );
  if( !light_obj )
    return CRhinoCommand::failure;

  // Prompt the user to pick a new color
  ON_Color color = light_obj->Light().Diffuse();
  if( !RhinoColorDialog(RhinoApp().MainWnd(), color) )
    CRhinoCommand::cancel;

  // Copy the light object's underlying ON_Light
  ON_Light light( light_obj->Light() );
  // Modify the diffuse color
  light.SetDiffuse( color );

  // Modify the light
  CRhinoLightTable& light_table = context.m_doc.m_light_table;
  light_table.ModifyLight( light, light_obj->LightIndex() );

  return CRhinoCommand::success;
}
```
