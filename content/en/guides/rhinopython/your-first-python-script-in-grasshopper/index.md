+++
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "This manual is for Grasshopper users who would like to create their own custom scripts using Grasshopper for Rhino."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Your First Python Script in Grasshopper"
type = "guides"
weight = 1
override_last_modified = "2019-10-25T13:24:40Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Grasshopper" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Introduction

Scripting components works as an integrated part of GH. They can get input and produce output from and to other standard GH components. They can be used to create specialized functionality that opens up tremendous potential beyond the standard components.

But there is a cool twist… the GhPython component supports rhinoscriptsyntax functions. The rhinoscriptsyntax functions can be set to generate geometry inside of Grasshopper that does not live in the Rhino document. We are using a concept called “duck typing” to swap the document that the rhinoscriptsyntax functions target: from the Rhino document to a Grasshopper document. This means that the following script:

```python
import rhinoscriptsyntax as rs
for x in range(10):
    rs.AddPoint((x,0,0)
```

will add 10 points to the Rhino document when run from Rhino’s “_RunPythonScript” or “_EditPythonScript” commands. The same script will add 10 points to a Grasshopper document that can be passed on to other components when run inside a GhPython component.

Grasshopper supports multiple .NET scripting languages such as VB and C# to help develop custom code. There is also the Python component. Python supports multiple programming paradigms, often used as a scripting language, but is also used in a wide range of advanced programming contexts. The [Rhino.Python](http://developer.rhino3d.com/guides/rhinopython/) website directory is a great place to get more information about Python in Rhino in general.

{{< image url="/images/ghpython-component.png" alt="/images/ghpython-component.png" class="float_right" width="275" >}}

The GhPython component brings:

- Rhinoscript syntax to Grasshopper
- a Python parallel to the C# and Vb.Net scripting components
- a dynamic UI with control over the number of inputs and outputs
- ability to reference .NET libraries and a huge number of Python packages
- integration with the Python editor included in Rhino



Rhino allows access to its algorithms through the Rhino SDK (software development kit). Rhino is written in C++ but it also provides a couple SDKs for scripting and programming languages.  The most basic SDK for Python is RhinoScriptSyntax. For more direct access to Rhino functions, more experienced programmers may choose to use the RhinoCommon SDK. There is extensive documentation about [RhinoScriptSyntax and Python](http://developer.rhino3d.com/guides/rhinopython/) on the Developer site. For more details about RhinoCommon, please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon).


## Where to find the script components

To add the Python script component to the canvas, drag and drop the component from the “Script” panel under the “Maths” tab. The component first shows orange indicating a warning. This is because there is no code typed yet inside it. If you click on the bubble at the top-right corner, you can see what the warning is.

{{< image url="/images/ghpython-component.png" alt="/images/ghpython-component.png" class="image_center" width="30%" >}}

The default script component has two inputs and two outputs. The user can change the names of input and output, the data type and data structure of the input and also add more inputs and outputs parameters or remove them.


{{< image url="/images/ghpython-component-detail.png" alt="/images/ghpython-component-detail.png" class="image_center" width="95%" >}}

- x: first input of a .NET type (object).
- y: second input of a .NET type (object).
- out: output string with compiling messages and prints.
- A: Returned output of type object.


## The HelloWorld Script

Let's start with the classic ["Hello World!" example](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) for our first script.

1. Drag a Python component onto the Grasshopper canvas.
2. Add a Boolean component (Params toolbar) and connect it to the *x* input.
3. Add a Panel component and connect it to the *a* output.

{{< image url="/images/ghpython-helloworld-canvas.png" alt="/images/ghpython-helloworld-canvas.png" class="image_center" width="75%" >}}

The "Hello World!" script will check for a *TRUE* in `x` to display the Hello World message through the 'a' output.

Double-click on the component to bring up the Python editor:

{{< image url="/images/ghpython-blankeditor.png" alt="/images/ghpython-blankeditor.png" class="image_center" width="75%" >}}

Type in the following Python code:

```python
if x:
    a = "Hello World!"
```

Click on the OK button of the editor to get back to the Grasshopper Canvas.

If you toggle the Boolean switch from true to false, the Panel should display `Hello World!`.

{{< image url="/images/ghpython-helloworld.png" alt="/images/ghpython-helloworld.png" class="image_center" width="75%" >}}

Congratulations!  You have compete your first Python script in Grasshopper.

To change the script, double-click o the Python component. Add another line of code:

```python
if x:
    a = "Hello World!"
else:
    a = "Nothing to say."
```

Now you can test that using the toggle.

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Loading Scripts](/guides/rhinopython/python-loading-scripts)
- [Running Scripts](/guides/rhinopython/python-running-scripts)
- [Canceling Scripts](/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts](/guides/rhinopython/python-editing-scripts)
- [Scripting Options](/guides/rhinopython/python-scripting-options)
- [Troubleshooting Python](/guides/rhinopython/python-troubleshooting-install)
