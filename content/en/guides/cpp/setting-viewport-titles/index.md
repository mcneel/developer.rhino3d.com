+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to set the title of a viewport using C/C++."
keywords = [ "rhino", "viewport" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Setting Viewport Titles"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/setviewname"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

You would like to change the name, or title, or a viewport using the the Rhino C/C++ SDK.  For example, you would like to rename the "Front" viewport to say "Facade."

## Solution

To change the title of a viewport, use `CRhinoViewport::SetName`.  A Rhino view contains a "main viewport" that fills the entire view client window.  To get a view's main viewport, you can call `CRhinoView::MainViewport`.

For example:

```cpp
CRhinoView* view = RhinoApp().ActiveView();
if (view)
  view->MainViewport().SetName("Facade");
```
