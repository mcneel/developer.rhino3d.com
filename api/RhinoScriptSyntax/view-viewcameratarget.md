---
layout: bootstrap
---

# ViewCameraTarget

Returns or sets the camera and target positions of the specified view
        

### Parameters:

view:[opt] title or id of the view. If omitted, current active view is used
camera:[opt] 3d point identifying the new camera location. If camera and
   target are not specified, current camera and target locations are returned
target:[opt] 3d point identifying the new target location. If camera and
   target are not specified, current camera and target locations are returned
        

### Returns:


if both camera and target are not specified, then the 3d points containing
  the current camera and target locations is returned
if either camera or target are specified, then the 3d points containing the
  previous camera and target locations is returned
        
