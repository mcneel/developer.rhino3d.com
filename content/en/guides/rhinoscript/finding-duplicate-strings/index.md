+++
aliases = ["/en/5/guides/rhinoscript/finding-duplicate-strings/", "/en/6/guides/rhinoscript/finding-duplicate-strings/", "/en/7/guides/rhinoscript/finding-duplicate-strings/", "/en/wip/guides/rhinoscript/finding-duplicate-strings/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates finding duplicate string using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Finding Duplicate Strings"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/findduplicatestrings"
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

Imagine you have an array of strings which contains duplicates.  RhinoScript has a method to cull the duplicate strings.  But rather than cull them, one would like to find them with a routine that will return the indices of the duplicate items.

Better yet, a routine that would return sets of indices, with each set containing the indices of a particular string would solve the problem. For example, if an array contained "Curve", "Surface", "curve", "surface", we would like to have an array containing [0,2] and [1,3] returned.

## Solution

VBScript's `Dictionary` is a useful tool for storing associative data, or data in the form of (key, item) pairs. In the problem outlined above, you could use a Dictionary to track each string and the indices where is appears in the array. In other words, use a Dictionary to store (string, indices) pairs.

To store the indices, you are going to need an array. But creating and resizing VBScript arrays is always a challenge. So, you might consider using a .NET's `ArrayList` object.  A .NET `ArrayList` is a COM-enabled object, which means it can be used in VBScript.

The following sample function demonstrates how you can use a `Dictionary` of strings and .NET `ArrayList` objects to find the indices of duplicate string items in an array.

```vbnet
Function FindDuplicateStrings(arrStrings, blnCase)

  ' Local variables
  Dim objDict, strKey, objItem, arrItems
  Dim i, j, nCount
  Dim arrResults()

  ' Default return value
  FindDuplicateStrings = Null

  ' Create a dictionary object and set it's compare mode
  Set objDict = CreateObject("Scripting.Dictionary")
  If (blnCase = True) Then
    objDict.CompareMode = vbBinaryCompare
  Else
    objDict.CompareMode = vbTextCompare
  End If

  ' Process input strings. If the string is not in the dictionary,
  ' then add it and add it's index to the ArrayList. Otherwise,
  ' just add it's index to the dictionary item's existing ArrayList.
  For i = 0 To UBound(arrStrings)
    strKey = arrStrings(i)
    If Not objDict.Exists(strKey) Then
      objDict.Add strKey, CreateObject("System.Collections.ArrayList")
    End If      
    objDict(strKey).Add(i)
  Next

  ' Find all of the dictionary items that have more than one index.
  ' Add those arrays to our result array
  nCount = 0
  arrItems = objDict.Items
  For Each objItem In arrItems
    If (objItem.Count > 1) Then
      ReDim Preserve arrResults(nCount)    
      arrResults(nCount) = objItem.ToArray()
      nCount = nCount + 1
    End If
  Next

  ' Done!
  FindDuplicateStrings = arrResults

End Function
```

Here is an example of how to use the above function:

```vbnet
Sub TestFindDuplicateStrings

  Dim arrStrings, arrResults, arrItem, nItem, i

  arrStrings = Array("Curve" ,  _
                     "Surface", _
                     "Mesh",    _
                     "Point",   _
                     "Surface", _
                     "Curve",   _
                     "Curve")

  arrResults = FindDuplicateStrings(arrStrings, False)
  If IsArray(arrResults) Then
    Call Rhino.Print("Duplicate Sets = " & CStr(UBound(arrResults) + 1))
    For i = 0 To UBound(arrResults)
      Call Rhino.Print("Set = " & CStr(i + 1))
      arrItem = arrResults(i)
      For Each nItem In arrItem
        Call Rhino.Print("Item " & CStr(nItem) & " = " & arrStrings(nItem))
      Next
    Next
  End If

End Sub
```

## Related Topics

- [Array Utilities](/guides/rhinoscript/array-utilities)
- [Sorting VBScript Arrays with .NET](/guides/rhinoscript/sorting-vbs-arrays-with-net)
- [VBScript Dictionaries](/guides/rhinoscript/vbscript-dictionaries)
