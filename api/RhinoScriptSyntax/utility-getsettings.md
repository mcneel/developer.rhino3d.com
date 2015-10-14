---
layout: bootstrap
---

# GetSettings

Returns string from a specified section in a initialization file.
        

### Parameters:

- ***filename*** = name of the initialization file
- ***section[opt]*** = section containing the entry
- ***entry[opt]*** = entry whose associated string is to be returned
        

### Returns:


If section is not specified, a list containing all section names
If entry is not specified, a list containing all entry names for a given section
If section and entry are specied, a value for entry
None if not successful
        
