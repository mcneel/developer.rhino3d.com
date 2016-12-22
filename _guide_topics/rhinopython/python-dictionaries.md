---
title: Python Dictionaries
description: This guide discusses using VBScript's Dictionary object in RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Fundamentals']
origin:
order: 100
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

One of the nice features of other scripting languages, such as Perl, LISP, and Python is what is called an associative array. An associative array differs from a "normal" array in one major way: rather than being indexed numerically (i.e. 0, 1, 2, 3, ...), it is indexed by a key, or an English-like word. Python has something very similar to an associative array. This object is called the Dictionary object. The Python Dictionary object provides an item indexing facility.

The Dictionary object is used to hold a set of data values in the form of (key, item) pairs.  A dictionary is sometimes called an associative array because it associates a key with an item.  The keys behave in a way similar to indices in an array, except that array indices are numeric and keys are arbitrary strings.  Each key in a single Dictionary object must be unique.

Dictionaries are frequently used when some items need to be stored and recovered by name.  For example, a dictionary can hold all the environment variables defined by the system or all the values associated with a registry key.  However, a dictionary can only store one item for each key value.  That is, dictionary keys must all be unique.

## Creating Dictionaries

To create an empty dictionay, use a pair of braces `{}`

```python
room_empty = {}
```

To construct an instance of a dictionary object with data, just use one of the the following methods:

```python
room_num = {'john': 425, 'tom': 212}
room_num1 = dict([('john', 425), ('tom', 212), ('jack', 325)]) # an alternative way to create a dictionary is to use the dcit() constructor to create a dictionary.
```
The `key` value is a string or number, followed be a colon `:` as a serprater from the associated value which can be any datatype. Then use a comma `,` to sperate different key:pairs in the dictionary.

## Adding Values

To add a value to a Dictionary, use the `.Add` method.  For example:

```python
room_num = {'john': 425, 'tom': 212}
room_num['isaac'] = 345 # Add a new key 'isaac' with the associated value
print room_num
```

Use the variable name with the new key value in brackets `[]` and after the equals is the item value.  The key is similar to the index in a numerically-based, indexed array, and the item is the value at that index.  There is no limit to the number of values that can be added to a dictionary (within the bounds of physical memory).

Changing a value for any of the keys follows the same syntax.  If the key allready exists in the dictionary, the value is simply updated.

## Removing Values

To remove a value from a dictionary, use the `del` method and specify the key to remove.  For example:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
del room_num['isaac']
print room_num
```

## Counting Values

Use the `len()` property to obtain a count of values in the dictionary.

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
print len(room_num)
```

## Get Values for Key

The `in` syntax returns True if the specified key exists within the dictionary.  For example:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
var1 = 'tom' in room_num # Looking wether a specific key exists.
print "Is tom in the dictionary" + str(var1)
var1 = 'isaac' not in room_num # using not also works for the opposite
print "Is isaac not in room_num " + str(var1)
```

Use the variable name and the key value in brackets `[]` to get the value assoted with the key.

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
var1 = room_num['isaac']
print room_num # will print the isaac value of 345
```

The `.keys()` and `.values()` methods return an array containing all the keys or values from the dictionary. For example:

```python
room_num = {'john': 425, 'tom': 212}
print (room_num.keys()) # print out a list of keys in the dictionary
print (room_num.values()) # print out a list of values in the dictionary
```

## Looping through Dictionaries

Dictionaires can be used to control loops.  In addition both the keys and values can be extracted at the same time using the `.items()` method:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
for k, v in room_num.items():
    print k + ' is in room ' + str(v)
```

You can also go through the dictionary backwards by using the `reversed()` method:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
for k, v in reversed(room_num.items()):
    print k + ' is in room ' + str(v)
```

## Sorting Dictionaries

On occasion, it may be important to sort your dictionary. Dictionaries and be sorted by `key` name or by `values`

To sort a dictionary by key using the following `sorted()` function:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
print sorted(room_num) # sort the dictionary by keys
```

To sort by `values` use the `sorted()` method along with the `.values()` function:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
print sorted(room_num.values()) # sort the dictionary by keys
```

The Dictionary object is not there to replace the array, but there are certainly times when it makes more sense to index your array using English-like terms as opposed to numerical values.
