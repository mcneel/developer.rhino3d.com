+++
aliases = ["/en/5/guides/cpp/type-casting-rhino-objects/", "/en/6/guides/cpp/type-casting-rhino-objects/", "/en/7/guides/cpp/type-casting-rhino-objects/", "/en/wip/guides/cpp/type-casting-rhino-objects/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses type casting Rhino C/C++ SDK objects."
keywords = [ "rhino", "casting" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Type Casting Rhino Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/casting"
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

Given a Rhino object, how can one convert it to another Rhino object?  For example, if you have a `CRhinoObject` pointer, how can I convert it to a `CRhinoCurveObject` pointer?  Or, how can one get the curve geometry?

## Solution

All Rhino C/C++ SDK classes derived from `ON_Object` provide conversions between pointers to related classes using a static `ON_Object::Cast` function.

If you have a pointer to some base class that inherits from `ON_Object`, and you want to convert it to a pointer of a derived class, than simply call the derived class `Cast` function.

For example:

```cpp
const CBase* a = ...;
const CDerived* b = CDerived::Cast( a );
```

## Samples

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select something" );
go.GetObjects( 1, 1 );
if( CRhinoCommand::success == go.CommandResult() )
{
  // Get the one (and only) object reference
  CRhinoObjRef obj_ref = go.Object(0);

  // Get the Rhino object
  const CRhinoObject* obj = obj_ref.Object();
  if( obj )
  {
    // Try casting as a Rhino point object
    const CRhinoPointObject* point_obj = CRhinoPointObject::Cast( obj );
    if( point_obj )
    {
      // Get the point object's point geometry
      const ON_Point& point = point_obj->Point();
      // todo...
    }

    // Try casting as a Rhino curve object
    const CRhinoCurveObject* curve_obj = CRhinoCurveObject::Cast( obj );
    if( curve_obj )
    {
      // Get the curve object's curve geometry
      const ON_Curve* curve = curve_obj->Curve();
      // todo...
    }

    // Try casting as a Rhino brep object
    const CRhinoBrepObject* brep_obj = CRhinoBrepObject::Cast( obj );
    if( brep_obj )
    {
      // Get the brep object's brep geometry
      const ON_Brep* brep = brep_obj->Brep();
      // todo...
    }

    // Try casting as a Rhino mesh object
    const CRhinoMeshObject* mesh_obj = CRhinoMeshObject::Cast( obj );
    if( mesh_obj )
    {
      // Get the mesh object's mesh geometry
      const ON_Mesh* mesh = mesh_obj->Mesh();
      // todo...
    }

    // etc...
  }
}
```

and...

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select something" );
go.GetObjects( 1, 1 );
if( CRhinoCommand::success == go.CommandResult() )
{
  // Get the one (and only) object reference
  CRhinoObjRef obj_ref = go.Object(0);

  // Get the Rhino object's geometry
  const ON_Geometry* geo = obj_ref.Geometry();
  if( geo )
  {
    // Try casting as a point object
    const ON_Point* point = ON_Point::Cast( geo );
    if( point )
    {
      // todo...
    }

    // Try casting as a curve object
    const ON_Curve* curve = ON_Curve::Cast( geo );
    if( curve )
    {
      // todo...
    }

    // Try casting as a brep object
    const ON_Brep* brep = ON_Brep::Cast( geo );
    if( brep )
    {
      // todo...
    }

    // Try casting as a mesh object
    const ON_Mesh* mesh = ON_Mesh::Cast( geo );
    if( mesh )
    {
      // todo...
    }

    // etc...
  }
}
```
