---
layout: bootstrap
---

# AddTorus

Adds a torus shaped revolved surface to the document
        

### Parameters:

- ***base*** = 3D origin point of the torus or the base plane of the torus
major_radius, minor_radius = the two radii of the torus
- ***directions[opt]*** = A point that defines the direction of the torus when base is a point.
  If omitted, a torus that is parallel to the world XY plane is created
        

### Returns:


The identifier of the new object if successful.
None if not successful, or on error.
        
