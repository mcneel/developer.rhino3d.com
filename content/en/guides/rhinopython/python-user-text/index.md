+++
aliases = ["/5/guides/rhinopython/python-user-text/", "/6/guides/rhinopython/python-user-text/", "/7/guides/rhinopython/python-user-text/", "/wip/guides/rhinopython/python-user-text/"]
authors = [ "scottd" ]
categories = [ "intermediate" ]
description = "How to create and access customer user text with Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Custom information on objects"
type = "guides"
weight = 35
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## User Text

The Rhino allows developers to store custom information on Rhino objects and inside the Rhino 3DM file.  This data is referred to as User Text.  There are two types of user text:

1.Document user text - custom strings that is stored at the document level of the 3DM file.
2.Object user text - custom strings that are attached to either an object's geometry or an object's attributes.

Important. When storing custom data on an object, the data can be stored on either the object's geometry (e.g. curve, surfaces, etc), or on the object's attributes. An object's attributes maintain it's layer, color and other non-geometric properties. The difference between the two storage methods is that adding or modifying user data that is located on an object's geometry will cause Rhino to place a copy of the object on the Undo stack. Thus, if you are working with large geometric object or lots of user data, it is more efficient to store object user data on an object's attributes.

RhinoScript supports both document user data and object user data.  The RhinoScript user data object organizes custom information by Key:Value pairs similar to that of a Windows-style initialization (INI) file or a single layer Python dictionary.  For example:

```
[Section1]  
Key1:String1  
Key2:String2
...  

[Section2]  
Key1:String1  
Key2:String2  
...
```
 
The `Section` value normally is normally a unique name for all the data you might store.

The RhinoScriptSyntax functions only store string values. Fortunetly a Python string can be easily converted from one data type to another if needed.

User Text Methods

Rhino provides a standardized mechanism for users, script writers, and plug-in developers to store and retrieve simple text information on an object and in the document. This mechanism called User Text.

Unlike RhinoScript's User Data methods, which stores data as Section/Entry/String, Rhino stores User Text key/value pairs.

Rhino supports this method of storing object data with its GetUserText, SetUserText, GetDocumentUserText and SetDocumentUserText commands. RhinoScript supports this mechanism with the GetUserText, SetUserText, GetDocumentUserText, and SetDocumentUserText methods. User text can be stored on layers by using the GetLayerUserText and SetLayerUserText methods. User text can be stored on groups using the GetGroupUserText and SetGroupUserText methods.

Runtime Data

When you declare a variable within a procedure, the variable can only be accessed within that procedure. When the procedure exits, the variable is destroyed. These variables are called local variables.

If you declare a variable outside a procedure, all procedures can access it. These variables are called global variables. The lifetime of these variables starts when they are declared, and ends when Rhino is closed. Note, if the Reinitialize script engine when opening new models option is enabled, all variables and procedures are destroyed when a new model is opened.

RhinoScript maintains a runtime data dictionary that you can use to store data. Runtime data is similar to global variables in that it can be accessed from all procedures. But unlike global variables, the runtime data will not be destroyed if the script engine is reinitialized. Runtime data persists until Rhino is closed. Runtime data can be stored and retrieved using the GetRuntimeData and SetRuntimeData methods.

User Data Methods





Method
 
Description
 

AttributeDataCount
 
Returns the number of RhinoScript user data items stored on an object's attributes.
 

DeleteAttributeData
 
Removes RhinoScript user data stored on an object's attributes.
 

DeleteDocumentData
 
Removes RhinoScript user data stored in the current document.
 

DeleteObjectData
 
Removes RhinoScript user data stored on an object's geometry.
 

DocumentDataCount
 
Returns the number of RhinoScript user data items stored in the current document.
 

GetAttributeData
 
Returns a RhinoScript user data item stored on an object's attributes.
 

GetDocumentData
 
Returns a RhinoScript user data item stored in the current document.
 

GetDocumentUserText
 
Returns user text that is stored in the document.
 

GetGroupUserText
 
Returns user text that is stored on a group.
 

GetLayerUserText
 
