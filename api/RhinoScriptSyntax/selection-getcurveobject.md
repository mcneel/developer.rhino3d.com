---
layout: bootstrap
---

# GetCurveObject

Prompts user to pick or select a single curve object
        

### Parameters:

- ***message[opt]*** = a prompt or message.
- ***preselect[opt]*** = Allow for the selection of pre-selected objects.
- ***select[opt]*** = Select the picked objects. If False, objects that
  are picked are not selected.
        

### Returns:


Tuple containing the following information
  element 0 = identifier of the curve object
  element 1 = True if the curve was preselected, otherwise False
  element 2 = selection method (see help)
  element 3 = selection point
  element 4 = the curve parameter of the selection point
  element 5 = name of the view selection was made
None if no object picked
        
