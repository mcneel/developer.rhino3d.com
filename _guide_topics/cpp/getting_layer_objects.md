---
title: Getting Layer Objects
description: This brief guide demonstrates how to get all of the objects on a layer using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/layerobjects
order: 1
keywords: ['rhino', 'layers']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You would like to get all the objects on a specific layer.

## Solution

You can get all of the objects on a specified layer in two ways:

1. Use `CRhinoDoc::LookupObject`.
1. Use a `CRhinoObjectIterator`.

The `CRhinoDoc::LookupObject` is somewhat easier.  So, we will demonstrate this in the following sample...

## Sample

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  ON_wString layer_name = L"Default"; // some layer name to search for
  int layer_index = context.m_doc.m_layer_table.FindLayer( layer_name );
  if( layer_index >= 0 )
  {
    const CRhinoLayer& layer = context.m_doc.m_layer_table[layer_index];
    ON_SimpleArray<CRhinoObject*> objects;
    int object_count = context.m_doc.LookupObject( layer, objects );
    if( object_count > 0 )
    {
      const CRhinoObject* object = 0;
      int i;
      RhinoApp().Print( L"%s layer objects:\n", layer_name );

      for( i = 0; i < object_count; i++ )
      {
        object = objects[ i ];
        if( object )
          RhinoApp().Print( L"  %s\n", object->ShortDescription(false) );
      }
    }
  }

  return CRhinoCommand::success;
}
```
