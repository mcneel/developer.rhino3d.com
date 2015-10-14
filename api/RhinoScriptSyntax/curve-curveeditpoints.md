---
layout: bootstrap
---

# CurveEditPoints

Returns the edit, or Greville, points of a curve object. 
        For each curve control point, there is a corresponding edit point.
        

### Parameters:

- ***curve_id*** = identifier of the curve object
- ***return_parameters[opt]*** = if True, return as a list of curve parameters.
  If False, return as a list of 3d points
- ***segment_index[opt]*** = the curve segment is curve_id identifies a polycurve
        

### Returns:


curve parameters of 3d points on success
None on error
        
