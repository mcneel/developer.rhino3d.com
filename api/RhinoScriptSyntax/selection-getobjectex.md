---
layout: bootstrap
---

# GetObjectEx

Prompts user to pick, or select a single object
        

### Parameters:

- ***message[opt]*** = a prompt or message.
- ***filter[opt]*** = The type(s) of geometry (points, curves, surfaces, meshes,...)
    that can be selected. Object types can be added together to filter
    several different kinds of geometry. use the filter class to get values
- ***preselect[opt]*** =  Allow for the selection of pre-selected objects.
- ***select[opt]*** = Select the picked objects.  If False, the objects that are
    picked are not selected.
- ***objects[opt]*** = list of object identifiers specifying objects that are
    allowed to be selected
        

### Returns:


Tuple of information containing the following information
  element 0 = identifier of the object
  element 1 = True if the object was preselected, otherwise False
  element 2 = selection method (see help)
  element 3 = selection point
  element 4 = name of the view selection was made
None if no object selected
        
