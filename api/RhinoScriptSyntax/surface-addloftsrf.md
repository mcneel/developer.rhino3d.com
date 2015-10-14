---
layout: bootstrap
---

# AddLoftSrf

Adds a surface created by lofting curves to the document.
        - no curve sorting performed. pass in curves in the order you want them sorted
        - directions of open curves not adjusted. Use CurveDirectionsMatch and
          ReverseCurve to adjust the directions of open curves
        - seams of closed curves are not adjusted. Use CurveSeam to adjust the seam
          of closed curves
        

### Parameters:

- ***object_ids*** = ordered list of the curves to loft through
start [opt] = starting point of the loft
end [opt] = ending point of the loft
loft_type [opt] = type of loft. Possible options are:
  0 = Normal. Uses chord-length parameterization in the loft direction
  1 = Loose. The surface is allowed to move away from the original curves
      to make a smoother surface. The surface control points are created
      at the same locations as the control points of the loft input curves.
  2 = Straight. The sections between the curves are straight. This is
      also known as a ruled surface.
  3 = Tight. The surface sticks closely to the original curves. Uses square
      root of chord-length parameterization in the loft direction
  4 = Developable. Creates a separate developable surface or polysurface
      from each pair of curves.
simplify_method [opt] = Possible options are:
  0 = None. Does not simplify.
  1 = Rebuild. Rebuilds the shape curves before lofting.
  2 = Refit. Refits the shape curves to a specified tolerance
value [opt] = A value based on the specified style.
  style=1 (Rebuild), then value is the number of control point used to rebuild
  style=1 is specified and this argument is omitted, then curves will be
  rebuilt using 10 control points.
  style=2 (Refit), then value is the tolerance used to rebuild.
  style=2 is specified and this argument is omitted, then the document's
  absolute tolerance us used for refitting.
        

### Returns:


Array containing the identifiers of the new surface objects if successful
None on error
        
