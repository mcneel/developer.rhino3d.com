---
layout: bootstrap
---

# IntersectSpheres

Calculates intersections of two spheres
        

### Parameters:

- ***sphere_plane0*** = an equatorial plane of the first sphere. The origin of the
  plane will be the center point of the sphere
- ***sphere_radius0*** = radius of the first sphere
- ***sphere_plane1*** = plane for second sphere
- ***sphere_radius1*** = radius for second sphere
        

### Returns:


List of intersection results
  element 0 = type of intersection (0=point, 1=circle, 2=spheres are identical)
  element 1 = Point of intersection or plane of circle intersection
  element 2 = radius of circle if circle intersection
None on error
        
