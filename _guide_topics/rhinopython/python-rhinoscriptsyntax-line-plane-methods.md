---
title: Line and Plane Methods
description: This guide provides an overview of the rhinoscriptsytntax Line and Plane methods.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 98
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Line and Plane Methods

The following methods are available for creating and manipulating lines and planes.

Lines are represented as zero-based, one-dimensional arrays containing two elements: the start point (3-D point) and the end point (3-D point).

Planes are represented as zero-based, one-dimensional arrays containing four elements: the plane's origin (3-D point), the plane's x-axis direction (3-D vector), the plane's y-axis direction (3-D vector), and the plane's z-axis direction (3-D vector).

For more information in [RhinoScript Fundamentals](({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-introduction)).

| Method | | |  Description |
|:--------|:-:|:-:|:--------|
| DistanceToPlane | | | Returns the distance from a plane to a point. |
| EvaluatePlane | | | Evaluates a point on a plane. |
| IntersectPlanes | | | Returns the point calculated by intersecting three planes. |
| LineArcIntersection | | | Intersects an infinite line and an arc. |
| LineBetweenCurves | | | Create a line perpendicular or tangent between two curves. |
| LineBoxIntersection | | | Intersects an infinite line and an axis aligned bounding box. |
| LineCircleIntersection | | | Intersects an infinite line and a circle. |
| LineClosestPoint | | | Finds the point on an infinite line that is closest to a test point. |
| LineCurveIntersection | | | Intersect an infinite line and a curve object. |
| LineCylinderIntersection | | | Calculates the intersection of a line and a cylinder. |
| LineIsFartherThan | | | Determines if the shortest distance from a line to a point or another line is greater than a specified distance. |
| LineLineIntersection | | | Returns the point calculated by intersecting two lines. |
| LineMaxDistanceTo | | | Finds the longest distance between the line, as a finite chord, and a point or another line. |
| LineMeshIntersection | | | Intersects an infinite line with a mesh object. |
| LineMinDistanceTo | | | Finds the shortest distance between the line, as a finite chord, and a point or another line. |
| LinePlane | | | Returns a plane that contains the line. |
| LinePlaneIntersection | | | Returns the point calculated by intersecting a line with a plane. |
| LineSphereIntersection | | | Calculates the intersection of a line and a sphere. |
| LineTransform | | | Transforms a line. |
| MovePlane | | | Moves the origin of a plane. |
| PlaneAngle | | | Calculates the angle between two points on a plane. |
| PlaneArcIntersection | | | Intersects a plane and an arc. |
| PlaneCircleIntersection | | | Intersects a plane and a circle. |
| PlaneClosestPoint | | | Returns the closest point on a plane from a point. |
| PlaneCurveIntersection | | | Intersects an infinite plane and a curve object. |
| PlaneEquation | | | Returns the equation of a plane. |
| PlaneFitFromPoints | | | Returns a plane through an array of points. |
| PlaneFromFrame | | | Creates a plane from an origin point, X axis direction, and Y axis direction. |
| PlaneFromNormal | | | Creates a plane from an origin point, and a normal direction. |
| PlaneFromPoints | | | Creates a plane from three non-colinear points. |
| PlanePlaneIntersection | | | Returns the line calculated by intersecting two planes. |
| PlaneSphereIntersection | | | Calculates the intersection of a plane and a sphere. |
| PlaneTransform | | | Transforms a plane. |
| RotatePlane | | | Rotates a plane. |
| WorldXYPlane | | | Returns Rhino's world XY plane. |
| WorldYZPlane | | | Returns Rhino's world YZ plane. |
| WorldZXPlane | | | Returns Rhino's world ZX plane. |
|=====
|
{: rules="groups"}

---

## Related Topics

- [What is RhinoScriptSyntax and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python List of Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
- [RhinoScript Points and Vectors Methods]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods)
