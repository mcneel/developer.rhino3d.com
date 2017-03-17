---
title: Adjusting Isocurve Density
description: This brief guide demonstrates how to modify the isocurve density of a surface.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/isocurvedensity
order: 1
keywords: ['rhino', 'isocurve']
layout: toc-guide-page
---

 
## Problem

When creating a new surface from a selected curve, it is always a single isocurve crossing the surface.  One has  to adjust isocurve density after the fact from Rhino's Properties window.   It is possible to do this automatically from a plugin?

## Solution

The isocurve density for surface object is stored on the object's attributes.  For C/C++ plugins, this would be the `CRhinoObjectAttributes` and `ON_3dmObjectAttributes` classes.  Just set the `m_wire_density` property.  Note: setting this property to zero (0) will disable the display of isocurves for that object.

## Example

```cpp
CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetGeometryFilter( CRhinoGetObject::surface_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() == CRhinoCommand::success )
  {
    const CRhinoObjRef& objref = go.Object(0);
    const CRhinoBrepObject* brep_obj = CRhinoBrepObject::Cast( objref.Object() );
    if( brep_obj )
    {
      CRhinoObjectAttributes atts = brep_obj->Attributes();
      atts.m_wire_density = 3; // for example
      context.m_doc.ModifyObjectAttributes( objref, atts );
      context.m_doc.Redraw();
    }
  }

  return go.CommandResult();
}
```
