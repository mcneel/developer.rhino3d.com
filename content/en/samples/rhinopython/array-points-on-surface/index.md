+++
aliases = ["/en/5/samples/rhinopython/array-points-on-surface/", "/en/6/samples/rhinopython/array-points-on-surface/", "/en/7/samples/rhinopython/array-points-on-surface/", "/en/wip/samples/rhinopython/array-points-on-surface/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to array points on a surface using Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Array Points on Surface"
type = "samples/python"
weight = 2

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++

```python
# Creates an array of points on a surface
import rhinoscriptsyntax as rs

def ArrayPointsOnSurface():
    # Get the surface object
    surface_id = rs.GetObject("Select surface", rs.filter.surface)
    if surface_id is None: return

    # Get the number of rows
    rows = rs.GetInteger("Number of rows", 2, 2)
    if rows is None: return

    # Get the number of columns
    columns = rs.GetInteger("Number of columns", 2, 2)
    if columns is None: return

    # Get the domain of the surface
    U = rs.SurfaceDomain(surface_id, 0)
    V = rs.SurfaceDomain(surface_id, 1)
    if U is None or V is None: return

    # Add the points
    for i in range(0,rows):
        param0 = U[0] + (((U[1] - U[0]) / (rows-1)) * i)
        for j in range(0,columns):
            param1 = V[0] + (((V[1] - V[0]) / (columns-1)) * j)
            point = rs.EvaluateSurface(surface_id, param0, param1)
            rs.AddPoint(point)


# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    # call the function defined above
    ArrayPointsOnSurface()
```
