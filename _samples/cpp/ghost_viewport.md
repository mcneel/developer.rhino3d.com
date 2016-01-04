---
title: Ghost Viewport
description: Demonstrates how to set a viewport to ghosted display.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/ghostedshade
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
