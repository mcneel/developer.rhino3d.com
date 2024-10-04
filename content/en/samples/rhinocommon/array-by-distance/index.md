+++
aliases = ["/en/5/samples/rhinocommon/array-by-distance/", "/en/6/samples/rhinocommon/array-by-distance/", "/en/7/samples/rhinocommon/array-by-distance/", "/wip/samples/rhinocommon/array-by-distance/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to array a user-selected object by specifying a start point and a contraint line."
keywords = [ "array", "distance", "command" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Array By Distance"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/arraybydistance"
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
  static double m_distance = 1;
  static Rhino.Geometry.Point3d m_point_start;
  public static Rhino.Commands.Result ArrayByDistance(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select object", true, Rhino.DocObjects.ObjectType.AnyObject, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    rc = Rhino.Input.RhinoGet.GetPoint("Start point", false, out m_point_start);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var obj = objref.Object();
    if (obj == null)
      return Rhino.Commands.Result.Failure;

    // create an instance of a GetPoint class and add a delegate
    // for the DynamicDraw event
    var gp = new Rhino.Input.Custom.GetPoint();
    gp.DrawLineFromPoint(m_point_start, true);
    var optdouble = new Rhino.Input.Custom.OptionDouble(m_distance);
    bool constrain = false;
    var optconstrain = new Rhino.Input.Custom.OptionToggle(constrain, "Off", "On");
    gp.AddOptionDouble("Distance", ref optdouble);
    gp.AddOptionToggle("Constrain", ref optconstrain);
    gp.DynamicDraw += ArrayByDistanceDraw;
    gp.Tag = obj;
    while (gp.Get() == Rhino.Input.GetResult.Option)
    {
      m_distance = optdouble.CurrentValue;
      if (constrain != optconstrain.CurrentValue)
      {
        constrain = optconstrain.CurrentValue;
        if (constrain)
        {
          var gp2 = new Rhino.Input.Custom.GetPoint();
          gp2.DrawLineFromPoint(m_point_start, true);
          gp2.SetCommandPrompt("Second point on constraint line");
          if (gp2.Get() == Rhino.Input.GetResult.Point)
            gp.Constrain(m_point_start, gp2.Point());
          else
          {
            gp.ClearCommandOptions();
            optconstrain.CurrentValue = false;
            constrain = false;
            gp.AddOptionDouble("Distance", ref optdouble);
            gp.AddOptionToggle("Constrain", ref optconstrain);
          }
        }
        else
        {
          gp.ClearConstraints();
        }
      }
    }

    if (gp.CommandResult() == Rhino.Commands.Result.Success)
    {
      m_distance = optdouble.CurrentValue;
      var pt = gp.Point();
      var vec = pt - m_point_start;
      double length = vec.Length;
      vec.Unitize();
      int count = (int)(length / m_distance);
      for (int i = 1; i < count; i++)
      {
        var translate = vec * (i * m_distance);
        var xf = Rhino.Geometry.Transform.Translation(translate);
        doc.Objects.Transform(obj, xf, false);
      }
      doc.Views.Redraw();
    }

    return gp.CommandResult();
  }

  // this function is called whenever the GetPoint's DynamicDraw
  // event occurs
  static void ArrayByDistanceDraw(object sender, Rhino.Input.Custom.GetPointDrawEventArgs e)
  {
    Rhino.DocObjects.RhinoObject rhobj = e.Source.Tag as Rhino.DocObjects.RhinoObject;
    if (rhobj == null)
      return;
    var vec = e.CurrentPoint - m_point_start;
    double length = vec.Length;
    vec.Unitize();
    int count = (int)(length / m_distance);
    for (int i = 1; i < count; i++)
    {
      var translate = vec * (i * m_distance);
      var xf = Rhino.Geometry.Transform.Translation(translate);
      e.Display.DrawObject(rhobj, xf);
    }
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Private Shared m_distance As Double = 1
  Private Shared m_point_start As Rhino.Geometry.Point3d
  Public Shared Function ArrayByDistance(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	rc = Rhino.Input.RhinoGet.GetPoint("Start point", False, m_point_start)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim obj = objref.Object()
	If obj Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	' create an instance of a GetPoint class and add a delegate
	' for the DynamicDraw event
	Dim gp = New Rhino.Input.Custom.GetPoint()
	gp.DrawLineFromPoint(m_point_start, True)
	Dim optdouble = New Rhino.Input.Custom.OptionDouble(m_distance)
	Dim constrain As Boolean = False
	Dim optconstrain = New Rhino.Input.Custom.OptionToggle(constrain, "Off", "On")
	gp.AddOptionDouble("Distance", optdouble)
	gp.AddOptionToggle("Constrain", optconstrain)
	AddHandler gp.DynamicDraw, AddressOf ArrayByDistanceDraw
	gp.Tag = obj
	Do While gp.Get() = Rhino.Input.GetResult.Option
	  m_distance = optdouble.CurrentValue
	  If constrain <> optconstrain.CurrentValue Then
		constrain = optconstrain.CurrentValue
		If constrain Then
		  Dim gp2 = New Rhino.Input.Custom.GetPoint()
		  gp2.DrawLineFromPoint(m_point_start, True)
		  gp2.SetCommandPrompt("Second point on constraint line")
		  If gp2.Get() = Rhino.Input.GetResult.Point Then
			gp.Constrain(m_point_start, gp2.Point())
		  Else
			gp.ClearCommandOptions()
			optconstrain.CurrentValue = False
			constrain = False
			gp.AddOptionDouble("Distance", optdouble)
			gp.AddOptionToggle("Constrain", optconstrain)
		  End If
		Else
		  gp.ClearConstraints()
		End If
	  End If
	Loop

	If gp.CommandResult() = Rhino.Commands.Result.Success Then
	  m_distance = optdouble.CurrentValue
	  Dim pt = gp.Point()
	  Dim vec = pt - m_point_start
	  Dim length As Double = vec.Length
	  vec.Unitize()
	  Dim count As Integer = CInt(Fix(length / m_distance))
	  For i As Integer = 1 To count - 1
		Dim translate = vec * (i * m_distance)
		Dim xf = Rhino.Geometry.Transform.Translation(translate)
		doc.Objects.Transform(obj, xf, False)
	  Next i
	  doc.Views.Redraw()
	End If

	Return gp.CommandResult()
  End Function

  ' this function is called whenever the GetPoint's DynamicDraw
  ' event occurs
  Private Shared Sub ArrayByDistanceDraw(ByVal sender As Object, ByVal e As Rhino.Input.Custom.GetPointDrawEventArgs)
	Dim rhobj As Rhino.DocObjects.RhinoObject = TryCast(e.Source.Tag, Rhino.DocObjects.RhinoObject)
	If rhobj Is Nothing Then
	  Return
	End If
	Dim vec = e.CurrentPoint - m_point_start
	Dim length As Double = vec.Length
	vec.Unitize()
	Dim count As Integer = CInt(Fix(length / m_distance))
	For i As Integer = 1 To count - 1
	  Dim translate = vec * (i * m_distance)
	  Dim xf = Rhino.Geometry.Transform.Translation(translate)
	  e.Display.DrawObject(rhobj, xf)
	Next i
  End Sub
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def dynamic_array():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select object", True, Rhino.DocObjects.ObjectType.AnyObject)
    if rc!=Rhino.Commands.Result.Success: return

    rc, pt_start = Rhino.Input.RhinoGet.GetPoint("Start point", False)
    if rc!=Rhino.Commands.Result.Success: return

    obj = objref.Object()
    if not obj: return

    dist = 1
    if scriptcontext.sticky.has_key("dynamic_array_distance"):
        dist = scriptcontext.sticky["dynamic_array_distance"]
    # This is a function that is called whenever the GetPoint's
    # DynamicDraw event occurs
    def ArrayByDistanceDraw( sender, args ):
        rhobj = args.Source.Tag
        if not rhobj: return
        vec = args.CurrentPoint - pt_start
        length = vec.Length
        vec.Unitize()
        count = int(length / dist)
        for i in range(1,count):
            translate = vec * (i*dist)
            xf = Rhino.Geometry.Transform.Translation(translate)
            args.Display.DrawObject(rhobj, xf)

    # Create an instance of a GetPoint class and add a delegate
    # for the DynamicDraw event
    gp = Rhino.Input.Custom.GetPoint()
    gp.DrawLineFromPoint(pt_start, True)
    optdouble = Rhino.Input.Custom.OptionDouble(dist)
    constrain = False
    optconstrain = Rhino.Input.Custom.OptionToggle(constrain,"Off", "On")
    gp.AddOptionDouble("Distance", optdouble)
    gp.AddOptionToggle("Constrain", optconstrain)
    gp.DynamicDraw += ArrayByDistanceDraw
    gp.Tag = obj
    while gp.Get()==Rhino.Input.GetResult.Option:
        dist = optdouble.CurrentValue
        if constrain!=optconstrain.CurrentValue:
            constrain = optconstrain.CurrentValue
            if constrain:
                gp2 = Rhino.Input.Custom.GetPoint()
                gp2.DrawLineFromPoint(pt_start, True)
                gp2.SetCommandPrompt("Second point on constraint line")
                if gp2.Get()==Rhino.Input.GetResult.Point:
                    gp.Constrain(pt_start, gp2.Point())
                else:
                    gp.ClearCommandOptions()
                    optconstrain.CurrentValue = False
                    constrain = False
                    gp.AddOptionDouble("Distance", optdouble)
                    gp.AddOptionToggle("Constrain", optconstrain)
            else:
                gp.ClearConstraints()
        continue
    if gp.CommandResult()==Rhino.Commands.Result.Success:
        scriptcontext.sticky["dynamic_array_distance"] = dist
        pt = gp.Point()
        vec = pt - pt_start
        length = vec.Length
        vec.Unitize()
        count = int(length / dist)
        for i in range(1, count):
            translate = vec * (i*dist)
            xf = Rhino.Geometry.Transform.Translation(translate)
            scriptcontext.doc.Objects.Transform(obj,xf,False)
        scriptcontext.doc.Views.Redraw()


if( __name__ == "__main__" ):
    dynamic_array()
```

</div>
