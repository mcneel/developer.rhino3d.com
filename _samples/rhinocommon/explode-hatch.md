---
title: Explode Hatch
description: Demonstrates how to explode a user-specified hatch object into its constituent parts (curves, points, etc.)
authors: ['steve_baer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/explodehatch
order: 1
keywords: ['explode', 'hatch']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result ExplodeHatch(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Hatch;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.Geometry.Hatch hatch = objref.Geometry() as Rhino.Geometry.Hatch;
    if (null == hatch)
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.GeometryBase[] hatch_geom = hatch.Explode();
    if (null != hatch_geom)
    {
      for (int i = 0; i < hatch_geom.Length; i++)
      {
        Rhino.Geometry.GeometryBase geom = hatch_geom[i];
        if (null != geom)
        {
          switch (geom.ObjectType)
          {
            case Rhino.DocObjects.ObjectType.Point:
              {
                Rhino.Geometry.Point point = geom as Rhino.Geometry.Point;
                if (null != point)
                  doc.Objects.AddPoint(point.Location);
              }
              break;
            case Rhino.DocObjects.ObjectType.Curve:
              {
                Rhino.Geometry.Curve curve = geom as Rhino.Geometry.Curve;
                if (null != curve)
                  doc.Objects.AddCurve(curve);
              }
              break;
            case Rhino.DocObjects.ObjectType.Brep:
              {
                Rhino.Geometry.Brep brep = geom as Rhino.Geometry.Brep;
                if (null != brep)
                  doc.Objects.AddBrep(brep);
              }
              break;
          }
        }
      }
    }

    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ExplodeHatch(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Hatch
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success OrElse objref Is Nothing Then
	  Return rc
	End If

	Dim hatch As Rhino.Geometry.Hatch = TryCast(objref.Geometry(), Rhino.Geometry.Hatch)
	If Nothing Is hatch Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim hatch_geom() As Rhino.Geometry.GeometryBase = hatch.Explode()
	If Nothing IsNot hatch_geom Then
	  For i As Integer = 0 To hatch_geom.Length - 1
		Dim geom As Rhino.Geometry.GeometryBase = hatch_geom(i)
		If Nothing IsNot geom Then
		  Select Case geom.ObjectType
			Case Rhino.DocObjects.ObjectType.Point
				Dim point As Rhino.Geometry.Point = TryCast(geom, Rhino.Geometry.Point)
				If Nothing IsNot point Then
				  doc.Objects.AddPoint(point.Location)
				End If
			Case Rhino.DocObjects.ObjectType.Curve
				Dim curve As Rhino.Geometry.Curve = TryCast(geom, Rhino.Geometry.Curve)
				If Nothing IsNot curve Then
				  doc.Objects.AddCurve(curve)
				End If
			Case Rhino.DocObjects.ObjectType.Brep
				Dim brep As Rhino.Geometry.Brep = TryCast(geom, Rhino.Geometry.Brep)
				If Nothing IsNot brep Then
				  doc.Objects.AddBrep(brep)
				End If
		  End Select
		End If
	  Next i
	End If

	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def ExplodeHatch():
    filter = Rhino.DocObjects.ObjectType.Hatch
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", False, filter)
    if rc != Rhino.Commands.Result.Success: return

    hatch = objref.Geometry()
    if not hatch: return

    hatch_geom = hatch.Explode()
    if hatch_geom:
        for geom in hatch_geom:
            if geom.ObjectType == Rhino.DocObjects.ObjectType.Point:
                scriptcontext.doc.Objects.AddPoint(geom)
            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Curve:
                scriptcontext.doc.Objects.AddCurve(geom)
            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Brep:
                scriptcontext.doc.Objects.AddBrep(geom)
        scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    ExplodeHatch()
```
{: #py .tab-pane .fade .in}
