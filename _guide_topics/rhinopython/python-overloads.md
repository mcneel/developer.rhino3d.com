---
title: Calling Overloaded Methods from Python
description: This guide discusses calling overloaded methods with IronPython.
authors: ['dale_fugier']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Intermediate']
origin:
order: 30
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---


## Overview

.NET supports [overloading methods](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/member-overloading) by both number of arguments and type of arguments.

When [IronPython](https://ironpython.net/) code calls an overloaded method, it tries to select one of the overloads at runtime based on the number and type of arguments passed to the method, and also names of any keyword arguments.

In most cases, the expected overload gets selected. Selecting an overload is easy when the argument types are an exact match with one of the overload signatures:

```
from System.Collections import BitArray
ba = BitArray(5)       # calls __new__(System.Int32)
ba = BitArray(5, True) # calls __new__(System.Int32, System.Boolean)
ba = BitArray(ba)      # calls __new__(System.Collections.BitArray)
```

The argument types do not have be an exact match with the method signature. IronPython will try to convert the arguments if an unambiguous conversion exists to one of the overload signatures. 

The following code calls `__new__(System.Int32)` even though there are two constructors which take one argument, and neither of them accept a float as an argument:

```
from System.Collections import BitArray
ba = BitArray(5.0)
```

However, note that IronPython will raise a `TypeError` if there are conversions to more than one of the overloads:

```
from System.Collections import BitArray
ba = BitArray((1, 2, 3))
--
Message: Multiple targets could match: 
  BitArray(Array[Byte]), 
  BitArray(Array[bool]), 
  BitArray(Array[int])
```

If you want to control the exact overload that gets called, you can use the **Overloads** method on *method* objects:

```
from System.Collections import BitArray
int_bool_new = BitArray.__new__.Overloads[int, type(True)]
ba = int_bool_new(BitArray, 5, True)    # calls __new__(System.Int32, System.Boolean)
ba = int_bool_new(BitArray, 5, "hello") # converts "hello" to a System.Boolan
```

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

To use the second overload, use the **Overloads** method in this manner:

```python
out = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
```
Here is the full working sample:

```python
import System
import System.Collections.Generic.IEnumerable as IEnumerable
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

def SplitItUp():

   id = rs.GetObject("Select Brep to split", filter = 8+16, preselect = True)
   if not id: return
   brep = rs.coercebrep(id)

   ids = rs.GetObjects("Select cutting Breps", filter = 8+16,)
   if not ids: return
   cutters = [rs.coercebrep(item) for item in ids]
    
   tol = sc.doc.ModelAbsoluteTolerance
   out = brep.Split.Overloads[IEnumerable[Rhino.Geometry.Brep], System.Double](cutters, tol)
   
   rs.DeleteObject(id)
   
   for item in out:
       sc.doc.Objects.AddBrep(item)
   sc.doc.Views.Redraw()

SplitItUp()
```
