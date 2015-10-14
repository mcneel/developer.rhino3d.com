---
layout: bootstrap
---

# UnitAbsoluteTolerance

Resturns or sets the document's absolute tolerance. Absolute tolerance
        is measured in drawing units. See Rhino's document properties command
        (Units and Page Units Window) for details
        

### Parameters:

tolerance [opt] = the absolute tolerance to set
- ***in_model_units[opt]*** = Return or modify the document's model units (True)
                      or the document's page units (False)
        

### Returns:


if tolerance is not specified, the current absolute tolerance
if tolerance is specified, the previous absolute tolerance
        
