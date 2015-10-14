---
layout: bootstrap
---

# ObjectGripLocations

Returns or modifies the location of all grips owned by an object. The
        locations of the grips are returned in a list of Point3d with each position
        in the list corresponding to that grip's index. To modify the locations of
        the grips, you must provide a list of points that contain the same number
        of points at grips
        

### Parameters:

- ***object_id*** = identifier of the object
points [opt] = list of 3D points identifying the new grip locations
        

### Returns:


if points is not specified, the current location of all grips
if points is specified, the previous location of all grips
None if not successful
        
