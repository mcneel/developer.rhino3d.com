+++
aliases = ["/en/5/samples/rhinocommon/hatch-curve/", "/en/6/samples/rhinocommon/hatch-curve/", "/en/7/samples/rhinocommon/hatch-curve/", "/wip/samples/rhinocommon/hatch-curve/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to create a hatch from a curve."
keywords = [ "creating", "hatch", "curve" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Hatch Curve"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/hatchcurve"
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
  public static Rhino.Commands.Result HatchCurve(Rhino.RhinoDoc doc)
  {
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select closed planar curve");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve;
    go.SubObjectSelect = false;
    go.Get();
    if( go.CommandResult() != Rhino.Commands.Result.Success )
      return go.CommandResult();

    var curve = go.Object(0).Curve();
    if( curve==null || !curve.IsClosed || !curve.IsPlanar() )
      return Rhino.Commands.Result.Failure;

    string hatch_name = doc.HatchPatterns[doc.HatchPatterns.CurrentHatchPatternIndex].Name;
    var rc = Rhino.Input.RhinoGet.GetString("Hatch pattern", true, ref hatch_name);
    if( rc!= Rhino.Commands.Result.Success )
      return rc;
    hatch_name = hatch_name.Trim();
    if( string.IsNullOrWhiteSpace(hatch_name) )
      return Rhino.Commands.Result.Nothing;
    int index = doc.HatchPatterns.Find(hatch_name, true);
    if( index < 0 )
    {
      Rhino.RhinoApp.WriteLine("Hatch pattern does not exist.");
      return Rhino.Commands.Result.Nothing;
    }

    var hatches = Rhino.Geometry.Hatch.Create( curve, index, 0, 1);
    for( int i=0; i<hatches.Length; i++ )
      doc.Objects.AddHatch(hatches[i]);
    if( hatches.Length>0 )
      doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function HatchCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go = New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select closed planar curve")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
	go.SubObjectSelect = False
	go.Get()
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	Dim curve = go.Object(0).Curve()
	If curve Is Nothing OrElse Not curve.IsClosed OrElse Not curve.IsPlanar() Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim hatch_name As String = doc.HatchPatterns(doc.HatchPatterns.CurrentHatchPatternIndex).Name
	Dim rc = Rhino.Input.RhinoGet.GetString("Hatch pattern", True, hatch_name)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	hatch_name = hatch_name.Trim()
	If String.IsNullOrWhiteSpace(hatch_name) Then
	  Return Rhino.Commands.Result.Nothing
	End If
	Dim index As Integer = doc.HatchPatterns.Find(hatch_name, True)
	If index < 0 Then
	  Rhino.RhinoApp.WriteLine("Hatch pattern does not exist.")
	  Return Rhino.Commands.Result.Nothing
	End If

	Dim hatches = Rhino.Geometry.Hatch.Create(curve, index, 0, 1)
	For i As Integer = 0 To hatches.Length - 1
	  doc.Objects.AddHatch(hatches(i))
	Next i
	If hatches.Length>0 Then
	  doc.Views.Redraw()
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def HatchCurve():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select closed planar curve")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
    go.SubObjectSelect = False
    go.Get()
    if go.CommandResult()!=Rhino.Commands.Result.Success: return

    curve = go.Object(0).Curve()
    if (not curve or not curve.IsClosed or not curve.IsPlanar()): return

    hatch_name = scriptcontext.doc.HatchPatterns[scriptcontext.doc.HatchPatterns.CurrentHatchPatternIndex].Name
    rc, hatch_name = Rhino.Input.RhinoGet.GetString("Hatch pattern", True, hatch_name)
    if rc!=Rhino.Commands.Result.Success or not hatch_name: return

    index = scriptcontext.doc.HatchPatterns.Find(hatch_name, True)
    if index<0:
        print "Hatch pattern does not exist."
        return

    hatches = Rhino.Geometry.Hatch.Create(curve, index, 0, 1)
    for hatch in hatches:
        scriptcontext.doc.Objects.AddHatch(hatch)
    if hatches: scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    HatchCurve()
```

</div>
