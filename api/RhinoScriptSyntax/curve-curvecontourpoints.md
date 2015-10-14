---
layout: bootstrap
---

# CurveContourPoints

Returns the 3D point locations calculated by contouring a curve object.
        

### Parameters:

- ***curve_id*** = identifier of a curve object.
- ***start_point*** = 3D starting point of a center line.
- ***end_point*** = 3D ending point of a center line.
interval [opt] = The distance between contour curves. If omitted, 
the interval will be equal to the diagonal distance of the object's
bounding box divided by 50.
        

### Returns:


A list of 3D points, one for each contour
        
