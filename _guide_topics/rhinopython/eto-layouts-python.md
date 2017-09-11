---
title: Eto Layouts in Rhino.Python
description: Using the Eto DynamicLayout to organize controls.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Intermediate']
origin:
order: 22
keywords: ['script', 'Rhino', 'python', 'Eto']
layout: toc-guide-page
---

[Eto is an open source cross-platform dialog box framework](https://github.com/picoe/Eto/wiki) available in Rhino 6.  This guide demonstrates the syntax required to create Layouts.  Layouts are containers in which controls are placed.  The layout will position the controls in a dialog or another Layout. It is possible to nest Layouts within eachother to handle more complex layouts.

For details on creating a complete Eto Dialog in Rhino.Python go to the [Getting Started with Eto Guide]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/). The samples in this guide can be added to the controls section of the Basic dialog framework covered in the [Getting Started Guide]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/).

There are [5 different layout style in Eto](https://github.com/picoe/Eto/wiki/Containers).  

- [Panel](https://github.com/picoe/Eto/blob/develop/Source/Eto/Forms/Controls/Panel.cs) - Controls that subclass `Panel`, such as `Window`, `GroupBox`, `Scrollable`, etc allow you to specify a single child Content control
- [TableLayout](https://github.com/picoe/Eto/wiki/TableLayout) - Similar to how an HTML table works, with a single control per cell
- [PixelLayout](https://github.com/picoe/Eto/wiki/PixelLayout) - Specify X,Y co-ordinates for the position of each control (from Upper-Left)
- [DynamicLayout](https://github.com/picoe/Eto/wiki/DynamicLayout) - Dynamic hierarchical horizontal and vertical layout
- [StackLayout](https://github.com/picoe/Eto/wiki/StackLayout) - Horizontal or Vertical list of controls

This guide will focus on using the [DynamicLayout](https://github.com/picoe/Eto/blob/develop/Source/Eto/Forms/Layout/DynamicLayout.cs. ) style only.  The `forms.DynamicLayout()` has a clear simple syntax in Python and is quite flexible. 

# Dynamic Layout

A layout in Eto is a virtual grid in which controls are placed. The layout arranges its child controls in a table structure of rows and columns. It is similar to the HTML table layout. 

In it simplest form a layout is built row by row using the `.AddRow` method.  Each `Addrow may contain one or more controls.  For each control in the list a column cell is made on the new row.

![{{ site.baseurl }}/images/eto-buttons.svg]({{ site.baseurl }}/images/eto-buttons.svg){: .img-center width="65%"}

Creating a new button is simple. Use the `forms.Button` and specify the `Text` that is shown on the button face. In addition to creating the new button, an action is commonly attached through the `.Click` event.  Use the  `+=` syntax as shown below to bind the action to button.

```python
        self.m_button = forms.Button(Text = 'OK')
        self.m_button.Click += self.OnButtonClick
```

The bound method, listed later in the calss definition is run if the button is clicked. 

```python
    # Close button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
```

In this specific case the button is clicked and the bound method `OnOKButtonClick` checks the Text of the `m_textbox` to to determine if anything has been entered. Then the method closes the dialog, returning either `True` or `False`.

The *Eto.Dialog class* has two special reserved names for buttons, the `DefaultButton` and the `AbortButton`.  The `DefaultButton` name will create a button that is a standard button and also will receive a click event if the `Enter Key` is used. The `AbortButton` is a button that recieves a `.Click` event if the `ESC` key is used.  These buttons are simple assigned through the name of the control, using `self`  syntax.

The syntax for the `DefaultButton` is:

```python
self.DefaultButton = forms.Button(Text = 'OK')
```

And for the `AbortButton` is:

```python
self.AbortButton = forms.Button(Text = 'Cancel')
```

The `DefaultButton` and `AbortButton` normally close the dialog by using the `self.close()` method of the dialog.  Please note that even though the dialog is closed, that values of the controls are still accesable to the rest of the script.

More details can be found in the [Eto Button API Documentation](http://api.etoforms.picoe.ca/html/T_Eto_Forms_Button.htm).

---

## Related Topics

- [RhinoScriptSyntax User interface methods]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#userinterface)
- [Custom Eto Forms in Python guide]({{ site.baseurl }}/guides/rhinopython/eto-forms-python/)
