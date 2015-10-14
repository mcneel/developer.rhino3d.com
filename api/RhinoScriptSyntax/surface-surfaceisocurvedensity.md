---
layout: bootstrap
---

# SurfaceIsocurveDensity

Returns or sets the isocurve density of a surface or polysurface object.
        An isoparametric curve is a curve of constant U or V value on a surface.
        Rhino uses isocurves and surface edge curves to visualize the shape of a
        NURBS surface
        

### Parameters:

- ***surface_id*** = the surface's identifier
- ***density[opt]*** = the isocurve wireframe density. The possible values are
    -1: Hides the surface isocurves
     0: Display boundary and knot wires
     1: Display boundary and knot wires and one interior wire if there
        are no interior knots
   >=2: Display boundary and knot wires and (N+1) interior wires
        

### Returns:


If density is not specified, then the current isocurve density if successful
If density is specified, the the previous isocurve density if successful
None on error
        
