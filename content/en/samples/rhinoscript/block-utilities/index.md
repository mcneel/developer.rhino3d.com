+++
aliases = ["/5/samples/rhinoscript/block-utilities/", "/6/samples/rhinoscript/block-utilities/", "/7/samples/rhinoscript/block-utilities/", "/wip/samples/rhinoscript/block-utilities/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "A couple of useful block utilities written in RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Block Utilities"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/blockutilities"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BlockUtilities.rvb -- November 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

' Script to update all linked blocks
Sub UpdateAllLinkedBlocks()
  Call Rhino.Command("_-BlockManager _Update _All _Enter _Enter _Enter", 0)
End Sub

' Script to insert multiple files as linked blocks
Sub InsertMultipleFilesAsBlocks()
  Dim arrFiles, strFiles
  arrFiles = Rhino.OpenFileNames("Insert", "Rhino 3D Models (*.3dm)|*.3dm|All Files (*.*)|*.*|")
  If IsArray(arrFiles) Then
    For Each strFile In arrFiles
      Call Rhino.Command("_-Insert _File=_Yes " & strFile & " _Block _Pause _Enter _Enter", 0)
    Next
  End If
End Sub

' Script to export select and then insert as linked block
Sub Externalize()

  Dim arrObjects, arrPoint, strFile
  Dim arrCopy, strPoint

  arrObjects = Rhino.GetObjects("Select objects to define block")
  If IsNull(arrObjects) Then Exit Sub

  arrPoint = Rhino.GetPoint("Block base point")
  If IsNull(arrPoint) Then Exit Sub

  strFile = Rhino.SaveFileName("Save", "Rhino 3D Model (*.3dm)|*.3dm|")
  If IsNull(strFile) Then Exit Sub

  Call Rhino.EnableRedraw(False)

  arrCopy = Rhino.CopyObjects(arrObjects, arrPoint, Array(0,0,0))
  Call Rhino.SelectObjects(arrCopy)

  Call Rhino.Command("_-Export " & Chr(34) & strFile & Chr(34), 0)

  strPoint = Rhino.Pt2Str(arrPoint)
  Call Rhino.Command("_-Insert _File=_Yes " & strFile & " _Block " & strPoint & " _Enter _Enter", 0)  

  Call Rhino.DeleteObjects(arrCopy)
  Call Rhino.DeleteObjects(arrObjects)

  Call Rhino.EnableRedraw(True)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "UpdateAllLinkedBlocks", "_NoEcho _-RunScript (UpdateAllLinkedBlocks)"
Rhino.AddAlias "InsertMultipleFilesAsBlocks", "_NoEcho _-RunScript (InsertMultipleFilesAsBlocks)"
Rhino.AddAlias "Externalize", "_NoEcho _-RunScript (Externalize)"
```
