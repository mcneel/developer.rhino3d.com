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

[Eto is an open source cross-platform dialog box framework](https://github.com/picoe/Eto/wiki) available in Rhino 6.  This guide shows the syntax required to create the most common Eto controls in Rhino.Python.  Controls include Labels, Buttons, Edit boxes and Sliders. In Eto there are [more than 35 different controls](https://github.com/picoe/Eto/wiki/Controls) that can be created. 

For details on creating the rest of an Eto Dialog in Rhino.Python go to the [Getting Started with Eto article]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/)

## Button Controls

Buttons are placed on almost every dialog.  

![{{ site.baseurl }}/images/eto-buttons.svg]({{ site.baseurl }}/images/eto-buttons.svg){: .img-center width="65%"}

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

![{{ site.baseurl }}/images/eto-controls-calendar.png]({{ site.baseurl }}/images/eto-controls-calendar.png){: .img-center width="45%"}

```python
    #Create a Calender
    self.m_calender = forms.Calendar()
```

There are a number of properties of a calender control that can be used to modify how the control works. 

```python
    #Create a Calendar
    self.m_calendar = forms.Calendar()
    self.m_calendar.Mode = forms.CalendarMode.Single
    self.m_calendar.MaxDate = System.DateTime(2017,7,31)
    self.m_calendar.MinDate = System.DateTime(2017,7,1)
    self.m_calendar.SelectedDate = System.DateTime(2017,7,15)
```
The `.Mode` property sets if only a single date can be setting `forms.CalendarMode.Single` or date range can be selected by setting `.mode` to `forms.CalendarMode.Range`.

The `MaxDate` and `.MinDate` property limits the range of dates that can be selected from. 

The `.SelectedDate` will result in that date being initially selected.

## CheckBox

Check box with text label.

![{{ site.baseurl }}/images/eto-dialog-checkbox.png]({{ site.baseurl }}/images/eto-dialog-checkbox.png){: .img-center width="45%"}

The simpliest syntax for a CheckBox is:

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

Pick a single color drop down color picker. Also supports a right-click on the dropdown arrow to support eye dropper and the standard system color picker dialog.

![{{ site.baseurl }}/images/eto-dialog-colorpicker.png]({{ site.baseurl }}/images/eto-dialog-colorpicker.png){: .img-center width="45%"}

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

A Combo box is a drop down list of items that also allows input of text directly:

![{{ site.baseurl }}/images/eto-controls-combobox.png]({{ site.baseurl }}/images/eto-controls-combobox.png){: .img-center width="45%"}

```python
        #Create Combobox
        self.m_combobox = forms.ComboBox()
        self.m_combobox.DataStore = ['first pick', 'second pick', 'third pick']
```

The default value can be set to display by adding the index postition to the DataStore property:

```python
        self.m_combobox.SelectedIndex = 1
```

## DateTimePicker

Control to enter a date and/or time

![{{ site.baseurl }}/images/eto-controls-datetimepicker.png]({{ site.baseurl }}/images/eto-controls-datetimepicker.png){: .img-center width="45%"}

```python
        #Create DateTime Picker in Date mode
        self.m_datetimedate = forms.DateTimePicker()
        self.m_datetimedate.Mode = forms.DateTimePickerMode.Date
        self.m_datetimedate.MaxDate = System.DateTime(2017,7,30)
        self.m_datetimedate.MinDate = System.DateTime(2017,7,1)
        self.m_datetimedate.Value = System.DateTime(2017,7,15)
```

```python
        #Create DateTime Picker in Date mode
        self.m_datetimetime = forms.DateTimePicker()
        self.m_datetimetime.Mode = forms.DateTimePickerMode.Time
        self.m_datetimetime.Value = System.DateTime.Now
        self.m_datetimetime.Value = System.DateTime(2017, 1, 1, 23, 43, 49, 500)
```

## DropDown

Drop down with a list of items. 

![{{ site.baseurl }}/images/eto-controls-combobox.png]({{ site.baseurl }}/images/eto-controls-combobox.png){: .img-center width="45%"}

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

A virtualized grid of data with editable cells:

![{{ site.baseurl }}/images/eto-controls-gridview.png]({{ site.baseurl }}/images/eto-controls-gridview.png){: .img-center width="65%"}

