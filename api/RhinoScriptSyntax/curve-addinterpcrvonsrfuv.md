---
layout: bootstrap
---

# AddInterpCrvOnSrfUV

Adds an interpolated curve object based on surface parameters,
        that lies on a specified surface. Note, this function will not
        create periodic curves, but it will create closed curves.
        

### Parameters:

- ***surface_id*** = identifier of the surface to create the curve on
- ***points*** = list of 2D surface parameters. The list must contain
         at least 2 sets of parameters
        

### Returns:


id of the new curve object if successful
        
