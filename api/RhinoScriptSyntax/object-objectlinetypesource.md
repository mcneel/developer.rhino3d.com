---
layout: bootstrap
---

# ObjectLinetypeSource

Returns of modifies the linetype source of an object
        

### Parameters:

- ***object_ids*** = identifiers of object(s)
- ***source[opt]*** = new linetype source. If omitted, the current source is returned.
  If object_ids is a list of identifiers, this parameter is required
    0 = By Layer
    1 = By Object
    3 = By Parent
        

### Returns:


If a source is not specified, the object's current linetype source
If source is specified, the object's previous linetype source
If object_ids is a list, the number of objects modified
        
