---
title: Getting Object UUIDs
description: This brief guide demonstrates how to get an object's UUID using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/getuuid
order: 1
keywords: ['rhino', 'uuid', 'guid']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

Rhino can create and manipulate many geometric objects, including points, point clouds, curves, surfaces, b-reps, meshes, lights, annotations, and references.  A globally unique identifier, or UUID, is assigned to each object in the Rhino document when the objects are created.  Because identifiers are saved in the 3DM file, an object's identifier will be the same between editing sessions.

## Sample

The following code sample demonstrates how to obtain an object's unique identifier, or UUID, using C/C++:

```cpp
CRhinoCommand::result CCommandTestID::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select object" );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& ref = go.Object( 0 );
  const CRhinoObject* obj = ref.Object();
  if( !obj )
    return CRhinoCommand::failure;

  ON_UUID uuid = obj->Attributes().m_uuid;
  ON_wString str;
  ON_UuidToString( uuid, str );
  ::RhinoApp().Print( L"The object's unique identifier is \"%s\".\n", str );
  return CRhinoCommand::success;
}
```
