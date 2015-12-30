---
layout: code-sample-rhinoscript
title: Splitting a File Path String
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to break a file path string in to its components using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/splitpath
order: 1
---

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
