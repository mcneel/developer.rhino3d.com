+++
aliases = ["/5/guides/rhinoscript/finding-perfect-squares/", "/6/guides/rhinoscript/finding-perfect-squares/", "/7/guides/rhinoscript/finding-perfect-squares/", "/wip/guides/rhinoscript/finding-perfect-squares/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates how to determine if an integer is a perfect square using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Finding Perfect Squares"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/perfectsquare"
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
