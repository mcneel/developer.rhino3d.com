---
layout: bootstrap
---

# FitCurve

Reduces number of curve control points while maintaining the curve's same
        general shape. Use this function for replacing curves with many control
        points. For more information, see the Rhino help for the FitCrv command.
        

### Parameters:

- ***curve_id*** = Identifier of the curve object
degree [opt] = The curve degree, which must be greater than 1.
               The default is 3.
distance_tolerance [opt] = The fitting tolerance. If distance_tolerance
    is not specified or <= 0.0, the document absolute tolerance is used.
angle_tolerance [opt] = The kink smoothing tolerance in degrees. If
    angle_tolerance is 0.0, all kinks are smoothed. If angle_tolerance
    is > 0.0, kinks smaller than angle_tolerance are smoothed. If
    angle_tolerance is not specified or < 0.0, the document angle
    tolerance is used for the kink smoothing.
        

### Returns:


The identifier of the new object
None if not successful, or on error.
        
