---
layout: bootstrap
---

# AddSrfContourCrvs

Adds a spaced series of planar curves resulting from the intersection of
        defined cutting planes through a surface or polysurface. For more
        information, see Rhino help for details on the Contour command
        

### Parameters:

- ***object_id*** = object identifier
- ***points_or_plane*** = either a list/tuple of two points or a plane
  if two points, they define the start and end points of a center line
  if a plane, the plane defines the cutting plane
- ***interval[opt]*** = distance beween contour curves.
        

### Returns:


ids of new curves on success
None on error
        
