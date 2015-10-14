---
layout: bootstrap
---

# ParentLayer

Return or modify the parent layer of a layer
        

### Parameters:

- ***layer*** = name of an existing layer
- ***parent[opt]*** = name of new parent layer. To remove the parent layer,
  thus making a root-level layer, specify an empty string
        

### Returns:


If parent is not specified, the name of the current parent layer
If parent is specified, the name of the previous parent layer
None if the layer does not have a parent
        
