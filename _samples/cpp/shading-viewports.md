---
title: Shading Viewports
description: Demonstrates how to set a viewport to shaded display.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/shadedisplay
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoView* view = RhinoApp().ActiveView();
  if( 0 == view )
    return CRhinoCommand::failure;

  ON::display_mode dm = view->ActiveViewport().DisplayMode();
  if( dm != ON::shaded_display )
  {
    view->ActiveViewport().SetDisplayMode( ON::shaded_display );
    context.m_doc.ViewModified( view );
    view->Redraw();
  }

  return CRhinoCommand::success;
}
```
