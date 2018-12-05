---
title: Multidimensional Arrays
description: This guide discusses rectangular and ragged multidimensional arrays.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/multidimensional
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

VBScript supports two kinds of multidimensional arrays, called rectangular and ragged.  Why are there two types of multidimensional arrays? What is the difference between the (x)(y) and (x,y) notation?  We will cover these questions as well as talk about resizing multidimensional arrays.

## Rectangular

A rectangular array is, well, "rectangular."  For example:

```vbnet
Dim MyArray(3,2)
```

and you get:

```vbs
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
(3,0) (3,1) (3,2)
```

which makes a nice rectangle. A three-dimensional array makes a rectangular prism, and so on up into the higher dimensions.

## Ragged

A common practice used by RhinoScript is to simulate multidimensional arrays by making an array of arrays known as ragged or nested arrays.  For example:

```vbnet
Dim MyArray
MyArray = Array(Array(1, 2, 3), Array(4, 5), Array(6, 7, 8, 9))
```

And so dereferencing the outer array gives you the inner array, which can then be dereferenced itself:

```vbnet
Rhino.Print MyArray(2)(0) ' 6
```

But, you notice something about the indices if we write them out as before:

```vbs
(0)(0) (0)(1) (0)(2)
(1)(0) (1)(1)
(2)(0) (2)(1) (2)(2) (2)(3)
```

The indices make a ragged pattern, not a straight rectangular pattern.  It is possible to create ragged higher dimensional, but allocating all the sub-arrays can be difficult.

Thus, in VBScript if you say:

```vbnet
MyArray(2,3)
```

then you are talking to a rectangular two-dimensional array.  And, if you say:

```vbnet
MyArray(2)(3)
```

then you are talking to a one dimensional array that contains another one dimensional array.

## Resizing

The `ReDim` statement is used to size or resize a dynamic array that has already been formally declared using a `Private`, `Public`, or `Dim` statement with empty parentheses (without dimension subscripts).  You can use the `ReDim` statement repeatedly to change the number of elements and dimensions in an array.

If you use the `Preserve` keyword, you can resize only the last array dimension, and you can't change the number of dimensions at all.  For example, if your array has only one dimension, you can resize that dimension because it is the last and only dimension.  However, if your array has two or more dimensions, you can change the size of only the last dimension and still preserve the contents of the array.

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>If you make an array smaller than it was originally, data in the eliminated elements is lost.</p>
</div>

The following example shows how you can increase the size of the last dimension of a dynamic array without erasing any existing data contained in the array.

```vbnet
ReDim arr(10, 10, 10)
...
ReDim Preserve arr(10, 10, 15)
```
