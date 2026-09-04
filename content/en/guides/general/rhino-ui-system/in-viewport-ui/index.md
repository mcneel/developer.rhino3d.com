+++
aliases = []
authors = [ "steve" ]
categories = [ "Fundamentals" ]
description = "How to draw interactive controls and grips directly inside a Rhino viewport."
keywords = [ "developer", "rhino", "ui", "viewport", "widget", "grip", "hud" ]
languages = [ "C/C++", "C#" ]
sdk = [ "General" ]
title = "In-Viewport User Interface"
type = "guides"
weight = 10

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = "In Progress"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

{{< figure src="in-viewport-ui.jpg" alt="In-viewport UI widgets in ArrayCrvAdvanced, Patch, GlobalEdgeContinuity, the Grasshopper widget components and ScaleEach" caption="Drag grips and readouts in ArrayCrvAdvanced, clickable continuity badges in Patch, numbered edge dots in GlobalEdgeContinuity, the Grasshopper widget components, and in-viewport sliders in ScaleEach." caption-align="left" >}}

## Overview

Rhino 9 adds an SDK for in-viewport user interface objects - widgets that draw inside a viewport and respond to the mouse. Instead of pushing the user out to a command line or panel, you can put the control next to the thing it controls.

If you have run Rhino 9 you may have already used them. `ArrayCrvAdvanced` uses on-curve span grips and rotation handles; `Patch` puts a clickable continuity badge on each constraint curve; `ScaleEach` and `RotateEach` use in-viewport sliders; `GlobalEdgeContinuity` drops a numbered dot at each evaluated edge; `Markup` is built as a floating HUD; and Grasshopper's Curve Widget and Angular Widget components are the same machinery.

The API is available in both RhinoCommon (the widget classes are in `Rhino.UI`; the `doc.ViewUserInterface` table is in `Rhino.DocObjects.Tables`) and the C/C++ SDK (*rhinoSdkUserInterfaceObject.h*).

## Two Kinds of UI Object

**World-space objects** live at a 3d point in the model. They pan and zoom with the scene, and they are depth-sorted against each other. The grip classes can additionally be dragged in 3d, constrained to a curve or circle, and osnapped. Use these when the control *is* a location: a base point, a direction, a rotation.

**Screen-space controls** are 2d widgets aligned to the viewport, at a fixed pixel size regardless of zoom. They can optionally "stick" to a 3d point so they follow an object around the screen while staying screen-aligned.

Everything derives from a common base - `UserInterfaceObjectBase` in RhinoCommon, `CRhinoUserInterfaceObject` in C++ - which is where the mouse events and visibility live.

## Adding and Removing Objects

UI objects belong to a document, and are added with a **group id**. The group id is how you find and remove them later, so a convenient convention is to use your command's id.

```cs
doc.ViewUserInterface.Add(new MyGrip(Point3d.Origin), this.Id);
```

```cpp
doc.AddUserInterfaceObject(new CMyGrip(ON_3dPoint::Origin), CommandUUID());
```

Removing is done by the same group id, and returns the number of objects removed. This gives you a natural toggle - a command that adds its widgets the first time it is run and clears them the next time:

```cs
public override string EnglishName => "SampleGrip";

protected override Result RunCommand(RhinoDoc doc, RunMode mode)
{
  // If the grip is already there, take it away. Otherwise, add one.
  bool gripExisted = doc.ViewUserInterface.RemoveByGroupId(this.Id) > 0;
  if (!gripExisted)
    doc.ViewUserInterface.Add(new MyGrip(new Point3d(0, 0, 0)), this.Id);

  doc.Views.Redraw();
  return Result.Success;
}
```

Note that the command returns immediately. The grip stays live in the viewport after the command has ended - it is owned by the document, not by the command that created it. This is the fundamental difference from a getter or a display conduit, and it is the reason these widgets feel like part of the model rather than part of a modal operation.

Redraws are not automatic when you add or remove objects. Call `doc.Views.Redraw()` (`CRhinoDoc::Redraw()` in C++) after changing what should be on screen.

## A World-Space Grip

Derive from the grip class and override `OnDrag` to be told where the user has moved it.

```cs
using Rhino;
using Rhino.Commands;
using Rhino.Geometry;
using Rhino.UI;

class MyGrip : GripUserInterfaceObject
{
  public MyGrip(Point3d location) : base(location)
  {
    GripFillColor = System.Drawing.Color.Orange;
  }

  protected override void OnDrag(Point3d newLocation, MouseState mouse)
  {
    base.OnDrag(newLocation, mouse);
    RhinoApp.WriteLine($"grip is at {GripLocation}");
  }
}
```

The same thing in C++:

