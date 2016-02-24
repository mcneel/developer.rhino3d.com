---
title: Highlighting Objects in Conduits
description: This guide demonstrates how to highlight objects in a conduit using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/highlightconduitobject
order: 1
keywords: ['rhino', 'display', 'conduit']
layout: toc-guide-page
---

# Highlighting Objects in Conduits

{{ page.description }}

## Problem

You need to highlight a curve object on display conduit.

## Solution

Consider the following sample `CRhinoDisplayConduit` derived class:

```cpp
class CTestHighlightCurveConduit : public CRhinoDisplayConduit
{
public:
  CTestHighlightCurveConduit();

  bool ExecConduit(
    CRhinoDisplayPipeline& dp,
    UINT nChannel,
    bool& bTerminate
    );

public:
  unsigned int m_runtime_object_serial_number;
};

CTestHighlightCurveConduit::CTestHighlightCurveConduit()
: CRhinoDisplayConduit( CSupportChannels::SC_DRAWOBJECT )
{
  // TODO: initialize members here
}

bool CTestHighlightCurveConduit::ExecConduit(
    CRhinoDisplayPipeline& dp,
    UINT nChannel,
    bool& bTerminate
    )
{
  switch( nChannel )
  {
  case CSupportChannels::SC_DRAWOBJECT:
    {
      if( m_pChannelAttrs->m_pObject->m_runtime_object_serial_number == m_runtime_object_serial_number )
        m_pDisplayAttrs->m_ObjectColor = RGB(255, 105, 180); // hot pink
    }
    break;
  }

  return true;
}
```

During the `SC_DRAWOBJECT` channel, the code looks for the target object.  If found, it overrides the object's drawing color.

To use this conduit, you could write a command such as this:

```cpp
CRhinoCommand::result CCommandTestHighlightCurve::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve to highlight" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObject* obj = go.Object(0).Object();
  if( 0 == obj )
    return CRhinoCommand::failure;

  CTestHighlightCurveConduit conduit;
  conduit.m_runtime_object_serial_number = obj->m_runtime_object_serial_number;
  conduit.Enable();
  context.m_doc.Redraw();

  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Press <Enter> to continue" );
  gs.GetString();

  conduit.Disable();
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
