---
layout: bootstrap
---

# BoundingBox

Returns either world axis-aligned or a construction plane axis-aligned
        bounding box of an object or of several objects
        

### Parameters:

- ***objects*** = The identifiers of the objects
- ***view_or_plane[opt]*** = Title or id of the view that contains the
    construction plane to which the bounding box should be aligned -or-
    user defined plane. If omitted, a world axis-aligned bounding box
    will be calculated
- ***in_world_coords[opt]*** = return the bounding box as world coordinates or
    construction plane coordinates. Note, this option does not apply to
    world axis-aligned bounding boxes.
        

### Returns:


Eight 3D points that define the bounding box. Points returned in counter-
clockwise order starting with the bottom rectangle of the box.
None on error
        
