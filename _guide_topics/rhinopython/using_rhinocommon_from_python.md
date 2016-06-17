---
title: Using RhinoCommon from Python
description: This brief guide cover using RhinoCommon from Python.
author: dan@mcneel.com
apis: ['RhinoPython', 'RhinoCommon']
languages: ['Python']
platforms: ['Cross-Platform']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/pythonandrhinocommon
order: 1
keywords: ['python', 'overview']
layout: toc-guide-page
TODO: 'needs more information.'
---

# {{ page.title }}

{{ page.description }}

## Overview

Along with the RhinoScript style functions you will be able to use all of the classes in the .NET Framework, including the classes available in RhinoCommon.  As a matter of fact, if you look at the source for the rhinoscriptsyntax functions, they are just python scripts that use RhinoCommon.  This allows you to do some pretty amazing things inside of a python script. Many of the features that once could only be done in a .NET plugin can now be done in a python script

For example, you can implement some custom drawing while a user is picking a point with the following script.  This script draws a Red and Blue line connected to the point under the mouse cursor while the user is picking a point.

```py
import Rhino
import System.Drawing

def GetPointDynamicDrawFunc( sender, args ):
  pt1 = Rhino.Geometry.Point3d(0,0,0)
  pt2 = Rhino.Geometry.Point3d(10,10,0)
  args.Display.DrawLine(pt1, args.CurrentPoint, System.Drawing.Color.Red, 2)
  args.Display.DrawLine(pt2, args.CurrentPoint, System.Drawing.Color.Blue, 2)

# Create an instance of a GetPoint class and add a delegate for the DynamicDraw event
gp = Rhino.Input.Custom.GetPoint()
gp.DynamicDraw += GetPointDynamicDrawFunc
gp.Get()
```
