+++
aliases = ["/en/5/samples/rhinopython/circle-from-length/", "/en/6/samples/rhinopython/circle-from-length/", "/en/7/samples/rhinopython/circle-from-length/", "/wip/samples/rhinopython/circle-from-length/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a circle based on its circumference using Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Circle From Length"
type = "samples/python"
weight = 3

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

```python
# Create a circle from a center point and a circumference.
import rhinoscriptsyntax as rs
import math

def CreateCircle(circumference=None):
    center = rs.GetPoint("Center point of circle")
    if center:
        plane = rs.MovePlane(rs.ViewCPlane(), center)
        length = circumference
        if length is None: length = rs.GetReal("Circle circumference")
        if length and length>0:
            radius = length/(2*math.pi)
            objectId = rs.AddCircle(plane, radius)
            rs.SelectObject(objectId)
            return length
    return None

# Check to see if this file is being executed as the "Main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == '__main__':
    CreateCircle()

# NOTE: see UseModule.py sample for using this script as a module
```
