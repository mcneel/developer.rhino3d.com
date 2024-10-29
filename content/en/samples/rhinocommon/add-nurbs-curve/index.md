+++
aliases = ["/en/5/samples/rhinocommon/add-nurbs-curve/", "/en/6/samples/rhinocommon/add-nurbs-curve/", "/en/7/samples/rhinocommon/add-nurbs-curve/", "/en/wip/samples/rhinocommon/add-nurbs-curve/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Curves" ]
description = "Demonstrates how to create a NURBS curve from a list of points."
keywords = [ "add", "nurbs", "curve" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add NURBS Curve"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addnurbscurve"
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
  public static Rhino.Commands.Result AddNurbsCurve(Rhino.RhinoDoc doc)
  {
    Rhino.Collections.Point3dList points = new Rhino.Collections.Point3dList(5);
    points.Add(0, 0, 0);
    points.Add(0, 2, 0);
    points.Add(2, 3, 0);
    points.Add(4, 2, 0);
    points.Add(4, 0, 0);
    Rhino.Geometry.NurbsCurve nc = Rhino.Geometry.NurbsCurve.Create(false, 3, points);
    Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
    if (nc != null && nc.IsValid)
    {
      if (doc.Objects.AddCurve(nc) != Guid.Empty)
      {
        doc.Views.Redraw();
        rc = Rhino.Commands.Result.Success;
      }
    }
    return rc;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddNurbsCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim points As New Rhino.Collections.Point3dList(5)
	points.Add(0, 0, 0)
	points.Add(0, 2, 0)
	points.Add(2, 3, 0)
	points.Add(4, 2, 0)
	points.Add(4, 0, 0)
	Dim nc As Rhino.Geometry.NurbsCurve = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
	If nc IsNot Nothing AndAlso nc.IsValid Then
	  If doc.Objects.AddCurve(nc) <> Guid.Empty Then
		doc.Views.Redraw()
		rc = Rhino.Commands.Result.Success
	  End If
	End If
	Return rc
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddNurbsCurve():
    points = Rhino.Collections.Point3dList(5)
    points.Add(0, 0, 0)
    points.Add(0, 2, 0)
    points.Add(2, 3, 0)
    points.Add(4, 2, 0)
    points.Add(4, 0, 0)

    nc = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
    rc = Rhino.Commands.Result.Failure
    if nc and nc.IsValid:
        if scriptcontext.doc.Objects.AddCurve(nc)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            rc = Rhino.Commands.Result.Success
    return rc

if __name__=="__main__":
    AddNurbsCurve()
```

</div>
