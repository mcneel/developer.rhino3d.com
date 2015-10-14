---
layout: bootstrap
---

# AddNurbsCurve

Adds a NURBS curve object to the document
        

### Parameters:

- ***points*** = list containing 3D control points
- ***knots*** = Knot values for the curve. The number of elements in knots must
    equal the number of elements in points plus degree minus 1
- ***degree*** = degree of the curve. must be greater than of equal to 1
- ***weights[opt]*** = weight values for the curve. Number of elements should
    equal the number of elements in points. Values must be greater than 0
        


