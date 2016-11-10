---
title: Project Curves onto Breps
description: This guide demonstrates how to project a curve onto a brep using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/projectcurvestobrep
order: 1
keywords: ['rhino', 'project', 'curve', 'brep']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You want to project curves onto a brep, but you do not function any C/C++ function to do this.  Is there a solution for this?

## Solution

It is true that the Rhino C/C++ SDK does not currently have a function that will project a curve onto a brep. But, using some of the existing functions, you can write your own function without too much effort.

To project a curve onto a brep, you need to do the following:

1. Extrude the curve through the brep using the `RhinoExtrudeCurveStraight()` function.
1. Intersect the two breps using `RhinoIntersectBreps()` function.
1. The results of the brep intersection will be the projected curves.

## Sample

The following sample code demonstrates how one might write such a function...

```cpp
/*
Description:
  Projects a curve onto a surface or polysurface
Parameters:
  brep  - [in] The brep to project the curve onto.
  curve - [in] The curve to project.
  dir   - [in] The direction of the projection.
  tol   - [in] The intersection tolerance.
  output_curves - [out] The output curves.
                        NOTE, the caller is responsible
                        for destroying these curves.
Returns:
  true if successful.
  false if unsuccessful.
*/
bool ProjectCurveToBrep(
        const ON_Brep& brep,
        const ON_Curve& curve,
        const ON_3dVector& dir,
        double tolerance,
        ON_SimpleArray<ON_Curve*>& output_curves
        )
{
  ON_3dVector n = dir;
  if( !n.Unitize() )
    return false;

  ON_BoundingBox bbox = brep.BoundingBox();
  bbox.Union( curve.BoundingBox() );

  ON_Surface* pExtrusion = RhinoExtrudeCurveStraight( &curve, dir, bbox.Diagonal().Length() );
  if( 0 == pExtrusion )
    return false;

  ON_Brep* pBrep = ON_Brep::New();
  pBrep->Create( pExtrusion );

  BOOL rc = RhinoIntersectBreps( *pBrep, brep, tolerance, output_curves );
  delete pBrep; // Don't leak...

  return ( rc ) ? true : false;
}
```
