---
title: Modify an Object's Name
description: Demonstrates how to modify an object's user-defined name.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/objectname
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
//This sample code demonstrates how to modify the name of a single object.
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  // Select an object to modify
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select object to change name" );
  go.EnablePreSelect( TRUE );
  go.EnableSubObjectSelect( FALSE );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Get the object reference
  const CRhinoObjRef& objref = go.Object(0);

  // Get the object
  const CRhinoObject* obj = objref.Object();
  if( !obj )
    return CRhinoCommand::failure;

  // Make copy of object attributes. This objects
  // holds an object's user-defined name.
  ON_3dmObjectAttributes obj_attribs = obj->Attributes();

  // Prompt for new object name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"New object name" );
  gs.SetDefaultString( obj_attribs.m_name );
  gs.AcceptNothing( TRUE );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Get the string entered by the user
  ON_wString obj_name = gs.String();
  obj_name.TrimLeftAndRight();

  // Is name the same?
  if( obj_name.Compare(obj_attribs.m_name) == 0 )
    return CRhinoCommand::nothing;

  // Modify the attributes of the object
  obj_attribs.m_name = obj_name;
  context.m_doc.ModifyObjectAttributes( objref, obj_attribs );

  return CRhinoCommand::success;
}
```

Alternatively:

```cpp
//This sample code demonstrates how to modify the name of one or more objects.
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select objects to modify
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects to change name" );
  go.EnablePreSelect( TRUE );
  go.EnableSubObjectSelect( FALSE );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Prompt for new object name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"New object name" );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Get the string entered by the user
  ON_wString obj_name = gs.String();
  obj_name.TrimLeftAndRight();

  // Process each selected object
  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    // Get the object reference
    const CRhinoObjRef& objref = go.Object(i);

    // Get the object
    const CRhinoObject* obj = objref.Object();
    if( !obj )
      return CRhinoCommand::failure;

    // Make copy of object attributes. This objects
    // holds an object's user-defined name.
    ON_3dmObjectAttributes obj_attribs = obj->Attributes();

    // Is name the same?
    if( obj_name.Compare(obj_attribs.m_name) == 0 )
      continue;

    // Modify the attributes of the object
    obj_attribs.m_name = obj_name;
    context.m_doc.ModifyObjectAttributes( objref, obj_attribs );
  }

  return CRhinoCommand::success;
}
```

...or:

```cpp
//This sample code demonstrates how to modify all normal (not locked and not hidden) objects.
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Prompt for new object name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"New object name" );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Get the string entered by the user
  ON_wString obj_name = gs.String();
  obj_name.TrimLeftAndRight();

  // Iterate through all normal (not locked and not hidden) objects
  CRhinoObjectIterator it( CRhinoObjectIterator::normal_objects, CRhinoObjectIterator::active_objects );
  CRhinoObject* obj = 0;
  for( obj = it.First(); obj; obj = it.Next() )
  {
    // Make copy of object attributes. This objects
    // holds an object's user-defined name.
    ON_3dmObjectAttributes obj_attribs = obj->Attributes();

    // Is name the same?
    if( obj_name.Compare(obj_attribs.m_name) == 0 )
      continue;

    // Modify the attributes of the object
    obj_attribs.m_name = obj_name;
    context.m_doc.ModifyObjectAttributes( CRhinoObjRef(obj), obj_attribs );
  }

  return CRhinoCommand::success;
}
```
