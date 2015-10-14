---
layout: bootstrap
---

# PlanarClosedCurveContainment

Determines the relationship between the regions bounded by two coplanar
        simple closed curves
        

### Parameters:

curve_a, curve_b = identifiers of two planar, closed curves
- ***plane[opt]*** = test plane. If omitted, the currently active construction
  plane is used
- ***tolerance[opt]*** = if omitted, the document absolute tolerance is used
        

### Returns:


a number identifying the relationship if successful
  0 = the regions bounded by the curves are disjoint
  1 = the two curves intersect
  2 = the region bounded by curve_a is inside of curve_b
  3 = the region bounded by curve_b is inside of curve_a
None if not successful
        
