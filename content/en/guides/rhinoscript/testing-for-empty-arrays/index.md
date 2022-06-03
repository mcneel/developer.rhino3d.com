+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide discusses how to determine a VBScript array is empty."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Testing for Empty Arrays"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/emptyarray"
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

It is often necessary to analyze an array to determine whether or not it is empty; that is, if it has any space to store elements.  Consider the following test...

```vbnet
Sub Main()
  Dim arr
  arr = Array()
  If IsArray(arr) Then
    Rhino.Print("This should not print")
  End If    
End Sub
```

...which does not seem to work.

## Solution

When you execute this statement:

```vbnet
arr = Array()
```

you are declaring an array that has an upper bounds of -1.  Because this variable is an array, it will pass the `IsArray()` test.  What the above code needs is an additional test condition to see if the upper bounds of the array is greater than -1:

```vbnet
Sub Main()
  Dim arr
  arr = Array()
  If IsArray(arr) And UBound(arr) >= 0 Then
    Rhino.Print("This should not print")
  End If    
End Sub
```

Now the code works as expected.  But, what if the code looked like this?

```vbnet
Sub Main()
  Dim arr()
   If IsArray(arr) And UBound(arr) >= 0 Then
    Rhino.Print("This should not print")
  End If    
End Sub
```

Notice that the above code gives you an "Script out of range: UBound" error.  This is because, although the variable is an array, it has not been dimensioned.  Thus the call to `UBound()` fails.  So, we need a better test - one that will test for both types of array declarations.  Consider the following function:

```vbnet
Function IsArrayDimmed(arr)
  IsArrayDimmed = False
  If IsArray(arr) Then
    On Error Resume Next
    Dim ub : ub = UBound(arr)
    If (Err.Number = 0) And (ub >= 0) Then IsArrayDimmed = True
  End If  
End Function
```

Notice how the function above provides error checking.  If an error occurs when calling `UBound()`, it is caught. Thus, the function knows when an array has not been dimensioned.  Also, if `UBound()` returns a value of -1, we know that the array has no space to store elements.  We can test this with the following function:

```vbnet
Sub Main()
  Dim arr0
  Dim arr1()
  Dim arr2(3)
  Dim arr3 : arr3 = Array()
  Dim arr4 : arr4 = Array(1,2,3)
  Rhino.Print "Arr0 dimmed = " &  IsArrayDimmed(arr0)
  Rhino.Print "Arr1 dimmed = " &  IsArrayDimmed(arr1)
  Rhino.Print "Arr2 dimmed = " &  IsArrayDimmed(arr2)
  Rhino.Print "Arr3 dimmed = " &  IsArrayDimmed(arr3)
  Rhino.Print "Arr4 dimmed = " &  IsArrayDimmed(arr4)
End Sub
```
