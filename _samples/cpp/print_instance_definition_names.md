---
title: Print Instance Definition Names
description: Demonstrates how to print the names of all instance definitions in the document.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/printinstancedefinitions
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

  int num_printed = 0;
  for (int i = 0; i < idef_count; i++)
  {
    const CRhinoInstanceDefinition* idef = idef_table[i];
    if (idef != 0 && idef->IsDeleted() == false)
    {
      ON_wString idef_name = idef->Name();
      RhinoApp().Print(L"Instance definition %d = %s\n", num_printed, idef_name);
      num_printed += 1;
    }
  }

  return CRhinoCommand::success;
}
```
