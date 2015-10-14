---
layout: bootstrap
---

# IsCurveClosable

Decide if it makes sense to close off the curve by moving the end point
        to the start point based on start-end gap size and length of curve as
        approximated by chord defined by 6 points
        

### Parameters:

- ***curve_id*** = identifier of the curve object
- ***tolerance[opt]*** = maximum allowable distance between start point and end
  point. If omitted, the document's current absolute tolerance is used
        

### Returns:


True or False
        
