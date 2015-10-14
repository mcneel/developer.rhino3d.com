---
layout: bootstrap
---

# ColorAdjustLuma

Change the luminance of a red-green-blue value. Hue and saturation are
        not affected
        

### Parameters:

- ***rgb*** = initial rgb value
- ***luma*** = The luminance in units of 0.1 percent of the total range. A
    value of - ***luma*** = 50 corresponds to 5 percent of the maximum luminance
- ***scale[opt]*** = if True, luma specifies how much to increment or decrement the
    current luminance. If False, luma specified the absolute luminance.
        

### Returns:


modified rgb value if successful
        
