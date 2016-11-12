---
title: Custom Picking Grip Objects
description: This guide discusses how to write a custom grip object picker in C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/customgripselection
order: 1
keywords: ['rhino', 'custom', 'grip']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Problem

Imagine you are trying to wrote code to pick grip objects, and you want that only grips at the boundary of a mesh to be selectable.  You might have just spent a considerable amount of time trying to get the following to work:

1. Derive a class from `CRhinoGetObject`.
1. Override `CRhinoGetObject::CustomGeometryFilter`.

What is missing is a pointer to a grip object inside `CRhinoGetObject::CustomGeometryFilter`.  One might think this code would work...

```cpp
CMyGetObject go;
go.SetGeometryFilter( CRhinoGetObject::grip_object );
```

but now `CRhinoGetObject::CustomGeometryFilter` override is not even called anymore.  On the other hand, if you do not specify a `CRhinoGetObject::SetGeometryFilter` up front, the function is called but you don't get any grip object from the geometry parameter of `CRhinoGetObject::CustomGeometryFilter`.

Is there a way around this problem?

## Solution

Yes.  In order to pick grip objects, using `CRhinoGetObject`, you must set the `CRhinoGetObject::grip_object` geometry filter.  If not, then Rhino will ignore grips in an effort to improve picking performance.

Also, if you want your `CRhinoGetObject::CustomGeometryFilter` override to be called, make sure to call `CRhinoGetObject::EnableSubObjectSelect` to disable subobject picking.  For example:

```cpp
CMyGetObject go;
go.SetGeometryFilter( CRhinoObject::grip_object );
go.EnableSubObjectSelect( false );
go.GetObjects( 1, 0 );
if( go.CommandResult() == CRhinoCommand::success )
{
  // TODO...
}
```

Regarding the picking of grips at the boundary of a mesh, here is a sample class that you can use...

```cpp
class CRhGetMeshBoundaryGrip : public CRhinoGetObject
{
public:
  bool CustomGeometryFilter(
    const CRhinoObject* obj,
    const ON_Geometry* geo,
    ON_COMPONENT_INDEX ci
    ) const;
};

bool CRhGetMeshBoundaryGrip::CustomGeometryFilter(
  const CRhinoObject* obj,
  const ON_Geometry* geo,
  ON_COMPONENT_INDEX ci
  ) const
{
  if( 0 == obj )
    return false;

  // Is grip object?
  const CRhinoGripObject* grip_obj = CRhinoGripObject::Cast( obj );
  if( 0 == grip_obj )
    return false;

  // Is mesh grip object?
  const CRhinoMeshObject* mesh_obj = CRhinoMeshObject::Cast( grip_obj->Owner() );
  if( 0 == mesh_obj )
    return false;

  // Is the grip on the border?
  const ON_Mesh* mesh = mesh_obj->Mesh();
  if( mesh && !mesh->IsClosed() )
  {
    const ON_MeshTopology& meshtop = mesh->Topology();
    int topvi = meshtop.m_topv_map[grip_obj->m_grip_index];
    const ON_MeshTopologyVertex& topv = meshtop.m_topv[topvi];
    for( int i = 0; i < topv.m_tope_count; i++ )
    {
      const ON_MeshTopologyEdge& tope = meshtop.m_tope[topv.m_topei[i]];
      if( 1 == tope.m_topf_count )
        return true;
    }
  }

  return false;
}
```
