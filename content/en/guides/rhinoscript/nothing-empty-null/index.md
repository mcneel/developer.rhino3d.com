+++
aliases = ["/en/5/guides/rhinoscript/nothing-empty-null/", "/en/6/guides/rhinoscript/nothing-empty-null/", "/en/7/guides/rhinoscript/nothing-empty-null/", "/wip/guides/rhinoscript/nothing-empty-null/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide discusses what nothing means in VBScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Nothing vs Empty vs Null"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/vbnothing"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

There has always been confusion about the semantics of data that are not even there.  Usually they've written code something like:

```vbnet
If varValue = Nothing Then
```

or

```vbnet
If varValue = Empty Then
```

or

```vbnet
If varValue = Null Then
```

Why does VBScript have `Null`, `Nothing` and `Empty`, and what are the differences between them?

## Empty

When you declare a variable in VBScript, the variable's value before the first assignment is undefined, or `Empty`.

```vbnet
Dim varValue ' Empty value
```

So basically, `Empty` says "I am an uninitialized variant."  If you need to detect whether a variable actually is an empty variant and not a string or a number, you can use `IsEmpty`.  Alternatively, you could use `TypeName` or `VarType`, but `IsEmpty` is best.

## Nothing

`Nothing` is similar to `Empty` but subtly different.  If `Empty` says "I am an uninitialized variant," `Nothing` says "I am an object reference that refers to no object."  Objects are assigned to variables using the `Set` statement.  Since the equality operator on objects checks for equality on the default property of an object, any attempt to say:

```vbnet
If varValue = Nothing Then
```

is doomed to failure; `Nothing` does not have a default property, so this will produce a run-time error.  To check to see if an object reference is invalid, use:

```vbnet
If varValue Is Nothing Then
```

## Null

`Null` is more obscure.  The semantics of `Null` are very poorly understood, particularly amongst people who have little experience with programming.  Empty says "I'm an uninitialized variant," `Nothing` says "I'm an invalid object" and `Null` says "I represent a value which is not known."  Null is not *True*, not *False*, but `Null`! The correct way to check for `Null` is much as you'd do for `Empty`: use `IsNull` (or `TypeName` or `VarType`.)
