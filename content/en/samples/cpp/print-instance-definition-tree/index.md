+++
aliases = ["/en/5/samples/cpp/print-instance-definition-tree/", "/en/6/samples/cpp/print-instance-definition-tree/", "/en/7/samples/cpp/print-instance-definition-tree/", "/wip/samples/cpp/print-instance-definition-tree/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to print the names of all instance definitions, including objects and sub-instances, in a tree-style format."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Print Instance Definition Tree"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/printinstancedefinitiontree"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
