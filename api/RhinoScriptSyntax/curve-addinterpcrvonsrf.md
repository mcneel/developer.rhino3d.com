---
layout: bootstrap
---

# AddInterpCrvOnSrf

Adds an interpolated curve object that lies on a specified
        surface.  Note, this function will not create periodic curves,
        but it will create closed curves.
        

### Parameters:

- ***surface_id*** = identifier of the surface to create the curve on
- ***points*** = list of 3D points that lie on the specified surface.
         The list must contain at least 2 points
        

### Returns:


id of the new curve object if successful
        
