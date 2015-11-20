---
layout: toc-guide-page
title: VBScript Constants
author: dale@mcneel.com
categories: ['Basics']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/vbsconstants
order: 1
---

# VBScript Constants

This brief guide is an overview of VBScript constants.

## Overview

A constant is a meaningful name that takes the place of a number or string and never changes. VBScript defines a number of intrinsic constants. You can get information about these intrinsic constants from the VBScript language reference.

## Creating Constants

You create user-defined constants in VBScript using the `Const` statement. Using the `Const` statement, you can create string or numeric constants with meaningful names and assign them literal values.  For example:

```vbnet
Const MyString = "This is my string."
Const MyAge = 49
```

Note that the string literal is enclosed in quotation marks (`" "`).  Quotation marks are the most obvious way to differentiate string values from numeric values.  You represent Date literals and time literals by enclosing them in number signs (`#`).  For example:

```vbnet
Const CutoffDate = #11-17-2008#
```

You may want to adopt a naming scheme to differentiate constants from variables.  This will prevent you from trying to reassign constant values while your script is running.  For example, you might want to use a "vb" or "con" prefix on your constant names, or you might name your constants in all capital letters.  Differentiating constants from variables eliminates confusion as you develop more complex scripts.

---

## Related Topics

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript)
