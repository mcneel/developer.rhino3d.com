---
layout: bootstrap
---

# ObjectLinetype

Returns of modifies the linetype of an object
        

### Parameters:

- ***object_ids*** = identifiers of object(s)
- ***linetype[opt]*** = name of an existing linetype. If omitted, the current
  linetype is returned. If object_ids is a list of identifiers, this parameter
  is required
        

### Returns:


If a linetype is not specified, the object's current linetype
If linetype is specified, the object's previous linetype
If object_ids is a list, the number of objects modified
        
