---
title: How to get user input in a script 
description: How to prompt the user for input into a script.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['intermediate']
origin:
order: 75
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Overview

Prompting the user of a script fo the input of a value, point in space, a Rhino object is important to many interactive scripts.

The RhinoscriptSyntax module contains many ways to interactively prompt for several different types of input.

- Values (strings or numbers)
- Pick Point(s)
- Select object(s)

Like many input methods, not only are the values captured, but they also can be validated so that only the proper input is accepted.


## The GET methods

GetPoint():

 Use rs.GetPoint() to ask the user for a single point location, say for the center of a circle. LIke most if not all of the Get methods, rs.GetPoint() allows you to specify some parameters- in this case they are all optional, the function will run without any of them specified in the code you type. For example, the default prompt is "Pick point", but you can specify a different prompt, for example, "Set center point" depending on what you wish to convey to the user. 
```python
pt = rs.GetPoint("Set center point")
```python

If the function succeeds, a Rhino point is returned, which can be treated as a list of three numbers representing the world x, y and z coordinates of the point. 

```python
import rhinoscriptsyntax as rs
pt = rs.GetPoint("Click to get information about a point location")
if pt is not None:# note it is a good idea to check if there is a result you can use
    print "That point has an x coordinate of " + str(pt[0])
```python


GetPoints()
Use rs.GetPoints() to ask the user for multiple point locations. As in rs.GetPoint(), all parameters are optional. Note that there is a separate prompt for the first point, and a second one for subsequent points. 

You need to set the parameters in order, separated by commas. If you do not want to specify a paramter at all, and accept the default, you can leave it out but you must then specify any following parameters explicitly using the parameter name. For example, this will not work to set a custom first prompt:
```python
import rhinoscriptsyntax as rs

pts = rs.GetPoints(  "Set the first point", "Set the next point")
```python

Why? because the function has two paramters that come before the first prompt, 'draw_lines' and 'in_plane'. If you leave these out, you must specify what paramters you are setting explicitly in order for it to be recognized:

```python
import rhinoscriptsyntax as rs
pts = rs.GetPoints(  message1= "Set the first point", message2= "Set the next point")
```python

You could also make sure to set the other parameters even if you don't care what they are i.e. defaults are OK:
```python
import rhinoscriptsyntax as rs
pts = rs.GetPoints( None, None, "Set the first point", "Set the next point")
```python



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
