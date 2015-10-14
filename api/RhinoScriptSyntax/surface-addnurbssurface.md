---
layout: bootstrap
---

# AddNurbsSurface

Adds a NURBS surface object to the document
        

### Parameters:

- ***point_count*** = number of control points in the u and v direction
- ***points*** = list of 3D points
- ***knots_u*** = knot values for the surface in the u direction.
          Must contain point_count[0]+degree[0]-1 elements
- ***knots_v*** = knot values for the surface in the v direction.
          Must contain point_count[1]+degree[1]-1 elements
- ***degree*** = degree of the surface in the u and v directions.
- ***weights[opt]*** = weight values for the surface. The number of elements in
  weights must equal the number of elements in points. Values must be
  greater than zero.
        

### Returns:


identifier of new object if successful
None on error
        
