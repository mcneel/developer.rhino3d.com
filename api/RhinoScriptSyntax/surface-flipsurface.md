---
layout: bootstrap
---

# FlipSurface

Returns or changes the normal direction of a surface. This feature can
        also be found in Rhino's Dir command
        

### Parameters:

- ***surface_id*** = identifier of a surface object
- ***flip[opt]*** = new normal orientation, either flipped(True) or not flipped (False).
        

### Returns:


if flipped is not specified, the current normal orientation
if flipped is specified, the previous normal orientation
None on error
        
