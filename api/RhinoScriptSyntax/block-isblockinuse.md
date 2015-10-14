---
layout: bootstrap
---

# IsBlockInUse

Verifies that a block definition is being used by an inserted instance
        

### Parameters:

- ***block_name*** = name of an existing block definition
where_to_look [opt] = One of the following values
     0 = Check for top level references in active document
     1 = Check for top level and nested references in active document
     2 = Check for references in other instance definitions
        

### Returns:


True or False
        
