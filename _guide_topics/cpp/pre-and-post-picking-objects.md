---
title: Pre- and Post-Picking Objects
description: This brief guide demonstrates how to both pre-pick and post-pick objects using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/prepostpick
order: 1
keywords: ['rhino', 'picking']
layout: toc-guide-page
---

 
## Overview

The normal operation for commands that manipulate geometric objects is to allow the user to either pre-pick or post-pick the objects.  Occasionally, though, it might be necessary for commands to want to allow for both pre-picked and post-picked objects.  That is, after it has been determined that objects were pre-picked, allow the user to continue to pos-pick more objects.

## Sample

The following code sample demonstrates this capability...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  bool bObjectsWerePreSelected = false;
  bool bObjectsWerePostSelected = false;
  ON_SimpleArray<const CRhinoObject*> obj_list;

  // Select some objects. Allow for pre-selected objects
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects" );
  go.EnablePreSelect( TRUE );
  go.GetObjects( 0, 0 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Add the selected objects to our list
  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoObjRef& objref = go.Object(i);
    const CRhinoObject* obj = objref.Object();
    if( obj )
      obj_list.Append( obj );
  }

  // Determine of the bjects were pre-selected
  // or post-selected.
  if( go.ObjectsWerePreSelected() )
    bObjectsWerePreSelected = true;
  else
    bObjectsWerePostSelected = true;

  // If objects were pre-selected, then select
  // more objects. But, ignore pre-selected ones.
  if( bObjectsWerePreSelected )
  {
    go.EnablePreSelect( FALSE );
    go.EnableDeselectAllBeforePostSelect( FALSE );
    go.GetObjects( 0, 0 );
    if( go.CommandResult() != CRhinoCommand::success )
      return go.CommandResult();

    for( i = 0; i < go.ObjectCount(); i++ )
    {
      const CRhinoObjRef& objref = go.Object(i);
      const CRhinoObject* obj = objref.Object();
      if( obj )
        obj_list.Append( obj );
    }

    bObjectsWerePostSelected = true;
  }

  if( obj_list.Count() == 0 )
    return CRhinoCommand::nothing;
  //
  // TODO: do something with the object list here
  //
  // The normal behavior of commands is that when they finish,
  // objects that were pre-selected remain selected and objects
  // that were post-selected will not be selected. Because we
  // potentially could have both, we'll try to do something
  // consistent.
  if( bObjectsWerePreSelected && bObjectsWerePreSelected )
  {
    for( i = 0; i < obj_list.Count(); i++ )
    {
      const CRhinoObject* obj = obj_list[i];
      if( obj && obj->IsSelected() )
        obj->Select( false );
    }
    context.m_doc.Redraw();
  }
  return CRhinoCommand::success;
}
```
