+++
aliases = ["/en/5/samples/rhinocommon/add-mesh-box/", "/en/6/samples/rhinocommon/add-mesh-box/", "/en/7/samples/rhinocommon/add-mesh-box/", "/wip/samples/rhinocommon/add-mesh-box/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a mesh box from a Brep box."
keywords = [ "add", "mesh" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Mesh Box"
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
  public static Rhino.Commands.Result AddMeshBox(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Box box;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
    if (rc == Rhino.Commands.Result.Success)
    {
      Rhino.Geometry.Mesh mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2);
      if (null != mesh)
      {
        doc.Objects.AddMesh(mesh);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }

    return Rhino.Commands.Result.Failure;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddMeshBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim box As Rhino.Geometry.Box = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetBox(box)
	If rc Is Rhino.Commands.Result.Success Then
	  Dim mesh As Rhino.Geometry.Mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2)
	  If Nothing IsNot mesh Then
		doc.Objects.AddMesh(mesh)
		doc.Views.Redraw()
		Return Rhino.Commands.Result.Success
	  End If
	End If

	Return Rhino.Commands.Result.Failure
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

