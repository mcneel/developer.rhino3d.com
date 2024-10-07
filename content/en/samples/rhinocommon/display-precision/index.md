+++
aliases = ["/en/5/samples/rhinocommon/display-precision/", "/en/6/samples/rhinocommon/display-precision/", "/en/7/samples/rhinocommon/display-precision/", "/en/wip/samples/rhinocommon/display-precision/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to change the display precision in a Rhino model."
keywords = [ "changing", "display", "precision" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Display Precision"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/displayprecision"
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
  public static Result DisplayPrecision(RhinoDoc doc)
  {
    var gi = new GetInteger();
    gi.SetCommandPrompt("New display precision");
    gi.SetDefaultInteger(doc.ModelDistanceDisplayPrecision);
    gi.SetLowerLimit(0, false);
    gi.SetUpperLimit(7, false);
    gi.Get();
    if (gi.CommandResult() != Result.Success)
      return gi.CommandResult();
    var distance_display-precision = gi.Number();

    if (distance_display-precision != doc.ModelDistanceDisplayPrecision)
      doc.ModelDistanceDisplayPrecision = distance_display-precision;

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DisplayPrecision(ByVal doc As RhinoDoc) As Result
	Dim gi = New GetInteger()
	gi.SetCommandPrompt("New display precision")
	gi.SetDefaultInteger(doc.ModelDistanceDisplayPrecision)
	gi.SetLowerLimit(0, False)
	gi.SetUpperLimit(7, False)
	gi.Get()
	If gi.CommandResult() <> Result.Success Then
	  Return gi.CommandResult()
	End If
	Dim distance_display-precision = gi.Number()

	If distance_display-precision IsNot doc.ModelDistanceDisplayPrecision Then
	  doc.ModelDistanceDisplayPrecision = distance_display-precision
	End If

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Input.Custom import *
from Rhino.Commands import *
from scriptcontext import doc
import rhinoscriptsyntax as rs

def RunCommand():
    distance_display-precision = rs.GetInteger("Display precision",
        doc.ModelDistanceDisplayPrecision, 0, 7)
    if distance_display-precision == None: return Result.Nothing

    if distance_display-precision != doc.ModelDistanceDisplayPrecision:
        doc.ModelDistanceDisplayPrecision = distance_display-precision

    return Result.Success

if __name__ ==  "__main__":
    RunCommand()
```

</div>
