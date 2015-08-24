---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Show Surface Direction
keywords: ['show', 'surface', 'direction']
categories: ['Other']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ShowSurfaceDirection(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface for direction display", False, Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim brep = objref.Brep()
	If brep Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim bIsSolid As Boolean = brep.IsSolid

	Dim conduit As New TestSurfaceDirConduit(brep)
	conduit.Enabled = True
	doc.Views.Redraw()

	Dim gf = New Rhino.Input.Custom.GetOption()
	gf.SetCommandPrompt("Press enter when done")
	gf.AcceptNothing(True)
	If Not bIsSolid Then
	  gf.AddOption("Flip")
	End If

	Do
	  Dim res = gf.Get()
	  If res Is Rhino.Input.GetResult.Option Then
		conduit.Flip = Not conduit.Flip
		doc.Views.Redraw()
		Continue Do
	  End If
	  If res Is Rhino.Input.GetResult.Nothing Then
		If Not bIsSolid AndAlso conduit.Flip Then
		  brep.Flip()
		  doc.Objects.Replace(objref, brep)
		End If
	  End If
	  Exit Do
	Loop

	conduit.Enabled = False
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class

Friend Class TestSurfaceDirConduit
	Inherits Rhino.Display.DisplayConduit

  Private ReadOnly m_brep As Brep
  Private ReadOnly m_points As List(Of Point3d)
  Private ReadOnly m_normals As List(Of Vector3d)

  Public Sub New(ByVal brep As Brep)
	m_brep = brep
	Flip = False

	Const SURFACE_ARROW_COUNT As Integer = 5
	Dim face_count As Integer = m_brep.Faces.Count
	Dim capacity As Integer = face_count * SURFACE_ARROW_COUNT * SURFACE_ARROW_COUNT
	m_points = New List(Of Point3d)(capacity)
	m_normals = New List(Of Vector3d)(capacity)

	For i As Integer = 0 To face_count - 1
	  Dim face = brep.Faces(i)
	  Dim [loop] = face.OuterLoop
	  If [loop] Is Nothing Then
		Continue For
	  End If

	  Dim udomain = face.Domain(0)
	  Dim vdomain = face.Domain(1)
	  Dim loop_bbox = [loop].GetBoundingBox(True)
	  If loop_bbox.IsValid Then
		Dim domain As New Interval(loop_bbox.Min.X, loop_bbox.Max.X)
		domain = Interval.FromIntersection(domain, udomain)
		If domain.IsIncreasing Then
		  udomain = domain
		End If
		domain = New Interval(loop_bbox.Min.Y, loop_bbox.Max.Y)
		domain = Interval.FromIntersection(domain, vdomain)
		If domain.IsIncreasing Then
		  vdomain = domain
		End If
	  End If

	  Dim bUntrimmed As Boolean = face.IsSurface
	  Dim bRev As Boolean = face.OrientationIsReversed
	  For u As Double = 0 To SURFACE_ARROW_COUNT - 1 Step 1.0
		Dim d As Double = u / (SURFACE_ARROW_COUNT - 1.0)
		Dim s As Double = udomain.ParameterAt(d)

		Dim intervals = face.TrimAwareIsoIntervals(1, s)
		If bUntrimmed OrElse intervals.Length > 0 Then
		  For v As Double = 0 To SURFACE_ARROW_COUNT - 1 Step 1.0
			d = v / (SURFACE_ARROW_COUNT - 1.0)
			Dim t As Double = vdomain.ParameterAt(d)
			Dim bAdd As Boolean = bUntrimmed
			Dim k As Integer = 0
			Do While Not bAdd AndAlso k < intervals.Length
			  If intervals(k).IncludesParameter(t) Then
				bAdd = True
			  End If
				k += 1
			Loop
			If bAdd Then
			  Dim pt = face.PointAt(s, t)
			  Dim vec = face.NormalAt(s, t)
			  m_points.Add(pt)
			  If bRev Then
				vec.Reverse()
			  End If
			  m_normals.Add(vec)
			End If
		  Next v
		End If
	  Next u
	Next i
  End Sub

  Public Property Flip() As Boolean

  Protected Overrides Sub DrawOverlay(ByVal e As Rhino.Display.DrawEventArgs)
	If m_points.Count > 0 Then
	  Dim color = Rhino.ApplicationSettings.AppearanceSettings.TrackingColor
	  For i As Integer = 0 To m_points.Count - 1
		If i Mod 100 = 0 AndAlso e.Display.InterruptDrawing() Then
		  Exit For
		End If

		Dim pt = m_points(i)
		Dim dir = m_normals(i)
		If Flip Then
		  dir.Reverse()
		End If
		e.Display.DrawDirectionArrow(pt, dir, color)
	  Next i
	End If
  End Sub
End Class
```
{: #vb .tab-pane .fade .in .active}

