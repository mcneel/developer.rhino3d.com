---
layout: bootstrap
---

# GetPlugInObject

Returns a scriptable object from a specified plug-in. Not all plug-ins
        contain scriptable objects. Check with the manufacturer of your plug-in
        to see if they support this capability.
        

### Parameters:

- ***plug_in*** = name or Id of a registered plug-in that supports scripting.
          If the plug-in is registered but not loaded, it will be loaded
        

### Returns:


scriptable object if successful
None on error
        
