---
layout: bootstrap
---

# IsObjectInGroup

Verifies that an object is a member of a group
        

### Parameters:

object_id: The identifier of an object
group_name[opt]: The name of a group. If omitted, the function
  verifies that the object is a member of any group
        

### Returns:


True if the object is a member of the specified group. If a group_name
  was not specified, the object is a member of some group.
False if the object is not a member of the specified group. If a
  group_name was not specified, the object is not a member of any group
        
