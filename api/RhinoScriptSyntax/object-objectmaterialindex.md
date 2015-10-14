---
layout: bootstrap
---

# ObjectMaterialIndex

Returns or changes the material index of an object. Rendering materials are stored in
        Rhino's rendering material table. The table is conceptually an array. Render
        materials associated with objects and layers are specified by zero based
        indices into this array.
        

### Parameters:

- ***object_id*** = identifier of an object
- ***index*** = optional. the new material index
        

### Returns:


If the return value of ObjectMaterialSource is "material by object", then
the return value of this function is the index of the object's rendering
material. A material index of -1 indicates no material has been assigned,
and that Rhino's internal default material has been assigned to the object.
None on failure      
        
