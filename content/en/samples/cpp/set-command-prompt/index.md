+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to set Rhino's command prompt text to show the progress of long processes."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Set Command Prompt"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/setcommandprompt"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
