+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to clear Rhino's Undo and Redo lists using C/C++."
keywords = [ "rhino", "clear", "undo", "redo" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Clear Undo and Redo Lists"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/clearundo"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## How To

Rhino allows users to undo the most recent or several create, edit, or transform commands. If you are performing editing operations on large memory consuming objects, Rhino's undo list can quickly grow very large. When this happens, most Rhino users run the ClearUndo command to clear the undo list. It is also possible to clear the undo list from within a plugin.

The following sample code demonstrates how to clear Rhino's undo and redo lists...

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context
        )
{
  RhinoApp().Print( L"Clearing undo and redo lists.\n" );
  context.m_doc.ClearUndoRecords( true );
  return CRhinoCommand::success;
}
```
