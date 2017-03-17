---
title: Show Hidden Objects
description: Demonstrates how to iterate through the geometry table and unhide hidden objects.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/showallhiddenobjects
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
int ShowAllHiddenObjects( CRhinoDoc& doc, bool bRedraw )
{
  CRhinoObjectIterator it(
        doc,
        CRhinoObjectIterator::undeleted_objects,
        CRhinoObjectIterator::active_and_reference_objects
        );
  it.IncludeLights();

  int count = 0;
  CRhinoObject* obj = 0;
  for( obj = it.First(); obj; obj = it.Next() )
  {
    // Ignore objects that are not hidden
    if( obj->Attributes().Mode() != ON::hidden_object )
      continue;
    // Ignore objects on hidden or locked layers
    if( ON::normal_layer != obj->ObjectLayer().Mode() )
      continue;
    if( doc.ShowObject(obj) )
      count++;
  }

  if( count > 0 && bRedraw )
    doc.Redraw();
  return count;
}
```
