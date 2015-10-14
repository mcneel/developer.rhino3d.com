---
layout: bootstrap
---

# OsnapMode

Returns or sets the object snap mode. Object snaps are tools for
        specifying points on existing objects
        

### Parameters:

mode [opt] = The object snap mode or modes to set. Object snap modes
             can be added together to set multiple modes
             0     None
             2     Near
             8     Focus
             32    Center
             64    Vertex
             128   Knot
             512   Quadrant
             2048  Midpoint
             8192  Intersection
             0x20000   End
             0x80000   Perpendicular
             0x200000   Tangent
             0x8000000  Point
        

### Returns:


if mode is not specified, then the current object snap mode(s)
if mode is specified, then the previous object snap mode(s) 
        
