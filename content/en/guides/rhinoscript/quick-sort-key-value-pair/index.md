+++
aliases = ["/5/guides/rhinoscript/quick-sort-key-value-pair/", "/6/guides/rhinoscript/quick-sort-key-value-pair/", "/7/guides/rhinoscript/quick-sort-key-value-pair/", "/wip/guides/rhinoscript/quick-sort-key-value-pair/"]
authors = [ "david" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to sort an array of key-value pairs in RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Quick Sort Key Value Pairs"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/quicksortkeyvaluepair"
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

The .NET Framework's `SortedList` class provides a hash table with automatically sorted key-value pairs.  The available methods and properties for `SortedList` are very similar to the ones available in [ArrayList](/guides/rhinoscript/sorting-vbs-arrays-with-net).

The following sample code creates a `SortedList` and populates it with some key-value pairs:

```vbnet
Set SortedList = CreateObject("System.Collections.Sortedlist")
SortedList.Add "First", "Hello"
SortedList.Add "Second", ","
SortedList.Add "Third", "Rhino"
SortedList.Add "Fourth", "!"

For i = 0 To SortedList.Count - 1
  Rhino.Print SortedList.GetKey(i) & vbTab & SortedList.GetByIndex(i)
Next
```

**NOTE**: `SortedList` only sorts the list by keys. It is not possible to sort the list by values.

## Quick Sort

VBScript and RhinoScript do not expose procedures for sorting multiple arrays.  The .NET framework does, but only a single Key-Value pair.  The algorithm outlined on below can be easily extended to work for any number of value arrays.  It is a standard implementation of the [QuickSort](http://en.wikipedia.org/wiki/Quicksort) algorithm.

QuickSort works through a [Divide and Conquer](http://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) approach and it's one of the fastest sorting algorithms available.  However, this implementation uses the recursive approach which may result in stack overflow errors on large datasets.  QuickSort works best on randomized arrays, if the array is already almost sorted the solution will take more steps.

This implementation comes as a collection of three procedures, but it can be easily packaged into one.

First, the big one.  This is the actual recursive algorithm:

```vbnet
Sub QuickSort(ByRef A(), ByRef B(), ByVal min, ByVal max)
  Dim i : i = min
  Dim k : k = max

  If (max - min) >= 1 Then
    Dim pivot : pivot = A(min)

    While (k > i)
      While (A(i) <= pivot And i <= max And k > i)
        i = i+1
      Wend

      While (A(k) > pivot And k >= min And k >= i)
        k = k-1
      Wend

      If (k > i) Then Call SwapElements(A, B, i, k)
    Wend

    Call SwapElements(A, B, min, k)
    Call QuickSort(A, B, min, k-1)
    Call QuickSort(A, B, k+1, max)
  End If
End Sub
```

It depends on the `SwapElement()` subroutine, which could have been written inline, but since it is called twice, it is placed in a a separate subroutine:

```vbnet
Sub SwapElements(ByRef A(), ByRef B(), ByVal i0, ByVal i1)
  Dim loc_A : loc_A = A(i0)
  Dim loc_B : loc_B = B(i0)

  A(i0) = A(i1)
  B(i0) = B(i1)
  A(i1) = loc_A
  B(i1) = loc_B
End Sub
```

Finally, there's a wrapper procedure that makes calling this function slightly easier:

```vbnet
Function SortByKey(ByRef Keys(), ByRef Values())
  Call QuickSort(Keys, Values, 0, Ubound(Keys))
End Function
```

## Related Topics

- [Sorting VBS Arrays with .NET](/guides/rhinoscript/sorting-vbs-arrays-with-net)
- [Quicksort on Wikipedia](http://en.wikipedia.org/wiki/Quicksort)
- [Divide and conquer algorithms on Wikipedia](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithms)
