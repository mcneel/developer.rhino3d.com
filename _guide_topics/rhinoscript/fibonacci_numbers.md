---
title: Fibonacci Numbers
description: This guide is a survey of Fibonacci number algorithms in RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/fibonacci
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# Fibonacci Numbers

{{ page.description }}

## Overview

By definition, [Fibonacci numbers](http://en.wikipedia.org/wiki/Fibonacci_number) are a series of numbers where the first two Fibonacci numbers are 0 and 1, and each remaining number is the sum of the previous two.

The formula for calculating Fibonacci numbers is: $$F(n) = F(n-1) + F(n-2)$$

with seed values: $$F(0) = 0$$ and $$F(1) = 1$$

There are a number of methods that one can use to calculate these numbers.  Here are a few...

## Recursion

You can calculate Fibonacci numbers using a recursive function...

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Compute Fibonacci number using recursion
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Fib_1(n)
  If (n < 2) Then
    Fib_1 = n
  Else
    Fib_1 = Fib_1(n-1) + Fib_1(n-2)
  End If
End Function
```

...but, it is not always the fastest method.

## Dynamic Iteration

One of the reasons the recursive algorithm can be slow is we keep recomputing the same subproblems over and over again.  In this iterative approach, we solve each subproblem once and then look up the solution later when we need it instead of repeatedly recomputing it...

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Compute Fibonacci number using dynamic iteration
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Fib_2(n)
  Dim f, i
  If (n < 2) Then
    Fib_2 = n
  Else
    ReDim f(n-1)
    f(0) = 1
    f(1) = 1
    For i = 2 To n - 1
      f(i) = f(i-1) + f(i-2)
    Next
    Fib_2 = f(n-1)
  End If
End Function
```

## Space Complexity Iteration

It turns out that the dynamic iteration can be modified to use a much smaller amount of space. Each step through the loop uses only the previous two values of F(n), so instead of storing these values in an array, we can simply use two variables. This requires some swapping around of values so that everything stays in the appropriate places.

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Compute Fibonacci number using space complexity iteration
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Fib_3(n)
  Dim a, b, c, i
  If (n < 2) Then
    Fib_3 = n
  Else  
    a = 1
    b = 1
    For i = 2 To n -1
      c = a + b
      a = b
      b = c
    Next           
    Fib_3 = b
  End If
End Function
```

## Binet's Formula

Binet's Formula for calculating the nth Fibonacci number is fast because it uses neither recursion nor iteration...

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Compute Fibonacci number using Binet's formula
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function Fib_4(n)
   Fib_4 = Round(((Sqr(5) + 1) / 2) ^ n / Sqr(5))
End Function
```

## Testing

You can use the following test code to benchmark the above functions:

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Tests the Fibonacci functions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TestFibonacci

  Dim s, a, n, i, st, et

  a = Array("Recursion", "Dynamic", "Space", "Binet")
  s = Rhino.GetString("Fibonacci algorithm to use",,a)
  If IsNull(s) Then Exit Sub

  n = Rhino.GetInteger("Number of iterations", 20, 1, 100)
  If IsNull(n) Then Exit Sub

  Select Case s
    ' Iterative
    Case "Recursion"
      st = Timer
      For i = 0 To n - 1
        Rhino.Print Fib_1(i)
      Next
      et = Timer
    ' Recursive
    Case "Dynamic"
      st = Timer
      For i = 0 To n - 1
        Rhino.Print Fib_2(i)
      Next
      et = Timer
    ' Space
    Case "Space"
      st = Timer
      For i = 0 To n - 1
        Rhino.Print Fib_3(i)
      Next
      et = Timer
    'Binet  
    Case Else
      st = Timer
      For i = 0 To n - 1
        Rhino.Print Fib_4(i)
      Next
      et = Timer
  End Select

  Call Rhino.Print(s & " calculation completed in " & FormatNumber(et-st,3) & " seconds.")

End Sub
```

---

## Related Topics

- [Fibonacci Numbers on Wikipedia](http://en.wikipedia.org/wiki/Fibonacci_number)
