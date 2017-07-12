---
title: Writing Customer Eto forms in Python
description: Using the Eto dialog framework to create customer dialogs.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Intermediate']
origin:
order: 2
keywords: ['script', 'Rhino', 'python', 'Eto']
layout: toc-guide-page
---

## Overview

[Eto is an open source cross-platform dialog box framework](https://github.com/picoe/Eto/wiki) available in Rhino 6.  Eto can be used in standalone applications, plugins and Rhino scripts to create advanced dialog boxes from within C#, C++ and Rhino.Python.

Rhino.Python comes with a series of [pre-defined user interface dialogs](/guides/rhinopython/python-user-input/).  But, if the pre-defined dialogs above are not enough for your purposes, a Eto dialog might be the right solution.

Here is an example, here is a custom collapsing dialog that uses many controls: 

![{{ site.baseurl }}/images/dialog-collapse.png]({{ site.baseurl }}/images/dialog-collapse.png){: .img-center  width="50%"}

The Eto framework allows creation of the dialog box, the establishment of the controls, the control and the actions executed by all the controls.

Eto is very powerful, but that power comes with more sophisticated specific Python syntax. Understanding how best to write, organize and use Eto dialogs will take some work.  This guide will cover the basics and best practices of creating Eto Dialogs in Python.  Some of the syntax may seem a little onerous, but in practice the following methods allow Eto code to efficiently be managed in Rhino.Python scripts. 

## The Eto framework

Conceptually an Eto dialog can be thought of as a set of layers:

![{{ site.baseurl }}/images/layered-form.svg]({{ site.baseurl }}/images/layered-form.svg){: .img-center  width="65%"}

Learning how each code each of these layers in Python is key to learing:

- [**Custom Dialog Class**](#custom-dlalog-class) - Extending the Eto Dialog/Form class is the best way to start a dialog.
- [**The Dialog Form**](#the-dialog-form).  The Dialog/Form is what all controls are built on top of.
- [**Eto Controls**](#eto-controls).  Controls such as labels, buttons and edit boxes can be created, then placed in a layout.
- [**The Layout**](#the-layout). Within each form, a layout is used to organize control positions.
- [**Control delegate**](#control-delegate). Any delegate actions must be bound to controls to manipulate and data with the control. 

Each of these layers will influence how the code is organized.  As an example of the layered approach of a dialog, here is a simple Eto Dialog with few controls.  The rest of this guide will cover the sections of this code in much more detail:

![{{ site.baseurl }}/images/dialog-sample-eto-room-number.png]({{ site.baseurl }}/images/dialog-sample-eto-room-number.png){: .img-center width="45%"}

The code for this dialog:

```python
# Imports
import Rhino
import scriptcontext
import System
import Eto
import Rhino.ui

# SampleEtoRoomNumber dialog class
class SampleRoomNumberDialog(Dialog[bool]):
    
    # Dialog box Class initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Sample Eto: Room Number'
        self.Padding = Padding(10)
        self.Resizable = False
        
        # Create controls for the dialog
        self.m_label = Label(Text = 'Enter the Room Number:')
        self.m_textbox = TextBox(Text = None) 
        
        # Create the default button
        self.DefaultButton = Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick

        # Create the abort button
        self.AbortButton = Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick

        # Create a table layout and add all the controls
        layout = DynamicLayout()
        layout.Spacing = Size(5, 5)
        layout.AddRow(self.m_label, self.m_textbox)
        layout.AddRow(None) # spacer
        layout.AddRow(self.DefaultButton, self.AbortButton)


        # Set the dialog content
        self.Content = layout

    # Start of the class functions

    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text

    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        self.m_textbox.Text = ""
        self.Close(False)

    # Close button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
            
    ## End of Dialog Class ##

# The script that will be using the dialog.
def RequestRoomNumber():
    dialog = SampleEtoRoomNumberDialog();
    rc = dialog.ShowModal(RhinoEtoApp.MainWindow)
    if (rc):
        print dialog.GetText() #Print the Room Number from the dialog control



##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    RequestRoomNumber()
```
{: .line-numbers}

This script is split into 3 main sections. 

1. The `Import` section to include the assemblies needed for the script.
2. The dialog class definition `SampleRoomNumberDialog()`
3. The script itself `RequestRoomNumber()` 

The Dialog definition does not have to appear in the same file as the python script.  By using the practice of creating a new class definitions for dialogs, the dialog definition may be in a separate file and then imported into any script. Or, a file could be created that contains many different dialogs as a Dialog library that could be included in any script. 


## Custom Dialog Class

As with most Python scripts the correct modules need to be imported so that the correct assemblies are accessable.  For an Eto dialog in Rhino, the Import section will include these:

```python
import Eto
import Rhino.Ui
```

Along the left column of the Python editor the methods within this Eto Assembly are listed.  For a detailed view of all the methods the Eto can be found in the [Eto.Forms API Documentation](http://api.etoforms.picoe.ca/html/R_Project_EtoForms.htm)  

The next section of the code creates a new class definition that extends a Eto class. [Creating classes in Python]({{ site.baseurl }}/guides/rhinopython/primer-101/7-classes/) requires some very specific syntax.  While it may seems little more complicated to create a class, the ability to reuse, import and interact with class based dialogs in Python scripts is well worth the practice.  A Class will contain the default information about the default layouts and actions of the class controls. The class will also be used to store all teh values of the controls for the while the script is running.  contain the values of

A dialog class is started with these lines:

```python
class SampleEtoViewRoomNumber(Dialog[bool]):
```

In this case the new class will be named `SampleEtoRoomNumberDialog` and extends the Eto class `Dialog[bool]`.  The `bool` argument shows that a Boolean value is expected back from the dialog.  This boolean value can be used to tell if the `OK` or `Cancel` button was hit when the dialog was exited. If more return values then True/False are need back from a dialog then a `Dialog[int]` or `Dialog[string]` might be needed.

There are a three main Eto class commonly used a a base class to extend:

1. **Dialog[T]** - A standard modal dialog template that returns an argument when closed.
2. **Semi-modal** - A special Rhino etension from the standard Dialog that allows the view to be manipulated while the dialog box is active.
3. **Form** - a non-modal form that can be used to interactively within Rhino.

This guide will only cover the the `Dialog[T]` dialog box.  The other dialog types may become useful for future projects.


## The Dialog Form  

Once the new class is declared, then the *init* instantiation operation to assign the defaults to the new dialog object when created.  Python uses the *self* variable in class declarations to reference the class members in the *init*. This of *self* as a placeholder for the class name once the class is actually created in the script. 

```python
class SampleEtoViewRoomNumber(Dialog[bool]):
    
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Sample Eto: Room Number'
        self.Padding = Padding(10)
        self.Resizable = False
```

The first section of the *init* is a few common properties that all dialogs have:

1. `self.Title` - Sets the title of the dialog.  
2. `self.Padding` - Set a blank border area within which any child content will be placed.  
3. `self.Resizable` - Whether the dialog box is resizable by dragging with the mouse.  

![{{ site.baseurl }}/images/dialog-properties.svg]({{ site.baseurl }}/images/dialog-properties.svg){: .img-center width="65%"}

There are a few `Padding` formats that are accepted. These match the margin and padding formats of standard CSS styling:

- Padding(10) - 10 pixel padding around all 4 sides.
- Padding(10, 20) - A padding of 10 to the left and right and a padding of 20 on top and bottom.
- Padding(10, 20, 30, 40) - A padding of 10 to the left, 20 to the top, 30 to the right and 40 to the bottom.

By default the dialog will automatically adjust its size to the contents it contains.  But an addition line can be added to set an initial size to the dialog using `self.ClientSize`:

```python
        self.ClientSize = Size(300, 400) #sets the (Width, Height)
```

Once the dialog foundation is formatted then a contents can be placed within the dialog using the `self.Content` property.  This is done on line 39. To create the contents for the dialog we will start to create some Controls.


## Eto Controls  

The business end of a dialog are the controls.  Controls may include Labels, Buttons, Edit boxes and Sliders. In Eto there are [more then 35 different controls](https://github.com/picoe/Eto/wiki/Controls) that can be created. 

Controls normally need to be setup properly before they are added to a layout in a dialog.  Here are some common control types:

### Label Control

The simplest control is the Label control.  It is simply a piece of text that normally is used to create a prompt, or label for another control.

![{{ site.baseurl }}/images/eto-label.svg]({{ site.baseurl }}/images/eto-label.svg){: .img-center width="65%"}

```python
        self.m_label = Label(Text = 'Enter the Room Number:')
```

As with many controls, the line above create a name for the control `m_label`.  Then the main property of a Label is the text it shows by setting the Text Property of the label.

Normally this is as complex as a label needs to be, but a label also has many more properties in addition to `Text`.  Properties include `VerticalAlignment`, `Horizontal Alignment`, `TextAlignment`, `Wrap`, `TextColor`, and `Font`. Additional properties can be added to the Text Property by useing a `,` for instance:

```python
        self.m_label = Label(Text = 'Enter the Room Number:', VerticalAlignment = VerticalAlignment.Center)
```

For a complete list of properties and events of Label, see the [Eto Label Class](http://api.etoforms.picoe.ca/html/T_Eto_Forms_Label.htm)

### TextBox Control

A TextBox is used to enter a string into the dialog.

![{{ site.baseurl }}/images/eto-textbox.svg]({{ site.baseurl }}/images/eto-textbox.svg){: .img-center width="65%"}

To check the contents of the textbox in the script, the textbox control must have a name to reference it.

```python
        self.m_textbox = TextBox() 
```

In this case the name `m_textbox` can be used to reference the control later in the class method starting on line 44:

```
    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text
```

Just creating a new `TextBox()` is common.  There are a numebr of additional properties of a TextBox which can be used to control the input. These properties include `MaxLength`, `PlaceholderText`, `InsertMode` and many more that can be seen in the [Eto TextBox Class](http://api.etoforms.picoe.ca/html/T_Eto_Forms_TextBox.htm).

### Button Controls

Buttons are placed on almost every dialog.  Buttons are created, then bound through their `.Click` event to run a method when the button is clicked. 

![{{ site.baseurl }}/images/eto-buttons.svg]({{ site.baseurl }}/images/eto-buttons.svg){: .img-center width="65%"}

Buttons can be assigned to any name. Along with the name, the `Text` property can be set to display on the button:

```python
        # Create the default button
        self.DefaultButton = Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick
```
Once created, the button then can be bound to an event method (`OnOKButtonClick`) through `.Click` class using the `+=` syntax as follows:

```python
        # Create the default button
        self.DefaultButton = Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick
```
The bound method is run if the button is clicked on.  The bound method is declared in the methods section later in the class:

```python
    # Close button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
```
In this case the button is clicked and the bound method `OnOKButtonClick` checks the Text of the `m_textbox` to to determine if anything has been entered. Then the method closes the dialog, returning either `True` or `False`.

The *Eto.Dialog class* has two special reserved names used in the sample code, the `DefaultButton` and the `AbortButton`.  The `DefaultButton` name will create a button that can be used as a standard button and receive a click event if the `Enter Key` is used.  The `AbortButton` is the button that is pressed if the `ESC` key is used.  These buttons are simple assigned through the name of the control.

This guide review the most basic controls.  To understand how to create and control more controls with Python see the Eto Controls in Python guide.

Once all the controls for the dialog are created then they can be placed in a layout to be positioned on a dialog.


## The Layout  

In the sample code a new Layout is created on line 30 in this section of the code:

```python
        # Create a table layout and add all the controls
        layout = DynamicLayout()
        layout.Spacing = Size(5, 5)
        layout.AddRow(self.m_label, self.m_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)


        # Set the dialog content
        self.Content = layout
```

The code for the layout comes further down in the class definition, because it seems to make sense to create the controls first before placing them in a layout. 

In this a case a new dynamic layout object is created at:

```python
        layout = DynamicLayout()
```

The [DynamicLayout](https://github.com/picoe/Eto/wiki/DynamicLayout) is one of [5 layout types](https://github.com/picoe/Eto/wiki/Containers) supported by Eto.  The Dynamic layout is a virtual grid that can organized controls both vertically and horizontally.

The spacing between controls in the layout is set by `layout.Spacing` on the line:

```python
        layout.Spacing = Size(5, 5)
```

The `Size(5, 5)` sets the horizontal spacing and vertical spacing of the controls to 5 pixels between the controls.

### Placing Rows

Once the Layout type has been setup then controls can be placed.   Control are placed into *Rows* in the layout.

![{{ site.baseurl }}/images/layout-rows.svg]({{ site.baseurl }}/images/layout-rows.svg){: .img-center width="65%"}

```python
        layout.AddRow(self.m_label, self.m_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
```

Each row can be added to the newly created `layout` object using the `.AddRow` method. Each control that is added in each row is given a cell on the row added.  So if two controls are added, the row will contain two cells that control the placement of the control.  The controls will stretch to fill up the cells.

The `DynamicLayout` can positioned controls vertically and horizontally. Each vertical set of controls can be aligned with controls in previous horizontal sections, giving a very easy way to build forms. For more information see the [Eto DynamicLayout documenation](https://github.com/picoe/Eto/wiki/DynamicLayout)

### Using None in a Layout.

Sometimes blank spacers are needed within a layout to help controls align properly. Sometimes blank cells need to be created to help align the number of cells from above.  Or a blanck rom may be needed to allow the hight of the layout to fill up the vertical space of the dialog.  In Python using the `None` value will allow for spacers.

In the sampel above a blank row is added between the controls:

```python
        layout.AddRow(None) # spacer
```
If the dialog box gets vertically taller, then the `None` row will expand to fill up the needed space.

`None` can also be used in a Row.  For instance the buttons could be dynamically justified to the right of the row by adding a `None` spacer at the start of the row:

```python
        layout.AddRow(None, self.DefaultButton, self.AbortButton)
```

The `None` cell will expand and contract to justify the buttons to the right.

There are many many options when using Layout, Rows and Cells with Eto to place controls.  For more information on the details of using Layouts see the Eto Layout advanced Options with Python


## Control delegate  

## Sample dialogs  

Now with some understanding of Eto Dialogs in Python, take a look at some of the Sample dialogs in the Python Developer Samples Repo:

1.  


2.  
3. ​

---

## Related Topics

- [Reading and Writing files with Python]({{ site.baseurl }}/guides/rhinopython/python-reading-writing)
- [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)
- [Eto Forms in Python]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/) guide
