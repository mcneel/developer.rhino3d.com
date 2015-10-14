---
layout: bootstrap
---

# CurveMeshIntersection

Calculates the intersection of a curve object and a mesh object
        

### Parameters:

- ***curve_id*** = identifier of a curve object
- ***mesh_id*** = identifier or a mesh object
- ***return_faces[opt]*** = return both intersection points and face indices.
  If False, then just the intersection points are returned
        

### Returns:


if return_false is omitted or False, then a list of intersection points
if return_false is True, the a one-dimensional list containing information
  about each intersection. Each element contains the following two elements
  (point of intersection, mesh face index where intersection lies)
None on error
        