Returns user text that is stored on a layer.
 

GetObjectData
 
Returns a RhinoScript user data item stored on an object's geometry.
 

GetRuntimeData
 
Retrieves data from RhinoScript's runtime data dictionary.
 

GetUserText
 
Returns user text that is stored on an object.
 

IsAttributeData
 
Verifies that an object's attributes contains RhinoScript user data.
 

IsDocumentData
 
Verifies that the current document contains RhinoScript user data.
 

IsDocumentUserText
 
Verifies that the document contains user text.
 

IsObjectData
 
Verifies that an object's geometry contains RhinoScript user data.
 

IsUserText
 
Verifies that an object contains user text.
 

ObjectDataCount
 
Returns the number of RhinoScript user data items stored on an object's geometry.
 

RuntimeDataCount
 
Returns the number of key/value pairs in RhinoScript's runtime data dictionary.
 

SetAttributeData
 
Adds or sets a RhinoScript user data item stored on an object's attributes.
 

SetDocumentData
 
Adds or sets a RhinoScript user data item stored in the current document.
 

SetDocumentUserText
 
Sets or removes user text stored in the document.
 

SetGroupUserText
 
Sets or removes user text stored on a group.
 

SetLayerUserText
 
Sets or removes user text stored on a layer.
 

SetObjectData
 
Adds or sets a RhinoScript user data item stored on an object's geometry.
 

SetRuntimeData
 
Adds, modifies, or removes data from RhinoScript's runtime data dictionary.
 

SetUserText
 
Sets or removes user text stored on an object.
 



## Overview

Prompting the user of a script fo the input of a value, selecting a layer, picking a point or selecting a Rhino object is important to many interactive scripts.

The RhinoscriptSyntax module contains many ways to interactively prompt for several different types of input. There are three main styles of input that are contained in Rhinosciptsyntax:

- Get methods. These are methods that work with the command line, wait for mouse input or prompt for specifc input.
- Dialog methods.  There are some simple specfic dialogs to prompt for input
- File sytem dialogs. Browsing, saving and opening files on the system with Python.

Many input methods will also validate the user input to make sure only the proper input is accepted.

rs.SetDocumentUserText





### The GET methods


#### GetPoint()


 Use `rs.GetPoint()` to ask the user for a single point location, say for the center of a circle. Like most if not all of the Get methods, rs.GetPoint() allows you to specify some parameters- in this case they are all optional, the function will run without any of them specified in the code you type. For example, the default prompt is "Pick point", but you can specify a different prompt, for example, "Set center point" depending on what you wish to convey to the user.
 
```python
pt = rs.GetPoint("Set center point")
```

If the function succeeds, a Rhino point is returned, which can be treated as a list of three numbers representing the world x, y and z coordinates of the point. 

```python
import rhinoscriptsyntax as rs
pt = rs.GetPoint("Click to get information about a point location")
if pt is not None:# note it is a good idea to check if there is a result you can use
    print "That point has an x coordinate of " + str(pt[0]) # when you build a string that includes elements that are not text, convert to a string with str()
```


#### GetPoints()

Use `rs.GetPoints()` to ask the user for multiple point locations. As in rs.GetPoint(), all parameters are optional. Note that there is a separate prompt for the first point, and a second one for subsequent points. 

You need to set the parameters in order, separated by commas. If you do not want to specify a paramter at all, and accept the default, you can leave it out but you must then specify any following parameters explicitly using the parameter name. For example, this will not work to set a custom first prompt:

```python

import rhinoscriptsyntax as rs

pts = rs.GetPoints(  "Set the first point", "Set the next point")
```

Why? because the function has two paramters that come before the first prompt, 'draw_lines' and 'in_plane'. If you leave these out, you must specify what paramters you are setting explicitly in order for it to be recognized:

```python
import rhinoscriptsyntax as rs
pts = rs.GetPoints(  message1= "Set the first point", message2= "Set the next point")
```

You could also make sure to set the other parameters even if you don't care what they are i.e. defaults are OK:

```python
import rhinoscriptsyntax as rs
pts = rs.GetPoints( None, None, "Set the first point", "Set the next point")
```



