---
layout: bootstrap
---

# CurveLength

Returns the length of a curve object.
        

### Parameters:

- ***curve_id*** = identifier of the curve object
segment_index [opt] = the curve segment if curve_id identifies a polycurve
sub_domain [opt] = list of two numbers identifing the sub-domain of the
    curve on which the calculation will be performed. The two parameters
    (sub-domain) must be non-decreasing. If omitted, the length of the
    entire curve is returned.
        

### Returns:


The length of the curve if successful.
None if not successful, or on error.
        
