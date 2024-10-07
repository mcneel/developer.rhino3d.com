+++
aliases = ["/en/5/guides/rhinocommon/display-conduits/", "/en/6/guides/rhinocommon/display-conduits/", "/en/7/guides/rhinocommon/display-conduits/", "/en/wip/guides/rhinocommon/display-conduits/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide gives an overview of Display Conduits and how to use them to access Rhino's display pipeline."
keywords = [ "RhinoCommon", "Display", "Conduits", "Rhino" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Display Conduits"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/displayconduit"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

 
Rhino lets you define your own display conduits, which provide access to many levels of the display pipeline.  They are a bit tricky.  This guide cover the concepts and basics of using display conduits.

## Conduit Concept

The DisplayPipeline in Rhino is a big and complicated class and we do not recommend you derive your own pipeline.  Instead, we've exposed something called a conduit for easy access.  The pipeline itself is structured like this (except in reality there are many more channels):

![Rhino Display Pipeline](/images/display-conduits-01.png)

At one end is the Rhino model, a collection of 3D geometry and data.  At the other end is the image we want to display on the screen, a collection of 2D pixels.  To get from model to image, the pipeline has to process a lot of information.  These steps have been put into channels.  When you implement a new conduit, you have to implement at least one of these channels, like so:

![Rhino Display Conduit](/images/display-conduits-02.png)

Note that the pipeline itself is not bound to the channels.  It just executes its code and raises events during specific phases of drawing.  During the drawing of a single frame the events are raised in the following order.  You hook into the pipeline by extending DisplayConduit and overriding the event handlers that have the same name as the pipeline events:

1. *ObjectCulling*: Create a list of all the objects to draw.
1. *CalculateBoundingBox*: Determine the extent of the entire scene.  Override this function to increase the bounding box of scene so it includes the geometry that you plan to draw.
1. *CalculateBoundingBoxZoomExtents*: If you want to participate in the Zoom Extents command with your display conduit, then you need to override ZoomExtentsBoundingBox.  Typically you could just call your CalculateBoundingBox override, but you may also want to spend a little more time here and compute a tighter bounding box for your conduit geometry.
1. *PreDrawObjects*: Called before objects are drawn.  Depth writing and testing are on. Here you could set up the object's display attributes.
1. *PreDrawObject*: Called before every object in the scene is drawn.
1. *PostDrawObjects*: Called after all non-highlighted objects are drawn.  Depth writing and testing are still turned on. If you want to draw without depth writing and testing, see DrawForeground.  Here you draw stuff on top of all the objects, like selection wireframes.
1. *DrawForeground*: Called after all non-highlighted objects are drawn and PostDrawObjects called. Depth writing and testing are turned *off*.  If you want to draw with depth writing and testing, see PostDrawObjects.  For example, here you could draw objects like the little axis-system in the lower left corner of viewports.
1. *DrawOverlay*: If Rhino is in a feedback mode, the draw overlay call lets temporary geometry be drawn on top of everything in the scene.  This is similar to the dynamic draw routine that occurs with custom get point.

You hook into the pipeline by extending DisplayConduit and overriding the key event handlers which have the same name as the pipeline events.

## Implementation

In the above image, the conduit overrode two event handlers; `CalculateBoundingBox` and `PostDrawObjects`. In RhinoCommon this conduit would look like:

```cs
class MyConduit : Rhino.Display.DisplayConduit
{
  protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
  {
    base.CalculateBoundingBox(e);
    // ..
  }

  protected override void PostDrawObjects(DrawEventArgs e)
  {
    base.PreDrawObjects(e);
    // ..
  }
}
```

By default, conduits are not enabled but it is easily done by setting the Enabled property of the DisplayConduit to true:

```cs
var conduit = new MyConduit();
conduit.Enabled = true;
```

Once our conduit is constructed and enabled, the overriden methods will be called whenever the Rhino pipeline raises the event for which our overridden method is registered.  In our case, this method will always be called once with the `CalculateBoundingBox` and the `PostDrawObjects` events have been raised (the events have the same name as the overridden methods).  Here's a simple example:

```cs
class MyConduit : Rhino.Display.DisplayConduit
{
  protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
  {
    base.CalculateBoundingBox(e);
    var bbox = new BoundingBox();
    bbox.Union(new Point3d(0, 0, 0));
    e.IncludeBoundingBox(bbox);
  }

  protected override void PreDrawObjects(DrawEventArgs e)
  {
    base.PreDrawObjects(e);
    e.Display.DrawPoint(new Point3d(0, 0, 0));
  }
}
```

The code above simply draws a single point at the world origin. Since a point is 3D geometry, it is subject to z-depth clipping. This means that if the point resides outside the z-buffer region, it will not be visible (it will get *clipped*). By default, the clipping planes are set up to encompass the bounding box of the entire Rhino model.  If you are drawing stuff which is potentially outside this box, you should override `CalculateBoundingBox` to make sure your objects are not clipped.

Let's take a look at a more complex drawing routine:

```cs
protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
{
  base.CalculateBoundingBox(e);
  var bbox = new BoundingBox();
  bbox.Union(e.Display.Viewport.ConstructionPlane().Origin);
  e.IncludeBoundingBox(bbox);
}

protected override void PreDrawObjects(DrawEventArgs e)
{
  base.PreDrawObjects(e);

  var cPlane = e.Display.Viewport.ConstructionPlane();
  var xColor = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor;
  var yColor = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor;
  var zColor = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor;

  e.Display.EnableDepthWriting(false);
  e.Display.EnableDepthTesting(false);

  e.Display.DrawPoint(cPlane.Origin, System.Drawing.Color.White);
  e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.XAxis) * 10.0), xColor);
  e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.YAxis) * 10.0), yColor);
  e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.ZAxis) * 10.0), zColor);

  e.Display.EnableDepthWriting(false);
  e.Display.EnableDepthTesting(false);
}
```

This piece of code draws a colored, c-plane axis system on top of all objects.  Because we disable DepthWriting and Testing before drawing my points and arrows, my objects are not obscured by the existing geometry (which was drawn in a channel previous to `PostDrawObjects`):

![Resulting Frame](/images/display-conduits-03.png)

## Warning

Another thing to realize is that there can be many other active conduits present as well.  There is no way of telling which one will be called first.  It is important to consider how your display conduits will interact with other conduits potentially called within the pipeline by other developers.  Do not write display conduit code that intentionally disrupts other conduits.

![Many Conduits](/images/display-conduits-04.png)
