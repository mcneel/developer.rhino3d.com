---
layout: bootstrap
---

# DocumentModified

Returns or sets the document's modified flag. This flag indicates whether
        or not any changes to the current document have been made. NOTE: setting the
        document modified flag to False will prevent the "Do you want to save this
        file..." from displaying when you close Rhino.
        

### Parameters:

modified [optional] = the modified state, either True or False
        

### Returns:


if no modified state is specified, the current modified state
if a modified state is specified, the previous modified state
        
