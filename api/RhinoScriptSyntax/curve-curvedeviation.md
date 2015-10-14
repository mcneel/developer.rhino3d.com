---
layout: bootstrap
---

# CurveDeviation

Returns the minimum and maximum deviation between two curve objects
        

### Parameters:

curve_a, curve_b = identifiers of two curves
        

### Returns:


tuple of deviation information on success
  element 0 = curve_a parameter at maximum overlap distance point
  element 1 = curve_b parameter at maximum overlap distance point
  element 2 = maximum overlap distance
  element 3 = curve_a parameter at minimum overlap distance point
  element 4 = curve_b parameter at minimum overlap distance point
  element 5 = minimum distance between curves
None on error
        
