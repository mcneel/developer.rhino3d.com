---
layout: bootstrap
---

# IsObjectInBox

Verifies an object's bounding box is inside of another bounding box
        

### Parameters:

object_id: String or Guid. The identifier of an object
box: bounding box to test for containment
- ***test_mode[opt]*** = If True, the object's bounding box must be contained by box
  If False, the object's bounding box must be contained by or intersect box
        

### Returns:


True if object is inside box
False is object is not inside box
        
