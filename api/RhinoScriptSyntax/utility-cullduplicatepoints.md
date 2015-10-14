---
layout: bootstrap
---

# CullDuplicatePoints

Removes duplicates from a list of 3D points.
        

### Parameters:

- ***points*** = A list of 3D points.
tolerance [opt] = Minimum distance between points. Points within this
  tolerance will be discarded. If omitted, Rhino's internal zero tolerance
  is used.
        

### Returns:


list of 3D points with duplicates removed if successful.
None if not successful
        
