---
layout: bootstrap
---

# GetMeshVertices

Prompts the user to pick one or more mesh vertices
        

### Parameters:

- ***object_id*** = the mesh object's identifier
- ***message[opt]*** = a prompt of message
- ***min_count[opt]*** = the minimum number of vertices to select
- ***max_count[opt]*** = the maximum number of vertices to select. If 0, the user must
  press enter to finish selection. If -1, selection stops as soon as there
  are at least min_count vertices selected.
        

### Returns:


list of mesh vertex indices on success
None on error
        
