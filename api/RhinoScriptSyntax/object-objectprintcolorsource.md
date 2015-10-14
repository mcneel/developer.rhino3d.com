---
layout: bootstrap
---

# ObjectPrintColorSource

Returns or modifies the print color source of an object
        

### Parameters:

- ***object_ids*** = identifiers of object(s)
- ***source[opt]*** = new print color source
  0 = print color by layer
  1 = print color by object
  3 = print color by parent
        

### Returns:


If source is not specified, the object's current print color source
If source is specified, the object's previous print color source
If object_ids is a list or tuple, the number of objects modified
        
