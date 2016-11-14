---
title: Finding Perfect Squares
description: This guide demonstrates how to determine if an integer is a perfect square using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/perfectsquare
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Problem

In mathematics, a perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.  For example, 9 is a perfect square, since it can be written as 3 × 3. How can one determine whether or not an integer is a perfect square in RhinoScript?

## Solution

Here is an example of a function that determines whether or not a number is a perfect square:

```vbnet
Function IsPerfectSquare(n)

  Dim h, t

  IsPerfectSquare = False ' default return value

  h = n And &HF ' last hexadecimal "digit"
  If (h > 9) Then Exit Function ' return immediately in 6 cases out of 16

  If (h <> 2 And h <> 3 And h <> 5 And h <> 6 And h <> 7 And h <> 8) Then
    t = Int(Rhino.Floor(Sqr(n)+0.5))
    If (t*t = n) Then IsPerfectSquare = True
  End If

End Function
```

You can test the above function as follows:

```vbnet
For i = 0 To 60^2
  If IsPerfectSquare(i) Then
    Call Rhino.Print(CStr(i) & "^2 = " & CStr(i^2))
  End If
Next
```
