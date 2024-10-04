+++
aliases = ["/en/5/samples/rhinocommon/circle-center/", "/en/6/samples/rhinocommon/circle-center/", "/en/7/samples/rhinocommon/circle-center/", "/wip/samples/rhinocommon/circle-center/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to find the center of a circle."
keywords = [ "find", "circles", "their", "centers" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Circle Center"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/circlecenter"
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
  public static Rhino.Commands.Result CircleCenter(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select objects");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve;
    go.GetMultiple(1, 0);
    if( go.CommandResult() != Rhino.Commands.Result.Success )
      return go.CommandResult();

    Rhino.DocObjects.ObjRef[] objrefs = go.Objects();
    if( objrefs==null )
      return Rhino.Commands.Result.Nothing;

    double tolerance = doc.ModelAbsoluteTolerance;
    for( int i=0; i<objrefs.Length; i++ )
    {
      // get the curve geometry
      Rhino.Geometry.Curve curve = objrefs[i].Curve();
      if( curve==null )
        continue;
      Rhino.Geometry.Circle circle;
      if( curve.TryGetCircle(out circle, tolerance) )
      {
        Rhino.RhinoApp.WriteLine("Circle{0}: center = {1}", i+1, circle.Center);
      }
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function CircleCenter(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select objects")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
	go.GetMultiple(1, 0)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	Dim objrefs() As Rhino.DocObjects.ObjRef = go.Objects()
	If objrefs Is Nothing Then
	  Return Rhino.Commands.Result.Nothing
	End If

	Dim tolerance As Double = doc.ModelAbsoluteTolerance
	For i As Integer = 0 To objrefs.Length - 1
	  ' get the curve geometry
	  Dim curve As Rhino.Geometry.Curve = objrefs(i).Curve()
	  If curve Is Nothing Then
		Continue For
	  End If
	  Dim circle As Rhino.Geometry.Circle = Nothing
	  If curve.TryGetCircle(circle, tolerance) Then
		Rhino.RhinoApp.WriteLine("Circle{0}: center = {1}", i+1, circle.Center)
	  End If
	Next i
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def CircleCenter():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select objects")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
    go.GetMultiple(1, 0)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()

    objrefs = go.Objects()
    if not objrefs: return Rhino.Commands.Result.Nothing

    tolerance = scriptcontext.doc.ModelAbsoluteTolerance
    for i, objref in enumerate(objrefs):
        # get the curve geometry
        curve = objref.Curve()
        if not curve: continue
        rc, circle = curve.TryGetCircle( tolerance )
        if rc:
            print "Circle", i+1, ": center = ", circle.Center
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    CircleCenter()
```

</div>
