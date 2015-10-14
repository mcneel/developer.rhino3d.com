---
layout: bootstrap
---

# CurveAreaCentroid

Returns area centroid of closed, planar curves. The results are based
        on the current drawing units.
        

### Parameters:

- ***curve_id*** = The identifier of a closed, planar curve object.
        

### Returns:


Tuple of area centroid information containing the following information:
  Element  Description
  0        The 3d centroid point. If more than one curve was specified,
           the value will be the cumulative area.
  1        A 3d vector with the absolute (+/-) error bound for the area
           centroid.
        
