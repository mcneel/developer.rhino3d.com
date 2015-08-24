---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Extracting Isoparametric Curves from Surfaces
keywords: ['extracting', 'isoparametric', 'curves', 'surfaces']
categories: ['Curves']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result ExtractIsoCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select surface", false, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success || obj_ref == null)
      return rc;
    var surface = obj_ref.Surface();

    var gp = new GetPoint();
    gp.SetCommandPrompt("Point on surface");
    gp.Constrain(surface, false);
    var option_toggle = new OptionToggle(false, "U", "V");
    gp.AddOptionToggle("Direction", ref option_toggle);
    Point3d point = Point3d.Unset;
    while (true)
    {
      var grc = gp.Get();
      if (grc == GetResult.Option)
        continue;
      else if (grc == GetResult.Point)
      {
        point = gp.Point();
        break;
      }
      else
        return Result.Nothing;
    }
    if (point == Point3d.Unset)
      return Result.Nothing;

    int direction = option_toggle.CurrentValue ? 1 : 0; // V : U
    double u_parameter, v_parameter;
    if (!surface.ClosestPoint(point, out u_parameter, out v_parameter)) return Result.Failure;

    var iso_curve = surface.IsoCurve(direction, direction == 1 ? u_parameter : v_parameter);
    if (iso_curve == null) return Result.Failure;

    doc.Objects.AddCurve(iso_curve);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ExtractIsoCurve(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface, obj_ref)
	If rc IsNot Result.Success OrElse obj_ref Is Nothing Then
	  Return rc
	End If
	Dim surface = obj_ref.Surface()

	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Point on surface")
	gp.Constrain(surface, False)
	Dim option_toggle = New OptionToggle(False, "U", "V")
	gp.AddOptionToggle("Direction", option_toggle)
	Dim point As Point3d = Point3d.Unset
	Do
	  Dim grc = gp.Get()
	  If grc Is GetResult.Option Then
		Continue Do
	  ElseIf grc Is GetResult.Point Then
		point = gp.Point()
		Exit Do
	  Else
		Return Result.Nothing
	  End If
	Loop
	If point Is Point3d.Unset Then
	  Return Result.Nothing
	End If

	Dim direction As Integer = If(option_toggle.CurrentValue, 1, 0) ' V : U
	Dim u_parameter As Double = Nothing, v_parameter As Double = Nothing
	If Not surface.ClosestPoint(point, u_parameter, v_parameter) Then
		Return Result.Failure
	End If

	Dim iso_curve = surface.IsoCurve(direction,If(direction = 1, u_parameter, v_parameter))
	If iso_curve Is Nothing Then
		Return Result.Failure
	End If

	doc.Objects.AddCurve(iso_curve)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject(
    "Select surface", False, ObjectType.Surface)
  if rc <> Result.Success or obj_ref == None:
    return rc
  surface = obj_ref.Surface()

  gp = GetPoint()
  gp.SetCommandPrompt("Point on surface")
  gp.Constrain(surface, False)
  option_toggle = OptionToggle(False, "U", "V")
  gp.AddOptionToggle("Direction", option_toggle)
  point = Point3d.Unset

  while True:
    grc = gp.Get()
    if grc == GetResult.Option:
      continue
    elif grc == GetResult.Point:
      point = gp.Point()
      break
    else:
      return Result.Nothing

  if point == Point3d.Unset:
    return Result.Nothing

  direction = 1 if option_toggle.CurrentValue else 0
  b, u_parameter, v_parameter = surface.ClosestPoint(point)
  if not b: return Result.Failure

  iso_curve = surface.IsoCurve(
    direction, u_parameter if direction == 1 else v_parameter)
  if iso_curve == None: 
    return Result.Failure

  doc.Objects.AddCurve(iso_curve)
  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in .active}

