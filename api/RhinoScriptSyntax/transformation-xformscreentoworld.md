---
layout: bootstrap
---

# XformScreenToWorld

Transforms a point from either client-area coordinates of the specified view
        or screen coordinates to world coordinates. The resulting coordinates are represented
        as a 3-D point
        

### Parameters:

- ***point*** = 2D point
- ***view[opt]*** = title or identifier of a view. If omitted, the active view is used
- ***screen_coordinates[opt]*** = if False, point is in client-area coordinates. If True,
point is in screen-area coordinates
        

### Returns:


3D point on success
None on error
        
