---
layout: bootstrap
---

# CurrentView

Returns or sets the currently active view
        

### Parameters:

view:[opt] String or Guid. Title or id of the view to set current.
  If omitted, only the title or identifier of the current view is returned
return_name:[opt] If True, then the name, or title, of the view is returned.
  If False, then the identifier of the view is returned
        

### Returns:


if the title is not specified, the title or id of the current view
if the title is specified, the title or id of the previous current view
None on error
        
