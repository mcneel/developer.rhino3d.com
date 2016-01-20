---
title: Determining if a Brep is a Box
description: This brief guide discusses how to determine if a brep object is a box using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Miscellaneous']
origin: http://wiki.mcneel.com/developer/sdksamples/isbrepbox
order: 1
keywords: ['rhino', 'brep']
layout: toc-guide-page
---

# Determining if a Brep is a Box

{{ page.description }}

## Problem

You would like to determine whether or not a polysurface is a (brep) box.

## Solution

For a polysurface to be a box, the following conditions must be true:

1. The brep must be solid.
1. The brep must have six faces.
1. Each of the six faces must be planar.
1. Each of the planar face must be either perpendicular or antiparallel to the other planar faces.

## Sample

The following sample functions demonstrate how to determine whether or not a polysurface is a box.

```cpp
bool IsBrepBox( const ON_Brep& brep )
{
  double zero_tolerance = 1.0e-6; // or whatever
  ON_3dVector N[6];

  bool rc = brep.IsSolid();

  if (rc)
    rc = (brep.m_F.Count() == 6);

  if (rc)
  {
    for (int i = 0; rc && i < 6; i++)
    {
      ON_Plane plane;
      if (brep.m_F[i].IsPlanar(&plane, zero_tolerance))
      {
        N[i] = plane.zaxis;
        N[i].Unitize();
      }
      else
        rc = false;
    }
  }

  if (rc)
  {
    for (int i = 0; rc && i < 6; i++)
    {
      int count = 0;
      for (int j = 0; rc && j < 6; j++)
      {
        double dot = fabs(N[i] * N[j]);
        if (fabs(dot) <= zero_tolerance)
          continue;
        if (fabs(dot - 1.0) <= zero_tolerance)
          count++;
        else
          rc = false;
      }

      if (rc)
      {
        if (2 != count)
          rc = false;
      }
    }
  }

  return rc;
}
```
