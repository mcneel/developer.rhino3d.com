---
layout: bootstrap
---

# ObjectColor

Returns of modifies the color of an object. Object colors are represented
        as RGB colors. An RGB color specifies the relative intensity of red, green,
        and blue to cause a specific color to be displayed
        

### Parameters:

- ***object_ids*** = id or ids of object(s)
- ***color[opt]*** = the new color value. If omitted, then current object
    color is returned. If object_ids is a list, color is required
        

### Returns:


If color value is not specified, the current color value
If color value is specified, the previous color value
If object_ids is a list, then the number of objects modified
        
