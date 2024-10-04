+++
aliases = ["/en/5/samples/rhinoscript/match-object-attributes/", "/en/6/samples/rhinoscript/match-object-attributes/", "/en/7/samples/rhinoscript/match-object-attributes/", "/wip/samples/rhinoscript/match-object-attributes/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates a custom object attribute matching function in RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Match Object Attributes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/matchobjectattributesex"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
' Description:
'   Matches, or copies, the attributes of a source object to a
'   target object or an array of target objects. If the source
'   object is not specified, the attributes of the target object(s)
'   will be reset to Rhino's default object attributes.
' Parameters:
'   arrTargets - An array of strings identifying the target objects.
'   strSource  - The identifier of the source object. If the source
'                object is not specified, the attributes of the target
'                object(s) will be reset to Rhino's default object
'                attributes.
'   intMode    - The group mode flag, where:
'                  intMode = -1, remove all groups from targets
'                  intMode =  0, do not copy source groups to targets
'                  intMode =  1, copy source groups to targets
'
Function MatchObjectAttributesEx(arrTargets, strSource, intMode)

  Dim strTarget, arrGroups, strGroup

  If intMode < -1 Then
    intMode = -1
  ElseIf intMode > 1 Then
    intMode = 1
  End If

  For Each strTarget In arrTargets

    If intMode = 0 Then
      arrGroups = Rhino.ObjectGroups(strTarget)
    Else
      arrGroups = Null
    End If

    Call Rhino.MatchObjectAttributes(strTarget, strSource)

    If intMode = -1 Or intMode = 0 Then
      Call Rhino.RemoveObjectFromAllGroups(strTarget)
    End If

    If intMode = 0 And Not IsNull(arrGroups) Then
      For Each strGroup In arrGroups
      	Call Rhino.AddObjectToGroup(strTarget, strGroup)
      Next
    End If

  Next

End Function
```
