---
layout: bootstrap
---

# CurveSurfaceIntersection

Calculates intersection of a curve object with a surface object.
        Note, this function works on the untrimmed portion of the surface.
        

### Parameters:

- ***curve_id*** = The identifier of the first curve object.
- ***surface_id*** = The identifier of the second curve object. If omitted,
    the a self-intersection test will be performed on curve.
tolerance [opt] = The absolute tolerance in drawing units. If omitted, 
    the document's current absolute tolerance is used.
angle_tolerance [opt] = angle tolerance in degrees. The angle
    tolerance is used to determine when the curve is tangent to the
    surface. If omitted, the document's current angle tolerance is used.
        

### Returns:


Two-dimensional list of intersection information if successful.
The list will contain one or more of the following elements:
  Element Type     Description
  (n, 0)  Number   The intersection event type, either Point(1) or Overlap(2).
  (n, 1)  Point3d  If the event type is Point(1), then the intersection point 
                   on the first curve. If the event type is Overlap(2), then
                   intersection start point on the first curve.
  (n, 2)  Point3d  If the event type is Point(1), then the intersection point
                   on the first curve. If the event type is Overlap(2), then
                   intersection end point on the first curve.
  (n, 3)  Point3d  If the event type is Point(1), then the intersection point 
                   on the second curve. If the event type is Overlap(2), then
                   intersection start point on the surface.
  (n, 4)  Point3d  If the event type is Point(1), then the intersection point
                   on the second curve. If the event type is Overlap(2), then
                   intersection end point on the surface.
  (n, 5)  Number   If the event type is Point(1), then the first curve parameter.
                   If the event type is Overlap(2), then the start value of the
                   first curve parameter range.
  (n, 6)  Number   If the event type is Point(1), then the first curve parameter.
                   If the event type is Overlap(2), then the end value of the
                   curve parameter range.
  (n, 7)  Number   If the event type is Point(1), then the U surface parameter.
                   If the event type is Overlap(2), then the U surface parameter
                   for curve at (n, 5).
  (n, 8)  Number   If the event type is Point(1), then the V surface parameter.
                   If the event type is Overlap(2), then the V surface parameter
                   for curve at (n, 5).
  (n, 9)  Number   If the event type is Point(1), then the U surface parameter.
                   If the event type is Overlap(2), then the U surface parameter
                   for curve at (n, 6).
  (n, 10) Number   If the event type is Point(1), then the V surface parameter.
                   If the event type is Overlap(2), then the V surface parameter
                   for curve at (n, 6).
        
