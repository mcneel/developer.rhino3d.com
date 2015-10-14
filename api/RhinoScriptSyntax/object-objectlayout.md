---
layout: bootstrap
---

# ObjectLayout

Returns or changes the layout or model space of an object
        

### Parameters:

- ***object_id*** = identifier of the object
- ***layout[opt]*** = to change, or move, an object from model space to page
  layout space, or from one page layout to another, then specify the
  title or identifier of an existing page layout view. To move an object
  from page layout space to model space, just specify None
- ***return_name[opt]*** = If True, the name, or title, of the page layout view
  is returned. If False, the identifier of the page layout view is returned
        

### Returns:


if layout is not specified, the object's current page layout view
if layout is specfied, the object's previous page layout view
None if not successful
        
