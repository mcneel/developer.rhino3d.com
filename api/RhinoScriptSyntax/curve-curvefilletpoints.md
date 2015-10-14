---
layout: bootstrap
---

# CurveFilletPoints

Find points at which to cut a pair of curves so that a fillet of a
        specified radius fits. A fillet point is a pair of points (point0, point1)
        such that there is a circle of radius tangent to curve curve0 at point0 and
        tangent to curve curve1 at point1. Of all possible fillet points, this
        function returns the one which is the closest to the base point base_point_0,
        base_point_1. Distance from the base point is measured by the sum of arc
        lengths along the two curves. 
        

### Parameters:

- ***curve_id_0*** = identifier of the first curve object.
- ***curve_id_1*** = identifier of the second curve object.
radius [opt] = The fillet radius. If omitted, a radius
               of 1.0 is specified.
base_point_0 [opt] = The base point on the first curve.
               If omitted, the starting point of the curve is used.
base_point_1 [opt] = The base point on the second curve. If omitted,
               the starting point of the curve is used.
return_points [opt] = If True (Default), then fillet points are
               returned. Otherwise, a fillet curve is created and
               it's identifier is returned.
        

### Returns:


If return_points is True, then a list of point and vector values
if successful. The list elements are as follows:
          
0    A point on the first curve at which to cut (arrPoint0).
1    A point on the second curve at which to cut (arrPoint1).
2    The fillet plane's origin (3-D point). This point is also
     the center point of the fillet
3    The fillet plane's X axis (3-D vector).
4    The fillet plane's Y axis (3-D vector).
5    The fillet plane's Z axis (3-D vector).
          
If return_points is False, then the identifier of the fillet curve
if successful.
None if not successful, or on error.                  
        
