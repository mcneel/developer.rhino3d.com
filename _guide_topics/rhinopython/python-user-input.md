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

