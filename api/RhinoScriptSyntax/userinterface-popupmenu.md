---
layout: bootstrap
---

# PopupMenu

Display a context-style popup menu. The popup menu can appear almost
        anywhere, and can be dismissed by clicking the left or right mouse buttons
        

### Parameters:

- ***items*** = list of strings representing the menu items. An empty string or None
  will create a separator
- ***modes[opt]*** = List of numbers identifying the display modes. If omitted, all
  modes are enabled.
    0 = menu item is enabled
    1 = menu item is disabled
    2 = menu item is checked
    3 = menu item is disabled and checked
- ***point[opt]*** = a 3D point where the menu item will appear. If omitted, the menu
  will appear at the current cursor position
- ***view[opt]*** = if point is specified, the view in which the point is computed.
  If omitted, the active view is used
        

### Returns:


index of the menu item picked or -1 if no menu item was picked
        
