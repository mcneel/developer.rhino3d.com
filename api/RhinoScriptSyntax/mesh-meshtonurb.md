---
layout: bootstrap
---

# MeshToNurb

Duplicates each polygon in a mesh with a NURBS surface. The resulting
        surfaces are then joined into a polysurface and added to the document
        

### Parameters:

- ***object_id*** = identifier of a mesh object
- ***trimmed_triangles[opt]*** = if True, triangles in the mesh will be
  represented by a trimmed plane
- ***delete_input[opt]*** = delete input object
        

### Returns:


list of identifiers for the new breps on success
        
