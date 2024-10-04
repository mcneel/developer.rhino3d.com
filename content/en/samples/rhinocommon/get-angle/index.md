+++
aliases = ["/en/5/samples/rhinocommon/get-angle/", "/en/6/samples/rhinocommon/get-angle/", "/en/7/samples/rhinocommon/get-angle/", "/wip/samples/rhinocommon/get-angle/"]
authors = [ "steve" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to interactively pick an angle given a base point and two reference points."
keywords = [ "interactively", "pick", "angle" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Get Angle"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/getangle"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *

def RunCommand():
    gp = GetPoint()
    gp.SetCommandPrompt("Base point")
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    base_point = gp.Point()

    gp.SetCommandPrompt("First reference point")
    gp.DrawLineFromPoint(base_point, True)
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    first_point = gp.Point()


    rc, angle_radians = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0)
    if rc == Result.Success:
        print "Angle = {0} degrees".format(RhinoMath.ToDegrees(angle_radians))
    return rc

if __name__ == "__main__":
    RunCommand()
```

</div>
