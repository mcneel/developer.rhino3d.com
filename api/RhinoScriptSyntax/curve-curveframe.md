---
layout: bootstrap
---

# CurveFrame

Returns the plane at a parameter of a curve. The plane is based on the
        tangent and curvature vectors at a parameter.
        

### Parameters:

- ***curve_id*** = identifier of the curve object.
- ***parameter*** = parameter to evaluate.
segment_index [opt] = the curve segment if curve_id identifies a polycurve
        

### Returns:


The plane at the specified parameter if successful. 
None if not successful, or on error.
        
