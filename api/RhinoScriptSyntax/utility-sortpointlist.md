---
layout: bootstrap
---

# SortPointList

Sorts list of points so they will be connected in a "reasonable" polyline order
        

### Parameters:

- ***points*** = the points to sort
- ***tolerance[opt]*** = minimum distance between points. Points that fall within this tolerance
  will be discarded. If omitted, Rhino's internal zero tolerance is used.
        

### Returns:


a list of sorted 3D points if successful
None on error
        
