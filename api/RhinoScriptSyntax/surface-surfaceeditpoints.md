---
layout: bootstrap
---

# SurfaceEditPoints

Returns the edit, or Greville points of a surface object. For each
        surface control point, there is a corresponding edit point
        

### Parameters:

- ***surface_id*** = the surface's identifier
- ***return_parameters[opt]*** = If False, edit points are returned as a list of
  3D points. If True, edit points are returned as a list of U,V surface
  parameters
- ***return_all[opt]*** = If True, all surface edit points are returned. If False,
  the function will return surface edit points based on whether or not the
  surface is closed or periodic
        

### Returns:


if return_parameters is False, a list of 3D points
if return_parameters is True, a list of U,V parameters
None on error
        
