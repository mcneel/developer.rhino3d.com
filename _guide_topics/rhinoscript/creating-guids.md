---
title: Creating GUIDs
description: This guide demonstrates how to create a Globally Unique Identifier (GUID) in RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/createguid
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

[Globally Unique Identifiers](https://en.wikipedia.org/wiki/Globally_unique_identifier) - or GUIDs - are unique identification numbers that are used to track items.  Rhino uses GUIDs just for this purpose.  GUIDs come in different formats, but are usually stored as 128-bit values, and are commonly displayed as 32 hexadecimal digits with groups separated by hyphens:

`{3AEC4721-34KP-3152-B2BB-17442C41208P}`

Let's write a script that creates GUIDs...

## GUID Generation

There is actually a very easy way to generate GUIDs.  The `Scriptlet.TypeLib` object includes a method that generates GUIDs. If you need a GUID, here is a short script that will supply you with one:

```vbnet
' Creates a Registry-formatted GUID string
' Ex: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
Function CreateGuidRegistryFormat
  Dim objTypeLib
  Set objTypeLib = CreateObject("Scriptlet.TypeLib")
  CreateGuidRegistryFormat = Left(objTypeLib.Guid, 38)
End Function
```

If you want to create a plain GUID - one without the surrounding curly brackets, then you can do something like this:

```vbnet
' Creates a plain-formatted GUID string
' Ex: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Function CreateGuidPlainFormat
  Dim objTypeLib
  Set objTypeLib = CreateObject("Scriptlet.TypeLib")
  CreateGuidPlainFormat = Mid(objTypeLib.Guid, 2, 36)
End Function
```

---

## Related Topics

- [Globally Unique Identifier (Wikipedia)](https://en.wikipedia.org/wiki/Globally_unique_identifier)
- [Converting GUIDs to Strings]({{ site.baseurl }}/guides/rhinoscript/converting-guids-to-strings)
