---
layout: bootstrap
---

# GetSurfaceObject

Prompts the user to select a single surface
        

### Parameters:

- ***message[opt]*** = prompt displayed
- ***preselect[opt]*** = allow for preselected objects
- ***select[opt]*** = select the picked object
        

### Returns:


tuple of information on success
  element 0 = identifier of the surface
  element 1 = True if the surface was preselected, otherwise False
  element 2 = selection method ( see help )
  element 3 = selection point
  element 4 = u,v surface parameter of the selection point
  element 5 = name of the view in which the selection was made
None on error
        
