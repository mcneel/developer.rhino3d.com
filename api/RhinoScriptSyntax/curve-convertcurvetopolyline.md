---
layout: bootstrap
---

# ConvertCurveToPolyline

Convert curve to a polyline curve
        

### Parameters:

- ***curve_id*** = identifier of a curve object
angle_tolerance [opt] = The maximum angle between curve tangents at line
  endpoints. If omitted, the angle tolerance is set to 5.0.
- ***tolerance[opt]*** = The distance tolerance at segment midpoints. If omitted,
  the tolerance is set to 0.01.
- ***delete_input[opt]*** = Delete the curve object specified by curve_id. If
  omitted, curve_id will not be deleted.
- ***min_edge_length[opt]*** = Minimum segment length
- ***max_edge_length[opt]*** = Maximum segment length
        

### Returns:


The new curve if successful.
        
