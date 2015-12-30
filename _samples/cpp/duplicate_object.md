---
layout: code-sample-cpp
title: Duplicate Object
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/duplicateobject
description: Demonstrates how to make a copy of a CRhinoObject-derived object.
order: 1
---

```cpp
const CRhinoObject* object = ..... // some object
CRhinoObject* duplicate = object->Duplicate();
if( duplicate )
{
  if( context.m_doc.AddObject(duplicate) )
    context.m_doc.Redraw;
  else
    delete duplicate;
}
```
