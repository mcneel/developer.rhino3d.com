---
layout: bootstrap
---

# Angle

Measures the angle between two points
        

### Parameters:

point1, point2: the input points
- ***plane[opt]*** = Boolean or Plane
  If True, angle calculation is based on the world coordinate system.
  If False, angle calculation is based on the active construction plane
  If a plane is provided, angle calculation is with respect to this plane
        

### Returns:


tuple containing the following elements if successful
  element 0 = the X,Y angle in degrees
  element 1 = the elevation
  element 2 = delta in the X direction
  element 3 = delta in the Y direction
  element 4 = delta in the Z direction
None if not successful
        
