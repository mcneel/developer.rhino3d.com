---
layout: bootstrap
---

# SurfaceCurvature

Returns the curvature of a surface at a U,V parameter. See Rhino help
        for details of surface curvature
        

### Parameters:

- ***surface_id*** = the surface's identifier
- ***parameter*** = u,v parameter
        

### Returns:


tuple of curvature information
  element 0 = point at specified U,V parameter
  element 1 = normal direction
  element 2 = maximum principal curvature
  element 3 = maximum principal curvature direction
  element 4 = minimum principal curvature
  element 5 = minimum principal curvature direction
  element 6 = gaussian curvature
  element 7 = mean curvature
None if not successful, or on error
        
