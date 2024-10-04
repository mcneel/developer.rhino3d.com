+++
aliases = ["/en/5/guides/rhinoscript/vbscript-procedures/", "/en/6/guides/rhinoscript/vbscript-procedures/", "/en/7/guides/rhinoscript/vbscript-procedures/", "/wip/guides/rhinoscript/vbscript-procedures/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses VBScript procedures."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "VBScript Procedures"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/vbsprocedures"
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

In VBScript, there are two kinds of procedures; the `Sub` procedure and the `Function` procedure.

## Sub Procedures

A `Sub` procedure is a series of VBScript statements (enclosed by `Sub` and `End Sub` statements) that perform actions but don't return a value.  A `Sub` procedure can take arguments (constants, variables, or expressions that are passed by a calling procedure).  If a `Sub` procedure has no arguments, its `Sub` statement should include an empty set of parentheses `()`.

The following `Sub` procedure uses two intrinsic, or built-in, VBScript functions, MsgBox and InputBox, to prompt a user for information.  It then displays the results of a calculation based on that information. The calculation is performed in a `Function` procedure created using VBScript.  The `Function` procedure is shown after the following discussion.

```vbnet
Sub ConvertTemp()
	temp = InputBox("Please enter the temperature in degrees F.", 1)
	MsgBox "The temperature is " & Celsius(temp) & " degrees C."
End Sub
```

## Function Procedures

A `Function` procedure is a series of VBScript statements enclosed by the `Function` and End `Function` statements.  A `Function` procedure is similar to a `Sub` procedure, but can also return a value.  A `Function` procedure can take arguments (constants, variables, or expressions that are passed to it by a calling procedure).  If a `Function` procedure has no arguments, its `Function` statement should include an empty set of parentheses.  A `Function` returns a value by assigning a value to its name in one or more statements of the procedure.  The return type of a `Function` is always a Variant.

In the following example, the Celsius `Function` calculates degrees Celsius from degrees Fahrenheit. When the `Function` is called from the `ConvertTemp` `Sub` procedure, a variable containing the argument value is passed to the `Function`.  The result of the calculation is returned to the calling procedure and displayed in a message box.

```vbnet
Sub ConvertTemp()
	temp = InputBox("Please enter the temperature in degrees F.", 1)
	MsgBox "The temperature is " & Celsius(temp) & " degrees C."
End Sub

Function Celsius(fDegrees)
	Celsius = (fDegrees - 32) * 5 / 9
End Function
```

## Getting Data In and Out

Each piece of data is passed into your procedures using an argument.  Arguments serve as placeholders for the data you want to pass into your procedure.  You can name your arguments any valid variable name.  When you create a procedure using either the `Sub` statement or the `Function` statement, parentheses must be included after the name of the procedure.  Any arguments are placed inside these parentheses, separated by commas.  For example, in the following example, `fDegrees` is a placeholder for the value being passed into the Celsius function for conversion.

```vbnet
Function Celsius(fDegrees)
	Celsius = (fDegrees - 32) * 5 / 9
End Function
```

To get data out of a procedure, you must use a `Function`.  Remember, a `Function` procedure can return a value; a `Sub` procedure cannot.

## Sub and Function

A `Function` in your code must always be used on the right side of a variable assignment or in an expression.  For example:

```vbnet
Temp = Celsius(fDegrees)
```

or

```vbnet
MsgBox "The Celsius temperature is " & Celsius(fDegrees) & " degrees."
```

To call a `Sub` procedure from another procedure, type the name of the procedure along with values for any required arguments, each separated by a comma.  The `Call` statement is not required, but if you do use it, you must enclose any arguments in parentheses.

The following example shows two calls to the `MyProc` procedure.  One uses the `Call` statement in the code; the other does not. Both do exactly the same thing.

```vbnet
Call MyProc(firstarg, secondarg)
MyProc firstarg, secondarg
```

Notice that the parentheses are omitted in the call when the `Call` statement is not used.

## Related Topics

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)
- [Parentheses](/guides/rhinoscript/parentheses)
