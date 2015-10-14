---
layout: bootstrap
---

# DivideCurve

Divides a curve object into a specified number of segments.
        

### Parameters:

- ***curve_id*** = identifier of the curve object
- ***segments*** = The number of segments.
create_points [opt] = Create the division points. If omitted or False,
    points are not created.
return_points [opt] = If omitted or True, points are returned.
    If False, then a list of curve parameters are returned.
        

### Returns:


If return_points is not specified or True, then a list containing 3D
division points.
If return_points is False, then an array containing division curve
parameters.
None if not successful, or on error.
        
