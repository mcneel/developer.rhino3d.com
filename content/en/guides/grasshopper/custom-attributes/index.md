+++
aliases = ["/5/guides/grasshopper/custom-attributes/", "/6/guides/grasshopper/custom-attributes/", "/7/guides/grasshopper/custom-attributes/", "/wip/guides/grasshopper/custom-attributes/"]
authors = [ "david" ]
categories = [ "Advanced" ]
description = "This guide contains a step-by-step walkthrough regarding custom object display."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Custom Attributes"
type = "guides"
weight = 3
override_last_modified = "2019-02-07T11:38:44Z"

[admin]
TODO = ""
origin = "http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

Objects on the Grasshopper canvas consist of two parts.  The most important piece is the class that implements the [IGH_DocumentObject](/api/grasshopper/html/T_Grasshopper_Kernel_IGH_DocumentObject.htm) interface.  This interface provides the basic plumbing needed to make objects work within a Grasshopper node network.  The interface part of objects however is handled separately.  Every `IGH_DocumentObject` carries around an instance of a class that implements the [IGH_Attributes](/api/grasshopper/html/T_Grasshopper_Kernel_IGH_Attributes.htm) interface (indeed, every `IGH_DocumentObject` knows how to create its own stand-alone attributes) and it is this class that takes care of display, mouse interactions, popup menus, tooltips and so forth.

In this guide we'll see how you can create your own attributes object.  Since it's not possible to have an `IGH_Attributes` instance work on its own, we need an `IGH_DocumentObject` to tie it to.  For this guide we'll assume we have a custom simple parameter (i.e. without persistent data) that holds integers.

## Attributes Object

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'vb')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
public class MySimpleIntegerParameter : GH_Param<Types.GH_Integer>
{
  public MySimpleIntegerParameter() :
    base(new GH_InstanceDescription("Integer with stats", "Int(stats)",
                                    "Integer with basic statistics",
                                    "Params", "Primitive")) { }

  public override System.Guid ComponentGuid
  {
    get { return new Guid("{33D07726-8298-4104-9EBC-5398D8AD5421}"); }
  }
}

```

</div>

<div class="codetab-content" id="vb">

```vbnet
Public Class MySimpleIntegerParameter
  Inherits GH_Param(Of Types.GH_Integer)

  Public Sub New()
    MyBase.New(New GH_InstanceDescription("Integer with stats", "Int(stats)", "Integer with basic statistics", "Params", "Primitive"))
  End Sub

  Public Overrides ReadOnly Property ComponentGuid() As System.Guid
    Get
      Return New Guid("{33D07726-8298-4104-9EBC-5398D8AD5420}")
    End Get
  End Property
End Class
```

</div>
</div>

What we'll do is create a special attributes object for this parameter which also displays the median and mean values of the collection of all integers.  We want to put this information below the parameter name, but inside the parameter box.  The first step here is to override the `CreateAttributes()` on `MySimpleIntegerParameter` and assign a new instance of our (yet to be written) attributes class:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'vb1')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
public override void CreateAttributes()
{
  m_attributes = new MySimpleIntegerParameterAttributes(this);
}

```

</div>

<div class="codetab-content1" id="vb1">

```vbnet
Public Overrides Sub CreateAttributes()
  m_attributes = New MySimpleIntegerParameterAttributes(Me)
End Sub
```

</div>
</div>

That's it, no more code is required inside the `MySimpleIntegerParameter` class.  This part at least is simple.  If you don't override the `CreateAttributes()` method, then an instance of [GH_FloatingParamAttributes](/api/grasshopper/html/T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm) will be created instead.  If your parameter is to be attached to a component as an input or output, then the component will assign an instance of [GH_LinkedParamAttributes](/api/grasshopper/html/T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm) to the parameter and `CreateAttributes()` will never be called.

## Grasshopper.Kernel.GH_Attributes

Although the [IGH_Attributes](/api/grasshopper/html/T_Grasshopper_Kernel_IGH_Attributes.htm) interface is required for custom attributes, it is usually a good idea to derive from one of the abstract attribute classes already available.  [GH_Attributes(T)](/api/grasshopper/html/T_Grasshopper_Kernel_GH_Attributes_1.htm) is the most basic and obvious choice and it implements a large amount of methods with default behaviour, saving you a lot of time and effort:

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen2">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'vb2')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content2" id="cs2">

