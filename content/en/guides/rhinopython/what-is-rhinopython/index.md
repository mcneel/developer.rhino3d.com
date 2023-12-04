+++
aliases = ["/5/guides/rhinopython/what-is-rhinopython/", "/6/guides/rhinopython/what-is-rhinopython/", "/7/guides/rhinopython/what-is-rhinopython/", "/wip/guides/rhinopython/what-is-rhinopython/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "This guide is an overview of Python in Rhino."
keywords = [ "python", "overview" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "What is Rhino.Python?"
type = "guides"
weight = 1
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = "needs more GHPython info."
origin = "http://wiki.mcneel.com/developer/python"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
version = [ "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++


{{< alt-version "https://developer.rhino3d.com/guides/rhinocommon/moving-to-dotnet-7/" "This guide is for Rhino 8 Python 3  For Rhino 7 Python 2? Click here!">}}

...but a better question is...

## What is Python?

[Python](https://www.python.org/) is a *modern programming language*. Python is sometimes called a scripting language or a glue language.  This means python is used often to run a series of commands as a script or used to create links between two other technologies as a glue. It is easier to learn and use than other non-scripting style, compiled languages like C#, VB, or C/C++.  Yet it is quite powerful.

Python is [interpreted](https://en.wikipedia.org/wiki/Programming_language_implementation), meaning it is executed one line at a time.  This makes the program flow easy to understand.  Also it is [semantically dynamic](https://en.wikipedia.org/wiki/Programming_language#Static_versus_dynamic_typing) which allows the syntax to be less restrictive and less formal when using declarations and variables types.  These characteristics add to Python's ease-of-use for basic programming tasks.

You may need Python if you want to:

- Automate a repetitive task in Rhino much faster than you could do manually.
- Perform tasks in Rhino or Grasshopper that you don't have access to in the standard set of Rhino commands or Grasshopper components.
- Generate geometry using algorithms.
- Many, many other things.  It is a programming language after all.

## Why Python?

Why should you use Python?  Well, Python is meant to be a simple language to read and write. Python also runs both the Windows and Mac versions of Rhino.  Since Rhino Python scripting is available on both platforms, the same Python scripts can run on both breeds of Rhino! Python also will run within a Grasshopper component.

But more importantly: Python is very popular outside of Rhino! Much of what you learn about Python can be applied in many other domains.

Rhino already has a scripting language called RhinoScript why do we need another?  RhinoScript is a very easy to use scripting language on Windows. We will continue to support Rhinoscript.  But, RhinoScript is based on an little older technology making it less flexible then the more modern Python language. RhinoScript cannot be supported on the Mac platform.  It also unfortunately is not supported by the commnuity to the same level as Python.

### What version of Python does Rhino use?

Rhino uses Python version 2.7. To be more specific Rhino uses [IronPython](http://ironpython.net/) which brings together the Python language and [Microsoft's .NET framework](https://en.wikipedia.org/wiki/.NET_Framework).

## Where can you use Python in Rhino?

Python can be used all over Rhino in many different ways. Python can be used to create

- Interactive scripts.
- New custom commands.
- Create new plug-ins.
- Read and Write customized file formats.
- Interact with cloud applications.
- Create realtime links to other applications
- Create customer Grasshopper components
- Store and display project specific information beyond what basic Rhino can store.

#### RhinoScript Style Functions

One of the key features of RhinoScript that make it easy to write powerful scripts is a large library of Rhino specific functions that can be called from scripts.  Our python implementation includes a set of similar functions that can be imported and used in any python script for Rhino.  This set of functions is known as the `rhinoscriptsyntax` package.

Let's compare scripts for letting a user pick two points and adding a line to Rhino...

Here's RhinoScript:

```vbnet
Dim arrStart, arrEnd
arrStart = Rhino.GetPoint("Start of line")
If IsArray(arrStart) Then
  arrEnd = Rhino.GetPoint("End of line")
  If IsArray(arrEnd) Then
    Rhino.AddLine arrStart, arrEnd
  End If
End If
```

compared with Python:

```py
import rhinoscriptsyntax as rs

start = rs.GetPoint("Start of line")
if start:
  end = rs.GetPoint("End of line")
  if end: rs.AddLine(start,end)
```

Yes, different...but similar enough that you should be able to figure out what is happening in python if you've written RhinoScript. Rhinoscriptsyntax also contains many helper functions to make it easier to program with in Python.

For more information on how to use Rhinoscriptsyntax and Python, see the [Rhino.Python Guide](/guides/rhinopython/)


#### Grasshopper

Python can also be used in Grasshopper to create custom components within a larger grasshopper definition. The GhPython component contains a Python script editor and direct access to Python, Rhino and Grasshopper functions.  Use GhPython to create and manipulate customer data within Grasshopper.

For an introduction to GhPython in Grasshopper, see the [Your First Python Script in Grasshopper Guide](/guides/rhinopython/your-first-python-script-in-grasshopper)

#### RhinoCommon

[Rhinocommon](/guides/rhinopython/what-is-rhinocommon/) is a low-level powerful SDK for all Rhino platforms used mainly by more experienced developers.  Python scripts can use Rhinocommon, to have full access to the .NET framework including access to Rhino's RhinoCommon SDK.  A guide of accessing RhinoCommon from Python scripts is at [Using RhinoCommon from Python](/guides/rhinopython/using-rhinocommon-from-python).

## Related Topics

- [Python Basic Syntax](/guides/rhinopython/python-statements/)
- [Rhinoscript Syntax in Python](/guides/rhinopython/python-rhinoscriptsyntax-introduction/)
- [Rhino.Python Home Page](/guides/rhinopython/)
- [Python (homepage)](https://www.python.org/)
