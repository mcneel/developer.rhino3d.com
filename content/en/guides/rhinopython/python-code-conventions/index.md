+++
aliases = ["/en/5/guides/rhinopython/python-code-conventions/", "/en/6/guides/rhinopython/python-code-conventions/", "/en/7/guides/rhinopython/python-code-conventions/", "/en/wip/guides/rhinopython/python-code-conventions/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide provides an overview of Python coding conventions."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Code Conventions"
type = "guides"
weight = 100
override_last_modified = "2022-04-29T08:06:15Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"
+++

## Overview

Coding conventions are suggestions designed to help you write Python and RhinoScript code.  Coding conventions can include the following:

- Naming conventions for objects, variables, and procedures
- Commenting conventions
- Code Block syntax
- Whitespace (spaces vs tabs)

The reason for using coding conventions is to standardize the structure and style of a script or set of scripts so that you and others can easily read and understand the code.  Using coding conventions results in clear, precise, and readable code that is consistent with other language conventions and is intuitive.

For the official documentation on Python Syntax, see the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Names and Capitalization

In Python names are used as identifiers of functions, classes, variables, etc....  Identifiers must start with a Letter (A-Z) or an underscore ("_"), followed by more letters or numbers.

Python does not allow characters such as @, $, and % within identifier names.

Python is case sensitive.  So "selection" and "Selection" are two different identifiers. Normally class names will begin with capital letters and other identifiers will be all lower case.  It is also common practice to start private identifiers with an underscore.

The body of a variable or procedure name should use mixed case and be as descriptive as necessary.  Also, procedure names should begin with a verb, such as `InitNameArray` or `ValidateLayer`.

For frequently used or long terms, standard abbreviations are recommended to help keep name length reasonable.  In general, variable names greater than 32 characters can be difficult to read.  When using abbreviations, make sure they are consistent throughout the entire script.  For example, randomly switching between `Cnt` and `Count` within a script may lead to confusion.

Best practices for Python naming can be found in the [Style Guide for Python Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions).

## Comments in Python

Comments in Pythons are used to leave notes in the code to better explain what is happening.  Comments are ignored by the interpreter during compile.

Python comments are started with a hash (#) sign.  The hash sign can be used at the start of a line, followed by a single line comment.  This is considered a blank line by the interpreter.

```python
# My first comment
# this is a second line to this comment
# use multiple hash characters to make multiline comments
```
A hash sign can also be added at the end of a line of code.  After the hash sign add the comment.  To Python this is considered an end of statement comment.

```python
print ("Hello, World!") # the second comment that I make
```

Remember the following points:

- Every important variable declaration should include an inline comment describing the use of the variable being declared.
- Variables and procedures should be named clearly to ensure that inline comments are only needed for complex implementation details.
- At the beginning of your script, you should include an overview that describes the script, enumerating objects, procedures, algorithms, dialog boxes, and other system dependencies.  Sometimes a piece of pseudocode describing the algorithm can be helpful.

## Block Statements

Python does not use braces to denote block statement.  Block statements are created using whitespace to the left of the lines within the block.  Each following line within the block must have the same amount of white space.

A good example is an if block. For example −

```python
if True:
    print ("Your answer is True.")
else:
  print ("Your answer is False.")
```

However, the following block generates an error −

```python
if True:
    print ("You are ")
    print ("correct")
else:
    print ("You are not")
  print ("correct")
```  

You may also see the use of the colon (:) in the statements above. The colon is used for compound code statements (suites in Python) such as if and while loops.

## Whitepace

While Python can interpret both tabs and spaces as whitespace to the left of a statement, it is recommended that spaces are used.  Common practice is to use 4 spaces to denote an indentation. 

## Code Formatting

Screen space should be conserved as much as possible, while still allowing code formatting to reflect logic structure and nesting.  Here are a few suggestions:

- Indent standard nested blocks four spaces.
- Indent the overview comments of a procedure one space.
- Indent the highest level statements that follow the overview comments two spaces, with each nested block indented an additional two spaces.

## In Summary

The following code adheres to Python coding conventions:

```python
#****************************************************
# Purpose: Locates the first occurrence of a specified
#          layer in the LayerList array.
# Inputs:  arrLayerList: the list of layers to be searched.
#          strTargetLayer: the name of the layer to search for.
# Returns: The index of the first occurrence of the
#          strTargetLayer in the strLayerList array.
#          If the target layer is not found, return -1.
#****************************************************
import rhinoscriptsyntax as rs

def FindLayer(LayerList, TargetLayer):

  FindLayer = -1 # Default return value
  i = 0          # Initialize loop counter
  blnFound = False
  while i < len(LayerList) and not blnFound:
    if LayerList[i] == TargetLayer:
      blnFound = True # Set flag to True
      FindLayer = i   # Set return value to loop count

    i = i + 1         # Increment loop counter
```

## Related Topics

- [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript)
