---
layout: bootstrap
---

# CurveDirectionsMatch

Tests if two curve objects are generally in the same direction or if they
        would be more in the same direction if one of them were flipped. When testing
        curve directions, both curves must be either open or closed - you cannot test
        one open curve and one closed curve.
        

### Parameters:

- ***curve_id_0*** = identifier of first curve object
- ***curve_id_1*** = identifier of second curve object
        

### Returns:


True if the curve directions match, otherwise False. 
        
