---
layout: bootstrap
---

# GetObjectGrips

Prompts user to pick one or more object grips from one or more objects.
        

### Parameters:

message [opt] = prompt for picking
preselect [opt] = allow for selection of pre-selected object grips
select [opt] = select the picked object grips
        

### Returns:


list containing one or more grip records. Each grip record is a tuple
  grip_record[0] = identifier of the object that owns the grip
  grip_record[1] = index value of the grip
  grip_record[2] = location of the grip
None on error
        
