---
title: Python Data Types
description: This guide is an overview of Python Data Types.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Fundamentals']
origin:
order: 3
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

 
## Overview

Python has five standard Data Types:

* [Numbers](#numbers)
* [String](#string)
* [List](#list)
* [Tuple](#tuple)
* [Dictionary](#dictionary)

Python sets the variable type based on the value that is assigned to it.  Unlike more riggeros lenguages, Python will change the variable type if the variable value is set to another value. For example:

```python
var1 = 123 # This will create a number integer assignment
var1 = 'john' # the `var1` varaible is now a string type.
```

## Numbers

Python numbers variables are created by the standard Python method:

```python
var1 = 382
```

Most of the time using the standard Python number type is fine. Python will automatically convert a number from one type to another if it needs. But, under certain circumstances that a specific number type is needed (ie. complex, hexidecimal), the format can be forced into a format by using additional syntax in the table below:

| Type | | |Format | | |  Description |
|:--------|:-:|:-:|:-|:-:|:-:|:--------|
| int  | | | a = 10 | | | Signed Integer   |
| long   | | | a = 345L | | | (L) Long integers, they can also be represented in octal and hexadecimal   |
| float   | | | a = 45.67 | | | (.) Floating point real values   |
| complex   | | | a = 3.14J | | | (J) Contains integer in the range 0 to 255.   |
|=====
|
{: rules="groups"}

Most of the time Python will do varibale convertion automatically. You can also use Python conversion functions [(int(), long(), float(), complex())](https://docs.python.org/2/library/stdtypes.html#id2) to convert data from one type to another. In addition, the `type` function returns information about how your data is stored within a variable.

## String

Create string variables by enclosing characters in quotes. Python uses single quotes (') double quotes (") and triple quotes (""") to denote literal strings.  Only the triple quoted strings (""") also will automatically continue across the end of line statement.

```python
var1 = 'john'
var2 = "smith"
var3 = """This is a string that will span across multiple lines. \nUsing newline characters
and no spaces for the next lines. The end of lines within this string also count as a newline when printed"""
```

Strings can be accessed as a whole string, or a substring of the complete variable using brackets ([]). Here are a couple examples:

```python
var1 = 'Hello World!'
var2 = 'RhinoPython'

print var1[0] # this will print the first character in the string an `H`
print var2[1:5] # this will print the substring 'hinoP`
```

For a more detailed look at sting variables in Python, see the [Tutorialspoint Python Tutorial on stings.](https://www.tutorialspoint.com/python/python_strings.htm)

## List

Lists are a very useful variable type in Python. A list can contain a series of values. List variables are declared by using brackets `[ ]` following the variable name.

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

You can assign data to a specific element of the list using an index into the list. The list index starts at zero. Data can be assigned to the elements of an array as follows:

```python
myList = [0, 0, 0, 0]
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

## Tuple

Tuples are a group of values like a list.  But tuples cannot be changed once they are assigned.  Tuples us paranthesis ().

```python
var1 = ('Rhino', "Grasshopper, 'Flamingo', 'Bongo')
```

For more information on Tuples, see the [TutorialPoint Python Tutorial on Tuples](https://www.tutorialspoint.com/python/python_tuples.htm)

## Dictionary

Dictionaries in Python are lists of `Key`:`Value` pairs. This is a very powerful datatype to hold a lot of related information that can be associated through `keys`. The main operation od a dictionary is to extract a value based on the `key` name. Unlike lists, where index numbers are used, dictionaries allow the use of a `key` to access its members.  Dictionaries can also be used to sort, iterate and compare data.

Dictionaries are created by using braces ({}) with pairs seperated by a comma (,) and the key values associated with a colon(:). In Dictionaries the `Key` must be unique.  Here is a quick example on how ditionaires might be used:


```python
room_num = {'john': 425, 'tom': 212}
room_num['john'] = 645  # set the value associated with the 'john' key to 645
print (room_num['tom']) # print the value of the 'tom' key.
room_num['isaac'] = 345 # Add a new key 'isaac' with the associated value
print (room_num.keys()) # print out a list of keys in the dictionary
print ('isaac' in room_num) # test to see if 'issac' is in the dictionary.  This returns true.
```

Dictionaries can be more complex to understand, but they are great to store data that is easy to access.  To find out more about using dictionaries see the [Python Fundamentals - Dictionaries]({{ site.baseurl }}/guides/rhinopython/python-dictionaries/)

---

## Related topics

- [What are Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Variables]({{ site.baseurl }}/guides/rhinopython/python-variables/)
- [Python Dictionaries]({{ site.baseurl }}/guides/rhinopython/python-dictionaries/)
