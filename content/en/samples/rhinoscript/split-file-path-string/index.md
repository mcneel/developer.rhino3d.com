+++
aliases = ["/en/5/samples/rhinoscript/split-file-path-string/", "/en/6/samples/rhinoscript/split-file-path-string/", "/en/7/samples/rhinoscript/split-file-path-string/", "/wip/samples/rhinoscript/split-file-path-string/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to break a file path string in to its components using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Split File Path String"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/splitpath"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub SplitPath(ByVal sPath, ByRef sDrive, ByRef sDir, ByRef sFname, ByRef sExt)
  Dim fso
  Set fso = CreateObject("Scripting.FileSystemObject")
  sDrive = fso.GetDriveName(sPath)
  sDir = Mid(fso.GetParentFolderName(sPath), Len(sDrive)+1) & "\"
  sFname = fso.GetBaseName(sPath)
  sExt = "." & fso.GetExtensionName(sPath)
  Set fso = Nothing
End Sub
```
