+++
aliases = ["/5/guides/rhinopython/python-overloads/", "/6/guides/rhinopython/python-overloads/", "/7/guides/rhinopython/python-overloads/", "/wip/guides/rhinopython/python-overloads/"]
authors = [ "dale" ]
categories = [ "Intermediate" ]
description = "This guide discusses calling overloaded methods with IronPython."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Calling Overloaded Methods from Python"
type = "guides"
weight = 30
override_last_modified = "2019-04-12T12:09:46Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0
version = [ "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Problem

When you run a script that calls a RhinoCommon method that has [overloads](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/member-overloading) , you might see the following error:
```
Message: Multiple targets could match
```

## More Information

.NET supports [overloading methods](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/member-overloading) by both number of arguments and type of arguments.

When [IronPython](https://ironpython.net/) code calls an overloaded method, it tries to select one of the overloads at runtime based on the number and type of arguments passed to the method, and also names of any keyword arguments.

In most cases, the expected overload gets selected. However, [IronPython](https://ironpython.net/) will raise a `TypeError` if there are conversions to more than one of the overloads:

To control the exact overload that gets called, use the **Overloads** method on *method* objects:

## Example

For a practical example, let's look at RhinoCommon's [Brep.Split](https://developer.rhino3d.com/api/RhinoCommon/html/Overload_Rhino_Geometry_Brep_Split.htm) method, which has five overloads:

```
// Splits a Brep into pieces using a Brep as a cutter.
public Brep[] Split(Brep splitter, double intersectionTolerance)

// Splits a Brep into pieces using Breps as cutters.
public Brep[] Split(IEnumerable<Brep> cutters, double intersectionTolerance)

// Splits a Brep into pieces using curves, at least partially on the Brep, as cutters.
public Brep[] Split(IEnumerable<Curve> cutters, double intersectionTolerance)

// Splits a Brep into pieces using a Brep as a cutter.
public Brep[] Split(Brep splitter, double intersectionTolerance, out bool toleranceWasRaised)

// Splits a Brep into pieces using a combination of curves, to be extruded, and Breps as cutters.
public Brep[] Split(IEnumerable<GeometryBase> cutters, Vector3d normal, bool planView, double intersectionTolerance)
```

If you run the following example code, which should split a `Brep` with one or more cutting `Breps`:

```
import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

id = rs.GetObject("Select Brep to split", filter = 8+16, preselect = True)
brep = rs.coercebrep(id)

ids = rs.GetObjects("Select cutting Breps", filter = 8+16,)
cutters = [rs.coercebrep(item) for item in ids]

tol = sc.doc.ModelAbsoluteTolerance
out_breps = brep.Split(cutters, tol)
new_ids = [sc.doc.Objects.AddBrep(brep) for brep in out_breps]
```

You will receive the following error:

```
Message: Multiple targets could match: Split(IEnumerable[Curve], float), Split(IEnumerable[Brep], float)
```

To use the second overload, use the **Overloads** method in this manner:

```python
out_breps = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
```
Here is the full working sample:

```python
import System
import System.Collections.Generic.IEnumerable as IEnumerable
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

id = rs.GetObject("Select Brep to split", filter = 8+16, preselect = True)
brep = rs.coercebrep(id)

ids = rs.GetObjects("Select cutting Breps", filter = 8+16,)
cutters = [rs.coercebrep(item) for item in ids]
    
tol = sc.doc.ModelAbsoluteTolerance
out_breps = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
new_ids = [sc.doc.Objects.AddBrep(brep) for brep in out_breps]
```
