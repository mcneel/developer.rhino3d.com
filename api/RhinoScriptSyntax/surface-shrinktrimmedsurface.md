---
layout: bootstrap
---

# ShrinkTrimmedSurface

Shrinks the underlying untrimmed surfaces near to the trimming
        boundaries. See the ShrinkTrimmedSrf command in the Rhino help.
        

### Parameters:

- ***object_id*** = the surface's identifier
- ***create_copy[opt]*** = If True, the original surface is not deleted
        

### Returns:


If create_copy is False, True or False indifating success or failure
If create_copy is True, the identifier of the new surface
None on error
        
