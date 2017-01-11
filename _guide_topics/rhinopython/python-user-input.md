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

Prompting the user of a script fo the input of a value, selecting a layer, picking a point or selecting a Rhino object is important to many interactive scripts.

The RhinoscriptSyntax module contains many ways to interactively prompt for several different types of input. There are three main styles of input that are contained in Rhinosciptsyntax:

- Get methods. These are methods that work with the command line, wait for mouse input or prompt for specifc input.
- Dialog methods.  There are some simple specfic dialogs to prompt for input
- File sytem dialogs. Browsing, saving and opening files on the system with Python.

Many input methods will also validate the user input to make sure only the proper input is accepted.

## The GET methods

<<<<<<< HEAD
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


=======
The most popular input methods are the Get methods.  These methods prompt for very specific information and return a simple object or list of objects.  

An common starting example is 'GetPoint()'.  Use GetPoint() to prompt and get a 3dPoint from Rhino.  Here is how to draw a simple line:

```python
import rhinoscriptsyntax as rs

point1 = rs.GetPoint("Pick first point")  # Prompt for the first point.
if point1: # considered valid only if a point is entered
    rs.AddPoint(point1)
    point2 = rs.GetPoint("Pick second point", point1) #Prompt for the second point while drawing a rubber band line to the first point.
    if point2:
        rs.AddLine(point1, point2)
```

A common practice when working with user input is to use `if` statements to amke sure a value was actually entered or selected.  In Python the `if` statement considers a non null values valid to contiue on.

Another common Get method is prompting for a number on the commandline with `GetReal()`:

```python
import rhinoscriptsyntax as rs
# GetReal prompts on the command line with optional defaults and a minimum allowable value
radius = rs.GetReal("Radius of new circle", 3.14, 1.0)
if radius: rs.AddCircle( (0,0,0), radius )
```
There are 22 different Get methods. For details on all the Get functions in RhinoScriptSyntax for Python go to the [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)

## Dialog Methods
>>>>>>> ab96ca6bfdd27924a53d3ee55b00bdfdcd909fc5

The Dialog methods in RhinoScript syntax are used to prompt of with generic custom information. Dialogs can be used to draw more attention to a required interaction with the user.  

The simplest dialog box is the `MessageBox()` function.  The `MessageBox()` comes with many options to customize the buttons based on your needs:

```python
import rhinoscriptsyntax as rs

rs.MessageBox("Hello Rhino!") # Simple message dialog
rs.MessageBox("Hello Rhino!", 4 | 32) # A Yes, No dialog
rs.MessageBox("Hello Rhino!", 2 | 48) # An Abort, Retry dialog
```
<img src="{{ site.baseurl }}/images/yes_no-dialog.png" alt="RunPythonScript" width="35%">

Some of the more advanced dialogs can be polulated with custom selections:

```python
import rhinoscriptsyntax as rs

options = ('First Pick', 'Second Pick', 'Third Pick')
if options:
    result = rs.ListBox(options, "Pick an option")
    if result: rs.MessageBox( result + " was selected" )
```
Here are a list of dialog box methods:

| Method | | | Description |
|:-------|-|-|:------------|
| CheckListBox | | | Displays a list of strings in a checkable list. |
| ComboListBox | | | Displays a list of strings in a combo list. |
| EditBox | | | Displays a dialog box with a multi-line edit control. |
| ListBox | | | Displays a list of strings in a simple list box. |
| MessageBox | | | Displays a Windows message box. |
| PopupMenu | | | Displays a context-like popup menu. |
| PropertyListBox | | | Displays a list of items and values in a property list. |
| RealBox | | | Displays a dialog box prompting the user to enter a number. |
| StringBox | | | Displays a dialog box prompting the user to enter a string. |
|=====
|
{: rules="groups"}

For details on all the dialog box functions in RhinoScriptSyntax for Python go to the [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)

## File System dialogs

Working with files and folders on the computer take a special class of dialogs. 

```python
import rhinoscriptsyntax as rs

filename = rs.OpenFileName()
if filename: rs.MessageBox(filename)
```
<img src="{{ site.baseurl }}/images/openfile_dialog.png" alt="RunPythonScript" width="55%">

| Method | | | Description |
|:-------|-|-|:------------|
| BrowseForFolder | | | Displays a Windows browse-for-folder dialog box. |
| OpenFileName | | | Displays a Windows file open dialog box. |
| OpenFileNames | | | Displays a Windows file open dialog box. |
| SaveFileName | | | Displays a Windows file save dialog box. |
|=====
|
{: rules="groups"}

For details on all the dialog box functions in RhinoScriptSyntax for Python go to the [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)

