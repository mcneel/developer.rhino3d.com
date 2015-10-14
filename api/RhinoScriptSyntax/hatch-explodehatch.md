---
layout: bootstrap
---

# ExplodeHatch

Explodes a hatch object into its component objects. The exploded objects
        will be added to the document. If the hatch object uses a solid pattern,
        then planar face Brep objects will be created. Otherwise, line curve objects
        will be created
        

### Parameters:

- ***hatch_id*** = identifier of a hatch object
- ***delete[opt]*** = delete the hatch object
        

### Returns:


list of identifiers for the newly created objects
None on error
        
