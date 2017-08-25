---
title: Eto control syntax in Python
description: Using the Eto dialog framework to create dialog controls.
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

## The Eto Controls  

[Eto is an open source cross-platform dialog box framework](https://github.com/picoe/Eto/wiki) available in Rhino 6.  This guide shows the syntax required to create the most common Eto controls in Rhino.Python.  Controls include Labels, Buttons, Edit boxes and Sliders. In Eto there are [more then 35 different controls](https://github.com/picoe/Eto/wiki/Controls) that can be created.

For details on creating the rest of an Eto Dialog in Rhino.Python go to the [Getting Started with Eto article]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/)

## Button Controls

Buttons are placed on almost every dialog.  

![{{ site.baseurl }}/images/dialog-sample-eto-buttons.png]({{ site.baseurl }}/images/dialog-sample-eto-buttons.png){: .img-center}

Creating a new button is simple completed by specifying the `Text` shown on the button face. In addition to creating the new button, commonly the `.Click` event is bound to a method usein the `+=` syntax as shown below.

```python
        self.m_button = forms.Button(Text = 'OK')
        self.m_button.Click += self.OnButtonClick
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

The *Eto.Dialog class* has two special reserved names for buttons, the `DefaultButton` and the `AbortButton`.  The `DefaultButton` name will create a button that is a standard button and also will receive a click event if the `Enter Key` is used. The `AbortButton` is a button that recieves a `.Click` event if the `ESC` key is used.  These buttons are simple assigned through the name of the control, using `self`  syntax.

The syntax for the `DefaultButton` is:

```python
self.DefaultButton = forms.Button(Text = 'OK')
```

And for the `AbortButton` is:

```python
self.AbortButton = forms.Button(Text = 'Cancel')
```

## Calendar

Calendar control to pick a date or range of dates

![{{ site.baseurl }}/images/dialog-sample-eto-buttons.png]({{ site.baseurl }}/images/eto-controls-calendar.png){: .img-center}

```python
    #Create a Calender
    self.m_calender = forms.Calendar()
```

There are a number of properties of a calender control that can be used to modify how the ccontrol works.

```python
    #Create a Calendar
    self.m_calendar = forms.Calendar()
    self.m_calendar.Mode = forms.CalendarMode.Single
    self.m_calendar.MaxDate = System.DateTime(2017,7,31)
    self.m_calendar.MinDate = System.DateTime(2017,7,1)
```

## CheckBox

Check box with text label.

```python
    #Create a Checkbox
    self.m_checkbox = forms.CheckBox(Text = 'My Checkbox')
```

By default the CheckBox is unchesked and carries a value of *None*.  Once checked it contains a booloean value of True.

The intial state of the checkbox can be set.  The checkbox will be checked by default by adding the line:

```python
    self.m_checkbox.Checked = True
```

## ColorPicker

Pick a single color drop down color picker. Also supports a right-click on the dropdown arrow to support eye dropper and the stanrd system color picker dialog.

```python
        #Create a ColorPicker Control
        self.m_colorpicker = forms.ColorPicker()
```

This will create a color picker with a blank default color.  A default color may be set in the control by adding:

```python
        defaultcolor = Eto.Drawing.Color.FromArgb(255, 0,0)
        self.m_colorpicker.Value = defaultcolor
```

## ComboBox

Text entry with a drop down list of items



## DateTimePicker

Control to enter a date and/or time

## Drawable

Owner-drawn control using Graphics object

## DropDown

Drop down with a list of items.

```python
        #Create Dropdown List
        self.m_dropdownlist = forms.DropDown()
        self.m_dropdownlist.DataStore = ['first', 'second', 'third']
```

The default selection can be set in the list by using the DataStore property:

```python
        self.m_dropdownlist.SelectedIndex = 1
```

## GridView

A virtualized grid of data with editable cells

## GroupBox

A panel with a border and optional title

## ImageView

A view to display a single image

## Label Control

The simplest control is the Label control.  It is simply a piece of text that normally is used to create a prompt, or label for another control.

![{{ site.baseurl }}/images/eto-label.svg]({{ site.baseurl }}/images/eto-label.svg){: .img-center width="65%"}

```python
        self.m_label = forms.Label(Text = 'Enter the Room Number:')
