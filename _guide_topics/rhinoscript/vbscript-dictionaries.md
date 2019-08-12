---
title: VBScript Dictionaries
description: This guide discusses using VBScript's Dictionary object in RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/scriptsamples/dictionaryobject
order: 100
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

One of the nice features of other scripting languages, such as Perl, LISP, and Python is what is called an associative array. A n associative array differs from a "normal" array in one major way: rather than being indexed numerically (i.e. 0, 1, 2, 3, ...), it is indexed by a key, or an English-like word.  VBScript has something very similar to an associative array.  This object is called the Dictionary object.  The VBScript Dictionary object provides an item indexing facility.  Dictionaries are part of Microsoft's Script Runtime Library.

The Dictionary object is used to hold a set of data values in the form of (key, item) pairs.  A dictionary is sometimes called an associative array because it associates a key with an item.  The keys behave in a way similar to indices in an array, except that array indices are numeric and keys are arbitrary strings.  Each key in a single Dictionary object must be unique.

Dictionaries are frequently used when some items need to be stored and recovered by name.  For example, a dictionary can hold all the environment variables defined by the system or all the values associated with a registry key.  However, a dictionary can only store one item for each key value.  That is, dictionary keys must all be unique.

## Creating Dictionaries

To construct an instance of a dictionary object, just use the following lines of code:

```vbnet
Dim objDictionary
Set objDictionary = CreateObject("Scripting.Dictionary")
```

Dictionary objects have one property that should be set before any data values are stored in the dictionary.  There are two modes for the .CompareMode property which control how individual keys are compared.  If the mode is `vbBinaryCompare` (the default), upper and lower case letters in keys are considered distinct.  If the mode is `vbTextCompare`, upper and lower case letters in keys are considered identical.  This means that a Dictionary object in binary mode can contain two keys "Key" and "key", whereas these would be considered the same key in text mode.

## Adding Values

To add a value to a Dictionary, use the `.Add` method.  For example:

```vbnet
Dim objDictionary
Set objDictionary = CreateObject("Scripting.Dictionary")
objDictionary.CompareMode = vbTextCompare
objDictionary.Add "Pastrami", "Great"
objDictionary.Add "Roast Beef", "OK on Sunday"
objDictionary.Add "Salami", "Not so good"
```

The first argument to the `.Add` method is the key value and the second argument is the item value.  The key is similar to the index in a numerically-based, indexed array, and the item is the value at that index.  There is no limit to the number of values that can be added to a dictionary (within the bounds of physical memory).

## Removing Values

To remove a value from a dictionary, use the `.Remove` method and specify the key to remove.  For example:

```vbnet
objDictionary.Remove "Salami"
```

To remove all values and clear the dictionary, use the `.RemoveAll` method.

## Counting Values

Use the `.Count` property to obtain a count of values in the dictionary.

## Get Values for Key

The `.Exists` method returns True if the specified key exists within the dictionary.  For example:

```vbnet
If objDictionary.Exists("Pastrami") Then Rhino.Print "Pastrami is available today."
```

To retrieve the item value for a given key, use the `.Item` property.  This is the default property for a Dictionary object.  For example:

```vbnet
If objDictionary.Exists("Salami") Then Rhino.Print objDictionary("Salami")
```

The `Rhino.Print` statement displays the item value stored in the dictionary for the `"Salami"` key.  Use the `.Key` property to change the key value for a given key.  For example:

```vbnet
objDictionary.Key("Salami") = "Italian Salami"
```

The `.Keys` and `.Items` methods return an array containing all the keys or items from the dictionary.  For example:

```vbnet
aMeats = oDict.Keys
aComments = oDict.Items
```

## Sorting Dictionaries

On occasion, it may be important to sort your dictionary.  You can sort a dictionary by using the following function...

```vbnet
' Description:
'   Sorts a dictionary by either key or item
' Parameters:
'   objDict - the dictionary to sort
'   intSort - the field to sort (1=key, 2=item)
' Returns:
'   A dictionary sorted by intSort
'
Function SortDictionary(objDict, intSort)

  ' declare constants
  Const dictKey  = 1
  Const dictItem = 2

  ' declare our variables
  Dim strDict()
  Dim objKey
  Dim strKey,strItem
  Dim X,Y,Z

  ' get the dictionary count
  Z = objDict.Count

  ' we need more than one item to warrant sorting
  If Z > 1 Then
    ' create an array to store dictionary information
    ReDim strDict(Z,2)
    X = 0
    ' populate the string array
    For Each objKey In objDict
        strDict(X,dictKey)  = CStr(objKey)
        strDict(X,dictItem) = CStr(objDict(objKey))
        X = X + 1
    Next

    ' perform a a shell sort of the string array
    For X = 0 To (Z - 2)
      For Y = X To (Z - 1)
        If StrComp(strDict(X,intSort),strDict(Y,intSort),vbTextCompare) > 0 Then
            strKey  = strDict(X,dictKey)
            strItem = strDict(X,dictItem)
            strDict(X,dictKey)  = strDict(Y,dictKey)
            strDict(X,dictItem) = strDict(Y,dictItem)
            strDict(Y,dictKey)  = strKey
            strDict(Y,dictItem) = strItem
        End If
      Next
    Next

    ' erase the contents of the dictionary object
    objDict.RemoveAll

    ' repopulate the dictionary with the sorted information
    For X = 0 To (Z - 1)
      objDict.Add strDict(X,dictKey), strDict(X,dictItem)
    Next

  End If

End Function
```

The Dictionary object is not there to replace the array, but there are certainly times when it makes more sense to index your array using English-like terms as opposed to numerical values.
