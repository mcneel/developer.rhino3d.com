---
layout: toc-guide-page
title: APIs Available to Python
author: alain@mcneel.com
categories: ['GettingStarted']
platforms: ['Windows', 'Mac', 'Cross-Platform']
apis: ['RhinoPython']
languages: ['Python']
keywords: ['Rhino.Python', 'Python']
origin: http://wiki.mcneel.com/developer/python
order: 3
---

# APIs Available to Python
{: .toc-title }

#### RhinoScriptSyntax

RhinoScriptSyntax is divided into [modules](/api/RhinoScriptSyntax/namespaces.html) and each module contains functions that are meant to duplicate the functionality provided by the RhinoScript language that's supported in Rhino for Windows.[^1].  In other words this is a Python equivalent of those RhinoScript functions so if you are familiar with RhinoScript in Rhino for Windows the transition to Python in Rhino for the Mac should be natural.  Not all of the RhinoScript functions have been added yet but this document will be updated as more functions are added.

#### RhinoCommon

An important detail that will become important as you are learning to script Rhino with Python is that the implementation of Python that is embedded in Rhino is called IronPython: a Python implementation in C# that runs on the .Net/mono platform which means that in addition to the Python language features and the [rhinoscriptsyntax package](/api/RhinoScriptSyntax/namespaces.html), you also have access to all the libraries in .Net/mono and [RhinoCommon](../../rhinocommon/what_is_rhinocommon/).

The rhinoscriptsyntax package is implemented on top of RhinoCommon so reading the source code is a great way to learn how to use RhinoCommon from Python.  The source code files are included in the Rhino distribution on your computer and the default location is:
```bash
/Users/<YOUR_HOME_DIRECTORY>/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/ironpython/settings/lib/rhinoscript
```

[^1]: Rhino for Mac supports Python whereas Rhino for Windows supports both RhinoScript and Python.
