---
title: Disposing of Variables
description: This guide discusses VBScript variables, their scope, and how to clean them up.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/dispose
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

VBScript’s garbage collector runs at the end of every statement and procedure, and does not do a search of all memory. Rather, it keeps track of everything allocated in the statement or procedure; if anything has gone out of scope, it frees it immediately.

Global variables, ones declared outside of a procedure, do not go out of scope until VBScript is reset or destroyed. Thus, for memory efficiency, it is best not use global variables.

With this said, one can conclude that it is more memory efficient to write scripts that contain a number of small, efficient procedures, so variables that are no longer needed are garbage collected, than it is to write a single, massive procedure.

But, sometimes is neither possible nor convenient to write a script in a granular fashion. In such cases, it is possible to manually clean up unused objects and variables along the way to keep your single, massive procedure memory efficient.

## Example

The following example demonstrates how to create a single procedure that is capable of cleaning up a number of different variable types. The idea is that when a variable is no longer needed, you can call a single procedure to clean it up, thus making your scripts use less memory.

For example, lets say your script used an array variable to store a massive amount of data. When you were finished with the variable, you could dispose of the array, and recover its memory, like this:

```vbnet
Call Dispose(arr)
```

This examples cleans up dictionary objects, arrays, and simple variables. But, it could be extended to include other types of objects, such as file streams, database recordsets, or user-defined class objects.

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Dispose.rvb -- April 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

' Disposes of dictionaries, arrays, and variables
Sub Dispose(ByRef obj)
  If IsObject(obj) Then
    If LCase(TypeName(obj)) = "dictionary" Then
     obj.RemoveAll ' Remove all key, item pairs
    End If
    Set Obj = Nothing ' Disassociate
  ElseIf IsArray(obj) Then
    Erase obj ' Clear the array
  End If
  obj = Empty ' Uninitialize
End Sub
```


---

## Related Topics

- [VBScript Variables]({{ site.baseurl }}/guides/rhinoscript/vbscript_variables)
