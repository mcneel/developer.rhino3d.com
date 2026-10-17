+++
aliases = ["/en/5/samples/rhinocommon/sprite-drawing/", "/en/6/samples/rhinocommon/sprite-drawing/", "/en/7/samples/rhinocommon/sprite-drawing/", "/en/wip/samples/rhinocommon/sprite-drawing/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to draw bitmap sprites in Rhino."
keywords = [ "sprite", "drawing" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Sprite Drawing"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  static bool m_draw_single_sprite;
  static float m_sprite_size = 30;
  static bool m_draw_world_location = true;

  public static Rhino.Commands.Result SpriteDrawing(RhinoDoc doc)
  {
    var sprite_mode = new Rhino.Input.Custom.OptionToggle(m_draw_single_sprite, "SpriteList", "SingleSprite");
    var size_option = new Rhino.Input.Custom.OptionDouble(m_sprite_size);
    var space_option = new Rhino.Input.Custom.OptionToggle(m_draw_world_location, "Screen", "World");
    var go = new Rhino.Input.Custom.GetOption();
    go.SetCommandPrompt("Sprite drawing mode");
    go.AddOptionToggle("Mode", ref sprite_mode);
    go.AddOptionDouble("Size", ref size_option);
    go.AddOptionToggle("DrawSpace", ref space_option);
    int option_go = go.AddOption("Spin");
    int option_file = go.AddOption("FileSprite");

    Rhino.Display.DisplayPipeline.PostDrawObjects += DisplayPipeline_PostDrawObjects;
    Rhino.Display.DisplayPipeline.CalculateBoundingBox += DisplayPipeline_CalculateBoundingBox;

    doc.Views.Redraw();
    while (go.Get() == Rhino.Input.GetResult.Option)
    {
      m_draw_single_sprite = sprite_mode.CurrentValue;
      m_sprite_size = (float)size_option.CurrentValue;
      m_draw_world_location = space_option.CurrentValue;
      if (go.OptionIndex() == option_go)
      {
        var gs = new Rhino.Input.Custom.GetOption();
        gs.SetCommandPrompt("press enter/escape to end");
        gs.SetWaitDuration(1);

        var vp = doc.Views.ActiveView.MainViewport;
        while (gs.Get() == Rhino.Input.GetResult.Timeout)
        {
          vp.Rotate(0.1, Vector3d.ZAxis, Point3d.Origin);
          doc.Views.Redraw();
        }
      }
      else if (go.OptionIndex() == option_file)
      {
        var dlg = new Rhino.UI.OpenFileDialog();
        if (dlg.ShowDialog())
        {
          System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(dlg.FileName);
          m_sprite = new Rhino.Display.DisplayBitmap(bmp);
        }
        doc.Views.Redraw();
      }
      else
        doc.Views.Redraw();
    }

    Rhino.Display.DisplayPipeline.PostDrawObjects -= DisplayPipeline_PostDrawObjects;
    Rhino.Display.DisplayPipeline.CalculateBoundingBox -= DisplayPipeline_CalculateBoundingBox;
    return Rhino.Commands.Result.Success;
  }

  static void DisplayPipeline_CalculateBoundingBox(object sender, Rhino.Display.CalculateBoundingBoxEventArgs e)
  {
    if (m_draw_single_sprite)
    {
      BoundingBox bbox = new BoundingBox(new Point3d(20, 0, 0), new Point3d(20, 0, 0));
      e.IncludeBoundingBox(bbox);
    }
    else
    {
      var items = GetItems();
      e.IncludeBoundingBox(items.BoundingBox);
    }
  }

  static void DisplayPipeline_PostDrawObjects(object sender, Rhino.Display.DrawEventArgs e)
  {
    var spr = GetSprite();
    if (m_draw_single_sprite)
    {
      if (m_draw_world_location)
        e.Display.DrawSprite(spr, new Point3d(20, 0, 0), m_sprite_size, System.Drawing.Color.White, false);
      else
        e.Display.DrawSprite(spr, new Point2d(150, 150), m_sprite_size, System.Drawing.Color.White);
    }
    else
    {
      var items = GetItems();
      e.Display.DrawSprites(spr, items, m_sprite_size, false);
    }
  }

  static Rhino.Display.DisplayBitmapDrawList m_items;
  static Rhino.Display.DisplayBitmapDrawList GetItems()
  {
    if (m_items == null)
    {
      m_items = new Rhino.Display.DisplayBitmapDrawList();
      var points = new System.Collections.Generic.List<Point3d>();
      var colors = new System.Collections.Generic.List<System.Drawing.Color>();
      var random = new System.Random();
      for (int i = 0; i < 200; i++)
      {
        double x = random.NextDouble();
        double y = random.NextDouble();
        double z = random.NextDouble();
        points.Add(new Point3d(-30 + x * 60, -30 + y * 60, -30 + z * 60));
        int r = (int)(x * 255);
        int g = (int)(y * 255);
        int b = (int)(z * 255);
        colors.Add(System.Drawing.Color.FromArgb(r, g, b));
      }
      m_items.SetPoints(points, colors);
    }
    return m_items;
  }

  static Rhino.Display.DisplayBitmap m_sprite;
  static Rhino.Display.DisplayBitmap GetSprite()
  {
    if (m_sprite == null)
    {
      var bmp = new System.Drawing.Bitmap(64, 64);
      using (System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(bmp))
      {
        g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
        g.Clear(System.Drawing.Color.Transparent);
        var pen = new System.Drawing.Pen(System.Drawing.Color.White, 6);
        pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;
        pen.StartCap = pen.EndCap;
        g.DrawArc(pen, new System.Drawing.Rectangle(16, 16, 32, 32), 0, 360);
        g.DrawLine(pen, new System.Drawing.Point(8, 8), new System.Drawing.Point(56, 56));
        g.DrawLine(pen, new System.Drawing.Point(8, 56), new System.Drawing.Point(56, 8));
        pen.Dispose();
      }
      m_sprite = new Rhino.Display.DisplayBitmap(bmp);
    }
    return m_sprite;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System
import scriptcontext as sc


# module-level state (equivalent to C# static fields)
m_draw_single_sprite = False
m_sprite_size = 30.0
m_draw_world_location = True
m_items = None
m_sprite = None


def GetItems():
    global m_items
    if m_items is None:
        m_items = Rhino.Display.DisplayBitmapDrawList()
        points = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
        colors = System.Collections.Generic.List[System.Drawing.Color]()
        random = System.Random()
        for i in range(200):
            x = random.NextDouble()
            y = random.NextDouble()
            z = random.NextDouble()
            points.Add(Rhino.Geometry.Point3d(-30 + x * 60, -30 + y * 60, -30 + z * 60))
            r = int(x * 255)
            g = int(y * 255)
            b = int(z * 255)
            colors.Add(System.Drawing.Color.FromArgb(r, g, b))
        m_items.SetPoints(points, colors)
    return m_items


def GetSprite():
    global m_sprite
    if m_sprite is None:
        bmp = System.Drawing.Bitmap(64, 64)
        g = System.Drawing.Graphics.FromImage(bmp)
        try:
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias
            g.Clear(System.Drawing.Color.Transparent)
            pen = System.Drawing.Pen(System.Drawing.Color.White, 6)
            pen.EndCap = System.Drawing.Drawing2D.LineCap.Round
            pen.StartCap = pen.EndCap
            g.DrawArc(pen, System.Drawing.Rectangle(16, 16, 32, 32), 0, 360)
            g.DrawLine(pen, System.Drawing.Point(8, 8), System.Drawing.Point(56, 56))
            g.DrawLine(pen, System.Drawing.Point(8, 56), System.Drawing.Point(56, 8))
            pen.Dispose()
        finally:
            g.Dispose()
        m_sprite = Rhino.Display.DisplayBitmap(bmp)
    return m_sprite


def DisplayPipeline_CalculateBoundingBox(sender, e):
    if m_draw_single_sprite:
        bbox = Rhino.Geometry.BoundingBox(
            Rhino.Geometry.Point3d(20, 0, 0), Rhino.Geometry.Point3d(20, 0, 0)
        )
        e.IncludeBoundingBox(bbox)
    else:
        items = GetItems()
        e.IncludeBoundingBox(items.BoundingBox)


def DisplayPipeline_PostDrawObjects(sender, e):
    spr = GetSprite()
    if m_draw_single_sprite:
        if m_draw_world_location:
            e.Display.DrawSprite(
                spr, Rhino.Geometry.Point3d(20, 0, 0), m_sprite_size,
                System.Drawing.Color.White, False,
            )
        else:
            e.Display.DrawSprite(
                spr, Rhino.Geometry.Point2d(150, 150), m_sprite_size,
                System.Drawing.Color.White,
            )
    else:
        items = GetItems()
        e.Display.DrawSprites(spr, items, m_sprite_size, False)


def RunCommand():
    global m_draw_single_sprite, m_sprite_size, m_draw_world_location, m_sprite

    sprite_mode = Rhino.Input.Custom.OptionToggle(m_draw_single_sprite, "SpriteList", "SingleSprite")
    size_option = Rhino.Input.Custom.OptionDouble(m_sprite_size)
    space_option = Rhino.Input.Custom.OptionToggle(m_draw_world_location, "Screen", "World")
    go = Rhino.Input.Custom.GetOption()
    go.SetCommandPrompt("Sprite drawing mode")
    go.AddOptionToggle("Mode", sprite_mode)
    go.AddOptionDouble("Size", size_option)
    go.AddOptionToggle("DrawSpace", space_option)
    option_go = go.AddOption("Spin")
    option_file = go.AddOption("FileSprite")

    Rhino.Display.DisplayPipeline.PostDrawObjects += DisplayPipeline_PostDrawObjects
    Rhino.Display.DisplayPipeline.CalculateBoundingBox += DisplayPipeline_CalculateBoundingBox

    sc.doc.Views.Redraw()
    while go.Get() == Rhino.Input.GetResult.Option:
        m_draw_single_sprite = sprite_mode.CurrentValue
        m_sprite_size = float(size_option.CurrentValue)
        m_draw_world_location = space_option.CurrentValue
        if go.OptionIndex() == option_go:
            gs = Rhino.Input.Custom.GetOption()
            gs.SetCommandPrompt("press enter/escape to end")
            gs.SetWaitDuration(1)

            vp = sc.doc.Views.ActiveView.MainViewport
            while gs.Get() == Rhino.Input.GetResult.Timeout:
                vp.Rotate(0.1, Rhino.Geometry.Vector3d.ZAxis, Rhino.Geometry.Point3d.Origin)
                sc.doc.Views.Redraw()
        elif go.OptionIndex() == option_file:
            dlg = Rhino.UI.OpenFileDialog()
            if dlg.ShowDialog():
                bmp = System.Drawing.Bitmap(dlg.FileName)
                m_sprite = Rhino.Display.DisplayBitmap(bmp)
            sc.doc.Views.Redraw()
        else:
            sc.doc.Views.Redraw()

    Rhino.Display.DisplayPipeline.PostDrawObjects -= DisplayPipeline_PostDrawObjects
    Rhino.Display.DisplayPipeline.CalculateBoundingBox -= DisplayPipeline_CalculateBoundingBox
    return Rhino.Commands.Result.Success


if __name__ == "__main__":
    RunCommand()
```

</div>
