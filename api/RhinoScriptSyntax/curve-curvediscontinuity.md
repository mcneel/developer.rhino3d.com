---
layout: bootstrap
---

# CurveDiscontinuity

Search for a derivatitive, tangent, or curvature discontinuity in
        a curve object.
        

### Parameters:

- ***curve_id*** = identifier of curve object
- ***style*** = The type of continuity to test for. The types of
    continuity are as follows:
    Value    Description
    1        C0 - Continuous function
    2        C1 - Continuous first derivative
    3        C2 - Continuous first and second derivative
    4        G1 - Continuous unit tangent
    5        G2 - Continuous unit tangent and curvature
        

### Returns:


List 3D points where the curve is discontinuous
        
