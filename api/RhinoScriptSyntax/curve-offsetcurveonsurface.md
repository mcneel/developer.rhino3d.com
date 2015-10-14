---
layout: bootstrap
---

# OffsetCurveOnSurface

Offset a curve on a surface. The source curve must lie on the surface.
        The offset curve or curves will be added to Rhino
        

### Parameters:

curve_id, surface_id = curve and surface identifiers
- ***distance_or_parameter*** = If a single number is passed, then this is the
  distance of the offset. Based on the curve's direction, a positive value
  will offset to the left and a negative value will offset to the right.
  If a tuple of two values is passed, this is interpreted as the surface
  U,V parameter that the curve will be offset through
        

### Returns:


Identifiers of the new curves if successful
None on error
        
