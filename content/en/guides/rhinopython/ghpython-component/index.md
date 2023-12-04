+++
aliases = ["/5/guides/rhinopython/ghpython-component/", "/6/guides/rhinopython/ghpython-component/", "/7/guides/rhinopython/ghpython-component/", "/wip/guides/rhinopython/ghpython-component/"]
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "The GhPython component is the key to working with Python in Grasshopper."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "An Overview of the GhPython Component"
type = "guides"
weight = 2
override_last_modified = "2019-09-14T11:27:08Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Grasshopper" ]
since = 0
version = [ "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++

The GhPython component acts as a Python interpreter in Grasshopper.  Along with its access to IronPython 2.7, the GhPython component can also access the-easy-to-use RhinoScriptSyntax. For more direct access to Rhino functions, more experienced programmers may choose to use the RhinoCommon, which also can be imported into the GhPython component. There is extensive documentation about [RhinoScriptSyntax and Python](http://developer.rhino3d.com/guides/rhinopython/) on the Developer site. For more details about RhinoCommon, please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon).

## Component Details

The GhPython conponent can be found on the Math > Script toolbar:

{{< image url="/images/ghpython-installed.png" alt="/images/ghpython-installed.png" class="image_center" width="95%" >}}

Drag and drop the component onto the canvas:

{{< image url="/images/ghpython-component-detail.png" alt="/images/ghpython-component-detail.png" class="image_center" width="95%" >}}


The default script component has two inputs and two outputs. The user can change the names of input and output, the data type and data structure of the input and also add more inputs and outputs parameters or remove them.

- x: first input of a .NET type (object).
- y: second input of a .NET type (object).
- Out: output string with compiling messages.
- A: Returned output of type object.

To edit the Python script in the component, simply double-click the component:

{{< image url="/images/ghpython-blankeditor.png" alt="/images/ghpython-blankeditor.png" class="image_center" width="75%" >}}

Simple type in the Python code, clicking on OK will save the code in the component.

## Input parameters

By default, there are two input parameters named x and y.  It is possible to edit parameters names, delete or add new ones. By zooming into a component new controls will appear on the component:

{{< image url="/images/ghpython-component.png" alt="/images/ghpython-component.png" class="image_center" width="30%" >}}

Use *+* and *-* buttons to add and subtract inputs.

{{< image url="/images/ghpython-removeinput.png" alt="/images/ghpython-removeinput.png" class="image_center" width="35%" >}}

You can also right-click on a parameter to change its name. The name is also the variable name in the Python script.

{{< image url="/images/ghpython-rename-input.png" alt="/images/ghpython-rename-input.png" class="image_center" width="35%" >}}

Please note that the names of the parameters must follow [Python identifier naming](https://docs.python.org/2/reference/lexical_analysis.html#identifiers) . Just make sure that these names are reflective of what the parameter is, and that they also do not contain white spaces or special characters.

The inputs will show up in the GhPython editor as global variables.  For instance, here is a simple definition:

{{< image url="/images/ghpython-input.png" alt="/images/ghpython-input.png" class="image_center" width="80%" >}}

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

{{< image url="/images/ghpython-component.png" alt="/images/ghpython-component.png" class="image_center" width="30%" >}}

To send the information out to *a* enter this line in the editor:

```python
a = "This string will be sent to the output"
```

{{< image url="/images/ghpython-output.png" alt="/images/ghpython-output.png" class="image_center" width="80%" >}}

Each time Grasshopper recalculates the definition, the Python component will run and send out the value(s) to the output.


## Out parameter

Out parameter is there by default to provide some useful information about your code. I often find myself connecting the out parameter to a panel component to be able to read the information directly without having to hover over the out parameter.

{{< image url="/images/ghpython-outerror.png" alt="/images/ghpython-outerror.png" class="image_center" width="80%" >}}

There are two types of messages that you can get in the out parameter.

- The compile-time messages. Those include errors and warning about your code that prevent your component from running or can potentially give incorrect results. These are very helpful information to help point you to the lines in code that the compiler is having trouble with so that you can make appropriate adjustments.
- The run-time messages.  You can send bits of text to the out parameter. You can use those to track information generated by your code as it is running.

## Advanced Input Properties

{{< image url="/images/ghpython-inputoptions.png" alt="/images/ghpython-inputoptions.png" class="float_right" width="300" >}}

For most basic work, the instructions above are all that are needed.  But, there are a few advanced options that can be set on the GhPython inputs that can be useful in certain situations.

To access the input options, right-click on any of the inputs.  

The top entry is the Parameter or variable name: you can click on it and type a new name.  

The next section is the general attributes or functions common to most GH components.  

Then is a section to input data directly to the component and to manage that data.

The three access options 'Item Access', 'List Access' and 'Tree Access' change the way lists and datatrees are imported into the GhPython component. This controls how lists of objects are imported.  For instance a string of characters can be input as each character individually:

```python
"This string"
[1,3,5,6]
```

If the input is set to 'Item Access', then each character is sent in separately:

{{< div class="line-numbers" >}}
```python
T
h
i
s

s
t
r
i
n
g

[
1
3
5
6
]
```
{{< /div >}}

While this is a good way to manipulate each character in order, by switching the input to `List Input`, then the complete string is sent in each Grasshopper iteration:

{{< div class="line-numbers" >}}
```python
This string
[1,3,5,6]
```
{{< /div >}}



The third section is most powerful to use the *Type hint*. Input parameters are set by default to the .NET type “object”. Sometimes is best to specify a datatype on input to make the code more readable and efficient. Types can be primitive such as integers or doubles, or geometry specific RhinoCommon types that are used only in Rhino such as “Point3d” or a “Curve”. You need to select the appropriate type for each input.

The rhinoscriptsyntax Type Hint is special: when it is selected, any geometry will be added to the Grasshopper document, and then its ID (Guid) inside it will be passed in the variable. With the rest of the hints, GhPython will call into Grasshopper and perform the same type of operations that Grasshopper does when it requires a special data type. This conversion is costly. If you want to make things as quick as possible, choose 'No Type Hint'. However, users of your component will benefit greatly from using a meaningfully-set and appropriate type hint.


## Next Steps

That lays out the basics of the GhPython component.  Next is a look into the component Python editor for Grasshopper.

## Related Topics

- [Your first script with Python in Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper)
- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [An Overview of the GhPython Editor](/guides/rhinopython/ghpython-editor)
- [Python Guide for Rhino](/guides/rhinopython/)
