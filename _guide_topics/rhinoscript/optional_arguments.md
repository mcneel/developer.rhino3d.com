---
title: Optional Arguments
description: This guide demonstrates how to implement optional arguments in VBScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/optionalarguments
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

It is not uncommon to want to make an argument of a VBScript function or subroutine optional.  In VBScript, the `Optional` keyword, which allows some arguments to be left out in Visual Basic, is not implemented.  This means that you must declare every argument that you want to use.

What you can do is pass null values to your functions.  For example:

```vbnet
Function SomeArgs(one, two, three, four)
  SomeArgs = one & two & three & four
End Function

Call SomeArgs(1, 2, 3, Null)
```

## Discussion

To work around this limitation, you can use an array-based approach to simulate optional arguments. To see how to use the array-based approach for creating subroutines with optional arguments, consider the following example:

```vbnet
Sub MySubroutine(arrArgs)

  ' Declare local variables
  Dim v1, v2, v3, v4

  ' Initialize the local variables with default values
  v1 = 1 : v2 = 2 : v3 = 3 : v4 = 4

  Select Case UBound(arrArgs)
    Case 0
      v1 = arrArgs(0)  
    Case 1
      v1 = arrArgs(0)
      v2 = arrArgs(1)
    Case 2
      v1 = arrArgs(0)
      v2 = arrArgs(1)
      v3 = arrArgs(2)
    Case 3
      v1 = arrArgs(0)
      v2 = arrArgs(1)
      v3 = arrArgs(2)
      v4 = arrArgs(3)
    Case Else
      Exit Sub
  End Select

  Rhino.Print "v1  = " & CStr(v1)
  Rhino.Print "v2  = " & CStr(v2)
  Rhino.Print "v3  = " & CStr(v3)
  Rhino.Print "v4  = " & CStr(v4)

End Sub
```

Notice in the subroutine declaration, only defined one argument has been defined:

```vbnet
 Sub MySubroutine(arrArgs)
```

The argument will be an array of values we would like to pass into the subroutine.  The next few lines declare local variables and initializes them to default values (simple numbers, in this case).  Next, use the `UBound()` function to determine the number of arguments passed.  Then assign the array elements to the local variables:

```vbnet
Select Case UBound(arrArgs)
  Case 0
    v1 = arrArgs(0)
  Case 1
    v1 = arrArgs(0)
    v2 = arrArgs(1)
  Case 2
    v1 = arrArgs(0)
    v2 = arrArgs(1)
    v3 = arrArgs(2)
  Case 3
    v1 = arrArgs(0)
    v2 = arrArgs(1)
    v3 = arrArgs(2)
    v4 = arrArgs(3)
  Case Else
    Exit Sub
End Select
```

Since the array is zero-based, the first case branch assigns the first element to our v1 variable.  As more arguments to the function are needed, one can easily add more case branches.

To call this subroutine, create an array of the size based on the number of arguments you want to pass into the function, and then populate this array with the values you want to pass to the function:

```vbnet
' Create the array to pass to MySubroutine
Dim arrArgs

' Call the subroutine with two arguments
Redim arrArgs(1)
arrArgs(0) = Value1
arrArgs(1) = Value2

Call MySubroutine(arrArgs)
```

Alternatively...

```vbnet
' Call MySubroutine with three arguments
Call MySubroutine(Array(Value1, Value2, Value3))
```
