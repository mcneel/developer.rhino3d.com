---
layout: code-sample-cpp
title: Set Command Prompt
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/setcommandprompt
description: Demonstrates how to set Rhino's command prompt text to show the progress of long processes.
order: 1
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
