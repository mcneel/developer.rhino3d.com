---
title: Box Shell
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Other']
origin: unset
order: 1
keywords: ['shell']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result BoxShell(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Box box;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
    if (rc == Rhino.Commands.Result.Success)
    {
      Rhino.Geometry.Brep brep = Rhino.Geometry.Brep.CreateFromBox(box);
      if (null != brep)
      {
        System.Collections.Generic.List<int> facesToRemove = new System.Collections.Generic.List<int>(1);
        facesToRemove.Add(0);
        Rhino.Geometry.Brep[] shells = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance);
        if (null != shells)
        {
          for (int i = 0; i < shells.Length; i++)
            doc.Objects.AddBrep(shells[i]);
          doc.Views.Redraw();
        }
      }
    }
    return rc;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function BoxShell(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim box As Rhino.Geometry.Box = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetBox(box)
	If rc Is Rhino.Commands.Result.Success Then
	  Dim brep As Rhino.Geometry.Brep = Rhino.Geometry.Brep.CreateFromBox(box)
	  If Nothing IsNot brep Then
		Dim facesToRemove As New System.Collections.Generic.List(Of Integer)(1)
		facesToRemove.Add(0)
		Dim shells() As Rhino.Geometry.Brep = Rhino.Geometry.Brep.CreateShell(brep, facesToRemove, 1.0, doc.ModelAbsoluteTolerance)
		If Nothing IsNot shells Then
		  For i As Integer = 0 To shells.Length - 1
			doc.Objects.AddBrep(shells(i))
		  Next i
		  doc.Views.Redraw()
		End If
	  End If
	End If
	Return rc
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

