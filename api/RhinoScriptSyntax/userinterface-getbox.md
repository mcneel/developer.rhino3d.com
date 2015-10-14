---
layout: bootstrap
---

# GetBox

Pauses for user input of a box
        

### Parameters:

- ***mode[opt]*** = The box selection mode.
   0 = All modes
   1 = Corner. The base rectangle is created by picking two corner points
   2 = 3-Point. The base rectangle is created by picking three points
   3 = Vertical. The base vertical rectangle is created by picking three points.
   4 = Center. The base rectangle is created by picking a center point and a corner point
- ***base_point[opt]*** = optional 3D base point
prompt1, prompt2, prompt3 [opt] = optional prompts to set
        

### Returns:


list of eight Point3d that define the corners of the box on success
None is not successful, or on error
        
