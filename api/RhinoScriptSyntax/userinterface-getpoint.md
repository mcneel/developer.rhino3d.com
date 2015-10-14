---
layout: bootstrap
---

# GetPoint

Pauses for user input of a point.
        

### Parameters:

message [opt] = A prompt or message.
base_point [opt] = list of 3 numbers or Point3d identifying a starting, or base point
distance  [opt] = constraining distance. If distance is specified, basePoint must also
                  be sepcified.
in_plane [opt] = constrains the point selections to the active construction plane.
        

### Returns:


point on success
None if no point picked or user canceled
        
