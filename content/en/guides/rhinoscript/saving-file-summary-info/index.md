+++
aliases = ["/en/5/guides/rhinoscript/saving-file-summary-info/", "/en/6/guides/rhinoscript/saving-file-summary-info/", "/en/7/guides/rhinoscript/saving-file-summary-info/", "/wip/guides/rhinoscript/saving-file-summary-info/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This brief guide demonstrates how to display the File Properties dialog when saving Rhino files using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Saving File Summary Info"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/supersaver"
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

When you right-click on a file, using Windows Explorer, and pick “Properties...”, to bring up the File Properties dialog, you can add summary information to a file by clicking on the Summary tab and entering the appropriate information.  Imagine you would like to do this when saving Rhino files. Rhino does not have this capability, but RhinoScript can help.

## Solution

The following example script will save the Rhino file by scripting Rhino's Save command.  If the command was successful in saving the file, script will then display the File Properties dialog and display the summary information for that file...

```vbnet
Sub SuperSaver()
  Rhino.Command "_Save"
  If (0 = Rhino.LastCommandResult()) Then
    Dim objShell, objFolder, objFolderItem, objInfo
    Set objShell = CreateObject("Shell.Application")
    Set objFolder = objShell.NameSpace(Rhino.DocumentPath)
    If (Not objFolder Is Nothing) Then
      Set objFolderItem = objFolder.ParseName(Rhino.DocumentName)
      If (Not objFolderItem Is Nothing) Then
        Call objFolderItem.InvokeVerbEx("properties", "summary")
      End If
      Set objFolderItem = Nothing
    End If
    Set objFolder = Nothing
    Set objShell = Nothing
  End If
End Sub
```
