+++
aliases = ["/en/5/samples/rhinocommon/show-surface-direction/", "/en/6/samples/rhinocommon/show-surface-direction/", "/en/7/samples/rhinocommon/show-surface-direction/", "/en/wip/samples/rhinocommon/show-surface-direction/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to show a surface's direction using a display conduit."
keywords = [ "show", "surface", "direction" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Show Surface Direction"
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
  public static Rhino.Commands.Result ShowSurfaceDirection(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface for direction display",
      false,
      Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter,
      out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var brep = objref.Brep();
    if (brep == null)
      return Rhino.Commands.Result.Failure;

    bool bIsSolid = brep.IsSolid;

    TestSurfaceDirConduit conduit = new TestSurfaceDirConduit(brep);
    conduit.Enabled = true;
    doc.Views.Redraw();

    var gf = new Rhino.Input.Custom.GetOption();
    gf.SetCommandPrompt("Press enter when done");
    gf.AcceptNothing(true);
    if (!bIsSolid)
      gf.AddOption("Flip");

    for (; ; )
    {
      var res = gf.Get();
      if (res == Rhino.Input.GetResult.Option)
      {
        conduit.Flip = !conduit.Flip;
        doc.Views.Redraw();
        continue;
      }
      if (res == Rhino.Input.GetResult.Nothing)
      {
        if (!bIsSolid && conduit.Flip)
        {
          brep.Flip();
          doc.Objects.Replace(objref, brep);
        }
      }
      break;
    }

    conduit.Enabled = false;
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}

class TestSurfaceDirConduit : Rhino.Display.DisplayConduit
{
  readonly Brep m_brep;
  readonly List<Point3d> m_points;
  readonly List<Vector3d> m_normals;

  public TestSurfaceDirConduit(Brep brep)
  {
    m_brep = brep;
    Flip = false;

    const int SURFACE_ARROW_COUNT = 5;
    int face_count = m_brep.Faces.Count;
    int capacity = face_count * SURFACE_ARROW_COUNT * SURFACE_ARROW_COUNT;
    m_points = new List<Point3d>(capacity);
    m_normals = new List<Vector3d>(capacity);

    for (int i = 0; i < face_count; i++)
    {
      var face = brep.Faces[i];
      var loop = face.OuterLoop;
      if (loop == null)
        continue;

      var udomain = face.Domain(0);
      var vdomain = face.Domain(1);
      var loop_bbox = loop.GetBoundingBox(true);
      if (loop_bbox.IsValid)
      {
        Interval domain = new Interval(loop_bbox.Min.X, loop_bbox.Max.X);
        domain = Interval.FromIntersection(domain, udomain);
        if (domain.IsIncreasing)
          udomain = domain;
        domain = new Interval(loop_bbox.Min.Y, loop_bbox.Max.Y);
        domain = Interval.FromIntersection(domain, vdomain);
        if (domain.IsIncreasing)
          vdomain = domain;
      }

      bool bUntrimmed = face.IsSurface;
      bool bRev = face.OrientationIsReversed;
      for (double u = 0; u < SURFACE_ARROW_COUNT; u += 1.0)
      {
        double d = u / (SURFACE_ARROW_COUNT - 1.0);
        double s = udomain.ParameterAt(d);

        var intervals = face.TrimAwareIsoIntervals(1, s);
        if (bUntrimmed || intervals.Length > 0)
        {
          for (double v = 0; v < SURFACE_ARROW_COUNT; v += 1.0)
          {
            d = v / (SURFACE_ARROW_COUNT - 1.0);
            double t = vdomain.ParameterAt(d);
            bool bAdd = bUntrimmed;
            for (int k = 0; !bAdd && k < intervals.Length; k++)
            {
              if (intervals[k].IncludesParameter(t))
                bAdd = true;
            }
            if (bAdd)
            {
              var pt = face.PointAt(s, t);
              var vec = face.NormalAt(s, t);
              m_points.Add(pt);
              if (bRev)
                vec.Reverse();
              m_normals.Add(vec);
            }
          }
        }
      }
    }
  }

  public bool Flip { get; set; }

  protected override void DrawOverlay(Rhino.Display.DrawEventArgs e)
  {
    if (m_points.Count > 0)
    {
      var color = Rhino.ApplicationSettings.AppearanceSettings.TrackingColor;
      for (int i = 0; i < m_points.Count; i++)
      {
        if (i % 100 == 0 && e.Display.InterruptDrawing())
          break;

        var pt = m_points[i];
        var dir = m_normals[i];
        if (Flip)
          dir.Reverse();
        e.Display.DrawDirectionArrow(pt, dir, color);
      }
    }
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import scriptcontext as sc

class TestSurfaceDirConduit(Rhino.Display.DisplayConduit):
    def __init__(self, brep):
        super().__init__()
        self.m_brep = brep
        self.Flip = False

        SURFACE_ARROW_COUNT = 5
        face_count = self.m_brep.Faces.Count
        self.m_points = []
        self.m_normals = []

        for i in range(face_count):
            face = brep.Faces[i]
            loop = face.OuterLoop
            if loop is None:
                continue

            udomain = face.Domain(0)
            vdomain = face.Domain(1)
            loop_bbox = loop.GetBoundingBox(True)
            if loop_bbox.IsValid:
                domain = Rhino.Geometry.Interval(loop_bbox.Min.X, loop_bbox.Max.X)
                domain = Rhino.Geometry.Interval.FromIntersection(domain, udomain)
                if domain.IsIncreasing:
                    udomain = domain
                domain = Rhino.Geometry.Interval(loop_bbox.Min.Y, loop_bbox.Max.Y)
                domain = Rhino.Geometry.Interval.FromIntersection(domain, vdomain)
                if domain.IsIncreasing:
                    vdomain = domain

            bUntrimmed = face.IsSurface
            bRev = face.OrientationIsReversed
            u = 0.0
            while u < SURFACE_ARROW_COUNT:
                d = u / (SURFACE_ARROW_COUNT - 1.0)
                s = udomain.ParameterAt(d)

                intervals = face.TrimAwareIsoIntervals(1, s)
                if bUntrimmed or len(intervals) > 0:
                    v = 0.0
                    while v < SURFACE_ARROW_COUNT:
                        d = v / (SURFACE_ARROW_COUNT - 1.0)
                        t = vdomain.ParameterAt(d)
                        bAdd = bUntrimmed
                        k = 0
                        while not bAdd and k < len(intervals):
                            if intervals[k].IncludesParameter(t):
                                bAdd = True
                            k += 1
                        if bAdd:
                            pt = face.PointAt(s, t)
                            vec = face.NormalAt(s, t)
                            self.m_points.append(pt)
                            if bRev:
                                vec.Reverse()
                            self.m_normals.append(vec)
                        v += 1.0
                u += 1.0

    def DrawOverlay(self, e):
        if len(self.m_points) > 0:
            color = Rhino.ApplicationSettings.AppearanceSettings.TrackingColor
            for i in range(len(self.m_points)):
                if i % 100 == 0 and e.Display.InterruptDrawing():
                    break

                pt = self.m_points[i]
                dir = self.m_normals[i]
                if self.Flip:
                    dir.Reverse()
                e.Display.DrawDirectionArrow(pt, dir, color)

def RunCommand():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject(
        "Select surface or polysurface for direction display",
        False,
        Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter)
    if rc != Rhino.Commands.Result.Success:
        return rc

    brep = objref.Brep()
    if brep is None:
        return Rhino.Commands.Result.Failure

    bIsSolid = brep.IsSolid

    conduit = TestSurfaceDirConduit(brep)
    conduit.Enabled = True
    sc.doc.Views.Redraw()

    gf = Rhino.Input.Custom.GetOption()
    gf.SetCommandPrompt("Press enter when done")
    gf.AcceptNothing(True)
    if not bIsSolid:
        gf.AddOption("Flip")

    while True:
        res = gf.Get()
        if res == Rhino.Input.GetResult.Option:
            conduit.Flip = not conduit.Flip
            sc.doc.Views.Redraw()
            continue
        if res == Rhino.Input.GetResult.Nothing:
            if not bIsSolid and conduit.Flip:
                brep.Flip()
                sc.doc.Objects.Replace(objref, brep)
        break

    conduit.Enabled = False
    sc.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
