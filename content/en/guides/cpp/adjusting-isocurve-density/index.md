+++
aliases = ["/en/5/guides/cpp/adjusting-isocurve-density/", "/en/6/guides/cpp/adjusting-isocurve-density/", "/en/7/guides/cpp/adjusting-isocurve-density/", "/wip/guides/cpp/adjusting-isocurve-density/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to modify the isocurve density of a surface."
keywords = [ "rhino", "isocurve" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Adjusting Isocurve Density"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/isocurvedensity"
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
