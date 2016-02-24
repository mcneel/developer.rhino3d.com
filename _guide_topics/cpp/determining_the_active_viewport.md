---
title: Determining the Active Viewport
description: This guide demonstrates how to determine the active viewport using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/activeviewport
order: 1
keywords: ['rhino', 'viewport']
layout: toc-guide-page
---

# Determining the Active Viewport

{{ page.description }}

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
  if( 0 == view )
    return CRhinoCommand::failure;

  if( view->IsKindOf(RUNTIME_CLASS(CRhinoPageView)) )
  {
    CRhinoPageView* page_view = static_cast<CRhinoPageView*>(view);
    if( page_view )
    {
      ON_wString layout_name = page_view->MainViewport().Name();

      ON_UUID active_detail_uuid = page_view->ActiveDetailObject();
      if( ON_UuidIsNotNil(active_detail_uuid) )
      {
        ON_wString detail_name = page_view->ActiveViewport().Name();
        RhinoApp().Print( L"The detail \"%s\" on layout \"%s\" is active.\n", detail_name, layout_name );
      }
      else
      {
        RhinoApp().Print( L"The layout \"%s\" is active.\n", layout_name );
      }
    }
  }
  else
  {
    ON_wString viewport_name = view->ActiveViewport().Name();
    RhinoApp().Print( L"The viewport \"%s\" is active.\n", viewport_name );
  }

  return CRhinoCommand::success;
}
```
