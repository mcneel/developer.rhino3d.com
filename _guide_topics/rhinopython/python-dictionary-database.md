---
title: Using Python Dictionary as a database
description: This guide discusses using Python's Dictionary object to access nested data.
authors: ['Scott Davidson']
author_contacts: ['scottd']
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

## Accessing the Datastore

There are many ways to access the data in this datastore:

```python
print datastore["store"]["bicycle"]
```

This returns the bicycle dictionary object`{ "color":"blue, "style":"trail", "price":49.95 }`

Knowing that the `value` for `bookshelf` is a list.  Use and index number to access any single book:

```python
 print datastore["store"]["bookshelf"][1]
```

This returns the dictionary object for The Grapes of Wrath.


The objects and values in the datastore can also be accessed with the `.get` method.  The direct method shown above will return an error if a key does not exist. The `.get` method is a little safer.  It will return a value or `None`.  This is much safer if you are not sure the key is always present.  The `isbn` key is a goot example of this.

```python
print datastore["store"]["toy"] # this produces an error.
print datastore["store"].get("toy")  #This will produce the value of None.
```
A convenient way to efficiently address a portion of the datastore is to assign the portion to a variable. In this case we can assign the list of books to a `books` variable:

```python
books = datastore['store']['bookshelf']
```
The variable is a reference to the object. Any changes made with books will also be reflected in the original datastore. Also, because books containsonly the list of books in the datastore, it is quite easy to step through the books with a `for` statement.  In the example below, the for loop is looking for a specifc book then updates the price:

```python
# Here is a method to find and change a value in the database.
  for item in books:
       if item.get('author') == "Seneca" :
           item['price'] = 10.00

  for item in datastore['store']['bookshelf']: # This loop shows the change is not only in books, but is also in database
       if item.get('author') == "Seneca" :
           print 'The book %s now costs %s' % (item.get("title"), format(item.get("price"), '.2f'))
```

