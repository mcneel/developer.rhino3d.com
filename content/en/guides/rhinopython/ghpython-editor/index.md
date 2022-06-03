+++
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "This guide looks at the details of the GhPython Editor."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "An Overview of the GhPython Editor"
type = "guides"
weight = 3
override_last_modified = "2018-12-05T14:59:06Z"

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

## Inside the script component

To show the code editor window for this script component, double click on the middle of the component, or select “Edit Source…” from the component center-icon context menu.

The Python editor runs IronPython 2.7, the GhPython component can also access the easy-to-use RhinoScriptSyntax. For more direct access to Rhino functions, more experienced programmers may choose to use the RhinoCommon, which also can be imported into the GhPython component. There is extensive documentation about [RhinoScriptSyntax and Python](http://developer.rhino3d.com/guides/rhinopython/) on the Developer site. For more details about RhinoCommon, please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon).

## Editor Interface

The code editor consists of 4 parts:

- Menu - Use this to import and save Python files, also to access Help resources.
- Code Window - Write the Python code here.
- Output window - Use this to see code status and error messages.
- Test Button - Runs the code without exiting the editor
- OK Button - Tests the code, saves it and closes the editor.
- Close Button - Saves the code and closes the editor.

{{< image url="/images/ghpython-blankeditor.png" alt="/images/ghpython-blankeditor.png" class="image_center" width="75%" >}}

### Menu

The Menu contains a File pulldown and a help pulldown.

<table class="multiline">
<tr>
<th width="15%">File Menu</th>
<th>Descritption</th>
<th>Shortcut</th>
</tr>
<tr>
<td>Close</td>
<td>This will save the definition and close the editor, returning back to the Grasshopper definition</td><td>Alt+F4</td>
</tr>
<tr>
<td>Test</td>
<td>The script will run within the Grasshopper definition.  The Output window will be update with the results and editor will stay open.  This is a great window for quick debugging of the script.</td>
<td>F5</td>
</tr>
<tr>
<td>OK</td>
<td>This will run the code, like the Test button.  Then will save the code and close the editor, returning you back to the Grasshopper definition.</td><td>Ctrl + F5</td>
</tr>
<tr>
<td>Import From...</td>
<td>Browse for and import a <i>.py</i> file into the editor. </td>
<td>Ctrl + I</td>
</tr>
<tr>
<td>Export As...</td>
<td>Save the code in the editor to a <i>.py</i> file on the disk.</td>
<td>Ctrl + E</td>
</tr>
</table>

### Code Window

This is where all the typing goes on and the grand ideas you have come to life.

This is very similar to the Rhino.Python script editor.  Simply type in the statements.

#### Importing modules

Normally a script will start with `import` statements.  The editor will autocomplete the modules which are available.
Note: some modules may not autocomplete but still be available.


{{< image url="/images/ghpython-editor-import.png" alt="/images/ghpython-editor-import.png" class="image_center" width="60%" >}}

Some common module that may be imported are:

```python
import rhinoscriptsyntax as rs
import math #Various math functions including Degree, Radian and Hypot
import statistics #Mean and median are here
```

There are hundreds of modules available, for a complete list, go to [Python Standard Libaries](https://docs.python.org/2/library/).  Here is a very short list of other modules that can be used:

```python
import rhino #imports the rhinocommon namespace
import cmath #Mathematical functions for complex numbers
import datetime #Basic date and time types
import string #Common string operations
import random #Generate pseudo-random numbers
import pickle #Python object to string for serialization
import system #System-specific parameters and functions
import os.path #Common pathname manipulations
import csv #CSV File Reading and Writing
import htmllib #A parser for HTML documents
import json #JSON encoder and decoder
```
Once a module is imported, typing the module name and a dot will show an autocomplete of all the methods within that module.

#### Input Variables

Each time Grasshopper recalculates the definition, the Python component will direct the inputs of the GhPython component as global variables in the Python script.  The name of those variables will correspond to the name of each input.  As a simple example this example:

{{< image url="/images/ghpython-input.png" alt="/images/ghpython-input.png" class="image_center" width="80%" >}}

The code to process the `x` input is as follows:

```python
if x:
    print("x is true.")
else:
    print("x is false.")
```

Understanding the type of date is being input and how that maps to standard Python components is important. If the datatype is not what is needed in the Python script by default, then use the `Type hint` option on the component. This assures the correct datatype on input.


#### Output variables

To output to the component set the value of the output name to a variable. For instance if the output is named `a`, then the code to send "Hello World!" to the output would be:

```python
a = "Hello World!"
```

The last assignment to the variable in the script will the value that is output.  If there are multiple assignments, as in a list of values assigned in a loop to the output variable, only the last one is sent out.  This can be a bit confusing.  The key is to assign the series of outputs to a list variable, then output that variable through the `a` output.

As an example, this does not work:

```python
l = [2,3,4,4,5,4,5,6,7,8,9]

a = []

for item in l:
    a = item + 5
```

There are two problems with the script above. An output variable in GhPython is created by the GhPython component.  It cannot be set to a specific variable type as in the line `a=[]`.  Also, the `for` will loop through he items in `l`, only to output the last assigned value to `a` at the completion of the Grasshopper cycle.

The proper way to output a series of values is to create a list variable to populate, then output that variable to `a` at the end of the script.

```python
l = [2,3,4,4,5,4,5,6,7,8,9]

li=[]

for item in l:
    li.append(item + 5)

a = li
```

#### Print function

The `print()` function used in the GhPtyhon script will print information out to the Output Window.  This is a good way to debug script in the window also.
Because we are using a flavor of Python 2, print is really a statement, that works also without parentheses. However, we prefer to look at is a function, that way it will work the same also in Python 3 flavors.

### Output Window

The Output Window contains help and messages about the status of the editor.  

1. If the script is run while the editor is open, the success or failure of the script will be displayed here.
2. If there is an error while testing the script, the error information will display in the Output Window.

```
Runtime error (SyntaxErrorException): EOL while scanning single-quoted string

File "", line 10
    import 'rhinoscriptsyntax as rs

           ^
SyntaxError: EOL while scanning single-quoted string
```

3. The `print()` function will output to this window.
4. While editing a script, information about the current method will be displayed here. The comments about a method are limited to arguement requirements.  For a fuller explaination of any method, go to the python help file.


### Test Button

Use the *Test* button to run the script while keeping the Ghpython editor is up on the screen.  The Grasshopper definition will also be updated at the same time.

### OK and Close Button

The *OK* button will save the script to the GhPython component and will close the editor, retuning to Grasshopper.

The *Close* button will revert any changes to the script and return to grasshopper, using the previously saved script.

## Example Script

Here is an example script:

{{< div class="line-numbers" >}}
```python
# sample script to show how to use this component and the rhinoscriptsyntax
"""Constructs a sinusoidal series of circles.
  Inputs:
    x: The number of circles. (integer)
    y: The radius of each circle. (float)
  Outputs:
    a: The list of circles. (list of circle)
    b: The list of radii. (list of float)
"""
import math
import rhinoscriptsyntax as rs

if x is None:
    x = 24    # if nothing is connected to x, set x to something (24).
if y is None:
    y = 0.3    # if nothing is connected to y, set y to 0.3.

circles = []            # create a list. We will add IDs to it later on.
radii = []              # ...and create another one.

for i in range(int(x)):
    pt = (i, math.cos(i), 0)             # a tuple (here for a point).
    id1 = rs.AddCircle(pt, y)
    circles.append(id1)
    endPt = rs.PointAdd(pt, (0, 0.3, 0)) # move the point by the vector.
    id2 = rs.AddLine(pt, endPt)
    radii.append(id2)

a = circles
b = radii
```
{{< /div >}}


<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>2...9</td>
<td>
A multiline comment that explains the inputs and outputs of the script.
</td>
</tr>
<tr>
<td>10...11</td>
<td>Importing a couple modules that are needed later in the script.</td>
</tr>
<tr>
<td>13...16</td>
<td>Here we check the values of the two inputs `x` and `y` have a value.  If not the values are set to default values.</td>
</tr>
<tr>
<td>21...27</td>
<td>Use a <i>For</i> loop to walk through each circle based on the value of <i>x</i>.</td>
</tr>
<tr>
<td>24</td>
<td>Each time through the loop, circles are added to the <i>circles</i> variable.</td>
</tr>
<tr>
<td>29</td>
<td>The circles are output to the <i>a</i> output</td>
</tr>
</table>

## Next Steps

That quick look at the GhPython editor.  Next is a try a Python script for yourself.

## Related Topics

- [Your first script with Python in Grasshopper](/guides/rhinopython/your-first-python-script-in-grasshopper/)
- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython/)
- [Editing Python in Grasshopper](/guides/rhinopython/ghpython-component/)
- [Python Guide for Rhino](/guides/rhinopython/)
