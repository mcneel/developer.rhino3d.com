---
layout: bootstrap
---

# ObjectPrintWidthSource

Returns or modifies the print width source of an object
        

### Parameters:

- ***object_ids*** = identifiers of object(s)
- ***source[opt]*** = new print width source
  0 = print width by layer
  1 = print width by object
  3 = print width by parent
        

### Returns:


If source is not specified, the object's current print width source
If source is specified, the object's previous print width source
If object_ids is a list or tuple, the number of objects modified
        
