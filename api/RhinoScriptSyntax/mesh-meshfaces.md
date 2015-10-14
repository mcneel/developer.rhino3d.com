---
layout: bootstrap
---

# MeshFaces

Returns face vertices of a mesh
        

### Parameters:

- ***object_id*** = identifier of a mesh object
- ***face_type[opt]*** = The face type to be returned. True = both triangles
  and quads. False = only triangles
        

### Returns:


a list of 3D points that define the face vertices of the mesh. If
face_type is True, then faces are returned as both quads and triangles
(4 3D points). For triangles, the third and fourth vertex will be
identical. If face_type is False, then faces are returned as only
triangles(3 3D points). Quads will be converted to triangles.
        
