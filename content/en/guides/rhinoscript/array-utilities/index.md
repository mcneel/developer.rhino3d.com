+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide presents an array of VBScript Array utilities."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Array Utilities"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/arrayutilities"
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

 
## Overview

Arrays are a very useful and easy way of storing variables - and they're especially easy to use in VBScript. This is due to several factors:

- VBScript is particularly liberal with any variable definition - that means that there is no strict defining of variables to a particular data type.
- The data type is assigned automatically when the variable is loaded with a value.
- It is even possible to mix data types within the same array.
- It is also possible to define the arrays in different ways:
    - Create the array element by element.
    - Use the VBScript `Array` method.
    - Use the VBScript `Split` method.
    - It is even possible to create multi-dimensional arrays and to make them dynamic rather than static.

But, VBScript falls short, compared to other programming languages, when it comes to providing tools for manipulating arrays. Some common array operations that VBScript does not provide methods for are:

- Adding a new elements to an array.
- Appending one array to the end of another array.
- Inserting new elements at given positions in an array.
- Removing elements from an array.
- Removing duplicate items from an array.
- Sorting the elements in an array.
- Reverse the order of the elements in an array.

For some of these tasks, RhinoScript does provide useful methods:

- `CullDuplicateNumbers` - Remove duplicates from an array of numbers.
- `CullDuplicatePoints` - Remove duplicates from an array of 3-D points.
- `CullDuplicateStrings` - Remove duplicates from an array of strings.
- `SortNumbers` - Sorts an array of numbers.
- `SortPoints` - Sorts an array of 3-D points.
- `SortStrings` - Sorts an array of strings.

For the other tasks, you will need to write your own procedures. Fortunately, VBScript provides us enough tools to write our own procedures to do most of what we would ever want to do with an array. Note,

## Utilities

The following examples are general purpose utilities.  If you need something more specific, these examples are a good starting point.

### Add Elements At End

Add a new element to the end of an array...

```vbnet
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

### Append Array

Append another array to the end of an array...

```vbnet
Sub ArrayAppend(ByRef arr, ByVal arr0)
  Dim i, ub
  If IsArray(arr) And IsArray(arr0) Then
    On Error Resume Next
    ub = UBound(arr)
    If Err.Number <> 0 Then ub = -1
    ReDim Preserve arr(ub + UBound(arr0) + 1)
    For i = 0 To UBound(arr0)
      arr(ub + 1 + i) = arr0(i)
    Next
  End If
End Sub
```

This example uses the .NET `ArrayList` object:

```vbnet
Sub ArrayAppend(ByRef arr, ByVal arr0)
  Dim i, list
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      Call list.Add(arr(i))
    Next
    For i = 0 To UBound(arr0)
      Call list.Add(arr0(i))
    Next
    arr = list.ToArray()    
  End If
End Sub
```

### Insert Elements

Insert a new element at a given position in an array...

```vbnet
Sub ArrayInsert(ByRef arr, ByVal pos, ByVal val)
  Dim i
  If IsArray(arr) Then
    If pos > UBound(arr) Then
      Call ArrayAdd(arr, val)
    ElseIf pos >= 0 Then
      ReDim Preserve arr(UBound(arr) + 1)
      For i = UBound(arr) To pos + 1 Step -1
        arr(i) = arr(i - 1)
      Next
      arr(pos) = val
    End If
  End If
End Sub
```

This example uses the .NET `ArrayList` object:

```vbnet
Sub ArrayInsert(ByRef arr, ByVal pos, ByVal val)
  Dim i, list
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      Call list.Add(arr(i))
    Next
    Call list.Insert(pos, val)
    arr = list.ToArray()    
  End If
End Sub
```

### Remove Elements

Remove an element from the end of an array...

```vbnet
Sub ArrayRemove(ByRef arr)
  If IsArray(arr) Then
    If UBound(arr) > -1 Then
      ReDim Preserve arr(UBound(arr) - 1)
    End If
  End If
End Sub
```

Remove an element at a given position from an array...

```vbnet
Sub ArrayRemoveAt(ByRef arr, ByVal pos)
  Dim i
  If IsArray(arr) Then
    If pos >= 0 And pos <= UBound(arr) Then
      For i = pos To UBound(arr) - 1
        arr(i) = arr(i + 1)
      Next
      ReDim Preserve arr(UBound(arr) - 1)
    End If
  End If
