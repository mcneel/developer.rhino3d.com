---
title: Set Command Prompt
description: Demonstrates how to set Rhino's command prompt text to show the progress of long processes.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/setcommandprompt
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  ON_wString prompt;
  int i, entity_count = 1000;
  for( i = 0; i < entity_count; i++ )
  {
    prompt.Format( L"Importing IGES entity %d of %d", i+1, entity_count );
    RhinoApp().SetCommandPrompt( prompt );
    RhinoApp().Wait(0);

    // TODO:
  }
  RhinoApp().Print( L"IGES import successful.\n" );

  return success;
}
```
