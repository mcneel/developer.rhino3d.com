+++
aliases = ""
authors = [ "scott" ]
categories = [ "Intermediate" ]
description = "This guide covers the various ways to import modules Python in Rhino."
keywords = [ "Rhino.Python", "Python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Module Libraries in Python"
type = "guides"
weight = 27
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/python"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## Overview

Python is an extensible programming language with hundreds of additional modules.  This allows Python to be used in many situations both inside Rhino and outside Rhino.  There are some specific additional models that are specifically of interest related to Rhino and Grasshopper.

These new modules can be accessed in a Python script by including the `import` method at the top of each Python script:

```python
import rhinoscriptsyntax as rs
import math
```

## RhinoScriptSyntax

The RhinoScriptSyntax methods library contains hundreds of easy-to-use functions that perform a variety of operations on Rhino.  The library allows Python to be aware of the Rhino's:

* Geometry
* Commands
* Document objects
* Application methods

To make these methods easy-to-use, all RhinoScriptSyntax methods return simple Python variables or Python List-based data structures. Thus, once you are familiar with Python, you will be able to use any and all functions in the RhinoScriptSyntax methods library. RhinoScriptSyntax is divided into [modules](/api/RhinoScriptSyntax/win) that mirror standard Rhino commands.

A good set of tutorials on using RhinoScript methods can be found in the [Python in Rhino tutorials](https://developer.rhino3d.com/guides/rhinopython/#python-in-rhino)

For those that are familiar with the RhinoScript language in Rhino for Windows.  RhinoScriptSyntax is meant to duplicate the functionality provided by the RhinoScript language. If you are familiar with RhinoScript in Rhino for Windows the transition to Python in Rhino should be natural.

## RhinoCommon

RhinoCommon is an extensive, low level .NET library of the Rhino SDK. It is meant for more experienced programmers that would like to most extensive access to Rhino and its classes.

An important detail that will become important as you are learning to script Rhino with Python is that the implementation of Python that is embedded in Rhino is called IronPython: a Python implementation in C# that runs on the .Net/mono platform which means that in addition to the Python language features and the [rhinoscriptsyntax package](/api/RhinoScriptSyntax/win), you also have access to all the libraries in .Net/mono and [RhinoCommon](../../rhinocommon/what-is-rhinocommon/).

The rhinoscriptsyntax package is implemented on top of RhinoCommon so reading the source code is a great way to learn how to use RhinoCommon from Python.  The source code files are included in the Rhino distribution on your computer and the default location is:

```
/Users/<YOUR_HOME_DIRECTORY>/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/ironpython/settings/lib/rhinoscript
```

## Common Python Modules

There are many modules other modules for Python. Here are a list of the most useful to modules for Rhino.Python are:

* Date and Time
  * datetime — Basic date and time types
  * time — Time access and conversions
* Numeric and Mathematical Modules
  * math — Mathematical functions
  * fractions — Rational numbers
  * random — Generate pseudo-random numbers
* File and Directory Access
  * System.IO — Common pathname manipulations
  * tempfile — Generate temporary files and directories
  * csv — CSV File Reading and Writing
* String Services
  * string — Common string operations
  * StringIO — Read and write strings as files
  * fpformat — Floating point conversions

A complete list of predefined modules in Python, see the [Python Standard Library modules](https://docs.python.org/3/library/)

## Python Package Index (PyPI)

PyPI is a repository of software for the Python programming language with over 500,000 packages.  Popular PiPy cpackage are:

* Pandas - data analysis toolkit
* Numpy - popular scientific computing with Python
* Scipy - modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing
* pyyaml - human-readable YAML-serialized data
* Pillow - Python Imaging Library
* openpyxl - library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

The [PyPI website](https://pypi.org/) can be searched for the many packages that are availble. 


## Related Topics

- [What are Python and RhinoScriptSyntax?](/guides/rhinopython/what-is-rhinopython)
- [Python Basic Syntax](/guides/rhinopython/python-statements/)
- [Python Procedures](/guides/rhinopython/python-procedures/)
- [Rhinoscript Syntax in Python](/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
- [Rhino.Python Home Page](/guides/rhinopython/)
- [Python (homepage)](https://www.python.org/)
