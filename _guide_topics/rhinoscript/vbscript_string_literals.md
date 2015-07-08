---
layout: toc-guide-page
title: VBScript String Literals
author: dale@mcneel.com
categories: ['VBScript Basics']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['RhinoScript']
keywords: ['script', 'Rhino', 'vbscript']
order: 1
---

# VBScript String Literals
{: .toc-title }

In VBScript, you enclose strings with double quote characters, and you use the ampersand (&) operator to concatenate strings. For example:

	Dim s
	s = "Hello"
	s = "Hello" & " Rhino!"

What if you want to assign “Hello Rhino!” (including the quotes) to the variables? In VBScript, you can use two double quote characters to include a double quote character in the string. For example:

	Dim s
	s = "Hello Rhino!"

Alternatively you can use the Chr(34) construct:

	Dim s
	s = Chr(34) & "Hello Rhino" & Chr(34)

Or, to make your code more readable, you can write a function.

	Function Quote(ByVal s)
		Quote = Null
		If (VarType(s) = vbString) Then
			Quote = Chr(34) & CStr(s) & Chr(34)
	End If
	End Function

	'...

	Dim s
	s = Quote("Hello Rhino!")
