---
title: Enabling Orthogonal Mode
description: This brief guide demonstrates how to enable Rhino's orthogonal mode using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/ortho
order: 1
keywords: ['rhino', 'orthogonal']
layout: toc-guide-page
---

 
## Problem

You are trying to draw a line and you need ortho enabled.

## Solution

The state of Rhino's orthogonal drawing mode is stored in Rhino's application settings, or it's `CRhinoAppSettings` object.  To check the current state of ortho, call `CRhinoAppSettings::Ortho`.  To enable or disable ortho, call `CRhinoAppSettings::EnableOrtho` and pass in the boolean value that is appropriate.  For more information on this and Rhino's application settings class, see *rhinoSdkAppSettings.h*.

## Sample

The following sample code illustrates how to use this feature:

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetPoint gp;
  gp.SetCommandPrompt(L"Starting point");
  gp.GetPoint();
  if (gp.CommandResult() != success)
    return gp.CommandResult();

  ON_3dPoint start_point = gp.Point();

  CRhinoAppSettings& settings = RhinoApp().AppSettings();
  bool bOldValue = settings.Ortho();
  if (bOldValue == false)
    settings.EnableOrtho(true);

  gp.SetCommandPrompt(L"Ending point");
  gp.SetBasePoint(start_point);
  gp.DrawLineFromPoint(start_point, true);
  gp.GetPoint();

  if (bOldValue != settings.Ortho())
    settings.EnableOrtho(bOldValue);

  if (gp.CommandResult() != success)
    return gp.CommandResult();

  ON_3dPoint end_point = gp.Point();

  ON_Line line(start_point, end_point);
  context.m_doc.AddCurveObject(line);
  context.m_doc.Redraw();

  return success;
}
```
