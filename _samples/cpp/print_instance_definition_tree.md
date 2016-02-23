---
title: Print Instance Definition Tree
description: Demonstrates how to print the names of all instance definitions, including objects and sub-instances, in a tree-style format.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/sdksamples/printinstancedefinitiontree
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  const CRhinoInstanceDefinitionTable& idef_table = context.m_doc.m_instance_definition_table;
  int idef_count = idef_table.InstanceDefinitionCount();
  if (idef_count == 0)
  {
    RhinoApp().Print("No instance definitions found.\n");
    return CRhinoCommand::nothing;
  }

  ON_wString writer;
  ON_TextLog dump( writer );
  dump.SetIndentSize( 4 );

  for (int i = 0; i < idef_count; i++)
    DumpInstanceDefinition( idef_table[i], dump, true );

  RhinoApp().Print( L"%s\n", writer );

  return CRhinoCommand::success;
}

void CCommandTest::DumpInstanceDefinition( const CRhinoInstanceDefinition* idef, ON_TextLog& dump, bool bRoot )
{
  if( idef && ! idef->IsDeleted() )
  {
    ON_wString node;
    if( bRoot )
      node = L"\u2500";
    else
      node = L"\u2514";
    dump.Print(L"%s Instance definition %d = %s\n", node, idef->Index(), idef->Name() );

    const int idef_object_count = idef->ObjectCount();
    if( idef_object_count )
    {
      dump.PushIndent();
      for( int i = 0; i < idef->ObjectCount(); i++ )
      {
        const CRhinoObject* obj = idef->Object( i );
        if( obj )
        {
          const CRhinoInstanceObject* iref = CRhinoInstanceObject::Cast( obj );
          if( iref )
            DumpInstanceDefinition( iref->InstanceDefinition(), dump, false ); // Recursive...
          else
            dump.Print(L"\u2514 Object %d = %s\n", i, obj->ShortDescription(false) );
        }
      }
      dump.PopIndent();
    }
  }
}
```
