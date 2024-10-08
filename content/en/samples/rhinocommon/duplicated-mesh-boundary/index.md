+++
aliases = ["/en/5/samples/rhinocommon/duplicated-mesh-boundary/", "/en/6/samples/rhinocommon/duplicated-mesh-boundary/", "/en/7/samples/rhinocommon/duplicated-mesh-boundary/", "/en/wip/samples/rhinocommon/duplicated-mesh-boundary/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a bounding polyline from naked edges of an open mesh."
keywords = [ "bounding", "polyline", "naked", "edges", "open", "mesh" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Duplicate Mesh Boundary"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/dupmeshboundary"
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
  public static Result DupMeshBoundary(RhinoDoc doc)
  {
    var gm = new GetObject();
    gm.SetCommandPrompt("Select open mesh");
    gm.GeometryFilter = ObjectType.Mesh;
    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh;
    gm.Get();
    if (gm.CommandResult() != Result.Success)
      return gm.CommandResult();
    var mesh = gm.Object(0).Mesh();
    if (mesh == null)
      return Result.Failure;

    var polylines = mesh.GetNakedEdges();
    foreach (var polyline in polylines)
    {
      doc.Objects.AddPolyline(polyline);
    }

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DupMeshBoundary(ByVal doc As RhinoDoc) As Result
	Dim gm = New GetObject()
	gm.SetCommandPrompt("Select open mesh")
	gm.GeometryFilter = ObjectType.Mesh
	gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
	gm.Get()
	If gm.CommandResult() <> Result.Success Then
	  Return gm.CommandResult()
	End If
	Dim mesh = gm.Object(0).Mesh()
	If mesh Is Nothing Then
	  Return Result.Failure
	End If

	Dim polylines = mesh.GetNakedEdges()
	For Each polyline In polylines
	  doc.Objects.AddPolyline(polyline)
	Next polyline

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino.Commands import *
from Rhino.Input.Custom import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
    gm = GetObject()
    gm.SetCommandPrompt("Select open mesh")
    gm.GeometryFilter = ObjectType.Mesh
    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
    gm.Get()
    if gm.CommandResult() != Result.Success:
        return gm.CommandResult()
    mesh = gm.Object(0).Mesh()
    if mesh == None:
        return Result.Failure

    polylines = mesh.GetNakedEdges()
    for polyline in polylines:
        doc.Objects.AddPolyline(polyline)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
