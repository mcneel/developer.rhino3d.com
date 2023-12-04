+++
aliases = ["/5/guides/rhinopython/python-dictionaries/", "/6/guides/rhinopython/python-dictionaries/", "/7/guides/rhinopython/python-dictionaries/", "/wip/guides/rhinopython/python-dictionaries/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses using Python's Dictionary object."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Dictionaries"
type = "guides"
weight = 100
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

One of the nice features of scripting languages such as Python is what is called an associative array. An associative array differs from a "normal" array in one major respect: rather than being indexed numerically (i.e. 0, 1, 2, 3, ...), it is indexed by a key, or an English-like word. Python has something very similar to an associative array in the Dictionary object. The Python Dictionary object provides a key:value indexing facility. Note that dictionaries are unordered - since the values in the dictionary are indexed by keys, they are not held in any particular order, unlike a list, where each item can be located by its position in the list.

The Dictionary object is used to hold a set of data values in the form of (key, item) pairs.  A dictionary is sometimes called an associative array because it associates a key with an item.  The keys behave in a way similar to indices in an array, except that array indices are numeric and keys are arbitrary strings.  Each key in a single Dictionary object must be unique.

Dictionaries are used when some items need to be stored and recovered by name.  For example, a dictionary can hold all of the environment variables defined by the system or all the values associated with a registry key. While this can be much faster than iterating a list looking for a match, a dictionary can only store one item for each key value.  That is, dictionary keys must all be unique.

## Creating Dictionaries

To create an empty dictionary, use a pair of braces `{}`

`room_empty = {}`


To construct an instance of a dictionary object with key:item pairs filled in, use one of the following methods.

The dictionary room_num is created and filled in with each key:value pair, rather than as an empty dictionary. The `key` is a string or number, in the example below it is a person's name,  followed be a colon `:` as a separator from the associated value which can be any datatype, in this case an integer. Commas `,`  seperate different key:value pairs in the dictionary:

`room_num = {'john': 425, 'tom': 212, 'sally':325}`

This dictionary is created from a list of tuples using the `dict` key word:

`room_num1 = dict([('john', 425), ('tom', 212), ('sally', 325)])`

The `dict`keyword can be used in other ways to construct dictionaries.


## Adding Values

To add a value to a Dictionary, specify the new key and set a value. Below, the code creates the dictionary *room_num* with two key:value pairs for John and Liz, then adds a third one for Isaac:

```python
room_num = {'John': 425, 'Liz': 212}
room_num['Isaac'] = 345
print room_num
```
There is no limit to the number of values that can be added to a dictionary (within the bounds of physical memory).

Changing a value for any of the keys follows the same syntax.  If the key already exists in the dictionary, the value is simply updated.

## Removing Values

To remove a value from a dictionary, use the `del` method and specify the key to remove:

```python
room_num = {'John': 425, 'Liz': 212, 'Isaac': 345}
del room_num['Isaac']
print room_num
```

## Counting Values

Use the `len()` property to obtain a count of values in the dictionary.

```python
room_num = {'John': 425, 'Liz': 212, 'Isaac': 345}
print len(room_num)
```

## Get Values for Key

The `in` syntax returns True if the specified key exists within the dictionary.  For example you may want to know if Tom is included in a dictionary, in this case False:

```python
room_num = {'John': 425, 'Liz': 212, 'Isaac': 345}
var1 = 'Tom' in room_num
print "Is Tom in the dictionary? " + str(var1)
```
or you may want to know if an Isaac is *not* in the dictionary. Below the answer will be also be False:

```python
room_num = {'John': 425, 'Liz': 212, 'Isaac': 345}
var1 = 'Isaac' not in room_num
print "Is Isaac not in room_num? " + str(var1)
```

Use the variable name and the key value in brackets `[]` to get the value associated with the key.

```python
room_num = {'John': 425, 'Liz': 212, 'Isaac': 345}
var1 = room_num['Isaac']
print "Isaac is in room number " + str(var1)
```

The `.keys()` and `.values()` methods return an array containing all the keys or values from the dictionary. For example:

```python
room_num = {'john': 425, 'tom': 212}
print (room_num.keys())
print (room_num.values())
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
print sorted(room_num)
```

To sort by `values` use the `sorted()` method along with the `.values()` function:

```python
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
print sorted(room_num.values())
```

The Dictionary object is not there to replace list iteration, but there are times when it makes more sense to index your array using English-like terms as opposed to numerical values. It can be much faster to locate an object in a dictionary than in a list.
