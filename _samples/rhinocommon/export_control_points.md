---
title: Export Control Points
description: Demonstrates how to export the control points of a user-selected curve and write them to a file.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: unset
order: 1
keywords: ['export', 'control', 'points']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result ExportControlPoints(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var get_rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", false, Rhino.DocObjects.ObjectType.Curve, out objref);
    if (get_rc != Rhino.Commands.Result.Success)
      return get_rc;
    var curve = objref.Curve();
    if (curve == null)
      return Rhino.Commands.Result.Failure;
    var nc = curve.ToNurbsCurve();

    var fd = new SaveFileDialog();
    //fd.Filters = "Text Files | *.txt";
    //fd.Filter = "Text Files | *.txt";
    //fd.DefaultExt = "txt";
    //if( fd.ShowDialog(Rhino.RhinoApp.MainWindow())!= System.Windows.Forms.DialogResult.OK)
    if (fd.ShowDialog(null) != DialogResult.Ok)
      return Rhino.Commands.Result.Cancel;
    string path = fd.FileName;
    using( System.IO.StreamWriter sw = new System.IO.StreamWriter(path) )
    {
      foreach( var pt in nc.Points )
      {
        var loc = pt.Location;
        sw.WriteLine("{0} {1} {2}", loc.X, loc.Y, loc.Z);
      }
      sw.Close();
    }
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ExportControlPoints(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim get_rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve, objref)
	If get_rc IsNot Rhino.Commands.Result.Success Then
	  Return get_rc
	End If
	Dim curve = objref.Curve()
	If curve Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If
	Dim nc = curve.ToNurbsCurve()

	Dim fd = New SaveFileDialog()
	'fd.Filters = "Text Files | *.txt";
	'fd.Filter = "Text Files | *.txt";
	'fd.DefaultExt = "txt";
	'if( fd.ShowDialog(Rhino.RhinoApp.MainWindow())!= System.Windows.Forms.DialogResult.OK)
	If fd.ShowDialog(Nothing) <> DialogResult.Ok Then
	  Return Rhino.Commands.Result.Cancel
	End If
	Dim path As String = fd.FileName
	Using sw As New System.IO.StreamWriter(path)
	  For Each pt In nc.Points
		Dim loc = pt.Location
		sw.WriteLine("{0} {1} {2}", loc.X, loc.Y, loc.Z)
	  Next pt
	  sw.Close()
	End Using
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

