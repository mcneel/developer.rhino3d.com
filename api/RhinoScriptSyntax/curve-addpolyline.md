---
layout: bootstrap
---

# AddPolyline

Adds a polyline curve to the current model
        

### Parameters:

- ***points*** = list of 3D points. Duplicate, consecutive points will be
         removed. The list must contain at least two points. If the
         list contains less than four points, then the first point and
         last point must be different.
- ***replace_id[opt]*** = If set to the id of an existing object, the object
         will be replaced by this polyline
        

### Returns:


id of the new curve object if successful
        
