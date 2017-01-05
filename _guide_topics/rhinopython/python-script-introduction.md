---
title: Python Scripting in Rhino
description: This guide provides an overview of the scripting with Python in Rhino.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['python-scripting']
origin:
order: 1
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Introduction

The Python language is a comprehensive programming language for both Windows, Macintosh and Grasshopper platforms. Python is meant to be a easy-to-learn language. Python is a great language for people that are not programmerrs and whom are just learning.

A key characteristic of python is that there is very few extra characters allowing the code to be shorter and potentially easier to read.  For more information on the history and development of Python, see [Python (programming language) on Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language)). Python is [open source](https://opensource.com/resources/what-open-source) and managed by the [Python Software Foundation](https://www.python.org/psf/)

We have added additional libraries to Python in the form of RhinoScriptSyntax and RhinoCommon. These libraries allow Python to be aware of Rhino and Grasshopper:

* Geometry
* Commands
* Document objects
* Application methods

Rhinoscript syntax is the easiest to use and learn library. To make these methods easy-to-use, all RhinoScriptSyntax methods return simple Python variables or Python List-based data structures. Thus, once you are familiar with Python, you will be able to use any and all functions in the RhinoScriptSyntax methods library.

RhinoCommon is an extensive, low level .NET library of the Rhino SDK. It is meanst for more experienced programmers that would like to most extensive access to Rhino and its classes.

This document introduces the built-in Script editor in Rhino and using Python with RhinoSciptSyntax to automate Rhino.

## Getting help

The information in this help file pertains to the usage of the RhinoScriptSyntax libraries. Additional support for Python in Rhino can be obtained from the following resources.

[McNeel Developer Documentation]({{ site.baseurl }}/guides/rhinopython)
[Rhino Scripting Forum](https://discourse.mcneel.com/c/scripting)

---
