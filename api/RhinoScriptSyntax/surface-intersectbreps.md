---
layout: bootstrap
---

# IntersectBreps

Intersects a brep object with another brep object. Note, unlike the
        SurfaceSurfaceIntersection function this function works on trimmed surfaces.
        

### Parameters:

- ***brep1*** = identifier of first brep object
- ***brep2*** = identifier of second brep object
- ***tolerance*** = Distance tolerance at segment midpoints. If omitted,
            the current absolute tolerance is used.
        

### Returns:


List of Guids identifying the newly created intersection curve and
point objects if successful.
None if not successful, or on error.
        
