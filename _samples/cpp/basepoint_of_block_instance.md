---
title: Basepoint of Block Instance
description: Demonstrates how to find the basepoint coordinates of a block instance.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/sdksamples/blockinsertionpoint
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
ON_3dPoint BlockInstanceInsertionPoint(const CRhinoInstanceObject* instance_obj)
{
  ON_3dPoint pt = ON_UNSET_POINT;
  if (instance_obj != 0)
  {
    pt = ON_origin;
    pt.Transform(instance_obj->InstanceXform());
  }
  return pt;
}
```
