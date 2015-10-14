---
layout: bootstrap
---

# CurveClosestObject

Returns the 3D point locations on two objects where they are closest to
        each other. Note, this function provides similar functionality to that of
        Rhino's ClosestPt command.
        

### Parameters:

- ***curve_id*** = identifier of the curve object to test
- ***object_ids*** = list of identifiers of point cloud, curve, surface, or
  polysurface to test against
        

### Returns:


Tuple containing the results of the closest point calculation.
The elements are as follows:
  0    The identifier of the closest object.
  1    The 3-D point that is closest to the closest object. 
  2    The 3-D point that is closest to the test curve.
        
