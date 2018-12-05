---
title: Replace Object Hatch Pattern
description: Demonstrates how to replace a Hatch Object's pattern.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/replacehatchpattern
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select hatches to replace pattern" );
  go.SetGeometryFilter( CRhinoGetObject::hatch_object );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Name of replacement hatch pattern" );
  gs.GetString();
  if( gs.CommandResult() != success )
    return gs.CommandResult();

  ON_wString pattern_name = gs.String();
  pattern_name.TrimLeftAndRight();
  if( pattern_name.IsEmpty() )
    return nothing;

  int hatch_index = context.m_doc.m_hatchpattern_table.FindHatchPattern( pattern_name );
  if( hatch_index < 0 )
  {
    RhinoApp().Print( L"Specified hatch pattern not found in the document.\n" );
    return nothing;
  }

  int i, replaced = 0;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoHatch* hatch_obj = CRhinoHatch::Cast( go.Object(i).Object() );
    if( 0 == hatch_obj )
      continue;

    if( hatch_index == hatch_obj->PatternIndex() )
      continue;

    const ON_Hatch* hatch = hatch_obj->Hatch();
    if( 0 == hatch )
      continue;

    ON_Hatch* dup_hatch = hatch->DuplicateHatch();
    if( 0 == dup_hatch )
      continue;

    dup_hatch->SetPatternIndex( hatch_index );

    CRhinoHatch* dup_obj = hatch_obj->Duplicate();
    if( 0 == dup_obj )
    {
      delete dup_hatch;
      continue;
    }

    dup_obj->SetHatch( dup_hatch );
    if( !context.m_doc.ReplaceObject(CRhinoObjRef(hatch_obj), dup_obj) )
    {
      delete dup_obj;
      continue;
    }

    replaced++;
  }

  if( replaced > 0 )
  {
    context.m_doc.Redraw();
    if( 1 == replaced )
      RhinoApp().Print( L"1 hatch pattern replaced.\n" );
    else
      RhinoApp().Print( L"%d hatch patterns replaced.\n", replaced );
  }
  else
    RhinoApp().Print( L"0 hatch patterns replaced.\n" );

  return success;
}
```
