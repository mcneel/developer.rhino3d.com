---
layout: bootstrap
---

# CurveCurvature

Returns the curvature of a curve at a parameter. See the Rhino help for
        details on curve curvature
        

### Parameters:

- ***curve_id*** = identifier of the curve
- ***parameter*** = parameter to evaluate
        

### Returns:


Tuple of curvature information on success
  element 0 = point at specified parameter
  element 1 = tangent vector
  element 2 = center of radius of curvature
  element 3 = radius of curvature
  element 4 = curvature vector
None on failure
        
