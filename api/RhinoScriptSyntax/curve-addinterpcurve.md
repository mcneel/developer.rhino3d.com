---
layout: bootstrap
---

# AddInterpCurve

Adds an interpolated curve object to the document. Options exist to make
        a periodic curve or to specify the tangent at the endpoints. The resulting
        curve is a non-rational NURBS curve of the specified degree.
        

### Parameters:

- ***points*** = list containing 3D points to interpolate. For periodic curves,
    if the final point is a duplicate of the initial point, it is
    ignored. The number of control points must be >= (degree+1).
- ***degree[opt]*** = The degree of the curve (must be >=1).
    Periodic curves must have a degree >= 2. For knotstyle = 1 or 2,
    the degree must be 3. For knotstyle = 4 or 5, the degree must be odd
knotstyle[opt]
    0 Uniform knots.  Parameter spacing between consecutive knots is 1.0.
    1 Chord length spacing.  Requires degree = 3 with arrCV1 and arrCVn1 specified.
    2 Sqrt (chord length).  Requires degree = 3 with arrCV1 and arrCVn1 specified.
    3 Periodic with uniform spacing.
    4 Periodic with chord length spacing.  Requires an odd degree value.
    5 Periodic with sqrt (chord length) spacing.  Requires an odd degree value.
start_tangent [opt] = 3d vector that specifies a tangency condition at the
    beginning of the curve. If the curve is periodic, this argument must be omitted.
end_tangent [opt] = 3d vector that specifies a tangency condition at the
    end of the curve. If the curve is periodic, this argument must be omitted.
        

### Returns:


id of the new curve object if successful
        
