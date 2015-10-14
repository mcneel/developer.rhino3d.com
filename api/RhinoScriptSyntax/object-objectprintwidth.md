---
layout: bootstrap
---

# ObjectPrintWidth

Returns or modifies the print width of an object
        

### Parameters:

- ***object_ids*** = identifiers of object(s)
- ***width[opt]*** = new print width value in millimeters, where width=0 means use
  the default width, and width<0 means do not print (visible for screen display,
  but does not show on print). If omitted, the current width is returned.
        

### Returns:


If width is not specified, the object's current print width
If width is specified, the object's previous print width
If object_ids is a list or tuple, the number of objects modified
        
