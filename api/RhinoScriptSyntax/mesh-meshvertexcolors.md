---
layout: bootstrap
---

# MeshVertexColors

Returns of modifies vertex colors of a mesh
        

### Parameters:

- ***mesh_id*** = identifier of a mesh object
- ***colors[opt]*** = A list of color values. Note, for each vertex, there must
  be a corresponding vertex color. If the value is None, then any
  existing vertex colors will be removed from the mesh
        

### Returns:


if colors is not specified, the current vertex colors
if colors is specified, the previous vertex colors
        
