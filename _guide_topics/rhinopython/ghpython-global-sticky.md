---
title: Creating Global Sticky Variables
description: How can DataTrees be accessed and created in GhPython.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac', 'Grasshopper']
categories: ['ghPython']
origin:
order: 5
keywords: ['python', 'commands', 'grasshopper']
layout: toc-guide-page
---

Creating a definition wide Global sticky variable can be helpful in Grasshopper. Each of you components can access it.

http://www.grasshopper3d.com/forum/topics/functions-in-sticky-to-make-them-available-to-other-python
https://discourse.mcneel.com/t/reference-input-values-between-different-ghpython-components/17425
http://www.grasshopper3d.com/forum/topics/exchanging-basic-python-types-between-separate-python-components




## Converting DataTrees to Python Lists.

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

Please note that the names of the parameters must follow [Python identifier naming](https://docs.python.org/2/reference/lexical_analysis.html#identifiers) . Just make sure that these names are reflective of what the parameter is, and that they also do not contain white spaces or special characters.

The inputs will show up in the GhPython editor as global variables.  For instance, here is a simple definition:

![{{ site.baseurl }}/images/ghpython-input.png]({{ site.baseurl }}/images/ghpython-input.png){: .img-center width="80%"}

The code to process the `x` input is as follows:

```python
if x:
    print("x is true.")
else:
    print("x is false.")
```

As the Boolean toggle is changed, the `x` value changes.  The `print` method will out put a string to the out of the component.


## Output parameters

Like the inputs, you can define as many outputs or returns as you need when you “zoom in” and push the “+” sign.  Unlike input parameters, there are no default datatypes associated with output.  The output datatype will be assigned inside your script.

To actually send information to the output from the script, simply assign the value(s) to the output variable name.  For instance, in this case the output is *a*:

![{{ site.baseurl }}/images/ghpython-component.png]({{ site.baseurl }}/images/ghpython-component.png){: .img-center width="30%"}

To send the information out to *a* enter this line in the editor:

```python
a = "This string will be sent to the output"
```

![{{ site.baseurl }}/images/ghpython-output.png]({{ site.baseurl }}/images/ghpython-output.png){: .img-center width="80%"}

Each time Grasshopper recalculates the definition, the Python component will run and send out the value(s) to the output.


## Out parameter

Out parameter is there by default to provide some useful information about your code. I often find myself connecting the out parameter to a panel component to be able to read the information directly without having to hover over the out parameter.

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

The third section is most powerful to use the *Type hint*. Input parameters are set by default to the .NET type “object”. Sometimes is best to specify a datatype on input to make the code more readable and efficient. Types can be primitive such as integers or doubles, or geometry specific RhinoCommon types that are used only in Rhino such as “Point3d” or a “Curve”. You need to select the appropriate type for each input.

The rhinoscriptsyntax Type Hint is special: when it is selected, any geometry will be added to the Grasshopper document, and then its ID (Guid) inside it will be passed in the variable. With the rest of the hints, GhPython will call into Grasshopper and perform the same type of operations that Grasshopper does when it requires a special data type. This conversion is costly. If you want to make things as quick as possible, choose 'No Type Hint'. However, users of your component will benefit greatly from using a meaningfully-set and appropriate type hint.


## Next Steps

That lays out the basics of the GhPython component.  Next is a look into the component Python editor for Grasshopper.

---

## Related Topics

- [Your first script with Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Editing Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/python-loading-scripts)
- [Python Guide for Rhino]({{ site.baseurl }}/guides/rhinopython/)
