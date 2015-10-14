---
layout: bootstrap
---

# MeshClosestPoint

Returns the point on a mesh that is closest to a test point
        

### Parameters:

- ***object_id*** = identifier of a mesh object
- ***point*** = point to test
- ***maximum_distance[opt]*** = upper bound used for closest point calculation.
  If you are only interested in finding a point Q on the mesh when
  point.DistanceTo(Q) < maximum_distance, then set maximum_distance to
  that value
        

### Returns:


Tuple containing the results of the calculation where
  element[0] = the 3-D point on the mesh
  element[1] = the index of the mesh face on which the 3-D point lies
None on error
        
