---
layout: bootstrap
---

# PointInPlanarClosedCurve

Determines if a point is inside of a closed curve, on a closed curve, or
        outside of a closed curve
        

### Parameters:

- ***point*** = text point
- ***curve*** = identifier of a curve object
- ***plane[opt]*** = plane containing the closed curve and point. If omitted,
    the currently active construction plane is used
- ***tolerance[opt]*** = it omitted, the document abosulte tolerance is used
        

### Returns:


number identifying the result if successful
    0 = point is outside of the curve
    1 = point is inside of the curve
    2 = point in on the curve
        
