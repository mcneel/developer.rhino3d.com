---
layout: bootstrap
---

# GetObjects

Prompts user to pick or select one or more objects.
        

### Parameters:

  message[opt] = a prompt or message.
  filter[opt] = The type(s) of geometry (points, curves, surfaces, meshes,...)
      that can be selected. Object types can be added together to filter
      several different kinds of geometry. use the filter class to get values
  group[opt] = Honor object grouping.  If omitted and the user picks a group,
      the entire group will be picked (True). Note, if filter is set to a
      value other than 0 (All objects), then group selection will be disabled.
  preselect[opt] =  Allow for the selection of pre-selected objects.
  select[opt] = Select the picked objects.  If False, the objects that are
      picked are not selected.
  objects[opt] = list of objects that are allowed to be selected
  mimimum_count, maximum_count[out] = limits on number of objects allowed to be selected
Returns
  list of Guids identifying the picked objects
        


