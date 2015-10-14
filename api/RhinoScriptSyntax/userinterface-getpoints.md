---
layout: bootstrap
---

# GetPoints

Pauses for user input of one or more points
        

### Parameters:

draw_lines [opt] = Draw lines between points
- ***in_plane[opt]*** = Constrain point selection to the active construction plane
- ***message1[opt]*** = A prompt or message for the first point
- ***message2[opt]*** = A prompt or message for the next points
- ***max_points[opt]*** = maximum number of points to pick. If not specified, an
                  unlimited number of points can be picked.
- ***base_point[opt]*** = a starting or base point
        

### Returns:


list of 3d points if successful
None if not successful or on error
        
