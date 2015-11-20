---
layout: toc-guide-page
title: VBScript String Literals
author: dale@mcneel.com
categories: ['Intermediate']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/stringliterals
order: 1
---

# VBScript String Literals

This brief guide demonstrates how to use string literals in VBScript.

## Overview

In VBScript, you enclose strings with double quote characters, and you use the ampersand (`&`) operator to concatenate strings.  For example:


```vbnet
Dim s
s = "Hello"
s = "Hello" & " Rhino!"
```

What if you want to assign `"Hello Rhino!"` (including the quotes) to the variables?  In VBScript, you can use two double quote characters to include a double quote character in the string.  For example:

```vbnet
Dim s
s = "Hello Rhino!"
```

Alternatively you can use the `Chr(34)` construct:

```vbnet
Dim s
s = Chr(34) & "Hello Rhino" & Chr(34)
```

Or, to make your code more readable, you can write a function...

```vbnet
Function Quote(ByVal s)
	Quote = Null
	If (VarType(s) = vbString) Then
		Quote = Chr(34) & CStr(s) & Chr(34)
End If
End Function

'...

Dim s
s = Quote("Hello Rhino!")
```
