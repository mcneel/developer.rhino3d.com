---
layout: toc-guide-page
title: Calculating Permutations
author: dale@mcneel.com
categories: ['Miscellaneous', 'Intermediate']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/permutations
order: 1
---

# Calculating Permutations

This guide discusses how to calculate permutations using RhinoScript.

## Overview

The permutation of a set is the number of ways that the items in the set can be uniquely ordered.  For example, the permutations of the set $$\{1, 2, 3\}$$ are: $$\{1, 2, 3\}$$, $$\{1, 3, 2\}$$, $$\{2, 1, 3\}$$, $$\{2, 3, 1\}$$, $$\{3, 1, 2\}$$, and $$\{3, 2, 1\}$$.

For $$N$$ objects, the number of permutations is $$N$$ (N factorial, or $$1 * 2 * 3 * N$$).

## Example

There are a number of methods for calculating permutation sets.  The implementation below uses an ordered, or lexicographic, permutation algorithm.  This algorithm is based on a a permutation algorithm from the book *Practical Algorithms in C++* by Bryan Flamig.

```vbnet
Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' TestPermute - the Main subroutine
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TestPermute
  Dim arr, n
  'arr = Array("One", "Two", "Three", "Four")
  'arr = Array(1, "Two", 3, "Four")
  arr = Array(1, 2, 3, 4)
  n = UBound(arr) + 1
  Rhino.ClearCommandHistory
  Call Rhino.Print(PermuteCount(n))
  Call Permute(arr, 0, n)
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Permute
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub Permute(ByRef arr, ByVal start, ByVal n)
  Dim i, j
  Call PermutePrint(arr)
  If (start < n) Then
    For i = n-2 To start Step -1
      For j = i+1 To n-1
        Call PermuteSwap(arr, i, j)
        Call Permute(arr, i+1, n)
      Next
      Call PermuteRotate(arr, i, n)
    Next
  End If
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PermutePrint
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub PermutePrint(ByRef arr)
  Dim s, v
  s = ""
  For Each v In arr
    s = s & CStr(v) & vbTab
  Next
  Rhino.Print s
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PermuteSwap
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub PermuteSwap(ByRef arr, ByVal i, ByVal j)
  Dim tmp
  tmp = arr(i)
  arr(i) = arr(j)
  arr(j) = tmp
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PermuteRotate
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub PermuteRotate(ByRef arr, ByVal start, ByVal n)
  Dim tmp, i
  tmp = arr(start)
  For i = start To n-2
    arr(i) = arr(i+1)
  Next
  arr(n-1) = tmp
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PermuteCount (e.g. Factorial)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function PermuteCount(ByVal n)
  If n <= 1 Then
    PermuteCount = 1
  Else
    PermuteCount = n * PermuteCount(n-1)
  End If
End Function
```
