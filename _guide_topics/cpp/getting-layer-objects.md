---
title: Getting Layer Objects
description: This brief guide demonstrates how to get all of the objects on a layer using C/C++.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/layerobjects
order: 1
keywords: ['rhino', 'layers']
layout: toc-guide-page
---

 
## Problem

You would like to get all the objects on a specific layer.

## Solution

You can get all of the objects on a specified layer in two ways:

1. Use `CRhinoDoc::LookupObject`.
1. Use a `CRhinoObjectIterator`.

The `CRhinoDoc::LookupObject` is somewhat easier.  So, we will demonstrate this in the following sample...

## Sample

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  const wchar_t* psz_layer_name = L"Default"; ;
  int layer_index = context.m_doc.m_layer_table.FindLayerFromFullPathName(psz_layer_name, ON_UNSET_INT_INDEX);
  if (layer_index >= 0 && layer_index < context.m_doc.m_layer_table.LayerCount())
  {
    const CRhinoLayer& layer = context.m_doc.m_layer_table[layer_index];
    ON_SimpleArray<CRhinoObject*> objects;
    int object_count = context.m_doc.LookupObject(layer, objects);
    if (object_count > 0)
    {
      RhinoApp().Print(L"%s layer object(s)s:\n", psz_layer_name);
      for (int i = 0; i < object_count; i++)
      {
        const CRhinoObject* object = objects[i];
        if (object)
          RhinoApp().Print(L"  %s\n", object->ShortDescription(false));
      }
    }
  }
  return CRhinoCommand::success;
}
```
