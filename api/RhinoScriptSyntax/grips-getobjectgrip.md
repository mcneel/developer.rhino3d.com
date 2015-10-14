---
layout: bootstrap
---

# GetObjectGrip

Prompts the user to pick a single object grip
        

### Parameters:

message [opt] = prompt for picking
preselect [opt] = allow for selection of pre-selected object grip.
select [opt] = select the picked object grip.
        

### Returns:


tuple defining a grip record.
  grip_record[0] = identifier of the object that owns the grip
  grip_record[1] = index value of the grip
  grip_record[2] = location of the grip
None on error
        
