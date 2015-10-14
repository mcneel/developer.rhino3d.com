---
layout: bootstrap
---

# AddHatch

Creates a new hatch object from a closed planar curve object
        

### Parameters:

- ***curve_id*** = identifier of the closed planar curve that defines the
    boundary of the hatch object
- ***hatch_pattern[opt]*** = name of the hatch pattern to be used by the hatch
    object. If omitted, the current hatch pattern will be used
- ***scale[opt]*** = hatch pattern scale factor
- ***rotation[opt]*** = hatch pattern rotation angle in degrees.
        

### Returns:


identifier of the newly created hatch on success
None on error
        
