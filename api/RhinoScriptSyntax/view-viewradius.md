---
layout: bootstrap
---

# ViewRadius

Returns or sets the radius of a parallel-projected view. Useful
        when you need an absolute zoom factor for a parallel-projected view
        

### Parameters:

view:[opt] title or id of the view. If omitted, current active view is used
radius:[opt] the view radius
mode: [opt] perform a "dolly" magnification by moving the camera 
  towards/away from the target so that the amount of the screen 
  subtended by an object changes.  true = perform a "zoom" 
  magnification by adjusting the "lens" angle
        

### Returns:


if radius is not specified, the current view radius for the specified view
if radius is specified, the previous view radius for the specified view
        
