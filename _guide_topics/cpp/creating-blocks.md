---
title: Creating Blocks
description: This guide demonstrates how to create an instance definition using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/createblock
order: 1
keywords: ['rhino', 'blocks']
layout: toc-guide-page
---

 
## Overview

Rhino blocks, known in the SDK as instances, are single objects that combine one or more objects.  Using blocks lets you:

- Create parts libraries.
- Update all instances by modifying the block definition.
- Keep a smaller model size by using block instances instead of copying identical geometry.
- Use the *BlockManager* command to view information about the blocks defined in the model.
- Use the *Insert* command to place block instances into your model, which scales and rotates the instance.

## How To

Creating instance definitions using C/C++ requires two steps:

1. Define the instance definition objects.  Instance definition objects are similar to regular Rhino objects - the ones that you see on the screen.  The difference is that instance definition objects reside in a different location in the document.  To add instance definition objects to the document, use `CRhinoDoc::AddObject` and make sure you set the bInstanceDefinition parameter to true.
1. Add a new instance definition object to Rhino's instance definition table, which is located on the Rhino document.  An instance definition defines the name of the instance and the instance definition objects used by it.

**NOTE**: An instance definition's base point is always the world origin (0,0,0).  Knowing this, you need to orient your instance definition geometry around the world origin.  The *Block* command does this by prompting the user for a base point and then transforming the selected objects from the user's picked point to the world origin.  If you are adding your own geometry on the fly, and not picking it, just create your objects knowing that the base point for your instance definition will be the world origin.

## Sample

The following example code demonstrates how to select one or more objects and create a block definition with them.

**NOTE**:  Unlike Rhino's *Block* command, this example code does not delete the selected objects, nor does it automatically insert a block instance at the location defined by the user.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select objects to define block
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects to define block" );
  go.EnableReferenceObjectSelect( false );
  go.EnableSubObjectSelect( false );
  go.EnableGroupSelect( true );

  // Phantoms, grips, lights, etc., cannot be in blocks.
  const unsigned int forbidden_geometry_filter
                = CRhinoGetObject::light_object
                | CRhinoGetObject::grip_object
                | CRhinoGetObject::phantom_object;
  const unsigned int geometry_filter = forbidden_geometry_filter
                               ^ CRhinoGetObject::any_object;
  go.SetGeometryFilter( geometry_filter );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Block base point
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Block base point" );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_3dPoint base_point = gp.Point();

  // Block definition name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Block definition name" );
  gs.GetString();
  if( gs.CommandResult() != success )
    return gs.CommandResult();

  // Validate block name
  ON_wString idef_name = gs.String();
  idef_name.TrimLeftAndRight();
  if( idef_name.IsEmpty() )
    return nothing;

  // See if block name already exists
  CRhinoInstanceDefinitionTable& idef_table = context.m_doc.m_instance_definition_table;
  int idef_index = idef_table.FindInstanceDefinition( idef_name );
  if( idef_index >= 0 )
  {
    RhinoApp().Print( L"Block definition \"%s\" already exists.\n", idef_name );
    return nothing;
  }

  // Create new block definition
  ON_InstanceDefinition idef;
  idef.SetName( idef_name );

  // Gather all of the selected objects
  ON_SimpleArray<const CRhinoObject*> objects( go.ObjectCount() );
  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoObject* obj = go.Object(i).Object();
    if( obj )
      objects.Append( obj);
  }

  ON_Xform xform;
  xform.Translation( ON_origin - base_point );

  // Duplicate all of the selected objects and add them
  // to the document as instance definition objects
  ON_SimpleArray<const CRhinoObject*> idef_objects( objects.Count() );
  for( i = 0; i < objects.Count(); i++ )
  {
    const CRhinoObject* obj = objects[i];
    if( obj )
    {
      CRhinoObject* dupe = context.m_doc.TransformObject( obj, xform, false, false, false );
      if( dupe)
      {
        context.m_doc.AddObject( dupe, false, true );
        idef_objects.Append( dupe );
      }
    }
  }

  if( idef_objects.Count() < 1 )
  {
    RhinoApp().Print( L"Unable to duplicate block definition geometry.\n" );
    return failure;
  }

  idef_index = idef_table.AddInstanceDefinition( idef, idef_objects );
  if( idef_index < 0 )
  {
    RhinoApp().Print( L"Unable to create block definition \"%s\".\n", idef_name );
    return failure;
  }

  return success;
}
```

## Related Topics

- [Dynamically Inserting Blocks]({{ site.baseurl }}/guides/cpp/dynamically-inserting-blocks)
