---
layout: bootstrap
---

# AddHatches

Creates one or more new hatch objects a list of closed planar curves
        

### Parameters:

- ***curve_ids*** = identifiers of the closed planar curves that defines the
    boundary of the hatch objects
- ***hatch_pattern[opt]*** = name of the hatch pattern to be used by the hatch
    object. If omitted, the current hatch pattern will be used
- ***scale[opt]*** = hatch pattern scale factor
- ***rotation[opt]*** = hatch pattern rotation angle in degrees.
        

### Returns:


identifiers of the newly created hatch on success
None on error
        