```

As with many controls, the line above create a name for the control `m_label`.  Then the main property of a Label is the text it shows by setting the Text Property of the label.

Normally this is as complex as a label needs to be, but a label also has many more properties in addition to `Text`.  Additonal properties include `VerticalAlignment`, `Horizontal Alignment`, `TextAlignment`, `Wrap`, `TextColor`, and `Font`. Properties can be added to the Text Property by using a comma(`,`):

```python
        self.m_label = forms.Label(Text = 'Enter the Room Number:', VerticalAlignment = VerticalAlignment.Center)
```

For a complete list of properties and events of the Label class, see the [Eto Label Class](http://api.etoforms.picoe.ca/html/T_Eto_Forms_Label.htm) documentation.

## LinkButton

A simple label that acts like a button, similar to a hyperlink

## ListBox

A scrollable list of items

## ListControl

Base for ListBox, DropDown, ComboBox, and other list-type controls

## MaskedTextBox

TextBox for variable or fixed length masks

## NumericUpDown

Numeric control that allows the user to adjust the value with the mouse

## Panel

A blank panel container to add other controls

## PasswordBox

Enter passwords or sensitive data

## ProgressBar

Show progress of long running tasks

## RadioButton

Used in a group of radio buttons to allow user to select from values

## RadioButtonList

Manages a list of radio buttons

## RichTextArea

## Multi-line

text area with rich text formatting

## Scrollable

A scrollable container

## SearchBox

A text box with search-box functionality

## Slider

A horizontal or vertical slider to select a value from a range

## Spinner

A spinner to show indeterminate progress in compact space

## Splitter

Splits two panes horizontally or vertically

## TabControl

Presents multiple TabPage containers which the user can select

## TabPage

A single page of a TabControl

## TextArea

Multi-line text control with scrollbars

## TextBox Control

A TextBox is used to enter a string into the dialog.

![{{ site.baseurl }}/images/eto-textbox.svg]({{ site.baseurl }}/images/eto-textbox.svg){: .img-center width="65%"}

To check the contents of the textbox in the script, the textbox control must have a name to reference it.

```python
        self.m_textbox = forms.TextBox()
```

In this case the name `m_textbox` can be used to reference the control later in the class method starting on line 44:

```
    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text
```

Just creating a new `Eto.Forms.TextBox()` is common.  There are a number of additional properties of a TextBox which can be used to control the input. These properties include `MaxLength`, `PlaceholderText`, `InsertMode` and many more that can be seen in the [Eto TextBox Class](http://api.etoforms.picoe.ca/html/T_Eto_Forms_TextBox.htm).


TextControl - Base for any control that contains text
TreeView - A control to present nodes in a tree
TreeGridView - A TreeView with columns
WebView - Control to present a web page through a url or static HTML


## Sample dialogs  

Now with some understanding of Eto Dialogs in Python, take a look at some of the Sample dialogs in the [Python Developer Samples Repo](https://github.com/mcneel/rhino-developer-samples/blob/{{ site.git_branch | default: "master" }}/rhinopython):

1.  [A very simple dialog](https://github.com/mcneel/rhino-developer-samples/blob/{{ site.git_branch | default: "master" }}/rhinopython/SampleEtoDialog.py)
2.  [Rebuild curve Dialog](https://github.com/mcneel/rhino-developer-samples/blob/{{ site.git_branch | default: "master" }}/rhinopython/SampleEtoRebuildCurve.py)
3.  [Capture a view dialog](https://github.com/mcneel/rhino-developer-samples/blob/{{ site.git_branch | default: "master" }}/rhinopython/SampleEtoViewCaptureDialog.py)
4.  [Collapsable controls on a Dialog](https://github.com/mcneel/rhino-developer-samples/blob/{{ site.git_branch | default: "master" }}/rhinopython/SampleEtoCollapsibleDialog.py)

---

## Related Topics

- [Reading and Writing files with Python]({{ site.baseurl }}/guides/rhinopython/python-reading-writing)
- [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)
- [Eto Forms in Python]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/) guide
