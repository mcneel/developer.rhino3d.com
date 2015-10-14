---
layout: bootstrap
---

# AddCircle

Adds a circle curve to the document
        

### Parameters:

- ***plane_or_center*** = plane on which the circle will lie. If a point is
  passed, this will be the center of the circle on the active
  construction plane
- ***radius*** = the radius of the circle
        

### Returns:


id of the new curve object
        ### Example:

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
rs.AddCircle( plane, 5.0 )
        ```

### See Also:

  - [AddCircle3Pt](curve-addcircle3pt.html)
  - [CircleCenterPoint](curve-circlecenterpoint.html)
  - [CircleCircumference](curve-circlecircumference.html)
  - [CircleRadius](curve-circleradius.html)
  - [IsCircle](curve-iscircle.html)
