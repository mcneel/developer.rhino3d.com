---
layout: bootstrap
---

# OffsetCurve

Offsets a curve by a distance. The offset curve will be added to Rhino
        

### Parameters:

- ***object_id*** = identifier of a curve object
- ***direction*** = point describing direction of the offset
- ***distance*** = distance of the offset
- ***normal[opt]*** = normal of the plane in which the offset will occur.
    If omitted, the normal of the active construction plane will be used
- ***style[opt]*** = the corner style
    0 = None, 1 = Sharp, 2 = Round, 3 = Smooth, 4 = Chamfer
        

### Returns:


List of ids for the new curves on success
None on error
        
