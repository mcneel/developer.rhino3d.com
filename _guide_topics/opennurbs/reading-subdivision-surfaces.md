---
title: Reading Subdivision Surfaces
description: This brief guide describes how to read subdivision surfaces using the openNURBS toolkit.
authors: ['dale_fugier']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: 
order: 1
keywords: ['openNURBS', 'reading', 'subd']
layout: toc-guide-page
---

## Overview

Rhino SubD objects are high-precision Catmull-Clark subdivision surfaces. They can have creases, sharp or smooth corners, and holes. The Rhino SubD object is designed to quickly model and edit complex organic shapes.

Unlike traditional mesh-based SubD implementations, Rhino SubD objects are NOT a subdivided mesh object.

The Rhino SubD user experience will be the same as Rhino NURBS and mesh object experience. There will also be new SubD modeling and editing tools based on traditional techniques. 

Rhino SubD surfaces are predictable, measurable, and manufacturable. They can be converted to either high-quality NURBS or mesh (quads or triangles) objects when needed.

Rhino SubD objects will be supported in all Rhino export formats that support either meshes or NURBS including IGES, STEP, OBJ, and STL.

## openNURBS and ON_SubD

Rhino SubD object are defined on openNURBS in the `ON_SubD` class. See `opennurbs_subd.h`, in the openNURBS source code, for details.

Like other Rhino objects, the `ON_SubD` class inherits from `ON_Geometry`. Thus when you are reading 3DM files, you can use `ONX_ModelComponentIterator` object to look for SubD object just like you would if you were looking for other types of geometry, such as curves, Breps, and meshes.

The following code sample demonstrates how to iterate an `ONX_Model` object and look for `ON_SubD` objects. When found, the control net mesh (or input mesh used to calculate a subdivision surface) is obtained.

```cpp
ONX_Model model = ...

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    // Test for subd object
    const ON_SubD* subd = ON_SubD::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != subd)
    {
      // Get control net mesh
      ON_Mesh* mesh = subd->GetControlNetMesh(nullptr, ON_SubDGetControlNetMeshPriority::Geometry);
      if (nullptr != mesh)
      {
        // TODO: do something with mesh
        delete mesh; // don't leak memory
      }
    }
  }
}
```

The control net is mesh generally coarse and not acceptable for use for rendering, rapid prototyping, and other. So the version of openNURBS, included with Rhino, contains two powerful functions that are useful for converting SubD objects to Breps or smooth meshes:

```
// Gets a ON_Brep representation the subdivision limit surface
ON_SubD::GetSurfaceBrep()

// Get a ON_Mesh representation of the subdivision limit surface
ON_SubD::GetSurfaceMesh()
```

These two function are used internally by Rhino when exporting to file formats that do not support SubD objects. However, these two functions **are not available** in the free, publicly available openNURBS toolkit. 

Rhino SubD objects are 100% "industry standard" and Rhino evaluation results comply 100% with public domain algorithms widely described in published technical literature. If you already have actually have code the correctly meshes and performs the "to NURBS on Catmull-Clark subdivision surfaces, then you should use it.

If you don't have this capability, then you might try subdividing the SubD object before acquiring the control net mesh.  Here is an example:

```
const ON_SubD* subd = ON_SubD::Cast(model_geometry->Geometry(nullptr));
if (nullptr != subd)
{
  ON_SubD* new_subd = subd->Duplicate();
  if (nullptr != new_subd)
  {
    // The number of subdivisions you require
    const int count = 3;
    
    // Apply the Catmull-Clark subdivision algorithm and save the results in this ON_SubD
    new_subd->GlobalSubdivide(count);
    
    // Get control net mesh
    ON_Mesh* mesh = new_subd->GetControlNetMesh(nullptr, ON_SubDGetControlNetMeshPriority::Geometry);
    if (nullptr != mesh)
    {
      // TODO: do something with mesh
      delete mesh; // don't leak memory
    }
    delete new_subd; // don't leak memory
  }
}
```


## Related Topics

[What is openNURBS?]({{ site.baseurl }}/guides/opennurbs/what-is-opennurbs)
