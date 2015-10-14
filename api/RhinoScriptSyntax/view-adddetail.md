---
layout: bootstrap
---

# AddDetail

Add new detail view to an existing layout view
        

### Parameters:

- ***layout_id*** = identifier of an existing layout
corner1, corner2 = 2d corners of the detail in the layout's unit system
- ***title[opt]*** = title of the new detail
- ***projection[opt]*** = type of initial view projection for the detail
    1 = parallel top view
    2 = parallel bottom view
    3 = parallel left view
    4 = parallel right view
    5 = parallel front view
    6 = parallel back view
    7 = perspective view
        

### Returns:


identifier of the newly created detial on success
None on error
        
