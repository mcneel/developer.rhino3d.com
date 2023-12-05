+++
aliases = ["/5/guides/rhinopython/ghpython-call-components/", "/6/guides/rhinopython/ghpython-call-components/", "/7/guides/rhinopython/ghpython-call-components/", "/wip/guides/rhinopython/ghpython-call-components/"]
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "It is possible to call a Grasshopper component from inside a Python script."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Node in Code from Python."
type = "guides"
weight = 5
override_last_modified = "2019-11-06T14:14:21Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Grasshopper" ]
since = 0
version = [  "7", "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++

**Node-in-Code™**: almost every Grasshopper component is now callable as a function in other places in Rhino.  Grasshopper components may be called in GhPython (on the Gh canvas) and from rhino.Python (off the canvas). This adds few thousand new functions accessible to GhPython. Functions are also available through 3rd party components.  Along with the new functionality that this provides, the technique can be used to simplify existing gh definition files by simply lumping together a bunch of related components into a single 'scott_davidson' script.

There is a module in `ghpythonlib.components` which attempts to make every component available in Python in the form of an easy to call function.

## Components As functions from GhPython

In this example we can make a new ghPhython component that combines the standard Grasshopper Voronoi component and the Grasshopper Area components.  Within one GhPython component the voronoi curves are created and the cell centroid points are output.

{{< image url="/images/node-in-code-voronoi.png" alt="/images/node-in-code-voronoi.png" class="image_center" width="25%" >}}

Use a GhPython component with these inputs:

{{< image url="/images/nod-in-code-sample.png" alt="/images/nod-in-code-sample.png" class="image_center" width="95%" >}}
Node in Code sample file

Before entering code in the GhPython component it to review the input properties to make sure the correct Type hint is used.  In this case the points input has a Point3D hint and a List Access level set.  Do this by right clicking on the GhPython component input.

Enter this code into the GhPython component:

```python
import ghpythonlib.components as ghcomp
curves = ghcomp.Voronoi(points) # call the Grasshopper Voronoi component
centroids = ghcomp.Area(curves).centroid # call Grasshopper Area component with curves from Voronoi
```

Of course you can mix in other Python to perform calculations on the results of the component function calls. I tweaked the above example to find the curve generated from Voronoi that has the largest area.

```python
import ghpythonlib.components as ghcomp

curves = ghcomp.Voronoi(points)
areas = ghcomp.Area(curves).area
#find the biggest curve in the set
max_area = -1
max_curve = None
for i, curve in enumerate(curves):
    if areas[i] > max_area:
        max_area = areas[i]
        max_curve = curve
```

Remember, this can be done for almost every component in Grasshopper (including every installed add-on component.) I use the term almost because there are cases where the function call doesn’t make sense. These cases are for things like Kangaroo or timers where the state of the component is important between iterations. Fortunately this is pretty rare.

### Configuring inputs:

There are a few techniques that can make working with `ghpythonlib.components` easier.
It is quite helpful and simplifies the code greatly if the proper [Type Hint](/guides/rhinopython/ghpython-component/#advanced-input-properties) is set on the Input of the Python component. Setting the Type Hint to a specific data type will give the script direct access to the objects.   Without the Type Hint a lot more data checking and conversion may be necessary. For instance in a case where `points` are expected as input, set Type Hint > Point3D.  This assures the GhPython components passes in actual point objects to Python. This is especially important for any inputs expecting geometry objects.

Inputs also should be set properly for [Object Access, List Access, or Tree Access](/guides/rhinopython/ghpython-component/#advanced-input-properties).  Setting the Object vs List level access is important for make sure the GhPython code gets objects one at a time, or as a whole list of objects all at once.

Working with multiple inputs and outputs from component methods is like working with any other Python functions.  Inputs can be passed to the function through a list of arguments.  For instance the Divide Curve component has multiple inputs (Curve, Number, Kinks)


{{< image url="/images/divide-comp.png" alt="/images/divide-comp.png" class="image_center" width="25%" >}}

To pass these arguments, use a sequential list:

```python
results = ghcomp.DivideCurve(C, N, K)
```

Inputs may also are still optional and can be left off the end. Arguments left out will use their built in defaults:

```python
results  = ghcomp.DivideCurve(C, N)
```

Inputs may also be passed as Keyword arguments `(**kwargs)`.  In this way options do not need to be assigned sequentially and certain optional inputs can be skipped:

```python
results  = ghcomp.DivideCurve(Curves = C, Kinks = K)
```

In the case above the missing input Number of divisions the default value of (10) is used.  Be careful on relying on default values.  It is possible default values can change in the future.

Help for details of specific Keyword Arguments names can be found in the help tab at the bottom the the GhPython editor while editing the arguments:

{{< image url="/images/node-in-code-help.png" alt="/images/node-in-code-help.png" class="image_center" width="50%" >}}

At present, there is no way to switch components that have special settings to any alternative. For example the Bounding Box component has a special setting, Union Box:

{{< image url="/images/node-in-code-option.png" alt="/images/node-in-code-option.png" class="image_center" width="65%" >}}

### Managing Outputs

Components with multiple outputs will pass back a list or results corresponding to the sequential order of outputs for the component. Outputs come out of  ghpythonlib.components as sequential lists of lists.  In the case of (Points, Tangent Vectors, Parameters(t))

```Python
results  = ghcomp.DivideCurve(C, N, K)
results[0] # List of points from Divide
results[1] # List of Tangent Vectors
Results[2] # List of Pameters on the curve
```

A nice Python trick can be used to separate the output into separate lists for each output return values:

```python
P, T, t  = ghcomp.DivideCurve(C, N, K)
```
Now each variable contains an already separate list of values that can be used in subsequent functions in the script.

## Node in code from rhino.Python

In addition to [calling Grasshopper components as functions from the GhPython code](#components-as-functions-from-ghpython), the Grasshopper components are also outside of the Grasshopper canvas through rhino.python.

While the Grasshopper canvas will not be visible during this operation, it is worth noting that Grasshopper will load up the first time you call into the `ghpythonlib` assembly.  This can take a couple seconds the first time you run the script in Rhino.

As an example her is a script that calls into Grasshopper to use the Voronoi component to create voronoi cells around a few selected points.

```python
import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
import scriptcontext

points = rs.GetPoints(True, True)
if points:
    curves = ghcomp.Voronoi(points)
    for curve in curves:
        scriptcontext.doc.Objects.AddCurve(curve)
    for point in points:
        scriptcontext.doc.Objects.AddPoint(point)
    scriptcontext.doc.Views.Redraw()
```
The key is the ghpythonlib modules are available in the standard Python editor in Rhino. Behind the scenes things are running through Grasshopper code, but you don’t have to use a canvas to do your work.

This also lets you work in a slightly different way where you can get points in Rhino using rhinoscriptsyntax “get input” type functions and pass those points (or curves or breps) into the Grasshopper component code.

{{< image url="/images/node-in-code-rhino-python.png" alt="/images/node-in-code-rhino-python.png" class="image_center" width="90%" >}}

This opens up many more methods which are available to rhino.Python. Remember, this can be done for almost every component in Grasshopper (including every installed add-on component.) I use the term almost because there are cases where the function call doesn’t make sense. These cases are for things like Kangaroo or timers where the state of the component is important between iterations. Fortunately this is pretty rare.

Help for specific component arguments and return values can be found in the help tab at the bottom the the rhino.Python editor while editing the arguments.

{{< image url="/images/node-in-code-help.png" alt="/images/node-in-code-help.png" class="image_center" width="50%" >}}

## Related Topics

- [Your first script with Python in Grasshopper](/guides/rhinopython/what-is-rhinopython)
- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Editing Python in Grasshopper](/guides/rhinopython/python-running-scripts)
- [Python Guide for Rhino](/guides/rhinopython/)
