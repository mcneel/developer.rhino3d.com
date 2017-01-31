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

## Inside the script component

To show the code editor window for this script component, double click on the middle of the component or select “Edit Source…” from the component menu. 

The Python editor runs IronPython 2.7, the GhPython component can also access the easy to use RhinoScritSyntax. For more direct access to Rhino functions, more experienced programmers may choose to use the RhinoCommon, which also can be imported into the GhPython component. There is extensive documentation about [RhinoScriptSyntax and Python](http://developer.rhino3d.com/guides/rhinopython/) on the Developer site. For more details about RhinoCommon, please refer to the [McNeel RhinoCommon Developer site](http://developer.rhino3d.com/guides/rhinocommon). 

## Editor Interface

The code editor consists of 4 parts: 

- Menu - Use this to import and save Python files, also to access Help resources. 
- Code Window - Write the Python code here.
- Output window - Use this to see code status and error messages.
- Test Button - Runs the code without exting the editor
- OK Button - Tests the code, saves it and closes the editor.
- Close Button - Saves the code and closes the editor.

![{{ site.baseurl }}/images/ghpython-blankeditor.png]({{ site.baseurl }}/images/ghpython-blankeditor.png){: .img-center width="75%"}

### Menu

The Menu contains a File pulldown and a help pulldown.

<table>
<tr>
<th width="15%">File Menu</th>
<th>Descritption</th>
<th>Shortcut</th>
</tr>
<tr>
<td>Close</td>
<td>This will save the definition and close the edito, returing back to the Grasshopper definition</td><td>Alt+F4</td>
</tr>
<tr>
<td>Test</td>
<td>The script will run within the Grasshopper definition.  The Output window will be update with the results and editor will stay open.  This is a great window for quick debuggin of the script.</td>
<td>F5</td>
</tr>
<tr>
<td>OK</td>
<td>This will run the code, like the Test button.  Then will save the code and close the editor, returing you back to the Grasshopper definition.</td><td>Ctrl + F5</td>
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
{: .multiline}
 
## Code Window

This is where all the typing goes on and the grand dieas you have come to life.

This is very similiar to the Rhino.Ptyhon script editor.  Simply type in the statements.

### Importing modules

Normally a script will start with `import` statments.  The editor will autocomplete the modules which are available.


![{{ site.baseurl }}/images/ghpython-editor-import.png]({{ site.baseurl }}/images/ghpython-editor-import.png){: .img-center width="60%"}

Some common module that may be imported are:

```python
import rhinoscriptsyntax as rs
import math #Various math functions including Degree, Radian and Hypot
import statistics #Mean and median are here
```

There are hundeds of modules available, for a complete list, go to [Python Standard Libaries](https://docs.python.org/2/library/).  Here is a very short list of other modules that can be used:

```python
import rhino #imports the rhinocommon namespace
import datetime #Basic date and time types
import string #Common string operations
import random #Generate pseudo-random numbers
import pickle #Python object to string for serialization
import system #System-specific parameters and functions
import os.path #Common pathname manipulations
import csv #CSV File Reading and Writing
import htmllib #A parser for HTML documents
import JSON #JSON encoder and decoder
```
Once a module is imported, typing the module name and a dot will show an autocomplete of all the methods within that module.

### Input Variables

Each time Grasshopper recalculates the definition, the Python component will imput the inputs of the GHPython component as global variables in the Python script.  The name of those variables will correspond to the name of each input.  As a simple example this example:

![{{ site.baseurl }}/images/ghpython-input.png]({{ site.baseurl }}/images/ghpython-input.png){: .img-center width="80%"}

The code to process the `x` input is as follows:

```python
if x:
    print "x is true."
else:
    print "x is false."
```

Understanding the type of deta is being input and how that maps to standard Python components is important. Some examples:

| Grasshopper Input | | | Python Datatype |
|:------------------|-|-|:----------------|
| String            | | | String          |





## Next Steps

That lays out the basics of the GhPython component.  Next is a look into the component Python editor for Grasshopper.

---

## Related Topics

- [Your first script with Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Editing Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/python-loading-scripts)
- [Python Guide for Rhino]({{ site.baseurl }}/guides/rhinopython/)
