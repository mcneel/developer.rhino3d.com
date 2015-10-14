---
layout: bootstrap
---

# DeleteLayer

Removes an existing layer from the document. The layer to be removed
        cannot be the current layer. Unlike the PurgeLayer method, the layer must
        be empty, or contain no objects, before it can be removed. Any layers that
        are children of the specified layer will also be removed if they are also
        empty.
        

### Parameters:

- ***layer*** = the name or id of an existing empty layer
        

### Returns:


True or False indicating success or failure
        