```cpp
class CMyGrip : public CRhinoGripUserInterfaceObject
{
public:
  CMyGrip(const ON_3dPoint& location)
    : CRhinoGripUserInterfaceObject(location)
  {
    SetGripFillColor(ON_Color(255, 165, 0));
  }

  void OnDrag(const ON_3dPoint& point, const CRhinoMouseEventArgs& mouse) override
  {
    CRhinoGripUserInterfaceObject::OnDrag(point, mouse);
    const ON_3dPoint pt = GripLocation();
    RhinoApp().Print(L"grip is at %g,%g,%g\n", pt.x, pt.y, pt.z);
  }
};
```

Calling the base implementation matters: the default `OnDrag` is what actually moves the grip. If you skip it, you take responsibility for setting the location yourself - the `GripLocation` property in RhinoCommon, `SetGripLocation` in C++. That is occasionally what you want, if you are snapping the value to something of your own.

Grips can be styled (`GripShape`, `GripRadius`, `GripColor`, `GripFillColor`, `GripStrokeWidth`) and constrained. `Constrain` accepts a curve, circle, line or arc, and restricts dragging to that geometry.

## Screen-Space Controls

Controls are positioned with a location in logical pixels plus an alignment, which together determine where they land in any given view. Alignment is relative to the viewport, so a `Left`/`Bottom` control with a location of `(10, 100)` sits 10 pixels in from the left edge and 100 up from the bottom, in every view, at every zoom level.

```cs
var btn = new UserInterfaceButton
{
  Text = "Bake",
  Location = new System.Drawing.PointF(10, 100),
  HorizontalAlignment = ControlHorizontalAlignment.Left,
  VerticalAlignment = ControlVerticalAlignment.Bottom
};
btn.Click += (s, e) => RhinoApp.WriteLine("clicked");
doc.ViewUserInterface.Add(btn, Id);

var slider = new UserInterfaceSlider
{
  Location = new System.Drawing.PointF(10, 140),
  HorizontalAlignment = ControlHorizontalAlignment.Left,
  VerticalAlignment = ControlVerticalAlignment.Bottom,
  Range = new Interval(0, 10),
  Value = 5,
  DigitPrecision = 0        // 0 == integers only
};
slider.ValueChanged += (s, e) => RhinoApp.WriteLine($"{slider.Value}");
doc.ViewUserInterface.Add(slider, Id);
```

Instead of text, a control can display an image based on an SVG string - `SetSvg` in RhinoCommon, `SetImageSVG` in C++. This is the recommended way to get a crisp icon at every DPI.

Leave `Size` unset (zero) and the control computes its own size from its contents. Set it explicitly only when you need a fixed footprint.

To make a control follow an object around the screen, give it a **tracking point**:

```cs
control.TrackingPoint = someObject.Geometry.GetBoundingBox(true).Center;
```

The control stays screen-aligned and screen-sized, but its position now updates as the user orbits and zooms.

## Modifying the Document from a Mouse Handler

Your mouse handler runs inside a mouse callback, not inside a command. Undo records and getters are not set up the way you would expect, so adding, deleting or transforming objects directly from `OnDrag` or a `Click` handler produces broken or missing undo.

In C++ there is an explicit path for this. Call `RunCommand(mouse)` from your handler, and do the actual document work in the `OnRunCommand` override, which executes in proper command scope:

```cpp
class CMyGrip : public CRhinoGripUserInterfaceObject
{
public:
  CMyGrip(const ON_3dPoint& location)
    : CRhinoGripUserInterfaceObject(location)
  {
  }

  void OnMouseUp(const CRhinoMouseEventArgs& mouse) override
  {
    CRhinoGripUserInterfaceObject::OnMouseUp(mouse);
    // Defer the document edit into command scope
    RunCommand(mouse);
  }

  CRhinoCommand::result OnRunCommand(const CRhinoCommandContext& context, const CRhinoMouseEventArgs& mouse) override
  {
    // Safe to modify the document here - this is inside a command,
    // so undo is recorded correctly.
    CRhinoDoc* doc = CRhinoDoc::FromRuntimeSerialNumber(context.m_rhino_doc_sn);
    if (nullptr == doc)
      return CRhinoCommand::failure;

    doc->AddPointObject(GripLocation());
    doc->Redraw();
    return CRhinoCommand::success;
  }
};
```

## Caveats

**Objects outlive the command that created them.** Nothing cleans them up when your command ends. If you add widgets, you are responsible for removing them - on document close, on plugin unload, or on the next run of your command.

**Sizes and locations are in logical pixels.** Rhino handles the DPI scaling for you. Do not pre-multiply by a scale factor.

**Redraw explicitly.** Changing a property on a widget, or adding and removing widgets, does not by itself trigger a redraw.

**Mouse handlers run on the UI thread and block the viewport.** Keep them cheap. Anything expensive belongs behind `RunCommand`, or on a background thread with the result marshalled back.

## Related Topics

- [The Rhino UI System](/guides/general/rhino-ui-system/)
- [Rhino Beta Feature: In-Viewport User Interface](https://discourse.mcneel.com/t/rhino-beta-feature-in-viewport-user-interface/221416) on Discourse
- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin)
