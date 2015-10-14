---
layout: bootstrap
---

# ExplodeMeshes

Explodes a mesh object, or mesh objects int submeshes. A submesh is a
        collection of mesh faces that are contained within a closed loop of
        unwelded mesh edges. Unwelded mesh edges are where the mesh faces that
        share the edge have unique mesh vertices (not mesh topology vertices)
        at both ends of the edge
        

### Parameters:

- ***mesh_ids*** = list of mesh identifiers
- ***delete[opt]*** = delete the input meshes
        

### Returns:


List of identifiers
        
