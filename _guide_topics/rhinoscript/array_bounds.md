---
title: Array Dimensions & Upper Bounds
description: This guide discusses how to determine the dimension and the upper bounds of arrays in RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/dimbounds
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# Array Dimensions & Upper Bounds

{{ page.description }}

## Overview

In a two-dimensional array, how do you determine the upper bounds of the array for each dimension?  Also, how do you handle jagged arrays?  That is, an array whose elements themselves are arrays?  How do I find the upper bounds of two, three, or n-dimensional array when the array is rectangular or jagged?

## UBound

To determine the upper bounds of an array, use VBScript's `UBound` method. The `UBound` method returns the largest available subscript for the indicated dimension of an array.  The syntax for `UBound` is:

```vbnet
UBound(arrayname [,dimension])
```

where...

- `arrayname` *(required)* is the name of the array variable.
- `dimension` *(optional)* is whole number indicating which dimension's upper bound is returned. Use 1 for the first dimension, 2 for the second, and so on. If dimension is omitted, 1 is assumed.

For example:

```vbnet
Dim A(100,3,4)
UBound(A)    ' 100
UBound(A, 1) ' 100
UBound(A, 2) ' 3
UBound(A, 3) ' 4
```

## Jagged Arrays

What if you do not know an array's dimensions, which might be the case with a jagged array? How do you know what dimension values are valid to pass to `UBound`?

VBScript does not have a function that returns the number of dimensions of an array. But, by using the `UBound` method and some simple error checking, we can write our own function that determines the number of dimension of an array.

Consider the following function:

```vbnet
'Description
'  Returns the dimension of an array.
'Parameters
'  arr - Name of the array variable.
'Returns
'  The dimension of the array if successful.
'  Null on error.
'
Function GetArrayDim(ByVal arr)
  GetArrayDim = Null
  Dim i
  If IsArray(arr) Then
    For i = 1 To 60
      On Error Resume Next
      UBound arr, i
      If Err.Number <> 0 Then
        GetArrayDim = i-1
        Exit Function
      End If
    Next
    GetArrayDim = i
  End If
End Function
```

`GetArrayDim` simply calls `UBound` with a different dimension parameter until an error is thrown. Note, since VBScript allows arrays of up to 60 dimensions, we must check up to this value.

Now that we have a function that will return the dimensions of an array, we can write a subroutine that dumps out the dimensions and upper bounds of either a rectangular or jagged array.

For example:

```vbnet
'Description
'  Prints an array's dimensions and upper bounds to the command line.
'Parameters
'  arr - Name of the array variable.
'
Sub DumpArrayInfo(arr)
  Dim i, j, d, b
  If IsArray(arr) Then
    For i = 0 To UBound(arr)
      If IsArray(arr(i)) Then
        d = GetArrayDim(arr(i))
        If IsNull(d) Then
          Rhino.Print "Element(" & CStr(i) & ") is not dimensioned"
        Else
          Rhino.Print "Element(" & CStr(i) & ") dimension = " & CStr(d)
          For j = 1 To d
            b = GetArrayUBound(arr(i), j)
            If IsNull(b) Then
              Rhino.Print "  Dimension(" & CStr(j) & ") has no bounds"
            Else
              Rhino.Print "  Dimension(" & CStr(j) & ") bounds = " & CStr(b)
            End If
          Next
        End If
      Else
        Rhino.Print "Element(" & CStr(i) & ") is not an array"
      End If
    Next
  End If
End Sub
```

For every element in an array, `DumpArrayInfo` calls `GetArrayDim` to determine the dimension of the array element.  If `GetArrayDim` returns a valid result, then the subroutine determines the upper bounds in each dimension of the array element and prints the results to the Rhino command line.

**NOTE**: `DumpArrayInfo` uses a `UBound` helper function named `GetArrayUBound` that is a little safer than just using `UBound`...

```vbnet
'Description
'  Safely returns the largest available subscript for
'  the indicated dimension of an array.
'Parameters
'  arr - Name of the array variable.
'  i   - Number indicating which dimension's upper bound to return.
'Returns
'  The upper bounds for the indicated dimension if successful.
'  Null on error.
'
Function GetArrayUBound(ByVal arr, ByVal i)
  GetArrayUBound = Null
  If IsArray(arr) Then
    On Error Resume Next
    b = UBound(arr, i)
    If Err.Number = 0 Then GetArrayUBound = b
  End If
End Function
```

We can test our array dumping subroutine as follows:

```vbnet
Sub TestDumpArrayInfo

  ' Declare arrays of various dimensions    
  Dim arr0(6)
  Dim arr1(5,4)
  Dim arr2(3,2,1)
  Dim arr3()
  Dim arr4

  ' Create a jagged array
  Dim arr(4)
  arr(0) = arr0
  arr(1) = arr1
  arr(2) = arr2
  arr(3) = arr3
  arr(4) = arr4  

  DumpArrayInfo arr

End Sub
```