End Sub
```

This example uses the .NET `ArrayList` object to remove an element from a given position in an array...

```vbnet
Sub ArrayRemoveAt(ByRef arr, ByVal pos)
  Dim i, list
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      Call list.Add(arr(i))
    Next
    Call list.RemoveAt(pos)
    arr = list.ToArray()    
  End If
End Sub
```

Remove all instances of a value from an array...

```vbnet
Sub ArrayRemoveVal(ByRef arr, ByVal val)
  Dim i, j
  If IsArray(arr) Then
    i = 0 : j = -1
    For i = 0 To UBound(arr)
      If arr(i) <> val Then
        j = j + 1
        arr(j) = arr(i)
      End If
    Next
  ReDim Preserve arr(j)
  End If
End Sub
```

Remove duplicate items from an array using VBScript's `Dictionary` object:

```vbnet
Sub ArrayCull(ByRef arr)
  Dim i, dict
  If IsArray(arr) Then
    Set dict = CreateObject("Scripting.Dictionary")
    For i = 0 To UBound(arr)
      If Not dict.Exists(arr(i)) Then
        Call dict.Add(arr(i), arr(i))
      End If
    Next
    arr = dict.Items
  End If
End Sub
```

Remove duplicate items from an array using the .NET `ArrayList` object:

```vbnet
Sub ArrayCull(ByRef arr)
  Dim i, list, tmp
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      If Not list.Contains(arr(i)) Then
        Call list.Add(arr(i))
      End If
    Next
    arr = list.ToArray()    
  End If
End Sub
```

### Find Elements

Find the first occurance of a value in an array...

```vbnet
Function ArraySearch(ByRef arr, ByVal val)
  Dim i
  ArraySearch = -1
  If IsArray(arr) Then
    For i = 0 To UBound(arr)
      If arr(i) = val Then
        ArraySearch = i
        Exit Function
      End If
    Next
  End If
End Function
```

### Sort Elements

This example uses a simple Bubble Sort algorithm...

```vbnet
Sub ArraySort(ByRef arr)
  Dim i, j, tmp
  If IsArray(arr) Then
    For i = UBound(arrShort) - 1 To 0 Step -1
      For j = 0 To i
        If arr(j) > arr(j + 1) Then
          tmp = arr(j + 1)
          arr(j + 1) = arr(j)
          arr(j) = tmp
        End If
      Next
    Next
  End If
End Sub
```

This example uses the .NET `ArrayList` object...

```vbnet
Sub ArraySort(ByRef arr)
  Dim i, list
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      Call list.Add(arr(i))
    Next
    Call list.Sort()
    arr = list.ToArray()
  End If    
End Sub
```

Reverse the order of the elements in an array...

```vbnet
Sub ArrayReverse(ByRef arr)
  Dim i, ub, ub2, tmp
  ub = UBound(arr)
  ub2 = Int(ub / 2)
  For i = 0 To ub2
    tmp = arr(i)
    arr(i) = arr(ub - i)
    arr(ub - i) = tmp
  Next
End Sub
```

This example uses the .NET `ArrayList` object to reverse the order of elements...

```vbnet
Sub ArrayReverse(ByRef arr)
  Dim i, list
  If IsArray(arr) Then
    Set list = CreateObject("System.Collections.ArrayList")
    For i = 0 To UBound(arr)
      Call list.Add(arr(i))
    Next
    Call list.Reverse()
    arr = list.ToArray()
  End If    
End Sub
```

### Verify Dimmed

Verifies that an array has been "dimmed"...

```vbnet
Function IsArrayDim(ByVal arr)
  IsArrayDim = False
  If IsArray(arr) Then
    On Error Resume Next
    Call UBound(arr)
    If Err.Number = 0 Then IsArrayDim = True
  End If
End Function
```

### Count Dimensions

Returns the number of dimensions to an array...

```vbnet
Public Function GetArrayDim(ByVal arr)
  Dim i
  If IsArray(arr) Then
    For i = 1 To 60
      On Error Resume Next
      Call UBound(arr, i)
      If Err.Number <> 0 Then
        GetArrayDim = i - 1
        Exit Function
      End If
    Next
    GetArrayDim = i
  Else
    GetArrayDim = Null
  End If
End Function
```

### Print Contents

Print the contents of an array...

```vbnet
Sub ArrayPrint(ByVal arr)
  Dim i
  If IsArray(arr) Then
    For i = 0 To UBound(arr)
      Call Rhino.Print("Item(" & CStr(i) & ") = " & CStr(arr(i)))
    Next
  End If
End Sub
```
