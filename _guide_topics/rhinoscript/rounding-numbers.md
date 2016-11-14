---
title: Rounding Numbers
description: This guide discusses number rounding in RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/rounding
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

You need to round when you want to convert a number of greater precision into a number of lesser precision.  The most common case is when you need to convert a floating-point number into an integer.  There are many different types of rounding: rounding up, rounding down, banker's rounding.  This guide covers many of the common rounding methods and demonstrates those that can be done in VBScript.

## Rounding Down

The simplest form of rounding is truncation.  Any digits after the desired precision are simply ignored.  The `Fix` function is an example of truncation.  For example:

```vbnet
Rhino.Print Fix( 3.5) '  3
Rhino.Print Fix(-3.5) ' -3
```

The `Int` function rounds down to the highest integer less than the value.  Both `Int` and `Fix` act the same way with positive numbers - truncating - but give different results for negative numbers:

```vbnet
Rhino.Print Int( 3.5) '  3
Rhino.Print Int(-3.5) ' -4
```

The `Fix` function is an example of symmetric rounding because it affects the magnitude (absolute value) of positive and negative numbers in the same way.  The `Int` function is an example of asymmetric rounding because it affects the magnitude of positive and negative numbers differently.

RhinoScript has a `Floor` function that truncates positive values, but does not work with negative numbers:

```vbnet
Rhino.Print Rhino.Floor( 3.5) '  3
Rhino.Print Rhino.Floor(-3.5) ' -4
```

## Rounding Up

RhinoScript has a `Ceil` function which always rounds fraction values up (more positive) to the next value.

```vbnet
Rhino.Print Rhino.Ceil( 3.5) '  4
Rhino.Print Rhino.Ceil(-3.5) ' -3
```

VBScript does not have a corresponding round-up function.  However, for negative numbers, both `Fix` and `Int` can be used to round upward, in different ways.

`Fix` rounds towards 0 (up in the absolute sense, but down in absolute magnitude):

```vbnet
Rhino.Print Fix( 3.5) '  3
Rhino.Print Fix(-3.5) ' -3
```

`Int` rounds away from 0 (up in terms of absolute magnitude, but down in the absolute sense):

```vbnet
Rhino.Print Int( 3.5) '  3
Rhino.Print Int(-3.5) ' -4
```

## Arithmetic Rounding

When you always round one direction, the resulting number is not necessarily the closest to the original number.  For example, if you round 1.9 down to 1, the difference is a lot larger than if you round it up to 2.  It is easy to see that numbers from 1.6 to 2.4 should be rounded to 2.

But, what about 1.5, which is equidistant between 1 and 2?  By convention, the half-way number is rounded up.

You can implement rounding half-way numbers in a symmetric fashion, such that -.5 is rounded down to -1, or in an asymmetric fashion, where -.5 is rounded up to 0.

VBScript does not have any functions that do arithmetic rounding.

## Banker's Rounding

When you add rounded values together, always rounding .5 in the same direction results in a bias that grows the more numbers you add together.  One way to minimize the bias is with banker's rounding.

Banker's rounding rounds .5 up sometimes and down sometimes.  The convention is to round to the nearest even number, so that both 1.5 and 2.5 round to 2, and 3.5 and 4.5 both round to 4.  Banker's rounding is symmetric.

In VBScript, the following numeric functions perform banker's rounding: `CByte`, `CInt`, `CLng`, `CCur`, and `Round`.

## Random Rounding

Even banker's rounding can bias totals. You can take an extra step to remove bias by rounding .5 up or down in a truly random fashion.  This way, even if the data is deliberately biased, bias might be minimized.  However, using random rounding with randomly distributed data might result in a larger bias than banker's rounding.  Random rounding could result in two different totals on the same data.

VBScript does not have any functions that do random rounding.

## Alternate Rounding

Alternate rounding is rounding between .5 up and .5 down on successive calls.

VBScript does not have any functions that do alternate rounding.

## Round to Nearest

Imagine you want to create a script that rounds a number up or down by a specified increment.  For example, given the number 3.23, rounding to the nearest .05 results in the number 3.25.  The example below accepts any positive rounding increment as a parameter.  In addition to rounding numbers to the nearest fractional amount, you can also round to whole numbers, such as 1, 10, or 100...

```vbnet
' Function:
'   RoundToNearest
' Description
'   Rounds a number by an increment
' Parameters:
'   Amt (Number) - number to round
'   RoundAmt (Number) - increment to which Amt will be rounded
'   bRoundUp (Boolean) - rounding direction (up or down)
'
Function RoundToNearest(Amt, RoundAmt, bRoundUp)
  On Error Resume Next
  Dim Temp : Temp = Amt / RoundAmt
  If Int(Temp) = Temp Then
    RoundToNearest = Amt
  Else
    If (bRoundUp = True) Then
     Temp = Int(Temp) + 1
    Else
     Temp = Int(Temp)
    End If
    RoundToNearest = Temp * RoundAmt
  End If
End Function
```

The above script can be used as follows...

```
MsgBox RoundToNearest(1.36, 0.25, True)
MsgBox RoundToNearest(1.36, 0.05, False)
MsgBox RoundToNearest(1.36, 0.75, True)
```

## Kitchen Sink

The code that follows provides sample implementations for each of the rounding types described.

All these functions take two arguments: the number to be rounded and a factor.  If the factor is 1, then the functions return an integer created by one of the above methods.  If the factor is something other than 1, the number is scaled by the factor to create different rounding effects. For example AsymArith(2.55, 10) produces 2.6, that is, it rounds to 1/factor = 1/10 = 0.1.

