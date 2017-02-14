---
title: Creating a script and module 
description: How to create a Python definition that is both a importable module and a script.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Intermediate']
origin:
order: 76
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Overview

A Python script normally can be full of functions that can be imported as a library of functions in other scripts, or a python script can be a command that runs in Rhino.  

There is a way to have Python definitions be both a library of functions and a direct command.

The key is to add these statments to the end of the file:

```python
if __name__ == '__main__':
    CreateCircle()  # Put the a call to the main function in the file.    
```

## A complete script example

Here is a complete Python sample that shows how the the `if __name__ == '__main__':` statement can be added to a Python script:

```python
# Create a circle from a center point and a circumference.
import rhinoscriptsyntax as rs
import math

def CreateCircle(circumference=None):
    center = rs.GetPoint("Center point of circle")
    if center:
        plane = rs.MovePlane(rs.ViewCPlane(), center)
        length = circumference
        if length is None: length = rs.GetReal("Circle circumference")
        if length and length>0:
            radius = length/(2*math.pi)
            objectId = rs.AddCircle(plane, radius)
            rs.SelectObject(objectId)
            return length
    return None

# Check to see if this file is being executed as the "Main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == '__main__':
    CreateCircle()

```

The CreateCricle file above will run as a script to create a circle.  But it can be used in the *UseModule.py* scipt as an imported module, as follows:

```python
# This script uses a function defined in the CircleFromLength.py
# script file
import CircleFromLength

# call the function a few times just for fun using the
# optional parameter
length = CircleFromLength.CreateCircle()
if length is not None and length>0.0:
    for i in range(4):
        CircleFromLength.CreateCircle(length)
```

## How it works

When the Python interpreter reads a source file, it executes all of the code found in it.

Before executing the code, it will define a few special variables. If Python is running the file as the main program then Ptyhon will create a `__name__` variable with the value of *__main__*. If python is importing the file as an import into an allready running *__main__* the `__name__` variable will be set to the module's name in the modules scope.

One of the reasons for doing this is that sometimes you write a module (a .py file) where it can be executed directly. Alternatively, it can also be imported and used in another module. By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
