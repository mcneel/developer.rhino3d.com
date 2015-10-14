---
layout: bootstrap
---

# UnitRelativeTolerance

Return or set the document's relative tolerance. Relative tolerance
        is measured in percent. See Rhino's DocumentProperties command
        (Units and Page Units Window) for details
        

### Parameters:

relative_tolerance [opt] = the relative tolerance in percent
in_model_units [opt] = Return or modify the document's model units (True)
                       or the document's page units (False)
        

### Returns:


if relative_tolerance is not specified, the current tolerance in percent
if relative_tolerance is specified, the previous tolerance in percent
        
