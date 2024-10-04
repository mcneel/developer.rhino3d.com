+++
aliases = ["/en/5/samples/rhinoscript/convert-block-to-group/", "/en/6/samples/rhinoscript/convert-block-to-group/", "/en/7/samples/rhinoscript/convert-block-to-group/", "/wip/samples/rhinoscript/convert-block-to-group/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to explode a block and group its components using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Convert Block to Group"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/convertblocktogroup"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ConvertBlockToGroup.rvb -- March 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Main procedure for script
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ConvertBlockToGroup()

  ' Local variables
  Dim arrBlocks, strBlock, arrObjects(), nBound

  ' Get blocks to explode
  arrBlocks = Rhino.GetObjects("Select blocks to convert", 4096, True, True)
  If IsNull(arrBlocks) Then Exit Sub

  ' Explode the blocks    
  For Each strBlock In arrBlocks  
    ' Reset our array of objects
    ReDim arrObjects(-1)  
    ' Explode the block
    Call BlockExplode(strBlock, arrObjects)
    ' See if any objects were added to our array
    On Error Resume Next
    nBound = UBound(arrObjects)
    If (Err.Number = 0) Then
      ' Group the objects
      Call Rhino.AddObjectsToGroup(arrObjects, Rhino.AddGroup())
    End If
  Next

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Explodes a block and all of its nested blocks
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub BlockExplode(ByVal strBlock, ByRef arrObjects)

 ' Local variables
 Dim arrExplodes, strExplode

 ' Explode the block
 If Rhino.IsBlockInstance(strBlock) Then
   arrExplodes = Rhino.ExplodeBlockInstance(strBlock)
   If IsArray(arrExplodes) Then
     For Each strExplode In arrExplodes
       ' Recusive call...
       Call BlockExplode(strExplode, arrObjects)
     Next
   End If
 Else
   ' Add the object to our array
   Call ArrayAdd(arrObjects, strBlock)   
 End If

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Adds a new element to the end of an array
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ArrayAdd(ByRef arr, ByVal val)
  Dim ub
  If IsArray(arr) Then
   On Error Resume Next
   ub = UBound(arr)
   If Err.Number <> 0 Then ub = -1
   ReDim Preserve arr(ub + 1)
   arr(UBound(arr)) = val
  End If
End Sub
```
