---
layout: bootstrap
---

# AddCutPlane

Adds a planar surface through objects at a designated location. For more
        information, see the Rhino help file for the CutPlane command
        

### Parameters:

- ***objects_ids*** = identifiers of objects that the cutting plane will
    pass through
start_point, end_point = line that defines the cutting plane
- ***normal[opt]*** = vector that will be contained in the returned planar
    surface. In the case of Rhino's CutPlane command, this is the
    normal to, or Z axis of, the active view's construction plane.
    If omitted, the world Z axis is used
        

### Returns:


identifier of new object on success
None on error
        
