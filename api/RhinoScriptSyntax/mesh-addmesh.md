---
layout: bootstrap
---

# AddMesh

Add a mesh object to the document
        

### Parameters:

- ***vertices*** = list of 3D points defining the vertices of the mesh
face_- ***vertices*** = list containing lists of 3 or 4 numbers that define the
  vertex indices for each face of the mesh. If the third a fourth vertex
  indices of a face are identical, a triangular face will be created.
- ***vertex_normals[opt]*** = list of 3D vectors defining the vertex normals of
  the mesh. Note, for every vertex, there must be a corresponding vertex
  normal
- ***texture_coordinates[opt]*** = list of 2D texture coordinates. For every
  vertex, there must be a corresponding texture coordinate
- ***vertex_colors[opt]*** = a list of color values. For every vertex,
  there must be a corresponding vertex color
        

### Returns:


Identifier of the new object if successful
None on error
        
