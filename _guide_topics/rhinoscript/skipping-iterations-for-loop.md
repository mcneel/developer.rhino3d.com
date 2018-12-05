---
title: Skipping current iteration in a For loop
description: This guide demonstrates how to skip the current iteration in a For Loop.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: https://wiki.mcneel.com/developer/scriptsamples/vbcontinue
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---


## Problem

Both the C++ and C# programming languages have a ```continue``` statement that, when used with a ```For``` loop, skips the remaining statements of that iteration and moves on to next iteration. Does VBScript have anything like this?

## Solution

There is no ```continue``` or continue-like statement in VBScript. But using a ```Do While loop``` inside of a ```For Each``` statement, you can achieve the same functionality. For example:

```vbnet
For i = 0 To 10
  Do
    If i = 4 Then Exit Do
    Rhino.Print i
  Loop While False
Next
```
Here is another example:
```vbnet
Sub TestContinue
 
  Dim arrTests, arrTest
 
  arrTests = Array( _
        Array(1) _
      , Array(1,2,3 ) _
      , Array(1,2) _
      , Array(1) _
      , Array(1,2,3) _
      )
 
  For Each arrTest In arrTests
     Call Rhino.Print("Process: {" & Join(arrTest, ", ") & "}")
     Do While True ' Continue trick
       Call Rhino.Print(" Process: " & arrTest(0))
       If 0 = UBound(arrTest) Then Exit Do ' Continue
       Call Rhino.Print(" Process: " & arrTest(1))
       If 1 = UBound(arrTest) Then Exit Do ' Continue
       Call Rhino.Print(" Process: " & arrTest(2))
       Exit Do
     Loop
  Next
 
End Sub
```
