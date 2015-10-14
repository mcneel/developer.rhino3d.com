---
layout: bootstrap
---

# ObjectColorSource

Returns of modifies the color source of an object.
        Paramters:
          object_ids = single identifier of list of identifiers
          source[opt] = new color source
              0 = color from layer
              1 = color from object
              2 = color from material
              3 = color from parent
        Returns:
          if color source is not specified, the current color source
          is color source is specified, the previous color source
          if color_ids is a list, then the number of objects modifief
        


