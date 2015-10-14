---
layout: bootstrap
---

# CurveBrepIntersect

Intersects a curve object with a brep object. Note, unlike the
        CurveSurfaceIntersection function, this function works on trimmed surfaces.
        

### Parameters:

- ***curve_id*** = identifier of a curve object
- ***brep_id*** = identifier of a brep object
tolerance [opt] = distance tolerance at segment midpoints.
                  If omitted, the current absolute tolerance is used.
        

### Returns:


List of identifiers for the newly created intersection curve and
point objects if successful. None on error.            
        
