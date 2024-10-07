+++
aliases = ["/en/5/guides/rhinopython/python-conditionals/", "/en/6/guides/rhinopython/python-conditionals/", "/en/7/guides/rhinopython/python-conditionals/", "/en/wip/guides/rhinopython/python-conditionals/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide is an survey of Python conditional statements."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Conditionals"
type = "guides"
weight = 5
override_last_modified = "2018-12-05T14:59:06Z"
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

You can control the flow of your script with conditional statements and looping statements.  Using conditional statements, you can write Python code that makes decisions and repeats actions.  The following conditional statements are available in Python:

* `if` statement
* `if`...`else` statement
* `if`...`elif`...`elif`...`else` nested statement

The `if`... statement is used to evaluate whether a condition is True or False and, depending on the result, to specify one or more statements to run.  Usually the condition is an expression that uses a comparison operator to compare one value or variable with another.  For information about comparison operators, see the [Python Operators](/guides/rhinopython/python-operators) guide. `if`... and `if...elif` statements can be nested to as many levels as you need.

Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value.

### if

To run only one statement when a condition is True, use the single-line syntax for the `if`... statement.  The following example shows the single-line syntax.

```python
var1 = 350
if var1 == 350 : print ("The value of the variable is 350")
```

To run more than one line of code, you must use the multiple-line (or block) syntax. The first line ends in a colon (:). As with all Python block syntax, the whitespaces to the left of the lines must be the same throughout the block. As an example:

```python
var1 = 350
if var1 == 350 :
    print ("The value of the variable is 350")
    var2 = 450
    print ("The value of variable 2 is 450")
```

### if..else

You can use an `if`...`else` statement to define two blocks of executable statements: one block to run if the condition is True, the other block to run if the condition is False...

```python
var1 = 350
if var1 == 0 :
    MyLayerColor = 'vbRed'
    MyObjectColor = 'vbBlue'
else :
    MyLayerColor = 'vbGreen'
    MyObjectColor = 'vbBlack'
print (MyLayerColor)
```

### if..elif..elif..else

A variation on the `if`...`else` statement allows you to choose from several alternatives.  Adding `elif` clauses expands the functionality of the `if`...`else` statement so you can control program flow based on multiple different possibilities. For example:

```python
var1 = 0
if var1 == 0 :
    print ("This is the first " + str(var1))
elif var1 == 1 :
    print ("This is the second " + str(var1))
elif var1 == 2 :
    print ("This is the third " + str(var1))
else :
    print ("Value out of range!")
```

You can add as many `elif` clauses as you need to provide alternative choices. Thie `elif` statement takes the place of the `Select Case` statement in other languages.

For more information on nesting if..elif..else statements see [Python nested if statements on TutorialsPoint](https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm)


## Related Topics

- [What are Python and RhinoScriptSyntax?](/guides/rhinopython/what-is-rhinopython)
- [Python Operators](/guides/rhinopython/python-operators)
