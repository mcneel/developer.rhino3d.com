---
layout: bootstrap
---

# ExtendSurface

Lengthens an untrimmed surface object
        

### Parameters:

- ***surface_id*** = identifier of a surface
- ***parameter*** = tuple of two values definfing the U,V parameter to evaluate.
  The surface edge closest to the U,V parameter will be the edge that is
  extended
- ***length*** = amount to extend to surface
- ***smooth[opt]*** = If True, the surface is extended smoothly curving from the
  edge. If False, the surface is extended in a straight line from the edge
        

### Returns:


True or False indicating success or failure
        
