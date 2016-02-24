---
title: Drawing Arrowheads in Display Conduits
description: This guide discusses and demonstrates how to draw arrowheads in Rhino Display Conduit.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/conduitarrowheads
order: 1
keywords: ['rhino', 'display', 'conduit', 'arrowheads']
layout: toc-guide-page
---

# Drawing Arrowheads in Display Conduits

{{ page.description }}

## Problem

You are trying to get your head around drawing arrowheads through conduits in the Rhino C/C++ SDK.  You create an instance of the `CRhinoArrowhead` class and set 2D information (point and direction) and then need to set a parent (any type of `CRhinoAnnotationObject`).  As `CRhinoAnnotationObject` is a virtual class, for your purposes the best version seems to be the leader class.  But (not surprisingly) the arrowhead behaves like a leader, sitting in world space, and is not aligned or scaled to the viewport's construction as desired.  Is there any other way to draw an arrowhead that does not involve using the `CRhinoArrowhead` class?

## Solution

Drawing arrowheads in a conduit by using an `CRhinoArrowhead` object might appear to be the correct approach, but this object is fairly specialized and designed to be used in conjunction with other annotation objects.  So in this case, this might not work well.

If you add your lines to the document, you can set the objects' decorations.  Then Rhino would draw the arrowheads for you.

But adding temporary geometry to the document just for display purposes is awkward and frowned upon.

You might be better off just drawing your own arrowheads.  It's really not that hard.  Draw arrowheads by calling the display pipeline's `DrawPolygon()` member with the fill parameter set to true.  The trick is defining the polygon you want to draw.

Below is some sample code that draws a 2D arrowhead at the end of a line similar to a leader object.  Perhaps this will give you an idea how to implement arrowhead drawing in your project.

```cpp
#pragma region SampleDrawArrowheadConduit conduit

class CSampleDrawArrowheadConduit : public CRhinoDisplayConduit
{
public:
  CSampleDrawArrowheadConduit(ON_Plane plane, ON_Line line, double scale);

  bool ExecConduit(CRhinoDisplayPipeline& dp, UINT channel, bool& terminate);

protected:
  bool GetArrowHead(ON_2dVector dir, ON_2dPoint tip, double scale, ON_3dPointArray& triangle);

protected:
  static double m_default_arrow_size;
  bool m_bDraw;
  ON_Line m_line;
  ON_Plane m_plane;
  ON_3dPointArray m_arrowhead;
};

double CSampleDrawArrowheadConduit::m_default_arrow_size = 1.0;

CSampleDrawArrowheadConduit::CSampleDrawArrowheadConduit(ON_Plane plane, ON_Line line, double scale)
  : CRhinoDisplayConduit(CSupportChannels::SC_CALCBOUNDINGBOX | CSupportChannels::SC_DRAWOVERLAY)
{
  m_bDraw = false;
  m_plane = plane;
  m_line = line;

  double x = 0.0, y = 0.0;

  m_plane.ClosestPointTo(line.from, &x, &y);
  ON_2dPoint from(x, y);

  m_plane.ClosestPointTo(line.to, &x, &y);
  ON_2dPoint to(x, y);

  ON_2dVector dir(from - to);
  dir.Unitize();

  m_bDraw = GetArrowHead(dir, from, scale, m_arrowhead);
}

bool CSampleDrawArrowheadConduit::ExecConduit(CRhinoDisplayPipeline& dp, UINT channel, bool& terminate)
{
  if (channel == CSupportChannels::SC_CALCBOUNDINGBOX)
  {
    m_pChannelAttrs->m_BoundingBox.Union(m_line.BoundingBox());
  }
  else if (channel ==CSupportChannels::SC_DRAWOVERLAY)
  {
    dp.DrawLine(m_line.from, m_line.to, m_pDisplayAttrs->m_ObjectColor | 0xFF000000, m_pDisplayAttrs->m_nLineThickness);
    if (m_bDraw)
      dp.DrawPolygon(m_arrowhead.Array(), m_arrowhead.Count(), m_pDisplayAttrs->m_ObjectColor | 0xFF000000, true);
  }
  return true;
}

bool CSampleDrawArrowheadConduit::GetArrowHead(ON_2dVector dir, ON_2dPoint tip, double scale, ON_3dPointArray& triangle)
{
  double arrow_size = CSampleDrawArrowheadConduit::m_default_arrow_size * scale;

  ON_2dPointArray corners(3);
  corners.SetCount(3);

  ON_2dVector up(-dir.y, dir.x);
  corners[0].Set(tip.x, tip.y);
  corners[1].x = tip.x + arrow_size * (0.25 * up.x - dir.x);
  corners[1].y = tip.y + arrow_size * (0.25 * up.y - dir.y);
  corners[2].x = corners[1].x - 0.5 * arrow_size * up.x;
  corners[2].y = corners[1].y - 0.5 * arrow_size * up.y;

  triangle.Reserve(corners.Count());
  triangle.SetCount(corners.Count());

  for (int i = 0; i < corners.Count(); i++)
    triangle[i] = m_plane.PointAt(corners[i].x, corners[i].y);

  return true;
}

#pragma endregion
```

Here is the above sample conduit used in a test command...

```cpp
CRhinoCommand::result CCommandSampleDrawArrowhead::RunCommand( const CRhinoCommandContext& context )
{
  ON_Line line;
  ON_Plane plane;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt(L"Start of line");
  gp.GetPoint();
  if (gp.CommandResult() != CRhinoCommand::success)
    return gp.CommandResult();

  line.from = gp.Point();
  plane = RhinoActiveCPlane();
  plane.SetOrigin(line.from);

  gp.SetCommandPrompt(L"End of line");
  gp.Constrain(plane);
  gp.SetBasePoint(line.from);
  gp.DrawLineFromPoint(line.from, TRUE);
  gp.GetPoint();
  if (gp.CommandResult() != CRhinoCommand::success)
    return gp.CommandResult();

  line.to = plane.ClosestPointTo(gp.Point());
  if (!line.IsValid())
    return CRhinoCommand::nothing;

  CSampleDrawArrowheadConduit conduit(plane, line, 1.0);
  conduit.Enable();
  context.m_doc.Redraw();

  CRhinoGetString gs;
  gs.SetCommandPrompt(L"Press <Enter> to continue");
  gs.AcceptNothing();
  gs.GetString();

  conduit.Disable();
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
