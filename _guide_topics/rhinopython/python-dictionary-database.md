---
title: Using Python Dictionary as a database
description: This guide discusses using Python's Dictionary object to access nested data.
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['intermediate']
origin:
order: 100
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---


## Overview

There are many modern data structures that use a structured key:value pairs to describe objects and the data that is stored within them.  A few popular ones are XML, JSON and Amazon S3(Dynamo).

The Dictionary object is used to hold a set of data values in the form of (key, value) pairs.  The values can be any standard datatype including lists. This article may serve help understand how Python can be used to create and access nested information.

## Creating a Key:Value datastore

Here is an example of a nested dictionary that stores many different items. Look closely at the bracket and paraens that are used.  The curly braces `{}` denote the a dictionary.  The square brackets `[]` represent a list as a value in the `bookshelf` key. The list in bookshelf actually contains a series of dictionaries for each book.

Using Dictionaries, list and a key:values can be used together to create this datastore.

```python
datastore = { "store": {
    "bookshelf": [
      { "category": "classic",
        "author": "Charles Dickens",
        "title": "Great Expectations",
        "price": 7.47
      },
      { "category": "classic",
        "author": "John Steinbeck",
        "title": "The Grapes of Wrath",
        "price": 11.18
      },
      { "category": "philosophy",
        "author": "Seneca",
        "title": "Letters from a Stoic",
        "isbn": "0-140-44210-3",
        "price": 12.84
      },
      { "category": "fiction",
        "author": "George Orwell",
        "title": "1984",
        "isbn": "0-451-52493-4",
        "price": 8.49
      }
    ],
    "bicycle": {
      "color": "blue",
      "style": "trail",
      "price": 49.95
    }
  }
}
```

## Accessing Values

There are many ways to access the data in this datastore:

  # print database["store"]["book"][0:2]
  # print database["store"]["book"][1]["author"]
  # print database["store"]["bicycle"]

  # Use this method to create a reference to a portion of the database.  In this case the list of books.
  # A list object is mutable in Python, therfore it is easy to walk though it with a for statement
  # becase this is dereived from database, any changing the books list will change in database.
  books = database['store']['bookshelf']

  # for item in books:
  #     if "author" in item:
  #         print item.get("author")

  # List all the authors of the books.  Use item.get because it is safe if there is no title or price in the object.
  #for item in books:
  #    if "author" in item:
  #        print 'The book %s by %s costs $%s.' % (item.get('title'), item.get("author"), format(item.get("price"), '.2f'))


  # Here is a method to find and change a value in the database.
  for item in books:
       if item.get('author') == "Nigel Rees" :
           item['price'] = 10.00

  for item in database['store']['bookshelf']: # This loop shows the change is not only in books, but is also in database
       if item.get('author') == "Nigel Rees" :
           print 'The book %s now costs %s' % (item.get("title"), item.get('price'))
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
