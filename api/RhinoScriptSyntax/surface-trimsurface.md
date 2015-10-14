---
layout: bootstrap
---

# TrimSurface

Remove portions of the surface outside of the specified interval
        

### Parameters:

- ***surface_id*** = surface identifier
- ***direction*** = 0(U), 1(V), or 2(U and V)
- ***interval*** = interval of the surface to keep.
  If both U and V then a list or tuple of 2 intervals
delete_input [opt] = should the input surface be deleted
        

### Returns:


new surface identifier on success
        
