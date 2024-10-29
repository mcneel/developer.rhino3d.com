+++
aliases = ["/en/5/guides/rhinopython/python-reference/", "/en/6/guides/rhinopython/python-reference/", "/en/7/guides/rhinopython/python-reference/", "/en/wip/guides/rhinopython/python-reference/"]
authors = [ "dale" ]
categories = [ "Intermediate" ]
description = "This guide discusses calling methods with by-ref parameters with IronPython."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Providing Arguments for By-Reference Parameters"
type = "guides"
weight = 30
override_last_modified = "2019-09-09T15:01:33Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"
+++

## Overview

Python functions can return multiple objects as a *tuple*. 

On the other hand, .NET methods, like those provided by RhinoCommon, can only return one object as the result of a call. In order to return more than one object, by-reference, or *by-ref*, parameters are needed. These parameters are decorated with the `ref` and  `out` keywords in C#.

## More Information

A example of a method that requires a by-ref parameter is [Dictionary.TryGetValue](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2.trygetvalue), which has a `value`  [output parameter](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier). The method returns `true` if the dictionary contains an element with the specified key (the element value itself is returned to the parameter "value"), otherwise it returns `false`.

When making calls to such methods in IronPython, we may not pass in arguments for the output parameters. Instead, the result of such .NET method call in IronPython will likely be a tuple (unless the .NET method's return type is `void` and the method has only one by-ref parameter), which contains the value of the output parameter (see the example below).

```python
import System
d = System.Collections.Generic.Dictionary[int, str]()
d[1], d[2] = 'One', 'Two'
 
print d.TryGetValue(1)         # (True, 'One')
print d.TryGetValue(2)[1]      # Two 
print d.TryGetValue(3)         # (False, None)
```

We may also pass a **clr.Reference** object for the output parameter. The **clr.Reference** object has only one member "Value", which will carry the output parameter value after the call. When encountering this type of argument, the IronPython code generation and runtime does something special to update the "Value".

```python
x = clr.Reference[str]()
print d.TryGetValue(1, x), x.Value   # True One
print d.TryGetValue(3, x), x.Value   # False None
```

For [reference parameters](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref), we are required to pass in something. If the argument is not a **clr.Reference** object, such reference argument value will also be part of the returned tuple; otherwise, the by-ref change is tracked inside **clr.Reference**.

Note, if the .NET method contains more than one by-ref parameter, Python expects the user to provide proper **clr.Reference** objects for either all or none of them. A mix of **clr.Reference** objects and normal argument/omission (for out parameter) will cause an error.

## Example

For a practical example, let's look at RhinoCommon's [NurbsSurfacePointList.GetPoint](https://developer.rhino3d.com/api/RhinoCommon/html/Overload_Rhino_Geometry_Collections_NurbsSurfacePointList_GetPoint.htm) method, which has two overloads:

```
// Gets a world 3-D, or Euclidean, control point at the given u,v index. 
// The 4-D representation is (x, y, z, 1.0).
public bool GetPoint(int u, int v, out Point3d point)

// Gets a homogeneous control point at the given (u, v) index, 
// where the 4-D representation is (x, y, z, w). 
// The world 3-D, or Euclidean, representation is (x/w, y/w, z/w).
public bool GetPoint(int u, int v, out Point4d point)
```

The following sample code calls each overloaded method. Notice how using **clr.Reference** eliminates the need for using the **Overloads** method, in this case. 

```python
import clr
import Rhino
import rhinoscriptsyntax as rs

srf_id = rs.GetObject("Select surface", rs.filter.surface)
srf = rs.coercesurface(srf_id)
ns = srf.ToNurbsSurface()

pt3d = clr.Reference[Rhino.Geometry.Point3d]()
for u in range(0, ns.Points.CountU):
    for v in range(0, ns.Points.CountV):
        if ns.Points.GetPoint(u, v, pt3d):
            print pt3d

pt4d = clr.Reference[Rhino.Geometry.Point4d]()
for u in range(0, ns.Points.CountU):
    for v in range(0, ns.Points.CountV):
        if ns.Points.GetPoint(u, v, pt4d):
            print pt4d
```
