---
layout: bootstrap
---

# UnitAngleTolerance

Return or set the document's angle tolerance. Angle tolerance is
        measured in degrees. See Rhino's DocumentProperties command
        (Units and Page Units Window) for details
        

### Parameters:

angle_tolerance_degrees [opt] = the angle tolerance to set
in_model_units [opt] = Return or modify the document's model units (True)
                       or the document's page units (False)
        

### Returns:


if angle_tolerance_degrees is not specified, the current angle tolerance
if angle_tolerance_degrees is specified, the previous angle tolerance
        
