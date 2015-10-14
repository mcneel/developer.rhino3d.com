---
layout: bootstrap
---

# PlaneClosestPoint

Returns the point on a plane that is closest to a test point.
        

### Parameters:

- ***plane*** = The plane
- ***point*** = The 3-D point to test.
return_point [opt] = If omitted or True, then the point on the plane
   that is closest to the test point is returned. If False, then the
   parameter of the point on the plane that is closest to the test
   point is returned.
        

### Returns:


If return_point is omitted or True, then the 3-D point
If return_point is False, then an array containing the U,V parameters
of the point
None if not successful, or on error.
        
