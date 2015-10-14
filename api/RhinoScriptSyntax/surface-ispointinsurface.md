---
layout: bootstrap
---

# IsPointInSurface

Verifies that a point is inside a closed surface or polysurface
        

### Parameters:

object_id: the object's identifier
point: list of three numbers or Point3d. The test, or sampling point
strictly_in[opt]: If true, the test point must be inside by at least tolerance
tolerance[opt]: distance tolerance used for intersection and determining
  strict inclusion. If omitted, Rhino's internal tolerance is used
        

### Returns:


True if successful, otherwise False
        
