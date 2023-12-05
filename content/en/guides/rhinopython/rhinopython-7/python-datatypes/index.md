+++
aliases = ["/5/guides/rhinopython/python-datatypes/", "/6/guides/rhinopython/python-datatypes/", "/7/guides/rhinopython/python-datatypes/", "/wip/guides/rhinopython/python-datatypes/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide is an overview of Python Data Types."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Data Types"
type = "guides"
weight = 3
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0
version = [ "7" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

Python has five standard Data Types:

* [Numbers](#numbers)
* [String](#string)
* [List](#list)
* [Tuple](#tuple)
* [Dictionary](#dictionary)

Python sets the variable type based on the value that is assigned to it.  Unlike more riggers languages, Python will change the variable type if the variable value is set to another value. For example:

```python
var = 123 # This will create a number integer assignment
var = 'john' # the `var` variable is now a string type.
```

## Numbers

Python numbers variables are created by the standard Python method:

```python
var = 382
```

Most of the time using the standard Python number type is fine. Python will automatically convert a number from one type to another if it needs. But, under certain circumstances that a specific number type is needed (ie. complex, hexidecimal), the format can be forced into a format by using additional syntax in the table below:

| Type | | |Format | | |  Description |
|:--------|:-:|:-:|:-|:-:|:-:|:--------|
| int  | | | a = 10 | | | Signed Integer   |
| long   | | | a = 345L | | | (L) Long integers, they can also be represented in octal and hexadecimal   |
| float   | | | a = 45.67 | | | (.) Floating point real values   |
| complex   | | | a = 3.14J | | | (J) Contains integer in the range 0 to 255.   |

Most of the time Python will do variable conversion automatically. You can also use Python conversion functions [(int(), long(), float(), complex())](https://docs.python.org/2/library/stdtypes.html#id2) to convert data from one type to another. In addition, the `type` function returns information about how your data is stored within a variable.

```python
message = "Good morning"
num = 85
pi = 3.14159

print(type(message))  # This will return a string
print(type(n))  # This will return an integer
print(type(pi))  # This will return a float
```

## String

Create string variables by enclosing characters in quotes. Python uses single quotes `'` double quotes `"` and triple quotes `"""` to denote literal strings.  Only the triple quoted strings `"""` also will automatically continue across the end of line statement.

```python
firstName = 'john'
lastName = "smith"
message = """This is a string that will span across multiple lines. Using newline characters
and no spaces for the next lines. The end of lines within this string also count as a newline when printed"""
```

Strings can be accessed as a whole string, or a substring of the complete variable using brackets '[]'. Here are a couple examples:

```python
var1 = 'Hello World!'
var2 = 'RhinoPython'

print var1[0] # this will print the first character in the string an `H`
print var2[1:5] # this will print the substring 'hinoP`
```

Python can use a special syntax to format multiple strings and numbers. The string formatter is quickly covered here because it is seen often and it is important to recognize the syntax.  

```python
print "The item {} is repeated {} times".format(element,count))
```

The `{}` are placeholders that are substituted by the variables `element` and `count` in the final string. This compact syntax is meant to keep the code more readable and compact.

Python is currently transitioning to the format syntax above, but python can use an older syntax, which is being phased out, but is still seen in some example code:

```python
print "The item %i is repeated %i times"% (element,count)
```

For more information on the string formatter in Python see the article: [PyFormat Website](https://pyformat.info/)


For a more detailed look at string variables in Python, see the [Tutorialspoint Python Tutorial on stings.](https://www.tutorialspoint.com/python/python_strings.htm) Note: this article does use the older formatting syntax, but has a lot useful information.

## List

Lists are a very useful variable type in Python. A list can contain a series of values. List variables are declared by using brackets `[ ]` following the variable name.

```python
A = [ ] # This is a blank list variable
B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
C = [2, 4, 'john'] # lists can contain different variable types.
```

All lists in Python are zero-based indexed. When referencing a member or the length of a list the number of list elements is always the number shown plus one.

```python
mylist = ['Rhino', 'Grasshopper', 'Flamingo', 'Bongo']
B = len(mylist) # This will return the length of the list which is 3. The index is 0, 1, 2, 3.
print mylist[1] # This will return the value at index 1, which is 'Grasshopper'
print mylist[0:2] # This will return the first 3 elements in the list.
```

You can assign data to a specific element of the list using an index into the list. The list index starts at zero. Data can be assigned to the elements of an array as follows:

```python
mylist = [0, 1, 2, 3]
mylist[0] = 'Rhino'
mylist[1] = 'Grasshopper'
mylist[2] = 'Flamingo'
mylist[3] = 'Bongo'
print mylist[1]
```

Lists aren't limited to a single dimension. Although most people can't comprehend more than three or four dimensions. You can declare multiple dimensions by separating an with commas.  In the following example, the MyTable variable is a two-dimensional array :

```python
MyTable = [[], []]
```

In a two-dimensional array, the first number is always the number of rows; the second number is the number of columns.

For a detailed look at managing lists, take a look at the article

- [Python Lists - Google developer](https://developers.google.com/edu/python/lists)
- [TutorialPoint Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Tuple

Tuples are a group of values like a list and are manipulated in similar ways.  But, tuples are fixed in size once they are assigned. In Python the fixed size is considered immutable as compared to a list that is dynamic and mutable. Tuples are defined by parenthesis ().

```python
myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')
```

Here are some advantages of tuples over lists:
1. Elements to a tuple. Tuples have no append or extend method.
2. Elements cannot be removed from a tuple.
3. You can find elements in a tuple, since this doesn’t change the tuple.
4. You can also use the in operator to check if an element exists in the tuple.
5. Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
6. It makes your code safer if you “write-protect” data that does not need to be changed.

It seems tuples are very restrictive, so why are they useful? There are many datastructures in Rhino that require a fixed set of values.  For instance a Rhino point is a list of 3 numbers `[34.5, 45.7, 0]`. If this is set as tuple, then you can be assured the original 3 number structure stays as a point `(34.5, 45.7, 0)`.  There are other datastructures such as lines, vectors, domains and other data in Rhino that also require a certain set of values that do not change.  Tuples are great for this.

For more information on Tuples, see the [TutorialPoint Python Tutorial on Tuples](https://www.tutorialspoint.com/python/python_tuples.htm) and the [Dive in Python section on tuples](http://getpython3.com/diveintopython3/native-datatypes.html#tuples).

## Dictionary

Dictionaries in Python are lists of `Key`:`Value` pairs. This is a very powerful datatype to hold a lot of related information that can be associated through `keys`. The main operation of a dictionary is to extract a value based on the `key` name. Unlike lists, where index numbers are used, dictionaries allow the use of a `key` to access its members.  Dictionaries can also be used to sort, iterate and compare data.

Dictionaries are created by using braces ({}) with pairs separated by a comma (,) and the key values associated with a colon(:). In Dictionaries the `Key` must be unique.  Here is a quick example on how dictionaries might be used:


```python
room_num = {'john': 425, 'tom': 212}
room_num['john'] = 645  # set the value associated with the 'john' key to 645
print (room_num['tom']) # print the value of the 'tom' key.
room_num['isaac'] = 345 # Add a new key 'isaac' with the associated value
print (room_num.keys()) # print out a list of keys in the dictionary
print ('isaac' in room_num) # test to see if 'issac' is in the dictionary.  This returns true.
```

Dictionaries can be more complex to understand, but they are great to store data that is easy to access.  To find out more about using dictionaries see the [Python Fundamentals - Dictionaries](/guides/rhinopython/python-dictionaries/)

## Related topics

- [What are Python and RhinoScript?](/guides/rhinopython/rhinopython-7/what-is-rhinopython)
- [Python Variables](/guides/rhinopython/rhinopython-7/python-variables/)
- [Python Dictionaries](/guides/rhinopython/rhinopython-7/python-dictionaries/)