```cs
public class MySimpleIntegerParameterAttributes : GH_Attributes<MySimpleIntegerParameter>
{
  public MySimpleIntegerParameterAttributes(MySimpleIntegerParameter owner) : base(owner) { }
}

```

</div>

<div class="codetab-content2" id="vb2">

```vbnet
Public Class MySimpleIntegerParameterAttributes
  Inherits GH_Attributes(Of MySimpleIntegerParameter)

  Public Sub New(ByVal owner As MySimpleIntegerParameter)
    MyBase.New(owner)
  End Sub
End Class
```

</div>
</div>

This is enough so far to make it work, even though all the logic is still standard.  We need to start overriding methods in `MySimpleIntegerParameterAttributes` to suit our needs.  But first some basic information regarding the default behaviour.

`GH_Attributes<T>` assumes that the object that owns it is rectangular.  This is true for most objects in Grasshopper, but there are some notable exceptions such as Pie-Graphs, Sketches and Scribbles.  But this assumption (which holds true in our case) allows `GH_Attributes<T>` to supply basic functionality for a wide variety of methods.

All attributes have a property that defines the size of the object called [Bounds](/api/grasshopper/html/P_Grasshopper_Kernel_IGH_Attributes_Bounds.htm).  Basically everything that happens outside of the `Bounds` goes by unnoticed.  Also, if the Bounds rectangle is not visible within the canvas area, Grasshopper might decide to not even bother calling any painting methods.

Because our parameter will be rectangular, we don't have to override any of the picking logic, as the default implementation of [IsPickRegion](/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm), [IsMenuRegion](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) and [IsTooltipRegion](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) will already work.

## Layout

We do however need to supply custom Layout logic.  The width of our attributes depends on both the length of the `NickName` of the `MySimpleIntegerParameter` that owns these attributes *and* on the length of the statistics information we want to include.  The height of the parameter however is fixed, though larger than the standard height for parameters in Grasshopper.

In order to supply custom layout logic, we need to override the [Layout](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm) method.  In this case I measure the width of the `NickName` of the Owner object, and make sure the parameter is never narrower than 80 pixels:

<div class="codetab">
  <button class="tablinks3" onclick="openCodeTab(event, 'cs3')" id="defaultOpen3">C#</button>
  <button class="tablinks3" onclick="openCodeTab(event, 'vb3')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content3" id="cs3">

```cs
protected override void Layout()
{
  // Compute the width of the NickName of the owner (plus some extra padding),
  // then make sure we have at least 80 pixels.
  int width = GH_FontServer.StringWidth(Owner.NickName, GH_FontServer.Standard);
  width = Math.Max(width + 10, 80);

  // The height of our object is always 60 pixels
  int height = 60;

  // Assign the width and height to the Bounds property.
  // Also, make sure the Bounds are anchored to the Pivot
  Bounds = new RectangleF(Pivot, new SizeF(width, height));
}

```

</div>

<div class="codetab-content3" id="vb3">

```vbnet
Protected Overrides Sub Layout()
  'Compute the width of the NickName of the owner (plus some extra padding),
  'then make sure we have at least 80 pixels.
  Dim width As Int32 = GH_FontServer.StringWidth(Owner.NickName, GH_FontServer.Standard)
  width = Math.Max(width + 10, 80)

  'The height of our object is always 60 pixels
  Dim height As Int32 = 60

  'Assign the width and height to the Bounds property.
  'Also, make sure the Bounds are anchored to the Pivot
  Bounds = New RectangleF(Pivot, New SizeF(width, height))
End Sub
```

</div>
</div>

The `Pivot` is a `PointF` structure that is changed when the object is dragged.  It is therefore important that you always "anchor" the layout of some attributes to the `Pivot`.  If you fail to do so, your attributes will become undraggable.

There is a method you can override that will be called prior to the call to `Layout` which can be used to destroy any cached data you might have that's to do with display.  But note that if you override [ExpireLayout](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) you *must* place a call to the base class method as well:

<div class="codetab">
  <button class="tablinks4" onclick="openCodeTab(event, 'cs4')" id="defaultOpen4">C#</button>
  <button class="tablinks4" onclick="openCodeTab(event, 'vb4')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content4" id="cs4">

```cs
publicoverride void ExpireLayout()
{    
  base.ExpireLayout();

  // Destroy any data you have that becomes
  // invalid when the layout expires.
}

```

</div>

<div class="codetab-content4" id="vb4">

