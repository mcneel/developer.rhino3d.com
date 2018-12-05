---
title: Uncommon Numeric Conversions
description: This brief guide demonstrates some useful (or not so useful) numeric conversions in RhinoScript.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/uncommonconversions
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Hexadecimal

This function converts numbers to their hexadecimal representation...

```vbnet
Function CHex(intNumber)

 Dim strChars, intSign

 strChars = "0123456789ABCDEF"
 intSign = Sgn(intNumber)

 intNumber = Fix(Abs(CDbl(intNumber)))
 If (intNumber = 0) Then
   CHex = "0"
   Exit Function
 End If

 While (intNumber > 0)
   CHex = Mid(strChars, 1 + (intNumber - 16 * Fix(intNumber / 16)), 1) & CHex
   intNumber = Fix(intNumber / 16)
 Wend

 If (intSign = -1) Then CHex = "-" & CHex

End Function
```

and can be used to...

```vbnet
Rhino.Print CHex(2008) '7D8
```

## Binary

The following function converts numbers to their binary representation...

```vbnet
Function CBinary(intNumber, intBits)

  Dim strBinary, intMask, i

  strBinary =
  intMask = 1

  For i = 1 To intBits
    If (intNumber And intMask) Then
      strBinary = "1" & strBinary
    Else
      strBinary = "0" & strBinary
    End If
    intMask = intMask * 2
  Next

  CBinary = strBinary

End Function
```

and can be used to...

```vbnet
Rhino.Print CBinary(2008, 16) '0000011111011000
```

## Roman Numerals

The following function converts numbers to their Roman numeral representation...

```vbnet
Function CRoman(intNumber)

  Dim v, w, x, y, arrOnes, arrTens, arrHund, arrThou

  arrOnes = Array(,"I","II","III","IV","V","VI","VII","VIII","IX")
  arrTens = Array(,"X","XX","XXX","XL","L","LX","LXX","LXXX","XC")
  arrHund = Array(,"C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
  arrThou = Array(,"M","MM","MMM","MMMM","MMMMM")

  v = ((intNumber - (intNumber Mod 1000)) / 1000)
  intNumber = (intNumber Mod 1000)

  w = ((intNumber - (intNumber Mod 100)) / 100)
  intNumber = (intNumber Mod 100)

  x = ((intNumber - (intNumber Mod 10)) / 10)

  y = (intNumber Mod 10)

  CRoman = arrThou(v) & arrHund(w) & arrTens(x) & arrOnes(y)

End Function
```

and can be used to...

```vbnet
Rhino.Print CRoman(2008) 'MMVIII
```

## Roman Numeral to Base 10

The following function converts Roman numeral representations to their base 10 representation...

```vbnet
Function CUnRoman(strRoman)

  Dim intvalue, strChar, i
  intValue = 0

  If InStr(strRoman, "CM") Then
    intValue = intValue + 900
    strRoman = Replace(strRoman, "CM", )
  End If

  If InStr(strRoman, "CD") Then
    intValue = intValue + 400
    strRoman = Replace(strRoman, "CD", )
  End If

  If InStr(strRoman, "XC") Then
    intValue = intValue + 90
    strRoman = Replace(strRoman, "XC", )
  End If

  If InStr(strRoman, "XL") Then
    intValue = intValue + 40
    strRoman = Replace(strRoman, "XL", )
  End If

  If InStr(strRoman, "IX") Then
    intValue = intValue + 9
    strRoman = Replace(strRoman, "IX", )
  End If

  If InStr(strRoman, "IV") Then
    intValue = intValue + 4
    strRoman = Replace(strRoman, "IV", )
  End If

  For i = 1 To Len(strRoman)
    strChar = Mid(strRoman, i, 1)
    Select Case strChar
      Case "I" intValue = intValue + 1
      Case "V" intValue = intValue + 5
      Case "X" intValue = intValue + 10
      Case "L" intValue = intValue + 50
      Case "C" intValue = intValue + 100
      Case "D" intValue = intValue + 500
      Case "M" intValue = intValue + 1000
    End Select
  Next

  CUnRoman = intValue

End Function
```

and can be used to...

```vbnet
Rhino.Print CUnRoman(MMVIII) '2008
```