```python
        #Create Gridview sometimes called a ListView
        self.m_gridview = forms.GridView()
#        self.m_gridview.Size = drawing.Size(400, 400)
        self.m_gridview.ShowHeader = True
        self.m_gridview.DataStore = (['first pick', 'second pick', 'third pick', True],['second','fourth','last', False])

        column1 = forms.GridColumn()
        column1.HeaderText = 'Column 1'
        column1.Editable = True
        column1.DataCell = forms.TextBoxCell(0)
        self.m_gridview.Columns.Add(column1)

        column2 = forms.GridColumn()
        column2.HeaderText = 'Column 2'
        column2.Editable = True
        column2.DataCell = forms.TextBoxCell(1)
        self.m_gridview.Columns.Add(column2)

        column3 = forms.GridColumn()
        column3.HeaderText = 'Column 3'
        column3.Editable = True
        column3.DataCell = forms.TextBoxCell(2)
        self.m_gridview.Columns.Add(column3)
        
        column4 = forms.GridColumn()
        column4.HeaderText = 'Column 4'
        column4.Editable = True
        column4.DataCell = forms.CheckBoxCell(3)
        self.m_gridview.Columns.Add(column4)
```

## GroupBox

A panel with a border and optional title.  

![{{ site.baseurl }}/images/eto-controls-groupbox.png]({{ site.baseurl }}/images/eto-controls-groupbox.png){: .img-center width="45%"}

Like the larger dialog, the GroupBox requires a Layout to hep postiion controls.  Within the layout, controls are placed:



TBD http://api.etoforms.picoe.ca/html/T_Eto_Forms_GroupBox.htm

## ImageView

A view to display a single image:

![{{ site.baseurl }}/images/eto-controls-imageview.png]({{ site.baseurl }}/images/eto-controls-imageview.png){: .img-center width="45%"}

```python
# Create an image view
        self.m_image_view = forms.ImageView()
        self.m_image_view.Size = drawing.Size(300, 200)
        self.m_image_view.Image = None
        
        # Capture the active view to a System.Drawing.Bitmap
        view = scriptcontext.doc.Views.ActiveView
        bitmap = view.CaptureToBitmap()
        
        # Convert the System.Drawing.Bitmap to an Eto.Drawing.Bitmap
        # which is required for an Eto image view control
        stream = System.IO.MemoryStream()
        format = System.Drawing.Imaging.ImageFormat.Png
        System.Drawing.Bitmap.Save(bitmap, stream, format)
        if stream.Length != 0:
          self.m_image_view.Image = drawing.Bitmap(stream)
        stream.Dispose()
```

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

A simple label that acts like a button, similar to a hyperlink.

![{{ site.baseurl }}/images/eto-controls-linkbutton.png]({{ site.baseurl }}/images/eto-controls-linkbutton.png){: .img-center width="45%"}

```python
# Create LinkButton
        self.m_linkbutton = forms.LinkButton(Text = 'For more details...')
        self.m_linkbutton.Click += self.OnLinkButtonClick
        
    # Linkbutton click handler
    def OnLinkButtonClick(self, sender, e):
        webbrowser.open("http://rhino3d.com")
```


## ListBox

A scrollable list of items:

![{{ site.baseurl }}/images/eto-controls-listbox.png]({{ site.baseurl }}/images/eto-controls-listbox.png){: .img-center width="45%"}

```python
        #Create ListBox
        self.m_listbox = forms.ListBox()
        self.m_listbox.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_listbox.SelectedIndex = 1
```

## NumericUpDown

Numeric control that allows the user to adjust the value with the mouse:

![{{ site.baseurl }}/images/eto-controls-numericupdown.png]({{ site.baseurl }}/images/eto-controls-numericupdown.png){: .img-center width="45%"}

```python
# Create Numeric Up Down
        self.m_numeric_updown = forms.NumericUpDown()
        self.m_numeric_updown.DecimalPlaces = 2
        self.m_numeric_updown.Increment = 0.01
        self.m_numeric_updown.MaxValue = 10.0
        self.m_numeric_updown.MinValue = 1.0
        self.m_numeric_updown.Value = 5.0
```

## PasswordBox

Enter passwords or sensitive data:

![{{ site.baseurl }}/images/eto-controls-password.png]({{ site.baseurl }}/images/eto-controls-password.png){: .img-center width="45%"}

