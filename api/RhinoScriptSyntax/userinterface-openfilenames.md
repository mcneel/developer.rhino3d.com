---
layout: bootstrap
---

# OpenFileNames

Displays file open dialog box allowing the user to select one or more file names.
        Note, this function does not open the file.
        

### Parameters:

- ***title[opt]*** = A dialog box title.
- ***filter[opt]*** = A filter string. The filter must be in the following form:
  "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.
  If omitted, the filter (*.*) is used.
- ***folder[opt]*** = A default folder.
- ***filename[opt]*** = a default file name
- ***extension[opt]*** = a default file extension
        

### Returns:


list of selected file names
        
