---
title: Reading Render Meshes
description: This brief guide describes how to read render meshes using the openNURBS toolkit.
author: ['Dale Lear', '@dalelear']
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onrendermesh
order: 1
keywords: ['openNURBS', 'reading', 'render', 'mesh']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

If you are developing software to read .3dm files, you might find that the software only *seems* to read NURBS data; but render meshes are ignored.  We do provide methods for third-party developers to read render meshes from .3dm files.

An object's render meshes are stored on that object. For example, the render meshes for an `ON_Brep` object are stored on that brep. The developer can obtain an object's render meshes from a brep by calling `ON_Brep:GetMesh`.

It should be noted that if the call to `ON_Brep:GetMesh` does not return any meshes, then the object did not have any render meshes.

If you are referencing the `Example_read` sample included with the openNURBS toolkit, then after the 3DM file has been read, you can obtain the render meshes from the `ONX_Model` object as follows:

```cpp
ONX_Model model = .....

int i;
for( i = 0; i < m_object_table.Count(); i++ )
{
 ONX_Model_Object model_object = m_object_table[i];
 ON_Brep* brep = ON_Brep::Cast( model_object->m_object );
 if( brep )
 {
   ON_SimpleArray<const ON_Mesh*> meshes;
   int mesh_count = brep->GetMesh( ON::render_mesh, meshes );
   if( mesh_count )
   {
      // TODO: do something with the array of meshes..
   }
 }
}
```