**NOTE**: a factor of 0 generates a run-time error: 1/factor = 1/0.

```vbnet
' Asymmetrically rounds numbers down - similar to Int().
' Negative numbers get more negative.
Function AsymDown(X, Factor)
  AsymDown = Int(X * Factor) / Factor
End Function

' Symmetrically rounds numbers down - similar to Fix().
' Truncates all numbers toward 0.
' Same as AsymDown for positive numbers.
Function SymDown(X, Factor)
  SymDown = Fix(X * Factor) / Factor
End Function

' Asymmetrically rounds numbers fractions up.
' Same as SymDown for negative numbers.
' Similar to Rhino.Ceil().
Function AsymUp(X, Factor)
  Dim Temp
  Temp = Int(X * Factor)
  AsymUp = (Temp + IIf(X = Temp, 0, 1)) / Factor
End Function

' Symmetrically rounds fractions up - that is, away from 0.
' Same as AsymUp for positive numbers.
' Same as AsymDown for negative numbers.
Function SymUp(X, Factor)
  Dim Temp
  Temp = Fix(X * Factor)
  SymUp = (Temp + IIf(X = Temp, 0, Sgn(X))) / Factor
End Function

' Asymmetric arithmetic rounding - rounds .5 up always.
Function AsymArith(X, Factor)
  AsymArith = Int(X * Factor + 0.5) / Factor
End Function

' Symmetric arithmetic rounding - rounds .5 away from 0.
' Same as AsymArith for positive numbers.
Function SymArith(X, Factor)
  SymArith = Fix(X * Factor + 0.5 * Sgn(X)) / Factor
End Function

' Banker's rounding.
' Rounds .5 up or down to achieve an even number.
' Symmetrical by definition.
Function BRound(X, Factor)
  Dim Temp, FixTemp
  Temp = X * Factor
  FixTemp = Fix(Temp + 0.5 * Sgn(X))
  If Temp - Int(Temp) = 0.5 Then
    If FixTemp / 2 <> Int(FixTemp / 2) Then
      FixTemp = FixTemp - Sgn(X)
    End If
  End If
  BRound = FixTemp / Factor
End Function

' Random rounding.
' Rounds .5 up or down in a random fashion.
' (Execute Randomize statement somewhere prior to calling.)
Function RandRound(X, Factor)
  Dim Temp, FixTemp
  Temp = X * Factor
  FixTemp = Fix(Temp + 0.5 * Sgn(X))
  If Temp - Int(Temp) = 0.5 Then
    FixTemp = FixTemp - Int(Rnd * 2) * Sgn(X)
  End If
  RandRound = FixTemp / Factor
End Function

' Alternating rounding.
' Alternates between rounding .5 up or down.
Public fReduce
Function AltRound(X, Factor)
  Dim Temp, FixTemp
  If IsEmpty(fReduce) Then fReduce = False
  Temp = X * Factor
  FixTemp = Fix(Temp + 0.5 * Sgn(X))
  If Temp - Int(Temp) = 0.5 Then
    If (fReduce And Sgn(X) = 1) Or (Not fReduce And Sgn(X) = -1) Then
      FixTemp = FixTemp - Sgn(X)
    End If
    fReduce = Not fReduce
  End If
  AltRound = FixTemp / Factor
End Function
```

Note, many of these sample functions require the following utility function...

```vbnet
' VBScript equivalent to VB's Immediate If function.
Function IIf(expr, true_val, false_val)
  If expr Then
    IIf = true_val
  Else
    IIf = false_val
  End If
End Function
```

The following table shows the effects of various factors:

| Expression | | | |  Result | | | | Comment |
|:--------|:-:|:-:|:-:|:-------:|:-:|:-:|:-:|:--------|
| `AsymArith(2.5)`   | | | | 3   | | | | Rounds up to next integer.   |
| `BRound(2.18, 20)`   | | | | 2.2   | | | | Rounds to the nearest 1/20.   |
| `SymDown(25, .1)`   | | | | 20   | | | | Rounds down to an even multiple of 10.   |
|=====
|
{: rules="groups"}

## Floating point Limitations

All the rounding implementations presented here use the double data type, which can represent approximately 15 decimal digits.

Since not all fractional values can be expressed exactly, you might get unexpected results because the display value does not match the stored value.

For example, the number 2.25 might be stored internally as 2.2499999..., which would round down with arithmetic rounding, instead of up as you might expect.  Also, the more calculations a number is put through, the greater possibility that the stored binary value will deviate from the ideal decimal value.

## Dropping Precision

As taught in school, rounding is usually arithmetic rounding using positive numbers.  With this type of rounding, you only need to know the number to 1 digit past where you are rounding to.  You ignore digits past the first decimal place.  In other words, precision is dropped as a shortcut to rounding the value.

For example, both 2.5 and 2.51 round up to 3, while both 2.4 and 2.49 round down to 2.

When you use banker's rounding (or other methods that round .5 either up or down) or when you round negative numbers using asymmetric arithmetic rounding, dropping precision can lead to incorrect results where you might not round to the nearest number.

For example, with banker's rounding, 2.5 rounds down to 2 and 2.51 rounds up to 3.

With asymmetric arithmetic rounding, -2.5 rounds up to -2 while -2.51 rounds down to -3.

The user-defined functions presented in this guide take the number's full precision into account when performing rounding.
