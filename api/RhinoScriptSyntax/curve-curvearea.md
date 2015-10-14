---
layout: bootstrap
---

# CurveArea

Returns area of closed planar curves. The results are based on the
        current drawing units.
        

### Parameters:

- ***curve_id*** = The identifier of a closed, planar curve object.
        

### Returns:


List of area information. The list will contain the following information:
  Element  Description
  0        The area. If more than one curve was specified, the
           value will be the cumulative area.
  1        The absolute (+/-) error bound for the area.
        
