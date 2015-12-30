---
layout: code-sample-cpp
title: Ghost Viewport
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/ghostedshade
description: Demonstrates how to set a viewport to ghosted display.
order: 1
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoView* view = RhinoApp().ActiveView();
  if( 0 == view )
    return CRhinoCommand::failure;

  CRhinoViewport& vp = view->ActiveViewport();

  const CDisplayPipelineAttributes* pStdAttrs = CRhinoDisplayAttrsMgr::StdGhostedAttrs();
  if( pStdAttrs )
  {
    vp.SetDisplayMode( pStdAttrs->Id() );
    view->Redraw();
  }

  return CRhinoCommand::success;
}
```
