---
layout: bootstrap
---

# BrepClosestPoint

Returns the point on a surface or polysurface that is closest to a test
        point. This function works on both untrimmed and trimmed surfaces.
        

### Parameters:

- ***object_id*** = The object's identifier.
- ***point*** = The test, or sampling point.
        

### Returns:


A tuple of closest point information if successful. The list will
contain the following information:
Element     Type             Description
   0        Point3d          The 3-D point at the parameter value of the 
                             closest point.
   1        (U, V)           Parameter values of closest point. Note, V 
                             is 0 if the component index type is brep_edge
                             or brep_vertex. 
   2        (type, index)    The type and index of the brep component that
                             contains the closest point. Possible types are
                             brep_face, brep_edge or brep_vertex.
   3        Vector3d         The normal to the brep_face, or the tangent
                             to the brep_edge.  
None if not successful, or on error.
        
