+++
aliases = ["/5/samples/rhinoscript/determining-selected-groups/", "/6/samples/rhinoscript/determining-selected-groups/", "/7/samples/rhinoscript/determining-selected-groups/", "/wip/samples/rhinoscript/determining-selected-groups/"]
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to determine what object groups are selected using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Determining Selected Groups"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/selectedgroups"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description
'   Returns an array of objects group names
'   from selected objects.
' Parameters
'   none
' Returns
'   An array of object group names or vbNull if none
'   of the selected objects belongs to a group.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function SelectedGroups()

  ' Declare locals
  Dim arrObjects, arrGroups(), strGroup
  Dim i, nCount, bAppend

  SelectedGroups = Null ' Default
  nCount = -1

  ' Get the selected objects  
  arrObjects = Rhino.SelectedObjects
  If Not IsArray(arrObjects) Then Exit Function

  ' Process each object. If the object belongs to an
  ' object group and that group name is not already
  ' in arrGroups, then append it to the end.    
  For i = 0 To UBound(arrObjects)
    bAppend = False
    strGroup = Rhino.ObjectTopGroup(arrObjects(i))
    If Not IsNull(strGroup) Then
      If (nCount = -1) Then
        bAppend = True
      ElseIf (FindGroup(strGroup, arrGroups) = -1) Then
        bAppend = True
      End If
      If bAppend = True Then
        nCount = nCount + 1
        ReDim Preserve arrGroups(nCount)
        arrGroups(nCount) = strGroup
      End If
    End If
  Next

  ' Return the array of group names    
  If (nCount > -1) Then SelectedGroups = arrGroups

End Function

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description
'   Searches an array of strings
' Parameters
'   strGroup - the name to look for
'   arrGroups - the array to search
' Returns
'   >= 0 if strGroup is found in arrGroups
'   -1 otherwise      
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function FindGroup(strGroup, arrGroups)
  Dim i
  FindGroup = -1 ' Default
  For i = 0 To UBound(arrGroups)
    If (StrComp(strGroup, arrGroups(i), 1) = 0) Then
      FindGroup = i
      Exit Function
    End If
  Next
End Function

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Test our SelectedGroups function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TestSelectedGroups
  Dim i, arrGroups
  arrGroups = SelectedGroups
  If IsArray(arrGroups) Then
    For i = 0 To UBound(arrGroups)
      Rhino.Print( arrGroups(i) )
    Next
  End If
End Sub
```
