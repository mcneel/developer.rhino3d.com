---
layout: bootstrap
---

# OffsetSurface

Offsets a trimmed or untrimmed surface by a distance. The offset surface
        will be added to Rhino.
        

### Parameters:

- ***surface_id*** = the surface's identifier
- ***distance*** = the distance to offset
tolerance [opt] = The offset tolerance. Use 0.0 to make a loose offset. Otherwise, the
  document's absolute tolerance is usually sufficient.
both_sides [opt] = Offset to both sides of the input surface
create_solid [opt] = Make a solid object
        

### Returns:


identifier of the new object if successful
None on error
        
