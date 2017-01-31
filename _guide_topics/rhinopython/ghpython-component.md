---
title: An Overview of the GhPython Component
description: This guide looks at the details of the GhPython component.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac', 'Grasshopper']
categories: ['GhPython']
origin:
order: 1
keywords: ['python', 'commands', 'grasshopper']
layout: toc-guide-page
---

The GHPython component is the key to working with Python in Grasshopper. 

The GhPython component acts as a Python interpreter in Grasshopper.  Along with its access to IronPython 2.7, the GhPython component can also access the easy to use RhinoScritSyntax. For more direct access to Rhino functions, more experienced programmers may choose to use the RhinoCommon, which also can be imported into the GhPython component. There is extensive documentation about [RhinoScriptSyntax and Python](http://developer.rhino3d.com/guides/rhinopython/) on the Developer site. For more details about RhinoCommon, please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon). 

## Component Details

The GhPython conponent can be found on the Math > Script toolbar:

![{{ site.baseurl }}/images/ghpython-installed.png]({{ site.baseurl }}/images/ghpython-installed.png){: .img-center width="95%"}

Drag and drop the component onto the canvas:

![{{ site.baseurl }}/images/ghpython-component-detail.png]({{ site.baseurl }}/images/ghpython-component-detail.png){: .img-center width="95%"}


The default script component has two inputs and two outputs. The user can change the names of input and output, the data type and data structure of the input and also add more inputs and outputs parameters or remove them.

- x: first input of a .NET type (object).
- y: second input of a .NET type (object).
- Out: output string with compiling messages.
- A: Returned output of type object.

To edit the Python script in the component, simply double-click the component:

![{{ site.baseurl }}/images/ghpython-blankeditor.png]({{ site.baseurl }}/images/ghpython-blankeditor.png){: .img-center width="75%"}

Simple type int he Python code, clicking on OK will save the code in the component.

## Input parameters

By default, there are two input parameters named x and y.  It is possible to edit parameters names, delete or add new ones. By zooming into a component new controls will appear on the component:

![{{ site.baseurl }}/images/ghpython-component.png]({{ site.baseurl }}/images/ghpython-component.png){: .img-center width="30%"}

Use *+* and *-* buttons to add and subtract inputs.

![{{ site.baseurl }}/images/ghpython-removeinput.png]({{ site.baseurl }}/images/ghpython-removeinput.png){: .img-center width="35%"}

You can also right-click on a parameter to change its name. The name is also the variable name in the Python script.

![{{ site.baseurl }}/images/ghpython-rename-input.png]({{ site.baseurl }}/images/ghpython-rename-input.png){: .img-center width="35%"}

Please note that the names of the parameters must follow [Python identifier naming](https://docs.python.org/2/reference/lexical_analysis.html#identifiers) . Just make sure that these names are reflective of what the parameter is and also it should not contain white spaces or special characters.

The inputs will show up in the GhPython editor as global variables.

## Output parameters

Like the inputs, you can define as many outputs or returns as you need when you “zoom in” and push the “+” sign.  Unlike input parameters, there are no default datatypes associated with output.  The output datatype can assign inside your script.

To actually send information to the output from the script, simply assign the value(s) to the output variable name.  For intance in this case the output is *a*:

![{{ site.baseurl }}/images/ghpython-component.png]({{ site.baseurl }}/images/ghpython-component.png){: .img-center width="30%"}

To send the information out to *a* enter this line in the editor:

```python
a = "This string will be sent to the output"
```

![{{ site.baseurl }}/images/ghpython-output.png]({{ site.baseurl }}/images/ghpython-output.png){: .img-center width="80%"}

Each time Grasshopper recalculates the definition, the Python component will run and send out the value(s) to the output.


## Out parameter

Out paramter is there by default to provide some useful information about your code. I often find myself connecting the out parameter to a panel component to be able to read the information directly without having to hover over the out parameter.

![{{ site.baseurl }}/images/ghpython-outerror.png]({{ site.baseurl }}/images/ghpython-outerror.png){: .img-center width="80%"}

There are two types of messages that you can get in the out parameter. 

- The compile-time messages. Those include errors and warning about your code that prevent your component from running or can potentially give incorrect results. These are very helpful information to help point you to the lines in code that the compiler is having trouble with so that you can make appropriate adjustments.
- The run-time messages.  You can send bits of text to the out parameter. You can use those to track information generated by your code as it is running.

## Advanced Input Properties

![{{ site.baseurl }}/images/ghpython-inputoptions.png]({{ site.baseurl }}/images/ghpython-inputoptions.png){: .float-img-right width="300"}

For most basic work, the instructions above are all that are needed.  But, there are a few advanced options that can be set on the GhPython inputs that can be useful in certain situations.

To access the input options, right-click on any of the inputs.  

The top entry is the Parameter or variable name: you can click on it and type a new name.  

The next section is the general attributes or functions common to most GH components.  

Then is a section to input data directly to the component and to manage that data.  

The third section is most powerful to use the *Type hint*. Input parameters are set by default to the.NET type “object”.  It is best to specify a type to make the code more readable and efficient. Types can be primitive, such as integer or double, or geometry specific RhinoCommon types that are used only in Rhino such as “Point3d” or a “Curve”. You need to select the appropriate type for each input.

Just like any other GH components, you can hook data to the input parameters of the script components. Your script component can be made to process numbers, curves or any other data type. You can specify the data type of your input using the Type hint as in the following image.






---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Loading Scripts]({{ site.baseurl }}/guides/rhinopython/python-loading-scripts)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
