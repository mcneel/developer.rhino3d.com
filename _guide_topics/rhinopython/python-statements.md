---
title: Python Basic Syntax
description: This guide presents an overview of Python syntax.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Fundamentals']
origin:
order: 1
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

 
## Overview

Many scripting and programming languages, such as JScript, C#, and C++, make no attempt to match the code that is run with the actual physical lines typed into the text editor.  This is because they not recognize the end of a line of code until it sees the termination character (in these cases, the semicolon).  Thus, the actual physical lines of type taken up by the code are irrelevant.

Unlike other languages, Python does not use an end of line character. Most of the time a simple <kbd>Enter</kbd> will do. Yet, Python is very peticular about indentation, spaces and lines in certain cases.  This document is to help understand Python formatting. 

It is important to understand how Python interperates:

2. End of Statement
1. Names and Capitalization
2. Comments
3. Block Structures
4. Tabs and Spaces

For the official very detailed documentation on Python Syntax, see the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## End of Statements

To end a statement in Python, you do not have to type in a semicolon or other special character; you simply press <kbd>Enter</kbd>.  For example, this code will generate a syntax error:

```python
var1
=
'John'
```

This will not:

```python
var1 = 'john'
```

In general, the lack of a required statement termination character simplifies script writing in Python.  There is, however, one complication: To enhance readability, it is recommended that you limit the length of any single line of code to 79 characters.  What happens, then, if you have a line of code that contains 100 characters?

Although it might seem like the obvious solution, you cannot split a statement into multiple lines simply by entering a carriage return. For example, the following code snippet returns a run-time error in Python because a statement was split by using <kbd>Enter</kbd>.

```python
  strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " & strUserLastName
  Rhino.Print strMessageToDisplay
```

You cannot split a statement into multiple lines in VBScript by pressing <kbd>Enter</kbd>. Instead, use the backslash (`\`) to indicate that a statement is continued on the next line.  In the revised version of the script, a blank space and an underscore indicate that the statement that was started on line 1 is continued on line 2.  To make it more apparent that line 2 is a continuation of line 1, line 2 is also indented four spaces.  (This was done for the sake of readability, but you do not have to indent continued lines.)

```python
  strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " \ & strUserLastName
  Rhino.Print strMessageToDisplay
```

Line continuation is automatic is the line split comes while in a statement inside paranthesis ((), brackets ([) or braces ({).  This is convinient, but can also lead to errors if there is no closing Partnthesis, bracket or brace.  Python would interperte the rest of the script as one statement in that case.

Python uses single quotes (') double quotes (") and triple quotes (""") to denote literal strings.  Only the triple quoted strings (""") also will automatically contiue across the end of line statement.

Sometime, more then one statement may be put on a single line.  In Python a semicolon (;) can be used to seperate multiple startments on the same line.  For instance three statements can be written:

```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```

To the Python interpreter, this would be the same set of statememts:

```python
import sys
x = 'foo'
sys.stdout.write(x + '\n')
```
