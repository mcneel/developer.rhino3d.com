---
layout: bootstrap
---

# MeshNakedEdgePoints

Identifies the naked edge points of a mesh object. This function shows
        where mesh vertices are not completely surrounded by faces. Joined
        meshes, such as are made by MeshBox, have naked mesh edge points where
        the sub-meshes are joined
        

### Parameters:

- ***object_id*** = identifier of a mesh object
        

### Returns:


List of boolean values that represent whether or not a mesh vertex is
naked or not. The number of elements in the list will be equal to
the value returned by MeshVertexCount. In which case, the list will
identify the naked status for each vertex returned by MeshVertices
None on error
        