#### Getreal()

Another common Get method is prompting for a *number* on the commandline with `rs.GetReal()`.

```python
import rhinoscriptsyntax as rs

# GetReal prompts on the command line with optional defaults and a minimum allowable value
radius = rs.GetReal("Radius of new circle", 3.14, 1.0)
if radius: rs.AddCircle( (0,0,0), radius )
```
rs.GetReal() accepts any number, including decimals. In some cases your code may need only whole numbers- in this case use `rs.GetInteger()`

There are 22 different Get methods. For details on all the Get functions in RhinoScriptSyntax for Python go to the [RhinoScriptSyntax User interface methods](/api/rhinoscriptsyntax/#userinterface)

## Dialog Methods


The Dialog methods in RhinoScript syntax are used to prompt of with generic custom information. Dialogs can be used to draw more attention to a required interaction with the user.  Dialogs generally interrupt the workflow - the script cannot continue until the dialog is dealt with by the user.

#### MessageBox()

The simplest dialog box is the `rs.MessageBox()` function.  The rs.MessageBox() comes with many options to customize the buttons based on your needs:

```python
import rhinoscriptsyntax as rs

rs.MessageBox("Hello Rhino!") # Simple message dialog
rs.MessageBox("Hello Rhino!", 4 | 32) # A Yes, No dialog
rs.MessageBox("Hello Rhino!", 2 | 48) # An Abort, Retry dialog
```


<img src="/images/yes_no-dialog.png" alt="RunPythonScript" width="35%">


Note that rs.MessageBox() returns a value - you can set a variable to record the result from a message box so that you can tell which button the user has clicked.

```python
import rhinoscriptsyntax as rs

button = rs.MessageBox("Hello Rhino!", 2 | 48) # An Abort, Retry dialog
```
The value of 'button' in the code above will tell the script which button was clicked and it can proceed appropriately. See the Rhino IronPython Help for details on the available buttons and the return codes from rs.MessageBox()

#### ListBox()

Some of the more advanced dialogs can be polulated with custom selections:

```python
import rhinoscriptsyntax as rs

options = ('First Pick', 'Second Pick', 'Third Pick')
if options:
    result = rs.ListBox(options, "Pick an option")
    if result: rs.MessageBox( result + " was selected" )
```
Here is a list of dialog box methods:

| Method | | | Description |
|:-------|-|-|:------------|
| CheckListBox | | | Displays a list of strings in a checkable list. The user can pick multiple items.|
| ComboListBox | | | Displays a list of strings in a combo list. |
| EditBox | | | Displays a dialog box with a multi-line edit control. |
| ListBox | | | Displays a list of strings in a simple list box. The user can pick one item.|
| MessageBox | | | Displays a Windows message box. |
| PopupMenu | | | Displays a context-like popup menu. |
| PropertyListBox | | | Displays a list of items and values in a property list. |
| RealBox | | | Displays a dialog box prompting the user to enter a number. |
| StringBox | | | Displays a dialog box prompting the user to enter a string. |

For details on all the dialog box functions in RhinoScriptSyntax for Python go to the [RhinoScriptSyntax User interface methods](/api/rhinoscriptsyntax/#userinterface)

## File System dialogs

Working with files and folders on the computer take a special class of dialogs. 

```python
import rhinoscriptsyntax as rs

filename = rs.OpenFileName()
if filename: rs.MessageBox(filename)
```

<img src="/images/openfile_dialog.png" alt="RunPythonScript" width="55%">

| Method | | | Description |
|:-------|-|-|:------------|
| BrowseForFolder | | | Displays a Windows browse-for-folder dialog box. |
| OpenFileName | | | Displays a Windows file open dialog box. |
| OpenFileNames | | | Displays a Windows file open dialog box. |
| SaveFileName | | | Displays a Windows file save dialog box. |

## Related Topics

- [Reading and Writing files with Python](/guides/rhinopython/python-reading-writing)
- [RhinoScriptSyntax User interface methods](/api/rhinoscriptsyntax/#userinterface)



