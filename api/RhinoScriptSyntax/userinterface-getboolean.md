---
layout: bootstrap
---

# GetBoolean

Pauses for user input of one or more boolean values. Boolean values are
        displayed as click-able command line option toggles
        

### Parameters:

- ***message*** = a prompt
- ***items*** = list or tuple of options. Each option is a tuple of three strings
  element 1 = description of the boolean value. Must only consist of letters
    and numbers. (no characters like space, period, or dash
  element 2 = string identifying the false value
  element 3 = string identifying the true value
- ***defaults*** = list of boolean values used as default or starting values
        

### Returns:


a list of values that represent the boolean values if successful
None on error
        
