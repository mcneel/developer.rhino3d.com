---
layout: bootstrap
---

# XformWorldToScreen

Transforms a point from world coordinates to either client-area coordinates of
        the specified view or screen coordinates. The resulting coordinates are represented
        as a 2D point
        

### Parameters:

- ***point*** = 3D point in world coordinates
- ***view[opt]*** = title or identifier of a view. If omitted, the active view is used
- ***screen_coordinates[opt]*** = if False, the function returns the results as
  client-area coordinates. If True, the result is in screen-area coordinates
        

### Returns:


2D point on success
None on error
        
