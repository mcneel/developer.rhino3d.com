---
layout: bootstrap
---

# GetRectangle

Pauses for user input of a rectangle
        

### Parameters:

- ***mode[opt]*** = The rectangle selection mode. The modes are as follows
    0 = All modes
    1 = Corner - a rectangle is created by picking two corner points
    2 = 3Point - a rectangle is created by picking three points
    3 = Vertical - a vertical rectangle is created by picking three points
    4 = Center - a rectangle is created by picking a center point and a corner point
- ***base_point[opt]*** = a 3d base point
prompt1, prompt2, prompt3 = optional prompts
        

### Returns:


a tuple of four 3d points that define the corners of the rectangle
None on error
        
