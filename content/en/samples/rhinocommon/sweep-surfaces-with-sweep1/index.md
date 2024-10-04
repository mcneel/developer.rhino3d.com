+++
aliases = ["/en/5/samples/rhinocommon/sweep-surfaces-with-sweep1/", "/en/6/samples/rhinocommon/sweep-surfaces-with-sweep1/", "/en/7/samples/rhinocommon/sweep-surfaces-with-sweep1/", "/wip/samples/rhinocommon/sweep-surfaces-with-sweep1/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to sweep along a single rail curve."
keywords = [ "sweeping", "surfaces", "using", "sweep1" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Sweep Surfaces with Sweep1"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/sweep1"
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
  public static Rhino.Commands.Result Sweep1(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef rail_ref;
    var rc = RhinoGet.GetOneObject("Select rail curve", false, Rhino.DocObjects.ObjectType.Curve, out rail_ref);
    if(rc!=Rhino.Commands.Result.Success)
      return rc;

    var rail_crv = rail_ref.Curve();
    if( rail_crv==null )
      return Rhino.Commands.Result.Failure;

    var gx = new Rhino.Input.Custom.GetObject();
    gx.SetCommandPrompt("Select cross section curves");
    gx.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    gx.EnablePreSelect(false, true);
    gx.GetMultiple(1,0);
    if( gx.CommandResult() != Rhino.Commands.Result.Success )
      return gx.CommandResult();

    var cross_sections = new List<Rhino.Geometry.Curve>();
    for( int i=0; i<gx.ObjectCount; i++ )
    {
      var crv = gx.Object(i).Curve();
      if( crv!= null)
        cross_sections.Add(crv);
    }
    if( cross_sections.Count<1 )
      return Rhino.Commands.Result.Failure;

    var sweep = new Rhino.Geometry.SweepOneRail();
    sweep.AngleToleranceRadians = doc.ModelAngleToleranceRadians;
    sweep.ClosedSweep = false;
    sweep.SweepTolerance = doc.ModelAbsoluteTolerance;
    sweep.SetToRoadlikeTop();
    var breps = sweep.PerformSweep(rail_crv, cross_sections);
    for( int i=0; i<breps.Length; i++ )
      doc.Objects.AddBrep(breps[i]);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function Sweep1(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim rail_ref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select rail curve", False, Rhino.DocObjects.ObjectType.Curve, rail_ref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim rail_crv = rail_ref.Curve()
	If rail_crv Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim gx = New Rhino.Input.Custom.GetObject()
	gx.SetCommandPrompt("Select cross section curves")
	gx.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	gx.EnablePreSelect(False, True)
	gx.GetMultiple(1,0)
	If gx.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gx.CommandResult()
	End If

	Dim cross_sections = New List(Of Rhino.Geometry.Curve)()
	For i As Integer = 0 To gx.ObjectCount - 1
	  Dim crv = gx.Object(i).Curve()
	  If crv IsNot Nothing Then
		cross_sections.Add(crv)
	  End If
	Next i
	If cross_sections.Count<1 Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim sweep = New Rhino.Geometry.SweepOneRail()
	sweep.AngleToleranceRadians = doc.ModelAngleToleranceRadians
	sweep.ClosedSweep = False
	sweep.SweepTolerance = doc.ModelAbsoluteTolerance
	sweep.SetToRoadlikeTop()
	Dim breps = sweep.PerformSweep(rail_crv, cross_sections)
	For i As Integer = 0 To breps.Length - 1
	  doc.Objects.AddBrep(breps(i))
	Next i
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext

def Sweep1():
    rail = rs.GetObject("Select rail curve", rs.filter.curve)
    rail_crv = rs.coercecurve(rail)
    if not rail_crv: return

    cross_sections = rs.GetObjects("Select cross section curves", rs.filter.curve)
    if not cross_sections: return
    cross_sections = [rs.coercecurve(crv) for crv in cross_sections]

    sweep = Rhino.Geometry.SweepOneRail()
    sweep.AngleToleranceRadians = scriptcontext.doc.ModelAngleToleranceRadians
    sweep.ClosedSweep = False
    sweep.SweepTolerance = scriptcontext.doc.ModelAbsoluteTolerance
    sweep.SetToRoadlikeTop()
    breps = sweep.PerformSweep(rail_crv, cross_sections)
    for brep in breps: scriptcontext.doc.Objects.AddBrep(brep)
    scriptcontext.doc.Views.Redraw()

if __name__ == "__main__":
    Sweep1()
```

</div>
