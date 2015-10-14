---
layout: bootstrap
---

# ObjectGripLocation

Returns or modifies the location of an object's grip
        

### Parameters:

- ***object_id*** = identifier of the object
- ***index*** = index of the grip to either query or modify
point [opt] = 3D point defining new location of the grip
        

### Returns:


if point is not specified, the current location of the grip referenced by index
if point is specified, the previous location of the grip referenced by index
None on error
        
