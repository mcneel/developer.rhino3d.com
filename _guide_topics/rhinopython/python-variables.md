---
title: Python Variables
description: This guide provides an overview of Python variables.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac' 'Windows']
categories: ['Fundamentals']
origin:
order: 3
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

 
## Overview

A variable is a convenient placeholder that refers to a computer memory location where you can store program information that may change during the time your script is running.  For example, you might create a variable called ClickCount to store the number of times a user performs a certain operation.  
When a variable is stored in memory, the interpreter will allocate a certain amount of space for each variable type.  Where the variable is stored in computer memory is unimportant.  What is important is that you know that a vairaible has a type, and you refer to a variable by name to see or change its value.  

In Python, variables are always one of the five fundamental data types: 

* Numbers
* String
* List
* Tuple
* Dictionary

For a detailed look at each variable type see (Python Variable Types)({{ site.baseurl }}/guides/rhinopython/python-datatypes/) in this guide.

While each variable has its own properties and methods, there are common methods we use to deal with all varaiable in Python.

## Declaration

In Python, variables are created the first time a value is assigned to them.  For example:

```python
number1 = 10
string1 = "This is a string"
```

You declare multiple variables by separating each variable name with a comma.  For example:

```python
a, b = True, False
```

This is the same the multilple line declaration of:

```python
a = True
b = False
```

## Naming Restrictions

Variable names follow the standard rules for naming anything in Python.  A variable name:

- Must begin with an alphabetic character (A -Z) or an underscore (_).
- Cannot contain a perios(.), @, $, or %.
- Must be unique in the scope in which it is declared.
- Python is case sensative.  So "selection" and " Selection" are two different variables.

Best practices for all Python naming can be found in the (Style Guide for Python Naming Conventions)[https://www.python.org/dev/peps/pep-0008/#naming-conventions] 

## Scope & Lifetime

Scope of a variable defines where that variable can be accessed in your code.  For instance a `global` variable can be accessed from anywhere in you code.  A `local` variable can only be accessed within the function it was declared in.  Generally a variable's scope is determined by where you declare it.  

When you declare a variable within a procedure, only code within that procedure can access or change the value of that variable.  It has local scope and is a procedure-level variable.  If you declare a variable outside a procedure, you make it recognizable to all the procedures in your script.  This is a global variable, and it has global scope.

Here are few examples:

```python
global_var = True

def function1():
    local_var = False
    print global_var
    print local_var

function1() # this runs the function
print global_var # this works because global_var is accessable
print local_var  # this gives an error because we are outside function1
```

It is important to be careful when declaring variables.  It is easy to create duplicate variable names that do not reference the correct values.  For instance do not declare a global varible this way:

```python
g_var = 'foo'
def function2():
    g_var = 'bar'
    print 'inside the function var is ', var

ex2()
print 'outside the function var is ', var
```
The example above will create a `Global` variable named `g_var`.  When dropping in the `function2` function, there will be a second `local` variable created named `g_var` with a different value. The proper way to work with a global variable is to be very explicate with the `global` statement in the `local` scope:

```python
g_var = 'foo'
def function2():
    global g_var
    g_var = 'bar'
    print 'inside the function var is ', var

ex2()
print 'outside the function var is ', var

```

For more scope example see the (Notes on Python Variables)[http://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/]

The lifetime of a variable depends on how long it exists.  The lifetime of a `global` variable extends from the time it is declared until the time the script is finished running. At procedure level, a variable exists only as long as you are in the procedure.  When the procedure exits, the variable is destroyed.  Local variables are ideal as temporary storage space when a procedure is executing.  You can have local variables of the same name in several different procedures because each is recognized only by the procedure in which it is declared.

## Assigning Values

Values are assigned to variables creating an expression as follows: the variable is on the left side of the expression and the value you want to assign to the variable is on the right.  For example:

```python
B = 200
```

The same value can be assigned to multiple variables at the same time:

```python
a = b = c = 1
```

And multiple variables can be assigned different values on a single line:

```python
a, b, c = 1, 2, "john"
```

This is the same as:

```python
a = 1
b = 2
c = "john"
```

## Scalar Variables & Lists

Much of the time, you only want to assign a single value to a variable you have declared. A variable containing a single value is a scalar variable.  Other times, it is convenient to assign more than one related value to a single variable.  Then you can create a variable that can contain a series of values. This is called an list variable. List variables and scalar variables are declared in the same way, except that the declaration of an array variable uses brackets `[ ]` following the variable name.

```python
A = [ ] # This is a blank list variable
B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
C = [2, 4, 'john'] # lists can contain different variable types.
```

All lists in Python are zero-based indexed. When referencing a member or the legnth of a list the number of list elements is always the number shown plus one.

```python
mylist = ['Rhino', 'Grasshopper', 'Flamingo', 'Bongo']
B = Len(Mylist) # This will return 3. The index is 0 - 3.
print = Mylist[1] # This will return the value at index 1, which is 'Grasshopper'
print = mylist[0:2] # This will return the first 3 elements in the list.
```

You can assign data to a sepcific element of the list using an index into the list. The list index starts at zero. Data can be assigned to the elements of an array as follows:

```python
mylist[0] = 'Rhino'
mylist[1] = 'Grasshopper'
mylist[2] = 'Flamingo'
mylist[3] = 'Bongo'
```

Lists aren't limited to a single dimension. Although most people can't comprehend more than three or four dimensions. You can declare multiple dimensions by separating an with commas.  In the following example, the MyTable variable is a two-dimensional array :

```python
MyTable = [[], []]
```

In a two-dimensional array, the first number is always the number of rows; the second number is the number of columns.

For a detailed look at managing lists, take a look at the article (TutorialPoint Python Lists)[https://www.tutorialspoint.com/python/python_lists.htm]

---

## Related topics

- [VBScript Data Types]({{ site.baseurl }}/guides/rhinoscript/vbscript-datatypes/)
- [VBScript Procedures]({{ site.baseurl }}/guides/rhinoscript/vbscript-procedures/)
