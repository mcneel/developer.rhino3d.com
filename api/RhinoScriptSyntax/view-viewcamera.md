---
layout: bootstrap
---

# ViewCamera

Returns or sets the camera location of the specified view
        

### Parameters:

view:[opt] title or id of the view. If omitted, the current active view is used
camera_location: [opt] a 3D point identifying the new camera location.
  If omitted, the current camera location is returned
        

### Returns:


If camera_location is not specified, the current camera location
If camera_location is specified, the previous camera location
None on error    
        
