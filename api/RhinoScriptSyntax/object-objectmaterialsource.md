---
layout: bootstrap
---

# ObjectMaterialSource

Returns or modifies the rendering material source of an object.
        

### Parameters:

- ***object_ids*** = one or more object identifiers
source [opt] = The new rendering material source. If omitted and a single
  object is provided in object_ids, then the current material source is
  returned. This parameter is required if multiple objects are passed in
  object_ids
  0 = Material from layer
  1 = Material from object
  3 = Material from parent
        

### Returns:


If source is not specified, the current rendering material source
If source is specified, the previous rendering material source
If object_ids refers to multiple objects, the number of objects modified
        
