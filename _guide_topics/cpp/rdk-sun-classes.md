---
title: RDK Sun classes
description: This document describes how to use the RDK sun classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin']
layout: toc-guide-page
---

## IRhRdkSun
<a name="IRhRdkSun"></a>
_IRhRdkSun_ is an abstract sun interface. It provides access to all the properties of a sun. It can be used to modify the RDK Document Sun or any temporary 'working' sun you might have access to.

## CRhRdkSun
<a name="CRhRdkSun"></a>
_CRhRdkSun_ is a simple sun object that can be placed on the stack or used as a class member. It can be used as a temporary 'working' sun and it provides access to an underlying implementation of IRhRdkSun. You can use this to do sun angle calculations without affecting the document sun. This might be useful, for example, to create an ephemeris or some other table of sun information.

## CRhRdkSunDialog
<a name="CRhRdkSunDialog"></a>
_CRhRdkSunDialog_ is a wrapper around a sun UI. TODO: data source.

<a name="DocumentSun"></a>
## The RDK Document Sun
The _RDK Document Sun_ is a special sun which has an effect on the viewport and renderings. If you have a Rhino document, you can read and write the document sun. As its name implies, changes to the document sun are stored in the document. Any changes you make will also appear in the main sun UI. Getting the sun from the document always returns a const reference. To write to the sun, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system.

```cpp
  // Read some information from the document sun.
  const auto& read_sun = pDoc->Sun();
  const bool b = read_sun.EnableOn();
  ... // Read other properties here.

  // Change some properties of the document sun.
  auto& write_sun = read_sun.BeginChange(RhRdkChangeContext::Program);
  write_sun.SetEnableOn(true);
  ... // Write other properties here.
  write_sun.EndChange();
```
