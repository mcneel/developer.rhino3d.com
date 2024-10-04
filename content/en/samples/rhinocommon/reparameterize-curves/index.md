+++
aliases = ["/en/5/samples/rhinocommon/reparameterize-curves/", "/en/6/samples/rhinocommon/reparameterize-curves/", "/en/7/samples/rhinocommon/reparameterize-curves/", "/wip/samples/rhinocommon/reparameterize-curves/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to reparameterize - or change the domain of - user-specified curves."
keywords = [ "reparamemterize", "curve" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Reparameterize Curves"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/reparameterizecrv"
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
  public static Result ReparameterizeCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select curve to reparameterize", false, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Failure;

    double domain_start = 0;
    rc = RhinoGet.GetNumber("Domain start", false, ref domain_start);
    if (rc != Result.Success)
      return rc;

    double domain_end = 0;
    rc = RhinoGet.GetNumber("Domain end", false, ref domain_end);
    if (rc != Result.Success)
      return rc;

    if (Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance &&
        Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance)
      return Result.Nothing;

    var curve_copy = curve.DuplicateCurve();
    curve_copy.Domain = new Interval(domain_start, domain_end);
    if (!doc.Objects.Replace(obj_ref, curve_copy))
      return Result.Failure;
    else
    {
      doc.Views.Redraw();
      return Result.Success;
    }
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ReparameterizeCurve(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select curve to reparameterize", False, ObjectType.Curve, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim curve = obj_ref.Curve()
	If curve Is Nothing Then
	  Return Result.Failure
	End If

	Dim domain_start As Double = 0
	rc = RhinoGet.GetNumber("Domain start", False, domain_start)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	Dim domain_end As Double = 0
	rc = RhinoGet.GetNumber("Domain end", False, domain_end)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	If Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance AndAlso Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance Then
	  Return Result.Nothing
	End If

	Dim curve_copy = curve.DuplicateCurve()
	curve_copy.Domain = New Interval(domain_start, domain_end)
	If Not doc.Objects.Replace(obj_ref, curve_copy) Then
	  Return Result.Failure
	Else
	  doc.Views.Redraw()
	  Return Result.Success
	End If
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from System import *
from  Rhino import *
from  Rhino.Commands import *
from  Rhino.DocObjects import *
from  Rhino.Geometry import *
from  Rhino.Input import *
from scriptcontext import doc

def RunCommand():

    rc, obj_ref = RhinoGet.GetOneObject("Select curve to reparameterize", False, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve = obj_ref.Curve()
    if curve == None:
        return Result.Failure

    domain_start = 0
    rc, domain_start = RhinoGet.GetNumber("Domain start", False, domain_start)
    if rc != Result.Success:
        return rc

    domain_end = 100
    rc, domain_end = RhinoGet.GetNumber("Domain end", False, domain_end)
    if rc != Result.Success:
        return rc

    if Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance and \
        Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance:
        return Result.Nothing

    curve_copy = curve.DuplicateCurve()
    curve_copy.Domain = Interval(domain_start, domain_end)
    if not doc.Objects.Replace(obj_ref, curve_copy):
        return Result.Failure
    else:
        doc.Views.Redraw()
        return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
