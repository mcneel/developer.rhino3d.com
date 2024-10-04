+++
aliases = ["/en/5/guides/rhinoscript/efficient-script-loading/", "/en/6/guides/rhinoscript/efficient-script-loading/", "/en/7/guides/rhinoscript/efficient-script-loading/", "/wip/guides/rhinoscript/efficient-script-loading/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide discusses different techniques of loading and running script and their efficiencies."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Efficient Script Loading"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/scriptloading"
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

 
## LoadScript and RunScript

When running a script from a toolbar button, is it better to use the *LoadScript* command or *RunScript* command?  Which is better for Rhino, resource wise?

The **LoadScript** command:

1. Opens the script file, reads the contents of the file into a buffer, and then closes the file.
1. Loads the buffer, read in from the script file, it into the scripting engine. The script engine, then, attempts to parse the script.
1. If the script was parsed successfully, it is run, or executed.

The **RunScript** command:

1. Runs the script, skipping steps 1. and 2. listed above.

## Considerations

Using *LoadScript* to load the same script file over and over and over again is somewhat inefficient and certainly unnecessary, as you are simply replacing the same script, over and over again, that is already resident in the script engine. The only time you need reload a script is if the script has changed, or if the script engine was reset.

One technique you can use to be more efficient, when loading scripts, is to have them load at startup. You can specify the scripts to load at startup by selecting **Tool** > **Option** > **RhinoScript**. Then, you can just use the *RunScript* to execute your pre-loaded scripts.

Another technique you can use it to load your scripts on demand. For example, say you have a *Hello.rvb* script file with a single function defined as such:

```vbnet
Sub Hello
  Call MsgBox("Hello Rhino!")
End Sub
```

From a toolbar button, you could use the following macro to load it on demand and then run it:

```vbnet
_-NoEcho _-RunScript (
If Not Rhino.IsProcedure("Hello") Then
  Call Rhino.Command("_-LoadScript Hello.rvb", 0)
End If
Call Hello
```

The code above checks for the existence of a user-defined procedure (e.g. subroutine or function) named `"Hello"`. If the procedure is not found, then script file, were the procedure is stored, is loaded by running the *LoadScript* command.  Finally, the specified procedure is called.

To ensure this technique works, make sure to included the path to Hello.rvb is included in Rhino's file search path by selecting **Tools** > **Options** > **Files**.

## Related Topics

- [Script Demand Loading](/guides/rhinoscript/script-demand-load)
