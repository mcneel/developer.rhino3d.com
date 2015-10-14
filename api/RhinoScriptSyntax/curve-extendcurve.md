---
layout: bootstrap
---

# ExtendCurve

Extends a non-closed curve object by a line, arc, or smooth extension
        until it intersects a collection of objects.
        

### Parameters:

curve_id: identifier of curve to extend
extension_type: 0 = line, 1 = arc, 2 = smooth
side: 0=extend from the start of the curve, 1=extend from the end of the curve
boundary_object_ids: curve, surface, and polysurface objects to extend to
        

### Returns:


The identifier of the new object if successful.
None if not successful
        