```python
# Create Password Box
        self.m_password = forms.PasswordBox()
        self.m_password.MaxLength = 7
```

## ProgressBar

Show progress of long running tasks:

![{{ site.baseurl }}/images/eto-controls-progressbar.png]({{ site.baseurl }}/images/eto-controls-progressbar.png){: .img-center width="45%"}

```python
# Create Progress Bar
        self.m_progressbar = forms.ProgressBar()
        self.m_progressbar.MinValue = 0
        self.m_progressbar.MaxValue = 10
```

```python
self.m_progress = 1

    # GoButton button click handler
    def OnGoButtonClick(self, sender, e):
        self.m_progress = self.m_progress + 1
        if self.m_progress > 10:
            self.m_progress = 10
        self.m_progressbar.Value = self.m_progress
```


## RadioButtonList

Manages a list of radio buttons:

![{{ site.baseurl }}/images/eto-controls-radiobuttonlist.png]({{ site.baseurl }}/images/eto-controls-radiobuttonlist.png){: .img-center width="45%"}

```python
# Create Radio Button List Control
        self.m_radiobuttonlist = forms.RadioButtonList()
        self.m_radiobuttonlist.DataStore = ['first pick', 'second pick', 'third pick']
        self.m_radiobuttonlist.Orientation = forms.Orientation.Vertical
        self.m_radiobuttonlist.SelectedIndex = 1
```

## RichTextArea

Multi-line text area with rich text formatting:

![{{ site.baseurl }}/images/eto-controls-richtextarea.png]({{ site.baseurl }}/images/eto-controls-richtextarea.png){: .img-center width="45%"}

 This differs from the TextBox in that it is used for multi-line text entry and can accept Tab and Enter input.

```python
# Create Rich Text Edit Box
        self.m_richtextarea = forms.RichTextArea()
        self.m_richtextarea.Size = drawing.Size(400, 400)
```

The text also can be formatted by using 

1. `ctrl B` for Bold text. 
2. `crtl I` for Italic.
3. `ctrl U` for Underline.
4. .......



## Slider

A horizontal or vertical slider to select a value from a range:

![{{ site.baseurl }}/images/eto-controls-slider.png]({{ site.baseurl }}/images/eto-controls-slider.png){: .img-center width="45%"}

```python
# Create a slider
        self.m_slider = forms.Slider()
        self.m_slider.MaxValue = 10
        self.m_slider.MinValue = 0
        self.m_slider.Value = 3
```

## Spinner

A spinner to show indeterminate progress in compact space:

![{{ site.baseurl }}/images/eto-controls-spinner.png]({{ site.baseurl }}/images/eto-controls-spinner.png){: .img-center width="45%"}

```python
# Create Spinner
        self.m_spinner = forms.Spinner()
        self.m_spinner.Enabled = True
```

## TextArea

Multi-line text control with scrollbars:

![{{ site.baseurl }}/images/eto-controls-richtextarea.png]({{ site.baseurl }}/images/eto-controls-richtextarea.png){: .img-center width="45%"}

```
# Create Text Area Box
        self.m_textarea = forms.TextArea()
        self.m_textarea.Size = drawing.Size(400, 400)
```

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

Now with some understanding of Eto Dialogs in Python, take a look at some of the Sample dialogs in the [Python Developer Samples Repo](https://github.com/mcneel/rhino-developer-samples/blob/wip/rhinopython):

1.  [A very simple dialog](https://github.com/mcneel/rhino-developer-samples/blob/wip/rhinopython/SampleEtoDialog.py)
2.  [Rebuild curve Dialog](https://github.com/mcneel/rhino-developer-samples/blob/wip/rhinopython/SampleEtoRebuildCurve.py)
3.  [Capture a view dialog](https://github.com/mcneel/rhino-developer-samples/blob/wip/rhinopython/SampleEtoViewCaptureDialog.py)
4.  [Collapsable controls on a Dialog](https://github.com/mcneel/rhino-developer-samples/blob/wip/rhinopython/SampleEtoCollapsibleDialog.py)

---

## Related Topics

- [Reading and Writing files with Python]({{ site.baseurl }}/guides/rhinopython/python-reading-writing)
- [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)
- [Eto Forms in Python]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/) guide
