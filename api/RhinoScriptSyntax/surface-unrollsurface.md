---
layout: bootstrap
---

# UnrollSurface

Flattens a developable surface or polysurface
        

### Parameters:

- ***surface_id*** = the surface's identifier
- ***explode[opt]*** = If True, the resulting surfaces ar not joined
- ***following_geometry[opt]*** = List of curves, dots, and points which
  should be unrolled with the surface
        

### Returns:


List of unrolled surface ids
if following_geometry is not None, a tuple where item 1
  is the list of unrolled surface ids and item 2 is the
  list of unrolled following geometry
        
