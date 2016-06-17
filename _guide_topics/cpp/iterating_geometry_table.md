---
title: Iterating the Geometry Table
description: This guide demonstrates how to use the C/C++ CRhinoObjectIterator class to iterate through the document.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/objectiterator
order: 1
keywords: ['rhino', 'document', 'iteration']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The `CRhinoGetObject` class is useful when you need the user to interactively pick one or more objects.  But, it is not too useful if you need to walk through the entire document looking for objects.  This is where the `CRhinoObjectIterator` class comes in.

The `CRhinoObjectIterator` class is used to iterate through the objects in a `CRhinoDoc` object.  You can limit the iteration by specifying one of five mutually exclusive object states and one of three mutually exclusive object categories.

## Sample

```cpp
CRhinoCommand::result CCommandTestIterator::RunCommand(
                  const CRhinoCommandContext& context )
{
  CRhinoObjectIterator it(
        CRhinoObjectIterator::undeleted_objects,
        CRhinoObjectIterator::active_and_reference_objects
        );
  it.IncludeLights( TRUE );
  it.IncludeGrips( false );
  int count = 0;
  for( CRhinoObject* pObject = it.First(); pObject; pObject = it.Next() )
  {
    if( pObject->IsSelected() )
      continue;
    if( !pObject->IsSelectable() )
      continue;
    pObject->Select();
    count++;
  }

  if( count )
    context.m_doc.Redraw();

  ::RhinoApp().Print( L"%d object(s) selected.\n", count );
  return CRhinoCommand::success;
}
```

For more information, see the *rhinoSdkDoc.h* SDK header file.