```vbnet
Public Overrides Sub ExpireLayout()
  MyBase.ExpireLayout()

  'Destroy any data you have that becomes
  'invalid when the layout expires.
End Sub
```

</div>
</div>

## Render

Now that we have handled the Layout, we need to override the display of the parameter.  There's two parts to doing so.  You always have to override the [Render](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_Render.htm) method, as this is where the drawing takes place.  Render is called a number of times as there are several "layers" or "channels" to a single Grasshopper canvas.  At first, the background of the canvas is drawn.  During this process attributes are not yet involved.  Then there will be four channels where `IGH_Attributes` will be allowed to draw various shapes.

First the groups are drawn (as they are behind all other objects), but every `GH_Attributes.Render()` method will be called once for the [Groups](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel.  Typically you should not draw anything in the Groups channel.

Next up is the [Wires](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel where all parameter connector wires are drawn.  If your object has input parameters or is a parameter, it is your responsibility to draw all wires coming into your object.  Wires going out the right side will be drawn by the recipient objects.

Next the actual Components and Parameters themselves are drawn inside the [Objects](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel.  This is typically the most work, though there are lots of classes that take care of common tasks.  The default visual style of Components and parameter objects is the shiny, rounded rectangle.  You can use the [GH_Capsule](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm) type to draw these shapes with a minimum of fuss.

Ultimately there's an [Overlay](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel which is rarely used but it allows you to draw shapes that need to be on top of all other components and parameters.  After this, there are still more channels to do with canvas widgets, but `IGH_Attributes` are not involved here.

Inside our implementation of the `Render()` method, we need to draw the wires coming into the `MySimpleIntegerParameter`, then the parameter capsule, while taking care to assign the correct colours (grey for normal, green for selected, dark for disabled, orange for warnings and red for errors).  Finally we have to draw three lines of text on top of the capsule; the name of the owner, the median integer and the mean integer.  The important types involved here are:

- [GH_Canvas](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm)
- [GH_Painter](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Painter.htm)
- [GH_Palette](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Palette.htm)
- [GH_RuntimeMessageLevel](/api/grasshopper/html/T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)
- [GH_Capsule](/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm)
- [GH_FontServer](/api/grasshopper/html/T_Grasshopper_Kernel_GH_FontServer.htm)

<div class="codetab">
  <button class="tablinks5" onclick="openCodeTab(event, 'cs5')" id="defaultOpen5">C#</button>
  <button class="tablinks5" onclick="openCodeTab(event, 'vb5')">VB.NET</button>
</div>

<div class="tab-content">
<div class="codetab-content5" id="cs5">

```cs
protected override void Render(GH_Canvas canvas, Graphics graphics, GH_CanvasChannel channel)
{
  // Render all the wires that connect the Owner to all its Sources.
  if (channel == GH_CanvasChannel.Wires)
  {
    RenderIncomingWires(canvas.Painter, Owner.Sources, Owner.WireDisplay);
    return;
  }

  // Render the parameter capsule and any additional text on top of it.
  if (channel == GH_CanvasChannel.Objects)
  {
    // Define the default palette.
    GH_Palette palette = GH_Palette.Normal;

    // Adjust palette based on the Owner's worst case messaging level.
    switch (Owner.RuntimeMessageLevel)
    {
      case GH_RuntimeMessageLevel.Warning:
        palette = GH_Palette.Warning;
        break;

      case GH_RuntimeMessageLevel.Error:
        palette = GH_Palette.Error;
        break;
     }

    // Create a new Capsule without text or icon.
    GH_Capsule capsule = GH_Capsule.CreateCapsule(Bounds, palette);

    // Render the capsule using the current Selection, Locked and Hidden states.
    // Integer parameters are always hidden since they cannot be drawn in the viewport.
    capsule.Render(graphics, Selected, Owner.Locked, true);

    // Always dispose of a GH_Capsule when you're done with it.
    capsule.Dispose();
    capsule = null;

    // Now it's time to draw the text on top of the capsule.
    // First we'll draw the Owner NickName using a standard font and a black brush.
    // We'll also align the NickName in the center of the Bounds.
    StringFormat format = new StringFormat();
    format.Alignment = StringAlignment.Center;
    format.LineAlignment = StringAlignment.Center;
    format.Trimming = StringTrimming.EllipsisCharacter;

    // Our entire capsule is 60 pixels high, and we'll draw
    // three lines of text, each 20 pixels high.
    RectangleF textRectangle = Bounds;
    textRectangle.Height = 20;

    // Draw the NickName in a Standard Grasshopper font.
    graphics.DrawString(Owner.NickName, GH_FontServer.Standard, Brushes.Black, textRectangle, format);


    // Now we need to draw the median and mean information.
    // Adjust the formatting and the layout rectangle.
    format.Alignment = StringAlignment.Near;
    textRectangle.Inflate(-5, 0);

    textRectangle.Y += 20;
    graphics.DrawString(String.Format("Median: {0}", Owner.MedianValue), _
                        GH_FontServer.StandardItalic, Brushes.Black, _
                        textRectangle, format);

    textRectangle.Y += 20;
    graphics.DrawString(String.Format("Mean: {0:0.00}", Owner.MeanValue), _
                        GH_FontServer.StandardItalic, Brushes.Black, _
                        textRectangle, format);

    // Always dispose of any GDI+ object that implement IDisposable.
    format.Dispose();
  }
}

```

</div>

<div class="codetab-content5" id="vb5">

```vbnet
Protected Overrides Sub Render(ByVal canvas As GH_Canvas, ByVal graphics As Graphics, ByVal channel As GH_CanvasChannel)
  'Render all the wires that connect the Owner to all its Sources.
  If (channel = GH_CanvasChannel.Wires) Then
    RenderIncomingWires(canvas.Painter, Owner.Sources, Owner.WireDisplay)
    Return
  End If

  'Render the parameter capsule and any additional text on top of it.
  If (channel = GH_CanvasChannel.Objects) Then
    'Define the default palette.
    Dim palette As GH_Palette = GH_Palette.Normal

    'Adjust palette based on the Owner's worst case messaging level.
    Select Case Owner.RuntimeMessageLevel
      Case GH_RuntimeMessageLevel.Warning
        palette = GH_Palette.Warning

      Case GH_RuntimeMessageLevel.Error
        palette = GH_Palette.Error
    End Select

    'Create a new Capsule without text or icon.
    Dim capsule As GH_Capsule = GH_Capsule.CreateCapsule(Bounds, palette)

    'Render the capsule using the current Selection, Locked and Hidden states.
    'Integer parameters are always hidden since they cannot be drawn in the viewport.
    capsule.Render(graphics, Selected, Owner.Locked, True)

    'Always dispose of a GH_Capsule when you're done with it.
    capsule.Dispose()
    capsule = Nothing

    'Now it's time to draw the text on top of the capsule.
    'First we'll draw the Owner NickName using a standard font and a black brush.
    'We'll also align the NickName in the center of the Bounds.
    Dim format As New StringFormat()
    format.Alignment = StringAlignment.Center
    format.LineAlignment = StringAlignment.Center
    format.Trimming = StringTrimming.EllipsisCharacter

    'Our entire capsule is 60 pixels high, and we'll draw
    'three lines of text, each 20 pixels high.
    Dim textRectangle As RectangleF = Bounds
    textRectangle.Height = 20

    'Draw the NickName in a Standard Grasshopper font.
    graphics.DrawString(Owner.NickName, GH_FontServer.Standard, Brushes.Black, textRectangle, format)


    'Now we need to draw the median and mean information.
    'Adjust the formatting and the layout rectangle.
    format.Alignment = StringAlignment.Near
    textRectangle.Inflate(-5, 0)

    textRectangle.Y += 20
    graphics.DrawString(String.Format("Median: {0}", Owner.MedianValue), _
                        GH_FontServer.StandardItalic, Brushes.Black, _
                        textRectangle, format)

    textRectangle.Y += 20
    graphics.DrawString(String.Format("Mean: {0:0.00}", Owner.MeanValue), _
                        GH_FontServer.StandardItalic, Brushes.Black, _
                        textRectangle, format)

    'Always dispose of any GDI+ object that implement IDisposable.
    format.Dispose()
  End If
End Sub
```

</div>
</div>

Note that in this case I assume that `MySimpleIntegerParameter` has two ReadOnly properties called `MedianValue` and `MeanValue`.  I haven't written those, as they are not within the scope of this guide.

If you have cached display objects (for whatever reason I don't want to hear), a good place to ensure they are [PrepareForRender](/api/grasshopper/html/M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) method.  It is called once (and only once) just before any calls to `Render()`.  You do not need to call the overridden method as it is empty by default.
