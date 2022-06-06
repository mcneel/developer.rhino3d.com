+++
aliases = ["/5/guides/cpp/modifying-an-objects-color/", "/6/guides/cpp/modifying-an-objects-color/", "/7/guides/cpp/modifying-an-objects-color/", "/wip/guides/cpp/modifying-an-objects-color/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide discuss how to modify an object's color using C/C++."
keywords = [ "rhino", "color" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Modify an Object's Color"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/modifyobjectcolor"
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

The color used to display an object is specified in one of four ways...

1. `ON::color_from_layer` - the object's layer color, `ON_Layer::Color()`, determines the object's color.  This is the default method used when adding new objects to Rhino
1. `ON::color_from_object` - the value of an object's `m_color` attribute determines the object's color.
1. `ON::color_from_material` - the diffuse color of the object's render material determines the object's color.
1. `ON::color_from_parent` - if the object is part of an instance reference, the color is taken from the instance

## Sample

The following code sample demonstrates how to override the default "color by layer" behavior and set an object to use "color by object."

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select object" );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& obj_ref = go.Object( 0 );
  const CRhinoObject* obj = obj_ref.Object();
  if( !obj )
    return CRhinoCommand::failure;

  ON_Color old_color = obj->Attributes().DrawColor();
  ON::object_color_source color_source = obj->Attributes().ColorSource();
  ON_Color new_color( old_color );

  if( !RhinoColorDialog( ::RhinoApp().MainWnd(), new_color) )
    return CRhinoCommand::cancel;

  if( new_color == old_color )
    return CRhinoCommand::nothing;

  CRhinoObjectAttributes att( obj->Attributes() );
  att.m_color = new_color;
  att.SetColorSource( ON::color_from_object );
  context.m_doc.ModifyObjectAttributes( obj_ref, att );
  context.m_doc.Redraw();
  return CRhinoCommand::success;
}
```

When adding new objects using the C/C++ SDK, you can specify the attributes of the object when adding it to Rhino.  Thus, if you want to override the default color behavior for new objects, just get a copy of the active document's default new object attributes, modify it in whatever way you want, and pass it (along with the geometry) to the appropriate object creation function...

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  ON_Circle circle;
  circle.Create( RhinoActiveCPlane(), 5.0 );
  ON_3dmObjectAttributes att;
  context.m_doc.GetDefaultObjectAttributes( att );

  att.m_color = RGB(255,191,191);
  att.SetColorSource( ON::color_from_object );
  context.m_doc.AddCurveObject( circle, &att );
  context.m_doc.Redraw();
  return CRhinoCommand::success;
}
```
