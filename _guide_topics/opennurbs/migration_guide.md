---
title: openNURBS 5.0 Migration Guide
description: unset
author: dalelear@mcneel.com
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Cross-Platform']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/on5migrate
order: 2
keywords: [openNURBS', 'migrating', 'versions']
layout: toc-guide-page
---

# openNURBS 5.0 Migration Guide

This guide contains information to help you migrate your application to openNURBS 5.0.

## Overview

The openNURBS 5.0 toolkit builds upon openNURBS 4.0 by adding the ability to read and write Rhino version 5 3DM files.

For most developers, migrating to openNURBS 5.0 will be a simple as recompiling their application against the new toolkit.

## New Features

### Lightweight Extrusions

Lightweight Extrusion objects allow creation of simple extruded shapes using a much more lightweight representation than Brep (polysurface) objects. Lightweight Extrusions are represented by the `ON_Extrusion` class and have the object type of `ON::extrusion_object`.

When reading 3DM files, in most cases, you will want to convert the Lightweight Extrusion object to a Brep, and then just pass the Brep to the Brep handling code that you've already written:

```cpp
ONX_model model = ...
...
for( int i = 0; i < model.m_object_table.Count(); i++ )
{
  const ONX_Model_Object& model_object = model.m_object_table[i];
  if( 0 == model_object.m_object )
    continue;

  if( ON::extrusion_object != model_object.m_object->ObjectType() )
    continue;

  const ON_Extrusion* extrusion = ON_Extrusion::Cast( model_object.m_object );
  if( 0 == extrusion )
    continue;

  ON_Brep* brep = ON_Brep::New();
  if( 0 == brep )
    continue;

  if( brep != extrusion->BrepForm(brep, true) )
  {
    delete brep; // don't leak...
    continue;
  }

  // TODO: do something with brep here...

  delete brep; // don't leak...
}
```

## Changed Features

### Text

- Justification support for text added.
- Text fields added:
    - Use `TextValue()` instead of `UserText()`
    - Use `SetTextValue()` instead of `SetUserText()`
- `TextFormula()`
- `SetTextFormula()`
- Layout scaling added. Scale per detail/paperspace.
    - `AnnotativeScaling()`
    - `SetAnnotativeScaling()`
    - `ON_Annotation2::m_annotative_scale`
- Text Mask support added for text and dimensions
    - `DrawTextMask()`
    - `SetDrawTextMask()`
    - `MaskColorSource()`
    - `SetMaskColorSource()`
    - `MaskColor()`
    - `SetMaskColor()`
    - `MaskOffsetFactor()`
    - `SetMaskOffsetFactor()`

### Annotation Scaling

- Per dimstyle for dimensions and global for text now
- Document global settings for what scaling is done
- New Rhino SDK class - `CRhinoAnnotationSettingsEx:`
    - Use `CRhinoDocProperties::GetON_3dmAnnotationSettings()` to access

### Dimension Styles

- Additions for worksessions and linked blocks.
- Added the concept of child dimstyles so that fields can be overridden:
    - `IsFieldOverride()`
    - `SetFieldOverride()`
    - `HasOverrides()`
    - `OverrideFields()`
    - `InheritFields()`
    - `IsChildDimstyle()`
    - `IsChildOf()`
    - `ParentId()`
    - `SetParentId()`
- New support for Tolerances, Text Masks and Scaling per dimstyle.

---

## Related topics

- [openNURBS initiative site](http://www.rhino3d.com/opennurbs)
