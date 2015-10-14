---
layout: bootstrap
---

# AddText

Adds a text string to the document
        

### Parameters:

- ***text*** = the text to display
- ***point_or_plane*** = a 3-D point or the plane on which the text will lie.
    The origin of the plane will be the origin point of the text
height [opt] = the text height
font [opt] = the text font
- ***font_style[opt]*** = any of the following flags
   0 = normal
   1 = bold
   2 = italic
   3 = bold and italic
- ***justification[opt]*** = text justification (see help for values)
        

### Returns:


Guid for the object that was added to the doc on success
None on failure
        
