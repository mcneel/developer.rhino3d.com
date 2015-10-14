---
layout: bootstrap
---

# DivideCurveLength

Divides a curve object into segments of a specified length.
        

### Parameters:

- ***curve_id*** = identifier of the curve object
- ***length*** = The length of each segment.
create_points [opt] = Create the division points. If omitted or False,
    points are not created.
return_points [opt] = If omitted or True, points are returned.
    If False, then a list of curve parameters are returned.
        

### Returns:


If return_points is not specified or True, then a list containing 3D
division points if successful.
If return_points is False, then an array containing division curve
parameters if successful.
None if not successful, or on error.
        
