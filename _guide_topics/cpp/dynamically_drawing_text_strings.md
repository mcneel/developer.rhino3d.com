---
title: Dynamically Drawing Text Strings
description: This guide demonstrates how to dynamically draw text strings using C/C++.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/drawstring
order: 1
keywords: ['rhino', 'text']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

On occasion, it is useful to dynamically display some text while in the middle of a point picking operation.  Rhino's `VariableFilletSrf` command is a good example of a command that does this.

To add this capability to an plugin command, you need to:

1. Derive a new class from `CRhinoGetPoint`.
1. Override the `CRhinoGetPoint::DynamicDraw` virtual function.
1. From within the `DynamicDraw` override, call `CRhinoViewport::DrawString`.

## Sample

The following example code demonstrates how to derive a new class from `CRhinoGetPoint`, override the `CRhinoGetPoint::DynamicDraw` member, and draw text dynamically.

```cpp
class CDrawStringGetPoint : public CRhinoGetPoint
{
public:
  CDrawStringGetPoint() {}
  void DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt );
};

void CDrawStringGetPoint::DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt )
{
  // Format active point as a string
  ON_wString str;
  RhinoFormatPoint( pt, str );

  // Build world-to-screen coordinate transformation
  ON_Xform w2s;
  vp.VP().GetXform( ON::world_cs, ON::screen_cs, w2s );

  // Transform point from world to screen coordinates
  ON_3dPoint screenpoint = w2s * pt;

  // Offset point so text does not overlap cursor
  screenpoint.x += 5.0;
  screenpoint.y += -5.0;

  // Draw string using the system font
  vp.DrawString( str, str.Length(), screenpoint, false, 0, 12, L"System" );

  // Allow base class to draw
  CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
}
```

You can use the above class as you would a `CRhinoGetPoint` object.  Just create a new `CDrawStringGetPoint` object, initialize the class by calling base class members, and call it's `GetPoint` member.  For example:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CDrawStringGetPoint gp;
  gp.SetCommandPrompt( L"Pick test point" );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  // TODO...

  return success;
}
```
