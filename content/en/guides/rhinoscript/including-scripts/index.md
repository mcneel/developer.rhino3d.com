+++
aliases = ["/en/5/guides/rhinoscript/including-scripts/", "/en/6/guides/rhinoscript/including-scripts/", "/en/7/guides/rhinoscript/including-scripts/", "/wip/guides/rhinoscript/including-scripts/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide discusses how to include or use functions from another source file in RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Including Scripts"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/includefiles"
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

 
## Problem

In programming languages like C/C++ and C#, there are statements like `#include` and `using` where you can reference functions from other source files.  This is often used when you want to build a library of common functions that can be used from within other scripts,

VBScript does not have an equivalent to the C/C++ `#include` statement.  But, its possible to write your own include-type function.

## Solution

The following subroutine can be used to include scripts...

```vbnet
' ---------------------------------------------------------------------------
' Subroutine:  Include
' Purpose:     Includes, or loads, other RhinoScript files
' Argument:    A script file name to include
' Example:     Call Include("C:\Scripts\MyScriptFile.rvb")
' ---------------------------------------------------------------------------
Sub Include(strScriptName)
  Dim objFSO, objFile
  Set objFSO = CreateObject("Scripting.FileSystemObject")
  Set objFile = objFSO.OpenTextFile(strScriptName)
  ExecuteGlobal objFile.ReadAll()
  objFile.Close
End Sub
```

Also, if you have a number of script files that define utility functions and procedures that you would like to call from any source file, then consider adding these script files to the list of startup script file (*Tools* > *Options* > *RhinoScript*).
