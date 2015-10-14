---
layout: bootstrap
---

# GetObject

Prompts user to pick, or select, a single object.
        

### Parameters:

- ***message[opt]*** = a prompt or message.
- ***filter[opt]*** = The type(s) of geometry (points, curves, surfaces, meshes,...)
    that can be selected. Object types can be added together to filter
    several different kinds of geometry. use the filter class to get values
- ***preselect[opt]*** =  Allow for the selection of pre-selected objects.
- ***select[opt]*** = Select the picked objects.  If False, the objects that are
    picked are not selected.
- ***subobjects[opt]*** = If True, subobjects can be selected. When this is the
    case, an ObjRef is returned instead of a Guid to allow for tracking
    of the subobject when passed into other functions
        

### Returns:


Identifier of the picked object
None if user did not pick an object
        
