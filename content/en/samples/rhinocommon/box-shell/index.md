+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to give thickness to (or shell) a Brep box."
keywords = [ "shell" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Box Shell"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

