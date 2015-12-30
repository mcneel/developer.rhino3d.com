---
layout: code-sample-cpp
title: Shading Viewports
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/shadedisplay
description: Demonstrates how to set a viewport to shaded display.
order: 1
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
