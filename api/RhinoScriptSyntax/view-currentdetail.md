---
layout: bootstrap
---

# CurrentDetail

Returns or changes the current detail view in a page layout view
        

### Parameters:

- ***layout*** = title or identifier of an existing page layout view
- ***detail[opt]*** = title or identifier the the detail view to set
- ***return_name[opt]*** = return title if True, else return identifier
        

### Returns:


if detail is not specified, the title or id of the current detail view
if detail is specified, the title or id of the previous detail view
None on error
        
