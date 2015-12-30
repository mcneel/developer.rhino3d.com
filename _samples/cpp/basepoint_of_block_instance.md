---
layout: code-sample-cpp
title: Basepoint of Block Instance
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/blockinsertionpoint
description: Demonstrates how to find the basepoint coordinates of a block instance.
order: 1
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
