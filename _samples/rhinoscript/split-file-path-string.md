---
title: Split File Path String
description: Demonstrates how to break a file path string in to its components using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/splitpath
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
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
