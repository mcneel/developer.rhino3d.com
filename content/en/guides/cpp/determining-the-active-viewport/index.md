+++
aliases = ["/5/guides/cpp/determining-the-active-viewport/", "/6/guides/cpp/determining-the-active-viewport/", "/7/guides/cpp/determining-the-active-viewport/", "/wip/guides/cpp/determining-the-active-viewport/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to determine the active viewport using C/C++."
keywords = [ "rhino", "viewport" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Determining the Active Viewport"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/activeviewport"
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

You are trying to determine if the current active view is a detail or a standard view.  You are having some trouble differentiating between an active page layout and an active detail in a page layout.

## Solution

Standard Rhino views are represented by the `CRhinoView` class.  Layout views are represented by the `CRhinoPageView` class.  This class is derived from `CRhinoView`.  A `CRhinoPageView` object maintains an array of `CRhinoDetailViewObject` objects - one for each detail in the layout.

To determine whether a layout or one if it's details is active, get the UUID of the layout's active detail object.  If the returned UUID is `nil`, then the layout itself is active.  Otherwise, the detail object that has the returned UUID is active.

## Sample

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoView* view = RhinoApp().ActiveView();
  if (nullptr == view)
    return CRhinoCommand::failure;

  CRhinoPageView* page_view = static_cast<CRhinoPageView*>(view);
  if (page_view)
  {
    ON_wString layout_name = page_view->MainViewport().Name();
    ON_UUID active_detail_uuid = page_view->ActiveDetailObject();
    if (ON_UuidIsNotNil(active_detail_uuid))
    {
      ON_wString detail_name = page_view->ActiveViewport().Name();
      RhinoApp().Print(L"The detail \"%s\" on layout \"%s\" is active.\n", 
        static_cast<const wchar_t*>(detail_name), 
        static_cast<const wchar_t*>(layout_name)
      );
    }
    else
    {
      RhinoApp().Print(L"The layout \"%s\" is active.\n", 
        static_cast<const wchar_t*>(layout_name)
      );
    }
  }
  else
  {
    ON_wString viewport_name = view->ActiveViewport().Name();
    RhinoApp().Print(L"The viewport \"%s\" is active.\n", 
      static_cast<const wchar_t*>(viewport_name)
    );
  }

  return CRhinoCommand::success;
}
```
