---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Interactively Pick an Angle
keywords: ['interactively', 'pick', 'angle']
categories: ['Picking and Selection']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result GetAngle(RhinoDoc doc)
  {
    var gp = new GetPoint();
    gp.SetCommandPrompt("Base point");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var base_point = gp.Point();

    gp.SetCommandPrompt("First reference point");
    gp.DrawLineFromPoint(base_point, true);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var first_point = gp.Point();

    double angle_radians;
    var rc = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0, out angle_radians);
    if (rc == Result.Success)
      RhinoApp.WriteLine("Angle = {0} degrees", RhinoMath.ToDegrees(angle_radians));

    return rc;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function GetAngle(ByVal doc As RhinoDoc) As Result
	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Base point")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim base_point = gp.Point()

	gp.SetCommandPrompt("First reference point")
	gp.DrawLineFromPoint(base_point, True)
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim first_point = gp.Point()

	Dim angle_radians As Double = Nothing
	Dim rc = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0, angle_radians)
	If rc Is Result.Success Then
	  RhinoApp.WriteLine("Angle = {0} degrees", RhinoMath.ToDegrees(angle_radians))
	End If

	Return rc
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *

def RunCommand():
  gp = GetPoint()
  gp.SetCommandPrompt("Base point")
  gp.Get()
  if gp.CommandResult() <> Result.Success:
    return gp.CommandResult()
  base_point = gp.Point()

  gp.SetCommandPrompt("First reference point")
  gp.DrawLineFromPoint(base_point, True)
  gp.Get()
  if gp.CommandResult() <> Result.Success:
    return gp.CommandResult()
  first_point = gp.Point()

  
  rc, angle_radians = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0)
  if rc == Result.Success:
    print "Angle = {0} degrees".format(RhinoMath.ToDegrees(angle_radians))
  return rc

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

