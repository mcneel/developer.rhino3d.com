---
title: Python Procedures
description: This guide discusses VBScript procedures.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac' 'Windows']
categories: ['Fundamentals']
origin: 
order: 2
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

 
## Overview

In Python a function is a named block of code that can perform a reusable action.  This allows Ptyhon code to be brocken down into functional, resuable blocks of code.

## User-Defined Procedures

A `Function` is a series of Python statements begins by a `def`, followed by the function name and enclosed in parenthesis. A Function may or may not return a value.  A `Function` procedure can take arguments (constants, variables, or expressions that are passed by a calling procedure).  If a `Function` procedure has no arguments, its `def` statement should include an empty set of parentheses `()`.  Parameters can also be defined within the paranthesis.  The parenthesis are followed by a colon (:) to end the first line.

The end of the function is marked by the loss of whitespace in the next line of the code (ending the code block). It is common practice to use a `return` statement followed by the arguement to return a value. You amay also finish a funtion with a return stanement and a simple colon (;).

In the following example, the Celsius `def` calculates degrees Celsius from degrees Fahrenheit. When the `def` is called from the `ConvertTemp` `def` procedure, a variable containing the argument value is passed to the `def`.  The result of the calculation is returned to the calling procedure and displayed in a message box.

```python
def Celsius(fDegrees):
	_Celsius = (fDegrees - 32) * 5 / 9
    return _Celsius;

# Use this code to call the Celsius function
temp = raw_input("Please enter the temperature in degrees F.", 1)
MsgBox "The temperature is " & Celsius(temp) & " degrees C."

```

## Getting Data In and Out

Each piece of data is passed into your procedures using an argument.  Arguments serve as placeholders for the data you want to pass into your procedure.  You can name your arguments any valid variable name.  When you create a procedure parentheses must be included after the name of the procedure.  Any arguments are placed inside these parentheses, separated by spaces.  For example, in the following example, `fDegrees` is a placeholder for the value being passed into the Celsius function for conversion.

```python
Function Celsius(fDegrees)
	_Celsius = (fDegrees - 32) * 5 / 9
    return _Celsius;
```

To call a `Sub` procedure from another procedure, type the name of the procedure along with values for any required arguments, each separated by a space. 

The function will returns a single value based on its final `return` statement. A return statement with a variable name, followed by a semicolon (;) returns the reference to that variable. A return statement with simply a semicolon (;) returns nothing. The return statement is not required to end a proceedure.

---

## Related Topics

- [What are Python and RhinoScriptSyntax?]({{ site.baseurl }}/guides/rhinopython/what-is-rhinopython)
- [Additional information onf Functions in Python](https://www.tutorialspoint.com/python/python_functions.htm)
