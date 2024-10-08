+++
aliases = ["/en/5/samples/rhinopython/sticky-values/", "/en/6/samples/rhinopython/sticky-values/", "/en/7/samples/rhinopython/sticky-values/", "/en/wip/samples/rhinopython/sticky-values/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "This module contains a standard python dictionary called sticky which sticks around."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Sticky Values"
type = "samples/python"
weight = 14

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++


```python
import rhinoscriptsyntax as rs
import scriptcontext


stickyval = 0
# restore stickyval if it has been saved
if scriptcontext.sticky.has_key("my_key"):
    stickyval = scriptcontext.sticky["my_key"]
nonstickyval = 12

print "sticky =", stickyval
print "nonsticky =", nonstickyval

val = rs.GetInteger("give me an integer")
if val:
    stickyval = val
    nonstickyval = val

# save the value for use in the future
scriptcontext.sticky["my_key"] = stickyval
```

The `scriptcontext` module contains a standard python dictionary called sticky which "sticks" around during the running of Rhino.  This dictionary can be used to save settings between execution of your scripts and then get at those saved settings the next time you run your script or from a completely different script.
