---
title: Modifying Advanced Display Settings
description: This guide demonstrates how to modify advanced display settings using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Miscellaneous']
origin: http://wiki.mcneel.com/developer/sdksamples/advanceddisplay
order: 1
keywords: ['rhino', 'display', 'settings']
layout: toc-guide-page
---

# Modifying Advanced Display Settings

{{ page.description }}

## Overview

The advanced display features in Rhino give the user almost unlimited control over how objects appear on the screen.  All of these features are also exposed to the C/C++ developer.

Rhino maintains advanced display settings using the `CDisplayPipelineAttributes` class.  Rhino will maintain a number of these objects, one for each advanced display setting created by the user (i.e. Wireframe, Shaded, Rendered, Ghosted, X-Ray, etc.) or by 3rd party plugins.

The C/C++ developer can gain access to these objects using the Display Attributes Manager, which is implemented as a number of static functions found on the `CRhinoDisplayAttrsMgr` class.

The process for updating advanced display settings is similar to updating or modifying other objects in Rhino.

1. Make a copy of the original.
1. Modify one or more setting or parameters.
1. Replace the original object with the modified copy.

## Sample

```cpp
// The following example code demonstrates how to modify advanced display settings using
// the Rhino SDK. In this example, a display mode's mesh wireframe thickness (in pixels)
// will be modified.
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Use the display attributes manager to build a list of display modes.
  // Note, these are copies of the originals...
  DisplayAttrsMgrList attrs_list;
  int attrs_count = CRhinoDisplayAttrsMgr::GetDisplayAttrsList( attrs_list );
  if( attrs_count == 0 )
    return failure;

  // Construct an options picker so the user can pick which
  // display mode they want modified
  CRhinoGetOption go;
  go.SetCommandPrompt( L"Display mode to modify mesh thickness" );

  ON_SimpleArray<int> opt_list( attrs_count );
  opt_list.SetCount( attrs_count );

  for( int i = 0; i < attrs_count; i++ )
  {
    // Verify the display mode had a valid
    // CDisplayPipelineAttributes pointer
    if( 0 == attrs_list[i].m_pAttrs )
    {
      opt_list[i] = 0;
      continue;
    }

    // Get the display attributes English name
    ON_wString english_name = attrs_list[i].m_pAttrs->EnglishName();
    english_name.Remove( L'_' );
    english_name.Remove( L' ' );
    english_name.Remove( L'-' );
    english_name.Remove( L',' );
    english_name.Remove( L'.' );

    // Get the display attributes localized name
    ON_wString local_name = attrs_list[i].m_pAttrs->LocalName();
    local_name.Remove( L'_' );
    local_name.Remove( L' ' );
    local_name.Remove( L'-' );
    local_name.Remove( L',' );
    local_name.Remove( L'.' );

    // Add the command option
    opt_list[i] = go.AddCommandOption( CRhinoCommandOptionName(english_name, local_name) );
  }

  // Get the command option
  go.GetOption();
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoCommandOption* opt = go.Option();
  if( 0 == opt )
    return failure;

  // Figure out which command option was picked
  int attrs_index = -1;
  for( int i = 0; i < opt_list.Count(); i++ )
  {
    if( opt_list[i] == opt->m_option_index )
    {
      attrs_index = i;
      break;
    }
  }

  // Validate...
  if( attrs_index < 0 | attrs_index >= attrs_count )
    return failure;

  // Get the display mode requested by the user
  DisplayAttrsMgrListDesc desc = attrs_list[attrs_index];
  if( 0 == desc.m_pAttrs )
    return failure;

  // Modify the desired display mode. In this case, we
  // will just set the mesh wireframe thickness to zero.
  desc.m_pAttrs->m_nMeshWireThickness = 0;

  // Use the display attributes manager to update the display mode.
  CRhinoDisplayAttrsMgr::UpdateAttributes( desc );

  // Force the document to regenerate.
  context.m_doc.Regen();

  return success;
}
```
